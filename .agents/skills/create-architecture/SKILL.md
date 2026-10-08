---
name: create-architecture
description: "Use this skill when approved module CDDs and ADRs must be synthesized into the master architecture document before implementation begins."
argument-hint: "[focus-area: full | layers | data-flow | api-boundaries | adr-audit] [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Bash, AskUserQuestion, Task
agent: technical-director
---

## Scope, decisions and exact evidence

Read `standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` from the
project root. Reuse original authorization only for its exact named paths, effects
and limits across roles/retries. Content agreement, writes, independent review,
ADR acceptance and Story/phase completion remain separate. Show a concrete draft
before asking about unresolved material choices or new effects; covered writes
need no repeated per-file or per-role permission.

Read/review-only never invokes a write entrypoint, including in memory. Report-only
may write its assigned new report, not inputs, indexes, session state, logs or T3
pointers. Each other effect needs existing scope or separate changeset authority.
No Memory Bank means the existing Story/review/conversation fallback, not activation.

Bind claims to original paths, full SHA-256 (64 hex), byte sizes, collection time
with timezone, source commit plus exact uncommitted/ignored/external identities.
Read actual bodies and minimum required direct/indirect evidence closure; retain
recoverable originals and disclose missing inputs. Resolve CDD DocKind/required
owner set and module semantic eight through `design/INSTRUCTIONS.md`, preserving
substantive aliases; headings, counts or existence cannot establish PASS.

Classify each meaningful choice as `covered`, `cdd-layer`, `no-adr`,
`documentation-update`, `adr-required` or `conflict`, with named requirement/owner,
existing TR-ID if assigned, exact Accepted ADR revision/section/scope or justified
no-ADR reason, affected paths/dependencies, evidence and action/owner/due phase.
Trust boundaries, public contracts, durable formats, state ownership and governing
architectural constraints require an Accepted decision or valid scoped exception
under existing governance before affected implementation starts/continues. Continue
independent work. Proposed, implemented, green tests, write approval and director
recommendations do not establish acceptance; historical approval needs exact input
and authority/scope match. Justified `cdd-layer`/`no-adr` waives no other readiness,
manifest or evidence prerequisite. The existing global Technical Setup minimum of
three Foundation ADRs in `workflow/workflow-catalog.yaml` remains a separate gate:
do not bypass it or manufacture ADRs to meet a count.

Absent, conflicting or ambiguous concept/domain evidence means Unknown. Continue
domain-independent checks; resolve the domain before applying its Game/Product
rules. Do not silently default to Game.

## User Guide

