---
name: architecture-review
description: "Use this skill when module CDDs and ADRs need a pre-implementation architecture audit for traceability gaps, conflicts, technology compatibility, and a PASS/CONCERNS/FAIL verdict."
argument-hint: "[focus: full | coverage | consistency | compatibility | engine | single-cdd path/to/cdd.md | rtm | architecture-file-path]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Task, AskUserQuestion
agent: technical-director
model: opus
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

## Progressive reading and review controls

Resolve reference paths relative to this package; read only those required by
the selected mode/phase. Referencing is not reading. Missing, unread or truncated
required material makes the affected step INCOMPLETE; complete consecutive
bounded reads before depending on it. Ship these references with either platform
entry and keep required neutral owners available locally for offline use.

An author's self-check, specialist consultation or new conversation/window alone
does not establish independent review. Where the selected workflow requires it,
use a separate reviewer of the exact bound inputs, without repair; unavailable
required review remains incomplete. No automatic acceptance or scope reduction.

## User Guide

- When to use: Validates completeness and consistency of the project architecture against all CDDs. Builds a traceability matrix recording each CDD technical requirement's justified disposition and exact governing owner, identifies coverage gaps, detects cross-ADR conflicts, verifies technology compatibility consistency across all decisions, and produces a PASS/CONCERNS/FAIL verdict. Supports both game and general product domains.
- Inputs: Command arguments: `/architecture-review [focus: full | coverage | consistency | compatibility | single-cdd path/to/cdd.md]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: Only when Memory Bank is initialized and each named write effect is covered: `memory_bank/t3_archive/reviews/review-index.md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Architecture Review

The architecture review validates that the complete body of architectural decisions
covers all game design requirements, is internally consistent, and correctly targets
the project's pinned engine version. It is the quality gate between Technical Setup
and Pre-Production.

**Domain detection.** The concept document at `design/cdd/` reveals the domain.
Sections below are marked **[通用场景]**, **[游戏专用]**, or **[通用产品]**.

**Argument modes:**
- **No argument / `full`**: Full review — all phases
- **`coverage`**: Traceability/dispositions — requirements or choices lacking justified current coverage
- **`consistency`**: Cross-ADR conflict detection only
- **`compatibility`**: Technology compatibility audit only (engine or stack)
- **`engine`**: Legacy game compatibility alias
- **Architecture file path**: Preserve legacy direct-path invocation; read that body
  and required CDD/decision dependencies. Missing path means incomplete input,
  never a fabricated passing verdict.
- **`single-cdd [path]`**: Review architecture coverage for one specific CDD
- **`rtm`**: Requirements Traceability Matrix — extends the standard matrix
  to include story file paths and test file paths; outputs
  `docs/architecture/requirements-traceability.md` with the full
  CDD requirement → exact Accepted decision or justified CDD/local disposition → Story → evidence chain. Use in Production phase when
  stories and tests exist.

---

## Phase 1: Load Everything

Read [Mode-Specific Evidence Loading](references/evidence-loading.md) before
collecting inputs for the selected mode. L0 summaries locate scope; they never
replace complete bodies required by that mode. Full/no-argument and coverage
retain every in-scope CDD, module-index, ADR and applicable technology/standards
input; direct-path and single-cdd retain their actual dependency closure. Resolve
uncertain applicability before skipping an inventory. Missing required originals
leave affected checks incomplete, never a narrowed passing review.

---

## Phase 2: Extract Technical Requirements from Every CDD

### Pre-load the TR Registry

All Phase 2 ID/text changes are read-only proposals until authorized Phase 8 writes.
Before extracting any requirements, read `docs/architecture/tr-registry.yaml`
if it exists. Index existing entries by `id` and by normalized `requirement`
text (lowercase, trimmed). This prevents ID renumbering across review runs.

For each requirement you extract, the matching rule is:
1. **Exact/near match** to an existing registry entry for the same system →
   reuse that entry's TR-ID unchanged. Update the `requirement` text in the
   registry only if the CDD wording changed (same intent, clearer phrasing) —
   add a `revised: [date]` field.
2. **No match** → assign a new ID: next available `TR-[system]-NNN` for that
   system, starting from the highest existing sequence + 1.
3. **Ambiguous** (partial match, intent unclear) → ask the user:
   > "Does '[new requirement text]' refer to the same requirement as
   > `TR-[system]-NNN: [existing text]'`, or is it a new requirement?"
   User answers: "Same requirement" (reuse ID) or "New requirement" (new ID).

