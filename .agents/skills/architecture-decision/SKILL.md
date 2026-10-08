---
name: architecture-decision
description: "Use this skill when a significant technical choice needs an ADR recording its context, alternatives, consequences, and implementation constraints for a game or software product."
argument-hint: "[title] [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Task, AskUserQuestion
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

- When to use: Creates an Architecture Decision Record (ADR) documenting a significant technical decision, its context, alternatives considered, and consequences. Supports both game and general product domains. Every major technical choice should have an ADR.
- Inputs: Command arguments: `/architecture-decision [title] [--review full|lean|solo]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

When this skill is invoked:

**Domain detection.** The concept document at `design/cdd/` reveals the domain:
- **游戏专用**: `game-concept.md` exists — ADR includes Engine Compatibility section
- **通用产品**: `product-concept.md` exists — ADR includes Stack Compatibility section

Sections below are marked **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

## 0. Parse Arguments — Detect Retrofit Mode

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

**If the argument starts with `retrofit` followed by a file path**
(e.g., `/architecture-decision retrofit docs/architecture/adr-0001-event-system.md`):

Enter **retrofit mode**:

1. Read the existing ADR file completely.
2. Identify which template sections are present by scanning headings:
   - `## Status` — **BLOCKING if missing**: `/story-readiness` cannot check ADR acceptance
   - `## ADR Dependencies` — HIGH if missing: dependency ordering breaks
   - **[游戏专用]** `## Engine Compatibility` — HIGH if missing: post-cutoff risk unknown
   - **[通用产品]** `## Stack Compatibility` — HIGH if missing: post-cutoff risk unknown
   - `## CDD Requirements Addressed` — MEDIUM if missing: traceability lost
3. Present to the user:
   ```
   ## Retrofit: [ADR title]
   File: [path]

   Sections already present (will not be touched):
   ✓ Status: [current value, or "MISSING — will add"]
   ✓ [section]

   Missing sections to add:
   ✗ Status — BLOCKING (stories cannot validate ADR acceptance without this)
   ✗ ADR Dependencies — HIGH
   ✗ Engine/Stack Compatibility — HIGH
   ```
4. Show the missing-section draft and named path/effects. Reuse existing retrofit
   authority; otherwise ask: "May I add these missing sections at [path]?"
   Preserve existing content outside the approved repair.
5. If yes:
   - For **Status**: verify historical acceptance against retained originals,
      authority, date and exact revision/scope. Do not infer Accepted from code
      or a status-choice widget. Unevidenced acceptance stays Proposed with unknown
      history; acceptance requires a separate authorized decision/effect. Preserve
      evidenced Deprecated/Superseded history without inventing dates.
   - For **ADR Dependencies**: ask — "Does this decision depend on any other ADR?
     Does it enable or block any other ADR or epic?" Accept "None" for each field.
   - **[游戏专用]** For **Engine Compatibility**: read the engine reference docs (same as Step 0 below)
     and ask the user to confirm the domain. Then generate the table with verified data.
   - **[通用产品]** For **Stack Compatibility**: read the stack reference docs (same as Step 0 below)
     and ask the user to confirm the domain. Then generate the table with verified data.
   - For **CDD Requirements Addressed**: ask — "Which CDD systems motivated this decision?
     What specific requirement in each CDD does this ADR address?"
   - Append each missing section to the ADR file using the Edit tool.
   - **Never modify any existing section.** Only append or fill absent sections.
6. After adding all missing sections, update the ADR's `## Date` field if it is absent.
7. Suggest: "Run `/architecture-review` to re-validate coverage now that this ADR
   has its Status and Dependencies fields."

If NOT in retrofit mode, proceed to Step 0 below (normal ADR authoring).

**No-argument guard**: If no argument was provided (title is empty), ask before
running Phase 0:

> "What technical decision are you documenting? Please provide a short title
> (e.g., `event-system-architecture`, `physics-engine-choice`)."

