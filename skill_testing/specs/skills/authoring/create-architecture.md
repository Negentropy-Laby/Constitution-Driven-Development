# Skill Test Spec: /create-architecture

## Skill Summary

`/create-architecture` guides the user through section-by-section authoring of a
technical architecture document. It uses a skeleton-first approach — the file is
created with all required section headers before any content is filled. Each
section is discussed, drafted, and written incrementally within its approved scope;
only unresolved material choices or new effects need further approval. If an
architecture document already exists, the skill offers retrofit mode to update
specific sections.

In `full` review mode, TD-ARCHITECTURE (technical-director) and LP-FEASIBILITY
(lead-programmer) review after writing: TD-ARCHITECTURE is a self-review in all
modes; full additionally spawns LP-FEASIBILITY. Lean/solo skip LP-FEASIBILITY. The skill writes to `docs/architecture/architecture.md`.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: APPROVED, NEEDS REVISION, MAJOR REVISION NEEDED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (`/architecture-review` or `/create-control-manifest`)
- [ ] Documents skeleton-first approach
- [ ] TD-ARCHITECTURE self-review always; full LP-FEASIBILITY; lean/solo skip only LP
- [ ] Documents retrofit mode for existing architecture documents

---

## Director Gate Checks

In full mode: TD-ARCHITECTURE self-review follows written document; then
LP-FEASIBILITY is spawned. Sign-off effect requires named write authority.

In lean mode: TD self-review remains; note "LP-FEASIBILITY skipped — Lean mode".

In solo mode: TD self-review remains; note LP-FEASIBILITY skipped.

---

## Test Cases

### Case 1: Happy Path — New architecture doc, skeleton-first, full mode gates approve

**Fixture:**
- No existing `docs/architecture/architecture.md`
- `docs/architecture/` contains Accepted ADRs for reference
- `production/review-mode.txt` contains `full`

**Input:** `/create-architecture`

**Expected behavior:**
1. Skill creates skeleton `docs/architecture/architecture.md` with all required section headers
2. For each section: drafts and shows content, reuses exact write scope; asks only for new effects
3. After all sections are drafted: TD self-review then full-mode LP-FEASIBILITY run
4. TD self-review returns actual APPROVE; LP returns actual FEASIBLE
5. Report document-write outcome, actual assessments and unresolved decisions separately;
   content/write approval alone cannot mark architecture or implementation qualified
6. Session state updated only within its separately named effect scope

**Assertions:**
- [ ] Skeleton file is created with all section headers before any content is written
- [ ] Covered section writes reuse named authority; new effects have a concrete approval draft
- [ ] TD self-review runs first; full-mode LP-FEASIBILITY follows sequentially
- [ ] Actual TD/LP assessments are reported before any authorized sign-off effect
- [ ] Actual APPROVE and FEASIBLE are not renamed APPROVED or treated as ADR acceptance
- [ ] Next-step handoff to `/architecture-review` or `/create-control-manifest` is present

---

### Case 2: Failure Path — TD-ARCHITECTURE self-review returns REJECT

**Fixture:**
- Architecture doc is fully drafted (all sections)
- `production/review-mode.txt` contains `full`
- TD-ARCHITECTURE self-review returns REJECT: "[specific structural issue]"

**Input:** `/create-architecture`

**Expected behavior:**
1. All sections are drafted and written
2. TD-ARCHITECTURE self-review runs and returns REJECT with specific feedback
3. Skill surfaces the feedback to the user
4. Architecture is NOT marked as finalized
5. User is asked: revise the flagged sections, or accept the document as a draft

**Assertions:**
- [ ] Architecture is NOT marked qualified when TD-ARCHITECTURE returns REJECT
- [ ] Gate feedback is shown to the user with specific issue descriptions
- [ ] User is given the option to revise specific sections
- [ ] Skill does NOT auto-finalize or allow affected implementation despite unresolved REJECT blockers

---

### Case 3: Lean Mode — TD self-review remains; LP-FEASIBILITY skipped

**Fixture:**
- No existing architecture doc
- `production/review-mode.txt` contains `lean`

**Input:** `/create-architecture`

**Expected behavior:**
1. Skeleton file is created
2. Sections are drafted incrementally within original exact authority; new effects alone need approval
3. After completion: TD self-review runs and LP-FEASIBILITY is skipped
4. Output notes: "LP-FEASIBILITY skipped — Lean mode"
5. Report TD self-review and LP skip accurately; document writing/user approval alone
   does not qualify unresolved decisions, required evidence or implementation readiness

**Assertions:**
- [ ] LP-FEASIBILITY skip note appear in output
- [ ] TD self-review remains in lean; no claim that both gates completed
- [ ] LP skip alone is not a blocker; unresolved required decisions/evidence still block affected scope
- [ ] Next-step handoff is still present

---

### Case 4: Retrofit Mode — Existing architecture doc, user updates a section

**Fixture:**
- `docs/architecture/architecture.md` already exists with all sections populated

