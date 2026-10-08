# Skill Test Spec: /skill-improve

## Skill Summary

`/skill-improve` runs a scoped test-fix-retest improvement loop on a skill
file. It invokes `/skill-test static` (and optionally `/skill-test category`) to
establish a baseline score, diagnoses the failing checks, proposes targeted fixes
to the SKILL.md file, checks scoped authority (requesting it when absent), applies
the fixes, and re-runs the tests to confirm improvement.

If the proposed fix makes the skill worse (regression), the fix is reverted within scoped rollback authority (requested if absent) rather than applied. If the applicable structural/category/spec and semantic checks show no gaps,
the skill exits immediately without making changes. No director gates apply. Verdicts:
IMPROVED (intended gaps fixed without required semantic regression), NO CHANGE (no improvements possible or user declined), or
REVERTED (fix was applied but caused regression and was reverted).

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: IMPROVED, NO CHANGE, REVERTED
- [ ] Actual scoped-authority behavior/shared-owner application governs fixes, not phrase presence
- [ ] Has a next-step handoff (e.g., run `/skill-test spec` to validate behavioral compliance)

---

## Director Gate Checks

None. `/skill-improve` is a meta-utility skill. No director gates apply.

---

## Test Cases

### Case 1: Happy Path — Skill With Two Static Findings, Both Fixed, IMPROVED

**Fixture:**
- `skills/some-skill/SKILL.md` has two static findings (one FAIL and one WARN):
  - Check 4 FAIL: write-capable actions lack scoped-authority behavior
  - Check 5 WARN: no next-step handoff at the end

**Input:** `/skill-improve some-skill`

**Expected behavior:**
1. Skill runs `/skill-test static some-skill` — baseline: 6/8 checks pass
2. Skill diagnoses actual Check 4 failure and Check 5 warning
3. Skill proposes fixes:
   - Apply actual named authority/absent-new-effect approval behavior
   - Add a next-step handoff section at the end
4. Skill reuses matching approval or asks "May I write improvements to `skills/some-skill/SKILL.md`?" after showing scope.
5. Fixes applied; `/skill-test static some-skill` re-run — now all current 8/8 checks pass
6. Verdict is IMPROVED only after required semantic/review checks pass (structural 6→8)

**Assertions:**
- [ ] Baseline score is established before any changes (6/8)
- [ ] Both actual findings are diagnosed and addressed; missing magic phrase alone is insufficient
- [ ] New authority is requested after draft/scope only when matching approval is absent
- [ ] Re-test confirms improvement (8/8)
- [ ] Verdict is IMPROVED with before/after score shown

---

### Case 2: Fix Causes Regression — Score Comparison Shows Regression, REVERTED

**Fixture:**
- `skills/some-skill/SKILL.md` has 1 static WARN (Check 5: missing handoff), with 0 FAILs
- Proposed fix inadvertently removes the verdict keywords section
  and Check 8 dual-domain behavior (introducing two failures)

**Input:** `/skill-improve some-skill`

**Expected behavior:**
1. Baseline: 7/8 checks pass (1 WARN: Check 5 missing handoff; 0 FAILs)
2. Skill proposes fix and asks "May I write improvements?"
3. Fix is applied; re-test runs
4. Re-test result: 6/8 (fixed Check 5 handoff, but broke required Check 3
   verdict keywords and Check 8 dual-domain behavior: two required FAILs)
5. Skill detects regression: score went DOWN
6. Skill checks existing rollback authority; if absent asks: "Fix caused a regression. May I restore the exact invocation baseline?"
7. Restore only within scoped authority; verify exact original bytes; verdict REVERTED.

**Assertions:**
- [ ] Re-test score is compared to baseline before finalizing
- [ ] Regression is detected when score decreases
- [ ] Existing scoped rollback authority is reused; request it only when absent
- [ ] Exact retained invocation bytes are restored within scoped authority
- [ ] Verdict is REVERTED

---

### Case 3: Skill With Category Assignment — Baseline Captures Both Scores

**Fixture:**
- `skills/gate-check/SKILL.md` is a gate skill with 1 static failure
  and 2 category (G-criteria) failures
- `skill_testing/quality-rubric.md` has Gate Skills section

**Input:** `/skill-improve gate-check`

**Expected behavior:**
1. Skill runs both static and category tests for the baseline:
   - Static: 7/8 checks pass
   - Category: 3/5 G-criteria pass
2. Combined baseline: 10/13
3. Skill diagnoses all 3 failures and proposes fixes
4. "May I write improvements to `skills/gate-check/SKILL.md`?"
5. Fixes applied; both test types re-run
6. Re-test: static 8/8, category 5/5 = 13/13
7. Verdict is IMPROVED (10→13)

**Assertions:**
- [ ] Both static and category scores are captured in the baseline
- [ ] Combined score is used for comparison (not just one type)
- [ ] All 3 failures are addressed in the proposed fix
- [ ] Re-test confirms improvement in both score types
- [ ] Verdict is IMPROVED with combined before/after

---

### Case 4: No Applicable Findings — Scoped NO CHANGE

**Fixture:**
- `skills/brainstorm/SKILL.md` has no applicable static findings
- Catalog resolves `brainstorm` to `utility`. U1 is Passes current static
  checks: COMPLIANT with 0 FAILs. U2 is Gate mode correct (if applicable): a
  director-gate branch reads review-mode and applies full/lean/solo correctly.
  If this fixture has no director-gate branch, U2 is justified N/A, not a pass.
- No applicable existing spec assertion or affected semantic gap remains. All
  required checks for the evaluated scope are available and satisfied; execution
  limits outside that scope are disclosed without claiming qualification.

