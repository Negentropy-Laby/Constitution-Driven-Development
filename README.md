<p align="center">
  <h1 align="center">Constitution Driven Development</h1>
  <p align="center">
    A runtime-neutral CDD governance framework with generated Claude Code and Codex adapters.
    <br />
    Turns AI-assisted coding into a staged, auditable, multi-agent delivery process — with a project brain.
    <br />
    memory_bank stores current laws, supporting context, execution state, and audit history.
    <br />
    53 agents. 74 skills. One governed CDD system for games, APIs, CLIs, web apps, SDKs, and data pipelines.
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/version-0.1.0-informational" alt="Version 0.1.0">
  <a href="agents"><img src="https://img.shields.io/badge/agents-53-blueviolet" alt="53 Agents"></a>
  <a href="skills"><img src="https://img.shields.io/badge/skills-74-green" alt="74 Skills"></a>
  <a href="hooks"><img src="https://img.shields.io/badge/hooks-11-orange" alt="11 Hooks"></a>
  <a href="rules"><img src="https://img.shields.io/badge/rules-16-red" alt="16 Rules"></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/runtime-Claude%20Code-f5f5f5?logo=anthropic" alt="Claude Code runtime"></a>
  <a href="https://learn.chatgpt.com/docs/agent-configuration/agents-md"><img src="https://img.shields.io/badge/runtime-Codex-10a37f" alt="Codex runtime"></a>
  <a href="https://github.com/Negentropy-Laby/Constitution-Driven-Development"><img src="https://img.shields.io/badge/repository-Negentropy--Laby%2FConstitution--Driven--Development-black?logo=github" alt="Repository: Negentropy-Laby/Constitution-Driven-Development"></a>
</p>

<p align="center">
  <strong>Latest release:</strong>
  <a href="https://github.com/Negentropy-Laby/Constitution-Driven-Development/releases/tag/v0.2.0">v0.2.0</a>
  — cross-runtime release gated by three-platform consistency and credential-free CLI contract evidence.
</p>

---

## Runtimes

CDD is runtime-neutral. In the designated Source library, canonical sources
(`skills/`, `agents/`, `hooks/`, `rules/`, `INSTRUCTIONS.md`) generate into their
declared runtime targets:

| Runtime | Root instructions | Skills | Agents | Hooks | Path rules |
|---|---|---|---|---|---|
| **Claude Code** (first-class) | `CLAUDE.md` | `.claude/skills/` | `.claude/agents/` | `.claude/hooks/` | `.claude/rules/` (native path globs) |
| **Codex** (first-class) | `AGENTS.md` | `.agents/skills/` | `.codex/agents/` (TOML) | `.codex/hooks/` | canonical `rules/` via guidance (no path-glob equivalent) |

Both runtimes share `INSTRUCTIONS.md`, `workflow/`, `templates/`, `standards/`,
`skill_testing/`, and nested `src/`/`design/`/`docs/` `INSTRUCTIONS.md` guidance.
The Source library delivers its developer templates and complete projections as
framework product assets. A Target first establishes actual CDD provenance,
ownership and delivery role, then applies [skill purpose](standards/skill-purpose.md)
only within that confirmed CDD asset collection. Project-owned skills, agents/roles,
tools, configuration and documents follow project rules even when used for development.
Required CDD templates, projections, generic standards/workflow originals and testing
definitions remain usable local inputs, excluded from Target Git tracking, staging,
commits and delivery/publication. They may be retained, discovered, loaded, take
effect and be used locally under existing authorization. Minimal required bindings
and independent portable configuration are CDD-related Git candidates only when
they neither carry nor reconstruct CDD instruction bodies or exclusive support.
Renaming or tailoring CDD content does not change its ownership; split confirmed
CDD content/support from project-owned candidates in mixed packages.
Codex's native `.codex/rules/*.rules` command-approval policy is unrelated and
never generator-owned.

