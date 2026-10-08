# Skill Test Spec: /dev-story

## Skill Summary

`/dev-story` loads exact Story/CDD/TR/decision/manifest inputs and implements
authorized code/test/evidence. It delegates specialist implementation, with the
documented direct Config/Data route. It does not invoke LP-CODE-REVIEW or mark
Stories Done/Complete; code review and closure are subsequent owning workflows.
Session writes need their own existing named effect scope.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: implementation summary, BLOCKED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (`/story-done`)
- [ ] Does not invent LP-CODE-REVIEW or automatic Story closure
- [ ] Documents specialist routing and its direct no-code Config/Data exception

---

## Director Gate Checks

No LP-CODE-REVIEW/closure gate runs inside this skill. Specialist routing and
implementation evidence are reported; /code-review and /story-done are separate.
Skipping optional/director modes never accepts ADRs or establishes completion.

---

## Test Cases

### Case 1: Happy Path — Scoped implementation and evidence, closure remains separate

**Fixture:**
- A story file exists at `production/epics/[layer]/story-[name].md` with:
  - `Status: Ready`
  - A TR-ID referencing a registered requirement
  - At least 2 Given-When-Then acceptance criteria
  - A test evidence path
- Referenced ADR has `Status: Accepted`
- `docs/architecture/control-manifest.md` exists
- `standards/technical-preferences.md` has engine and language configured
- `production/review-mode.txt` contains `full`

**Input:** `/dev-story production/epics/[layer]/story-[name].md`

**Expected behavior:**
1. Skill reads the story file and all referenced context
2. Skill verifies the ADR is Accepted (no block)
3. Skill routes implementation to the correct specialist agent
4. All acceptance criteria are verified as met
5. Implementation/evidence summary reports actual files and criteria
6. Existing authorization is reused; new effects require concrete approval
7. Story status is not set Complete; recommend code review then Story closure

**Assertions:**
- [ ] Skill reads story before spawning any agent
- [ ] ADR status is checked before implementation begins
- [ ] Implementation is delegated to a specialist agent (not done inline)
- [ ] Actual implementation/evidence coverage is reported with manual/deferred limits
- [ ] No invented LP-CODE-REVIEW gate is invoked
- [ ] No automatic Story status Complete/Done transition occurs
- [ ] Test file is written as part of implementation (not deferred)

---

### Case 2: Failure Path — Referenced ADR is Proposed

**Fixture:**
- A story file exists with `Status: Ready`
- The story's TR-ID points to a significant required proposed choice in an ADR with `Status: Proposed`

**Input:** `/dev-story production/epics/[layer]/story-[name].md`

**Expected behavior:**
1. Skill reads the story file
2. Skill resolves the TR-ID and reads the governing ADR
3. ADR status is Proposed — skill outputs a BLOCKED message
4. Skill names the specific ADR blocking the story
5. Skill recommends running `/architecture-decision` to advance the ADR
6. Implementation does NOT begin

**Assertions:**
- [ ] Skill does NOT begin implementation with a Proposed ADR
- [ ] BLOCKED message names the specific ADR number and title
- [ ] Skill recommends `/architecture-decision` as the next action
- [ ] Story status remains unchanged (not set to In Progress or Complete)

---

### Case 3: Ambiguous Acceptance Criteria — Skill asks for clarification

**Fixture:**
- A story file exists with `Status: Ready`
- Referenced ADR is Accepted
- One acceptance criterion is ambiguous (not Given-When-Then; uses subjective language like "feels responsive")

**Input:** `/dev-story production/epics/[layer]/story-[name].md`

**Expected behavior:**
1. Skill reads the story and identifies the ambiguous criterion
2. Before routing to the specialist, skill asks the user to clarify the criterion
3. User provides a concrete, testable restatement
4. Skill proceeds with implementation using the clarified criterion
5. Skill does NOT guess at the intended behavior

**Assertions:**
- [ ] Skill surfaces the ambiguous criterion before implementation starts
- [ ] Skill asks for user clarification (not auto-interpretation)
- [ ] Implementation begins only after clarification is provided
- [ ] Clarified criterion is used in the test (not the original vague version)

---

