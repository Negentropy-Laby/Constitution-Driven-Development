---
name: constitute
description: "Constitution Driven Development project governance — establishes, derives, updates, or amends governing principles at any project stage. Reads existing artifacts to derive a constitution, audits alignment, tracks versions, and supports formal amendment workflow. Domain-agnostic, stage-aware unified onboarding entry."
argument-hint: "[no arguments]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, AskUserQuestion
---

## User Guide

- When to use: Constitution Driven Development project governance — establishes, derives, updates, or amends governing principles at any project stage. Reads existing artifacts to derive a constitution, audits alignment, tracks versions, and supports formal amendment workflow. Domain-agnostic, stage-aware unified onboarding entry.
- Inputs: Command arguments: `/constitute`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: `memory_bank/document_map.yaml`, `memory_bank/README.md`, `memory_bank/t0_core/*`, `memory_bank/t1_axioms/knowledge_graph.md`, `memory_bank/t2_execution/*`, and `memory_bank/t3_archive/*` skeleton/index files described below.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Constitution Legislation — Stage-Aware Project Governance

This skill initializes the `memory_bank/` governance control plane: T0 core
laws and current state, T1 supporting axioms, T2 execution mirrors/indexes, and
T3 archive indexes. It also writes `production/review-mode.txt`.

Unlike the legacy first-session-only onboarding flow, this skill can be
invoked at **any project stage**. It detects what you've already built and
adapts: deriving a constitution from existing artifacts, auditing alignment,
running formal amendments with version tracking, or guiding a fresh project
through discovery.

---

## Phase 1: Silent State Detection

Before asking anything, gather context silently. Do NOT show these results
unprompted — they inform your recommendations, not the conversation opener.

Check each of these and classify the project into one of 6 stages:

| Check | What to look for |
|-------|-----------------|
| Constitution exists? | `memory_bank/t0_core/basic_law_index.md` |
| Concept doc exists? | `design/cdd/game-concept.md` or `design/cdd/product-concept.md` |
| Tech prefs configured? | `standards/technical-preferences.md` (not `[CHOOSE]` or `[TO BE CONFIGURED]`) |
| Module index exists? | `design/cdd/module-index.md` |
| CDDs exist? | `design/cdd/*.md` (excluding concept, index, principles) |
| ADRs exist? | `docs/architecture/adr-*.md` |
| Architecture doc exists? | `docs/architecture/architecture.md` |
| Source code exists? | `src/` has source files |
| Production artifacts? | `production/sprints/`, `production/epics/` |
| Current stage? | `production/stage.txt` |
| Prototypes exist? | `prototypes/` has subdirectories |
| Review mode set? | `production/review-mode.txt` |

**Stage classification:**

| Stage | Detection |
|-------|-----------|
| **0. Empty** | No concept doc, no source, no ADRs |
| **1. Concept only** | Concept doc exists, no module index, no ADRs, no constitution |
| **2. Designed** | Module index + CDDs exist, no or few ADRs |
| **3. Architected** | ADRs exist, architecture doc may exist |
| **4a. Source only** | Source code exists, no production artifacts (no `production/sprints/`, no `production/epics/`) |
| **4b. Implemented** | Source code + production artifacts both exist |
| **5. Constitution exists** | `memory_bank/t0_core/basic_law_index.md` exists |

**Priority rule**: If `basic_law_index.md` exists, classify as Stage 5 first regardless
of what else is present. Then inspect concept doc, CDDs, ADRs, and source changes
inside Stage 5 to determine what the returning user needs (audit, amend, or revise).

---

## Phase 2: Route Based on Detected Stage

After Phase 1 determines the current stage, read only the matching stage section in [stage routing](references/stage-routing.md). Apply that route before entering Phase 3 or any later workflow. The reference contains the stage-specific questions, artifact rules, and return-user behavior.

## Phase 3: Interactive Legislation (from scratch)

This phase is entered when the user wants to define a constitution manually
with no concept doc to derive from.

### Phase 3a: Domain + Core Thesis

**Domain question — only ask if not already established.** If the user arrived
from Stage 0 (Question 1 was already answered) or the domain was detected from
a concept doc, skip this. Only ask when entering Phase 3 from Stage 1 "Start
from scratch" where no domain context exists.

