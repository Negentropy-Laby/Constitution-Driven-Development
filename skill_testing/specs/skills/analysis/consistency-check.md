# Skill Test Spec: /consistency-check

## Skill Summary

`/consistency-check` compares registered facts against the registry-derived
source/reference closure. Its `full` mode checks all registered entries and their
relevant definitions, not a Full-body holistic design review. Grep locates
definitions; actual contextual reads decide consistency. PASS means agreement
within that declared registry scope; CONFLICTS FOUND and INCOMPLETE name problems.
Read-only analysis may propose separately authorized report/registry/log effects.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains scoped verdicts PASS, CONFLICTS FOUND, INCOMPLETE
- [ ] Does NOT require "May I write" language during analysis (read-only scan)
- [ ] Has a next-step handoff at the end
- [ ] Documents that report writing is optional and requires approval

---

## Director Gate Checks

No director gates — this skill spawns no director gate agents. Consistency
checking is a mechanical scan; no creative or technical director review is
required as part of the scan itself.

---

## Test Cases

### Case 1: Happy Path — 4 GDDs with no conflicts

**Fixture:**
- Registry entries bind all compared facts to their source/reference definitions
- `design/cdd/` contains exactly 4 system GDDs
- All GDDs have consistent formulas (no overlapping variables with different values)
- No two GDDs claim ownership of the same game entity or mechanic
- All dependency references point to GDDs that exist

**Input:** `/consistency-check`

**Expected behavior:**
1. Skill reads the complete registry-derived comparison closure for the four CDDs
2. Runs cross-GDD consistency checks (formulas, ownership, references)
3. No conflicts found
4. Outputs structured findings table showing 0 issues
5. Verdict: PASS

**Assertions:**
- [ ] Every registered source/reference definition is contextually read before conclusions
- [ ] Findings table is present (even if empty — shows "No conflicts found")
- [ ] Verdict is PASS when no conflicts exist
- [ ] Skill does NOT write any files without user approval
- [ ] Next-step handoff is present

---

### Case 2: Failure Path — Two GDDs with conflicting damage formulas

**Fixture:**
- GDD-A defines damage formula: `damage = attack * 1.5`
- GDD-B defines damage formula: `damage = attack * 2.0` for the same entity type
- Both GDDs refer to the same "attack" variable and registry formula entry

**Input:** `/consistency-check`

**Expected behavior:**
1. Skill reads the registered formula definitions and detects the contextual mismatch
2. Findings table includes an entry: GDD-A vs GDD-B | Formula Mismatch | HIGH
3. Specific conflicting formulas are shown (not just "formula conflict exists")
4. Verdict: CONFLICTS FOUND

**Assertions:**
- [ ] Verdict is CONFLICTS FOUND (not PASS)
- [ ] Conflict entry names both GDD filenames
- [ ] Conflict type is "Formula Mismatch"
- [ ] Severity is HIGH for a direct formula contradiction
- [ ] Both conflicting formulas are shown in the findings table
- [ ] Skill does NOT auto-resolve the conflict

---

### Case 3: Partial Path — GDD references a system with no GDD

**Fixture:**
- A registered GDD-A definition requires the system-B contract to compare meaningfully
- No GDD for system-B exists in `design/cdd/`
- All other GDDs are consistent

**Input:** `/consistency-check`

**Expected behavior:**
1. Skill follows the registered definition's required contract dependency
2. GDD-A's reference to "system-B" cannot be resolved — no GDD exists for it
3. Findings table includes: GDD-A vs (missing) | Dependency Gap | MEDIUM
4. Verdict: INCOMPLETE with a DEPENDENCY GAP finding; absence cannot establish PASS

**Assertions:**
- [ ] Missing required definition yields INCOMPLETE, not registry agreement
- [ ] Findings entry names GDD-A and the missing system-B
- [ ] Severity is MEDIUM for an unresolved dependency reference
- [ ] Skill suggests running `/design-system system-B` to create the missing GDD

---

### Case 4: Edge Case — No GDDs found

**Fixture:**
- `design/cdd/` directory is empty or does not exist

**Input:** `/consistency-check`

**Expected behavior:**
1. Skill attempts to read files in `design/cdd/`
2. No GDD files found
3. Skill outputs an error: "No GDDs found in `design/cdd/`. Run `/design-system` to create GDDs first."
4. No findings table is produced
5. No verdict is issued

**Assertions:**
- [ ] Skill outputs a clear error message when no GDDs are found
- [ ] No verdict is produced (PASS / CONFLICTS FOUND / INCOMPLETE (DEPENDENCY GAP is an INCOMPLETE finding))
- [ ] Skill recommends the correct next action (`/design-system`)
- [ ] Skill does NOT crash or produce a partial report

---

### Case 5: Director Gate — No gate spawned; no review-mode.txt read

**Fixture:**
- `design/cdd/` contains ≥2 GDDs
- `production/review-mode.txt` exists with `full`

**Input:** `/consistency-check`

**Expected behavior:**
1. Skill reads all GDDs and runs the consistency scan
2. Skill does NOT read `production/review-mode.txt`
3. No director gate agents are spawned at any point
4. Findings table and verdict are produced normally

**Assertions:**
- [ ] No director gate agents are spawned (no CD-, TD-, PR-, AD- prefixed gates)
- [ ] Skill does NOT read `production/review-mode.txt`
- [ ] Output contains no "Gate: [GATE-ID]" or gate-skipped entries
- [ ] Review mode has no effect on this skill's behavior

---

## Protocol Compliance

- [ ] Reads all relevant registered definitions/closure before the findings table
- [ ] Findings table shown in full before any write ask (if report is requested)
- [ ] Verdict is scoped PASS, CONFLICTS FOUND or INCOMPLETE; gaps remain findings
- [ ] No director gates — no review-mode.txt read
- [ ] Report writing (if requested) gated by "May I write" approval
- [ ] Ends with next-step handoff appropriate to verdict

---

## Coverage Notes

- This skill checks registry-scoped factual/contract consistency. Full-body design theory
  analysis (pillar drift, dominant strategies) is handled by `/review-all-gdds`.
- Formula conflict detection relies on consistent formula notation across GDDs —
  informal descriptions of the same mechanic may not be detected.
- The conflict severity rubric (HIGH / MEDIUM / LOW) is defined in the skill body
  and not re-enumerated here.

---

### Semantic case: Registry scope and contextual exceptions

Register the original Game damage formula but add an exception/range qualifier
outside a three-line grep excerpt, and a Product schema contract in an indirect
attachment. Expect complete relevant definitions/closure before comparing,
not a false conflict or PASS from excerpts. Full means all registered comparisons,
not holistic body/design-theory review. A missing required attachment yields
INCOMPLETE; empty registry cannot establish PASS. Change an ignored dependency
from the exact prior manifest without changing report dates: incremental scope
must include it. No report-only registry correction or reflexion-log append.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.

---

### Invalid selector and changing-byte counterexamples

Invoke `/consistency-check unknown:name`, `entity:`, `schema:` with whitespace name
and `full --unknown`. Expect legal mode/selector usage and correction, then stop
before spawn/write/verdict. Preserve every documented valid selector.

Bind a registered Game formula's grep scan to digest A; change the body/qualifier
to digest B before deep interpretation. Expect affected PASS withheld, preserved
earlier findings and a fresh baseline/recheck; do not combine A excerpts with B
meaning. Unchanged unrelated comparisons can retain their declared findings.
