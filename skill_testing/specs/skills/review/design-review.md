# Skill Test Spec: /design-review

## Skill Summary

`/design-review` reads the resolved design-document kind and evaluates its
actual owner requirements. Game/Product module CDDs use the eight semantic roles;
Concept/Quick Spec/Module Index use their actual templates/workflow sets.
It checks for internal consistency, implementability, and cross-system
conflicts. It produces a verdict of APPROVED, NEEDS REVISION, or MAJOR
REVISION NEEDED. Analysis is read-only. Optional report/log/index or repair effects require
separate named authority; allowed Write/Edit does not imply permission. Actual
review depth and reviewer independence are recorded, not inferred from a fork.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings or numbered steps
- [ ] Contains verdict keywords: APPROVED, NEEDS REVISION, MAJOR REVISION NEEDED
- [ ] Distinguishes read-only analysis, report-only and separately authorized repairs/indexes
- [ ] Output format is documented (review template shown in skill body)

---

## Test Cases

### Case 1: Happy Path — Complete GDD, all 8 sections present

**Fixture:**
- An isolated `design/cdd/light-manipulation.md` fixture is constructed with
  the eight substantive Game bodies below; a concept document is not a CDD stand-in
- All 8 required sections are populated with substantive content
- Formulas section contains at least one formula with defined variables
- Acceptance Criteria section contains at least 3 testable criteria

**Input:** `/design-review design/cdd/light-manipulation.md`

**Expected behavior:**
1. Skill reads the target document in full
2. Skill reads CLAUDE.md for project context and standards
3. Skill evaluates substantive bodies for all eight semantic roles, preserving aliases
4. Skill checks internal consistency (formulas match described behavior)
5. Skill checks implementability (rules are precise enough to code)
6. Skill outputs structured review with section-by-section status
7. Skill outputs APPROVED verdict

**Assertions:**
- [ ] Skill reads the target file before producing any output
- [ ] Module output maps X/8 substantive roles; other kinds use their owner X/Y
  with actual bodies and required evidence
- [ ] Output includes an "Internal Consistency" section
- [ ] Output includes an "Implementability" section
- [ ] Output ends with a verdict line: APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED
- [ ] APPROVED needs complete substantive coverage and all required selected-depth checks

---

### Case 2: Failure Path — Incomplete GDD (4/8 sections)

**Fixture:**
- Construct an isolated `design/cdd/light-manipulation.md` with four real
  bodies (Overview, Player Fantasy, Detailed Rules, Dependencies); Formulas,
  Edge Cases, Tuning Knobs and Acceptance Criteria are absent or placeholders.
  This is a declarative fixture, not a reference to a nonexistent tracked file.

**Input:** `/design-review design/cdd/light-manipulation.md`

**Expected behavior:**
1. Skill reads the document
2. Skill identifies 4 missing sections
3. Skill outputs "Completeness: 4/8 semantic roles substantively covered"
4. Skill lists specifically which 4 sections are missing
5. Skill outputs MAJOR REVISION NEEDED verdict (not APPROVED or NEEDS REVISION)

**Assertions:**
- [ ] Output shows "4/8" in the completeness section (not a higher number)
- [ ] Output explicitly names each missing section (Formulas, Edge Cases, Tuning Knobs, Acceptance Criteria)
- [ ] This fixture's missing formulas/outcomes/criteria cause MAJOR REVISION NEEDED;
  severity follows semantic impact, not section-count qualification alone
- [ ] Output does not suggest the document is implementation-ready
- [ ] Skill does not write any files (read-only enforcement)

---

### Case 3: Partial Path — 7/8 sections, minor inconsistency

**Fixture:**
- GDD has all sections except Formulas
- The described behavior mentions numeric values but no formulas are defined
- Acceptance Criteria exist but are vague ("feels good" rather than measurable)

**Input:** `/design-review design/cdd/[document].md`

**Expected behavior:**
1. Skill identifies missing Formulas section
2. Skill flags vague acceptance criteria as an implementability issue
3. Skill outputs NEEDS REVISION verdict (not APPROVED, not MAJOR REVISION NEEDED)
4. Skill provides specific remediation notes for each issue

**Assertions:**
- [ ] Verdict is NEEDS REVISION (not APPROVED, not MAJOR REVISION NEEDED) for 7/8 with issues
- [ ] Output identifies the missing Formulas section specifically
- [ ] Output flags the vague acceptance criteria as an implementability gap
- [ ] Each flagged issue has a specific, actionable remediation note

---