Use the user's response as the title, then proceed to Step 0.

---

## 0. Load Technology Context (ALWAYS FIRST)

Before doing anything else, establish the technology environment.

**[游戏专用]** Engine context:

1. Read `docs/engine-reference/[engine]/VERSION.md` to get:
   - Engine name and version
   - LLM knowledge cutoff date
   - Post-cutoff version risk levels (LOW / MEDIUM / HIGH)

2. Identify the **domain** of this architecture decision from the title or
   user description. Common game domains: Physics, Rendering, UI, Audio, Navigation,
   Animation, Networking, Core, Input, Scripting.

3. Read the corresponding module reference if it exists:
   `docs/engine-reference/[engine]/modules/[domain].md`

4. Read `docs/engine-reference/[engine]/breaking-changes.md` — flag any
   changes in the relevant domain that post-date the LLM's training cutoff.

5. Read `docs/engine-reference/[engine]/deprecated-apis.md` — flag any APIs
   in the relevant domain that should not be used.

6. **Display a knowledge gap warning** before proceeding if the domain carries
   MEDIUM or HIGH risk:

   ```
   ⚠️  ENGINE KNOWLEDGE GAP WARNING
   Engine: [name + version]
   Domain: [domain]
   Risk Level: HIGH — This version is post-LLM-cutoff.

   Key changes verified from engine-reference docs:
   - [Change 1 relevant to this domain]
   - [Change 2]

   This ADR will be cross-referenced against the engine reference library.
   Proceed with verified information only — do NOT rely solely on training data.
   ```

   If no engine has been configured yet, prompt: "No engine is configured.
   Run `/setup-engine` first, or tell me which engine you are using."

**[通用产品]** Stack context:

1. Read `docs/reference/[stack]/VERSION.md` to get:
   - Stack name and version
   - LLM knowledge cutoff date
   - Post-cutoff version risk levels (LOW / MEDIUM / HIGH)

2. Identify the **domain** of this architecture decision from the title or
   user description. Common product domains: API Design, Data Storage, Authentication,
   Caching, Messaging, Frontend, CLI, DevOps, Security, Performance.

3. Read the corresponding module reference if it exists:
   `docs/reference/[stack]/modules/[domain].md`

4. Read `docs/reference/[stack]/breaking-changes.md` — flag any
   changes in the relevant domain that post-date the LLM's training cutoff.

5. Read `docs/reference/[stack]/deprecated-apis.md` — flag any APIs
   in the relevant domain that should not be used.

6. **Display a knowledge gap warning** before proceeding if the domain carries
   MEDIUM or HIGH risk:

   ```
   ⚠️  STACK KNOWLEDGE GAP WARNING
   Stack: [name + version]
   Domain: [domain]
   Risk Level: HIGH — This version is post-LLM-cutoff.

   Key changes verified from stack-reference docs:
   - [Change 1 relevant to this domain]
   - [Change 2]

   This ADR will be cross-referenced against the stack reference library.
   Proceed with verified information only — do NOT rely solely on training data.
   ```

   If no stack has been configured yet, prompt: "No technology stack is configured.
   Run `/setup-engine` first, or tell me which stack you are using."

---

## 1. Determine the next ADR number

Scan `docs/architecture/` for existing ADRs to find the next number.

---

## 2. Gather context

Read related code, Notes/Story evidence, existing ADRs and relevant CDDs from
`design/cdd/`. Classify the choice first. Exact `covered`, CDD-owned `cdd-layer`
or justified local `no-adr` needs no duplicate ADR; report its reason/owner.
Route significant `adr-required`/`conflict` choices to an Accepted decision/revision
before affected implementation, continuing independent authorized work.

### 2a: Architecture Registry Check (BLOCKING gate)

Read `docs/registry/architecture.yaml`. Extract entries relevant to this ADR's
domain and decision (grep by system name, domain keyword, or state being touched).
Verify each stance against the actual Accepted revision and scope. Proposed or
unevidenced registry entries are tentative, not locked constraints. A missing
registry uses actual governing decisions, never invented stances.