- When to use: Guided, section-by-section authoring of the master architecture document. Reads all CDDs, the module index, existing ADRs, and the reference library to produce a complete architecture blueprint before any code is written. Supports both game and general product domains.
- Inputs: Command arguments: `/create-architecture [focus-area: full | layers | data-flow | api-boundaries | adr-audit] [--review full|lean|solo]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Create Architecture

This skill produces `docs/architecture/architecture.md` — the master architecture
document that translates all approved CDDs into a concrete technical blueprint.
It sits between design and implementation, and must exist before sprint planning begins.

**Distinct from `/architecture-decision`**: ADRs record individual point decisions.
This skill creates the whole-system blueprint that gives ADRs their context.

Resolve the review mode once and store it for all gate spawns this run:
1. If `--review` was passed, require an explicit value of `full`, `lean` or `solo`.
2. Else read the actual `production/review-mode.txt` if present and require its
   value to be `full`, `lean` or `solo`.
3. Only when neither override nor global file is present, default to `lean`.

A missing/invalid explicit value or invalid selected global value requires correction
before gate dispatch. Report the actual source/value error; never silently fall back,
claim a skipped/completed gate, or infer approval from invalid mode input.
A valid explicit override takes precedence over the global file. Resolve only once.
See `standards/director-gates.md` for the full check pattern.

**Domain detection.** The concept document at `design/cdd/` reveals the domain:
- **游戏专用**: `game-concept.md` exists — use game architecture layers and engine reference docs
- **通用产品**: `product-concept.md` exists — use product architecture layers and stack reference docs

Sections below are marked **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

**Argument modes:**
- **No argument / `full`**: Full guided walkthrough — all sections, start to finish
- **`layers`**: Focus on the module layer diagram only
- **`data-flow`**: Focus on data flow between modules only
- **`api-boundaries`**: Focus on API boundary definitions only
- **`adr-audit`**: Audit existing ADRs for compatibility gaps only

---

## Phase 0: Load All Context

Before anything else, load the full project context in this order:

### 0a. Technology Context (Critical)

**[游戏专用]** Read the engine reference library completely:

1. `docs/engine-reference/[engine]/VERSION.md`
   → Extract: engine name, version, LLM cutoff, post-cutoff risk levels
2. `docs/engine-reference/[engine]/breaking-changes.md`
   → Extract: all HIGH and MEDIUM risk changes
3. `docs/engine-reference/[engine]/deprecated-apis.md`
   → Extract: APIs to avoid
4. `docs/engine-reference/[engine]/current-best-practices.md`
   → Extract: post-cutoff best practices that differ from training data
5. All files in `docs/engine-reference/[engine]/modules/`
   → Extract: current API patterns per domain

If no engine is configured, stop and prompt:
> "No engine is configured. Run `/setup-engine` first. Architecture cannot be
> written without knowing which engine and version you are targeting."

**[通用产品]** Read the stack reference library completely:

1. `docs/reference/[stack]/VERSION.md`
   → Extract: stack name, version, LLM cutoff, post-cutoff risk levels
2. `docs/reference/[stack]/breaking-changes.md`
   → Extract: all HIGH and MEDIUM risk changes
3. `docs/reference/[stack]/deprecated-apis.md`
   → Extract: APIs to avoid
4. `docs/reference/[stack]/current-best-practices.md`
   → Extract: post-cutoff best practices that differ from training data
5. All files in `docs/reference/[stack]/modules/`
   → Extract: current API patterns per domain

If no stack is configured, stop and prompt:
> "No technology stack is configured. Run `/setup-engine` first. Architecture cannot be
> written without knowing which stack and version you are targeting."

### 0b. Design Context + Technical Requirements Extraction

Read all approved design documents and extract technical requirements from each:

1. **游戏专用**: `design/cdd/game-concept.md` — game pillars, genre, core loop
   **通用产品**: `design/cdd/product-concept.md` — product principles, user journey, MVP
2. `design/cdd/module-index.md` — all modules, dependencies, priority tiers
3. `standards/technical-preferences.md` — naming conventions, performance budgets,
   allowed libraries, forbidden patterns
4. **Every CDD in `design/cdd/`** — for each, extract technical requirements:
   - Data structures implied by the game rules
   - Performance constraints stated or implied
   - Engine capabilities the system requires
   - Cross-system communication patterns (what talks to what, how)
   - State that must persist (save/load implications)
   - Threading or timing requirements

Build a **Technical Requirements Baseline** — a flat list of all extracted
requirements across in-scope CDDs. Read `docs/architecture/tr-registry.yaml`
first; reuse active exact IDs, never renumber or fabricate registration. Unassigned
requirements retain their named CDD section and owning registration action.
Present the baseline as:

```
## Technical Requirements Baseline
Extracted from [N] CDDs | [X] total requirements

| Req ID | CDD | System | Requirement | Domain |
|--------|-----|--------|-------------|--------|
| TR-combat-001 | combat.md | Combat | Hitbox detection per-frame | Physics |
| TR-combat-002 | combat.md | Combat | Combo state machine | Core |
| TR-inventory-001 | inventory.md | Inventory | Item persistence | Save/Load |
```

This baseline feeds every phase. Each requirement needs a justified disposition,
owner and current evidence, not a separate ADR. Read substantive owner bodies under
`design/INSTRUCTIONS.md`, preserving existing section aliases.

### 0c. Existing Architecture Decisions

Read all files in `docs/architecture/` to understand what has already been decided.
List any ADRs found and their domains.

### 0d. Generate Knowledge Gap Inventory

Before proceeding, display a structured summary:

```
## Technology Knowledge Gap Inventory
Technology: [name + version]
LLM Training Covers: up to approximately [version]
Post-Cutoff Versions: [list]

### HIGH RISK Domains (must verify against reference docs before deciding)
- [Domain]: [Key changes]

### MEDIUM RISK Domains (verify key APIs)
- [Domain]: [Key changes]

### LOW RISK Domains (in training data, likely reliable)
- [Domain]: [no significant post-cutoff changes]