For any requirement with `status: deprecated` in the registry — skip it.
It was removed from the CDD intentionally.

For each CDD, read it and extract all **technical requirements** — things the
architecture must provide for the system to work. A technical requirement is any
statement relevant to architecture or a CDD-owned detailed contract; classify before requiring an ADR.

Categories to extract:

| Category | Example |
|----------|---------|
| **Data structures** | "Each entity has health, max health, status effects" → needs a component/data schema |
| **Performance constraints** | "Collision detection must run at 60fps with 200 entities" → physics budget ADR |
| **Engine capability** | "Inverse kinematics for character animation" → IK system ADR |
| **Cross-system communication** | "Damage system notifies UI and audio simultaneously" → event/signal architecture ADR |
| **State persistence** | "Player progress persists between sessions" → save system ADR |
| **Threading/timing** | "AI decisions happen off the main thread" → concurrency ADR |
| **Platform requirements** | "Supports keyboard, gamepad, touch" → input system ADR |

For each CDD, produce a structured list:

```
CDD: [filename]
System: [system name]
Technical Requirements:
  TR-[CDD]-001: [requirement text] → Domain: [Physics/Rendering/etc]
  TR-[CDD]-002: [requirement text] → Domain: [...]
```

This becomes the **requirements baseline** — the complete set of what the
architecture must cover.

---

## Phase 3: Build the Traceability Matrix

For every requirement/choice read governing CDD bodies, Notes, ADRs and actual
in-scope implementation/evidence when present. Missing ADR links never skip review.
Apply the shared dispositions: `covered` requires exact Accepted revision/section/
scope; `cdd-layer` cites its detailed contract owner; `no-adr` states local reason/
owner; `documentation-update` names factual repairs; `adr-required` resolves the
significant choice before affected implementation; `conflict` resolves with its owner.

Build a matrix with named CDD path/section, existing TR-ID or unassigned requirement,
choice/disposition, exact Accepted scope or no-ADR reason, evidence, affected paths/
dependencies and remaining action/owner. Preserve the Game examples:

| Requirement ID | CDD | System | Requirement | Coverage / disposition |
|---|---|---|---|---|
| TR-combat-001 | combat.md | Combat | Hitbox detection < 1 frame | ADR-0003 exact Accepted scope: covered |
| TR-combat-002 | combat.md | Combat | Combo window timing | CDD detailed rule: cdd-layer, verify evidence |
| TR-inventory-001 | inventory.md | Inventory | Persistent item storage | ADR-0005 exact Accepted scope: covered |

Count each disposition/incomplete check. Only significant `adr-required` choices
create ADR gaps; justified CDD/local coverage does not require manufactured ADRs.
No-ADR coverage removes no Story/test/manifest/global Technical Setup prerequisite.

---

## Phase 3b: Story and Test Linkage (rtm and applicable full mode)

*Skip this phase unless the argument is `rtm` or `full` with stories present.*

Run this phase for `rtm` and for `full` when Stories are actually present. If a
full run's Story scope is unresolved, retain Unknown and resolve it before skipping
this phase; missing required files cannot establish a skip. Read the real Story/test
linkage and decision/evidence sources required below.

This phase extends the Phase 3 matrix to include the story that implements
each requirement and the test that verifies it — producing the full
Requirements Traceability Matrix (RTM).

Before linking Stories/tests, Read Phase 3b in
[Mode-Specific Evidence Loading](references/evidence-loading.md). Load actual
Stories, test evidence and configured runner/discovery; directly Read each declared
test original even when discovery excludes it. Confirm absence before MISSING;
unread/inaccessible/unresolved inputs are INCOMPLETE, and discovery is not PASS.

### Step 3b-3 — Build the extended RTM

For each TR-ID in the Phase 3 matrix, add:
- **Story**: the story file path(s) that reference this TR-ID (may be multiple)
- **Test File**: the test file path stated in the story's Test Evidence section
- **Test Status**: LINKED / NOT RUN (file exists), PASS/FAIL only from actual
  identified execution evidence, MISSING (confirmed absent required original),
  INCOMPLETE (unread, inaccessible or unresolved original/discovery),
  NONE (justified manual evidence type), or NO STORY. Exact test/report identities
  are required; existence is not PASS.

Before presenting the extended matrix, Read the Phase 3b display in
[Extended RTM Formats](references/rtm-format.md). Show the full requirement,
disposition, Story, exact test and actual-status chain, retaining justified
manual NONE and unimplemented NO STORY cases.

