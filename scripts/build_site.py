#!/usr/bin/env python3
"""Build a deterministic GitHub-style page from this repository's README."""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin

from refresh import ROOT, atomic_write, load_catalog, validate_selection

# Reused from the approved GitHub Markdown preview; tables scroll within the page.
CSS = '''body{margin:0;color:#1f2328;background:#fff;font:16px/1.55 -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}.markdown-body{box-sizing:border-box;max-width:1012px;margin:auto;padding:32px}h1,h2{line-height:1.25;border-bottom:1px solid #d1d9e0;padding-bottom:.3em}h1{font-size:32px}h2{font-size:24px;margin-top:32px}h3{font-size:20px;margin-top:28px}a{color:#0969da;text-decoration:none;overflow-wrap:anywhere}code,pre{background:#f6f8fa;border-radius:4px}pre{padding:16px;overflow:auto}code{font-size:85%}p code,li code,td code{overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:6px 13px;border:1px solid #d1d9e0;text-align:left;vertical-align:top}tr:nth-child(even){background:#f6f8fa}.table-wrap,markdown-accessiblity-table{display:block;overflow-x:auto;max-width:100%}section{display:flow-root}nav{margin-bottom:24px;font-size:14px}@media(max-width:600px){.markdown-body{padding:16px}table{min-width:620px}h1{font-size:28px}}'''


def github_markdown(readme, repo):
    payload = json.dumps({'text': readme, 'mode': 'gfm', 'context': repo})
    result = subprocess.run(['gh', 'api', 'markdown', '--method', 'POST', '--input', '-'],
                            input=payload, text=True, capture_output=True, timeout=60)
    if result.returncode:
        raise RuntimeError('GitHub Markdown rendering failed')
    return result.stdout


class VisibleLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'a' and attributes.get('href'):
            self.links.add(attributes['href'])


def prepare_fragment(fragment, repo):
    # Relative document and image links should open the source on GitHub, not a
    # missing file under /docs. In-page anchors stay on this rendered README.
    def link(match):
        prefix, value = match.groups()
        raw = html.unescape(value)
        if raw.startswith(('#', 'https://', 'http://', 'mailto:', 'data:')):
            return match[0]
        absolute = urljoin('https://github.com/' + repo + '/blob/main/', raw)
        return prefix + '"' + html.escape(absolute, quote=True) + '"'
    fragment = re.sub(r'((?:href|src)=)"([^\"]*)"', link, fragment)
    # GitHub may emit its own user-content anchors. Preserve those and provide
    # the readable heading IDs used by this README's table of contents.
    used = set()
    def heading(match):
        level, attributes, content = match.groups()
        text = html.unescape(re.sub('<[^>]*>', '', content)).strip().lower()
        slug = re.sub(r'[^\w -]', '', text).replace(' ', '-')
        candidate, number = slug, 0
        while candidate in used:
            number += 1
            candidate = slug + '-' + str(number)
        used.add(candidate)
        if re.search(r'\bid=', attributes):
            return match[0]
        return '<h' + level + attributes + ' id="' + candidate + '">' + content + '</h' + level + '>'
    fragment = re.sub(r'<h([1-6])([^>]*)>(.*?)</h\1>', heading, fragment, flags=re.S)
    return re.sub(r'(<table\b.*?</table>)', r'<div class="table-wrap">\1</div>', fragment, flags=re.S)


def build(root=ROOT, render=github_markdown):
    catalog = load_catalog(root)
    readme = (root / 'README.md').read_text()
    validate_selection(readme, catalog)
    fragment = render(readme, catalog['repo'])
    if not fragment.strip() or '<h1' not in fragment:
        raise ValueError('README rendering is empty or missing its title')
    links = VisibleLinks()
    links.feed(fragment)
    missing = [entry['id'] for entry in catalog['entries'] if entry['url'] not in links.links]
    if missing:
        raise ValueError('Selected URLs missing from visible README: ' + ', '.join(missing))
    body = prepare_fragment(fragment, catalog['repo'])
    owner, slug = catalog['repo'].split('/')
    canonical = 'https://' + owner.lower() + '.github.io/' + slug + '/'
    structured = {'@context': 'https://schema.org', '@type': 'ItemList',
                  'name': catalog['title'], 'url': canonical,
                  'numberOfItems': len(catalog['entries']),
                  'itemListElement': [{'@type': 'ListItem', 'position': i,
                                       'name': entry['name'], 'url': entry['url']}
                                      for i, entry in enumerate(catalog['entries'], 1)]}
    # This is deliberately the only structured-data type emitted. FAQ remains
    # ordinary visible prose in the README.
    data = json.dumps(structured, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    forthcoming = catalog['publication_status'] == 'forthcoming'
    nav = ('Publication status: forthcoming. This list is prepared for publication.' if forthcoming else
           '<a href="https://github.com/' + catalog['repo'] + '">View this list on GitHub</a>')
    robots = '<meta name="robots" content="noindex">' if forthcoming else ''
    output = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
              '<meta name="viewport" content="width=device-width,initial-scale=1">'
              '<title>' + html.escape(catalog['title']) + '</title>'
              '<link rel="canonical" href="' + canonical + '">' + robots
              + '<style>' + CSS + '</style><script type="application/ld+json">' + data
              + '</script></head><body><main class="markdown-body"><nav>' + nav
              + '</nav>' + body + '</main></body></html>\n')
    changed = atomic_write(root / 'docs/index.html', output)
    atomic_write(root / 'docs/.nojekyll', '')
    return {'selected_entries': len(catalog['entries']), 'canonical': canonical,
            'publication_status': catalog['publication_status'], 'changed': changed}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root)))
    except (ValueError, KeyError, TypeError, RuntimeError, OSError, subprocess.SubprocessError) as error:
        raise SystemExit('Build failed; page was not updated: ' + str(error))