### Modules from CDD that touch HIGH/MEDIUM risk domains:
- [CDD module name] → [domain] → [risk level]
```

Ask: "This inventory identifies [N] modules in HIGH RISK technology domains. Shall I
continue building the architecture with these warnings flagged throughout?"

---

## Phase 1: Module Layer Mapping

Map every module from `module-index.md` into an architecture layer.

**[游戏专用]** The standard game architecture layers are:

```
┌─────────────────────────────────────────────┐
│  PRESENTATION LAYER                         │  ← UI, HUD, menus, VFX, audio
├─────────────────────────────────────────────┤
│  FEATURE LAYER                              │  ← gameplay systems, AI, quests
├─────────────────────────────────────────────┤
│  CORE LAYER                                 │  ← physics, input, combat, movement
├─────────────────────────────────────────────┤
│  FOUNDATION LAYER                           │  ← engine integration, save/load,
│                                             │    scene management, event bus
├─────────────────────────────────────────────┤
│  PLATFORM LAYER                             │  ← OS, hardware, engine API surface
└─────────────────────────────────────────────┘
```

**[通用产品]** The standard product architecture layers are:

```
┌─────────────────────────────────────────────┐
│  PRESENTATION LAYER                         │  ← UI components, API endpoints, CLI commands
├─────────────────────────────────────────────┤
│  FEATURE LAYER                              │  ← business logic, integrations, user-facing features
├─────────────────────────────────────────────┤
│  CORE LAYER                                 │  ← auth, data access, config, logging
├─────────────────────────────────────────────┤
│  FOUNDATION LAYER                           │  ← framework integration, ORM/database,
│                                             │    message queue, storage abstraction
├─────────────────────────────────────────────┤
│  INFRASTRUCTURE LAYER                       │  ← OS, cloud services, container runtime
└─────────────────────────────────────────────┘
```

**[通用场景]** For each module, ask:
- Which layer does it belong to?
- What are its module boundaries?
- What does it own exclusively? (data, state, behaviour)

Present the layer assignment and resolve material choices. Show the skeleton/path-
and-effect draft before new write authority; within approved scope write sections
incrementally. Existing files are edited in place, never replaced with skeletons.
Content agreement alone is not file-write authority.

**[游戏专用]** **Engine awareness check**: For each module assigned to the Core and Foundation
layers, flag if it touches a HIGH or MEDIUM risk engine domain. Show the relevant
engine reference excerpt inline.

**[通用产品]** **Stack awareness check**: For each module assigned to the Core and Foundation
layers, flag if it touches a HIGH or MEDIUM risk stack domain. Show the relevant
stack reference excerpt inline.

---

## Phase 2: Module Ownership Map

For each module defined in Phase 1, define ownership:

- **Owns**: what data and state this module is solely responsible for
- **Exposes**: what other modules may read or call
- **Consumes**: what it reads from other modules
- **Technology APIs used**: **[游戏专用]** which specific engine classes/nodes/signals this module
  calls directly (with version and risk level noted). **[通用产品]** which specific framework
  classes/decorators/middleware this module uses directly (with version and risk level noted).

Format as a table per layer, then as an ASCII dependency diagram.

**[游戏专用]** **Engine awareness check**: For every engine API listed, verify against the
relevant module reference doc. If an API is post-cutoff, flag it:

```
⚠️  [ClassName.method()] — Godot 4.6 (post-cutoff, HIGH risk)
    Verified against: docs/engine-reference/godot/modules/[domain].md
    Behaviour confirmed: [yes / NEEDS VERIFICATION]
```

**[通用产品]** **Stack awareness check**: For every framework API listed, verify against the
relevant module reference doc. If an API is post-cutoff, flag it:

```
⚠️  [ClassName.method()] — Django 5.2 (post-cutoff, HIGH risk)
    Verified against: docs/reference/django/modules/[domain].md
    Behaviour confirmed: [yes / NEEDS VERIFICATION]
