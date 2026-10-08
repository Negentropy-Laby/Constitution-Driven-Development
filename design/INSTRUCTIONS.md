# Design Directory

When authoring or editing files in this directory, follow these standards.

## CDD Files (`design/cdd/`)

First resolve document kind through the owner routing below, then identify its domain:
- **Game** CDDs usually sit beside `design/cdd/game-concept.md` and describe
  mechanics, systems, levels, economy, narrative, UI/HUD, or player-facing
  behavior.
- **Product** CDDs usually sit beside `design/cdd/product-concept.md` and
  describe API, CLI, web/app, library, data, migration, service, or operational
  workflows.

Every **Game module** CDD must include all **8 required sections** in this order:
1. Overview — one-paragraph summary
2. Player Fantasy — intended feeling and experience
3. Detailed Rules — unambiguous mechanics
4. Formulas — all math defined with variables
5. Edge Cases — unusual situations handled
6. Dependencies — other systems listed
7. Tuning Knobs — configurable values identified
8. Acceptance Criteria — testable success conditions

Every **Product module** CDD must include the equivalent **8 required sections**:
1. Overview — one-paragraph summary of the module or workflow
2. User Promise / JTBD — what the user is trying to accomplish
3. Detailed Behavior — API, CLI, UI, data, library, or integration behavior
4. Contracts / Data Model — schemas, inputs, outputs, errors, exit codes, migrations
5. Edge Cases — invalid input, permissions, retries, partial failure, rollback
6. Dependencies — upstream/downstream modules, services, packages, docs
7. Configuration Knobs — environment variables, feature flags, limits, defaults
8. Acceptance Criteria — contract, workflow, migration, docs, observability checks

## Document-kind routing

Resolve kind using actual generating workflow/provenance, declared purpose and
the full body; filename/location alone does not make every `design/cdd/*.md` a
module CDD. Record kind, domain and required-set owner in the review. Existing
headings/numbering/aliases remain valid when substantive bodies cover the owner's
roles. No kind is exempt from full body reading and required reference closure.

- **Module CDD:** `/design-system` module/retrofit/sync output specifies one
  system/module's detailed behavior; use this file's Game/Product semantic eight.
- **Game Concept:** `skills/brainstorm/SKILL.md`'s Game generation workflow plus
  `templates/game-concept.md` jointly own the required set. Read both actual
  bodies, including workflow-added requirements beyond the template. Require
  meaningful Elevator Pitch, Core
  Identity, Core Fantasy, Unique Hook, Player Experience Analysis (MDA Framework),
  Player Motivation Profile, Core Loop, Game Pillars, Inspiration and References,
  Target Player Profile, Technical Considerations, Risks and Open Questions,
  MVP Definition and Next Steps, including required subroles/tables. The actual
  /brainstorm workflow additionally requires **Visual Identity Anchor** for Game:
  selected direction, one-line visual rule, supporting principles and design
  philosophy summary, even though the Game template lacks that heading. It need not
  invent module Formulas/Tuning Knobs merely to satisfy Module8.
- **Product Concept:** `skills/brainstorm/SKILL.md`'s Product generation workflow
  plus `templates/product-concept.md` jointly own the required set. Read both
  actual bodies and workflow-added requirements; require substantive Core Identity, Discovery
  Brief, User Journey, User Motivation Analysis, Principles, Visual Identity
  Anchor, Target Users, Scope, Risks and Next Steps, including required
  subroles/tables; use its JTBD, MVP/Full Vision and compatibility scope as written.
- **Quick Spec:** the category and inline format in `skills/quick-design/SKILL.md`
  own requirements. Tuning needs Change, Tuning Knob Mapping and Acceptance
  Criteria; Tweak/Addition needs Change Summary, Motivation, Design Delta, New
  Rules/Values, Affected Systems, Acceptance Criteria and CDD Update Required;
  New Small System needs Overview, Core Rules, Tuning Knobs, Acceptance Criteria
  and Systems Index disposition. Product quick specs need Change Summary, Product
  Motivation, Contract/Workflow Delta, Public Surface Impact, Compatibility and
  Migration, Acceptance Criteria and CDD/ADR/Docs Update Required, plus that
  category's metadata/source requirements. Read the actual applicable format;
  its lightweight pipeline does not remove required behavior/evidence.
