# Technical Preferences

<!-- Populated by /setup-engine. Updated as the user makes decisions throughout development. -->
<!-- All agents reference this file for project-specific standards and conventions. -->

## Domain and capability evidence

Read concept bodies, explicit project decisions and actual configured fields.
Filenames, placeholders, copied templates and source counts do not establish
a domain. Record Game, Product or Unknown for the current scope with its actual
source. Conflicting concept bodies or mixed-domain scope require a concrete Game
or Product selection before dependent single-domain routing. Report the actual
scope; do not invent a Both project-domain route or infer qualified completion.
Without a concept, legacy Game compatibility needs actual configured engine/domain
and Game behavior evidence; actual configured Product remains Product. Unknown
blocks domain-dependent routing while independent neutral reporting continues.

Read valid populated legacy Product sections as substantive aliases:
`Language & Framework` supplies language, framework and runtime choices;
`Platform & Deployment` supplies targets and deployment;
`Agent Routing` and its `File Extension Routing` supply specialist routing.
Resolve each table in its owning domain context, not by extension alone.
These existing sections are written by `skills/setup-engine/SKILL.md` and
`skills/setup-engine/references/technical-preferences.md`. `Product Stack` is
a parallel format, not a requirement to relocate or overwrite them. Compare
actual values across aliases, concept and new fields; conflicts block the
affected route, while placeholders establish no configured fact. Actual
configured legacy Product facts can support Product routing without a concept.

Resolve capabilities from the owning CDD/Story, configured target platforms/input
methods and Product surface profile. API/CLI/data/auth/UI/jobs rules apply to
actual surfaces; Game-only engine/gameplay/scene/frame constraints apply where
those capabilities exist. Record justified N/A with its owner.

Configured references (`docs/engine-reference/[engine]/VERSION.md` for Game;
`docs/reference/[stack]/VERSION.md` for Product) identify intended versions, not
installed tools or executed verification. Missing references leave affected
version checks incomplete. Read actual runtime metadata and `adapters/README.md`
or the existing T2 framework contract before supported-behavior claims.
Definitions, generated copies and CLI help do not prove autoload, agent execution
or qualification. Do not install/activate a runtime while diagnosing facts.

## Engine & Language [Game]

- **Engine**: [TO BE CONFIGURED — run /setup-engine]
- **Language**: [TO BE CONFIGURED]
- **Rendering**: [TO BE CONFIGURED]
- **Physics**: [TO BE CONFIGURED]

## Input & Platform [Game]

<!-- Written by /setup-engine. Read by /ux-design, /ux-review, /test-setup, /team-ui, and /dev-story -->
<!-- to scope interaction specs, test helpers, and implementation to the correct input methods. -->

- **Target Platforms**: [TO BE CONFIGURED — e.g., PC, Console, Mobile, Web]
- **Input Methods**: [TO BE CONFIGURED — e.g., Keyboard/Mouse, Gamepad, Touch, Mixed]
- **Primary Input**: [TO BE CONFIGURED — the dominant input for this game]
- **Gamepad Support**: [TO BE CONFIGURED — Full / Partial / None]
- **Touch Support**: [TO BE CONFIGURED — Full / Partial / None]
- **Platform Notes**: [TO BE CONFIGURED — any platform-specific UX constraints]

## Product Stack [Product]

- **Language / Version**: [TO BE CONFIGURED — run /setup-engine]
- **Framework / Runtime**: [TO BE CONFIGURED]
- **Build / Package Tools**: [TO BE CONFIGURED]
- **Database / Queue / Storage**: [TO BE CONFIGURED or justified N/A]
- **Deployment Targets / Environments**: [TO BE CONFIGURED]
- **API / CLI / SDK / UI / Data / Auth Surfaces**: [TO BE CONFIGURED; owning CDD/surface profile]
- **Version Reference**: [TO BE CONFIGURED — docs/reference/<stack>/VERSION.md]
- **Language / Framework Specialists**: [TO BE CONFIGURED; actual supported routing]
- **Service / Workflow Budgets**: [TO BE CONFIGURED — latency, throughput, memory, retries as applicable]

## Naming Conventions

- **Classes**: [TO BE CONFIGURED]
- **Variables**: [TO BE CONFIGURED]
- **Signals/Events**: [TO BE CONFIGURED]
- **Files**: [TO BE CONFIGURED]
- **Scenes/Prefabs [Game]**: [TO BE CONFIGURED]
- **Constants**: [TO BE CONFIGURED]

## Performance Budgets [Game]

- **Target Framerate**: [TO BE CONFIGURED]
- **Frame Budget**: [TO BE CONFIGURED]
- **Draw Calls**: [TO BE CONFIGURED]
- **Memory Ceiling**: [TO BE CONFIGURED]

## Testing

- **Framework**: [TO BE CONFIGURED]
- **Minimum Coverage**: [TO BE CONFIGURED]
- **Required Tests [Game]**: Balance formulas, gameplay systems, networking (if applicable)
- **Required Tests [Product]**: Actual API/CLI/SDK contracts, auth boundaries,
  data/migration and workflow behavior required by the owning CDD/Story.
  Coverage targets need a configured rationale and denominator; no blanket
  per-file 100% policy or execution proof from test counts is implied.

## Forbidden Patterns

<!-- Add patterns that should never appear in this project's codebase -->
- [None configured yet — add as architectural decisions are made]

## Allowed Libraries / Addons

<!-- Add approved third-party dependencies here -->
- [None configured yet — add as dependencies are approved]

## Architecture Decisions Log

<!-- Quick reference linking to full ADRs in docs/architecture/ -->
- [No ADRs yet — use /architecture-decision to create one]

## Engine Specialists [Game]

<!-- Written by /setup-engine when engine is configured. -->
<!-- Read by /code-review, /architecture-decision, /architecture-review, and team skills -->
<!-- to know which specialist to spawn for engine-specific validation. -->

- **Primary**: [TO BE CONFIGURED — run /setup-engine]
- **Language/Code Specialist**: [TO BE CONFIGURED]
- **Shader Specialist**: [TO BE CONFIGURED]
- **UI Specialist**: [TO BE CONFIGURED]
- **Additional Specialists**: [TO BE CONFIGURED]
- **Routing Notes**: [TO BE CONFIGURED]

### File Extension Routing

<!-- Skills use this table to select the right specialist per file type. -->
<!-- Unconfigured routing is reported; do not invent a specialist or completed invocation. -->

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (primary language) | [TO BE CONFIGURED] |
| Shader / material files | [TO BE CONFIGURED] |
| UI / screen files | [TO BE CONFIGURED] |
| Scene / prefab / level files | [TO BE CONFIGURED] |
| Native extension / plugin files | [TO BE CONFIGURED] |
| General architecture review | Primary |

Product routing uses configured language/framework specialists for actual
API/CLI/service/data/auth/UI capabilities. Keep the Game extension table above;
do not select an engine specialist from a shared extension alone or require
database/UI/queue capabilities that a Product lacks.