```

Get user approval on the ownership map before writing.

---

## Phase 3: Data Flow

Define how data moves between modules during key scenarios.

**[游戏专用]** Cover at minimum these game data flows:

1. **Frame update path**: Input → Core systems → State → Rendering
2. **Event/signal path**: How systems communicate without tight coupling
3. **Save/load path**: What state is serialised, which module owns serialisation
4. **Initialisation order**: Which modules must boot before others

**[通用产品]** Cover at minimum these product data flows:

1. **Request/response path**: Request → Middleware → Business logic → Response
2. **Message queue/event path**: How modules communicate asynchronously without tight coupling
3. **Persistence path**: Unit of work → Repository → Database (what state is persisted, which module owns the schema)
4. **Startup order**: Config load → Database connection → Route registration → Server listen

**[通用场景]** Use ASCII sequence diagrams where helpful. For each data flow:
- Name the data being transferred
- Identify the producer and consumer
- State whether this is synchronous call, signal/event/message, or shared state
- Flag any data flows that cross thread/process boundaries

Get user approval per scenario before writing.

---

## Phase 4: API Boundaries

Define the public contracts between modules. For each boundary:

- What is the interface a module exposes to the rest of the system?
- What are the entry points (functions/signals/properties)?
- What invariants must callers respect?
- What must the module guarantee to callers?

Write in pseudocode or the project's actual language (from technical preferences).
These become the contracts programmers implement against.

**[游戏专用]** **Engine awareness check**: If any interface uses engine-specific types (e.g.
`Node`, `Resource`, `Signal` in Godot), flag the version and verify the type
exists and has not changed signature in the target engine version.

**[通用产品]** **Stack awareness check**: If any interface uses framework-specific types (e.g.
`Request`, `Response`, `Middleware` in FastAPI/Django), flag the version and verify the type
exists and has not changed signature in the target stack version.

---

## Phase 5: ADR Audit + Traceability Check

Review all existing ADRs from Phase 0c against both the architecture built in
Phases 1-4 AND the Technical Requirements Baseline from Phase 0b.

### ADR Quality Check

For each ADR:
- [ ] **[游戏专用]** Does it have an Engine Compatibility section? **[通用产品]** Does it have a Stack Compatibility section?
- [ ] Is the technology version recorded?
- [ ] Are post-cutoff APIs flagged?
- [ ] Does it have a "CDD Requirements Addressed" section?
- [ ] Does it conflict with the layer/ownership decisions made in this session?
- [ ] Is it still valid for the pinned version?

| ADR | Technology Compat | Version | CDD Linkage | Conflicts | Valid |
|-----|-------------------|---------|-------------|-----------|-------|
| ADR-0001: [title] | ✅/❌ | ✅/❌ | ✅/❌ | None/[conflict] | ✅/⚠️ |

### Traceability Coverage Check

Map every requirement/choice to the shared six dispositions. Verify `covered`
against exact Accepted revision/section/scope; cite named CDD owner for `cdd-layer`
or local reason/owner for `no-adr`. Missing ADR links alone are not gaps:

| Req ID | Requirement | ADR Coverage | Status |
|--------|-------------|--------------|--------|
| TR-combat-001 | Hitbox detection per-frame | ADR-0003 | ✅ |
| TR-combat-002 | Combo state machine | combat.md detailed rules | cdd-layer (verify no new architecture) |

Count each disposition separately. Only significant `adr-required` choices need a
new ADR/revision; `conflict` needs owner resolution. Missing evidence is incomplete,
never falsely covered.

### Required New ADRs

List only `adr-required` choices and conflict resolutions requiring an Accepted
revision/successor, by affected layer/dependencies, Foundation first. CDD contracts
and local details do not automatically require ADRs. Preserve the separate global
Technical Setup minimum of three Foundation ADRs.

**Foundation Layer (must be Accepted before affected coding):**
- `/architecture-decision [title]` → covers: TR-[id], TR-[id]

**Core Layer:**
- `/architecture-decision [title]` → covers: TR-[id]

---

## Phase 6: Missing ADR List

Based on the full architecture, produce a complete list of ADRs that should exist
but don't yet. Group by priority:

**Must be Accepted before affected coding (significant Foundation & Core decisions):**
- [e.g. "Scene management and scene loading strategy"]
- [e.g. "Event bus vs direct signal architecture"]

**Should have before the relevant system is built:**
- [e.g. "Inventory serialisation format"]

**Local choices may defer; classify materiality before affected implementation:**
- [e.g. "Specific shader technique for water"]

---

## Phase 7: Write the Master Architecture Document

Once all sections are approved, write the complete document to
`docs/architecture/architecture.md`.

Reuse existing exact architecture write authority. Only for uncovered effects ask:
"May I write the master architecture document to `docs/architecture/architecture.md`?"

The document structure:

```markdown
# [Project Name] — Master Architecture

## Document Status
- Version: [N]
- Last Updated: [date]
- **[游戏专用]** Engine: [name + version]
- **[通用产品]** Stack: [language] + [framework] [version]
- CDDs Covered: [list]
- ADRs Referenced: [list]

## Technology Knowledge Gap Summary
[Condensed from Phase 0d inventory — HIGH/MEDIUM risk domains and their implications]

## Module Layer Map
[From Phase 1]

## Module Ownership
[From Phase 2]

## Data Flow
[From Phase 3]