### Case 4: Edge Case — No argument; reads from session state

**Fixture:**
- No argument is provided
- `production/session-state/active.md` references an active story file
- That story file exists with `Status: In Progress`

**Input:** `/dev-story` (no argument)

**Expected behavior:**
1. Skill detects no argument is provided
2. Skill reads `production/session-state/active.md`
3. Skill finds the active story reference
4. Skill confirms with user: "Continuing work on [story title] — is that correct?"
5. After confirmation, skill proceeds with that story

**Assertions:**
- [ ] Skill reads session state when no argument is provided
- [ ] Skill confirms the active story with the user before proceeding
- [ ] Skill does NOT silently assume the active story without confirmation
- [ ] If session state has no active story, skill asks which story to implement

---

### Case 5: New material choice / manifest mismatch / session scope

**Fixture:** Implementable Game story, exact CDD/TR/Accepted scope, current complete
manifest identity. During implementation a significant state-ownership choice
appears; another fixture has same readable date but changed raw manifest bytes.

**Expected:** Stop affected implementation, record adr-required/conflict and route
architecture-decision before resuming; independent authorized work can continue.
Same-date mismatch and date-only records require LegacyRecheck of actual rules/
dependencies and authorized Story identity repair. No invented old bytes/digest.
Session state is written only within its named effect authority; code/test authority
does not imply session/status/T3 writes or Story completion.

**Assertions:**
- [ ] Original scope/limits pass to agents without new per-role permission.
- [ ] Valid cdd-layer/no-adr does not waive other prerequisites.
- [ ] No automatic Story closure or phase advancement.

---

## Protocol Compliance

- [ ] Delegates specialist code; documented direct Config/Data route respects the same scope
- [ ] Reads all context (story, TR-ID, ADR, manifest, engine prefs) before implementation
- [ ] Existing named code/test/evidence scope reused; ask only about uncovered effects
- [ ] Skipped gates noted by name and mode in output
- [ ] Updates session state only within existing named append/create authority
- [ ] Ends with next-step handoff: `/story-done`

---

## Exact scope and decision counterexamples

These are required semantic cases, not claims that keyword/static checks ran them.
Fixtures use actual UTF-8 bytes/complete dependencies and preserve Game/Product
owner requirements under `design/INSTRUCTIONS.md`.

- CDD-owned detail and local helper: classify cdd-layer/no-adr with named owner/
  reason; do not manufacture an ADR or waive CDD/TR/manifest/evidence prerequisites.
- Significant new trust/public-contract/durable-format/state-ownership choice:
  adr-required before affected implementation; independent scoped work may continue.
- Exact Accepted section conflicts with actual choice: conflict, named affected
  dependencies/action/owner; green tests or implemented status cannot establish covered.
- Content agreement, report/write permission or director APPROVED: no automatic
  ADR acceptance, Story readiness/completion or phase advancement.
- Historical approval with changed raw bytes/scope: retain history, do not reuse it
  as current approval. Preserve originals, full hashes/sizes/paths and UTC collection.
- Report-only saves only its new report; inputs/index/session/log/T3 effects require
  separate named scope. Review-only invokes no write entrypoint, including in memory.
- Unknown/both/neither domain: common checks continue, domain-specific findings
  remain incomplete until resolved; no silent Game fallback.
- Separate global Technical Setup min-three Foundation ADR rule remains in force;
  local no-ADR classifications neither waive it nor justify fabricated ADRs.

### Case 7: Required dependency facts cannot be synthesized from status or risk acceptance

**Fixture:** A required dependency is missing; another remains In Progress; a third
says Complete without the required closure evidence. The user says "accept risk" or
"it is done" and permits status writing, but provides no valid governance exception
or actual required closure proof.

**Expected:** All affected implementation remains Blocked, with no affected programmer.
Risk acceptance, status text, declaration or write permission cannot create closure.
Read exact dependency originals/evidence and route /story-done before any separately
authorized status effect. Independent authorized work may continue.

A valid existing-governance exact scoped exception variant permits only its declared
paths/effects/limits, preserving Incomplete dependency facts and named actions/risks.