If domain is unknown, use `AskUserQuestion`:
- **Prompt**: "What kind of project is this?"
- **Options**:
  - `A game` — 2D/3D interactive experience (any genre, any engine)
  - `A general product` — web app, CLI tool, API, library, mobile app, data pipeline

Record the domain. Then: "We'll start with one sentence: **what is this project, and what is it NOT?**"

Guide the user to produce: Project Name, Core Thesis (BL-01), Anti-Thesis.

Present the draft. Once approved, write `memory_bank/t0_core/active_context.md`
with `Constitution Version: 0.1 (Draft)`.

### Phase 3b: Core Principles (3-5)

"Now the most important part: the **non-negotiable principles** that govern
every decision."

Explain the criteria: 3-5 max, must be falsifiable, must create tension, must
apply to all aspects, each needs a design test.

Use `AskUserQuestion` to present draft principles. Each law gets:
- Support ID (BL-02 through BL-06)
- Status: `Proposed`
- The principle statement
- Current-state requirement
- A design test

Once approved, write `memory_bank/t0_core/basic_law_index.md`.
All laws start as `Status: Proposed`.

### Phase 3c: Technology & Constraints

Ask for broad technology preferences. Detailed configuration is deferred to
`/setup-engine`. Write `memory_bank/t1_axioms/tech_context.md`,
`system_patterns.md`, `behavior_context.md` at a high level.

### Phase 3d: Review Mode

Check `production/review-mode.txt`. If not set, use `AskUserQuestion`:
Full / Lean (recommended) / Solo. Write choice to file.

### Phase 3e: Ratification

Before finalizing, present the complete constitution for ratification:

```
## Constitution Ratification
Version: 1.0
All laws are currently Status: Proposed.

To take effect, they must be ratified (Status: Accepted).
```

Use `AskUserQuestion`:
- **Prompt**: "The constitution is drafted. Ratify it?"
- **Options**:
  - `Ratify — all laws become Accepted` — Write version 1.0 with all laws Accepted. Record sign-off.
  - `Revise first` — I want to edit before ratifying.
  - `Leave as Draft` — Write as version 0.1 (Draft). Ratify later.

If "Ratify": update all law statuses to `Accepted ([date])`.
Write version 1.0 to `active_context.md` with changelog entry and sign-off.
Write `memory_bank/README.md`.

### Phase 3e.1: Memory Bank Control Plane Skeleton

After ratification, create the project memory-bank skeleton from
`templates/memory-bank/`. Do not move detailed work files out of
`design/`, `docs/`, `workflow/`, `templates/`, `standards/`, or `production/`;
the memory bank indexes and mirrors those paths.

Create or update these files:

- `memory_bank/document_map.yaml`
- `memory_bank/t0_core/current_state.md`
- `memory_bank/t0_core/release_state.md`
- `memory_bank/t0_core/amendment_log.md`
- `memory_bank/t1_axioms/architecture_context.md`
- `memory_bank/t1_axioms/ux_accessibility_context.md`
- `memory_bank/t1_axioms/qa_context.md`
- `memory_bank/t1_axioms/knowledge_graph.md`
- `memory_bank/t1_axioms/module_support_map.yaml`
- `memory_bank/t2_execution/README.md`
- `memory_bank/t2_execution/workflow_contract.md`
- `memory_bank/t2_execution/phase_checklists.md`
- `memory_bank/t2_execution/gate_required_artifacts.md`
- `memory_bank/t2_execution/current_roadmap.md`
- `memory_bank/t2_execution/framework_contract.md`
- `memory_bank/t2_execution/adapter_state.yaml`
- `memory_bank/t2_execution/skill_testing/README.md`
- `skill_testing/catalog.yaml`
- `skill_testing/quality-rubric.md`
- `skill_testing/specs/skills/`
- `skill_testing/specs/agents/`
- `skill_testing/templates/`
- `memory_bank/t3_archive/README.md`
- `memory_bank/t3_archive/qa_evidence_index.md`
- `memory_bank/t3_archive/release_evidence/README.md`
- `memory_bank/t3_archive/gate_runs/README.md`
- `memory_bank/t3_archive/reviews/README.md`
- `memory_bank/t3_archive/reviews/review-index.md`
- `memory_bank/t3_archive/sprint_snapshots/README.md`
- `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md`
- `memory_bank/t3_archive/amendments/README.md`
- `memory_bank/t3_archive/skill_testing/README.md`
- `memory_bank/t3_archive/skill_testing/coverage-index.yaml`
- `memory_bank/t3_archive/skill_testing/results/static/README.md`
- `memory_bank/t3_archive/skill_testing/results/spec/README.md`
- `memory_bank/t3_archive/skill_testing/results/category/README.md`
- `memory_bank/t3_archive/skill_testing/results/audit/README.md`
- `memory_bank/t3_archive/skill_testing/improvements/README.md`