An import-mode consumer uses its approved installed platform files directly and
keeps necessary support and project customizations. General CDD `agents/` and `skills/`
definitions are owned by the designated Source library; the consumer excludes a general
source mirror from its Git submission/publication set. Local placement is allowed
inside or outside the project and does not confer Source authority. Read installed entries and their required references to use
them; a local maintenance kit, import profile or lock is not a normal-use gate.
Optional maintenance readers can provide additional identity diagnostics, but
installed-file observations do not verify current Source or completed workflows.
Reproduction, generation and common-source edits still need the actual Source
and their own reviewed scope; ordinary installed use grants none of that authority.

Documentation uses slash-prefixed names as logical CDD command notation. Invoke
that form directly in Claude Code. In Codex, use `/skills` to browse
interactively or mention a skill explicitly with its `$name`; `codex exec`
automation uses the `$name` form.

## Start Here

Choose the path that matches your situation. For the short version with only
first command, outputs, and next step, read [docs/START-HERE.md](docs/START-HERE.md).
For the practical operating manual, including game, product, adoption, gate, and
release workflows, read [docs/USER-MANUAL.md](docs/USER-MANUAL.md).

| Path | First command | What it starts | Next normal checkpoint |
|------|---------------|----------------|------------------------|
| **New game project** | `/constitute` | Creates `memory_bank/` T0-T3 governance, ratifies laws, sets review mode, and routes concept direction | `/brainstorm game ideas` if needed, then `/design-review` and `/gate-check concept` |
| **New product / API / CLI / Web App** | `/constitute` | Creates `memory_bank/` T0-T3 governance, ratifies product principles, sets review mode, and routes workflow planning | `/brainstorm product ideas` if needed, then `/design-review` and `/gate-check concept` |
| **Existing project adoption** | `/project-stage-detect` | Stage diagnosis from existing design, architecture, source, tests, and production artifacts | `/adopt` or `/constitute` in existing-project mode, then retrofit missing artifacts |

Run `/help` at any time to see the next required step. Run `/cdd-status` when you
want a saved progress dashboard at `production/project-roadmap.md`; see
[`docs/examples/project-roadmap.example.md`](docs/examples/project-roadmap.example.md)
for the expected shape. Advancement follows the owning workflow and its required
checks. Optional/advisory risks may be accepted only as the actual policy allows.
Required `FAIL`, `NotRun`, `Blocked`, `Pending` or `Unknown` remain recorded;
risk acceptance or unrelated green checks do not turn them into PASS, completion
or a qualified phase. Record a legitimate scoped exception and explicitly
authorized independent continuing work separately; neither implies transition.
Qualified transition requires the owning workflow's exact evidence and named
authority. Editing `production/stage.txt` alone records a declaration, not
qualification.
Each slash command includes a local `User Guide` block covering when to use it,
inputs, outputs, memory-bank writes, and recommended next steps. Recommended
next steps never auto-run; users still advance by explicit command and approval.

---

## The Project Brain: memory_bank/

Every CDD project starts by creating or refreshing `memory_bank/`, the project
brain and governance control plane maintained by the workflow:

| Layer | What it answers | Maintained by |
|-------|-----------------|---------------|
| **T0 Core** | What is true now? | `/constitute`, `/gate-check`, `/team-release` |
| **T1 Axioms** | Why is it true? | `/constitute`, architecture, UX, QA, and design workflows |
| **T2 Execution** | What should happen next? | `/help`, `/cdd-status`, workflow catalog generators |
| **T3 Archive** | What evidence proves it? | Gate, review, QA, story, sprint, milestone, and release workflows |

`memory_bank/` does not replace `design/`, `docs/`, `workflow/`, `templates/`,
`standards/`, `skill_testing/`, or `production/`. Those directories are the
working bench for detailed source artifacts. The memory bank indexes, mirrors,
and summarizes them so the current state, next step, and audit trail stay
discoverable.

---

## Why This Exists

Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"