**Input:** `/skill-improve brainstorm`

**Expected behavior:**
1. Skill runs `/skill-test static brainstorm` — 8/8 checks pass
2. Evaluate actual utility U1/U2. Report U1 PASS and U2 N/A with the actual
   no-director-gate rationale, or verify U2 PASS for an applicable gate branch.
   Use 2/2 only when both apply and pass; N/A is excluded from the applicable
   denominator and execution limits remain separate.
3. Skill outputs: "No applicable improvements in the evaluated scope; runtime
   qualification and unexecuted cases remain separately disclosed."
4. Skill exits without proposing any changes
5. No "May I write" is asked; no files are modified
6. Verdict is NO CHANGE

**Assertions:**
- [ ] Skill confirms no applicable semantic/spec gap before reporting NO CHANGE
- [ ] Reports "No applicable improvements in the evaluated scope" and discloses
  runtime qualification and unexecuted cases separately, matching the scoped output.
- [ ] An unavailable applicable required check prevents this NO CHANGE conclusion;
  structural scores alone cannot establish no semantic/spec gaps.
- [ ] No changes are proposed
- [ ] No "May I write" is asked
- [ ] Verdict is NO CHANGE

---

### Case 5: Director Gate Check — No gate; skill-improve is a meta utility

**Fixture:**
- Skill with at least 1 static failure

**Input:** `/skill-improve some-skill`

**Expected behavior:**
1. Skill runs the test-fix-retest loop
2. No director agents are spawned
3. No gate IDs appear in output

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Verdict is IMPROVED, NO CHANGE, or REVERTED — no gate verdict

---

## Protocol Compliance

- [ ] Always establishes a baseline score before proposing any changes
- [ ] Shows before/after score comparison in the output
- [ ] Shows concrete fix/scope and applies existing authority; asks only for new material effects
- [ ] Detects regressions by comparing re-test score to baseline
- [ ] Rollback reuses scoped authority or requests it if absent; never discards pre-existing changes
- [ ] Reverts via a pre-write snapshot of the canonical `skills/<name>/SKILL.md`, restoring the exact invocation baseline independently of Git/index state (not `git checkout`)
- [ ] After approved canonical edit, real whole-class plan checks all output effects;
  only covered clean scope runs existing `python scripts/sync_adapters.py --write --class skills`
- [ ] Ends with IMPROVED, NO CHANGE, or REVERTED verdict

---

## Coverage Notes

- The documented improvement loop runs one fix-retest cycle per
  invocation; running multiple iterations requires re-invoking `/skill-improve`.
- Behavioral compliance (spec-mode test results) is not included in the
  improvement loop — structural/category scores alone do not prove behavior; evaluate affected existing
  spec/semantics and disclose unexecuted runtime cases.
- The case where the skill file cannot be read (permissions error or missing file)
  is not tested; this would result in an error before the baseline is established.


## Shared Authority and Evidence Cases

### Case 6: Named approval, report-only and review-only

**Fixture:** Variant A authorizes canonical fix plus all actual changed skills-class output effects
and named report/index together. B permits only a new assigned report. C is review-only.

**Assertions:**
- [ ] A reuses named scope across roles/files/retries; edits canonical source then
  real generator output, never hand-edits adapters or requests every path again.
- [ ] B leaves canonical inputs/adapters/coverage/state unchanged; C invokes no
  write entrypoint including in-memory resealing. No automatic Memory Bank activation.
- [ ] Preserve exact originals/full hashes/minimum indirect attachment witnesses.
- [ ] Writer retests are not independent review; obtain a fresh exact baseline for
  independent verification required by the selected workflow.

### Case 7: Semantic regression despite increased score

**Fixture:** Static/category scores improve but candidate changes public contract,
trust boundary, durable format or state ownership without Accepted ADR.

**Assertions:**
- [ ] Score increase/keywords alone do not establish IMPROVED. Record
  `adr-required`/`conflict` and block affected implementation/closure until decision
  acceptance or valid scoped exception; continue independent work.
- [ ] A CDD-owned detail with named owner may instead be `cdd-layer` or justified
  `no-adr`; do not manufacture an ADR to satisfy a link check.
- [ ] Historical approval needs exact input/authority match. Writing a report,
  synchronizing documentation or running tests is not publication/acceptance/completion.
- [ ] Restore tests use isolated copies; permanent deletion requires separate
  exact object-list authority. Preserve failed candidate/history and disclose omissions.

### Case 8: Whole-class generator scope and guarded rollback

**Fixture:** Named canonical fix/rollback authority; real `--class skills` plan
also changes another owner's adapter or reports EXTRA. Variant has no unrelated
drift and covered output effects. After application another actor changes canonical
or one touched adapter; baseline/after bytes and context are retained.
- [ ] Scope the actual whole class including resource projections; no invented
  per-skill CLI/API. Uncovered other-owner drift/EXTRA stops writes, not implicit
  deletion from internally recognized EXTRA. Exact deletion requires independent
  object-list authority.
- [ ] Covered clean variant uses the existing generator after canonical repair.
- [ ] Rollback requires live==this invocation's exact after for each touched object,
  matching manifest/generator context; other-actor changes stop affected restore.
- [ ] Restore only retained invocation before bytes; preserve prior user edits,
  failed candidate and evidence, never `git checkout` or unconditional overwrite.
- [ ] Reduced total FAIL/WARN cannot hide new Required regression/authority gap or
  lost Game/Product behavior; required independent review uses fresh exact inputs.
