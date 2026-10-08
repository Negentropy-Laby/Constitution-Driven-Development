# Skill Test Spec: /qa-plan

## Skill Summary

`/qa-plan` generates a structured QA test plan for a feature or sprint milestone.
It reads story files for the specified sprint, extracts acceptance criteria from
each story, cross-references test standards from `standards/coding-standards.md` to assign
the appropriate test type (unit, integration, visual, UI, or config/data), and
produces a prioritized QA plan document.

For first/missing/new write authority, the skill asks "May I write to `production/qa/qa-plan-sprint-NNN.md`?" before
persisting the output. If an existing test plan for the same sprint is found, the
skill offers to update rather than replace. The verdict is COMPLETE when the plan
is written. No director gates are used — gate-level story readiness is handled by
`/story-readiness`.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keyword: COMPLETE
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (e.g., `/smoke-check` or `/story-readiness`)

---

## Director Gate Checks

None. `/qa-plan` is a planning utility. Story readiness gates are separate.

---

## Test Cases

### Case 1: Happy Path — Sprint with 4 stories generates full test plan

**Fixture:**
- `production/sprints/sprint-003.md` lists 4 stories with defined acceptance criteria
- Stories span types: 1 logic (formula), 1 integration, 1 visual, 1 UI
- `standards/coding-standards.md` is present with test evidence table

**Input:** `/qa-plan sprint-003`

**Expected behavior:**
1. Skill reads sprint-003.md and identifies 4 stories
2. Skill reads each story's acceptance criteria
3. Skill assigns test types per coding-standards.md table:
   - Logic story → Unit test (BLOCKING)
   - Integration story → Integration test (BLOCKING)
   - Visual story → Screenshot + lead sign-off (ADVISORY)
   - UI story → Manual walkthrough doc (ADVISORY)
4. Skill drafts QA plan with story-by-story test type breakdown
5. With no existing named plan-write scope, skill asks "May I write to `production/qa/qa-plan-sprint-003.md`?"; covered scope proceeds without re-asking
6. File is written on approval; verdict is COMPLETE

**Assertions:**
- [ ] All 4 stories are included in the plan
- [ ] Test type is assigned per coding-standards.md (not guessed)
- [ ] Actual required AC/evidence obligations are separate from optional type recommendations
- [ ] Missing/new write authority gets the exact-path "May I write" question; existing covered scope is reused
- [ ] Verdict is COMPLETE

---

### Case 2: Story With No Acceptance Criteria — Flagged as UNTESTABLE

**Fixture:**
- `production/sprints/sprint-004.md` lists 3 stories; one story has empty
  acceptance criteria section

**Input:** `/qa-plan sprint-004`

**Expected behavior:**
1. Skill reads all 3 stories
2. Skill detects the story with no AC
3. Story is flagged as `UNTESTABLE — Acceptance Criteria required` in the plan
4. Other 2 stories receive normal test type assignments
5. Plan is written with the UNTESTABLE story flagged; verdict is COMPLETE

**Assertions:**
- [ ] UNTESTABLE label appears for the story with no AC
- [ ] Plan is not blocked — the other stories are still planned
- [ ] Output suggests adding AC to the flagged story (next step)
- [ ] Verdict is COMPLETE (the plan is still generated)

---

### Case 3: Existing Test Plan Found — Offers update rather than replace

**Fixture:**
- `production/qa/qa-plan-sprint-003.md` already exists from a previous run
- Sprint-003 has 2 new stories added since the last plan

**Input:** `/qa-plan sprint-003`

**Expected behavior:**
1. Skill reads sprint-003.md and detects 2 stories not in the existing plan
2. Skill reports: "Existing QA plan found for sprint-003 — offering to update"
3. Skill presents the 2 new stories and their proposed test assignments
4. Reuse covered plan-update scope; if missing/new, ask "May I update `production/qa/qa-plan-sprint-003.md`?" with preservation of existing entries
5. Updated plan is written on approval

**Assertions:**
- [ ] Skill detects the existing plan file
- [ ] "update" language is used (not "overwrite")
- [ ] Only new stories are proposed for addition — existing entries preserved
- [ ] Verdict is COMPLETE

---

### Case 4: No Stories Found for Sprint — Error with guidance

**Fixture:**
- `production/sprints/sprint-007.md` does not exist
- No other sprint file matching sprint-007

**Input:** `/qa-plan sprint-007`

**Expected behavior:**
1. Skill attempts to read sprint-007.md — file not found
2. Skill outputs: "No sprint file found for sprint-007"
3. Skill suggests running `/sprint-plan` to create the sprint first
4. No plan is written; no "May I write" is asked

**Assertions:**
- [ ] Error message names the missing sprint file
- [ ] `/sprint-plan` is suggested as the remediation step
- [ ] No write tool is called
- [ ] Verdict is not COMPLETE (error state)

---

### Case 5: Director Gate Check — No gate; QA planning is a utility

**Fixture:**
- Sprint with valid stories and AC

**Input:** `/qa-plan sprint-003`

**Expected behavior:**
1. Skill generates and writes QA plan
2. No director agents are spawned
3. No gate IDs appear in output

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Skill reaches COMPLETE without any gate check

---

## Protocol Compliance

- [ ] Reads coding-standards.md test evidence table before assigning test types
- [ ] Actual Story/DoD/selected policy owns requirements; advisory type recommendations waive no required AC evidence
- [ ] Flags stories with no AC as UNTESTABLE (does not silently skip them)
- [ ] Detects existing plan and offers update path
- [ ] Resolve named create/update authority; ask "May I write" only for missing/new plan scope, without repeated confirmation for covered effects
- [ ] Verdict is COMPLETE when plan is written

---

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations, without
treating planning or uninvoked closure workflows as runtime execution.

### Case 6: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/qa-plan sprint` with each stated policy/evidence variant

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

### Case 7: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A separate
variant has actual conflicting policy or unresolved required applicability.

**Input:** `/qa-plan sprint` under the stated scope

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

### Case 8: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant authorizes only a report, excluding inputs/index/status/closure; another
introduces a materially new effect. Current input identities are supplied.

**Input:** `/qa-plan sprint` under the stated scope

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

### Case 9: Configured legacy Product and conflicting domain

**Fixture:**
No concept document; actual populated `Language & Framework`,
`Platform & Deployment` and `Agent Routing` establish a Python CLI Product.
Newer Product Stack fields remain placeholders. Variant introduces a real
contradictory Game concept/configuration.

**Input:** `/qa-plan sprint`

**Expected behavior:**
1. Read actual populated legacy configuration and relevant concept bodies.
2. Resolve consistent Product scope; keep contradictory dependent routing Unknown.

**Assertions:**
- [ ] Resolve the consistent legacy fixture as Product before asking a domain question; use actual
      Product contracts/workflows and configured routing.
- [ ] Read substantive bodies/configuration, not filenames or keyword counts.
- [ ] Conflicting real owners leave affected routing Unknown; neutral checks continue without a
      silent Game fallback or an invented Both project enum.
- [ ] No Memory Bank initialization or completion claim follows from routing.

**Case Verdict:** PASS / FAIL / PARTIAL

## Coverage Notes

- The case where `standards/coding-standards.md` is missing (skill cannot assign test types)
  is not fixture-tested; behavior would follow the BLOCKED pattern with a note
  to restore the standards file.
- Multi-sprint planning (spanning 2 sprints) is not tested; the skill is designed
  for one sprint at a time.
- Config/data story type (balance tuning → smoke check) follows the same
  assignment pattern as other types in Case 1 and is not separately tested.
