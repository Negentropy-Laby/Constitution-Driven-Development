# Skill Test Spec: /cdd-status

## Skill Summary

`/cdd-status` generates a project progress dashboard from the workflow catalog.
It reads current phase evidence, required-step artifacts, validation gaps, and
project state. With user approval, it writes `production/project-roadmap.md` and,
when `memory_bank/` exists, mirrors the same governance state to
`memory_bank/t2_execution/current_roadmap.md`. It displays recorded adapter
freshness without recomputing or owning that state.

---

## Static Assertions (Structural)

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has at least two phase or numbered workflow headings
- [ ] Contains status keywords such as `COMPLETE`, `PARTIAL`, `MISSING`, or `MANUAL`
- [ ] Contains approval language before writing roadmap files
- [ ] Ends with next-command or blocker guidance

---

## Director Gate Checks

None. `/cdd-status` is a reporting and roadmap mirror workflow. It does not make
phase advancement decisions and does not invoke director gates.

---

## Test Cases

### Case 1: Dry Run

**Fixture:**
- `workflow/workflow-catalog.yaml` exists
- `production/stage.txt` exists

**Input:** `/cdd-status --dry-run`

**Expected behavior:**
1. Reads catalog and project state.
2. Reports current phase, blocker, progress count, and next commands.
3. Writes no files.

**Assertions:**
- [ ] Output includes current phase and current blocker
- [ ] Output includes three recommended next commands when available
- [ ] No roadmap file is written

---

### Case 2: Approved Write With memory_bank

**Fixture:**
- `memory_bank/` exists
- Catalog and phase evidence exist
- User approves writing

**Input:** `/cdd-status --write`

**Expected behavior:**
1. Writes `production/project-roadmap.md`.
2. Writes `memory_bank/t2_execution/current_roadmap.md`.
3. T2 mirror identifies itself as a governance memory mirror.

**Assertions:**
- [ ] Each roadmap/mirror effect is covered by actual named authority; `--write` does not gift unrelated state writes
- [ ] T2 mirror names `/cdd-status` and workflow catalog as sources
- [ ] Output reports both write destinations

---

### Case 3: Approved Write Without memory_bank

**Fixture:**
- `memory_bank/` does not exist
- User approves writing

**Input:** `/cdd-status --write`

**Expected behavior:**
1. Writes only `production/project-roadmap.md`.
2. Does not create `memory_bank/`.
3. Reports optional mirror skipped; initialization is neither performed nor required.

**Assertions:**
- [ ] No `memory_bank/` directory is created
- [ ] Output explains that T2 mirror was skipped
- [ ] Optional absence is disclosed without forcing initialization or blocking independent reporting

---

### Case 4: Product Surface Decisions

**Fixture:**
- Product concept exists
- `design/ux/surface-profile.md` exists

**Input:** `/cdd-status`

**Expected behavior:**
1. Reads product surface profile.
2. Reports interaction-patterns, design-system, and style-guide applicability.
3. Flags missing required product surface evidence.

**Assertions:**
- [ ] Product Surface Decisions table is present
- [ ] Required/N/A/optional status is evidence-backed
- [ ] N/A decisions without surface-profile rationale are flagged as risks

---

### Case 5: Manual Evidence Handling

**Fixture:**
- Current phase has a required step with no machine-checkable artifact

**Input:** `/cdd-status`

**Expected behavior:**
1. Marks the step `MANUAL`, not `COMPLETE`.
2. Describes what evidence must be verified.
3. Keeps gate advancement advisory rather than automatic.

**Assertions:**
- [ ] Manual steps are not silently marked complete
- [ ] Missing evidence appears in risks or current phase checklist
- [ ] No automatic transition; risk acceptance cannot convert required failed/unexecuted checks to PASS

### Case 6: Recorded adapter freshness

**Fixture:**
- `memory_bank/t2_execution/adapter_state.yaml` is fresh, stale, uninitialized, or missing

**Expected behavior:**
1. Displays the recorded status and checked commit/time when available.
2. Adds a `/constitute-check` risk for stale, uninitialized, or missing state.
3. Does not run the adapter checker, write adapter state, or change catalog-derived next commands.

---

## Protocol Compliance

- [ ] Uses approval before writing roadmap files
- [ ] Honors `--dry-run` by writing nothing
- [ ] Does not create `memory_bank/` when missing
- [ ] Recommends next commands without auto-running them
- [ ] Treats adapter freshness as recorded context, not a phase blocker

---

## Coverage Notes

Live verification should include both `--dry-run` and `--write` paths in a test
fixture with and without `memory_bank/`.

### Case 7: Locator/recorded facts are not qualified completion

**Fixture:** Globs/min_count/patterns met; YAML/user says done; required check
NotRun, and adapter_state records fresh at an old exact baseline. Both concepts
conflict. Variant has no concept but actual configured Product or legacy Game.
- [ ] Preserve declared facts, read observed bodies and report candidate separately;
  required qualified completion remains incomplete, with actual denominator.
- [ ] Recorded adapter freshness is historical context, not live runtime/spec/
  category qualification. Neutral supports need their own exact identity.
- [ ] Conflict blocks affected domain branch; configured Product never defaults Game,
  and legacy Game needs actual evidence. Independent neutral report continues.

### Case 8: Dry run, report-only and named mirror authority

**Fixture:** A authorizes only new roadmap, B names roadmap and existing T2 mirror;
C selects `--dry-run`, with optional Memory Bank absent in variant.
- [ ] A writes only roadmap; B reuses both exact effects across retries.
- [ ] C writes nothing; absent memory creates no memory/testing tree.
- [ ] No laws/current-state/workflow-contract/adapter-state/index/session/sprint/stage
  writes. Full draft/path-effect disclosure precedes only missing/new authority.

### Concrete domain scope, optional governance and legacy aliases

**Fixture:** Substantive Game/Product concepts conflict or explicitly mixed scope
has no concrete Game or Product selection. Variant has no concept but populated
legacy Product language/framework, deployment and routing sections; Product Stack
is absent. Optional Memory Bank is absent in both variants.
- [ ] Unresolved variants keep dependent catalog applicability pending, do not
  select Both or qualify phase completion; neutral roadmap reporting continues.
- [ ] Valid legacy Product aliases route the actual Product scope without moving/
  overwriting sections; placeholders/conflicting new values do not qualify routing.
- [ ] Governance setup advice may suggest `/constitute` when requested, but neither
  it nor default QA/neutral reports initialize Memory Bank or require optional
  setup. Covered roadmap writes remain separate from mirror/state effects.

### Referenced ignored attachment is present, then genuinely absent

For paired Game/Product fixtures, an owning CDD or required evidence references
an ignored `production/qa/inputs/assumptions.txt` with substantive body content.
Its existence is stable across the dry-run and continuing read-only turn. A
separate fixture removes only that attachment while preserving its references.
- [ ] Directly read the existing attachment and bind its actual path/full hash/
  bytes; discovery omissions never produce a missing-attachment finding.
- [ ] The absent variant uses a direct path-specific result and reports only
  affected required evidence missing/incomplete; it cannot qualify COMPLETE.
- [ ] Unread/inaccessible is Pending/unverified, distinct from confirmed absence.
- [ ] Retain each original fixture and actual observations; no write entrypoint
  or repair of the fixture is part of this read-only acceptance.
