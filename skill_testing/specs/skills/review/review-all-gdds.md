# Skill Test Spec: /review-all-gdds

## Skill Summary

`/review-all-gdds` is an Opus-tier skill that performs a holistic cross-GDD review
across all files in `design/cdd/`. It runs two complementary review phases in
parallel: Phase 2 checks for consistency (contradictions, formula mismatches,
stale references, competing ownership), and Phase 3 checks design theory (dominant
strategies, pillar drift, cognitive overload, economic imbalance). Because the two
phases are independent, they are spawned simultaneously to save time. The skill
produces a PASS / CONCERNS / FAIL verdict and is read-only — no
files are written without explicit user approval.

The skill is itself the holistic review gate in the pipeline. It is invoked after
individual GDDs are complete and before architecture work begins. It does NOT spawn
any director gate agents (it IS the director-level review).

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥5 phase headings (complex multi-phase skill)
- [ ] Contains verdict keywords: PASS, CONCERNS, FAIL
- [ ] Analysis is read-only; report-only and index/status effects have separate authority
- [ ] Has a next-step handoff at the end
- [ ] Documents parallel phase spawning (Phase 2 and Phase 3 are independent)

---

## Director Gate Checks

No director gates — this skill spawns no director gate agents. It IS the holistic
review; delegating to a director gate would create a circular dependency.

---

## Test Cases

### Case 1: Happy Path — Clean GDD set with no conflicts

**Fixture:**
- `design/cdd/` contains ≥3 system GDDs
- All GDDs are internally consistent: no formula contradictions, no competing ownership, no stale references
- All GDDs align with the pillars defined in `design/cdd/game-pillars.md`

**Input:** `/review-all-gdds`

**Expected behavior:**
1. Skill reads all GDD files in `design/cdd/`
2. Phase 2 (consistency scan) and Phase 3 (design theory check) spawn in parallel
3. Phase 2 finds no contradictions, no formula mismatches, no ownership conflicts
4. Phase 3 finds no pillar drift, no dominant strategies, no cognitive overload
5. Skill outputs a structured findings table with 0 blocking issues
6. Verdict: PASS

**Assertions:**
- [ ] Both review phases are spawned in parallel (not sequentially)
- [ ] Output includes a findings table (even if empty — shows "No issues found")
- [ ] Verdict is PASS when no conflicts are found
- [ ] Skill does NOT write any files without user approval
- [ ] Next-step handoff to `/architecture-review` or `/create-architecture` is present

---

### Case 2: Failure Path — Conflicting rules between two GDDs

**Fixture:**
- GDD-A defines a floor value (e.g. "minimum [output] is [N]")
- GDD-B states a mechanic that bypasses that floor (e.g. "[mechanic] can reduce [output] to 0")
- The two GDDs are otherwise complete and valid

**Input:** `/review-all-gdds`

**Expected behavior:**
1. Phase 2 (consistency scan) detects the contradiction between GDD-A and GDD-B
2. Conflict is reported with: both filenames, the specific conflicting rules, and severity HIGH
3. Verdict: FAIL
4. Handoff instructs user to resolve the conflict and re-run before proceeding

**Assertions:**
- [ ] Verdict is FAIL (not PASS or CONCERNS)
- [ ] Both GDD filenames are named in the conflict entry
- [ ] The specific contradicting rules are quoted or described (not vague "conflict found")
- [ ] Issue is classified as severity HIGH (blocking)
- [ ] Skill does NOT auto-resolve the conflict

---

### Case 3: Partial Path — Single GDD with orphaned dependency reference

**Fixture:**
- GDD-A lists a dependency in its Dependencies section pointing to "system-B"
- No GDD for system-B exists in `design/cdd/`
- All other GDDs are consistent

**Input:** `/review-all-gdds`

**Expected behavior:**
1. Phase 2 detects the orphaned dependency reference in GDD-A
2. Issue is reported as: DEPENDENCY GAP — GDD-A references system-B which has no GDD
3. No other conflicts found
4. Verdict follows impact: a declared future/advisory dependency can be CONCERNS;
   a required missing contract makes affected checks incomplete and blocks dependants