Canonical knowledge graph path is `memory_bank/t1_axioms/knowledge_graph.md`.
If an older project has `memory_bank/t0_core/knowledge_graph.md`, treat it as a deprecated compatibility pointer and migrate future updates to the T1 path.

`memory_bank/t2_execution/phase_checklists.md` and
`memory_bank/t2_execution/gate_required_artifacts.md` are generated mirrors.
Refresh them with `python scripts/generate_phase_checklists.py --write --memory-bank`
and `python scripts/generate_gate_required_sections.py --write --memory-bank`.
`memory_bank/t2_execution/current_roadmap.md` is maintained by `/cdd-status`.
Copy `framework_contract.md` and `adapter_state.yaml` from their matching
`templates/memory-bank/t2_execution/` sources. The adapter state must remain the
exact deterministic `uninitialized` template: do not fabricate digests, a
commit, a timestamp, or a `fresh` result during `/constitute`. After the
skeleton is approved and written, tell the user to run `/constitute-check` to
perform the live read-only check and optionally record its result.
`skill_testing/` defines cross-project CDD skill and agent test standards.
`memory_bank/t2_execution/skill_testing/README.md` records the project-memory
mount contract for those canonical assets. `memory_bank/t3_archive/skill_testing/`
records approved `/skill-test` runs and `/skill-improve` evidence.

### Phase 3f: Handoff After Interactive Legislation

Constitution written from scratch. Now route to the correct next step.
This is the handoff for Path C "Formalize first" — the user has a clear spec
but no concept doc yet. Note this explicitly:

> "Your constitution is established. Your concept isn't yet formalized as a
> document. Run `/brainstorm [your spec]` to produce `design/cdd/game-concept.md`
> (or `product-concept.md`) — it will validate your principles against a
> structured concept. Then return to `/constitute` to update."

This is a unique state: constitution exists, but no concept doc. Stage 1a
assumes a concept doc already exists, so do NOT use Stage 1a routing here.
Instead, route directly to `/brainstorm`:

- Phase 3d Review Mode (if not already set from Phase 3d)
- Handoff: "Type `/brainstorm [your spec]` to begin."
- After `/brainstorm` completes, return to `/constitute`. It will detect the
  existing constitution AND the new concept doc, and offer to update via
  Stage 5 → `Revise from source` (Phase 6 amendment workflow). The revision
  will compare the new concept doc against the existing principles and
  propose amendments for any changes.

---

## Phase 4: Auto-Derivation Workflow (from existing artifacts)

### Step 4a: Read Source Artifacts Silently

Read all available artifacts. Build a complete picture.

### Step 4b: Extract and Present Section by Section

For each constitutional element, extract from the best available source:

| Element | Primary Source | Fallback |
|---------|---------------|----------|
| Core thesis | Concept doc → elevator pitch | — |
| Principles | Concept doc → pillars/principles | — |
| Anti-thesis | Concept doc → anti-pillars/anti-principles | — |
| Domain | Concept doc content | Ask user |
| Tech context | technical-preferences.md | Concept doc platform section |
| System patterns | ADRs → architecture decisions | — |
| Behavior context | CDDs → implicit conventions | — |

Present each section with `AskUserQuestion`:
- **Prompt**: "[Section name] derived from your project."
- **Options**:
  - `Approve — write as-is`
  - `Edit — I want to refine this`
  - `Skip this section`

### Step 4c: Write Approved Sections

