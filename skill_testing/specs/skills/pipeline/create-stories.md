# Skill Test Spec: /create-stories

## Skill Summary

`/create-stories` breaks a single epic into developer-ready story files. It reads
the EPIC.md, the corresponding CDD, governing ADRs, the control manifest, and the
TR registry. Each story gets structured frontmatter including: Title, Epic, Layer,
Priority, Status, TR-ID, ADR references, Acceptance Criteria, and Definition of
Done. Stories are classified by type (Logic / Integration / Visual/Feel / UI /
Config/Data) which determines the required test evidence path.

In `full` review mode, a QL-STORY-READY check reviews the full decomposed list before write approval. In
`lean` or `solo` mode, QL-STORY-READY is skipped. The skill asks "May I write"
only for uncovered named story-set/EPIC effects, reusing exact existing authority.
Stories are written to
`production/epics/[epic-slug]/story-NNN-[name].md`.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED, NEEDS WORK
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (`/story-readiness`, `/dev-story`)
- [ ] Documents story Status: Blocked when governing ADR is Proposed
- [ ] Documents QL-STORY-READY gate: active in full mode, skipped in lean/solo

---

## Director Gate Checks

In `full` mode: QL-STORY-READY check reviews the full decomposed list before write approval. Stories that
fail the check are noted as NEEDS WORK before the "May I write" ask.

In `lean` mode: QL-STORY-READY is skipped. Output notes:
"QL-STORY-READY skipped — lean mode" for the resolved run; no invented per-story gate invocations.

In `solo` mode: QL-STORY-READY is skipped with equivalent notes.

---

## Test Cases

### Case 1: Happy Path — Epic with 3 stories, all ADRs Accepted

**Fixture:**
- `production/epics/[epic-slug]/EPIC.md` exists with 3 CDD requirements
- Corresponding CDD exists with matching acceptance criteria
- All governing ADRs have `Status: Accepted`
- `docs/architecture/control-manifest.md` exists
- `docs/architecture/tr-registry.yaml` has TR-IDs for all 3 requirements
- `production/review-mode.txt` contains `lean`

**Input:** `/create-stories [epic-name]`

**Expected behavior:**
1. Skill reads EPIC.md, CDD, governing ADRs, control manifest, and TR registry
2. Classifies each requirement into a story type (Logic / Integration / Visual/Feel / UI / Config/Data)
3. Drafts 3 story files with correct frontmatter schema
4. QL-STORY-READY is skipped (lean mode) — noted in output
5. Reuses exact story-set/EPIC authority; asks "May I write" only for uncovered effects
6. Writes all 3 story files after approval

**Assertions:**
- [ ] Each story's frontmatter contains: Title, Epic, Layer, Priority, Status, TR-ID, ADR reference, Acceptance Criteria, DoD
- [ ] Story types are correctly classified (at least one Logic type in fixture)
- [ ] Exact story-set/EPIC scope is reused; one concrete approval covers new named effects
- [ ] QL-STORY-READY skip is noted in output
- [ ] All 3 story files are written with correct naming: `story-[name].md`
- [ ] Skill does NOT start implementation

---

### Case 2: Failure Path — No epic file found

**Fixture:**
- The epic path provided does not exist in `production/epics/`

**Input:** `/create-stories nonexistent-epic`

**Expected behavior:**
1. Skill attempts to read the EPIC.md file
2. File not found
3. Skill outputs a clear error with the path it searched
4. Skill suggests checking `production/epics/` or running `/create-epics` first
5. No story files are created

**Assertions:**
- [ ] Skill outputs a clear error naming the missing file path
- [ ] No story files are written
- [ ] Skill recommends the correct next action (`/create-epics`)
- [ ] Skill does NOT create stories without a valid EPIC.md

---

### Case 3: Blocked Story — ADR is Proposed

**Fixture:**
- EPIC.md exists with 2 requirements
- Requirement 1 is covered by an Accepted ADR
- Requirement 2 has a required proposed choice in an ADR with `Status: Proposed`
- Other required CDD/TR/manifest/evidence prerequisites actually pass for Requirement 1

**Input:** `/create-stories [epic-name]`

**Expected behavior:**
1. Skill reads the ADR for Requirement 2 and finds Status: Proposed
2. Story for Requirement 2 is drafted with `Status: Blocked`
3. Blocking note references the specific ADR: "BLOCKED: ADR-NNN is Proposed"
4. Story for Requirement 1 is drafted normally with `Status: Ready`
5. Both qualified drafts are shown; reuse exact story-set scope or ask for new effects

**Assertions:**
- [ ] Story 2 has `Status: Blocked` in its frontmatter
- [ ] Blocking note names the specific ADR number and recommends `/architecture-decision`
- [ ] Story 1 has `Status: Ready` — blocked status does not affect non-blocked stories
- [ ] Blocked status is shown in the draft preview before writing
- [ ] Both story files are written (blocked stories are still written — just flagged)

---

### Case 4: Edge Case — No argument provided

**Fixture:**
- `production/epics/` directory exists with ≥2 epic subdirectories

**Input:** `/create-stories` (no argument)

**Expected behavior:**
1. Skill detects no argument is provided
2. Asks which epic to decompose and lists actual epics; no silent selection
3. Skill lists available epics from `production/epics/`
4. No story files are created