## API Boundaries
[From Phase 4]

## ADR Audit
[From Phase 5]

## Required ADRs
[From Phase 6]

## Architecture Principles
[3-5 key principles that govern all technical decisions for this project,
derived from the concept document, CDDs, and technical preferences]

## Open Questions
[Decisions deferred — must be resolved before the relevant layer is built]
```

---

## Phase 7b: Technical Director Sign-Off + Lead Programmer Feasibility Review

After writing the master architecture document, perform an explicit sign-off before handoff.

**Step 1 — Technical Director self-review** (this skill runs as technical-director):

Apply gate **TD-ARCHITECTURE** (`standards/director-gates.md`) as a self-review. Check all four criteria from that gate definition against the completed document.

**Review mode check** — apply before spawning LP-FEASIBILITY:
- `solo` → skip LP. Note: "LP-FEASIBILITY skipped — Solo mode." Continue to Step 3 with actual TD assessment and LP Skipped state.
- `lean` → skip LP (not a PHASE-GATE). Note: "LP-FEASIBILITY skipped — Lean mode." Continue to Step 3 with actual TD assessment and LP Skipped state.
- `full` → spawn as normal.

**Step 2 — Spawn `lead-programmer` via Task using gate LP-FEASIBILITY (`standards/director-gates.md`):**

Pass: architecture document path, technical requirements baseline summary, ADR list.

**Step 3 — Present actual assessment states to the user:**

Show the actual TD-ARCHITECTURE self-review result (APPROVE/CONCERNS/REJECT).
In full mode show the completed LP-FEASIBILITY result (FEASIBLE/CONCERNS/INFEASIBLE);
in lean/solo report LP skipped, never claim that both reviewers completed.
Record each assessment's run state separately: Completed, Skipped with mode,
NotRun or Blocked with reason. NotRun/Blocked has no fabricated gate verdict.
Unavailable required review remains incomplete and blocks affected qualification.
Required blockers remain unresolved until their owning workflow/evidence closes them.

For unresolved choices use `AskUserQuestion` — "Architecture assessments are shown
above. How would you like to proceed?"
Options: `Proceed to handoff with actual status` / `Revise flagged items first` /
`Discuss specific concerns`. This content choice cannot accept an ADR or clear blockers.

**Step 4 — Record sign-off in the architecture document:**

Update the Document Status section:
```
- Technical Director Run State: [Completed / NotRun / Blocked with reason]
- Technical Director Assessment: [date] — [actual APPROVE / CONCERNS / REJECT; N/A if not completed]
- Lead Programmer Run State: [Completed / Skipped with mode / NotRun / Blocked with reason]
- Lead Programmer Feasibility: [actual FEASIBLE / CONCERNS / INFEASIBLE; N/A if not completed]
- Unresolved required actions: [affected scope, owner and required closure]
```

Reuse existing authority for this exact Document Status effect; otherwise show the
actual assessment/status changes and ask:
"May I update the Document Status section in `docs/architecture/architecture.md` with the sign-off?"
Report actual reviewed qualification; a status write cannot invent a completed review,
accept a decision or establish implementation readiness.

---

## Phase 8: Handoff

After writing the document, provide a clear handoff:

1. **Run these ADRs next** (from Phase 6, prioritised): list the top 3
2. **Qualification**: Report document-write outcome separately from actual
   assessment/decision/readiness findings. Run `/gate-check pre-production` only when
   required decisions are Accepted and the separate global gate is satisfied.
3. **Session state**: Write `production/session-state/active.md` only within its
   authorized path/effect; otherwise show the summary in conversation.

---

## Collaborative Protocol

This skill follows the collaborative design principle at every phase:

1. **Load context silently** — do not narrate file reads
2. **Present findings** — show the knowledge gap inventory and layer proposals
3. **Ask before deciding** — present options for each architectural choice
4. **Get approval before writing** — each phase section is written only after
   the path/effect is authorized and material choices are approved
5. **Incremental writing** — write each approved section immediately; do not
   accumulate everything and write at the end. This survives session crashes.

Never make a binding architectural decision without user input. If the user is
unsure, present 2-4 options with pros/cons before asking them to decide.

---

## Recommended Next Steps

- Run `/architecture-decision [title]` for each required ADR listed in Phase 6 — Foundation layer ADRs first
- Run `/create-control-manifest` once the required ADRs are Accepted to produce the layer rules manifest
- Run `/gate-check pre-production` when required ADRs are Accepted, the global gate is satisfied and architecture is signed off
