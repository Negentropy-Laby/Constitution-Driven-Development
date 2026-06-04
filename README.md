<p align="center">
  <h1 align="center">Constitution Driven Development</h1>
  <p align="center">
    Turn a single Claude Code session into a coordinated development team.
    <br />
    Also supports product development: APIs, CLIs, web apps, data pipelines.
    <br />
    53 agents. 74 skills. One coordinated AI team.
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/version-0.1.0-informational" alt="Version 0.1.0">
  <a href=".claude/agents"><img src="https://img.shields.io/badge/agents-53-blueviolet" alt="53 Agents"></a>
  <a href=".claude/skills"><img src="https://img.shields.io/badge/skills-74-green" alt="74 Skills"></a>
  <a href=".claude/hooks"><img src="https://img.shields.io/badge/hooks-12-orange" alt="12 Hooks"></a>
  <a href=".claude/rules"><img src="https://img.shields.io/badge/rules-16-red" alt="16 Rules"></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/built%20for-Claude%20Code-f5f5f5?logo=anthropic" alt="Built for Claude Code"></a>
  <a href="https://github.com/Negentropy-Laby/Constitution-Driven-Development"><img src="https://img.shields.io/badge/repository-Negentropy--Laby%2FConstitution--Driven--Development-black?logo=github" alt="Repository: Negentropy-Laby/Constitution-Driven-Development"></a>
</p>

<p align="center">
  <strong>Latest release:</strong>
  <a href="https://github.com/Negentropy-Laby/Constitution-Driven-Development/releases/tag/v0.1.0">v0.1.0</a>
  — stable template release validated by Template Consistency on Ubuntu, macOS, and Windows.
</p>

---

## Start Here

Choose the path that matches your situation. For the short version with only
first command, outputs, and next step, read [docs/START-HERE.md](docs/START-HERE.md).
For the practical operating manual, including game, product, adoption, gate, and
release workflows, read [docs/USER-MANUAL.md](docs/USER-MANUAL.md).

| Path | First command | What it starts | Next normal checkpoint |
|------|---------------|----------------|------------------------|
| **New game project** | `/constitute` | Governing principles, project memory, review mode, and game concept direction | `/brainstorm game ideas` if needed, then `/design-review` and `/gate-check concept` |
| **New product / API / CLI / Web App** | `/constitute` | Governing principles, product promise, user workflow, and stack-neutral planning | `/brainstorm product ideas` if needed, then `/design-review` and `/gate-check concept` |
| **Existing project adoption** | `/project-stage-detect` | Stage diagnosis from existing design, architecture, source, tests, and production artifacts | `/adopt` or `/constitute` in existing-project mode, then retrofit missing artifacts |

Run `/help` at any time to see the next required step. Run `/cdd-status` when you
want a saved progress dashboard at `production/project-roadmap.md`; see
[`docs/examples/project-roadmap.example.md`](docs/examples/project-roadmap.example.md)
for the expected shape. Gates are
governed advisory: they must run before normal advancement; a `FAIL` requires
explicit override and a risk note before `production/stage.txt` advances.

---

## Why This Exists

Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"

**Constitution Driven Development** solves this by giving your AI session the structure of a real studio. Instead of one general-purpose assistant, you get 53 specialized agents organized into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do the hands-on work. Each agent has defined responsibilities, escalation paths, and quality gates.

Building a product (API, CLI, web app, data pipeline) with AI faces the same challenges — no architectural guardrails, skipped design specs, untested migrations, no one asking "does this actually solve the user's problem?" The same agent hierarchy works for product projects: directors guard the product principles, department leads own their domains (architecture, UX, QA), and language specialists (Python, TypeScript, Rust, Go) do the hands-on work.

The result: you still make every decision, but now you have a team that asks the right questions, catches mistakes early, and keeps your project organized from first brainstorm to launch.

---

## Table of Contents

