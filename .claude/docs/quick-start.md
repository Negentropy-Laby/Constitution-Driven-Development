# Constitution Driven Development — Quick Start Guide

## What Is This?

This is a complete Claude Code agent architecture supporting both **game development**
and **general product development** (web apps, CLI tools, APIs, data pipelines).

It organizes 53 specialized AI agents into a studio hierarchy that mirrors
real development teams, with defined responsibilities, delegation rules, and
coordination protocols.

**Game projects**: engine-specialist agents for Godot, Unity, and Unreal — each with
dedicated sub-specialists for major engine subsystems. Design agents and templates are
grounded in established game design theory (MDA Framework, Self-Determination Theory,
Flow State, Bartle Player Types).

**Product projects**: language-specialist agents (Python, TypeScript, Rust, Go) with
stack-aware architecture, testing, and deployment workflows. Design agents and
templates are grounded in product development theory (JTBD, user psychology,
action-first design).

Use whichever agent set matches your project.

## How to Use

### 1. Understand the Hierarchy

There are three tiers of agents:

- **Tier 1 (Opus)**: Directors who make high-level decisions
  - `creative-director` -- vision and creative conflict resolution
  - `technical-director` -- architecture and technology decisions
  - `producer` -- scheduling, coordination, and risk management

- **Tier 2 (Sonnet)**: Department leads who own their domain
  - `game-designer`, `lead-programmer`, `art-director`, `audio-director`,
    `narrative-director`, `qa-lead`, `release-manager`, `localization-lead`

- **Tier 3 (Sonnet/Haiku)**: Specialists who execute within their domain
  - Designers, programmers, artists, writers, testers, engineers

### 2. Pick the Right Agent for the Job

Ask yourself: "What department would handle this in a real studio?"

| I need to... | Use this agent |
|-------------|---------------|
| Design a new mechanic | `game-designer` |
| Design an API endpoint or CLI command | `lead-programmer` or `ux-designer` |
| Write combat code | `gameplay-programmer` |
| Write API/backend code | `lead-programmer` + language specialist |
| Create a shader | `technical-artist` |
| Architect a database schema | `lead-programmer` |
| Design a user workflow | `ux-designer` |
| Review code quality | `lead-programmer` (via `/code-review`) |
| Write dialogue | `writer` |
| Plan the next sprint | `producer` |
| Review code quality | `lead-programmer` |
| Write test cases | `qa-tester` |
| Design a level | `level-designer` |
| Fix a performance problem | `performance-analyst` |
| Set up CI/CD | `devops-engineer` |
| Design a loot table | `economy-designer` |
| Resolve a creative conflict | `creative-director` |
| Make an architecture decision | `technical-director` |
| Manage a release | `release-manager` |
| Prepare strings for translation | `localization-lead` |
| Test a mechanic idea quickly | `prototyper` |
| Review code for security issues | `security-engineer` |
| Check accessibility compliance | `accessibility-specialist` |
| Get Unreal Engine advice | `unreal-specialist` |
| Get Unity advice | `unity-specialist` |
| Get Godot advice | `godot-specialist` |
| Design GAS abilities/effects | `ue-gas-specialist` |
| Define BP/C++ boundaries | `ue-blueprint-specialist` |
| Implement UE replication | `ue-replication-specialist` |
| Build UMG/CommonUI widgets | `ue-umg-specialist` |
| Design DOTS/ECS architecture | `unity-dots-specialist` |
| Write Unity shaders/VFX | `unity-shader-specialist` |
| Manage Addressable assets | `unity-addressables-specialist` |
| Build UI Toolkit/UGUI screens | `unity-ui-specialist` |
| Write idiomatic GDScript | `godot-gdscript-specialist` |
| Create Godot shaders | `godot-shader-specialist` |
| Build GDExtension modules | `godot-gdextension-specialist` |
| Plan live events and seasons | `live-ops-designer` |
| Write patch notes for players | `community-manager` |
| Brainstorm a new game idea | Use `/brainstorm` skill |

### 3. Use Slash Commands for Common Tasks