- [ ] Missing required dependency is a blocker, not a warning followed by implementation.
- [ ] Fake Complete without actual required evidence does not pass the dependency check.
- [ ] No automatic dependency/Story closure or session write.

### Case 8: Legal no-ADR technical sources

A cdd-layer/no-adr Story binds a substantive exact CDD/local owner, active TR, current
manifest and configured VERSION/stack references. Read those real contracts/technology
sources; ADR-only Decision/Guidelines/Compatibility/Dependencies are justified N/A.
Send the same selected sources to the programmer. Missing required technology risk/
verification stays Blocked; never fabricate an ADR or waive remaining prerequisites.

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations, without
treating planning or uninvoked closure workflows as runtime execution.

### Case 9: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/dev-story [fixture Story path]` with each stated policy/evidence variant

**Expected behavior:**
1. Read the actual catalog, owning requirements and each variant's policy/authority/evidence.
2. Keep sufficiency, operation finish, execution, risk acceptance and completion separate.
3. Report only eligible scope and remaining required owner/actions.

**Assertions:**
- [ ] Default optional plan/team orchestration, every required AC/check actual PASS: no invented
      strict gate; optional follow-up retains owner/due phase.
- [ ] Explicit selected strict check unavailable: actual source/authority/scope recorded;
      NotRun/Blocked/Pending prevents dependent qualification/closure. Review mode or missing QA
      Context cannot silently invent/waive strict or passing status.
- [ ] One required AC untested (even below 50%) or Blocked Must Have: no eligible Story
      COMPLETE/COMPLETE WITH NOTES/done or all-complete message. Optional orchestration waives no
      required behavior. Planning cases/ADEQUATE review is not execution.
- [ ] Legacy COMPLETE WITH RISKS aliases NOTES only after every required actual PASS/
      decision/review/completion authority fact verified; original label preserved.
      Failed/unexecuted scope stays BLOCKED with separate risk acceptance.
- [ ] Report-only authority, self-review, explicit gate skip, unbound/stale evidence, missing
      original or Unknown scope leaves required dependent findings incomplete; no index/state/phase
      repair or broadened partial-scope approval.
- [ ] Exact permitted historical results retain original runtime/observer/inputs/scope and
      historical label, never this run's execution. Performance, required distinct sessions, target-
      platform/Product qualification need actual bound observations; file counts/keywords/line
      quotes/assumptions do not prove them.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 10: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A separate
variant has actual conflicting policy or unresolved required applicability.

**Input:** `/dev-story [fixture Story path]` under the stated scope

**Expected behavior:**
1. Read actual catalog/defaults and required owning inputs.
2. Continue unaffected work without initializing optional context.

**Assertions:**
- [ ] No Memory Bank/QA Context exists and no explicit strict selection is recorded: use actual
      catalog default optional orchestration, disclose optional absence and continue required
      Story/DoD/evidence checks. Do not invent Unknown policy, a strict gate, passing execution,
      initialization or stage/closure authority. Actual conflicting policy or unresolved required
      applicability remains Unknown for dependent claims.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 11: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant authorizes only a report, excluding inputs/index/status/closure; another
introduces a materially new effect. Current input identities are supplied.

**Input:** `/dev-story [fixture Story path]` under the stated scope

**Expected behavior:**
1. Match current inputs and planned effects to the retained approval.
2. Execute covered effects and request only missing material scope.

**Assertions:**
- [ ] An existing user-authorized changeset already names this exact output path and create/update
      effect. Reuse that authority through roles/retries and proceed after required facts/reviews
      pass; do not ask "May I write" again for the same scope. Missing authority or a materially new
      path/effect asks once after a concrete draft. A new report alone does not cover
      input/index/status/closure effects; director or content approval does not independently
      authorize writes.

**Case Verdict:** PASS / FAIL / PARTIAL

## Coverage Notes

- Engine routing logic (Godot vs Unity vs Unreal) is not tested per engine —
  the routing pattern is consistent; engine selection is a config fact.
- Visual/Feel and UI story types (no automated test required) have different
  evidence requirements and are not covered in these cases.
- Integration story type follows the same pattern as Logic but with a different
  evidence path — not independently fixture-tested.
