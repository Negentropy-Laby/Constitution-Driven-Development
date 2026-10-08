# Skill Test Spec: /smoke-check

## Skill Summary

`/smoke-check` is the gate between implementation and QA hand-off. It detects the
test environment, runs the automated test suite (via Bash), scans test coverage
against sprint stories, and uses `AskUserQuestion` to batch-verify manual smoke
checks with the developer. It writes a report to `production/qa/smoke-[date].md`
after explicit user approval.

Verdicts: PASS (tests pass, all smoke checks pass, no missing test evidence),
PASS WITH WARNINGS (every required check actually passes, only optional follow-up), FAIL (any applicable required executed check failed), or INCOMPLETE (required NotRun/Blocked/Pending/Unknown or missing evidence).

No director gates apply. The skill does NOT invoke any director agents.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: PASS, PASS WITH WARNINGS, FAIL, INCOMPLETE
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (e.g., `/bug-report` on FAIL, QA hand-off guidance on PASS)

---

## Director Gate Checks

None. `/smoke-check` is a pre-QA utility skill. No director gates apply.

---

## Test Cases

### Case 1: Happy Path — Automated tests pass, manual items confirmed, PASS

**Fixture:**
- `tests/` directory exists with a GDUnit4 runner script
- Engine detected as Godot from `technical-preferences.md`
- `production/qa/qa-plan-sprint-005.md` exists
- Automated test runner reports 12 tests, 12 passing, 0 failing
- Developer confirms all Batch 1 and Batch 2 smoke checks as PASS
- All required Story ACs have test bodies with behavioral oracles and exact-bound actual passing results; file matches only locate those originals

**Input:** `/smoke-check`

**Expected behavior:**
1. Skill detects test directory and engine, directly reads the existing QA plan
   and verifies its sprint/Story/platform scope; retains the actual path and full
   input binding rather than assuming a match from the filename
2. Runs `godot --headless --script tests/gdunit4_runner.gd` via Bash
3. Parses output: 12/12 passing
4. Reads test bodies/oracles and exact input/scope/runtime result bindings; file matches alone do not establish semantic coverage or PASS
5. Uses `AskUserQuestion` for Batch 1 (core stability) and Batch 2 (sprint mechanics)
6. Developer selects PASS for all items
7. Report assembled: automated tests PASS, all smoke checks PASS, no MISSING coverage
8. With no existing named report-write scope, asks "May I write this smoke check report to `production/qa/smoke-[date].md`?"; covered scope proceeds without re-asking
9. Writes report after approval
10. Delivers verdict: PASS

**Assertions:**
- [ ] Automated test runner is invoked via Bash
- [ ] `AskUserQuestion` is used for manual smoke check batches
- [ ] Missing/new report scope gets an exact-path "May I write" question; existing covered authority is reused
- [ ] Report is written to `production/qa/smoke-[date].md`
- [ ] Verdict is PASS
- [ ] QA hand-off names the actual selected scope-matched plan path and binding;
      it does not construct a different undated path

---

### Case 2: Failure Path — Automated test fails, FAIL verdict

**Fixture:**
- `tests/` directory exists, engine is Godot
- Automated test runner reports 10 tests run: 8 passing, 2 failing
  - Failing tests: `test_health_clamp_at_zero`, `test_damage_calculation_negative`
- QA plan exists

**Input:** `/smoke-check`

**Expected behavior:**
1. Skill runs automated tests via Bash
2. Parses output — 2 failures detected
3. Records failing test names
4. Proceeds through manual smoke check batches
5. Report shows automated tests as FAIL with failing test names listed
6. Reuses covered report authority or asks for missing/new scope; writes only the covered report effect
7. Delivers FAIL verdict with message: "The smoke check failed. Do not hand off to
   QA until these failures are resolved." Lists failing tests and suggests fixing
   then re-running `/smoke-check`

**Assertions:**
- [ ] Failing test names are listed in the report
- [ ] Verdict is FAIL
- [ ] Post-verdict message directs developer to fix failures before QA hand-off
- [ ] `/smoke-check` re-run is suggested after fixing

---

### Case 3: Optional follow-up warnings versus required missing evidence

Fixture: Game runner actually passes 8/8 required checks, manual observations bind
exact build/observer/steps/time, but an additional optional coverage recommendation
has no matching test. Expected: PASS WITH WARNINGS only for optional follow-up,
owner/due phase named. If instead the missing evidence supports a required Logic
AC, hand-off is INCOMPLETE and affected Story cannot close, even when all other
checks pass. No file existence or required MISSING coverage is a warning-pass.

Assertions:
- [ ] Required actual PASS and optional warnings are separately recorded.
- [ ] Any required NotRun/Blocked/Pending/Unknown yields INCOMPLETE, not PASS WITH WARNINGS.
- [ ] Report-only authority writes only a new report; no implicit index/state effect.

---

### Case 4: Configured Test Roots and Missing Required Setup

**Fixture A:** No `tests/` directory, but actual config selects an available
GDUnit4 runner in `qa/checks/` and a documented command/input scope there.
**Input:** `/smoke-check`
**Expected:** read that config and run its existing configured command; absence
of conventional `tests/` alone does not stop, scaffold or fail the project.

**Fixture B:** Required test config/runner is actually absent or unavailable and
no valid alternate root/command exists.
**Expected:** record current NotRun/Blocked with the concrete missing dependency
and INCOMPLETE hand-off, suggest applicable `/test-setup`, continue independent
available checks. No observed automated FAIL, invented PASS or forced directory.