Present any relevant stances to the user **before** the collaborative design
begins, as locked constraints:

```
## Existing Architectural Stances (must not contradict)

State Ownership:
  player_health → owned by health-system (ADR-0001)
  Interface: HealthComponent.current_health (read-only float)
  → If this ADR reads or writes player health, it must use this interface.

Interface Contracts:
  damage_delivery → signal pattern (ADR-0003)
  Signal: damage_dealt(amount, target, is_crit)
  → If this ADR delivers or receives damage events, it must use this signal.

Forbidden Patterns:
  ✗ autoload_singleton_coupling (ADR-0001)
  ✗ direct_cross_system_state_write (ADR-0000)
  → The proposed approach must not use these patterns.
```

If the user's proposed decision would contradict any registered stance, surface
the conflict immediately:

> "⚠️ Conflict: This ADR proposes [X], but ADR-[NNNN] established that [Y] is
> the accepted pattern for this purpose. Proceeding without resolving this will
> produce contradictory ADRs and inconsistent stories.
> Options: (1) Align with the existing stance, (2) Supersede ADR-[NNNN] with
> an explicit replacement, (3) Explain why this case is an exception."

Surface conflict before affected implementation. Step 3 may draft alignment or a
successor; an exception needs explicit existing-governance authority, exact scope,
risks and duration. It does not relabel a conflict resolved or Proposed ADR Accepted.

---

## 3. Guide the decision collaboratively

Before asking anything, derive the skill's best guesses from the context already
gathered (CDDs read, engine reference loaded, existing ADRs scanned). Then present
a **confirm/adjust** prompt using `AskUserQuestion` — not open-ended questions.

**Derive assumptions first:**
- **Problem**: Infer from the title + CDD context what decision needs to be made
- **Alternatives**: Propose 2-3 concrete options from engine reference + CDD requirements
- **Dependencies**: Scan existing ADRs for upstream dependencies; assume None if unclear
- **CDD linkage**: Extract which CDD systems the title directly relates to
- **Status**: Always `Proposed` for new ADRs — never ask the user what the status is

**Scope of assumptions tab**: Assumptions cover only: problem framing, alternative approaches, upstream dependencies, CDD linkage, and status. Schema design questions (e.g., "How should spawn timing work?", "Should data be inline or external?") are NOT assumptions — they are design decisions belonging to a separate step after the assumptions are confirmed. Do not include schema design questions in the assumptions AskUserQuestion widget.

**After assumptions are confirmed**, if the ADR involves schema or data design choices, use a separate multi-tab `AskUserQuestion` to ask each design question independently before drafting.

**Present assumptions with `AskUserQuestion`:**

```
Here's what I'm assuming before drafting:

Problem: [one-sentence problem statement derived from context]
Alternatives I'll consider:
  A) [option derived from engine reference]
  B) [option derived from CDD requirements]
  C) [option from common patterns]
CDD systems driving this: [list derived from context]
Dependencies: [upstream ADRs if any, otherwise "None"]
Status: Proposed

[A] Proceed — draft with these assumptions
[B] Change the alternatives list
[C] Adjust the CDD linkage
[D] Add a performance budget constraint
[E] Something else needs changing first
```

Resolve new material assumptions with the user; reuse already explicit decisions
in their exact approved scope. Do not guess unresolved choices.

**After engine specialist and TD reviews return** (Step 4.5/4.6), if unresolved
decisions remain, present each one as a separate `AskUserQuestion` with the proposed
options as choices plus a free-text escape:

```
Decision: [specific unresolved point]
[A] [option from specialist review]
[B] [alternative option]
[C] Different approach — I'll describe it
```

**ADR Dependencies** — derive from existing ADRs, then confirm:
- Does this decision depend on any other ADR not yet Accepted?
- Does it unlock or unblock any other ADR or epic?
- Does it block any specific epic from starting?

