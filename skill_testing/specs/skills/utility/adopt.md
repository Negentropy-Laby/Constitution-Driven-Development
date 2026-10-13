# Skill Test Spec: /adopt

## Skill Summary

`/adopt` audits an existing project's artifacts — GDDs, ADRs, stories, infrastructure
files, and `standards/technical-preferences.md` — for format compliance with the template's
skill pipeline. It classifies every gap by severity (BLOCKING / HIGH / MEDIUM / LOW),
composes a numbered, ordered migration plan, and writes it to `docs/adoption-plan-[date].md`
within exact named plan-write authority; missing/new scope uses `AskUserQuestion`
after the concrete preview.

This skill is distinct from `/project-stage-detect` (which checks what exists).
`/adopt` checks selected substantive format/owner compatibility; this is not
runtime execution or qualification proof.

No director gates apply. The skill does NOT invoke any director agents.

## Fixture and evidence contract

The cases below describe isolated fixture inputs. Apply the complete current
`/skill-test` owner and `standards/evidence-lifecycle.md`: spec reasoning,
static structure checks, fixture execution and independent review are separate
results. An expected result or fixture description is not a recorded runtime PASS.

Before execution, bind the selected runtime entries, actual governing project
instructions, configuration and required direct/indirect input bytes. Use
`standards/technical-preferences.md` as the canonical preference path.
Read substantive bodies; missing/unread required originals leave the affected
check pending. Optional, example, future-output and inapplicable references are
not required inputs merely because their paths appear in an instruction.

Establish actual CDD provenance, ownership and Source/Target delivery role before
classifying purpose. Source developer templates and complete projections are
framework product assets. In a Target, confirmed CDD packages/support remain
local-only but readable ignored inputs may be discovered, loaded and used within
authority. Project-owned development skills, native roles, tools and documents
retain project rules. A maintenance toolkit is optional for ordinary use.

Reasoning/review-only runs invoke no write entrypoint. Any expected writer action
runs only in an isolated fixture with the exact named paths/effects approved.
Reuse matching authority without repeated per-file/section questions; report-only
covers its assigned new report and excludes inputs/indexes/state. Law/ADR acceptance,
evidence publication, runtime qualification and Story/stage completion remain
separate. Preserve before bytes and disclose unavailable checks.

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

### Shared full-audit fixture inputs

Cases 1-3 and 5 use an isolated Game Target whose project-owned root instructions
contain the actual accepted Source/Target boundary text and declare Godot 4.3 +
GDScript, PC/keyboard input and existing review mode `lean`. This fixture
governance is an input assumption, not acceptance of the real Source or any Target.
The selected runtime is Codex. Its complete installed `adopt`, `constitute`,
`brainstorm`, `quick-design`, `map-systems` and `design-system` entries, applicable
owner/reference/policy bodies and actual runtime-definition metadata are readable.
The expanded input list binds the real portable sole Source identity/revision,
installed paths and approved customizations through existing project configuration;
it does not claim autoload, skill execution, Source freshness or project qualification.

Unless a case explicitly removes an input, provide substantive bodies for
`design/INSTRUCTIONS.md`, `rules/design-docs.md`, applicable document templates,
the shared authority/evidence/decision standards, `adapters/README.md` and required
direct/indirect references. Provide these project inputs with their actual roles:

| Input | Required fixture content/role |
|---|---|
| `standards/technical-preferences.md` | Actual Game engine/language/rendering/physics, naming, budgets and routing values; no applicable placeholders. Forbidden Patterns/Allowed Libraries explicitly state none configured, not speculative dependencies. |
| `docs/engine-reference/godot/VERSION.md` | User-confirmed 4.3 pin and substantive applicable compatibility basis; reference presence is not installed-engine proof. |
| `docs/architecture/tr-registry.yaml` | Complete readable registry resolving every TR-ID actually assigned in this fixture; none fabricated for unassigned requirements. |
| `docs/architecture/control-manifest.md` | Substantive rules, actual `Manifest Version:`, relied-on decision links and raw-byte identity metadata. |
| `docs/architecture/architecture-traceability.md` | Actual requirements/decision mappings consistent with the registry and manifest. |
| `production/sprint-status.yaml` | Valid owner-format projection with zero stories in Case 1; actual five Story rows in Case 3. YAML status is declared, not independent closure proof. |
| `production/stage.txt` | Declared `Technical Setup`; qualified transition remains unverified. |

No module index is present, so module-index format checks are N/A with the actual
absence noted; this does not waive required inputs to any selected owner. Story
counts are zero in Cases 1-2. Every supplied module/ADR has substantive applicable
sections and status/acceptance/evidence metadata, except the exact defects stated
by each case. Required manifest identities are computed from retained fixture bytes,
not guessed digest literals. Missing required originals invalidate only their
affected claim; this baseline must be materialized and read before asserting zero gaps.
There is no required live Source comparison or maintenance toolkit for this audit.

All these invocations approve only the displayed `docs/adoption-plan-[date].md`
create effect. The date is fixed by the fixture clock and no plan exists at that
path. Repairs, review-mode setup, state/index updates, acceptance and publication
are excluded; a follow-up recommendation does not execute a repair.

