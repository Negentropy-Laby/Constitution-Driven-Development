# Skill Test Spec: /adopt

## Skill Summary

`/adopt` audits an existing project's artifacts — GDDs, ADRs, stories, infrastructure
files, and `technical-preferences.md` — for format compliance with the template's
skill pipeline. It classifies every gap by severity (BLOCKING / HIGH / MEDIUM / LOW),
composes a numbered, ordered migration plan, and writes it to `docs/adoption-plan-[date].md`
after explicit user approval via `AskUserQuestion`.

This skill is distinct from `/project-stage-detect` (which checks what exists).
`/adopt` checks selected substantive format/owner compatibility; this is not
runtime execution or qualification proof.

No director gates apply. The skill does NOT invoke any director agents.

---

## Static Assertions (Structural)

Structural observations by `/skill-test static` are separate from behavioral reasoning/execution.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains severity tier keywords: BLOCKING, HIGH, MEDIUM, LOW
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (e.g., offering to fix the highest-priority gap immediately)

---

## Director Gate Checks

None. `/adopt` is a brownfield audit utility. No director gates apply.

---

## Test Cases

### Case 1: Happy Path — All GDDs compliant, no gaps, COMPLIANT

**Fixture:**
- `design/cdd/` contains 3 GDD files; each has all 8 required sections with content
- `docs/architecture/adr-0001.md` exists with `## Status`, `## Engine Compatibility`,
  and all other required sections
- `production/stage.txt` exists
- `docs/architecture/tr-registry.yaml` and `docs/architecture/control-manifest.md` exist
- Engine configured in `technical-preferences.md`

**Input:** `/adopt`

**Expected behavior:**
1. Skill emits "Scanning project artifacts..." then reads all artifacts silently
2. Reports detected phase, GDD count, ADR count, story count
3. Phase 2 audit: all 3 GDDs have all 8 sections, Status field present and valid
4. ADR audit: all required sections present
5. Infrastructure audit: all critical files exist
6. Phase 3: zero BLOCKING, zero HIGH, zero MEDIUM, zero LOW gaps
7. Summary reports no blocking gaps in the audited format scope; runtime/project
   qualification remains separately unverified.
8. Uses `AskUserQuestion` to ask about writing the plan; user selects write
9. Adoption plan is written to `docs/adoption-plan-[date].md`
10. Phase 7 offers next action: no blocking gaps, offers options for next steps

**Assertions:**
- [ ] Skill reads silently before presenting any output
- [ ] "Scanning project artifacts..." appears before the silent read phase
- [ ] Gap counts show 0 BLOCKING, 0 HIGH, 0 MEDIUM (or only LOW)
- [ ] Existing named plan authority continues; absent scope uses `AskUserQuestion` before writing
- [ ] Adoption plan file is written to `docs/adoption-plan-[date].md`
- [ ] Phase 7 offers a specific next action (not just a list)

---

### Case 2: Non-Compliant Documents — GDDs missing sections, NEEDS MIGRATION

**Fixture:**
- `design/cdd/` contains 2 GDD files:
  - `combat.md` — missing `## Acceptance Criteria` and `## Formulas` sections
  - `movement.md` — all 8 sections present
- One ADR (`adr-0001.md`) is missing `## Status` section
- `docs/architecture/tr-registry.yaml` does not exist

**Input:** `/adopt`

**Expected behavior:**
1. Skill scans all artifacts
2. Phase 2 audit finds:
   - `combat.md`: 2 missing sections (Acceptance Criteria, Formulas)
   - `adr-0001.md`: missing `## Status` — BLOCKING impact
   - `tr-registry.yaml`: missing — HIGH impact
