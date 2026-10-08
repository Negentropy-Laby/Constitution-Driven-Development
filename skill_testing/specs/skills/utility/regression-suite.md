# Skill Test Spec: /regression-suite

## Skill Summary

Use `[update | audit | report]` for actual Game/Product critical paths and original
closed Bug scenarios. Update/audit may maintain `tests/regression-suite.md` under
covered scope; report is read-only. Static coverage and actual execution are
separate. No director gate; manifest operation COMPLETE completes no Story/release.

## Static Assertions (Structural)

These inspect instruction structure; they do not establish runtime behavior.

- [ ] Required frontmatter fields exist: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] At least two phase or numbered section headings exist
- [ ] Declared result vocabulary includes COVERED / PARTIAL / MISSING and INCOMPLETE; operation COMPLETE is separate
- [ ] Scoped authority/shared-contract references and next-step handoff are present
- [ ] Modes `update`, `audit` and `report` and their output path are documented

## Director Gate Checks

N/A: this skill does not trigger director gates. Specialist delegation,
where required by the canonical owner, is distinct from a director gate.

## Test Cases

### Case 1: Critical-path audit

**Fixture:**
Separate Game save/load/combat and Product API/CLI/permission/migration
fixtures supply owning ACs, tests, helpers and actual configured paths. Manual
visual/UI evidence is required where the owner selects it.

**Input:** `/regression-suite audit`

**Expected behavior:**
1. Read each owner/test/helper/fixture body and map its scenario and behavioral oracle.
2. Report COVERED/PARTIAL/MISSING with actual execution recorded separately.
3. Draft only a covered manifest update, preserving existing entries.

**Assertions:**
- [ ] Names and keywords locate evidence but do not establish behavioral coverage.
- [ ] Game and Product mappings follow their actual contracts and paths.
- [ ] Automation N/A does not waive required manual evidence or create runtime PASS.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 2: Original Bug before regression claim

**Fixture:**
Closed BUG-NNN retains the original scenario and required attachment. A test
quotes its ID but exercises another failure. Variant: the original attachment is missing.

**Input:** `/regression-suite audit`

**Expected behavior:**
1. Read the original Bug, fix, attachment and test before matching the scenario.
2. Identify whether the behavioral guard actually reproduces/prevents the original failure.
3. Keep missing originals and absent pre/post-fix execution explicit.

**Assertions:**
- [ ] The quoted ID alone does not yield HAS REGRESSION TEST.
- [ ] Unavailable required originals yield INCOMPLETE, not invented scenario coverage.
- [ ] Static coverage never substitutes for actual pre/post-fix execution; absent results stay NotRun.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 3: Drift/quarantine and required gaps

**Fixture:**
A Complete-labeled Story lacks required coverage, a new critical path is absent
and a Game regression is quarantined. The selected owner identifies required checks.

**Input:** `/regression-suite audit`

**Expected behavior:**
1. Compare current requirements with actual tests and preserved quarantine rationale.
2. Distinguish dependent required gaps from optional follow-up.
3. Report affected closure gaps and remaining owner/action.

**Assertions:**
- [ ] A Complete label does not establish current required coverage.
- [ ] Quarantine/disablement preserves actual failure or unexecuted state, never PASS.
- [ ] No universal regression-artifact gate is invented.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 4: Report-only and audit preservation

**Fixture:**
Variant A has no suite and selects report mode. Variant B authorizes an
additive audit/update to an existing manifest with rationale and history.

**Input:** A: `/regression-suite report`; B: `/regression-suite audit` or `update`

**Expected behavior:**
1. A renders conversation guidance without a write entrypoint.
2. B reads the original manifest and drafts only covered additive effects.
3. Retain existing entries/history; request new scope for any proposed removal.

**Assertions:**
- [ ] A does not create a suite, test, index or state file.
- [ ] Audit authority implies no broad replacement or deletion.
- [ ] B completes only the authorized manifest operation, without Story/release completion.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 5: Historical regression input changes

**Fixture:**
Permitted historical results retain exact originals. Variant changes one
build/config/fixture dependency while the old result path remains the same.

**Input:** `/regression-suite audit`

**Expected behavior:**
1. Compare full current dependency identities with the retained historical result.
2. Reuse exact permitted results only with their original runtime/observer/scope label.
3. Keep the changed scope incomplete until appropriate verification occurs.

**Assertions:**
- [ ] Historical reuse is not this run's execution.
- [ ] Changed dependencies invalidate the affected old claim.
- [ ] Operation COMPLETE changes no FAIL/NotRun fact or completion authority.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Exact owner/Bug/test/attachments bind full SHA/size/recoverable originals.
- [ ] Full reading vs discovery, static coverage vs runtime separately recorded.
- [ ] Report-only leaves manifest/test/index/state unchanged; new effects need scope.

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

**Input:** `/regression-suite audit` with each stated policy/evidence variant

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

**Input:** `/regression-suite audit` under the stated scope

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

**Input:** `/regression-suite audit` under the stated scope

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

**Input:** `/regression-suite audit`

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

These semantic fixture instructions are not actual Game/Product test execution.
Runtime qualification is NotRun without actual exactly bound observations.