Write each approved section to the appropriate `memory_bank/` file immediately.
Create directories as needed. All derived laws start as `Status: Accepted`
since they come from already-approved concept documents.

Also create the T0-T3 memory-bank control plane skeleton listed in Phase 3e.1.
For derived projects, populate `document_map.yaml`, `current_state.md`,
`workflow_contract.md`, and T1 index files from the source artifacts when
evidence exists; otherwise leave template placeholders with clear `missing` or
`not started` status.

### Step 4d: Alignment Report (if CDDs or ADRs exist)

Generate:
```
## Constitution Alignment Report
Constitution Version: 1.0

### Principles
✓ [Law 1]: [name] — supported by ADR-0001, ADR-0003
⚠ [Law 2]: [name] — no ADR coverage found
⚠ [Law 3]: [name] — CDD [module].md may conflict

### Gaps
1. [gap + suggested fix]

Overall: ALIGNED / NEEDS ATTENTION
```

### Step 4e: Write Version and Sign-Off

Write version 1.0 to `active_context.md` with changelog entry:
`Initial constitution derived from concept doc and [N] CDDs / [M] ADRs`.
Record sign-off with current date.

### Step 4f: Review Mode and Stage-Aware Handoff

Constitution is established. Now set review mode and route to the correct
next phase based on the detected stage.

**Review Mode**: Check `production/review-mode.txt`. If not set, use
`AskUserQuestion`: Full / Lean (recommended) / Solo. Write choice.

**Stage-aware handoff** — the next steps differ by stage:

| Stage | Detected Artifacts | Next Steps |
|-------|-------------------|------------|
| **1. Concept** | Concept doc exists, module index missing | `/design-review` on concept → `/gate-check concept` → `/map-systems` |
| **2a. Mapped** | Module index exists, MVP CDDs incomplete | `/map-systems next` or `/design-system [module]` → `/design-review` |
| **2b. Designed** | Module index + MVP CDDs exist | `/review-all-gdds` → `/gate-check systems-design` → `/setup-engine` |
| **3. Architected** | ADRs exist | `/gate-check` to validate current phase. Next incomplete phase from pipeline. |
| **4a. Source only** | Source code exists, no production artifacts | "You have source code but no production tracking. Run `/project-stage-detect` to assess your current phase, or `/gate-check` if you know where you are." |
| **4b. Implemented** | Source + production artifacts exist | `/gate-check` to validate current phase. Next incomplete phase from pipeline. |

Show the full pipeline from Phase 7 for context, then use `AskUserQuestion`:
- **Prompt**: "Constitution established. Which step would you like to start with?"
- **Options**: 3-4 concrete next steps from the stage-appropriate list above.
  Include `Something else — I'll tell you`.

When confirmed: "Type `[skill command]` to begin."

---

## Phase 5: Alignment Report (standalone audit)

When invoked on a project with an existing constitution and CDDs/ADRs/code,
generate this report. Already integrated into Stage 3-4 routing.

---

## Phase 6: Amendment Workflow

This is the formal process for changing an existing constitution.

### Step 6a: Determine Amendment Trigger

Amendments are triggered when:
- User selects "Amend constitution" (Stage 5)
- User selects "Revise from source" (Stage 5)
- Concept document has changed (Stage 3-4 with existing constitution)
- `/constitute-check` flags stale principles
- User explicitly requests amendment

### Step 6b: Load and Compare

1. Read current constitution (`basic_law_index.md` + `active_context.md`)
2. Read changed source artifacts (concept doc, CDDs, ADRs — whatever triggered this)
3. Compute what changed:
   - **New content in concept doc** → candidate new principles
   - **Changed content in concept doc** → candidate principle amendments
   - **Removed content in concept doc** → candidate principle deprecation
   - **New CDDs** → principles may need scope expansion
   - **New ADRs** → may formalize previously implicit principles

### Step 6c: Present Amendment Proposal

Present the proposed changes as a structured diff:

```
## Proposed Constitutional Amendment
Current Version: 1.2
Proposed Version: 1.3

### Changed Principles
Law 2 (BL-03): "API-first design" → "API-first design with OpenAPI spec"
  Reason: concept doc now specifies OpenAPI requirement
  Impact: ADR-0005 (API framework choice) needs review
  Status: Accepted → Accepted (amended)

### New Principles
Law 6 (BL-08): "Observability by default" — all services must expose metrics
  Source: derived from new CDD monitoring-module.md
  Design test: if choosing between a logging library and a metrics library, this
    principle says choose the one that provides both structured logs AND metrics
  Status: Proposed

### Deprecated Principles
Law 4 (BL-05): "Monolith-first" → Superseded by Law 6
  Reason: project has grown beyond monolith scale; observability requires
    service-level instrumentation
  Status: Accepted → Superseded by BL-08

### Principles Unchanged
Law 1 (BL-02): [name] — no change
Law 3 (BL-04): [name] — no change
Law 5 (BL-07): [name] — no change
```

### Step 6d: User Review Each Change

Present each changed/new/deprecated principle individually using `AskUserQuestion`:
- **Prompt**: "Amendment: [change description]. Approve this change?"
- **Options**:
  - `Approve — apply this amendment`
  - `Revise — I want to edit this amendment`
  - `Reject — keep the current version for this principle`

### Step 6e: Write Amended Constitution

1. Update `basic_law_index.md`:
   - Changed laws: update text, keep Support ID, set Status to `Accepted (amended [date])`
   - New laws: add with new Support ID, Status `Accepted ([date])`
   - Deprecated laws: set Status to `Superseded by BL-XX ([date])` or `Deprecated ([date])`
2. Bump version in `active_context.md`
3. Append changelog entry
4. Record sign-off
5. Update `memory_bank/t0_core/amendment_log.md`
6. Write `memory_bank/t3_archive/amendments/amendment-v[version]-[YYYY-MM-DD].md`
   as the detailed amendment evidence. If the same filename exists, use
   `amendment-v[version]-[YYYY-MM-DD]-[NN].md` and do not overwrite history.

The T3 amendment evidence must include: version, date, trigger, changed
principles, rationale, rejected alternatives, approval/sign-off, impacted T1/T2/T3 files, and follow-up checks.

### Step 6f: Changelog and Sign-Off

Append to `active_context.md`:

```
## Constitution Changelog
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.2 | 2026-05-01 | [user] + AI | Amended Law 2 (BL-03): API-first → API-first with OpenAPI. Added Law 6 (BL-08): Observability by default. Superseded Law 4 (BL-05) → BL-08. |

## Amendment Sign-Off
This amendment was approved on 2026-05-01.
Changes reviewed and accepted:
  - BL-03: amended (API-first with OpenAPI spec)
  - BL-05: superseded by BL-08
  - BL-08: added as Accepted
Amendment session: /constitute (triggered by concept doc update)
```

### Step 6g: Impact Warnings

After writing, flag any downstream impacts:

> "Amendment complete. The following artifacts may need review:
> - ADR-0005: references Law 2 — verify the amended principle is still compatible
> - monitoring-module.md: new CDD — run `/design-review` to validate"

---

## Phase 7: Pipeline and Hand Off

Show the user the full journey ahead based on their detected stage and domain.

### Stage 0 (Empty) Pipeline

**[游戏专用] Game Pipeline:**

**Concept Phase:**
`/brainstorm` → `/constitute` → `/design-review` → `/gate-check concept`

**Systems Design Phase:**
`/map-systems` → `/design-system [system]` → `/design-review` → `/review-all-gdds` → `/gate-check systems-design`

**Technical Setup Phase:**
`/setup-engine` → `/create-architecture` → `/architecture-decision (×N)` → `/architecture-review` → `/create-control-manifest`
Then create `design/accessibility-requirements.md` from `templates/accessibility-requirements.md` → `/test-setup` → `/gate-check technical-setup`

**Pre-Production Phase:**
`/ux-design` → `/ux-review` → `/prototype` → `/playtest-report` → `/create-epics` → `/create-stories` → `/sprint-plan` → `/story-readiness` → `/gate-check pre-production`

**Production Phase:**
`/dev-story` (repeat) → `/story-done` → `/code-review` → `/sprint-status`

**Polish Phase:**
`/perf-profile` → `/balance-check` → `/team-polish`