### Case 4: Edge Case — File not found

**Fixture:**
- The path provided does not exist in the project

**Input:** `/design-review design/cdd/nonexistent.md`

**Expected behavior:**
1. Skill attempts to read the file
2. File not found
3. Skill outputs an error message naming the missing file
4. Skill suggests checking the path or listing files in `design/cdd/`
5. Skill does NOT produce a verdict

**Assertions:**
- [ ] Skill outputs a clear error when the file is not found
- [ ] Skill does NOT output APPROVED, NEEDS REVISION, or MAJOR REVISION NEEDED when file is missing
- [ ] Skill suggests a corrective action (check path, list available GDDs)

---

---

### Case 5: Director Gate — no gate spawned regardless of review mode

**Fixture:**
- `design/cdd/light-manipulation.md` exists with all 8 sections
- `production/review-mode.txt` exists with `full` (most permissive mode)

**Input:** `/design-review design/cdd/light-manipulation.md` (with full review mode active)

**Expected behavior:**
1. Skill reads the GDD document
2. Skill does NOT read `review-mode.txt` — this skill has no director gates
3. Skill produces the review output normally
4. No director-gate workflow is spawned; full analysis still runs its actual
   specialists and senior creative-director review role
5. Verdict is APPROVED (all 8 sections present in fixture)

**Assertions:**
- [ ] Skill does NOT spawn any director gate agent (CD-, TD-, PR-, AD- prefixed agents)
- [ ] Skill does NOT read `review-mode.txt` or equivalent mode file
- [ ] The `--review` flag or `full` mode state has NO effect on whether directors spawn
- [ ] Output does not contain any "Gate: [GATE-ID]" entries
- [ ] Director gates are distinct from the selected-depth specialists/senior synthesis

---

## Protocol Compliance

- [ ] Read-only calls no write entrypoint; report-only touches only its new assigned report
- [ ] Presents complete findings before any verdict
- [ ] Does not ask for approval before producing output (no writes to approve)
- [ ] Ends with recommended next step (e.g., fix issues and re-run, or proceed to `/map-systems`)

---

## Coverage Notes

- Cross-system consistency checking (Case 3 in the skill's own phase list) is
  not directly tested here because it requires multiple GDD files to compare;
  this is covered by the `/review-all-gdds` spec instead.
- Actual specialist execution and independence require runtime/actor evidence;
  a new context or static source assertions cannot establish those qualifications.
- Performance and edge cases involving very large GDD files are not in scope.

---

### Semantic case: Repairs invalidate the old review baseline

Begin a read-only full review with exact CDD/dependency identities and actual
required specialists. Put a contradictory rule in an indirectly referenced
attachment while keeping the primary CDD unchanged. Expect the conflict found
through closure and no input/index/session writes. Repair by the author produces
new input identities; the original review is preserved and cannot certify them.
A non-writing reviewer must check the revised baseline. Same-byte continuation
may resume unfinished checks only with the same rule/scope/closure; pending
specialists cannot be relabeled full completion. Saving one assigned report
does not update the rolling log, module index or T3 index.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.


### Invalid mode/depth input

Supply an invalid explicit mode/depth (or invalid global director mode where
used). Expect a named corrective error and no silent fallback, reviewer spawn
or write. Absent settings retain the documented default. Analysis depth,
director mode and write authority remain distinct.

---

### Document-kind counterexamples: Concept, Quick Spec, Module Index and unknown

Construct fully authored Game/Product concept fixtures using actual
`skills/brainstorm/SKILL.md` generation requirements together with
`templates/game-concept.md` and `templates/product-concept.md` sets, including
workflow-required Visual Identity Anchor and required referenced bodies/evidence. Invoke the real /brainstorm handoff
`/design-review design/cdd/game-concept.md` and Product equivalent. Expect
kind/provenance/template owner reported and full-body/template-role review;
absence of module Formulas/Tuning Knobs alone is not a missing concept role.
Replace Game Core Loop or Product User Journey with placeholders: coverage fails,
despite many headings. Remove the Game Visual Identity Anchor while preserving
all Game-template headings: the workflow-added required role is missing and
concept completeness cannot pass. Repeat for Product's missing Anchor body.
No template/kind exemption from full-body reading or required closure.

Use the actual /quick-design Tuning format and /map-systems module-index template:
review their complete category/owner sets, not Module8. An unknown title/body with
no resolvable owner prompts classification and remains incomplete, never default
module or APPROVED. Record X/Y against the resolved owner, Y=8 only for a module.