| Command | What it does |
|---------|-------------|
| `/constitute` | CDD onboarding — asks where you are, establishes governing principles, routes to the right workflow |
| `/help` | Context-aware "what do I do next?" — reads your current phase and artifacts |
| `/project-stage-detect` | Analyze project state, detect stage, identify gaps |
| `/setup-engine` | Configure engine + version for games, or language/framework stack for products; populate reference docs |
| `/adopt` | Brownfield audit and migration plan for existing projects |
| `/brainstorm` | Guided concept ideation from scratch: game concepts or product concepts |
| `/map-systems` | Decompose concept into systems, map dependencies, guide per-system CDDs |
| `/design-system` | Guided, section-by-section CDD authoring for a game system or product module |
| `/quick-design` | Lightweight spec for small changes — tuning, tweaks, minor additions |
| `/review-all-gdds` | Cross-CDD consistency review; game design theory for games, workflow/value coherence for products |
| `/propagate-design-change` | Find ADRs and stories affected by a CDD change |
| `/ux-design` | Author UX specs (screen/flow, HUD, interaction patterns) |
| `/ux-review` | Validate UX specs for accessibility and CDD alignment |
| `/create-architecture` | Master architecture document for game systems and product modules |
| `/architecture-decision` | Creates an ADR |
| `/architecture-review` | Validate all ADRs, dependency ordering, CDD traceability |
| `/create-control-manifest` | Flat programmer rules sheet from Accepted ADRs |
| `/create-epics` | Translate CDDs + ADRs into epics (one per architectural module) |
| `/create-stories` | Break a single epic into implementable story files |
| `/dev-story` | Read a story and implement it — routes to the correct programmer agent |
| `/sprint-plan` | Creates or updates sprint plans |
| `/sprint-status` | Quick 30-line sprint snapshot |
| `/story-readiness` | Validate a story is implementation-ready before pickup |
| `/story-done` | End-of-story completion review — verifies acceptance criteria |
| `/estimate` | Produces structured effort estimates |
| `/design-review` | Reviews a design document |
| `/code-review` | Reviews code for quality and architecture |
| `/balance-check` | Game balance formulas/economy; product quotas, rate limits, pricing tiers, permissions, and workflow friction |
| `/asset-audit` | Game asset compliance; product build artifacts, API schemas, docs assets, release bundles |
| `/content-audit` | CDD-specified content vs. implemented — find gaps |
| `/scope-check` | Detect scope creep against plan |
| `/perf-profile` | Performance profiling and bottleneck ID |
| `/tech-debt` | Scan, track, and prioritize tech debt |
| `/gate-check` | Validate phase readiness (PASS/CONCERNS/FAIL) |
| `/consistency-check` | Scan all CDDs for cross-document inconsistencies (conflicting stats, names, rules) |
| `/reverse-document` | Generate design/architecture docs from existing code |
| `/milestone-review` | Reviews milestone progress |
| `/retrospective` | Runs sprint/milestone retrospective |
| `/bug-report` | Structured bug report creation |
| `/playtest-report` | Game playtest report; product user-test / workflow validation report |
| `/onboard` | Generates onboarding docs for a role |
| `/release-checklist` | Validates pre-release checklist |
| `/launch-checklist` | Complete launch readiness validation |
| `/changelog` | Generates changelog from git history |
| `/patch-notes` | Generate game player-facing patch notes or product developer/user-facing release notes |
| `/hotfix` | Emergency fix with audit trail |
| `/prototype` | Scaffolds a throwaway prototype |
| `/localize` | Localization scan, extract, validate |
| `/team-combat` | Game combat feature squad; product critical-workflow/API/CLI feature squad |
| `/team-narrative` | Game narrative/worldbuilding squad; product content/onboarding/docs narrative squad |
| `/team-ui` | Game UI/HUD squad; product web UI, CLI interaction, or API consumer journey squad |
| `/team-release` | Game release squad; product deployment/release squad |
| `/team-polish` | Game polish pass; product UX/API/CLI/docs/reliability polish pass |
| `/team-audio` | Game audio squad; product notification/status feedback and accessibility signal squad |
| `/team-level` | Game level/area squad; product workflow/module area squad |
| `/team-live-ops` | Game live-ops squad; product lifecycle/feature flag/analytics operations squad |
| `/team-qa` | Game QA/playtest squad; product contract/integration/migration/user-test QA squad |
| `/qa-plan` | Generate a QA test plan for a sprint or feature |
| `/bug-triage` | Re-prioritize open bugs, assign to sprints, surface systemic trends |
| `/smoke-check` | Run critical path smoke test gate before QA hand-off (PASS/FAIL) |
| `/soak-test` | Game extended play-session soak test; product endurance/load/reliability soak protocol |
| `/regression-suite` | Map coverage to CDD critical paths, flag gaps, maintain regression suite |
| `/test-setup` | Scaffold test framework + CI pipeline for the project's game engine or product stack (run once) |
| `/test-helpers` | Generate game engine-specific or product language/stack-specific test helper libraries and factory functions |
| `/test-flakiness` | Detect flaky tests from CI history, flag for quarantine or fix |
| `/test-evidence-review` | Quality review of test files and manual evidence — ADEQUATE/INCOMPLETE/MISSING |
| `/skill-test` | Validate skill files for compliance and correctness (static / spec / audit) |

### 4. Use Templates for New Documents

Templates are in `.claude/docs/templates/`:

- `constitution-design-document.md` -- game-specific CDD reference for mechanics and systems, including Player Fantasy, Game Feel, and playtest acceptance
- `product-concept.md` -- for initial general product concepts, user journeys, MVP scope, and adoption risks
- `game-design-document.md` -- historical GDD / game-specific reference template
- `architecture-decision-record.md` -- for technical decisions
- `architecture-traceability.md` -- maps CDD requirements to ADRs to story IDs
- `risk-register-entry.md` -- for new risks
- `narrative-character-sheet.md` -- for new characters
- `test-plan.md` -- for feature test plans
- `sprint-plan.md` -- for sprint planning
- `milestone-definition.md` -- for new milestones
- `level-design-document.md` -- for new levels
- `game-pillars.md` -- game-specific core design pillars
- `art-bible.md` -- for visual style reference
- `technical-design-document.md` -- for per-system technical designs
- `post-mortem.md` -- for project/milestone retrospectives
- `sound-bible.md` -- for audio style reference
- `release-checklist-template.md` -- for platform release checklists
- `changelog-template.md` -- for game player-facing patch notes and product changelog/release categories
- `release-notes.md` -- for player-facing release notes
- `incident-response.md` -- for live incident response playbooks
- `game-concept.md` -- for initial game concepts (MDA, SDT, Flow, Bartle)
- `pitch-document.md` -- for pitching the game to stakeholders
- `economy-model.md` -- for virtual economy design (sink/faucet model)
- `faction-design.md` -- for faction identity, lore, and gameplay role
- `module-index.md` -- for systems/modules decomposition and dependency mapping
- `t0/` -- T0 constitutional memory bank templates
- `t1/` -- T1 context and pattern memory bank templates
- `project-stage-report.md` -- for project stage detection output
- `design-doc-from-implementation.md` -- for reverse-documenting existing code into CDDs
- `architecture-doc-from-code.md` -- for reverse-documenting code into architecture docs
- `concept-doc-from-prototype.md` -- for reverse-documenting prototypes into concept docs
- `ux-spec.md` -- for per-screen UX specifications (layout zones, states, events)
- `hud-design.md` -- for whole-game HUD philosophy, zones, and element specs
- `accessibility-requirements.md` -- for project-wide accessibility tier and feature matrix
- `interaction-pattern-library.md` -- for standard UI controls and game-specific patterns
- `player-journey.md` -- for 6-phase emotional arc and retention hooks by time scale
- `difficulty-curve.md` -- for difficulty axes, onboarding ramp, and cross-system interactions
- `test-evidence.md` -- template for recording manual test evidence (screenshots, walkthrough notes)

Also in `.claude/docs/templates/collaborative-protocols/` (used by agents, not typically edited directly):

- `design-agent-protocol.md` -- question-options-draft-approval cycle for design agents
- `implementation-agent-protocol.md` -- story pickup through /story-done cycle for programming agents
- `leadership-agent-protocol.md` -- cross-department delegation and escalation for director-tier agents

### 5. Follow the Coordination Rules

1. Work flows down the hierarchy: Directors -> Leads -> Specialists
2. Conflicts escalate up the hierarchy
3. Cross-department work is coordinated by the `producer`
4. Agents do not modify files outside their domain without delegation
5. All decisions are documented

## First Steps for a New Project

**Don't know where to begin?** Run `/constitute`. It asks where you are, what kind of project you're building, and routes you to the right workflow. No assumptions about your domain or experience level.

If you already know what you need, jump directly to the relevant path:

### Path A: "I have no idea what to build"

1. **Run `/constitute`** (or `/brainstorm open`) — guided onboarding:
   what you want to build, your constraints, your governing principles
   - Establishes your project constitution, then routes to concept exploration
   - For games: produces a game concept document and recommends an engine
2. **Set up the engine** — Run `/setup-engine` (uses the brainstorm recommendation)
   - Configures CLAUDE.md, detects knowledge gaps, populates reference docs
   - Creates `.claude/docs/technical-preferences.md` with naming conventions,
     performance budgets, and engine-specific defaults
   - If the engine version is newer than the LLM's training data, it fetches
     current docs from the web so agents suggest correct APIs
3. **Validate the concept** — Run `/design-review` on your concept document
4. **Decompose into systems** — Run `/map-systems` to map all systems and dependencies
5. **Design each system** — Run `/design-system [system-name]` (or `/map-systems next`)
   to write CDDs in dependency order
6. **Test the core loop** — Run `/prototype [core-mechanic]`
7. **Playtest it** — Run `/playtest-report` to validate the hypothesis
8. **Plan the first sprint** — Run `/sprint-plan new`
9. Start building

### Path B: "I know what I want to build"

If you already have a game concept and engine choice:

1. **Set up the engine** — Run `/setup-engine [engine] [version]`
   (e.g., `/setup-engine godot 4.6`) — also creates technical preferences
