# Contribute a useful Claude Code plugin

Suggest an addition or correction through an issue or pull request. Describe the developer job it helps with and how it differs from an entry already listed.

When adding or removing a selected entry, update both `README.md` and `catalog.json`. Their selected URLs must agree so the nightly table and Pages ItemList cover exactly the visible selection. Run `python3 -B scripts/test_refresh.py` to check the update rules.

For an addition, include:

1. The primary repository, its plugin manifest and the exact marketplace entry used to install it.
2. A specific “use it when,” plus the skills, agents, commands, hooks and servers it adds.
3. A working upstream installation guide, required runtimes/accounts and material service costs.
4. The source repository's latest commit date, archived status and applicable license. Check the actual plugin directory in a shared repository.
5. Any important data access, background process, automatic action or overlapping tool a developer should understand before installation.

This list selects plugins, not standalone skills, command snippets, marketplaces or unrelated CLI tools. A plugin can legitimately use a marketplace-defined manifest; identify that packaging explicitly rather than inventing a plugin.json file. Prefer a focused maintained entry over several near-duplicates.

Keep descriptions factual and brief. Link to upstream code and documentation rather than copying their contents. State whether you reviewed sources, actually installed a plugin or measured a result. Repository activity and popularity do not establish safety or effectiveness.

For a correction, identify the affected entry and link the upstream change. Do not include credentials, private project records, personal data or session contents.

Repository stars, latest commit and archived status refresh nightly. The maintainer reviews source content and installation routes monthly and after reported upstream changes. Automated metadata dates and manual review dates are distinct. Contributions to the list's original text use its MIT license; linked plugins retain their own terms.

## Featured in this list

If your project is listed, you may add this optional badge to your README. It links readers to the comparison and does not imply endorsement by your project or a security certification.

```markdown
[![Featured in Best Claude Code Plugins](https://img.shields.io/badge/Featured%20in-Best%20Claude%20Code%20Plugins-blue)](https://github.com/gbouslov/best-claude-code-plugins)
```