**Input:** `/create-architecture`

**Expected behavior:**
1. Skill detects existing architecture doc and reads its current content
2. Skill offers retrofit mode: "Architecture doc already exists. Which section would you like to update?"
3. User selects a section
4. Skill authors only that section within covered scope; asks "May I write [section]?" only for new effects
5. Only the selected section is updated — other sections unchanged

**Assertions:**
- [ ] Skill detects and reads the existing architecture doc before offering retrofit
- [ ] User is asked which section to update — not asked to rewrite the whole document
- [ ] Only the selected section is updated
- [ ] Other sections are not modified during a retrofit session

---

### Case 5: Director Gate — Architecture references a Proposed ADR; flagged as risk

**Fixture:**
- Architecture doc is being authored
- One section references or depends on an ADR that has `Status: Proposed`
- `production/review-mode.txt` contains `full`

**Input:** `/create-architecture`

**Expected behavior:**
1. Skill authors all sections
2. During authoring, skill detects a reference to a Proposed ADR
3. Skill flags: "Note: [section] references ADR-NNN which is Proposed — this blocks affected implementation until exact acceptance/valid scoped exception"
4. Risk flag is embedded in the relevant section's content
5. TD-ARCHITECTURE and LP-FEASIBILITY still run — they are informed of the Proposed ADR risk

**Assertions:**
- [ ] Proposed ADR reference is detected and flagged during section authoring
- [ ] Risk note is embedded in the architecture document section
- [ ] TD self-review runs and full-mode LP spawns; their review does not accept the Proposed decision
- [ ] Risk flag names the specific ADR number and title

---

## Protocol Compliance

- [ ] Skeleton file created with all section headers before any content is written
- [ ] Covered section writes reuse named authority; new effects have a concrete approval draft
- [ ] TD self-review then full-mode LP-FEASIBILITY run in full mode
- [ ] Skipped gates noted by name and mode in lean/solo output
- [ ] Proposed ADR references flagged as risks in the document
- [ ] Ends with next-step handoff: `/architecture-review` or `/create-control-manifest`

---

## Coverage Notes

- The required section list for architecture documents is defined in the skill
  body and in the `/architecture-review` skill — not re-enumerated here.
- Engine version stamping in the architecture doc (parallel to ADR stamping)
  is part of the authoring workflow — tested implicitly via Case 1.
- The retrofit mode for updating multiple sections in one session follows the
  same continuing exact-scope pattern; material new effects require approval —
  not independently tested for multi-section retrofits.

## Exact scope and decision counterexamples

These are required semantic cases, not claims that keyword/static checks ran them.
Fixtures use actual UTF-8 bytes/complete dependencies and preserve Game/Product
owner requirements under `design/INSTRUCTIONS.md`.

- CDD-owned detail and local helper: classify cdd-layer/no-adr with named owner/
  reason; do not manufacture an ADR or waive CDD/TR/manifest/evidence prerequisites.
- Significant new trust/public-contract/durable-format/state-ownership choice:
  adr-required before affected implementation; independent scoped work may continue.
- Exact Accepted section conflicts with actual choice: conflict, named affected
  dependencies/action/owner; green tests or implemented status cannot establish covered.
- Content agreement, report/write permission or director APPROVED: no automatic
  ADR acceptance, Story readiness/completion or phase advancement.
- Historical approval with changed raw bytes/scope: retain history, do not reuse it
  as current approval. Preserve originals, full hashes/sizes/paths and UTC collection.
- Report-only saves only its new report; inputs/index/session/log/T3 effects require
  separate named scope. Review-only invokes no write entrypoint, including in memory.
- Unknown/both/neither domain: common checks continue, domain-specific findings
  remain incomplete until resolved; no silent Game fallback.
- Separate global Technical Setup min-three Foundation ADR rule remains in force;
  local no-ADR classifications neither waive it nor justify fabricated ADRs.

### Assessment run-state counterexample

In lean/solo, TD self-review still runs; Phase 7b reports LP Skipped with mode before
handoff and records N/A LP verdict. In full, unavailable LP is NotRun/Blocked with
actual reason, never FEASIBLE. Actual required review/decision/evidence blockers
remain unresolved regardless of document-write approval. Status effects need scope.

### Review-mode input counterexamples

Verify the actual once-per-run resolver before any gate dispatch:

| Fixture | Expected actual result |
|---|---|
| No override and no `production/review-mode.txt` | Resolve lean once; report actual documented gate skips |
| Valid explicit full/lean/solo plus a different global value | Explicit override wins and stays fixed for this run |
| No override, present global full/lean/solo | Use the actual validated global value |
| `--review` missing its value, or invalid explicit value | Report input error and require correction; no fallback/gate verdict |
| No override, present invalid or empty global file | Report its actual path/value error and require correction; never default lean/full |

These are semantic cases to execute or independently review, not claims of test
execution from keyword presence. Invalid mode cannot fabricate gate completion or
ADR/Story/phase acceptance; independent read-only findings may be reported with limits.