RTM coverage summary:
- VERIFIED: [N] — justified disposition + Story + exact passing required evidence; count LINKED / NOT RUN separately
- LINKED / NOT RUN: [N] — exact test original available, execution not established
- MISSING test: [N] — confirmed absent required test original
- INCOMPLETE: [N] — required original or runner discovery unread, inaccessible or unresolved
- NO STORY: [N] — requirements with ADR but no story yet
- ADR REQUIRED: [N] — significant choices without Accepted scope; cdd-layer/no-adr count separately
- Full chain verified: [N/total] ([%]); report unknowns without inferring execution from paths

---

## Phase 4: Cross-ADR Conflict Detection

Before presenting these findings, Read the Phase 4 section of
[Architecture Finding Formats](references/finding-formats.md).

Compare every ADR against every other ADR to detect contradictions. A conflict
exists when:

- **Data ownership conflict**: Two ADRs claim exclusive ownership of the same data
- **Integration contract conflict**: ADR-A assumes System X has interface Y, but
  ADR-B defines System X with a different interface
- **Performance budget conflict**: ADR-A allocates N ms to physics, ADR-B allocates
  N ms to AI, together they exceed the total frame budget
- **Dependency cycle**: ADR-A says System X initialises before Y; ADR-B says Y
  initialises before X
- **Architecture pattern conflict**: ADR-A uses event-driven communication for a
  subsystem; ADR-B uses direct function calls to the same subsystem
- **State management conflict**: Two ADRs define authority over the same game state
  (e.g. both Combat ADR and Character ADR claim to own the health value)

For each conflict, show both exact ADR claims, type, impact and resolution
options using the Phase 4 Conflicts format in the finding reference.

### ADR Dependency Ordering

After conflict detection, analyse the dependency graph across all ADRs:

1. **Collect all `Depends On` fields** from every ADR's "ADR Dependencies" section
2. **Topological sort**: Determine the correct implementation order — ADRs with no
   dependencies come first (Foundation), ADRs that depend on those come next, etc.
3. **Flag unresolved dependencies**: If ADR-A's "Depends On" field references an ADR
   that is still `Proposed` or does not exist, flag it:
   ```
   ⚠️  ADR-0005 depends on ADR-0002 — but ADR-0002 is still Proposed.
       ADR-0005 cannot be safely implemented until ADR-0002 is Accepted.
   ```
4. **Cycle detection**: If ADR-A depends on ADR-B and ADR-B depends on ADR-A (directly
   or transitively), flag it as a `DEPENDENCY CYCLE`:
   ```
   🔴 DEPENDENCY CYCLE: ADR-0003 → ADR-0006 → ADR-0003
      This cycle must be broken before either can be implemented.
   ```
5. **Output recommended implementation order**: show the topological Foundation,
   dependent and Feature layers with their prerequisite IDs, using the Phase 4
   dependency-order display in the finding reference. Preserve unresolved/cyclic
   dependencies as findings rather than silently ordering them away.

---

## Phase 5: Technology Compatibility Cross-Check

Before presenting these findings, Read the Phase 5 section of
[Architecture Finding Formats](references/finding-formats.md).

Across all ADRs, check for technology consistency.

**[游戏专用]** Engine checks:

### Version Consistency
- Do all ADRs that mention an engine version agree on the same version?
- If any ADR was written for an older engine version, flag it as potentially stale

### Post-Cutoff API Consistency
- Collect all "Post-Cutoff APIs Used" fields from all ADRs
- For each, verify against the relevant module reference doc
- Check that no two ADRs make contradictory assumptions about the same post-cutoff API

### Deprecated API Check
- Grep all ADRs for API names listed in `deprecated-apis.md`
- Flag any ADR referencing a deprecated API

### Missing Compatibility Sections
- List all ADRs that are missing the Technology Compatibility section entirely
- These are blind spots — their technology assumptions are unknown

**[通用产品]** Stack checks (same structure, stack reference docs):

### Version Consistency
- Do all ADRs that mention a stack version agree on the same version?

### Post-Cutoff API Consistency
- Collect all "Post-Cutoff APIs Used" fields, verify against stack reference docs

### Deprecated API Check
- Grep ADRs for API names listed in stack `deprecated-apis.md`

### Missing Compatibility Sections
- List ADRs missing the Technology Compatibility section

Present technology/version, compatibility-section coverage, deprecated/stale
references and API conflicts using the Phase 5 format in the finding reference.

---

### Technology Specialist Consultation