**Assertions:**
- [ ] Configured legal roots outside `tests/` are supported without scaffolding.
- [ ] Language labels select no command without actual matching config/runner.
- [ ] Unknown JavaScript tooling does not trigger guessed `npm test -- --runInBand`.
- [ ] Unavailable/missing required setup remains NotRun/Blocked, not observed FAIL.
- [ ] Exact-bound historical originals are separate from current execution;
      unbound verbal confirmation cannot change current NotRun or yield PASS.
- [ ] Writes use covered named effects only; setup is never auto-created.

---

### Case 5: Director Gate Check — No gate; smoke-check is a QA pre-check utility

**Fixture:**
- Valid test setup, automated tests pass, manual smoke checks confirmed

**Input:** `/smoke-check`

**Expected behavior:**
1. Skill runs all phases and produces a PASS or PASS WITH WARNINGS verdict
2. No director agents are spawned at any point
3. No gate IDs (CD-*, TD-*, AD-*, PR-*) appear in output
4. No `/gate-check` is invoked

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Verdict is PASS, PASS WITH WARNINGS, FAIL or INCOMPLETE for exact scope; no director gate verdict is invented

---

### Case 6: Current plan scope beats newer unrelated plan

**Fixture:** Game and Product variants each name an actual current sprint and
its Story/CDD/build/platform inputs. Two real plan originals exist: the older
plan covers this exact scope, while the newer-mtime plan names a different
sprint/Story or platform. Configured test and actual required smoke evidence are
available; report authority names only a new smoke report.

**Input:** `/smoke-check sprint` with the existing current-scope instruction.

**Expected behavior and assertions:**
- [ ] Directly read both candidate bodies and relevant scope owners; compare the
      actual current scope rather than mtime, date or filename alone.
- [ ] Select the actual matching plan, bind its full SHA-256/bytes/collection
      time and scope, and use that same original for coverage/manual checks.
- [ ] QA hand-off cites exactly that existing selected path/binding for the
      checked scope, including a dated or legacy path when it truly matches.
- [ ] Do not synthesize a replacement path, write a plan, run another workflow
      or update inputs/indexes/state under report-only authority.

### Case 7: Ambiguous actual candidates require a real path choice

**Fixture:** Two existing plans cover the selected current Story set but differ
in unresolved build/platform or check scope; no authoritative owner selects one.

**Input:** `/smoke-check sprint`; the next turn chooses one actual displayed
candidate path within the same existing review/report authority.

**Expected behavior and assertions:**
- [ ] Present both real paths and their scope differences for selection. Do not
      silently choose the latest file or offer a fabricated plan path.
- [ ] Until resolved, plan-dependent checks/hand-off stay Pending; independent
      available checks may continue without invented execution or qualification.
- [ ] After the real choice, reread/bind that original and continue only within
      its matched scope and existing authority; no repeated report-write ask.

### Case 8: Missing, mismatched or unreadable plan is disclosed

**Fixture:** No usable current-scope plan exists, or the explicit plan cannot be
directly read. Available Story/CDD/configured smoke evidence is still retained.
Variant A keeps plan orchestration optional. Variant B supplies a real selected
workflow entry criterion requiring that exact scope-matched plan.

**Expected behavior and assertions:**
- [ ] Report actual absence, mismatch or access failure separately; do not infer
      a match from a filtered file list or invent an existing plan.
- [ ] Continue independent available checks from actual scope owners and make a
      scoped `/qa-plan` recommendation; do not write/run it or initialize memory.
- [ ] Optional plan absence does not invent a strict gate or erase actual smoke
      results. Required plan gaps keep the affected hand-off INCOMPLETE.
- [ ] A passing limited smoke result without a selected plan does not announce a
      plan-dependent QA hand-off or name a synthesized undated plan path.

---

## Protocol Compliance

- [ ] Uses `AskUserQuestion` for all manual smoke check batches (Batch 1, Batch 2, Batch 3)
- [ ] Uses an available verified shell/runtime for actual configured commands; absent capability stays NotRun and does not prevent independent checks
- [ ] Requires covered named report authority; "May I write" only for missing/new effects, with no repeated ask for authorized scope
- [ ] Verdict is PASS / PASS WITH WARNINGS / FAIL / INCOMPLETE, with actual per-check truth retained
- [ ] Observed FAIL in automation or any applicable required smoke batch (including Batch 3 data/performance and requested platform checks) yields FAIL; required NotRun/Blocked/Pending/Unknown yields INCOMPLETE
- [ ] PASS WITH WARNINGS requires every required check/evidence pass; only optional MISSING follow-up can warn
- [ ] Required unavailable engine/runner execution stays NotRun and INCOMPLETE, not PASS WITH WARNINGS or observed test FAIL
- [ ] Does not invoke director gates at any point
- [ ] The selected QA plan and current scope are verified from actual bodies;
      report and hand-off reuse its exact existing path and input binding.
- [ ] Ambiguous real candidates need an actual path choice; missing/unreadable
      required plans remain incomplete without fabricated originals or new effects.

---

## Reduced Quick Scope Counterexample

`quick` skips only its documented coverage/Batch 3 work. Required omitted checks
remain NotRun for the original scope; reduced-scope PASS cannot approve that scope.
An actually observed required Batch 3 or requested platform failure remains FAIL
when applicable, with its exact original evidence and scope retained.
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

**Input:** `/smoke-check sprint` with each stated policy/evidence variant

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

**Input:** `/smoke-check sprint` under the stated scope

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

**Input:** `/smoke-check sprint` under the stated scope

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

- The `quick` argument (skips Phase 3 coverage scan and Batch 3) is not separately
  fixture-tested; it follows the same pattern as Case 1 with a coverage-skip note in output.
- The `--platform` argument adds platform-specific AskUserQuestion batches and a
  per-platform verdict table; not separately tested here.
- Missing runner, quick-scope omissions and platform gaps remain required incomplete when selected; no runtime/platform qualification is inferred.