**Constitution Driven Development** solves this by giving your AI session the structure of a real studio. Instead of one general-purpose assistant, you get 53 specialized agents organized into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do the hands-on work. Each agent has defined responsibilities, escalation paths, and quality gates.

Building a product (API, CLI, web app, data pipeline) with AI faces the same challenges — no architectural guardrails, skipped design specs, untested migrations, no one asking "does this actually solve the user's problem?" The same agent hierarchy works for product projects: directors guard the product principles, department leads own their domains (architecture, UX, QA), and language specialists (Python, TypeScript, Rust, Go) do the hands-on work.

The result: you still make every decision, but now you have a team that asks the right questions, catches mistakes early, and keeps your project organized from first brainstorm to launch.

---

## Table of Contents

- [Start Here](#start-here)
- [The Project Brain](#the-project-brain-memory_bank)
- [What's Included](#whats-included)
- [How It Fits Together](#how-it-fits-together)
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
| **Memory Bank** | T0-T3 | Project governance brain for current laws, supporting context, execution mirrors, and audit evidence |
| **Agents** | 53 | Specialized subagents across design, programming, art, audio, narrative, QA, production, and language-specific product implementation |
| **Skills** | 74 | Slash commands for every workflow phase (`/constitute`, `/help`, `/cdd-status`, `/brainstorm`, `/design-system`, `/create-epics`, `/dev-story`, `/story-done`, etc.) |
| **Hooks** | 11 | Automated validation on commits, pushes, asset changes, session lifecycle, agent audit trail, and gap detection |
| **Rules** | 16 | Canonical path policies for actual matching capabilities; runtime loading/manual consultation and semantic verification are separate |
| **Templates** | 82 | Document templates for CDDs, UX specs, ADRs, sprint plans, HUD design, accessibility, product surface profiles, product style guides, memory-bank governance, and UI-heavy design systems |
| **Skill Testing** | 132 files | Cross-project skill/agent test catalog, specs, rubric, and spec templates |

## How It Fits Together

CDD turns a single AI agent session into a governed studio. A single owner ratifies the
project constitution, the memory bank carries current state, agents do the work, skills
and automated safety keep it honest, and gates guard release.

```text
Human Owner  (every binding decision)
      │  /constitute
      ▼
memory_bank/  — project brain & governance control plane
  T0 Core  │  T1 Axioms  │  T2 Execution  │  T3 Archive
      │  governs
      ▼
Studio Hierarchy — Directors (Opus) · Leads (Sonnet) · Specialists (Sonnet/Haiku)
      │  drive
      ▼
74 Skills (slash commands)   ──   11 Hooks + 16 Rules (automated safety)
      │
      ▼
Gate Checks — governed advisory: PASS / CONCERNS / FAIL
      │
      ▼
Evidence → Release  (T3 archive + production/stage.txt)
```

Every binding decision stays with the human owner; agents propose, draft, and request
approval before writing or committing. See [Studio Hierarchy](#studio-hierarchy) and
[How It Works](#how-it-works) for the details.

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
- An AI agent runtime — **Claude Code** (`npm install -g @anthropic-ai/claude-code`), **Codex**, or both
- Optional local maintenance only: [Python](https://www.python.org/) 3.11+ when running separately provided adapter-generation or consistency scripts (stdlib `tomllib`).
- **Recommended**: [jq](https://jqlang.github.io/jq/) for hook validation (hooks fall back to `grep` when absent)

Normal template and installed-platform use does not require Python or a local maintenance kit. Maintenance scripts are local-only and supplied separately; a fresh Source clone need not contain them. Python 3.11+ is required if those scripts are used. `jq` is optional for separately configured hooks, which fall back to `grep` when it is missing.

### Setup

These steps use a Source-library checkout's installed platform files. For an
ordinary Target import, use the selected platform's complete installed packages,
project instructions and required neutral originals; no additional complete copy
of Source-root `agents/` or `skills/` is required. See
[Ordinary Target installation](standards/directory-structure.md#ordinary-target-installation)
for platform paths and input requirements. Authorized local copies remain allowed;
exclude confirmed CDD source mirrors and full platform packages from Target Git
delivery while preserving project-owned skills, roles and configuration. An optional
maintenance profile may describe import/update work, but is not needed for ordinary use.

1. **Clone the Source library**:
   ```bash
   git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git my-cdd-project
   cd my-cdd-project
   ```

2. **Open your runtime** and start a session:
   - Claude Code: `claude`
   - Codex: `codex` (run from the project root so it discovers `AGENTS.md`)

3. **Run the `constitute` skill** — `/constitute` in Claude Code, or
   `$constitute` in Codex. The system creates or refreshes `memory_bank/`
   T0-T3 governance, asks where you are and what kind of project you are
   building, then guides you to the right workflow.

   Or jump directly to a specific skill if you already know what you need:
   **Game**: `/brainstorm game ideas` or `/setup-engine godot 4.6`
   **Product**: `/brainstorm product ideas` or `/setup-engine python 3.13 flask`
   **Either**: `/project-stage-detect` — analyze an existing project

### Project rules inherited by initialization and import

The reusable project-rule template is
`templates/memory-bank/t0_core/basic_law_index.md`, section "CDD Source and
Target Project Boundaries". It distinguishes the source library's template-only
delivery from the target's own business code, project documents and genuine QA
or acceptance evidence.

The complete boundary text is bundled inside the installed `constitute` entry
for both runtimes. A new target uses its approved platform package and project
instructions, then `/constitute` or `$constitute` includes this section in the
draft `memory_bank/t0_core/basic_law_index.md`. It does not need a local
maintenance toolkit or copies of general root `agents/` or `skills/`.
The skill still requires approval for project writes and separate ratification.

For imports, include full installed `constitute` and `adopt` entries in the approved
local-use platform package. These CDD framework entries and exclusive support remain
available for authorized local use and outside Target Git tracking, staging, commits
and delivery/publication. Review Git candidates separately from the complete
local package and neutral template/spec inputs. `adopt full` or `adopt infra` checks the actual
project-owned instructions or existing law index and proposes only an additive,
approved merge when these boundary rules are missing. Importing them does not
force Memory Bank creation, replace project rules or exclude normal business
design, QA, acceptance and historical documents. Use the delivered template
version; an older Git pin or clone does not acquire unpublished working changes.

### Using CDD in an existing project

Use the [ordinary Target installation rules](standards/directory-structure.md#ordinary-target-installation).
The selected platform supplies the agent and skill definitions; an extra complete
root `agents/` or `skills/` copy is not a normal import requirement. Required
local originals and references must still be complete and readable, including
when Git ignores them. Installation need does not determine Git eligibility.

**Confirm asset ownership before instruction purpose.** First establish actual CDD
framework provenance, ownership and delivery role for the complete package and its
required support. Apply instruction-purpose classification only within that confirmed
CDD asset collection. Project-owned skills, agents/roles, tools, configuration and
documents follow their project's rules; development use, native instruction fields
and skill-directory placement do not make them CDD assets. Renaming or tailoring a
CDD template does not itself change its ownership. Unresolved ownership stays pending.

**Target Git separation preserves authorized local use.** CDD framework assets and
maintenance tools are excluded from Target Git tracking, staging, commits and delivery/
publication contents. This does not prohibit their authorized local retention,
discovery, loading, effect or use. Keep complete required inputs at usable paths.
Ordinary template use must not depend on the local maintenance toolkit. Ignore and
runtime loading are separate; existing tracked content requires separately authorized,
recoverable tracking-only migration that leaves local files and required references intact.

Within confirmed CDD packages, independent portable configuration must neither carry
nor reconstruct CDD instruction bodies or exclusive support, and must have substantive
readers independent of those packages. A native loader alone does not qualify.

Read the approved installed platform entries, their required references and the
project's instructions. Ordinary use works offline without a local maintenance
reader, profile or lock. Missing required installed originals leave the affected
work incomplete; installation alone does not prove loading, execution or freshness.

The designated CDD Source owns general CDD definitions independently of local storage.
CDD separation concerns Target Git tracking, staging, commits and delivery/publication
content; it preserves authorized local retention, discovery, loading, effect and use.
Local maintenance files may stay inside or outside either repository; their
presence alone does not authorize a move, deletion or log-path change. Retain
project-specific configuration, reviewed differences, business documents and
recoverable history. Updates require the actual Source, scoped write authority,
independently reviewed update-write paths and required local-input allowlist,
separately reviewed Git submission candidates and readback of the installed
result. Source absence or identity/ownership conflicts block affected updates.
Preserve runtime settings and project customizations; hook activation and changes
to project state need their own authority.

### 3-Minute Smoke Test

For a quick validation path, run:

```text
Claude Code: /constitute -> /help -> /cdd-status --dry-run
Codex:      $constitute -> $help -> $cdd-status --dry-run
```

This mirrors the [New Project Smoke Path](docs/CUSTOMER-ACCEPTANCE.md#4-new-project-smoke-path).
For a fuller walkthrough, see [docs/QUICK-START.md](docs/QUICK-START.md).

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
# --- Canonical common sources in the Source library (hand-authored) ---
INSTRUCTIONS.md                     # Canonical root instructions (generated to CLAUDE.md + AGENTS.md)
skills/                             # 74 slash commands (canonical; generated into adapter runtimes)
agents/                             # Canonical agents (53; generated into adapter runtimes)
hooks/                              # Canonical hooks (11; generated into adapter runtimes)
rules/                              # Canonical path-scoped policies (16; -> .claude/rules/)
workflow/                           # Canonical workflow catalog + generated views
  workflow-catalog.yaml             # 7-phase pipeline definition (read by /help)
  generated/                        # Generated workflow views for gates
templates/                          # 82 document templates (docs + memory-bank)
standards/                          # Shared coding, coordination, context, setup standards
skill_testing/                      # Cross-project skill/agent test catalog, specs, rubric
adapters/                           # Adapter boundary notes (Claude, Codex, future runtimes)
# --- Nested instruction sources (generate CLAUDE.md + AGENTS.md per dir) ---
src/INSTRUCTIONS.md                 # -> src/CLAUDE.md + src/AGENTS.md
design/INSTRUCTIONS.md              # -> design/CLAUDE.md + design/AGENTS.md
docs/INSTRUCTIONS.md                # -> docs/CLAUDE.md + docs/AGENTS.md
# --- Installed runtime adapters (derived from their declared canonical owners) ---
CLAUDE.md                           # Generated root instructions (Claude)
AGENTS.md                           # Generated root instructions (Codex)
.claude/                            # MIXED OWNERSHIP: generated adapters + hand-authored config
  settings.json                     #   Hooks, permissions, model (hand-authored)
  statusline.sh                     #   Status line (hand-authored)
  agents/ skills/ hooks/ rules/     #   GENERATED Claude adapters
.agents/skills/                     # GENERATED Codex skill adapters
.codex/                             # MIXED OWNERSHIP: generated adapters + hand-authored config
  hooks.json                        #   Codex hook wiring (hand-authored)
  agents/ hooks/                    #   GENERATED Codex adapters (agents as TOML)
  rules/*.rules                     #   Codex NATIVE command-approval (runtime-owned; never generated)
# --- Project source / design / docs / production ---
memory_bank/                        # Project brain created by /constitute (T0-T3 governance)
  t0_core/                           # Current laws, current state, release state
  t1_axioms/                         # Technical, architecture, UX, QA, module context
  t2_execution/                      # Workflow contract, generated mirrors, roadmap
  t3_archive/                        # Gate, review, QA, story, sprint, release evidence indexes
src/                                # Game or product source code
  gameplay/ core/ ai/ networking/ ui/        # Game systems
  api/ cli/ services/ data/                  # Product systems
assets/                             # Game assets or product-facing assets/artifacts
design/                             # CDDs, product specs, narrative, levels, balance, UX
docs/                               # Technical documentation and ADRs
  engine-reference/                 # Game engine reference snapshots (version-pinned)
  reference/<stack>/                # Product stack/framework reference snapshots
tests/                              # Unit, integration, performance, playtest, contract, CLI, E2E, migration
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes (isolated from src/)
production/                         # Sprint plans, milestones, release tracking
```

## Reference: Slash Commands

The list below contains all 74 skills using logical slash-prefixed notation.
Claude Code invokes that form directly; Codex uses `/skills` to browse or
`$name` to invoke a specific skill:

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

### Project Brain Loop

CDD workflows work by reading and maintaining the project brain:

1. `/constitute` creates or refreshes `memory_bank/` T0-T3 governance.
2. `/help` and `/cdd-status` read workflow evidence and report the next step.
3. `/gate-check` evaluates exact required evidence; report, transition and T0 effects
   require their covered scope, with no automatic stage advance.
4. Review/QA/story/sprint/milestone/release workflows maintain only covered T3
   effects, preserving original evidence and unresolved actual checks.
5. Detailed work remains in `design/`, `docs/`, `workflow/`, `templates/`,
   `standards/`, `skill_testing/`, and `production/`.

Any high-impact workflow that produces a `PASS/FAIL`, `APPROVED/REJECTED`,
`GO/NO-GO`, `PROCEED/PIVOT/KILL`, `CUT/KEEP/DEFER`, or `RELEASE/HOLD` decision
may update only exact named T1/T0/T3 effects included in continuing authority.
Saving the original artifact alone excludes these pointers/state/indexes. Without
optional Memory Bank use established detailed artifact/report/conversation owners.

### Cross-Project Skill Testing

CDD's own skill and agent testing assets live in the neutral root
`skill_testing/` directory, not in a Claude adapter directory and not in a
separate top-level legacy framework. The memory-bank T2 template keeps only the
mount contract at `memory_bank/t2_execution/skill_testing/README.md`. Root
`skill_testing/` holds reusable standards: `catalog.yaml`, `quality-rubric.md`,
specs, and templates. T3 holds approved evidence:
`memory_bank/t3_archive/skill_testing/coverage-index.yaml`, result reports, and
skill improvement records. `/skill-test` and `/skill-improve` read actual canonical
`skill_testing/` assets through the optional mount; covered optional T3 report
writes and coverage-index effects are separate. Missing Memory Bank uses existing
fallback without creating another testing tree or activating governance.

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
5. **Approve scope** — named authority continues across sections/roles/retries;
   only material new effects or unresolved decisions need another approval

You stay in control. The agents provide structure and expertise, not autonomy.

### Automated Safety

**Hooks** below declare intended triggers. Actual supported runtime wiring and
observed execution determine whether a hook ran; generated scripts alone do not:

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

> **Note**: When their supported triggers are configured and fire, these hooks
> exit early for irrelevant commands/paths. Configuration or file presence alone
> does not prove this session executed them.

**Permission rules** in hand-authored `settings.json` apply only through the
actual supported runtime configuration. They do not replace scoped user authority;
Codex native command policies remain runtime-owned and separate.

### Path-Scoped Rules

Canonical policies are selected by their actual path globs. Claude Code supports
path-based loading; Codex consults canonical `rules/*.md` manually through root
guidance. Neither source presence nor loading certifies semantic enforcement:

| Path | Policy guidance |
|------|----------|
| `src/gameplay/**` | Data-driven values, delta time usage, no UI references |
| `src/core/**` | Zero allocations in hot paths, thread safety, API stability |
| `src/ai/**` | Performance budgets, debuggability, data-driven parameters |
| `src/networking/**` | Server-authoritative, versioned messages, security |
| `src/ui/**` | Applicable Game state/input/audio/thread rules and Product state/workflow/accessibility |
| `src/api/**` | Contract stability, status/error semantics, schema documentation, security checks |
| `src/cli/**` | Stable flags, stdout/stderr boundaries, exit codes, help text, scripted usage |
| `src/app/**`, `src/web/**` | Workflow ownership, accessibility, localization, error states, API handoff |
| `src/services/**` | Dependency isolation, retries/timeouts, idempotency, observability |
| `migrations/**` | Reversible or dry-run behavior, data safety, versioned rollout notes |
| `config/**` | No secrets, environment separation, documented defaults |
| `design/cdd/**` | Module CDD semantic eight; concept/index/support use actual DocKind owners |
| `tests/**` | Configured naming, required evidence and isolated fixtures |
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

The Source library is a **template**, not a locked framework. The choices below
apply to authorized source-authoring changes, not automatic writes in an imported
project. An import-mode project prepares reviewed project differences with exact
base/result identities and installs only an approved local-input allowlist. Classify
complete instruction/role packages before choosing separate Git candidates; project-specific
developer overlays gain no exception. Common
improvements require a separately approved Source changeset. Do not recreate
root `agents/` or `skills/` mirrors in consumer Git delivery as a customization shortcut:

- **Add/remove agents** — delete agent files you don't need, add new ones for your domains
- **Edit agent prompts** — tune agent behavior, add project-specific knowledge
- **Modify skills** — adjust workflows to match your team's process
- **Add rules** — create new path-scoped rules for your project's directory structure
- **Tune hooks** — adjust validation strictness, add new checks
- **Pick your engine or stack** — use the Godot, Unity, or Unreal agent set for games; use the Python, TypeScript, Rust, or Go specialist path for product projects
- **Set review intensity** — `full` (all director gates), `lean` (phase gates only), or `solo` (none). Set during `/constitute` or edit `production/review-mode.txt`. Override per-run with `--review solo` only on gate-using skills whose actual interface accepts it; consult that skill's instructions.

## Platform Support

Installed adapters target Claude Code and Codex. Windows local hook execution
requires Git Bash; Windows toast notifications are optional and fall back to
plain hook output when unavailable. Read the actual runtime configuration and
required installed inputs before claiming a supported action ran.

Historical Source releases may carry `Template Consistency` evidence for
**Ubuntu**, **macOS**, and **Windows**, plus credential-free `Runtime Contract`
CLI trials. Those local-only workflows are excluded from the current template
delivery; their results cover only the identified release commit and actual
checks. They do not prove live autoload, agent execution, semantic qualification
or project completion. Current delivery acceptance follows
[docs/CUSTOMER-ACCEPTANCE.md](docs/CUSTOMER-ACCEPTANCE.md) and the target's real
test/QA contract without requiring a local maintenance kit.

## Community

- **Discussions** — [GitHub Discussions](https://github.com/Negentropy-Laby/Constitution-Driven-Development/discussions) for questions, ideas, and showcasing what you've built
- **Issues** — [Bug reports and feature requests](https://github.com/Negentropy-Laby/Constitution-Driven-Development/issues)

---

## Maintainers

Constitution Driven Development is free and open source. It is maintained in the [Negentropy-Laby/Constitution-Driven-Development](https://github.com/Negentropy-Laby/Constitution-Driven-Development) repository.

---

*A runtime-neutral CDD framework with generated Claude Code and Codex adapters. Contributions welcome via [GitHub Discussions](https://github.com/Negentropy-Laby/Constitution-Driven-Development/discussions).*

## License

MIT License. See [LICENSE](LICENSE) for details.

Runtime transforms and mixed ownership are documented in `adapters/README.md`.
The framework's generated source adapters remain usable; optional `memory_bank/`
initialization, actual runtime execution and qualified project state are separate
facts. Adapter source digests exclude neutral linked supports, whose exact bytes
must accompany relied-on review evidence under `standards/evidence-lifecycle.md`.