When Phase 5 compatibility auditing applies, Read
[Technology Specialist Consultation](references/specialist-consultation.md)
before resolving the configured Game engine or Product language specialist and
issuing that consultation. An actually unconfigured engine/stack permits the
specified skip; an unavailable configured consultation stays incomplete. Include
specialist findings with the same weight as audit findings. Consultation or a new
window alone does not establish independent review of the exact changeset.

---

## Phase 5b: Design Revision Flags (Architecture → CDD Feedback)

Before presenting these findings, Read the Phase 5b section of
[Architecture Finding Formats](references/finding-formats.md).

For each **HIGH RISK technology finding** from Phase 5, check whether any CDD
makes an assumption that verified technology behaviour contradicts.

Specific cases to check:

1. **Post-cutoff API behaviour differs from training-data assumptions**: If an ADR
   records a verified API behaviour that differs from the default LLM assumption,
   check all CDDs that reference the related system. Look for design rules written
   around the old (assumed) behaviour.

2. **Known technology limitations in ADRs**: If an ADR records a known engine,
   framework, runtime, database, or platform limitation, check CDDs that design
   behavior around the affected capability.

3. **Deprecated API conflicts**: If Phase 5 flagged a deprecated API used in an ADR,
   check whether any CDD contains mechanics, workflows, data contracts, or module
   behavior that assumes the deprecated API's behaviour.

For each conflict, record the CDD, assumption, verified reality/owner and
required revision using the Phase 5b format in the finding reference.

If no revision flags are found, write: "No CDD revision flags — all CDD assumptions
are consistent with verified technology behaviour."

Ask: "Should I flag these CDDs for revision in the module index?"
- If yes: update the relevant systems' Status field to "Needs Revision"
  and add a short inline note in the adjacent Notes/Description column explaining the conflict.
  Ask for approval before writing.
  (Do NOT use parentheticals like "Needs Revision (Architecture Feedback)" — other skills
  match the exact string "Needs Revision" and parentheticals break that match.)

---

## Phase 6: Architecture Document Coverage

If `docs/architecture/architecture.md` exists, validate it against CDDs:

- Does every system from `module-index.md` appear in the architecture layers?
- Does the data flow section cover all cross-system communication defined in CDDs?
- Do the API boundaries support all integration requirements from CDDs?
- Are there systems in the architecture doc that have no corresponding CDD
  (orphaned architecture)?

---

## Phase 7: Output the Review Report

Before presenting the report, Read Phase 7 in
[Review and Traceability Report Formats](references/report-formats.md).
Present the complete findings/disposition matrix, per-area results, counts,
blocking dependencies and required/advisory actions before the verdict:

- **PASS**: Every in-scope requirement/choice has current justified disposition
  and evidence; no unresolved required decision/conflict; technology consistent.
- **CONCERNS**: Only permitted advisory repairs remain with owner/due phase.
- **FAIL**: Required `adr-required`/`conflict` or incomplete required evidence;
  name affected dependencies and continue independent checks.

Neither a summary scan nor a report format reduces the complete selected review.

---

## Phase 8: Write and Update Traceability Index

Review-only stays read-only, including no in-memory write entrypoint. Report-only
writes only its assigned new report. Reuse existing named effects; for new effects
show the concrete changeset and use `AskUserQuestion` for approval:
- "Review complete. What would you like to write?"
  - [A] Write all three files (review report + traceability index + TR registry)
  - [B] Write review report only — `docs/architecture/architecture-review-[date].md`
  - [C] Don't write anything yet — I need to review the findings first

### RTM Output (rtm mode only)

For `rtm` mode, reuse existing exact matrix effect authority. Only for uncovered
effects additionally ask: "May I write the full Requirements Traceability
Matrix to `docs/architecture/requirements-traceability.md`?"

Before the authorized RTM write, Read the Phase 8 saved format in
[Extended RTM Formats](references/rtm-format.md). Preserve full matrix, status
counts/denominator, layer-prioritized gaps and history. Paths/coverage do not
establish execution or PASS.

### TR Registry Update

Only if the registry effect is not already covered, ask: "May I update
`docs/architecture/tr-registry.yaml` with these proposed IDs/repairs?"
Report-only approval never covers this. IDs remain prospective until the authorized
registry update is read back; never claim fabricated active registration.

If yes:
- **Append** any new TR-IDs that weren't in the registry before this review
- **Update** `requirement` text and `revised` date for any entries whose CDD
  wording changed (ID stays the same)
- **Mark** `status: deprecated` for any registry entries whose CDD requirement
  no longer exists (confirm with user before marking deprecated)
