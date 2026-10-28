#!/usr/bin/env python3
"""Refresh public source metadata; selection and descriptions remain hand curated."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- freshness:start -->', '<!-- freshness:end -->'
REPO_PATTERN = r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+'


def load_catalog(root):
    catalog = json.loads((root / 'catalog.json').read_text())
    if not re.fullmatch(REPO_PATTERN, catalog.get('repo', '')):
        raise ValueError('Invalid catalog repository')
    if catalog.get('publication_status') not in ('published', 'forthcoming'):
        raise ValueError('Missing publication status')
    if catalog.get('selection_format') not in ('linked-h3', 'linked-first-cell'):
        raise ValueError('Missing selection format')
    if not isinstance(catalog.get('title'), str) or not catalog['title'].strip():
        raise ValueError('Missing title')
    entries = catalog.get('entries')
    if not isinstance(entries, list) or not entries:
        raise ValueError('Empty selection')
    ids, urls = set(), set()
    for entry in entries:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', entry.get('id', '')):
            raise ValueError('Invalid entry id')
        if not re.fullmatch(REPO_PATTERN, entry.get('repo', '')):
            raise ValueError('Invalid source repository')
        if not entry.get('url', '').startswith('https://github.com/' + entry['repo']):
            raise ValueError('Entry URL and repository differ')
        suffix = entry['url'][len('https://github.com/' + entry['repo']):]
        if suffix and not suffix.startswith('/'):
            raise ValueError('Entry URL repository boundary differs')
        if not isinstance(entry.get('name'), str) or not entry['name'].strip() or re.search(r'[\n\r|\[\]<>]', entry['name']):
            raise ValueError('Invalid entry name')
        if entry['id'] in ids or entry['url'] in urls:
            raise ValueError('Duplicate selected entry')
        ids.add(entry['id'])
        urls.add(entry['url'])
    return catalog


def validate_selection(readme, catalog):
    """Validate the hand-curated resources, excluding the generated activity table."""
    source = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', readme, flags=re.S)
    pattern = (r'^### \[[^]]+\]\((https://github\.com/[^)]+)\)\s*$'
               if catalog['selection_format'] == 'linked-h3' else
               r'^\| \[[^]]+\]\((https://github\.com/[^)]+)\) \|')
    visible = re.findall(pattern, source, re.M)
    selected = [entry['url'] for entry in catalog['entries']]
    if len(visible) != len(selected) or set(visible) != set(selected):
        raise ValueError('Hand-curated README resources and catalog differ; update both together')


def gh_json(endpoint):
    result = subprocess.run(['gh', 'api', '--method', 'GET', endpoint],
                            text=True, capture_output=True, timeout=45)
    if result.returncode:
        # Do not echo provider output: supported-client errors can contain account data.
        raise RuntimeError('GitHub request failed for ' + endpoint)
    return json.loads(result.stdout)


def fetch_metadata(repo, fetch=gh_json):
    info = fetch('repos/' + repo)
    commits = fetch('repos/' + repo + '/commits?per_page=1')
    if (not isinstance(info, dict) or info.get('private') is not False
            or info.get('full_name', '').lower() != repo.lower()
            or type(info.get('stargazers_count')) is not int
            or info['stargazers_count'] < 0 or type(info.get('archived')) is not bool):
        raise ValueError('Incomplete public repository metadata: ' + repo)
    if not isinstance(commits, list) or not commits:
        raise ValueError('Missing actual commit: ' + repo)
    sha = commits[0].get('sha', '')
    date = commits[0].get('commit', {}).get('committer', {}).get('date', '')
    if not re.fullmatch(r'[a-f0-9]{40}', sha):
        raise ValueError('Missing commit SHA: ' + repo)
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', date):
        raise ValueError('Missing commit date: ' + repo)
    dt.datetime.fromisoformat(date.replace('Z', '+00:00'))
    return {'stars': info['stargazers_count'], 'archived': info['archived'], 'sha': sha, 'date': date}


def block(catalog, metadata, checked):
    lines = [START, '', '## Repository activity', '',
             'Repository metadata checked **' + checked + ' (UTC)**. Stars, latest default-branch commit and archive status describe each source repository, including shared repositories; they do not measure an individual plugin or skill release. Selection and installation guidance are reviewed separately.', '',
             '| Selected resource | Repository stars | Latest repository commit (UTC) | Archived |',
             '|---|---:|---|---|']
    for entry in catalog['entries']:
        item = metadata[entry['repo']]
        commit_url = 'https://github.com/' + entry['repo'] + '/commit/' + item['sha']
        lines.append('| [' + entry['name'] + '](' + entry['url'] + ') | '
                     + format(item['stars'], ',') + ' | [' + item['date'][:10]
                     + '](' + commit_url + ') | ' + ('Yes' if item['archived'] else 'No') + ' |')
    return '\n'.join(lines + ['', END])


def atomic_write(path, value):
    if path.exists() and path.read_text() == value:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.' + path.name + '-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as handle:
            handle.write(value)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return True


def refresh(root=ROOT, fetch=gh_json, checked=None):
    catalog = load_catalog(root)
    path = root / 'README.md'
    original = path.read_text()
    if original.count(START) != 1 or original.count(END) != 1 or original.index(START) > original.index(END):
        raise ValueError('Exactly one ordered freshness marker pair is required')
    validate_selection(original, catalog)
    metadata = {repo: fetch_metadata(repo, fetch) for repo in dict.fromkeys(e['repo'] for e in catalog['entries'])}
    checked = checked or dt.datetime.now(dt.timezone.utc).date().isoformat()
    dt.date.fromisoformat(checked)
    before, tail = original.split(START)
    _, after = tail.split(END)
    updated = before + block(catalog, metadata, checked) + after
    if path.read_text() != original:
        raise RuntimeError('README changed during metadata retrieval; retry from the new source')
    changed = atomic_write(path, updated)
    return {'selected_entries': len(catalog['entries']), 'repositories': len(metadata), 'changed': changed, 'checked': checked}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(json.dumps(refresh(args.root)))
    except (ValueError, KeyError, TypeError, RuntimeError, OSError, subprocess.SubprocessError) as error:
        raise SystemExit('Refresh failed; README was not updated: ' + str(error))