**Assertions:**
- [ ] Skill asks which epic when no argument is given
- [ ] Skill lists available epics to help the user choose
- [ ] No story files are written
- [ ] Skill does NOT silently pick an epic without user input

---

### Case 5: Director Gate — Full mode runs QL-STORY-READY; stories failing noted as NEEDS WORK

**Fixture:**
- EPIC.md exists with 2 requirements
- Both governing ADRs are Accepted
- `production/review-mode.txt` contains `full`
- QL-STORY-READY check finds one story has ambiguous acceptance criteria

**Input:** `/create-stories [epic-name]`

**Expected behavior:**
1. Both stories are drafted
2. QL-STORY-READY check runs for the decomposed list before writes
3. Story 1 passes QL-STORY-READY
4. Story 2 fails QL-STORY-READY — noted as NEEDS WORK with specific feedback
5. Both stories are shown to user with pass/fail status before "May I write"
6. User can proceed (story written as-is with NEEDS WORK note) or revise first

**Assertions:**
- [ ] QL-STORY-READY results appear per story in the output
- [ ] Story 2 is flagged as NEEDS WORK with the specific failing criteria
- [ ] Story 1 shows as passing QL-STORY-READY
- [ ] User is given the choice to proceed or revise before writing
- [ ] Skill does NOT auto-block writing of stories that fail QL-STORY-READY without user input

---

## Protocol Compliance

- [ ] All context (EPIC, CDD, ADRs, manifest, TR registry) loaded before drafting stories
- [ ] Story drafts shown in full before any "May I write" ask
- [ ] Existing named story-set/EPIC authority persists; ask only for uncovered effects
- [ ] Blocked stories flagged before write approval — not discovered after writing
- [ ] TR-IDs reference the registry — specific CDD requirement/criteria and exact CDD/TR identities are recorded
- [ ] Control manifest rules quoted per-story from the manifest, not invented
- [ ] Ends with next-step handoff: `/story-readiness` → `/dev-story`

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

### Case 6: No-ADR story and raw manifest identity

Exact CDD body/current active TR plus justified cdd-layer/no-adr can produce a
scoped draft without an invented governing ADR. Required missing/Proposed decisions
block affected drafts; other stories continue. Missing TR is unassigned/Blocked,
never TR-??? fabricated as active. Each Story stores complete manifest SHA-256,
byte size/path/time beside the legacy readable date. Same-day change/date-only
LegacyRecheck requires current rule/dependency review and authorized identity repair.
Story creation and EPIC table updates require named effects, with no implementation.

### Case 7: Actual input status, legal no-ADR source and resolved mode

**Fixture:** One Game CDD-owned detailed rule has a real TR-ID and justified cdd-layer;
a local no-adr helper has an exact owner/reason. Both use configured VERSION/reference
evidence, and current complete manifest SHA-256/size. Another affected draft lacks a
required Accepted input; a variant has unknown required technology risk.

**Expected:** Do not fabricate ADR compatibility/Knowledge Risk sections. Record real
CDD/local/reference sources and justified N/A ADR-only fields. Missing Accepted input
or required risk evidence keeps affected drafts Blocked, never "all confirmed present."
Closing write outcome reports actual Draft/Blocked/Ready counts and findings.

- [ ] Missing override and missing global mode resolve lean once.
- [ ] Explicit valid full/lean/solo overrides the actual global mode.
- [ ] Invalid explicit/global values require correction; no fallback or gate claim.
- [ ] Legal cdd-layer/no-adr does not waive CDD/TR/manifest/readiness/evidence checks.

### QA provenance counterexample (no QA-policy change)

Lean/solo skip or unavailable QA produces no qa-lead-authored test plan. Story
`QA Test Cases` records actual author/source and Completed/Skipped/NotRun/Blocked
state; absent plan/action remains explicit under applicable Story checks. Full-mode
actual qa-lead output may be embedded with its original identity. Never infer QA
execution from a template label. Default/strict evidence policy belongs to its owner.

### Implementation-note source label counterexample

A legitimate cdd-layer/no-adr Story's Implementation Notes label names its actual
substantive CDD/local owner contract and exact path/section/identity, with justified
N/A ADR-only fields. It must not label those notes as ADR-NNNN Guidelines. Covered
uses the actual governing Accepted ADR Guidelines. Other readiness checks remain.

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations, without
treating planning or uninvoked closure workflows as runtime execution.

### Case 8: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/create-stories [fixture epic]` with each stated policy/evidence variant

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

### Case 9: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A separate
variant has actual conflicting policy or unresolved required applicability.

**Input:** `/create-stories [fixture epic]` under the stated scope

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

### Case 10: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant authorizes only a report, excluding inputs/index/status/closure; another
introduces a materially new effect. Current input identities are supplied.

**Input:** `/create-stories [fixture epic]` under the stated scope

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

- Integration story test evidence (playtest doc alternative) follows the same
  approval pattern as Logic stories — not independently fixture-tested.
- Story ordering (foundational first, UI last) is validated implicitly via
  Case 1's multi-story fixture.
- The story sizing rule (splitting large requirement groups) is not tested here
  — it is addressed in the `/create-stories` skill's internal logic.
