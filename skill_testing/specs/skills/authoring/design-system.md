# Skill Test Spec: /design-system

## Skill Summary

`/design-system` authors, retrofits or synchronizes Game/Product CDDs.
`design/INSTRUCTIONS.md` owns the semantic eight roles and existing aliases.
New files use an authorized skeleton; existing bodies/examples are preserved
outside named changes. Document/batch/sync authority persists across sections.
CD-GDD-ALIGN runs once after completed scoped drafting in full mode; lean/solo
skip it. Drafting, gate verdict, independent review and completion are distinct.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: APPROVED, NEEDS REVISION, MAJOR REVISION
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end
- [ ] Documents new-file skeleton and preservation of existing retrofit/sync bodies
- [ ] Documents CD-GDD-ALIGN: full post-design; skipped in lean/solo
- [ ] Documents retrofit mode for existing GDD files

---

## Director Gate Checks

Resolve mode once using explicit `--review`, `production/review-mode.txt`,
then lean. CD-GDD-ALIGN runs after post-design readback in full mode. Lean/solo
report it skipped; no repeated per-section gate. A gate objection requires
resolution/recheck of affected scope, not retroactive claims that the draft was
never written. The gate cannot grant file authority or independent author review.

---

## Test Cases

### Case 1: Happy Path — New Game CDD in lean mode

**Fixture:** No target CDD; `production/review-mode.txt` is lean. The user
authorizes the shown new CDD path and full document drafting, excluding indexes.

**Input:** `/design-system [system-name]`

**Expected behavior:** Create the authorized skeleton, draft and write meaningful
Game sections incrementally, then read actual bodies and required closure.
Reuse the document authority without a question for every section. Report
CD-GDD-ALIGN skipped in lean, all eight semantic roles and independent review pending.

**Assertions:**
- [ ] Game Player Fantasy, rules, formulas, edge outcomes and measurable criteria are substantive
- [ ] No repeated covered-write approval or CD-GDD-ALIGN spawn
- [ ] Session state, registry and module index remain unchanged when excluded
- [ ] Draft completion does not claim independent review or Story/phase completion

---

### Case 2: Retrofit Mode — Existing GDD, update specific section

**Fixture:**
- `design/cdd/[system-name].md` already exists with all 8 sections populated

**Input:** `/design-system [system-name]`

**Expected behavior:**
1. Skill detects existing GDD file and reads its current content
2. Skill offers named gap/selected-section retrofit and preserves existing prose
3. User selects a specific section (e.g., Formulas)
4. Skill authors only the authorized Formulas section, runs the selected-mode
   post-design gate and asks "May I write?" only if authority is absent
5. Only the selected section is updated — other sections are not modified

**Assertions:**
- [ ] Skill detects and reads existing GDD before offering retrofit mode
- [ ] User is asked which section to update — not asked to rewrite the whole document
- [ ] Only the selected section is rewritten — others remain unchanged
- [ ] CD-GDD-ALIGN runs post-design only if full mode was selected
- [ ] "May I write" is asked before updating the section

---

### Case 3: Director Gate — Objection to completed Player Fantasy

**Fixture:** A new Game CDD is drafted in full mode. Its actual post-design
CD-GDD-ALIGN review flags the Player Fantasy as contrary to the named pillar.

**Input:** `/design-system [system-name] --review full`

**Expected behavior:** Surface the actual finding, revise only affected content
within authority and reread a fresh exact baseline. Repeat the affected gate
check before finalization; preserve prior results and pending independent review.

**Assertions:**
- [ ] Actual post-design gate and its input scope are recorded
- [ ] Unresolved pillar issue is not represented as finalized approval
- [ ] Repair changes the baseline; an old review cannot certify new bytes
- [ ] Unrelated existing Game examples remain intact

---

### Case 4: Solo Mode — CD-GDD-ALIGN skipped; sections written with user approval only

**Fixture:**
- New GDD being authored; user explicitly prefers approval per section
- `production/review-mode.txt` contains `solo`

**Input:** `/design-system [system-name]`

**Expected behavior:**
1. Skeleton file is created with 8 section headers
2. For each section: drafted, shown to user
3. CD-GDD-ALIGN is skipped — noted for the run: "CD-GDD-ALIGN skipped — solo mode"
4. "May I write [section]?" asked after user reviews draft
5. Section written after user approval
6. No gate review at any stage

**Assertions:**
- [ ] "CD-GDD-ALIGN skipped — solo mode" noted for the run
- [ ] Sections are written after user approval alone (no gate required)
- [ ] Skill does NOT spawn any CD-GDD-ALIGN gate in solo mode
- [ ] Full GDD is written with only user approval in solo mode

---

### Case 5: Director Gate — Empty sections not written to file

**Fixture:**
- GDD authoring in progress
- User and skill discuss one section but do not produce any approved content
  (e.g., discussion ends without a decision, or user says "skip for now")

