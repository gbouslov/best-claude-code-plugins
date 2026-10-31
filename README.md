# Best Claude Code Plugins (2026): Choose by the Job

An awesome Claude Code plugins list and directory of 34 selected packages for building features, reviewing code, testing in a browser, connecting services and keeping context across sessions. Compare what each plugin installs, the setup it needs and its source repository's latest commit before adding it to your project.

**Start with your next task.** For a new feature, choose Feature Dev; for current library documentation, Context7; for browser checks, Playwright. Add a service plugin when the task needs that service. You do not need the whole list.

Plugin manifests and installation routes reviewed **28 October 2026**. Each detailed entry's version and “Latest repository commit” line is a snapshot from that manual review, including shared repositories; these are not dates of individual plugin releases. For current stars, commit dates and archived status, use the [nightly activity table](#repository-activity). Installation commands and contents were checked against the marketplace, including its pinned source versions.

## Choose a plugin in one minute

On a phone, scroll the table sideways to see every column.

| Your next job | Start here | What changes in your setup |
|---|---|---|
| Build a feature in an unfamiliar codebase | [Feature Dev](#feature-dev) | A guided command plus exploration, architecture and review agents. |
| Follow a development process across tasks | [Superpowers](#superpowers) | Skills for planning, tests, debugging and verification, with a session hook. |
| Review a GitHub pull request | [Code Review](#code-review) | A PR-review command using GitHub CLI; posting is a separate option. |
| Inspect tests, errors and types before merging | [PR Review Toolkit](#pr-review-toolkit) | Six specialized reviewers you can call for different concerns. |
| Look up a library's current API | [Context7](#context7) | A hosted documentation MCP connection; no local Node process. |
| Navigate or refactor an existing codebase | [Serena](#serena) | A local semantic-code MCP server backed by language tooling. |
| Check a user journey in a real browser | [Playwright](#playwright) | A browser-control MCP server launched through npm tooling. |
| Debug a production exception | [Sentry](#sentry) | Sentry debugging skills and a connection to your monitoring data. |
| Work on a Supabase backend | [Supabase](#supabase) | Database/platform skills plus an authenticated Supabase MCP connection. |
| Keep a long-running project's plan on disk | [Planning with Files](#planning-with-files) | Planning skills, commands and lifecycle hooks. |
| Search useful context from past sessions | [Claude-Mem](#claude-mem) | Session capture, a local worker and searchable persistent memory. |
| See context and tool activity while working | [Claude HUD](#claude-hud) | Setup commands for a terminal status line. |

Browse: [by job](#best-claude-code-plugins-for-web-development) · [marketplaces](#official-and-community-marketplaces) · [install](#install-and-manage) · [build](#build-plan-and-refine-code) · [review](#review-code-and-find-security-issues) · [docs and testing](#look-up-code-and-test-the-result) · [services](#connect-your-development-services) · [memory](#manage-context-and-session-memory) · [terminal](#see-whats-happening-and-learn) · [customize](#build-your-own-claude-code-setup) · [FAQ](#frequently-asked-questions).

## Best Claude Code plugins for web development

Start with [Feature Dev](#feature-dev) for a feature in an existing application, [Context7](#context7) for library APIs and [Playwright](#playwright) for the running browser journey. Add [Supabase](#supabase), [Firebase](#firebase), [Stripe](#stripe) or [Vercel](#vercel) when that service is part of the job.

For a frontend change, the useful sequence is concrete: understand the component, check the relevant library API, implement it, and check the result in a browser. Add the plugin covering the step your current setup is missing.

## Best Claude Code plugins for frontend design or website design

Use [Figma](#figma) when you have a design file to implement: it connects Claude to design context and component mappings. Use [Playwright](#playwright) to inspect the implemented page and its interactions, then [Code Simplifier](#code-simplifier) for focused cleanup. Bring the actual design, content and acceptance criteria to the task.

Figma access and browser testing solve different problems. Choose the design connection for source designs and the browser connection for the page people will use.

## Best Claude Code plugins for mobile app development

For app development, [Superpowers](#superpowers) supplies planning, debugging and verification workflows, while [Context7](#context7) helps with framework documentation. [Firebase](#firebase), [Supabase](#supabase) and [Sentry](#sentry) fit the backend and production-error parts of a mobile app when you already use those services.

Use your platform's simulator, device and build tools to verify native behavior. Playwright fits web pages and mobile web journeys. For Expo, React Native, Flutter or iOS-specific workflows, the companion [Best Claude Code Skills](https://github.com/gbouslov/best-claude-code-skills) list is forthcoming and covers those specialist collections.

## Best Claude Code plugins for developers

Pick the missing development step: [Serena](#serena) for symbols and references, [Code Review](#code-review) for a GitHub pull request, [PR Review Toolkit](#pr-review-toolkit) for selected review concerns, and [Commit Commands](#commit-commands) for explicit Git commit and PR commands. [GitHub](#github), [GitLab](#gitlab), [Linear](#linear) and [Atlassian](#atlassian) connect the service where the work is tracked.

For a developer building an agent application itself, [Agent SDK Dev](#agent-sdk-dev) targets Python and TypeScript SDK projects. The [overlap table](#compare-plugins-that-seem-to-overlap) helps avoid adding two packages for the same step.

## Best Claude Code plugins to save tokens or reduce token usage

Start by checking the cost of your current setup. Run `claude plugin details <name>` in a terminal for an installed plugin's footprint, and inspect `/context` inside Claude Code. Disable unused plugins before adding another context tool. [Official plugin overview](https://code.claude.com/docs/en/plugins/overview#what-an-enabled-plugin-adds-to-your-sessions).

[Context Mode](#context-mode) indexes large tool outputs so selected results can return to the conversation. [Claude HUD](#claude-hud) makes usage visible; [Planning with Files](#planning-with-files) preserves an explicit plan. Compare them on the same task and include extra model calls and background processing in the cost. No percentage saving is assumed here.

## Official and community marketplaces

Anthropic's [official marketplace](https://github.com/anthropics/claude-plugins-official) is the install source for 30 entries here, including external publishers distributed through that catalog. An official listing identifies the distribution channel; upstream ownership and licenses still differ. Anthropic also maintains a [community marketplace](https://github.com/anthropics/claude-code), distinct from its official catalog. See [Anthropic's marketplace guide](https://code.claude.com/docs/en/plugins/anthropic-marketplaces).

Four entries here use their own community marketplaces: [Planning with Files](https://github.com/OthmanAdi/planning-with-files), [Context Mode](https://github.com/mksglu/context-mode), [Claude-Mem](https://github.com/thedotmack/claude-mem) and [Claude HUD](https://github.com/jarrodwatts/claude-hud). Each entry includes the registration and installation commands. For broader discovery, [Awesome Claude Plugins](https://github.com/Chat2AnyLLM/awesome-claude-plugins) catalogs marketplaces; this page selects individual developer plugins.

## Plugins and skills, compared

A **skill** is reusable task guidance in a folder containing `SKILL.md`. A **plugin** is an installable package that can include skills, agents, hooks and MCP connections; an **MCP server** supplies tools or data access. Choose a skill for a focused workflow, a plugin for a packaged setup, and a server when you need a connection. [Official component overview](https://code.claude.com/docs/en/plugins/overview).

For example, Supabase's plugin combines guidance with a live service connection; a skills-only installation can supply SQL guidance without that connection. The forthcoming [Best Claude Code Skills](https://github.com/gbouslov/best-claude-code-skills) companion covers document, web, mobile, security and research skills. A skill's portability does not automatically carry a plugin's hooks or server configuration to another agent.

## Install and manage

The fenced `sh` commands on this page run in your **terminal**. Commands beginning with `/`, such as `/reload-plugins`, run **inside Claude Code**.

Register Anthropic's marketplace once if it is not already available:

```sh
claude plugin marketplace add anthropics/claude-plugins-official
```

The install commands below use `--scope local`: enable the plugin for you in the current repository. Use `--scope user` for all your projects, or `--scope project` for a shared repository setup. Community entries include their own marketplace registration command. A marketplace's registered name can differ from its GitHub repository name.

After installing, run `/reload-plugins` if Claude Code requests it, or start a new session. Check the Installed tab in `/plugin` and use `/mcp` for bundled server connection status. Some entries need a sign-in, runtime or one-time setup before their tools work. [Official installation and scope guide](https://code.claude.com/docs/en/discover-plugins).

To list installed plugins and registered marketplaces, run these in your terminal:

```sh
claude plugin list
claude plugin marketplace list
```

To browse available plugins, open `/plugin` inside Claude Code and choose Discover. Your installed list and the available marketplace catalog serve different purposes.

To manage one package, use its qualified name and intended scope:

```sh
claude plugin update feature-dev@claude-plugins-official
claude plugin disable feature-dev@claude-plugins-official --scope local
claude plugin enable feature-dev@claude-plugins-official --scope local
claude plugin uninstall feature-dev@claude-plugins-official --scope local
```

The [plugin commands reference](https://code.claude.com/docs/en/plugins/cli-reference) explains scope defaults and flags. See the FAQ for updating a whole marketplace's installed plugins.

## Troubleshooting GitHub plugin auth and setup

First identify which connection failed: **downloading a marketplace from GitHub**, **connecting the GitHub MCP service**, or **running a command that uses GitHub CLI**. Their credentials and failure messages can differ.

1. For a marketplace clone error, confirm the `owner/repo` exists and you can access it. `git ls-remote <repository-url>` checks Git access; a private repository requires non-interactive authentication. GitHub CLI users can configure Git with `gh auth login` followed by `gh auth setup-git`. See the [official authentication troubleshooting steps](https://code.claude.com/docs/en/plugins/troubleshooting#ssh-authentication-failed-or-https-authentication-failed).
2. For the listed [GitHub plugin](#github), inspect `/mcp` inside Claude Code. Its checked wrapper expects the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable; a successful marketplace download does not configure this server. Follow [GitHub MCP authentication](https://github.com/github/github-mcp-server#remote-github-mcp-server) for your host and account.
3. For Code Review or Commit Commands, check `gh auth status` in the terminal and the repository access the command requires. If a newly installed plugin is missing, inspect the Errors tab of `/plugin`, check the marketplace name and run `/reload-plugins`. [Plugin troubleshooting](https://code.claude.com/docs/en/plugins/troubleshooting).

Keep credential values out of issue reports. Share the command, error text with secrets removed, Claude Code version, and whether the failure is in cloning, loading or connecting a server.

## Build, plan and refine code

### [Feature Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/feature-dev)

**Use it when:** you need to understand an existing application before implementing a substantial feature.

**Adds:** the `feature-dev` command and three agents for exploration, architecture and code review. **Setup:** a code repository; the workflow uses multiple agent calls. Start with `/feature-dev:feature-dev` and describe the feature.

```sh
claude plugin install feature-dev@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Superpowers](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3)

**Use it when:** you want a repeatable process for requirements, implementation plans, tests and debugging across development tasks.

**Adds:** development workflow skills and a SessionStart hook that introduces the workflow. **Setup:** your project's normal development tools. It overlaps with Feature Dev; choose one starting workflow before combining them.

```sh
claude plugin install superpowers@claude-plugins-official --scope local
```

Marketplace bundle: **7.0.0**. Latest repository commit: **2026-10-21**.

### [Planning with Files](https://github.com/OthmanAdi/planning-with-files)

**Use it when:** a multi-session task needs a durable plan, findings and progress that you can inspect in your repository.

**Adds:** planning skills, commands and lifecycle hooks that restore selected planning context. **Setup:** the documented shell/Python helpers for your platform. Its optional completion gate changes when the agent can stop; use the ordinary planning mode first. This stores plans; it does a different job from Claude-Mem's session capture.

```sh
claude plugin marketplace add OthmanAdi/planning-with-files
claude plugin install planning-with-files@planning-with-files --scope local
```

Latest repository commit: **2026-10-28**.

### [Code Simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier)

**Use it when:** a recent change works but needs clearer structure and less unnecessary complexity.

**Adds:** a code-simplification agent. **Setup:** the changed code and your project's tests. Ask for simplification of the recent diff; run the tests afterward. Choose this focused agent instead of a full review workflow for a small cleanup.

```sh
claude plugin install code-simplifier@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Agent SDK Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev)

**Use it when:** you are creating an application with the Claude Agent SDK in Python or TypeScript.

**Adds:** a `new-sdk-app` command and separate Python/TypeScript verification agents. **Setup:** the chosen language runtime, SDK dependencies and model access for the application. This targets an SDK application rather than general feature development.

```sh
claude plugin install agent-sdk-dev@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Ralph Loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop)

**Use it when:** a bounded implementation task has an explicit completion condition and benefits from repeated attempts.

**Adds:** loop, cancel and help commands plus a Stop hook that continues the task. **Setup:** Bash and the documented platform helpers. Set `--max-iterations` on the loop command: its default is unlimited, and each iteration consumes model usage. Use `/ralph-loop:cancel-ralph` to cancel.

```sh
claude plugin install ralph-loop@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

## Review code and find security issues

### [Code Review](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review)

**Use it when:** you want a review of a specific GitHub pull request, with candidate issues checked before reporting.

**Adds:** a PR-review command that coordinates multiple review agents. **Setup:** GitHub CLI (`gh`), authenticated repository access and a pull request. The checked command keeps findings in the session unless you supply `--comment`; that option can post to GitHub.

```sh
claude plugin install code-review@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [PR Review Toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit)

**Use it when:** you need separate opinions on test coverage, error handling, comments, type design or code quality.

**Adds:** the `review-pr` command and six specialized agents, including a silent-failure hunter and code simplifier. **Setup:** the changes to review and relevant project tools. Choose it over Code Review when you want to direct particular review lenses rather than one GitHub PR routine.

```sh
claude plugin install pr-review-toolkit@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Security Guidance](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance)

**Use it when:** you want security feedback during edits and at the end of a turn or before a commit.

**Adds:** lifecycle hooks for pattern warnings, model-based diff review and agentic commit review. **Setup:** Claude Code 2.1.144+, Python 3.8+ and supported model authentication; gateway sign-in requires 2.1.195+. Reviews consume additional model usage and default to Opus. The review sends code/diffs through the configured model route; check that route for the repository you are working in.

```sh
claude plugin install security-guidance@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Semgrep Guardian](https://github.com/semgrep/guardian/tree/b58f407c6ac0f5fe47dee8301602f2e290a8ecfb/plugin)

**Use it when:** you want Semgrep findings on code the agent writes, with tools for investigating and fixing them.

**Adds:** a local Guardian MCP process, lifecycle hooks and supporting skills. **Setup:** Semgrep onboarding/sign-in through the plugin. Guardian sends edited files, their previous contents and dependency manifests to Semgrep's scanner; it also downloads its runtime and can update itself. Review the upstream data-handling and telemetry controls for private code.

```sh
claude plugin install semgrep@claude-plugins-official --scope local
```

Marketplace bundle: **2.7.0**. Latest repository commit: **2026-10-22**.

## Look up code and test the result

### [Context7](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7)

**Use it when:** you need documentation or examples for the particular version of a library you are using.

**Adds:** a hosted MCP connection for resolving libraries and querying their documentation. **Setup:** network access to Context7; the checked bundle does not launch a local npm server. Anonymous access has shared limits; upstream documents an optional API key for higher limits. Match the returned version to your project.

```sh
claude plugin install context7@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Serena](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/serena)

**Use it when:** understanding symbols and their references will help you navigate or change a large existing codebase.

**Adds:** a local Serena MCP server launched with `uvx`. **Setup:** `uv`/`uvx` and language tooling supported by [Serena](https://github.com/oraios/serena). It provides semantic code tools; it does a different job from Context7's external library documentation. The checked launcher retrieves Serena from its Git repository.

```sh
claude plugin install serena@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27** (plugin wrapper repository).

### [Playwright](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/playwright)

**Use it when:** Claude needs to navigate your running application, inspect a page or reproduce a browser interaction.

**Adds:** Microsoft's Playwright MCP server, launched through `npx`. **Setup:** Node/npm, browser dependencies and a reachable application. Follow [Playwright MCP's browser setup](https://github.com/microsoft/playwright-mcp); the plugin registers a server, not a ready-made test suite. Browser actions can submit forms and use signed-in sessions.

```sh
claude plugin install playwright@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27** (plugin wrapper repository).

## Connect your development services

### [GitHub](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/github)

**Use it when:** your task spans repository search, issues and pull requests in GitHub.

**Adds:** a hosted GitHub MCP connection. **Setup:** the checked wrapper expects `GITHUB_PERSONAL_ACCESS_TOKEN`; use the permissions your task requires. Pair it with Code Review when you also want a review process. Check existing GitHub connections before adding another copy of the same tools.

```sh
claude plugin install github@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [GitLab](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/gitlab)

**Use it when:** your repository, merge requests and CI/CD work live in GitLab.

**Adds:** a hosted MCP connection to GitLab's API endpoint. **Setup:** supported GitLab access and authentication. The checked endpoint is GitLab.com; check GitLab's deployment-specific instructions before using a self-managed instance. Tool access follows the connected account's permissions.

```sh
claude plugin install gitlab@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Commit Commands](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/commit-commands)

**Use it when:** you want explicit commands for the commit-to-pull-request part of development.

**Adds:** `commit`, `commit-push-pr` and `clean_gone` commands. **Setup:** Git, plus authenticated GitHub CLI for PR creation. Choose the command deliberately: `commit-push-pr` can push and open a PR; `clean_gone` removes local branches and associated worktrees whose remotes are gone.

```sh
claude plugin install commit-commands@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Linear](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/linear)

**Use it when:** you need issue, project and status context from a Linear workspace while coding.

**Adds:** a hosted Linear MCP connection. **Setup:** authenticate to the intended Linear workspace. The tools include writes such as issue creation and status changes, so distinguish looking up a ticket from updating it.

```sh
claude plugin install linear@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Atlassian](https://github.com/atlassian/atlassian-mcp-server/tree/b74220d41142fae52b4f680c805b2ab81050991a)

**Use it when:** the feature's requirements are in Confluence and the delivery work is tracked in Jira.

**Adds:** Atlassian's hosted MCP connection and skills for knowledge search, issue triage, status reports and turning specifications into backlog work. **Setup:** access to the relevant Atlassian sites and their authorization flow. Choose it for the Jira/Confluence workflow rather than adding several unrelated ticket tools.

```sh
claude plugin install atlassian@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-07**.

### [Sentry](https://github.com/getsentry/plugin-claude/tree/73e53541d7af21672e27428c7067f4264b8a3d65)

**Use it when:** a production exception needs error context, stack-trace investigation or monitoring changes.

**Adds:** Sentry skills for instrumentation/debugging and a hosted Sentry MCP connection. **Setup:** authorize access to the intended Sentry organization. Error events can include application and user data. This repository is generated from Sentry's upstream skill library; contribute fixes to the source linked in its README.

```sh
claude plugin install sentry@claude-plugins-official --scope local
```

Marketplace bundle: **1.4.0**. Latest repository commit: **2026-10-22**.

### [Supabase](https://github.com/supabase-community/supabase-plugin/tree/2c6d02d4565babe784103ee4d446a93ae9b24151)

**Use it when:** you need both Supabase product guidance and live access to projects, databases or Edge Functions.

**Adds:** the `supabase` and `supabase-postgres-best-practices` skills plus a hosted Supabase MCP connection. **Setup:** browser authorization to your Supabase account. If you only want SQL advice, a skills-only install is a smaller option. The upstream guide explains removing a manually added duplicate MCP connection.

```sh
claude plugin install supabase@claude-plugins-official --scope local
```

Marketplace bundle: **0.1.16**. Latest repository commit: **2026-10-16**.

### [Firebase](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/firebase)

**Use it when:** you are building or operating a Firebase-backed application.

**Adds:** a Firebase MCP server launched through `firebase-tools` with `npx`. **Setup:** Node/npm and Firebase CLI authentication/project access; follow [Firebase's MCP guide](https://firebase.google.com/docs/ai-assistance/mcp-server). Service operations can change deployed resources and consume service quotas.

```sh
claude plugin install firebase@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27** (plugin wrapper repository).

### [Stripe](https://github.com/stripe/ai/tree/deae744bc0cbf6034b4b6f22f51c690b71a4e779/providers/claude/plugin)

**Use it when:** you need Stripe integration guidance alongside tools for the Stripe account you are developing against.

**Adds:** Stripe skills, commands, an agent, lifecycle hooks and a hosted Stripe MCP connection. **Setup:** Stripe authorization; local hooks use Node. Check test versus live mode before account actions. Installing this plugin does not create a sandbox account or make a live payment safe to try.

```sh
claude plugin install stripe@claude-plugins-official --scope local
```

Marketplace bundle: **0.11.17**. Latest repository commit: **2026-10-28**.

### [Vercel](https://github.com/vercel/vercel-plugin/tree/882e66c2698689324c341b7bb8fd8beb92c27bf6)

**Use it when:** you need to build, inspect or deploy an application using Vercel's platform.

**Adds:** platform skills, commands, agents, lifecycle hooks and a hosted Vercel MCP connection. **Setup:** Node for the hooks and OAuth for the intended Vercel team. The checked marketplace bundle describes its MCP connection as read-only for docs, projects, deployments and logs. Its separate deployment command can use deployment tooling; check team access and plan limits before running it.

```sh
claude plugin install vercel@claude-plugins-official --scope local
```

Marketplace bundle: **0.50.0**. Latest repository commit: **2026-10-26**.

### [Figma](https://github.com/figma/mcp-server-guide/tree/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5)

**Use it when:** implementation needs design context, component mappings or another workflow in a Figma file.

**Adds:** Figma workflow skills and a hosted Figma MCP connection. **Setup:** Figma authorization and access to the source file; available features and limits depend on your account. Unlike a general UI-writing skill, this connects the task to actual designs and component information.

```sh
claude plugin install figma@claude-plugins-official --scope local
```

Marketplace bundle: **2.2.157**. Latest repository commit: **2026-10-28**.

## Manage context and session memory

### [Context Mode](https://github.com/mksglu/context-mode)

**Use it when:** large tool outputs are filling the context window and you need to index/search them before returning selected results to Claude.

**Adds:** a local MCP server, skills and lifecycle hooks for tool routing and session continuity. **Setup:** Node.js 22.5+ or the upstream-supported Bun setup; run `/context-mode:ctx-doctor` after reloading. It changes tool routing and stores indexed content. Its Elastic License 2.0 is source-available, with managed-service restrictions. Evaluate it on your workload; no percentage saving is assumed here.

```sh
claude plugin marketplace add mksglu/context-mode
claude plugin install context-mode@context-mode --scope local
```

Latest repository commit: **2026-10-28**.

### [Claude-Mem](https://github.com/thedotmack/claude-mem/tree/main/plugin)

**Use it when:** later sessions need to retrieve useful observations from previous development work.

**Adds:** memory/search skills, session lifecycle hooks, a local worker and an MCP search connection. **Setup:** Node.js 20+, with Bun/uv dependencies that upstream can install automatically. Session observations persist on disk, and compression uses a model; review retention and provider settings for sensitive work. Use the Code plugin below; the repository also distributes a separate Cowork plugin.

```sh
claude plugin marketplace add thedotmack/claude-mem
claude plugin install claude-mem@thedotmack --scope local
```

Latest repository commit: **2026-10-28**.

## See what's happening and learn

### [Claude HUD](https://github.com/jarrodwatts/claude-hud)

**Use it when:** you want context usage, tool activity, agents and task progress visible below your terminal input.

**Adds:** setup/configuration commands and the status-line implementation. **Setup:** Node.js 18+ or Bun on macOS/Linux; Node.js 18+ on Windows. After reloading, run `/claude-hud:setup` inside Claude Code. That configures a status line; review an existing custom status line before replacing it.

```sh
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud@claude-hud --scope local
```

Latest repository commit: **2026-10-26**.

### [Explanatory Output Style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/explanatory-output-style)

**Use it when:** understanding the reason for an implementation decision matters alongside the code change.

**Adds:** a SessionStart hook with instructions to explain codebase patterns and choices. **Setup:** no external service. The extra instructions and explanations consume tokens; enable it for work where those explanations help.

```sh
claude plugin install explanatory-output-style@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Learning Output Style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/learning-output-style)

**Use it when:** you want to participate in writing meaningful parts of the code while Claude guides the work.

**Adds:** a SessionStart hook combining explanations with prompts for your contribution. **Setup:** no external service. It already includes explanatory behavior, so start with Learning alone if you want both. Expect a more interactive session and additional token use.

```sh
claude plugin install learning-output-style@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

## Build your own Claude Code setup

### [Claude Code Setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup)

**Use it when:** you want suggestions for which automations fit the repository you actually have.

**Adds:** a codebase-analysis skill that recommends hooks, skills, MCP servers, agents and commands. **Setup:** an accessible codebase. The recommender is read-only: it proposes a setup; it does not install those recommendations for you.

```sh
claude plugin install claude-code-setup@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [CLAUDE.md Management](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management)

**Use it when:** the repository instructions have drifted from the code or a session revealed something worth preserving.

**Adds:** an instruction-file audit skill and a `revise-claude-md` command. **Setup:** your repository's instruction files. Review suggested changes before sharing them: these files shape future sessions for everyone who reads them.

```sh
claude plugin install claude-md-management@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Hookify](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify)

**Use it when:** a recurring unwanted action should trigger a warning or block based on a rule you can inspect.

**Adds:** rule-writing guidance, commands, a conversation-analysis agent and Python lifecycle hooks. **Setup:** Python 3.7+. Rules are Markdown files with event/pattern settings. Test the exact behavior you intend to prevent; a rule existing on disk does not show that it caught the event.

```sh
claude plugin install hookify@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Plugin Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev)

**Use it when:** you want to package skills, commands, agents or tools as your own Claude Code plugin.

**Adds:** seven plugin-development skills, a `create-plugin` command and three agents for authoring and validation. **Setup:** the runtimes your plugin will use. It helps build a plugin; publishing that plugin and granting it access remain separate actions.

```sh
claude plugin install plugin-dev@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

### [Skill Creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator)

**Use it when:** you need to create or improve a reusable skill and evaluate its behavior on example tasks.

**Adds:** the skill-creation workflow, evaluation helpers and reference material as an installable plugin. **Setup:** tools and model access for the evaluations you choose to run. Use Plugin Dev when you need the surrounding distribution package; choose Skill Creator for the skill's content and behavior.

```sh
claude plugin install skill-creator@claude-plugins-official --scope local
```

Latest repository commit: **2026-10-27**.

## Compare plugins that seem to overlap

On a phone, scroll the table sideways to see every column.

| Choice | The useful distinction | Start with |
|---|---|---|
| Feature Dev / Superpowers / Planning with Files | Feature Dev guides one feature; Superpowers supplies a development process; Planning with Files persists plans and progress. | The one matching your immediate problem; avoid stacking three workflow systems at once. |
| Code Review / PR Review Toolkit / Code Simplifier | One GitHub PR routine; specialized review lenses; focused cleanup of recent code. | Code Review for a GitHub PR, Toolkit for targeted checks, Simplifier for cleanup. |
| Context7 / Serena / Playwright | External library docs; symbols in your codebase; behavior in a running browser. | The missing information: API, code structure or actual page behavior. |
| Security Guidance / Semgrep Guardian / Hookify | Model/pattern security reviews; Semgrep scanning and findings; custom event/pattern rules. | The security service or enforcement behavior your project needs. |
| Planning with Files / Claude-Mem / Context Mode | Explicit project plans; cross-session observations; large-output indexing and routing. | Plans for visible progress, memory for retrieval, Context Mode for output-heavy tasks. |
| GitHub / Code Review / Commit Commands | GitHub service tools; a review workflow; commit/push/PR commands. | The missing step in your existing workflow; check overlapping tool connections. |
| Learning / Explanatory Output Style | Learning includes explanations and asks you to contribute code; Explanatory focuses on explanations. | Learning for hands-on participation; Explanatory for narrated implementation. |
| Plugin Dev / Skill Creator / Claude Code Setup | Build a distribution bundle; improve a skill; recommend an existing setup. | The artifact you need to produce. |

## Three small setups for real work

**Ship a feature:** use Feature Dev to explore and plan the change. Add Context7 when a library API is uncertain. Add Playwright when you need to check the user journey in the running application. Each plugin addresses a different part of the task.

**Fix a production bug:** use Sentry to understand the error. Add Serena when tracing symbols across the codebase becomes the bottleneck. Reproduce the failure and verify the fix with your project's tests or Playwright. Error data and source access should match the project you are working on.

**Continue a long project:** start with Planning with Files when the missing thing is an explicit plan. Add Claude HUD for visibility. Consider Claude-Mem only when cross-session retrieval is useful; consider Context Mode when large outputs are consuming the context window. These solve different problems, so add them when the problem appears.

## How to choose and keep your setup useful

Pick a plugin for a task you can name. Read its primary source and inspect what `/plugin` says it will install. Skills and commands add instructions; agents run specialized work; hooks run at lifecycle events; MCP servers connect tools and data. A plain skills install can omit a plugin's hooks or server configuration.

For a service connection, check the account, permissions and test/live environment. For a local MCP process or hook, check the runtime, code and background behavior. Installing a plugin is not a security review. A recent commit or a large star count does not prove safety.

Check for duplicate MCP connections and overlapping workflow instructions before adding another plugin. Inspect `/context` after setup to see what is using the window. Third-party marketplaces normally require you to enable automatic updates or update manually; review updates that change permissions or background behavior. [Plugin security and trust](https://code.claude.com/docs/en/plugins/security).

This list includes plugin bundles with their own manifests and checked installation routes. Entries are selected by developer job; stars are shown as repository metadata. The nightly refresh checks stars, latest repository commit and archived status. Manual source and installation-route reviews are separate, performed monthly and after reported changes; [contribute a correction](CONTRIBUTING.md) when an upstream package changes.

The [MIT license](LICENSE) covers this list's original text. Each linked plugin has its own license and service terms; source-available packages are identified where relevant. No affiliate links or paid placements.

Maintained by [Gabe Bouslov](https://gabebouslov.com). Star the repository to find it again, or propose a concrete improvement through an issue or pull request.

## Alternatives

For a single reusable workflow, a standalone skill can be sufficient; the forthcoming [Best Claude Code Skills](https://github.com/gbouslov/best-claude-code-skills) list compares collections by task. For tools or live data alone, configure an [MCP server](https://code.claude.com/docs/en/mcp). For repository conventions, [Claude Code's memory and instructions](https://code.claude.com/docs/en/memory) can hold the shared guidance.

If your comparison is Claude Code plugins versus GitHub Copilot, [Copilot on GitHub](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) offers repository chat, coding tasks and pull-request review. Choose the host that fits where you work, then check which extensions it supports; a Claude Code plugin package is not automatically a Copilot extension.

For a larger awesome-list, browse [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code). For community experience, the [Reddit plugins-and-skills discussion](https://www.reddit.com/r/ClaudeCode/comments/1shlte1/what_are_your_favourite_pluginsskills_for_claude/) can suggest things to investigate; check each suggestion's current primary source before installing.

## About the nightly activity check

Stars and commit dates belong to the source repository. Multiple plugins in Anthropic's shared repository therefore show the same metadata; a repository commit can concern a different plugin. The manual manifest review date near the top of this page describes a different check.

<!-- freshness:start -->

## Repository activity

Repository metadata checked **2026-10-31 (UTC)**. Stars, latest default-branch commit and archive status describe each source repository, including shared repositories; they do not measure an individual plugin or skill release. Selection and installation guidance are reviewed separately.

| Selected resource | Repository stars | Latest repository commit (UTC) | Archived |
|---|---:|---|---|
| [Feature Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/feature-dev) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Superpowers](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) | 309,519 | [2026-10-21](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) | No |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | 27,782 | [2026-10-30](https://github.com/OthmanAdi/planning-with-files/commit/b6580cd24af1d8a95ab268794456e05608a1afd3) | No |
| [Code Simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Agent SDK Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Ralph Loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Code Review](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [PR Review Toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Security Guidance](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Semgrep Guardian](https://github.com/semgrep/guardian/tree/b58f407c6ac0f5fe47dee8301602f2e290a8ecfb/plugin) | 19 | [2026-10-22](https://github.com/semgrep/guardian/commit/653bd65347baf7f9fcfbf4f5376dee12599eb61b) | No |
| [Context7](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Serena](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/serena) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Playwright](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/playwright) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [GitHub](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/github) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [GitLab](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/gitlab) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Commit Commands](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/commit-commands) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Linear](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/linear) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Atlassian](https://github.com/atlassian/atlassian-mcp-server/tree/b74220d41142fae52b4f680c805b2ab81050991a) | 1,139 | [2026-10-29](https://github.com/atlassian/atlassian-mcp-server/commit/37e57a78b1938a099d1dcffdfc5a61154068c15e) | No |
| [Sentry](https://github.com/getsentry/plugin-claude/tree/73e53541d7af21672e27428c7067f4264b8a3d65) | 4 | [2026-10-22](https://github.com/getsentry/plugin-claude/commit/1b082a07d1a8149cf8a50596dd609fd1edf8f7df) | No |
| [Supabase](https://github.com/supabase-community/supabase-plugin/tree/2c6d02d4565babe784103ee4d446a93ae9b24151) | 40 | [2026-10-16](https://github.com/supabase-community/supabase-plugin/commit/016bf5b36670f7ad189ca90223513bd10406392d) | No |
| [Firebase](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/firebase) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Stripe](https://github.com/stripe/ai/tree/deae744bc0cbf6034b4b6f22f51c690b71a4e779/providers/claude/plugin) | 2,009 | [2026-10-31](https://github.com/stripe/ai/commit/1e24cf59cb0dd78df298afc3b7d372e5a5055ece) | No |
| [Vercel](https://github.com/vercel/vercel-plugin/tree/882e66c2698689324c341b7bb8fd8beb92c27bf6) | 321 | [2026-10-29](https://github.com/vercel/vercel-plugin/commit/67977fdf723174f4927dd5b9292a9d04c2a821ec) | No |
| [Figma](https://github.com/figma/mcp-server-guide/tree/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5) | 2,131 | [2026-10-28](https://github.com/figma/mcp-server-guide/commit/f3f264d9cbae059d9b96289ee33ce444b5c8e7e6) | No |
| [Context Mode](https://github.com/mksglu/context-mode) | 32,955 | [2026-10-30](https://github.com/mksglu/context-mode/commit/1e64208082f9ee10d1f6a8f60be5da723349ee47) | No |
| [Claude-Mem](https://github.com/thedotmack/claude-mem/tree/main/plugin) | 106,508 | [2026-10-30](https://github.com/thedotmack/claude-mem/commit/70aa40042cfb8157a0d84954b9c0d2b30b50af80) | No |
| [Claude HUD](https://github.com/jarrodwatts/claude-hud) | 29,040 | [2026-10-30](https://github.com/jarrodwatts/claude-hud/commit/83e98cf0806d137ea94133ea4945821ede9ee420) | No |
| [Explanatory Output Style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/explanatory-output-style) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Learning Output Style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/learning-output-style) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Claude Code Setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [CLAUDE.md Management](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Hookify](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Plugin Dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |
| [Skill Creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) | 45,465 | [2026-10-30](https://github.com/anthropics/claude-plugins-official/commit/a7ba5b93db0c7c8d17f3f1d25853adca79598a1a) | No |

<!-- freshness:end -->

## Frequently asked questions

### What are Claude Code plugins?

Plugins package reusable components such as skills, agents, hooks and MCP connections for installation together. The [component overview](https://code.claude.com/docs/en/plugins/overview) explains what each part adds; individual entries above identify the parts in that package.

### What is the difference between skills and plugins in Claude Code?

A skill teaches a reusable task through `SKILL.md`; a plugin distributes a setup that can include that skill and other components. Choose a standalone skill when you need the instructions alone, or a plugin when you want the surrounding agents, hooks or connections. See [plugins and skills, compared](#plugins-and-skills-compared).

### What are the best Claude Code plugins?

Start with your next job: Feature Dev for exploring and building a feature, Context7 for library documentation, and Playwright for a running web journey. Choose Figma for a source design or Sentry for production-error context; the [one-minute table](#choose-a-plugin-in-one-minute) compares the setup each adds.

### How to install Claude Code plugins?

Use `claude plugin install <plugin>@<marketplace> --scope local` in a terminal after registering the marketplace. Each entry above gives its specific command and prerequisites; `/reload-plugins` inside Claude Code loads a newly installed package into an existing session. [Install and manage](#install-and-manage).

### How to install Claude Code plugins from GitHub?

Register the publisher's marketplace with `claude plugin marketplace add owner/repo`, then install the plugin using that marketplace's registered name. A repository containing a skill alone is a different package type; use its upstream skill installation guide. [Marketplace setup](https://code.claude.com/docs/en/plugin-marketplaces).

### How to list Claude Code plugins?

Run `claude plugin list` in the terminal for installed plugins, or open `/plugin` inside Claude Code. Use its Discover view for available plugins and `claude plugin marketplace list` for registered catalogs. [Command reference](https://code.claude.com/docs/en/plugins/cli-reference).

### Are Claude Code plugins free?

The entries link to publicly accessible packages, each with its own license. Model usage, connected services and compute can cost money; check the entry's setup notes and upstream terms before choosing a package.

### How to update all Claude Code plugins?

Open `/plugin`, select a marketplace in Marketplaces, and choose Update marketplace to refresh that catalog and its installed plugins; some source types still need individual updates. The shell command `claude plugin marketplace update` refreshes listings, while `claude plugin update <plugin>@<marketplace>` updates a selected package. [Update behavior and exceptions](https://code.claude.com/docs/en/discover-plugins#update-plugins-now).

### How to uninstall Claude Code plugins?

Run `claude plugin uninstall <plugin>@<marketplace> --scope local` for a local installation, or choose the corresponding scope in `/plugin`. Use `disable` when you want to stop a plugin while keeping it installed. [Command reference](https://code.claude.com/docs/en/plugins/cli-reference).

### Are Claude Code plugins safe?

Review the package and its access before enabling it: hooks can execute commands, and servers can reach data and services with your permissions. Inspect the specific components, runtimes and accounts listed above and follow [Anthropic's security and trust guide](https://code.claude.com/docs/en/plugins/security); repository popularity is one signal about adoption, not a security assessment.

Read this directory on [GitHub Pages](https://gbouslov.github.io/best-claude-code-plugins/) or [GitHub](https://github.com/gbouslov/best-claude-code-plugins). Star it to keep the comparison handy.