**Assertions:**
- [ ] Required dependency gaps cannot become a passing complete review;
  advisory gaps retain their exact scope and owner
- [ ] The specific GDD filename and the missing dependency name are reported
- [ ] Skill suggests running `/design-system system-B` to resolve the gap
- [ ] Skill does NOT skip or silently ignore the missing dependency

---

### Case 4: Edge Case — No GDD files found

**Fixture:**
- `design/cdd/` directory is empty or does not exist
- No GDD files are present

**Input:** `/review-all-gdds`

**Expected behavior:**
1. Skill attempts to read files in `design/cdd/`
2. No files found — skill outputs an error with guidance
3. Skill recommends running `/brainstorm` and `/design-system` before re-running
4. Skill does NOT produce a verdict (PASS / CONCERNS / FAIL)

**Assertions:**
- [ ] Skill outputs a clear error message when no GDDs are found
- [ ] No verdict is produced when the directory is empty
- [ ] Skill recommends the correct next action (`/brainstorm` or `/design-system`)
- [ ] Skill does NOT crash or produce a partial report

---

### Case 5: Director Gate — No gate spawned regardless of review mode

**Fixture:**
- `design/cdd/` contains ≥2 consistent system GDDs
- `production/review-mode.txt` exists with content `full`

**Input:** `/review-all-gdds`

**Expected behavior:**
1. Skill reads all GDDs and runs the two review phases
2. Skill does NOT read `review-mode.txt`
3. Skill does NOT spawn any director gate agent (CD-, TD-, PR-, AD- prefixed)
4. Skill completes and outputs its verdict normally
5. Review mode setting has no effect on this skill's behavior

**Assertions:**
- [ ] No director gate agents are spawned at any point
- [ ] Skill does NOT read `production/review-mode.txt`
- [ ] Output does not contain any "Gate: [GATE-ID]" or "skipped" gate entries
- [ ] The skill produces a verdict regardless of review mode
- [ ] R4 metric: gate count for this skill = 0 in all modes

---

## Protocol Compliance

- [ ] Phase 2 (consistency) and Phase 3 (design theory) spawned in parallel — not sequentially
- [ ] Does NOT write any files without "May I write" approval
- [ ] Findings table shown before any write ask
- [ ] Verdict is one of exactly: PASS, CONCERNS, FAIL
- [ ] Ends with appropriate handoff: FAIL → fix and re-run; CONCERNS → may proceed with awareness; PASS → `/create-architecture`

---

## Coverage Notes

- Economic balance analysis (source/sink loops) requires cross-GDD resource data — covered
  structurally by Case 2 (the conflict detection pattern is the same).
- The design theory phase (Phase 3) checks including dominant strategy detection and
  cognitive overload are not individually fixture-tested — they follow the same
  pattern as consistency checks and are validated via the pillar drift case structure.
- Exact-baseline incremental/continuation cases below cover working-tree and
  dependency changes; static source checks do not certify actual full reading.

---

### Semantic case: Incremental, Full and continuation are different claims

Bind a previous full review to exact CDDs, required attachments and rule inputs.
Change an unstaged CDD and an ignored indirect contract without changing the
report mtime; expect `since-last-review` to include both and affected relationships.
Compare a missing baseline: request/disclose a new full or narrower current-scope
review, never "no changes." Restore the exact bytes and resume an interrupted
same-scope review: report continuation, completed/pending actual passes and the
historical baseline, without claiming continuous unchanged history or a new Full
review. A focused consistency pass does not certify design-theory completion.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.

---

### Invalid focus/flag counterexamples

Invoke `/review-all-gdds unknown-focus` and `/review-all-gdds full --unknown`.
Expect named legal focus usage/correction and no spawn, write or review verdict.
Absent focus remains full; all four documented focus invocations remain valid.