3. Phase 3 classifies:
   - BLOCKING: relied-on `adr-0001.md` lacks verifiable status/acceptance
   - HIGH: `tr-registry.yaml` missing; `combat.md` missing Acceptance Criteria (can't generate stories)
   - MEDIUM: `combat.md` missing Formulas
4. Phase 4 builds ordered migration plan:
   - Step 1 (BLOCKING): Add `## Status` to `adr-0001.md` — command: `/architecture-decision retrofit`
   - Step 2 (HIGH): Run `/architecture-review` to bootstrap tr-registry.yaml
   - Step 3 (HIGH): Add Acceptance Criteria to `combat.md` — command: `/design-system retrofit`
   - Step 4 (MEDIUM): Add Formulas to `combat.md`
5. Gap Preview shows BLOCKING items as bullets (actual file names), HIGH/MEDIUM as counts
6. `AskUserQuestion` asks to write the plan; writes after approval
7. Phase 7 offers to fix the highest-priority gap (ADR Status) immediately

**Assertions:**
- [ ] BLOCKING gaps are listed as explicit file-name bullets in the Gap Preview
- [ ] HIGH and MEDIUM shown as counts in Gap Preview
- [ ] Migration plan items are in BLOCKING-first order
- [ ] Each plan item includes the fix command or manual steps
- [ ] Missing/new scope is requested before writing; matching named authority continues
- [ ] Phase 7 offers to immediately retrofit the first BLOCKING item

---

### Case 3: Mixed State — Some docs compliant, some not, partial report

**Fixture:**
- 4 GDD files: 2 fully compliant, 2 with gaps (one missing Tuning Knobs, one missing Edge Cases)
- ADRs: 3 files — 2 compliant, 1 missing `## ADR Dependencies`
- Stories: 5 files — 3 have TR-ID references, 2 do not
- Infrastructure: all critical files present; `technical-preferences.md` fully configured

**Input:** `/adopt`

**Expected behavior:**
1. Skill audits all artifact types
2. Audit summary shows totals: "4 GDDs (2 fully compliant, 2 with gaps); 3 ADRs
   (2 fully compliant, 1 with gaps); 5 stories (3 with TR-IDs, 2 without)"
3. Gap classification:
   - No BLOCKING gaps
   - HIGH: 1 ADR missing `## ADR Dependencies`
   - MEDIUM: 2 GDDs with missing sections; 2 stories missing TR-IDs
   - LOW: none
4. Migration plan lists HIGH gap first, then MEDIUM gaps in order
5. Note preserves existing stories and requires current legacy recheck for missing
   required identity/evidence; it does not promise missing-field auto-pass.
6. `AskUserQuestion` to write plan; writes after approval

**Assertions:**
- [ ] Per-artifact compliance tallies are shown (N compliant, M with gaps)
- [ ] Existing bodies/history preserved; absent required fields do not auto-pass
- [ ] No BLOCKING gaps results in no BLOCKING section in migration plan
- [ ] HIGH gap precedes MEDIUM gaps in plan ordering
- [ ] Missing/new scope is requested before writing; matching named authority continues

---

### Case 4: No Artifacts Found — Fresh project, guidance to run /constitute

**Fixture:**
- Repository has no files in `design/cdd/`, `docs/architecture/`, `production/epics/`
- `production/stage.txt` does not exist
- `src/` directory does not exist or has fewer than 10 files
- No game-concept.md, no module-index.md

**Input:** `/adopt`

**Expected behavior:**
1. Phase 1 existence check finds no artifacts
2. Skill infers "Fresh" — no brownfield work to migrate
3. Uses `AskUserQuestion`:
   - "This looks like a fresh project — no existing artifacts found. `/adopt` is for
     projects with work to migrate. What would you like to do?"
   - Options: "Run `/constitute`", "My artifacts are in a non-standard location", "Cancel"
4. Skill stops — does not proceed to audit regardless of user selection

**Assertions:**
- [ ] `AskUserQuestion` is used (not a plain text message) when no artifacts are found
- [ ] `/constitute` is presented as a named option
- [ ] Skill stops after the question — no audit phases run
- [ ] No adoption plan file is written

---

### Case 5: Director Gate Check — No gate; adopt is a utility audit skill

**Fixture:**
- Project with a mix of compliant and non-compliant GDDs

**Input:** `/adopt`

**Expected behavior:**
1. Skill completes full audit and produces migration plan
2. No director agents are spawned at any point
3. No gate IDs (CD-*, TD-*, AD-*, PR-*) appear in output
4. No `/gate-check` is invoked during the skill run

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Skill reaches plan-writing or cancellation without any gate verdict

---

## Protocol Compliance

- [ ] Emits "Scanning project artifacts..." before silent read phase
- [ ] Reads all artifacts silently before presenting any results
- [ ] Shows Adoption Audit Summary and Gap Preview before asking to write
- [ ] Reuses exact named plan authority; requests absent/new effects after concrete scope
- [ ] Adoption plan written to `docs/adoption-plan-[date].md` — not to any other path
- [ ] Migration plan items ordered: BLOCKING first, HIGH second, MEDIUM third, LOW last
- [ ] Phase 7 always offers a single specific next action (not a generic list)
- [ ] Preserves existing bodies/history and repairs only named approved gaps
- [ ] Does not invoke director gates at any point

---

## Coverage Notes

- The `cdds`, `adrs`, `stories`, and `infra` argument modes narrow the audit scope;
  each follows the same pattern as the full audit but limited to that artifact type.
  Not separately fixture-tested here.
- The module-index.md parenthetical status value check (BLOCKING) is a special case
  that triggers an immediate fix offer before writing the plan; not separately tested.
- The review-mode.txt prompt (Phase 6b) runs after plan writing if `production/review-mode.txt`
  does not exist; not separately tested here.

## Domain, owner and effect counterexamples

**Fixture A:** Game combat/movement CDDs keep Player Fantasy/formulas/tuning
bodies. Product CLI/API/data/auth CDDs use substantive User Promise/JTBD,
Detailed Behavior, Contracts/Data Model and Configuration Knobs aliases.
Concept/index/support documents use their own actual DocKind contracts.
- [ ] Read actual bodies/owners; both module branches are audited without requiring
  a module-eight shape on concept/index/support or deleting Game examples.
- [ ] Placeholder headings/keyword hits cannot establish compliance/qualification.

**Fixture B:** Existing Story lacks manifest identity and references no ADR;
its local detail has a valid named CDD/no-ADR disposition. Variant changes a
public trust boundary without Accepted decision.
- [ ] First receives required current LegacyRecheck, not missing-field auto-PASS
  or manufactured ADR/TR-ID. Second blocks affected decision coverage under
  `standards/notes-adr-sync.md`, with independent audit continuing.

**Fixture C:** Report-only/declined plan save; absent review-mode or an existing
empty/invalid review-mode; source definitions and adapter copies exist.
- [ ] No repair/review-mode/state writes from report-only or preference selection.
- [ ] Invalid existing modes are surfaced instead of silently skipped.
- [ ] Scoped named plan authority continues without repeated requests.
- [ ] Zero high/blocking format gaps and adapter presence do not prove runtime
  execution, qualification, acceptance, publication or completion.