Record answers in the **ADR Dependencies** section. Write "None" for each field if no constraints apply.

---

## 4. Generate the ADR

Following this format:

```markdown
# ADR-[NNNN]: [Title]

## Status
Proposed

## Acceptance Record
[Pending for a new ADR. On separately authorized acceptance record actual authority,
date/time, exact retained reviewed original/revision/path + full SHA-256 and byte
size, accepted decision/implementation scope and exceptions. Preserve the reviewed
Proposed original and predecessor. Write approval is not acceptance.]

## Date
[Date of decision]

## Technology Compatibility

| Field | Value |
|-------|-------|
| **[游戏专用] Engine / [通用产品] Stack** | [e.g. Godot 4.6 / Django 5.1] |
| **Domain** | **[游戏专用]** [Physics / Rendering / UI / Audio / Navigation / Animation / Networking / Core / Input] **[通用产品]** [API Design / Data Storage / Auth / Caching / Messaging / Frontend / CLI / DevOps / Security] |
| **Knowledge Risk** | [LOW / MEDIUM / HIGH — from VERSION.md] |
| **References Consulted** | [List reference docs read, e.g. `docs/engine-reference/godot/modules/physics.md` or `docs/reference/django/modules/orm.md`] |
| **Post-Cutoff APIs Used** | [Any APIs from post-LLM-cutoff versions this decision depends on, or "None"] |
| **Verification Required** | [Specific behaviours to test before shipping, or "None"] |

## ADR Dependencies

| Field | Value |
|-------|-------|
| **Depends On** | [ADR-NNNN (must be Accepted before this can be implemented), or "None"] |
| **Enables** | [ADR-NNNN (this ADR unlocks that decision), or "None"] |
| **Blocks** | [Epic/Story name — cannot start until this ADR is Accepted, or "None"] |
| **Ordering Note** | [Any sequencing constraint that isn't captured above] |

## Context

### Problem Statement
[What problem are we solving? Why does this decision need to be made now?]

### Constraints
- [Technical constraints]
- [Timeline constraints]
- [Resource constraints]
- [Compatibility requirements]

### Requirements
- [Must support X]
- [Must perform within Y budget]
- [Must integrate with Z]

## Decision

[The specific technical decision made, described in enough detail for someone
to implement it.]

### Architecture Diagram
[ASCII diagram or description of the system architecture this creates]

### Key Interfaces
[API contracts or interface definitions this decision creates]

## Alternatives Considered

### Alternative 1: [Name]
- **Description**: [How this would work]
- **Pros**: [Advantages]
- **Cons**: [Disadvantages]
- **Rejection Reason**: [Why this was not chosen]

### Alternative 2: [Name]
- **Description**: [How this would work]
- **Pros**: [Advantages]
- **Cons**: [Disadvantages]
- **Rejection Reason**: [Why this was not chosen]

## Consequences

### Positive
- [Good outcomes of this decision]

### Negative
- [Trade-offs and costs accepted]

### Risks
- [Things that could go wrong]
- [Mitigation for each risk]

## CDD Requirements Addressed

| CDD System | Requirement | How This ADR Addresses It |
|------------|-------------|--------------------------|
| [system-name].md | [specific rule, formula, or performance constraint from that CDD] | [how this decision satisfies it] |

## Performance Implications
- **CPU**: [Expected impact]
- **Memory**: [Expected impact]
- **Load Time**: [Expected impact]
- **Network**: [Expected impact, if applicable]

## Migration Plan
[If this changes existing code, how do we get from here to there?]

## Validation Criteria
[How will we know this decision was correct? What metrics or tests?]

## Related Decisions
- [Links to related ADRs]
- [Links to related design documents]
```

4.5. **Technology Specialist Validation** — Before saving, spawn the appropriate specialist via Task to validate the drafted ADR:

**[游戏专用]** **Engine Specialist Validation**:
   - Read `standards/technical-preferences.md` `Engine Specialists` section to get the primary specialist
   - If no engine is configured (`[TO BE CONFIGURED]`), skip this step
   - Spawn `subagent_type: [primary specialist]` with: the ADR's Technology Compatibility section, Decision section, Key Interfaces, and the engine reference docs path. Ask them to:
     1. Confirm the proposed approach is idiomatic for the pinned engine version
     2. Flag any APIs or patterns that are deprecated or changed post-training-cutoff
     3. Identify engine-specific risks or gotchas not captured in the current ADR draft
   - If the specialist identifies a **blocking issue** (wrong API, deprecated approach, engine version incompatibility): revise the Decision and Technology Compatibility sections accordingly, then confirm the changes with the user before proceeding
   - If the specialist finds **minor notes** only: incorporate them into the ADR's Risks subsection

**[通用产品]** **Language Specialist Validation**:
   - Read `standards/technical-preferences.md` to determine the primary language specialist (python-specialist, typescript-specialist, rust-specialist, or go-specialist)
   - If no stack is configured, skip this step
   - Spawn the language specialist with: the ADR's Technology Compatibility section, Decision section, Key Interfaces, and the stack reference docs path. Ask them to:
     1. Confirm the proposed approach is idiomatic for the pinned framework version
     2. Flag any APIs or patterns that are deprecated or changed post-training-cutoff
     3. Identify stack-specific risks or gotchas not captured in the current ADR draft
   - If the specialist identifies a **blocking issue**: revise accordingly, then confirm with the user
   - If the specialist finds **minor notes** only: incorporate them into the ADR's Risks subsection

**Review mode check** — apply before spawning TD-ADR:
- `solo` → skip. Note: "TD-ADR skipped — Solo mode." Proceed to Step 4.7 (CDD sync check).
- `lean` → skip (not a PHASE-GATE). Note: "TD-ADR skipped — Lean mode." Proceed to Step 4.7 (CDD sync check).
- `full` → spawn as normal.

4.6. **Technical Director Strategic Review** — After the engine specialist validation, spawn `technical-director` via Task using gate **TD-ADR** (`standards/director-gates.md`):
   - Pass: the ADR file path (or draft content), engine version, domain, any existing ADRs in the same domain
   - The TD validates architectural coherence (is this decision consistent with the whole system?) — distinct from the engine specialist's API-level check
   - If CONCERNS or REJECT: revise the Decision or Alternatives sections accordingly before proceeding

4.7. **CDD Sync Check** — Before presenting the write approval, scan all CDDs
referenced in the "CDD Requirements Addressed" section for naming inconsistencies
with the ADR's Key Interfaces and Decision sections (renamed signals, API methods,
or data types). If any are found, surface them as a **prominent warning block**
immediately before the write approval — not as a footnote:

```
⚠️ CDD SYNC REQUIRED
[gdd-filename].md uses names this ADR has renamed:
  [old_name] → [new_name_from_adr]
  [old_name_2] → [new_name_2_from_adr]
The CDD must be updated before or alongside writing this ADR to prevent
developers reading the CDD from implementing the wrong interface.
```

If no inconsistencies: skip this block silently.

5. **Write authority** — Reuse existing exact scope after presenting the draft.
Only for uncovered effects use `AskUserQuestion` below:

If CDD sync issues were found:
- "ADR draft is complete. How would you like to proceed?"
  - [A] Write ADR + update CDD in the same pass
  - [B] Write ADR only — I'll update the CDD manually
  - [C] Not yet — I need to review further

If no CDD sync issues:
- "ADR draft is complete. May I write it?"
  - [A] Write ADR to `docs/architecture/adr-[NNNN]-[slug].md`
  - [B] Not yet — I need to review further

Within existing named scope write the new ADR as Proposed; ask only for uncovered
effects. For [A], name exact CDD paths/sections and update effects. For [B], retain
required synchronization action/owner and block affected implementation until
resolved; ADR writing alone does not settle the CDD conflict. Read back exact bytes.

