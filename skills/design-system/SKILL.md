---
name: design-system
description: "Use this skill when authoring or retrofitting the CDD for one module listed in design/cdd/module-index.md, including dependencies, behavior, data, edge cases, and acceptance criteria."
argument-hint: "<module-name> [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Task, AskUserQuestion, TodoWrite
---

## User Guide

- When to use: Guided, section-by-section CDD authoring for a single module. Gathers context from existing docs, walks through each required section collaboratively, cross-references dependencies, and writes incrementally to file. Supports both game and general product domains.
- Inputs: Command arguments: `/design-system <module-name> [--review full|lean|solo]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

When this skill is invoked:

**Domain detection.** The concept document reveals the domain:
- **游戏专用**: Read `design/cdd/game-concept.md` — concept contains game-specific sections (Core Loop, MDA analysis, player types) → use game CDD section names (Player Fantasy, Detailed Rules, Formulas, Tuning Knobs, Visual/Audio)
- **通用产品**: Read `design/cdd/product-concept.md` — concept contains product-specific sections (User Journey, JTBD, user personas) → use product CDD section names (User Promise, Detailed Design, Data Model, Configuration, Integration)

Sections below are marked **[通用场景]**, **[游戏专用]**, or **[通用产品]**.

## 1. Parse Arguments & Validate

Resolve the review mode (once, store for all gate spawns this run):
1. If `--review [full|lean|solo]` was passed → use that
2. Else read `production/review-mode.txt` → use that value
3. Else → default to `lean`

See `standards/director-gates.md` for the full check pattern.

A module name or retrofit path is **required**. If missing:

1. Check if `design/cdd/module-index.md` exists.
2. If it exists: read it, find the highest-priority module with status "Not Started" or equivalent, and use `AskUserQuestion`:
   - Prompt: "The next module in your design order is **[module-name]** ([priority] | [layer]). Start designing it?"
   - Options: `[A] Yes — design [module-name]` / `[B] Pick a different module` / `[C] Stop here`
   - If [A]: proceed with that module name. If [B]: ask which module to design (plain text). If [C]: exit.
3. If no module index exists, fail with:
   > "Usage: `/design-system <module-name>` — e.g., `/design-system movement`
   > Or to fill gaps in an existing CDD: `/design-system retrofit design/cdd/[module-name].md`
   > No module index found. Run `/map-systems` first to map your modules and get the design order."

**Detect retrofit mode:**
If the argument starts with `retrofit` or the argument is a file path to an
existing `.md` file in `design/cdd/`, enter **retrofit mode**:

1. Read the existing CDD file.
2. Identify which of the 8 required sections are present (scan for section headings).
   Required sections: Overview, Player Fantasy, Detailed Design/Rules, Formulas,
   Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria.
3. Identify which sections contain only placeholder text (`[To be designed]` or
   equivalent — blank, a single line, or obviously incomplete).
4. Present to the user before doing anything:
   ```
   ## Retrofit: [System Name]
   File: design/cdd/[filename].md

   Sections already written (will not be touched):
   ✓ [section name]
   ✓ [section name]

   Missing or incomplete sections (will be authored):
   ✗ [section name] — missing
   ✗ [section name] — placeholder only
   ```
5. Ask: "Shall I fill the [N] missing sections? I will not modify any existing content."
6. If yes: proceed to **Phase 2 (Gather Context)** as normal, but in **Phase 3**
   skip creating the skeleton (file already exists) and in **Phase 4** skip
   sections that are already complete. Only run the section cycle for missing/
   incomplete sections.
7. **Never overwrite existing section content.** Use Edit tool to replace only
   `[To be designed]` placeholders or empty section bodies.

If NOT in retrofit mode, normalize the system name to kebab-case for the
filename (e.g., "combat system" becomes `combat-system`).

---

## 2. Gather Context (Read Phase)

Read all relevant context **before** asking the user anything. This is the skill's
primary advantage over ad-hoc design — it arrives informed.

### 2a: Required Reads

- **Concept document**: Read the appropriate concept document based on domain:
  - **游戏专用**: Read `design/cdd/game-concept.md`
  - **通用产品**: Read `design/cdd/product-concept.md`
  > If missing: "No concept document found. Run `/brainstorm` first."
- **Module index**: Read `design/cdd/module-index.md` — fail if missing:
  > "No module index found at `design/cdd/module-index.md`. Run `/map-systems` first to map your modules."
- **Target system**: Find the system in the index. If not listed, warn:
  > "[system-name] is not in the module index. Would you like to add it, or
  > design it as an off-index system?"
- **Entity registry**: Read `design/registry/entities.yaml` if it exists.
  Extract all entries referenced by or relevant to this system (grep
  `referenced_by.*[system-name]` and `source.*[system-name]`). Hold these
  in context as **known facts** — values that other CDDs have already
  established and this CDD must not contradict.
- **Reflexion log**: Read `docs/consistency-failures.md` if it exists.
  Extract entries whose Domain matches this system's category. These are
  recurring conflict patterns — present them under "Past failure patterns"
  in the Phase 2d context summary so the user knows where mistakes have
  occurred before in this domain.

### 2b: Dependency Reads

From the module index, identify:
- **Upstream dependencies**: Systems this one depends on. Read their CDDs if they
  exist (these contain decisions this system must respect).
- **Downstream dependents**: Systems that depend on this one. Read their CDDs if
  they exist (these contain expectations this system must satisfy).

For each dependency CDD that exists, extract and hold in context:
- Key interfaces (what data flows between the systems)
- Formulas that reference this system's outputs
- Edge cases that assume this system's behavior
- Tuning knobs that feed into this system

### 2c: Optional Reads

- **Game pillars**: Read `design/cdd/game-pillars.md` if it exists
- **Existing CDD**: Read `design/cdd/[system-name].md` if it exists (resume, don't
  restart from scratch)
- **Related CDDs**: Glob `design/cdd/*.md` and read any that are thematically related
  (e.g., if designing a system that overlaps with another in scope, read the related CDD
  even if it's not a formal dependency)

### 2d: Present Context Summary

Before starting design work, present a brief summary to the user:

> **Designing: [System Name]**
> - Priority: [from index] | Layer: [from index]
> - Depends on: [list, noting which have CDDs vs. undesigned]
> - Depended on by: [list, noting which have CDDs vs. undesigned]
> - Existing decisions to respect: [key constraints from dependency CDDs]
> - Pillar alignment: [which pillar(s) this system primarily serves]
> - **Known cross-system facts (from registry):**
>   - [entity_name]: [attribute]=[value], [attribute]=[value] (owned by [source CDD])
>   - [item_name]: [attribute]=[value], [attribute]=[value] (owned by [source CDD])
>   - [formula_name]: variables=[list], output=[min–max] (owned by [source CDD])
>   - [constant_name]: [value] [unit] (owned by [source CDD])
>   *(These values are locked — if this CDD needs different values, surface
>   the conflict before writing. Do not silently use different numbers.)*
>
> If no registry entries are relevant: omit the "Known cross-system facts" section.

If any upstream dependencies are undesigned, warn:
> "[dependency] doesn't have a CDD yet. We'll need to make assumptions about
> its interface. Consider designing it first, or we can define the expected
> contract and flag it as provisional."

### 2e: Technical Feasibility Pre-Check

Before asking the user to begin designing, load technology context and surface
any constraints or knowledge gaps that will shape the design. Use the detected
domain from Phase 2.

**[游戏专用] Step 1 — Determine the engine domain for this system:**
Map the system's category (from `module-index.md`) to an engine domain:

| System Category | Engine Domain |
|----------------|--------------|
| Combat, physics, collision | Physics |
| Rendering, visual effects, shaders | Rendering |
| UI, HUD, menus | UI |
| Audio, sound, music | Audio |
| AI, pathfinding, behavior trees | Navigation / Scripting |
| Animation, IK, rigs | Animation |
| Networking, multiplayer, sync | Networking |
| Input, controls, keybinding | Input |
| Save/load, persistence, data | Core |
| Dialogue, quests, narrative | Scripting |

**[通用产品] Step 1 — Determine the stack domain for this module:**
Map the module's category (from `module-index.md`) to a stack domain:

| Module Category | Stack Domain |
|----------------|--------------|
| Foundation/Infrastructure, config, logging, error handling | Framework / Runtime |
| API, web services, request handling | API Design / Framework |
| Data models, schemas, storage | Data Storage / ORM |
| Auth, permissions, security | Auth / Security |
| UI, frontend, user-facing interfaces | Frontend / UI |
| CLI, tooling, developer-facing | CLI / Distribution |
| Data pipelines, ETL, analytics | Data Pipeline / Analytics |
| Integration, webhooks, third-party APIs | Integration / Messaging |
| Performance, caching, optimization | Performance / Caching |

**[游戏专用] Step 2 — Read engine context (if available):**
- Read `standards/technical-preferences.md` to identify the engine and version
- If engine is configured, read `docs/engine-reference/[engine]/VERSION.md`
- Read `docs/engine-reference/[engine]/modules/[domain].md` if it exists
- Read `docs/engine-reference/[engine]/breaking-changes.md` for domain-relevant entries
- Glob `docs/architecture/adr-*.md` and read any ADRs whose domain matches
  (check the Engine Compatibility table's "Domain" field)

**[通用产品] Step 2 — Read stack context (if available):**
- Read `standards/technical-preferences.md` to identify the language, framework,
  runtime, database, and pinned versions
- If stack reference docs are configured, read `docs/reference/[stack]/VERSION.md`
- Read `docs/reference/[stack]/modules/[domain].md` if it exists
- Read `docs/reference/[stack]/breaking-changes.md` for domain-relevant entries
- Glob `docs/architecture/adr-*.md` and read any ADRs whose domain matches
  (check the Technology Compatibility table's "Domain" field)

**Step 3 — Present the Feasibility Brief:**

**[游戏专用]** If engine reference docs exist, present before starting design:

```
## Technical Feasibility Brief: [System Name]
Engine: [name + version]
Domain: [domain]

### Known Engine Capabilities (verified for [version])
- [capability relevant to this system]
- [capability 2]

### Engine Constraints That Will Shape This Design
- [constraint from engine-reference or existing ADR]

### Knowledge Gaps (verify before committing to these)
- [post-cutoff feature this design might rely on — mark HIGH/MEDIUM risk]

### Existing ADRs That Constrain This System
- ADR-XXXX: [decision summary] — means [implication for this CDD]
  (or "None yet")
```

**[通用产品]** If stack reference docs exist, present before starting design:

```
## Technical Feasibility Brief: [Module Name]
Stack: [language] + [framework/runtime] [version]
Domain: [domain]

### Known Stack Capabilities (verified for [version])
- [capability relevant to this module]
- [capability 2]

### Stack Constraints That Will Shape This Design
- [constraint from stack reference or existing ADR]

### Knowledge Gaps (verify before committing to these)
- [post-cutoff framework/API behavior this design might rely on — mark HIGH/MEDIUM risk]

### Existing ADRs That Constrain This Module
- ADR-XXXX: [decision summary] — means [implication for this CDD]
  (or "None yet")
```

**[游戏专用]** If no engine reference docs exist (engine not yet configured), show a short note:
> "No engine configured yet — skipping technical feasibility check. Run
> `/setup-engine` before moving to architecture if you haven't already."

**[通用产品]** If no stack reference docs exist (stack not yet configured), show a short note:
> "No technology stack configured yet — skipping technical feasibility check. Run
> `/setup-engine` before moving to architecture if you haven't already."

**Step 4 — Ask before proceeding:**

Use `AskUserQuestion`:
- "Any constraints to add before we begin, or shall we proceed with these noted?"
  - Options: "Proceed with these noted", "Add a constraint first", "I need to check the technology docs — pause here"

---

Use `AskUserQuestion`:
- "Ready to start designing [system-name]?"
  - Options: "Yes, let's go", "Show me more context first", "Design a dependency first"

---

## 3. Create File Skeleton

Once the user confirms, **immediately** create the CDD file with empty section
headers. This ensures incremental writes have a target.

Use the inline skeleton below. Do not read an external CDD template file here;
the former external game design document template has been folded into this skill.

```markdown
# [System Name]

> **Status**: In Design
> **Author**: [user + agents]
> **Last Updated**: [today's date]
> **Implements Pillar**: [from context]

## Overview

[To be designed]

## Player Fantasy

[To be designed]

## Detailed Design

### Core Rules

[To be designed]

### States and Transitions

[To be designed]

### Interactions with Other Systems

[To be designed]

## Formulas

[To be designed]

## Edge Cases

[To be designed]

## Dependencies

[To be designed]

## Tuning Knobs

[To be designed]

## Visual/Audio Requirements

[To be designed]

## UI Requirements

[To be designed]

## Acceptance Criteria

```

[Product] For product CDDs, use this skeleton instead of the game skeleton above:

```markdown
# [Module Name]

> **Status**: In Design

## Overview
[To be designed]

## User Promise
[To be designed]

## Detailed Design
### Core Specification
[To be designed]
### States and Transitions
[To be designed]
### Interactions with Other Modules
[To be designed]

## Data Model
[To be designed]

## Edge Cases
[To be designed]

## Dependencies
[To be designed]

## Configuration
[To be designed]

## Integration Requirements
[To be designed]

## UI Requirements
[To be designed]

## Acceptance Criteria

[To be designed]

## Open Questions

[To be designed]
```

Ask: "May I create the skeleton file at `design/cdd/[system-name].md`?"

After writing, update `production/session-state/active.md`:
- Use Glob to check if the file exists.
- If it **does not exist**: use the **Write** tool to create it. Never attempt Edit on a file that may not exist.
- If it **already exists**: use the **Edit** tool to update the relevant fields.

File content:
- Task: Designing [system-name] CDD
- Current section: Starting (skeleton created)
- File: design/cdd/[system-name].md

---

## 4. Section-by-Section Design

Walk through each section in order. For **each section**, follow this cycle:

### The Section Cycle

```
Context  ->  Questions  ->  Options  ->  Decision  ->  Draft  ->  Approval  ->  Write
```

1. **Context**: State what this section needs to contain, and surface any relevant
   decisions from dependency CDDs that constrain it.

2. **Questions**: Ask clarifying questions specific to this section. Use
   `AskUserQuestion` for constrained questions, conversational text for open-ended
   exploration.

3. **Options**: Where the section involves design choices (not just documentation),
   present 2-4 approaches with pros/cons. Explain reasoning in conversation text,
   then use `AskUserQuestion` to capture the decision.

4. **Decision**: User picks an approach or provides custom direction.

5. **Draft**: Write the section content in conversation text for review. Flag any
   provisional assumptions about undesigned dependencies.

6. **Approval**: Immediately after the draft — in the SAME response — use
   `AskUserQuestion`. **NEVER use plain text. NEVER skip this step.**
   - Prompt: "Approve the [Section Name] section?"
   - Options: `[A] Approve — write it to file` / `[B] Make changes — describe what to fix` / `[C] Start over`

   **The draft and the approval widget MUST appear together in one response.**
   If the draft appears without the widget, the user is left at a blank prompt
   with no path forward — this is a protocol violation.

****

7. **Write**: Use the Edit tool to replace the placeholder with the approved content.
   **CRITICAL**: Always include the section heading in the `old_string` to ensure
   uniqueness — never match `[To be designed]` alone, as multiple sections use the
   same placeholder and the Edit tool requires a unique match. Use this pattern:
   ```
   old_string: "## [Section Name]\n\n[To be designed]"
   new_string: "## [Section Name]\n\n[approved content]"
   ```
   Confirm the write.

8. **Registry conflict check** (Sections C and D only — Detailed Design and Formulas):
   After writing, scan the section content for entity names, item names, formula
   names, and numeric constants that appear in the registry. For each match:
   - Compare the value just written against the registry entry.
   - If they differ: **surface the conflict immediately** before starting the next
     section. Do not continue silently.
     > "Registry conflict: [name] is registered in [source CDD] as [registry_value].
     > This section just wrote [new_value]. Which is correct?"
   - If new (not in registry): flag it as a candidate for registry registration
     (will be handled in Phase 5).

After writing each section, update `production/session-state/active.md` with the
completed section name. Use Glob to check if the file exists — use Write to create
it if absent, Edit to update it if present.

### Section-Specific Guidance

Before drafting each Phase 4 section, read the matching heading in [section guidance](references/section-guidance.md). Load only the current section and detected domain branch. Its delegation, cross-reference, completion-format, and approval requirements are mandatory.

## 5. Post-Design Validation

After all sections are written:

### 5a: Self-Check

Read back the complete CDD from file (not from conversation memory — the file is
the source of truth). Verify:
- All 8 required sections have real content (not placeholders)
- Formulas reference defined variables
- Edge cases have resolutions
- Dependencies are listed with interfaces
- Acceptance criteria are testable

### 5a-bis: Creative Director Pillar Review

**Review mode check** — apply before spawning CD-GDD-ALIGN:
- `solo` → skip. Note: "CD-GDD-ALIGN skipped — Solo mode." Proceed to Step 5b.
- `lean` → skip (not a PHASE-GATE). Note: "CD-GDD-ALIGN skipped — Lean mode." Proceed to Step 5b.
- `full` → spawn as normal.

Before finalizing the CDD, spawn `creative-director` via Task using gate **CD-GDD-ALIGN** (`standards/director-gates.md`).

Pass: completed CDD file path, project pillars/principles (from `design/cdd/game-concept.md`, `design/cdd/product-concept.md`, or `design/cdd/principles.md` if present).
- **[游戏专用]** MDA aesthetics target.
- **[通用产品]** User promise target from product concept.

Handle verdict per the standard rules in `director-gates.md`. After resolution, record the verdict in the CDD Status header:
`> **Creative Director Review (CD-GDD-ALIGN)**: APPROVED [date] / CONCERNS (accepted) [date] / REVISED [date]`

---

### 5b: Update Entity Registry

Scan the completed CDD for cross-system facts that should be registered:
- Named entities (enemies, NPCs, bosses) with stats or drops
- Named items with values, weights, or categories
- Named formulas with defined variables and output ranges
- Named constants referenced by value in more than one place

For each candidate, check if it already exists in `design/registry/entities.yaml`:
```
Grep pattern="  - name: [candidate_name]" path="design/registry/entities.yaml"
```

Present a summary:
```
Registry candidates from this CDD:
  NEW (not yet registered):
    - [entity_name] [entity]: [attribute]=[value], [attribute]=[value]
    - [item_name] [item]: [attribute]=[value], [attribute]=[value]
    - [formula_name] [formula]: variables=[list], output=[min–max]
  ALREADY REGISTERED (referenced_by will be updated):
    - [constant_name] [constant]: value=[N] ← matches registry ✅
```

Ask: "May I update `design/registry/entities.yaml` with these [N] new entries
and update `referenced_by` for the existing entries?"

If yes: append new entries and update `referenced_by` arrays. Never modify
existing `value` / attribute fields without surfacing it as a conflict first.

### 5c: Offer Design Review

Present a completion summary:

> **CDD Complete: [System Name]**
> - Sections written: [list]
> - Provisional assumptions: [list any assumptions about undesigned dependencies]
> - Cross-system conflicts found: [list or "none"]

> **To validate this CDD, open a fresh Claude Code session and run:**
> `/design-review design/cdd/[system-name].md`
>
> **Never run `/design-review` in the same session as `/design-system`.** The reviewing
> agent must be independent of the authoring context. Running it here would inherit
> the full design history, making independent critique impossible.

**NEVER offer to run `/design-review` inline.** Always direct the user to a fresh window.

### 5d: Update Module Index

After the CDD is complete (and optionally reviewed):

- Read the module index
- Update the target system's row:
  - If design-review was run and verdict is APPROVED: Status → "Approved"
  - If design-review was run and verdict is NEEDS REVISION: Status → "In Review"
  - If design-review was skipped: Status → "Designed" (pending review)
  - If the user chose "I'll review it myself first": Status → "Designed"
  - Design Doc: link to `design/cdd/[system-name].md`
- Update the Progress Tracker counts

Ask: "May I update the module index at `design/cdd/module-index.md`?"

### 5d: Update Session State

Update `production/session-state/active.md` with:
- Task: [system-name] CDD
- Status: Complete (or In Review if design-review was run)
- File: design/cdd/[system-name].md
- Sections: All 8 written
- Next: [suggest next system from design order]

### 5e: Suggest Next Steps

Use `AskUserQuestion`:
- "What's next?"
  - Options:
    - "Run `/consistency-check` — verify this CDD's values don't conflict with existing CDDs (recommended before designing the next system)"
    - "Design next system ([next-in-order])" — if undesigned systems remain
    - "Fix review findings" — if design-review flagged issues
    - "Stop here for this session"
    - "Run `/gate-check`" — if enough MVP systems are designed

---

## 6. Specialist Agent Routing

Before delegating a section, read the matching domain and module category in [specialist routing](references/specialist-routing.md). Load only the applicable routing row. Specialists return proposals to the main session and never write project files directly.

## 7. Recovery & Resume

If the session is interrupted (compaction, crash, new session):

1. Read `production/session-state/active.md` — it records the current system and
   which sections are complete
2. Read `design/cdd/[system-name].md` — sections with real content are done;
   sections with `[To be designed]` still need work
3. Resume from the next incomplete section — no need to re-discuss completed ones

This is why incremental writing matters: every approved section survives any
disruption.

---

## Collaborative Protocol

This skill follows the collaborative design principle at every step:

1. **Question -> Options -> Decision -> Draft -> Approval** for every section
2. **AskUserQuestion** at every decision point (Explain -> Capture pattern):
   - Phase 2: "Ready to start, or need more context?"
   - Phase 3: "May I create the skeleton?"
   - Phase 4 (each section): Design questions, approach options, draft approval
   - Phase 5: "Run design review? Update module index? What's next?"
3. **"May I write to [filepath]?"** before the skeleton and before each section write
4. **Incremental writing**: Each section is written to file immediately after approval
5. **Session state updates**: After every section write
6. **Cross-referencing**: Every section checks existing CDDs for conflicts
7. **Specialist routing**: Complex sections get expert agent input, presented to
   the user for decision — never written silently

**Never** auto-generate the full CDD and present it as a fait accompli.
**Never** write a section without user approval.
**Never** contradict an existing approved CDD without flagging the conflict.
**Always** show where decisions come from (dependency CDDs, pillars, user choices).

## Context Window Awareness

This is a long-running skill. After writing each section, check if the status line
shows context at or above 70%. If so, append this notice to the response:

> **Context is approaching the limit (≥70%).** Your progress is saved — all approved
> sections are written to `design/cdd/[system-name].md`. When you're ready to continue,
> open a fresh Claude Code session and run `/design-system [system-name]` — it will
> detect which sections are complete and resume from the next one.

---

## Recommended Next Steps

- Run `/design-review design/cdd/[system-name].md` in a **fresh session** to validate the completed CDD independently
- Run `/consistency-check` to verify this CDD's values don't conflict with other CDDs
- Run `/map-systems next` to move to the next highest-priority undesigned system
- Run `/review-all-gdds`, then `/gate-check systems-design` when all MVP CDDs are authored and reviewed