2. **Write the Game Pillars** — delegate to `creative-director`
3. **Decompose into systems** — Run `/map-systems` to enumerate systems and dependencies
4. **Design each system** — Run `/design-system [system-name]` for CDDs in dependency order
5. **Create the initial ADR** — Run `/architecture-decision`
6. **Create the first milestone** in `production/milestones/`
7. **Plan the first sprint** — Run `/sprint-plan new`
8. Start building

### Path C: "I know the game but not the engine"

If you have a concept but don't know which engine fits:

1. **Run `/setup-engine`** with no arguments — it will ask about your game's
   needs (2D/3D, platforms, team size, language preferences) and recommend
   an engine based on your answers
2. Follow Path B from step 2 onward

### Path D: "I have an existing project"

If you have design docs, prototypes, or code already:

1. **Run `/constitute`** (or `/project-stage-detect`) — analyzes what exists,
   identifies gaps, establishes governance, and recommends next steps
2. **Run `/adopt`** if you have existing CDDs, ADRs, or stories — audits
   internal format compliance and builds a numbered migration plan to fill gaps
   without overwriting your existing work
3. **Configure engine/stack if needed** — Run `/setup-engine` if not yet configured
4. **Validate phase readiness** — Run `/gate-check` to see where you stand
5. **Plan the next sprint** — Run `/sprint-plan new`

---

## Product Quick-Start Paths `[通用产品]`

The paths above cover game projects. For product projects, use these equivalents:

### Product Path A: "I have no idea what to build"

1. **Run `/constitute`** (or `/brainstorm open`) — guided onboarding:
   choose product domain (API, CLI, web, data pipeline), establish principles
   - Produces a product concept document (JTBD, user psychology, MVP scope)
2. **Set up the stack** — Run `/setup-engine` to pick language + framework
   (e.g., `python 3.13 flask`, `typescript 5 node express`, `rust axum`, `go chi`)
   - Creates technical-preferences.md with naming conventions, performance budgets
3. **Validate the concept** — Run `/design-review` on your product concept
4. **Decompose into modules** — Run `/map-systems` to map all modules and dependencies
5. **Design each module** — Run `/design-system [module-name]` to write CDDs in dependency order
6. **Prototype the riskiest assumption** — Run `/prototype [core-workflow]` (API spike, CLI spike, data pipeline spike, or workflow prototype)
7. **Smoke test / user test** — Validate the hypothesis with real usage data
8. **Plan the first sprint** — Run `/sprint-plan new`
9. Start building

### Product Path B: "I know what I want to build"

If you already have a product concept and stack choice:

1. **Set up the stack** — Run `/setup-engine [lang] [framework]`
   (e.g., `/setup-engine python 3.13 flask`) — also creates technical preferences
2. **Decompose into modules** — Run `/map-systems` to enumerate modules and dependencies
3. **Design each module** — Run `/design-system [module-name]` for CDDs in dependency order
4. **Create the architecture** — Run `/create-architecture` for the master blueprint
5. **Create initial ADRs** — Run `/architecture-decision` for Foundation-layer decisions
6. **Create epics and stories** — Run `/create-epics layer: foundation`, then `layer: core`
7. **Plan the first sprint** — Run `/sprint-plan new`
8. Start building

### Product Path C: "I know the product but not the stack"

If you have a concept but don't know which stack fits:

1. **Run `/setup-engine`** with no arguments — it will ask about your product's
   needs (API/CLI/web, scale expectations, team language preferences) and recommend
   a stack based on your answers
2. Follow Product Path B from step 2 onward

### Product Path D: Shared

Product Path D is identical to the shared Path D above — `/constitute` or
`/project-stage-detect` handles both game and product projects.

## File Structure Reference

```
CLAUDE.md                          -- Master config (read this first, ~60 lines)
.claude/
  settings.json                    -- Claude Code hooks and project settings
  agents/                          -- 53 agent definitions (YAML frontmatter)
  skills/                          -- 73 slash command definitions (YAML frontmatter)
  hooks/                           -- 12 hook scripts (.sh) wired by settings.json
  rules/                           -- 16 path-specific rule files
  docs/
    quick-start.md                 -- This file
    technical-preferences.md       -- Project-specific standards (populated by /setup-engine)
    coding-standards.md            -- Coding and design doc standards
    coordination-rules.md          -- Agent coordination rules
    context-management.md          -- Context budgets and compaction instructions
    directory-structure.md         -- Project directory layout
    workflow-catalog.yaml          -- 7-phase pipeline definition (read by /help)
    setup-requirements.md          -- System prerequisites (Git Bash, jq, Python)
    settings-local-template.md     -- Personal settings.local.json guide
    templates/                     -- 37 document templates
```