- **Never** renumber or delete existing entries
- Update the `last_updated` and `version` fields at the top

This ensures all future story files can reference stable TR-IDs that persist
across every subsequent architecture review.

### Reflexion Log Update

Only within separately authorized log-append scope, add identified 🔴 CONFLICT
entries to `docs/consistency-failures.md` if it exists. Report approval does not
permit the log effect; otherwise retain action/owner in the report:

Before an authorized log append, Read the Reflexion log entry in
[Optional Closure Write Formats](references/closure-formats.md).

Only append CONFLICT entries — do not log GAP entries (missing ADRs are expected
before the architecture is complete). Do not create the file if missing — only
append when it already exists.

### Session State Update

Only within its authorized path/append effect, update
`production/session-state/active.md`; otherwise give the summary in conversation:

Before an authorized session update, Read the Session extract in
[Optional Closure Write Formats](references/closure-formats.md).

Create `active.md` only if creation is authorized. Confirm actual writes only;
otherwise report the pending effect without writing.

### Memory Bank Review Index

When `memory_bank/` exists, update its index/pointer only within separately covered
effect authority. Report-only approval does not cover this write. Bind entries to
immutable report revisions and exact reviewed input manifests.

Update the Memory Bank index only after the report is saved and only with authority
for that named index effect. Initialization alone, read-only scope and report-only
scope do not authorize it. If initialization or the intended effect is unresolved,
retain Unknown and leave the index unchanged. Before an authorized update, read
the saved immutable report revision and its exact input/evidence identities;
a proposed report or an INFO result is insufficient. This step does not initialize
Memory Bank.

- Review Type: `architecture-review`
- Source Artifact: `docs/architecture/architecture-review-[date].md`
- Use `Source Artifact` as the dedupe key.
- If the same source artifact already exists, update Date, Verdict, and
  Follow-up Owner instead of adding a duplicate row.
- If `memory_bank/` does not exist, do not create it from
  `/architecture-review`; keep the existing report behavior and say:
  "Run `/constitute` to establish the memory_bank governance control plane."

Before an authorized traceability-index write, Read the Phase 8 index format in
[Review and Traceability Report Formats](references/report-formats.md). Include
the complete Phase 3 matrix, coverage, known gaps and superseded requirements.
Read back each actual approved write; record pending/failed effects separately.

---

## Phase 9: Handoff

After completing the review and writing approved files, present:

1. **Immediate actions**: List the top 3 ADRs to create (highest-impact gaps first,
   Foundation layer before Feature layer)
2. **Gate guidance**: "When all blocking issues are resolved, run `/gate-check pre-production` to advance"
3. **Rerun trigger**: "Re-run `/architecture-review` after each new ADR is written
   to verify coverage improves"

Then close with `AskUserQuestion`:
- "Architecture review complete. What would you like to do next?"
  - [A] Write a missing ADR — open a fresh session and run `/architecture-decision [system]`
  - [B] Run `/gate-check pre-production` — if all blocking gaps are resolved
  - [C] Stop here for this session

---

## Error Recovery Protocol

If any spawned agent returns BLOCKED, errors, or fails to complete:

1. **Surface immediately**: Report "[AgentName]: BLOCKED — [reason]" before continuing
2. **Assess dependencies**: If the blocked agent's output is required by a later phase, do not proceed past that phase without user input
3. **Offer options** via AskUserQuestion with three choices:
   - Skip this agent and note the gap in the final report
   - Retry with narrower scope (fewer CDDs, single-system focus)
   - Stop here and resolve the blocker first
4. **Always produce a partial report** — output whatever was completed so work is not lost

---

## Collaborative Protocol

1. **Read silently** — do not narrate every file read
2. **Show the matrix** — present the full traceability matrix before asking for
   anything; let the user see the state
3. **Don't guess** — if a requirement is ambiguous, ask: "Is [X] a technical
   requirement or a design preference?"
4. **Scope before writing** — reuse covered effects; show drafts for new ones
5. **Affected blockers** — unresolved required decisions/conflicts block affected
   implementation unless existing governance permits an explicit scoped exception.
   Record authority/risks without relabeling findings; no automatic PASS.

## Exact-byte check availability

Use available read-only tools to collect complete raw-file SHA-256/byte size without
normalizing line endings. If exact bytes/digest or a required dependency cannot be
read, report the affected check incomplete; do not substitute a date, text rendering,
short hash or file existence. Analysis invokes no write entrypoint.