- **Module Index:** `skills/map-systems/SKILL.md` and `templates/module-index.md`
  own requirements: Overview, Module Enumeration, Categories, Priority Tiers,
  Dependency Map, Recommended Design Order, Circular Dependencies, High-Risk
  Modules, Progress Tracker and Next Steps with real rows, rationale and source
  concept. It is not an individual module CDD.
- **Other/unknown:** resolve an actual governing workflow/template and required
  set before a completeness verdict. Ask for missing kind/owner information;
  never default to Module8 or pass an unknown kind. Continue independent checks
  while the affected classification/qualification remains incomplete.

These are owner routes, not a second schema or a frozen copy of the templates.
Read the current generating workflow and template bodies, combine applicable
workflow-added requirements with the template set, follow required references
and bind all owner identities; template headings alone cannot certify coverage. Missing
required owner/input or placeholder content prevents a complete passing claim.
Apply kind-appropriate consistency, feasibility and design alignment checks
without fabricating formulas or code-level contracts for a concept.

## Semantic eight-section contract

This file owns the eight semantic roles above for module CDD authoring/review.
Apply other document kinds' actual owner requirements below. Keep the established
order for new module CDDs. Existing numbered sections, translations
and aliases remain valid when their actual body covers the role: Game `Detailed
Design / Core Rules` can cover Detailed Rules; Product `User Promise` or `JTBD`,
`Detailed Design`, `Data Model / Contracts` and `Configuration` can cover their
corresponding roles. Map roles to actual paths/headings/subsections in the review.
One section may contain several roles; do not count a heading twice without
distinct substantive content. Extra Integration/UI/Open Questions sections are
retained and do not replace missing core roles.

Read the actual body and required references. A header, TODO, example scaffold,
`[To be designed]`, unexplained value, vague acceptance statement or stale link is
not substantive coverage. Judge whether the content states the actual domain
behavior, rules/contracts, variables, outcomes, dependencies, knobs and testable
success conditions. A concise complete section may pass; line/word counts cannot
decide completeness. A genuinely inapplicable role needs an explicit rationale
and governing-owner decision, not an empty section silently counted complete.
An unresolved required dependency makes the affected role incomplete.

New documents may start with an authorized skeleton. Retrofit/synchronization
preserves existing prose, examples, aliases and unaffected decisions, changing
only named gaps or approved affected sections. Follow `standards/evidence-lifecycle.md`
and `standards/notes-adr-sync.md` for continuing scope, exact evidence and separate
authority. Keep observed As-Is, governing Target, discrepancies and actions
distinct; missing implementation is a gap against Target, not permission to
reduce it. Record completeness, consistency, runtime checks, independent review,
write approval and completion separately.

**File naming:** `[system-or-module-slug].md` (e.g. `movement-system.md`,
`combat-system.md`, `imports-api.md`, `reporting-cli.md`)

**Module index:** `design/cdd/module-index.md` — include its path and update effect
in the authorized changeset when adding a Game system or Product module CDD.

**Design order:** Foundation → Core → Feature → Presentation → Polish

**Validation:** Recommend `/design-review [path]` after authoring or synchronizing
a CDD and `/review-all-gdds` after a related batch. Run them when the existing
scope includes review or the user selects it; document writing does not itself
establish a review verdict.

## Quick Specs (`design/quick-specs/`)

Lightweight specs for tuning changes, minor mechanics, or balance adjustments.
For Product projects, also use quick specs for small API response changes, CLI
flag behavior, config defaults, copy/help text, docs-only updates, or isolated
workflow adjustments. Use `/quick-design` to author.

## UX Specs (`design/ux/`)

- Per-screen specs: `design/ux/[screen-name].md`
- HUD design: `design/ux/hud.md`
- Interaction pattern library: `design/ux/interaction-patterns.md`
- Accessibility requirements: `design/ux/accessibility-requirements.md`
- Product workflow specs: `design/ux/[workflow-name].md`
- Product API/CLI consumer journey specs: `design/ux/[surface]-journey.md`

Use `/ux-design` to author. Validate with `/ux-review` before passing Game
UI/HUD work or Product web/API/CLI workflow work to `/team-ui`.