- [Start Here](#start-here)
- [What's Included](#whats-included)
- [Studio Hierarchy](#studio-hierarchy)
- [Getting Started](#getting-started)
- [User Manual](#user-manual)
- [Upgrading](#upgrading)
- [Project Structure](#project-structure)
- [Reference: Slash Commands](#reference-slash-commands)
- [How It Works](#how-it-works)
- [Design Philosophy](#design-philosophy)
- [Customization](#customization)
- [Platform Support](#platform-support)
- [Community](#community)
- [Maintainers](#maintainers)
- [License](#license)

---

## What's Included

| Category | Count | Description |
|----------|-------|-------------|
| **Agents** | 53 | Specialized subagents across design, programming, art, audio, narrative, QA, production, and language-specific product implementation |
| **Skills** | 74 | Slash commands for every workflow phase (`/constitute`, `/help`, `/cdd-status`, `/brainstorm`, `/design-system`, `/create-epics`, `/dev-story`, `/story-done`, etc.) |
| **Hooks** | 12 | Automated validation on commits, pushes, asset changes, session lifecycle, agent audit trail, and gap detection |
| **Rules** | 16 | Path-scoped coding standards enforced when editing gameplay, engine, AI, UI, network, API, CLI, services, config, migrations, data, and infrastructure code |
| **Templates** | 50 | Document templates for CDDs, UX specs, ADRs, sprint plans, HUD design, accessibility, product surface profiles, product style guides, and UI-heavy design systems |

## Studio Hierarchy

Agents are organized into three tiers, matching how real studios operate:

```
Tier 1 — Directors (Opus)
  creative-director    technical-director    producer

Tier 2 — Department Leads (Sonnet)
  game-designer        lead-programmer       art-director
  audio-director       narrative-director    qa-lead
  release-manager      localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
  gameplay-programmer  engine-programmer     ai-programmer
  network-programmer   tools-programmer      ui-programmer
  systems-designer     level-designer        economy-designer
  technical-artist     sound-designer        writer
  world-builder        ux-designer           prototyper
  performance-analyst  devops-engineer       analytics-engineer
  security-engineer    qa-tester             accessibility-specialist
  python-specialist    typescript-specialist rust-specialist
  go-specialist
  live-ops-designer    community-manager
```

### Engine Specialists

The template includes agent sets for all three major engines. Use the set that matches your project:

| Engine | Lead Agent | Sub-Specialists |
|--------|-----------|-----------------|
| **Godot 4** | `godot-specialist` | GDScript, Shaders, GDExtension |
| **Unity** | `unity-specialist` | DOTS/ECS, Shaders/VFX, Addressables, UI Toolkit |
| **Unreal Engine 5** | `unreal-specialist` | GAS, Blueprints, Replication, UMG/CommonUI |

### Product Language Specialists

Product projects use language-specialist agents for stack-specific implementation and review:

| Language | Specialist |
|----------|------------|
| **Python** | `python-specialist` |
| **TypeScript** | `typescript-specialist` |
| **Rust** | `rust-specialist` |
| **Go** | `go-specialist` |

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- **Recommended**: [jq](https://jqlang.github.io/jq/) (for hook validation) and Python 3 (for JSON validation)

All hooks fail gracefully if optional tools are missing — nothing breaks, you just lose validation.

### Setup

1. **Clone or use as template**:
   ```bash
   git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git my-cdd-project
   cd my-cdd-project
   ```

2. **Open Claude Code** and start a session:
   ```bash
   claude
   ```

3. **Run `/constitute`** — the system asks where you are and what kind of project
   (game or product, fresh idea, clear design, existing work) and guides you to the
   right workflow. No assumptions about your domain.

   Or jump directly to a specific skill if you already know what you need:
   **Game**: `/brainstorm game ideas` or `/setup-engine godot 4.6`
   **Product**: `/brainstorm product ideas` or `/setup-engine python 3.13 flask`
   **Either**: `/project-stage-detect` — analyze an existing project

## User Manual

For the full user-facing operating guide, see [docs/USER-MANUAL.md](docs/USER-MANUAL.md).
It covers first commands, game and product paths, brownfield adoption, gates,
generated artifacts, release evidence, and troubleshooting.

## Upgrading

Already using an older version of this template? See [UPGRADING.md](UPGRADING.md)
for step-by-step migration instructions, a breakdown of what changed between
versions, and which files are safe to overwrite vs. which need a manual merge.

## Project Structure

```
CLAUDE.md                           # Master configuration
.claude/
  settings.json                     # Hooks, permissions, safety rules
  agents/                           # 53 agent definitions (markdown + YAML frontmatter)
  skills/                           # 74 slash commands (subdirectory per skill)
  hooks/                            # 12 hook scripts (bash, cross-platform)
  rules/                            # 16 path-scoped coding standards
  statusline.sh                     # Status line script (context%, model, stage, epic breadcrumb)
  docs/
    workflow-catalog.yaml           # 7-phase pipeline definition (read by /help)
    templates/                      # 50 document templates
src/                                # Game source code or product source code
  gameplay/                         # Game mechanics and playable systems
  core/                             # Engine/framework/core domain code
  api/                              # Product API endpoints and schemas
  cli/                              # Product CLI commands and terminal UX
  services/                         # Product services, jobs, integrations
  app/ or web/                      # Product web/mobile/desktop UI surface
  data/                             # Product data pipelines and transforms
assets/                             # Game assets or product-facing assets/artifacts
design/                             # CDDs, product specs, brand/style docs, narrative docs, level designs, UX
docs/                               # Technical documentation and ADRs
  engine-reference/                 # Game engine reference snapshots
  reference/<stack>/                # Product stack/framework reference snapshots
tests/                              # Unit, integration, performance, playtest, contract, CLI, E2E, migration
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes (isolated from src/)
production/                         # Sprint plans, milestones, release tracking
```

## Reference: Slash Commands

Type `/` in Claude Code to access all 74 skills:

**Onboarding & Navigation**
`/constitute` `/constitute-check` `/help` `/cdd-status` `/project-stage-detect` `/setup-engine` `/adopt`

**Concept & Systems Design**
`/brainstorm` `/map-systems` `/design-system` `/quick-design` `/review-all-gdds` `/propagate-design-change`

**Art, Assets & Product Artifacts**
`/art-bible` `/asset-spec` `/asset-audit`

**UX & Interface Design**
`/ux-design` `/ux-review`

**Architecture**
`/create-architecture` `/architecture-decision` `/architecture-review` `/create-control-manifest`

**Stories & Sprints**
`/create-epics` `/create-stories` `/dev-story` `/sprint-plan` `/sprint-status` `/story-readiness` `/story-done` `/estimate`

**Reviews & Analysis**
`/design-review` `/code-review` `/balance-check` `/content-audit` `/scope-check` `/perf-profile` `/tech-debt` `/gate-check` `/consistency-check` `/security-audit`

**QA & Testing**
`/qa-plan` `/smoke-check` `/soak-test` `/regression-suite` `/test-setup` `/test-helpers` `/test-evidence-review` `/test-flakiness` `/skill-test` `/skill-improve`

**Production / Implementation**
`/milestone-review` `/retrospective` `/bug-report` `/bug-triage` `/reverse-document` `/playtest-report`

**Release**
`/release-checklist` `/launch-checklist` `/changelog` `/patch-notes` `/hotfix` `/day-one-patch`

**Prototyping & Content**
`/prototype` `/onboard` `/localize`

**Team Orchestration (Game/Product)**
`/team-combat` `/team-narrative` `/team-ui` `/team-release` `/team-polish` `/team-audio` `/team-level` `/team-live-ops` `/team-qa`

## How It Works

### Agent Coordination

Agents follow a structured delegation model:

1. **Vertical delegation** — directors delegate to leads, leads delegate to specialists
2. **Horizontal consultation** — same-tier agents can consult each other but can't make binding cross-domain decisions
3. **Conflict resolution** — disagreements escalate up to the shared parent (`creative-director` for design, `technical-director` for technical)
4. **Change propagation** — cross-department changes are coordinated by `producer`
5. **Domain boundaries** — agents don't modify files outside their domain without explicit delegation

### Collaborative, Not Autonomous

This is **not** an auto-pilot system. Every agent follows a strict collaboration protocol:

1. **Ask** — agents ask questions before proposing solutions
2. **Present options** — agents show 2-4 options with pros/cons
3. **You decide** — the user always makes the call
4. **Draft** — agents show work before finalizing
5. **Approve** — nothing gets written without your sign-off

You stay in control. The agents provide structure and expertise, not autonomy.

### Automated Safety

**Hooks** run automatically on every session:

| Hook | Trigger | What It Does |
|------|---------|--------------|
| `validate-commit.sh` | PreToolUse (Bash) | Checks for hardcoded values, TODO format, JSON validity, design doc sections — exits early if the command is not `git commit` |
| `validate-push.sh` | PreToolUse (Bash) | Warns on pushes to protected branches — exits early if the command is not `git push` |
| `validate-assets.sh` | PostToolUse (Write/Edit) | Validates naming conventions and JSON structure — exits early if the file is not in `assets/` |
| `session-start.sh` | Session open | Shows current branch and recent commits for orientation |
| `detect-gaps.sh` | Session open | Detects fresh projects (suggests `/constitute`) and missing design docs when code or prototypes exist |
| `pre-compact.sh` | Before compaction | Preserves session progress notes |
| `post-compact.sh` | After compaction | Reminds Claude to restore session state from `active.md` |
| `notify.sh` | Notification event | Shows Windows toast notification via PowerShell |
| `session-stop.sh` | Session close | Archives `active.md` to session log and records git activity |
| `log-agent.sh` | Agent spawned | Audit trail start — logs subagent invocation |
| `log-agent-stop.sh` | Agent stops | Audit trail stop — completes subagent record |
| `validate-skill-change.sh` | PostToolUse (Write/Edit) | Advises running `/skill-test` after any `.claude/skills/` change |

> **Note**: `validate-commit.sh`, `validate-assets.sh`, and `validate-skill-change.sh` fire on every Bash/Write tool call and exit immediately (exit 0) when the command or file path is not relevant. This is normal hook behavior — not a performance concern.

**Permission rules** in `settings.json` auto-allow safe operations (git status, test runs) and block dangerous ones (force push, `rm -rf`, reading `.env` files).

### Path-Scoped Rules

Coding standards are automatically enforced based on file location:

| Path | Enforces |
|------|----------|
| `src/gameplay/**` | Data-driven values, delta time usage, no UI references |
| `src/core/**` | Zero allocations in hot paths, thread safety, API stability |
| `src/ai/**` | Performance budgets, debuggability, data-driven parameters |
| `src/networking/**` | Server-authoritative, versioned messages, security |
| `src/ui/**` | No game state ownership, localization-ready, accessibility |
| `src/api/**` | Contract stability, status/error semantics, schema documentation, security checks |
| `src/cli/**` | Stable flags, stdout/stderr boundaries, exit codes, help text, scripted usage |
| `src/app/**`, `src/web/**` | Workflow ownership, accessibility, localization, error states, API handoff |
| `src/services/**` | Dependency isolation, retries/timeouts, idempotency, observability |
| `migrations/**` | Reversible or dry-run behavior, data safety, versioned rollout notes |
| `config/**` | No secrets, environment separation, documented defaults |
| `design/cdd/**` | Required 8 sections, formula format, edge cases |
| `tests/**` | Test naming, coverage requirements, fixture patterns |
| `prototypes/**` | Relaxed standards, README required, hypothesis documented |

## Design Philosophy

This template is grounded in professional game and product development practices.

For **game projects**, it preserves established game design theory:

- **MDA Framework** — Mechanics, Dynamics, Aesthetics analysis for game design
- **Self-Determination Theory** — Autonomy, Competence, Relatedness for player motivation
- **Flow State Design** — Challenge-skill balance for player engagement
- **Bartle Player Types** — Audience targeting and validation
- **Verification-Driven Development** — Tests first, then implementation

For **product projects**, it uses equivalent product-development discipline:

- **Jobs To Be Done** — what the user is trying to accomplish, in context
- **Workflow-first design** — model the user's path, decision points, and failure states before implementation
- **Contract-first implementation** — API schemas, CLI flags, data models, migrations, and integration promises are explicit
- **Operational readiness** — observability, error handling, rollback, security, and documentation are part of done
- **Verification-Driven Development** — tests first for stable contracts, critical workflows, and migration safety

## Customization

This is a **template**, not a locked framework. Everything is meant to be customized:

- **Add/remove agents** — delete agent files you don't need, add new ones for your domains
- **Edit agent prompts** — tune agent behavior, add project-specific knowledge
- **Modify skills** — adjust workflows to match your team's process
- **Add rules** — create new path-scoped rules for your project's directory structure
- **Tune hooks** — adjust validation strictness, add new checks
- **Pick your engine or stack** — use the Godot, Unity, or Unreal agent set for games; use the Python, TypeScript, Rust, or Go specialist path for product projects
- **Set review intensity** — `full` (all director gates), `lean` (phase gates only), or `solo` (none). Set during `/constitute` or edit `production/review-mode.txt`. Override per-run with `--review solo` on any skill.

## Platform Support

Template consistency CI verifies **Ubuntu**, **macOS**, and **Windows** runners. Local hook execution on Windows requires **Git Bash**; hook scripts use POSIX-compatible shell patterns and are smoke-tested through Bash. Windows toast notifications are optional and fall back to plain hook output when unavailable.

## Community

- **Discussions** — [GitHub Discussions](https://github.com/Negentropy-Laby/Constitution-Driven-Development/discussions) for questions, ideas, and showcasing what you've built
- **Issues** — [Bug reports and feature requests](https://github.com/Negentropy-Laby/Constitution-Driven-Development/issues)

---

## Maintainers

Constitution Driven Development is free and open source. It is maintained in the [Negentropy-Laby/Constitution-Driven-Development](https://github.com/Negentropy-Laby/Constitution-Driven-Development) repository.

---

*Built for Claude Code. Maintained and extended — contributions welcome via [GitHub Discussions](https://github.com/Negentropy-Laby/Constitution-Driven-Development/discussions).*

## License

MIT License. See [LICENSE](LICENSE) for details.
