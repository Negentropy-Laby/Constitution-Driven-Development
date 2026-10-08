# Skill Test Spec: /reverse-document

## Skill Summary

`/reverse-document` generates design or architecture documentation from existing
source code. It reads the exact specified source set, documents observed behavior,
asks unresolved intent and preserves governing Target separately, producing either a
GDD skeleton (for gameplay systems) or an architecture overview (for technical
systems). The output is a best-effort inference — magic numbers and undocumented
logic may result in a PARTIAL verdict.

The skill asks "May I write to [inferred path]?" before creating the document.
No director gates apply. COMPLETE/PARTIAL describes document execution/coverage,
not independent review or decision acceptance. Architecture output remains Proposed.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, PARTIAL
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (e.g., `/design-review` to validate the generated doc)

---

## Director Gate Checks

None. `/reverse-document` is a documentation utility. No director gates apply.

---

## Test Cases

### Case 1: Well-Structured Source — Accurate design doc skeleton produced

**Fixture:**
- `src/gameplay/health_system.gd` exists with:
  - `@export var max_health: int = 100`
  - `func take_damage(amount: int)` with clamping logic
  - `signal health_changed(new_value: int)`
  - Docstrings on all public methods

**Input:** `/reverse-document src/gameplay/health_system.gd`

**Expected behavior:**
1. Skill reads the source file and identifies the health system
2. Skill observes max health, take_damage behavior and health signal at the
   bound baseline; intent is clarified or labeled unknown
3. Skill produces substantive Game bodies mapped to eight required roles:
   Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies,
   Tuning Knobs, Acceptance Criteria
4. Formulas section includes the inferred clamping formula
5. Tuning Knobs notes `max_health = 100` as a configurable value
6. Skill asks "May I write to `design/cdd/health-system.md`?"
7. Authorized file written/read back; document outcome COMPLETE with review pending

**Assertions:**
- [ ] All 8 required GDD sections are present in the output
- [ ] `max_health = 100` appears as a Tuning Knob
- [ ] Clamping formula is captured in the Formulas section
- [ ] "May I write" is asked with the inferred path
- [ ] Verdict is COMPLETE

---

### Case 2: Ambiguous Source — Magic Numbers, PARTIAL Verdict

**Fixture:**
- `src/gameplay/enemy_ai.gd` exists with:
  - Inline magic numbers: `if distance < 150:`, `speed = 3.5`
  - No comments or docstrings
  - Complex state machine logic that is not self-explanatory

**Input:** `/reverse-document src/gameplay/enemy_ai.gd`

**Expected behavior:**
1. Skill reads the file and detects magic numbers with no context
2. Skill produces a GDD skeleton with notes: "AMBIGUOUS VALUE: 150 (unknown units —
   is this pixels, world units, or tiles?)"
3. Skill marks the Formulas and Tuning Knobs sections as requiring human review
4. Skill asks "May I write to `design/cdd/enemy-ai.md`?" with PARTIAL advisory
5. File written with PARTIAL markers; verdict is PARTIAL

**Assertions:**
- [ ] AMBIGUOUS VALUE annotations appear for magic numbers
- [ ] Sections needing human review are marked explicitly
- [ ] Verdict is PARTIAL (not COMPLETE)
- [ ] File is still written — PARTIAL is not a blocking failure

---

### Case 3: Multiple Interdependent Files — Cross-System Overview Produced

**Fixture:**
- User provides 2 source files: `combat_system.gd` and `damage_resolver.gd`
- The files reference each other (combat calls damage_resolver)

**Input:** `/reverse-document src/gameplay/combat_system.gd src/gameplay/damage_resolver.gd`

**Expected behavior:**
1. Skill reads both files and detects the dependency relationship
2. With architecture type selected, skill produces a Proposed cross-system
   ADR/analysis; multiple filenames alone do not authorize architecture acceptance
3. Overview describes: Combat System → Damage Resolver interaction, shared
   interfaces, data flow between the two
4. Skill asks "May I write to `docs/architecture/combat-damage-overview.md`?"
5. Overview written after approval; verdict is COMPLETE (or PARTIAL if ambiguous)

**Assertions:**
- [ ] Both files are analyzed together (not as two separate docs)
- [ ] Cross-system dependency is documented in the output
- [ ] Output file is written to `docs/architecture/` (not `design/cdd/`)
- [ ] Verdict is COMPLETE or PARTIAL

---

### Case 4: Source File Not Found — Error

**Fixture:**
- `src/gameplay/inventory_system.gd` does not exist

**Input:** `/reverse-document src/gameplay/inventory_system.gd`

**Expected behavior:**
1. Skill attempts to read the specified file — not found
2. Skill outputs: "Source file not found: src/gameplay/inventory_system.gd"
3. Skill suggests checking the path or running `/map-systems` to identify
   the correct source file
4. No document is created

**Assertions:**
- [ ] Error message names the missing file with the full path
- [ ] Alternative suggestion (check path or `/map-systems`) is provided
- [ ] No write tool is called
- [ ] No verdict is issued (error state)

---

### Case 5: Director Gate Check — No gate; reverse-document is a utility

**Fixture:**
- Well-structured source file exists

**Input:** `/reverse-document src/gameplay/health_system.gd`

**Expected behavior:**
1. Skill generates and writes the design doc
2. No director agents are spawned
3. No gate IDs appear in output

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Verdict is COMPLETE or PARTIAL — no gate verdict involved

---

## Protocol Compliance

- [ ] Reads source file(s) before generating any content
- [ ] Produces all 8 required GDD sections when target is a gameplay system
- [ ] Annotates ambiguous values with AMBIGUOUS VALUE markers
- [ ] Multiple source files form an exact declared input set; explicit type controls output
- [ ] Asks "May I write" before creating any output file
- [ ] Verdict is COMPLETE (clean inference) or PARTIAL (ambiguous fields)

---

## Coverage Notes

- Architecture and CDD formats differ; explicit type/scope controls output,
  while legacy path-only invocations ask unresolved type rather than accepting a decision.
- The case where a source file is readable but contains only auto-generated
  boilerplate with no meaningful logic is not tested; skill would likely produce
  a near-empty skeleton with a PARTIAL verdict.
- C# and Blueprint source files follow the same inference pattern as GDScript;
  language-specific differences are handled in the skill body.

---

### Semantic case: Shipped code does not accept a decision

Use the original Game health/damage fixture and a Product public contract whose
implemented error behavior violates its governing Target. With explicit existing
CDD update scope, record exact source/test identities and As-Is/Target/gap bodies;
preserve original promised behavior and unknown intent. Select architecture type:
the generated decision is Proposed with reverse-documentation provenance, even
with green tests and write approval. No inferred decision maker/date accepts it.
A read-only analysis and assigned report never change code, status/indexes or
sensitive settings; missing retained source bytes prevents exact reconstruction.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.
