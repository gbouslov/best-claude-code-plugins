#!/usr/bin/env python3
"""Offline regression checks for all-or-nothing public metadata updates."""
import json
from pathlib import Path
import re
import tempfile
import unittest

import build_site
import refresh


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.catalog = {'repo': 'owner/list', 'title': 'Useful resources',
                        'publication_status': 'published', 'selection_format': 'linked-h3', 'entries': [
                            {'id': 'first', 'name': 'First', 'url': 'https://github.com/team/first', 'repo': 'team/first'},
                            {'id': 'second', 'name': 'Second', 'url': 'https://github.com/team/second', 'repo': 'team/second'}]}
        (self.root / 'catalog.json').write_text(json.dumps(self.catalog))
        self.original = '# Useful resources\n\nManual review: 2026-10-01.\n\n### [First](https://github.com/team/first)\n\n### [Second](https://github.com/team/second)\n\n' + refresh.START + '\nold\n' + refresh.END + '\n\nKeep this paragraph.\n'
        (self.root / 'README.md').write_text(self.original)
        self.calls = []

    def fetch(self, endpoint):
        self.calls.append(endpoint)
        repo = endpoint.removeprefix('repos/').split('/commits')[0]
        if '/commits?' in endpoint:
            return [{'sha': 'a' * 40, 'commit': {'committer': {'date': '2026-10-27T03:04:05Z'}}}]
        return {'full_name': repo, 'private': False, 'stargazers_count': 1234, 'archived': False}

    def render(self, readme, context):
        self.assertEqual(context, self.catalog['repo'])
        return '<h1>Useful resources</h1><h2>Quick start</h2><a href="#quick-start">Start</a><a href="CONTRIBUTING.md">Contribute</a>' + ''.join(
            '<a href="' + item['url'] + '">' + item['name'] + '</a>' for item in self.catalog['entries'])

    def test_all_sources_and_only_bounded_region_updated(self):
        outcome = refresh.refresh(self.root, self.fetch, '2026-10-28')
        self.assertEqual((outcome['selected_entries'], outcome['repositories']), (2, 2))
        self.assertEqual(len(self.calls), 4)
        actual = (self.root / 'README.md').read_text()
        self.assertEqual(actual.split(refresh.START)[0], self.original.split(refresh.START)[0])
        self.assertEqual(actual.split(refresh.END)[1], self.original.split(refresh.END)[1])
        self.assertIn('1,234', actual)
        self.assertIn('/commit/' + 'a' * 40, actual)
        self.assertNotIn('pushed_at', actual)

    def test_same_day_identical_metadata_is_noop(self):
        refresh.refresh(self.root, self.fetch, '2026-10-28')
        first = (self.root / 'README.md').read_bytes()
        stamp = (self.root / 'README.md').stat().st_mtime_ns
        outcome = refresh.refresh(self.root, self.fetch, '2026-10-28')
        self.assertFalse(outcome['changed'])
        self.assertEqual(first, (self.root / 'README.md').read_bytes())
        self.assertEqual(stamp, (self.root / 'README.md').stat().st_mtime_ns)

    def test_late_failure_preserves_readme_and_checked_date(self):
        def failing(endpoint):
            if endpoint.endswith('second/commits?per_page=1'):
                raise RuntimeError('Fixture API failure')
            return self.fetch(endpoint)
        with self.assertRaises(RuntimeError):
            refresh.refresh(self.root, failing, '2026-10-28')
        self.assertEqual((self.root / 'README.md').read_text(), self.original)

    def test_missing_commit_and_incomplete_repository_fail_closed(self):
        for mutation in ('commit', 'stars', 'private'):
            def broken(endpoint):
                item = self.fetch(endpoint)
                if mutation == 'commit' and isinstance(item, list):
                    return []
                if mutation == 'stars' and isinstance(item, dict):
                    item.pop('stargazers_count')
                if mutation == 'private' and isinstance(item, dict):
                    item['private'] = True
                return item
            with self.assertRaises(ValueError):
                refresh.refresh(self.root, broken, '2026-10-28')
            self.assertEqual((self.root / 'README.md').read_text(), self.original)

    def test_marker_error_performs_no_fetch(self):
        (self.root / 'README.md').write_text('# Missing markers\n')
        with self.assertRaises(ValueError):
            refresh.refresh(self.root, self.fetch, '2026-10-28')
        self.assertEqual(self.calls, [])

    def test_concurrent_manual_edit_is_preserved(self):
        edited = self.original + '\nA contributor added this.\n'
        def concurrent(endpoint):
            (self.root / 'README.md').write_text(edited)
            return self.fetch(endpoint)
        with self.assertRaises(RuntimeError):
            refresh.refresh(self.root, concurrent, '2026-10-28')
        self.assertEqual((self.root / 'README.md').read_text(), edited)

    def test_site_is_deterministic_and_itemlist_matches_selected_visible_urls(self):
        build_site.build(self.root, self.render)
        original = (self.root / 'docs/index.html').read_text()
        self.assertFalse(build_site.build(self.root, self.render)['changed'])
        data = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', original)[1])
        self.assertEqual(data['@type'], 'ItemList')
        self.assertEqual(data['numberOfItems'], 2)
        self.assertEqual([e['url'] for e in data['itemListElement']], [e['url'] for e in self.catalog['entries']])
        self.assertIn('<link rel="canonical" href="https://owner.github.io/list/">', original)
        self.assertIn('https://github.com/owner/list/blob/main/CONTRIBUTING.md', original)
        self.assertIn('id="quick-start"', original)
        self.assertNotIn('FAQPage', original)
        self.assertNotIn('"Question"', original)

    def test_missing_visible_entry_does_not_replace_existing_site(self):
        build_site.build(self.root, self.render)
        original = (self.root / 'docs/index.html').read_bytes()
        with self.assertRaises(ValueError):
            build_site.build(self.root, lambda text, context: '<h1>Incomplete</h1>')
        self.assertEqual((self.root / 'docs/index.html').read_bytes(), original)

    def test_forthcoming_publication_is_visible_and_not_indexable(self):
        self.catalog['publication_status'] = 'forthcoming'
        (self.root / 'catalog.json').write_text(json.dumps(self.catalog))
        build_site.build(self.root, self.render)
        output = (self.root / 'docs/index.html').read_text()
        self.assertIn('Publication status: forthcoming', output)
        self.assertIn('<meta name="robots" content="noindex">', output)

    def test_new_hand_curated_resource_requires_catalog_update(self):
        (self.root / 'README.md').write_text(self.original + '\n### [Third](https://github.com/team/third)\n')
        with self.assertRaises(ValueError):
            refresh.refresh(self.root, self.fetch, '2026-10-28')
        self.assertEqual(self.calls, [])
        with self.assertRaises(ValueError):
            build_site.build(self.root, self.render)

    def test_workflow_stages_only_allowlisted_outputs_and_default_token(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/refresh.yml').read_text()
        stages = re.findall(r'^\s*git add (.+)$', workflow, re.M)
        self.assertEqual(stages, ['-- README.md docs/index.html docs/.nojekyll'])
        self.assertNotIn('secrets.', workflow)
        self.assertIn('GH_TOKEN: ${{ github.token }}', workflow)
        self.assertIn('timeout-minutes: 15', workflow)
        self.assertIn('pages: write', workflow)
        self.assertIn('repos/${GITHUB_REPOSITORY}/pages/builds', workflow)
        self.assertIn("if: steps.commit.outputs.changed == 'true'", workflow)
        self.assertIn('"$publication_status" != "published"', workflow)


if __name__ == '__main__':
    unittest.main()