**Acceptance is separate.** Only existing-governance acceptance authority may accept
the exact reviewed revision and scope. Capture the Acceptance Record and retain the
reviewed original before an authorized status transition. Specialist/TD approval,
tests, implemented code, content agreement and write approval do not accept ADRs.
Changed Accepted choices need a reviewed revision/successor preserving predecessor
and supersession history.

6. **Update Architecture Registry**

Scan the written ADR for candidate stances. Governing registry entries require
exact-scope acceptance; authorized Proposed entries stay explicitly tentative and
cannot override Accepted constraints. The registry write is a separate named effect.
Candidate categories:
- State it claims ownership of
- Interface contracts it defines (signal signatures, method APIs)
- Performance budget it claims
- API choices it makes explicitly
- Patterns it bans (Consequences → Negative or explicit "do not use X")

Present candidates:
```
Registry candidates from this ADR:
  NEW state ownership:      player_stamina → stamina-system
  NEW interface contract:   stamina_depleted signal
  NEW performance budget:   stamina-system: 0.5ms/frame
  NEW forbidden pattern:    polling stamina each frame (use signal instead)
  EXISTING (referenced_by update only): player_health → already registered ✅
```

**Registry append logic**: When writing to `docs/registry/architecture.yaml`, do NOT assume sections are empty. The file may already have entries from previous ADRs written in this session. Before each Edit call:
1. Read the current state of `docs/registry/architecture.yaml`
2. Find the correct section (state_ownership, interfaces, forbidden_patterns, api_decisions)
3. Append the new entry AFTER the last existing entry in that section — do not try to replace a `[]` placeholder that may no longer exist
4. If the section has entries already, use the closing content of the last entry as the `old_string` anchor, and append the new entry after it

**Registry writes need exact path/effect authority.** Reuse existing registry scope;
otherwise show entries and ask below.

Only for uncovered registry effects ask using `AskUserQuestion`:
- "May I update `docs/registry/architecture.yaml` with these [N] new stances?"
  - Options: "Yes — update the registry", "Not yet — I want to review the candidates", "Skip registry update"

Within authorized scope append entries. A changed governing stance requires an
Accepted reviewed revision/successor first; preserve old entry/history and add the
successor with exact identity. Proposed writing cannot supersede Accepted constraints.

---

## 7. Closing Next Steps

After the ADR is written (and registry optionally updated), close with `AskUserQuestion`.

Before generating the widget:
1. Read `docs/registry/architecture.yaml` — check if any priority ADRs are still unwritten (look for ADRs flagged in technical-preferences.md or module-index.md as prerequisites)
2. Check if all prerequisite ADRs are now written. If yes, include a "Start writing CDDs" option.
3. List ALL remaining priority ADRs as individual options — not just the next one or two.

Widget format:
```
ADR-[NNNN] written and registry updated. What would you like to do next?
[1] Write [next-priority-adr-name] — [brief description from prerequisites list]
[2] Write [another-priority-adr] — [brief description]  (include ALL remaining ones)
[N] Start writing CDDs — run `/design-system [first-undesigned-system]` (only show if all prerequisite ADRs are written)
[N+1] Stop here for this session
```

If there are no remaining priority ADRs and no undesigned CDD systems, offer only "Stop here" and suggest running `/architecture-review` in a fresh session.

**Always include this fixed notice in the closing output (do NOT omit it):**

> To validate ADR coverage against your CDDs, open a **fresh Codex session**
> and run `/architecture-review`.
>
> **Never run `/architecture-review` in the same session as `/architecture-decision`.**
> The reviewing agent must be independent of the authoring context to give an unbiased
> assessment. Running it here would invalidate the review.

List affected blocked Stories and recommend `/story-readiness` after exact-scope
acceptance and required synchronization. Neither ADR writing nor acceptance changes
Story status automatically. Later status writes need their own effect authority
and all remaining readiness checks.
