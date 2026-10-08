# Skill Test Spec: /ux-design

## Skill Summary

`/ux-design` is a guided, section-by-section UX spec authoring skill. It produces
user flow diagrams (described textually), interaction state definitions, wireframe
descriptions, and accessibility notes for a specified screen or HUD element. The
skill uses an authorized skeleton for a new file, then fills sections incrementally
within the approved document/batch scope. Retrofit preserves existing substantive
bodies and examples outside selected changes.

The skill has no inline director gates — `/ux-review` is the separate review step.
Uncovered writes need "May I write [path]?"; existing scope persists. If a UX spec
already exists for the named screen, the skill offers to retrofit individual sections
rather than replace. Verdict is COMPLETE when all sections are written.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keyword: COMPLETE
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (e.g., `/ux-review` to validate the completed spec)

---

## Director Gate Checks

None. `/ux-design` has no inline director gates. `/ux-review` is the separate
review skill invoked after this skill completes.

---

## Test Cases

### Case 1: Happy Path — New HUD spec, all sections authored and written

**Fixture:**
- No existing HUD UX spec in `design/ux/`
- Engine and rendering preferences configured

**Input:** `/ux-design hud`

**Expected behavior:**
1. Skill creates a skeleton file `design/ux/hud.md` with all section headers
2. Skill discusses and drafts each section: User Flows, Interaction States
   (normal/hover/focus/disabled), Wireframe Description, Accessibility Notes
3. After each draft, reuse explicit HUD document scope; ask only unresolved
   choices, uncovered effects or an explicit section-by-section preference
4. Each section is written in sequence after approval
5. After all sections are written, verdict is COMPLETE
6. Skill suggests running `/ux-review` as the next step

**Assertions:**
- [ ] Skeleton file is created first (with empty section bodies)
- [ ] Approved HUD document scope persists without repeated covered-write asks
- [ ] All required sections are present: User Flows, Interaction States,
     Wireframe Description, Accessibility Notes
- [ ] Handoff to `/ux-review` is at the end
- [ ] Verdict is COMPLETE

---

### Case 2: Existing UX Spec — Retrofit: user picks section to update

**Fixture:**
- `design/ux/hud.md` already exists with all sections populated
- User wants to update only the Accessibility Notes section

**Input:** `/ux-design hud`

**Expected behavior:**
1. Skill reads existing `design/ux/hud.md` and detects all sections are populated
2. Skill reports: "UX spec already exists for HUD — offering to retrofit"
3. Skill lists all sections and asks which to update
4. User selects Accessibility Notes
5. Skill drafts updated accessibility content and asks "May I write section
   Accessibility Notes to `design/ux/hud.md`?"
6. Only that section is updated; other sections are preserved; verdict is COMPLETE

**Assertions:**
- [ ] Existing spec is detected and retrofit is offered
- [ ] User selects which section(s) to update
- [ ] Only the selected section is updated — other sections unchanged
- [ ] "May I write" is asked for the updated section
- [ ] Verdict is COMPLETE

---

### Case 3: Dependency Gap — Spec references a system with no design doc

**Fixture:**
- User is authoring a UX spec for the inventory screen
- `design/cdd/inventory.md` does not exist

**Input:** `/ux-design inventory-screen`

**Expected behavior:**
1. Skill begins authoring the inventory screen UX spec
2. During the User Flows section, skill attempts to reference inventory system rules
3. Skill detects: "No GDD found for inventory system — UX spec has a DEPENDENCY GAP"
4. The dependency gap is flagged in the spec (noted inline: "DEPENDENCY GAP: inventory GDD")
5. Skill continues independent sections while marking affected rules incomplete;
   placeholders do not establish coverage or lower the governing Target
6. Draft execution and affected dependency/readiness status are reported separately

**Assertions:**
- [ ] DEPENDENCY GAP label appears in the spec for the missing system doc
- [ ] Only affected rules/readiness remain blocked; independent sections may proceed
- [ ] Dependency gap is also noted in the skill output (not just in the file)
- [ ] Handoff suggests both `/ux-review` and writing the missing GDD

---

### Case 4: No Argument Provided — Resolve surface and output path

**Fixture:** No screen/HUD/flow argument or established scope.

**Input:** `/ux-design`

**Expected behavior:** Ask the documented mode/surface question, offering Game
HUD/screen/flow and relevant Product workflow choices. Resolve the actual output
path before drafting/new-file creation. No choice means no arbitrary file write.

**Assertions:**
- [ ] Existing explicit surface/scope is reused when present
- [ ] Missing surface is requested; no guessed target is written
- [ ] New-file authority is separate from the surface/content decision
- [ ] No module/session/Memory Bank side effect accompanies selection

---

### Case 5: Director Gate Check — No gate; ux-review is the separate review skill

**Fixture:**
- New screen spec with argument provided

**Input:** `/ux-design settings-menu`

**Expected behavior:**
1. Skill authors all sections of the settings menu UX spec
2. No director agents are spawned
3. No gate IDs appear in output during authoring

**Assertions:**
- [ ] No director gate is invoked during ux-design
- [ ] No gate skip messages appear
- [ ] Verdict is COMPLETE without any gate check

---

## Protocol Compliance

- [ ] Creates an authorized skeleton only for new files; existing specs are preserved
- [ ] Discusses and drafts one section at a time
- [ ] Reuses approved scope; asks unresolved design choices/uncovered effects
- [ ] Detects existing spec and offers retrofit path
- [ ] Ends with handoff to `/ux-review`
- [ ] Verdict is COMPLETE when all sections are written

---

## Coverage Notes

- Interaction state enumeration (normal/hover/focus/disabled/error) is a core
  requirement of each spec; the `/ux-review` skill checks for completeness.
- Wireframe descriptions are text-only (no images); image references may be
  added manually by a designer after the fact.
- Responsive layout concerns (different screen sizes) are noted as optional
  content and not assertion-tested here.

---

### Semantic case: Retrofit and bounded dependency gap

Start with the original Game HUD layout/examples and a Product workflow spec.
Authorize only named accessibility sections as one batch. Preserve all other
bodies and reuse the scope without repeated write questions. Leave a required
inventory/permission contract inaccessible: mark the affected interaction rules
incomplete, preserve Target and continue independent accessibility work.
Read back actual spec and required journey/pattern/contract closure. Optional
state/cross-links remain unchanged when excluded; recommendations do not run
/ux-review. Draft completion cannot claim independent review or readiness.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.