**Input:** `/design-system [system-name]`

**Expected behavior:**
1. Section discussion produces no approved content
2. Skill does NOT write an empty or placeholder body to the section
3. The section header remains in the skeleton file but the body stays empty
4. Skill moves to the next section without writing the empty one
5. At the end, incomplete sections are listed and user is reminded to return to them

**Assertions:**
- [ ] Empty or unapproved sections are NOT written to the file
- [ ] Skeleton section header remains (preserves structure)
- [ ] Skill tracks and lists incomplete sections at the end of the session
- [ ] Skill does NOT write "TBD" or placeholder content without user approval

---

### Case 6: CDD semantic aliases and document-kind scope

**Fixture:**
A Game ModuleCDD substantively covers all eight roles but uses Core
Specification instead of Detailed Rules. A second ModuleCDD lacks actual edge
behavior. A separate Concept/Registry has its own non-Module8 owner set.

**Input:** `/design-system [fixture module]` in the existing retrofit scope

**Expected behavior:**
1. Resolve DocKind and required owner roles from design/INSTRUCTIONS.md.
2. Preserve valid substantive aliases and identify genuinely missing required roles.
3. Apply the non-module document's own requirements without forcing Module8.

**Assertions:**
- [ ] The valid alias is retained and is not failed solely for its heading.
- [ ] The real missing edge-case role remains a named gap, not a passing keyword check.
- [ ] Concept/Registry scope is not forced into the eight-module-section contract.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Skeleton only for a new file; retrofit/sync preserves unaffected bodies
- [ ] Approved paths/effects persist; unresolved material choices remain explicit
- [ ] Actual bodies map to eight roles with legacy aliases under `design/INSTRUCTIONS.md`
- [ ] Full post-design gate versus lean/solo skip is reported accurately
- [ ] Readback, semantic coverage, independent review and completion are separate
- [ ] Next steps are recommendations unless execution is already authorized

---

## Coverage Notes

- The 8 required sections are validated against the project's design document
  standards owned by `design/INSTRUCTIONS.md`, including Product aliases.
- The skill's internal section-ordering logic (which section to author first) is
  not independently tested — the order follows the standard GDD template.
- Pillar alignment checking within CD-GDD-ALIGN is evaluated holistically by
  the gate agent — specific pillar checks are not fixture-tested here.

---

### Semantic case: Implementation-first synchronization preserves Target

Construct a Game CDD with an existing `Detailed Design / Core Rules` alias and
original crafting/damage examples, plus a Product CDD using `User Promise`,
`Data Model` and `Configuration` aliases. Bind a fixed commit plus a working
source change and an ignored referenced test input. Authorize only two named
CDD section edits, excluding registry/session/index effects.

Invoke `/design-system sync [named scope]`. Expect actual eight-role body mapping,
exact old/new evidence, retained unaffected examples and distinct As-Is/Target.
A shipped state-ownership change is `adr-required` until acceptance; an unrelated
tuning clarification can be `cdd-layer`. Reuse approved writes, block only affected
implementation and obtain required non-writing review of the final bound inputs.
A placeholder/heading-only role cannot pass merely because eight headings exist.


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

### Dispatcher counterexample: Sync cannot create a module

Authorize a sync batch over two existing CDDs. After exact readback, applicable
validation and required review, expect a batch report and skill return; neither
a file named for the scope nor a new skeleton/module-index row/section cycle is
created. Invoke `/design-system sync` with no scope and invoke a valid module with
`--unknown`: expect legal usage/correction and stop before spawn/write/verdict.
Existing module, retrofit-path and valid --review invocations remain supported.


### Retrofit kind guard

Invoke the legacy existing-file/retrofit route on Game/Product concept and
Module Index fixtures with full substantive owner content. Expect full target
read and kind verification, the actual /brainstorm or /map-systems owner route
and legal module retrofit usage, then return without writes or Module8 gap edits.
Unknown kind is clarified rather than assumed module. A verified module keeps
legacy retrofit behavior; explicitly authorized sync continues to use each kind's
actual workflow-plus-template owner set.

### Effective public defaults differ from private helper defaults

Product fixture: the CLI parser's `--dry-run` is false when absent and passes its
parsed value explicitly to a validation helper whose own default is true. The
CDD owns the public CLI default and separately permits the helper's safe default.
Game fixture: the configured public timing window is 120 ms and is explicitly
passed to a helper whose local default is 90 ms. A separate variant stops passing
the configured value, producing a real governing public-contract mismatch.
- [ ] Read the owning entrypoint, parser/configuration and actual call flow;
  record public defaults/overrides separately from internal safe defaults.
- [ ] Matching effective public behavior is not reported as a default mismatch;
  real unrelated contract gaps remain findings under their own actual evidence.
- [ ] The true mismatching variant preserves Target and reports affected gaps
  without silently changing helper/source/CDD inputs under review-only authority.