### Case 1: Happy Path — All GDDs compliant, no gaps, COMPLIANT

**Fixture:**
- Use the shared full-audit inputs above with no declared defects.
- `design/cdd/combat.md`, `movement.md` and `stamina.md` are three module CDDs,
  each substantively covering the Game semantic eight and a valid Status field.
- `docs/architecture/adr-0001.md` has all actual applicable sections, including
  Status, Acceptance Record, Engine Compatibility, ADR Dependencies, CDD
  Requirements Addressed and Performance Implications. Its exact fixture choice
  and Accepted scope have verifiable fixture authority; no additional Foundation
  gate/three-ADR qualification is claimed by this one-ADR format audit.

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
8. Shows the concrete plan path/effect and reuses its matching fixture authority;
   the no-prior-authority variant uses `AskUserQuestion`, then user selects write
9. Adoption plan is written to `docs/adoption-plan-[date].md`
10. Phase 7 gives one specific primary next action for this zero-gap format audit
    (for example `/project-stage-detect`), with optional alternatives secondary;
    required bodies/inputs are checked before an actionable recommendation

**Assertions:**
- [ ] After the single initial scanning line, skill reads the complete selected
  artifact/input scope silently before audit findings, counts or recommendations
- [ ] "Scanning project artifacts..." appears before the silent read phase
- [ ] With the complete zero-defect fixture, gap counts show 0 BLOCKING, 0 HIGH,
  0 MEDIUM and 0 LOW; qualification/runtime remain separately unverified
- [ ] Existing named plan authority continues; absent scope uses `AskUserQuestion` before writing
- [ ] Adoption plan file is written to `docs/adoption-plan-[date].md`
- [ ] Phase 7 names one specific primary next action; optional choices remain
  secondary and no next skill is auto-run

---

### Case 2: Non-Compliant Documents — GDDs missing sections, NEEDS MIGRATION

**Fixture:**
- Start from the shared full-audit baseline, replace the three modules with the
  two below, remove only the declared required inputs/sections, and retain other
  complete bodies and identities. The missing ADR Status blocks relied-on scope;
  the existing root governance is not re-ratified by this audit.
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
- Use the shared baseline with four module bodies, three ADRs and five Stories.
  All supplied manifest/required-reference identities are complete; local Story
  details use valid named CDD/no-ADR dispositions where no material ADR is required.
- 4 GDD files: 2 fully compliant, 2 with gaps (one missing Tuning Knobs, one missing Edge Cases)
- ADRs: 3 files — 2 compliant, 1 missing `## ADR Dependencies`
- Stories: 5 substantive files — 3 have registry-resolved assigned TR-IDs,
  2 omit required TR-ID references. All retain status, governing AC, decision
  disposition, manifest identities and history; unexecuted AC remains NotRun.
- Infrastructure: all critical files present; `standards/technical-preferences.md` fully configured

**Input:** `/adopt`

**Expected behavior:**
1. Skill audits all artifact types
2. Audit summary shows format totals: "4 GDDs (2 fully compliant, 2 with gaps);
   3 ADRs (2 fully compliant, 1 with gaps); 5 Stories (3 format-compliant,
   2 with gaps — missing required TR-ID references)". These tallies do not certify
   runtime AC, Story closure or project qualification.
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
- [ ] Per-artifact format tallies are shown for CDDs (2/2), ADRs (2/1) and
  Stories (3/2), with the actual missing roles; tallies do not imply qualification
- [ ] Existing bodies/history preserved; absent required fields do not auto-pass
- [ ] With 0 BLOCKING gaps, migration plan has no BLOCKING action section or
  fake blocking task; the audit summary still reports BLOCKING: 0
- [ ] HIGH gap precedes MEDIUM gaps in plan ordering
- [ ] Missing/new scope is requested before writing; matching named authority continues

---

### Case 4: No Artifacts Found — Fresh project, guidance to run /constitute

**Fixture:**
- Repository has no files in `design/cdd/`, `docs/architecture/`, `production/epics/`
- `production/stage.txt` does not exist
- `src/` directory does not exist or has fewer than 10 files
- Neither substantive Game nor Product concept exists; no module-index.md

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
- Use Case 2 complete baseline and declared defects. The audit completes and
  the named plan-only write is approved; no repair or review-mode write is covered.

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
- [ ] After a completed audit, Phase 7 offers one specific primary next action
  with optional choices secondary; the fresh-project stop remains the Case 4 route
- [ ] Preserves existing bodies/history and repairs only named approved gaps
- [ ] Does not invoke director gates at any point

---

## Coverage Notes

- The `cdds`, `adrs`, `stories`, and `infra` argument modes narrow the audit scope;
  each follows the same pattern as the full audit but limited to that artifact type.
  Not separately fixture-tested here.
- The module-index.md status check follows its actual owner and downstream
  comparison. Valid historical labels or parenthetical notes are not inherently
  BLOCKING. Phase 7 offers immediate help only for the highest-priority actual
  BLOCKING gap; repair still needs its own scoped authority. Not separately tested.
- The review-mode.txt prompt (Phase 6b) runs after plan writing only when review-mode
  setup is in the requested scope and `production/review-mode.txt` is absent.
  A preference selection alone does not authorize its write. Not separately tested.

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