**Release Phase:**
`/release-checklist` → `/launch-checklist` → `/team-release`

`/changelog` and `/patch-notes` are optional release communication artifacts.
`/hotfix` is emergency-only after release or incident discovery.

**[通用产品] Product Pipeline:**

**Concept Phase:**
`/brainstorm` → `/constitute` → `/design-review` → `/gate-check concept`

**Specification Phase:**
`/map-systems` → `/design-system [module]` → `/design-review` → `/review-all-gdds` → `/gate-check systems-design`

**Architecture Phase:**
`/setup-engine` → `/create-architecture` → `/architecture-decision (×N)` → `/architecture-review` → `/create-control-manifest`
Then create `design/accessibility-requirements.md` from `templates/accessibility-requirements.md` → `/test-setup` → `/gate-check technical-setup`

**Pre-Implementation Phase:**
`/ux-design` → `/ux-review` → `/prototype` → `/playtest-report` (Product workflow validation) → `/create-epics` → `/create-stories` → `/sprint-plan` → `/story-readiness` → `/gate-check pre-production`

**Implementation Phase:**
`/story-readiness` → implement → `/story-done` → `/code-review` → `/sprint-status`

**Verification Phase:**
`/qa-plan` → `/smoke-check` → `/gate-check`

**Release Phase:**
`/release-checklist` → `/launch-checklist` → `/team-release`

`/changelog` and `/patch-notes` are optional release communication artifacts.
`/hotfix` is emergency-only after release or incident discovery.

### Stage 1 Pipeline (Concept only, after /brainstorm)

The user has a concept doc from `/brainstorm` but no module index.

**[游戏专用] Game:**
`/design-review` (on concept) → `/gate-check concept` → `/map-systems`
Then continue with Systems Design phase from Stage 0 pipeline.

**[通用产品] Product:**
`/design-review` (on concept) → `/gate-check concept` → `/map-systems`
Then continue with Specification phase from Stage 0 pipeline.

### Stage 2a Pipeline (Module index exists, MVP CDDs incomplete)

The user has a module index. Continue Systems Design / Specification.

**[游戏专用] Game:**
`/map-systems next` → `/design-system [system]` → `/design-review`
Then continue with Systems Design phase.

**[通用产品] Product:**
`/map-systems next` → `/design-system [module]` → `/design-review`
Then continue with Specification phase.

### Stage 2 Pipeline (Designed — module index + CDDs exist)

The user has CDDs. Next steps depend on whether architecture work has begun:
If no ADRs: run `/review-all-gdds` → `/gate-check systems-design` → `/setup-engine`
If some ADRs exist: continue with next architecture step from Stage 0 pipeline.

### Stage 3-5 Pipeline

Skip to the next incomplete phase based on what's detected. Show the full
Stage 0 pipeline for context and highlight which phase the user should
enter at.

Use `AskUserQuestion`: "Which step would you like to start with?"
Show 3-4 concrete next steps. Include `Something else — I'll tell you`.

When confirmed: "Type `[skill command]` to begin."

Verdict: **COMPLETE**

---

## Principle Lifecycle Reference

All laws in `basic_law_index.md` must have a `Status` field:

| Status | Meaning | When to use |
|--------|---------|-------------|
| `Proposed` | Drafted, not yet ratified | During Phase 3 interactive legislation, before ratification |
| `Accepted` | In effect | After ratification (Phase 3e) or derivation (Phase 4) |
| `Accepted (amended [date])` | In effect, text changed | After amendment (Phase 6) |
| `Superseded by BL-XX ([date])` | Replaced by another law | When a new law makes this one obsolete |
| `Deprecated ([date])` | Intentionally removed | When a principle is no longer relevant with no replacement |

---

## Collaborative Protocol

1. **Detect first** — never assume the project stage
2. **Derive when possible** — extract from existing artifacts rather than asking from scratch
3. **Present diffs** — show old vs new when amending
4. **Section-by-section approval** — each constitutional element approved individually
5. **Track versions** — every write bumps the version and logs the change
6. **Record sign-off** — every ratification or amendment records who approved it and when
7. **Flag impacts** — after amendments, note what downstream artifacts need review
8. **No auto-execution** — recommend next skill, don't run it without asking
