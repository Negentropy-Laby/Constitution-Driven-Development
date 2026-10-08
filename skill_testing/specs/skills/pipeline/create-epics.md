# Skill Test Spec: /create-epics

## Skill Summary

`/create-epics` reads all approved CDDs and translates them into EPIC.md files,
one per system. Epics are organized by layer (Foundation → Core → Feature →
Presentation) and processed in priority order within each layer. Each EPIC.md
includes scope, governing ADRs, CDD requirements, Technology Risk, and a
Definition of Done. It reuses exact named epic/index scope, asking "May I write"
only for uncovered effects.

In `full` review mode, a PR-EPIC gate (producer) runs after drafting epics and
before writing any files. In `lean` or `solo` mode, PR-EPIC is skipped and noted.
Epics are written to `production/epics/[epic-slug]/EPIC.md`.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (`/create-stories`)
- [ ] Documents PR-EPIC gate behavior: runs in full mode; skipped in lean/solo

---

## Director Gate Checks

In `full` mode: PR-EPIC (producer) gate runs after epics are drafted and before
any epic file is written. If PR-EPIC returns CONCERNS, epics are revised before
the "May I write" ask.

In `lean` mode: PR-EPIC is skipped. Output notes: "PR-EPIC skipped — lean mode".

In `solo` mode: PR-EPIC is skipped. Output notes: "PR-EPIC skipped — solo mode".

---

## Test Cases

### Case 1: Happy Path — Two approved CDDs create two EPIC files

**Fixture:**
- `design/cdd/module-index.md` exists with 2 systems listed
- Both systems have approved CDDs in `design/cdd/`
- `docs/architecture/architecture.md` exists with matching modules
- Each requirement has exact Accepted scope or justified cdd-layer/no-adr; separate global Foundation ADR gate remains satisfied
- `production/review-mode.txt` contains `lean`

**Input:** `/create-epics`

**Expected behavior:**
1. Skill reads systems index and both CDDs
2. Drafts 2 EPIC definitions (layer, CDD path, ADRs, requirements, technology risk)
3. PR-EPIC gate is skipped (lean mode) — noted in output
4. Presents each qualified epic; reuses named scope, asking "May I write" only for uncovered effects
5. After approval: writes both EPIC files
6. Creates/updates `production/epics/index.md` only within its named effect scope

**Assertions:**
- [ ] Epic summary is shown before any write ask
- [ ] Named approved epic/index scope persists; only uncovered effects need "May I write"
- [ ] Each EPIC.md contains: layer, CDD path, governing ADRs, requirements table, Definition of Done
- [ ] PR-EPIC skip is noted in output
- [ ] `production/epics/index.md` updates only within its named effect scope
- [ ] Skill does NOT write EPIC files outside named approved scope

---

### Case 2: Failure Path — No approved CDDs found

**Fixture:**
- `design/cdd/module-index.md` exists
- No CDDs in `design/cdd/` have approved status (all are Draft or In Progress)

**Input:** `/create-epics`

**Expected behavior:**
1. Skill reads systems index and attempts to find approved CDDs
2. No approved CDDs found
3. Skill outputs: "No approved CDDs to convert. CDDs must be Approved before creating epics."
4. Skill suggests running `/design-system` and completing CDD approval first
5. Skill exits without creating any EPIC files

**Assertions:**
- [ ] Skill stops cleanly with a clear message when no approved CDDs exist
- [ ] No EPIC files are written
- [ ] Skill recommends the correct next action
- [ ] Verdict is BLOCKED

---

### Case 3: Director Gate — Full mode spawns PR-EPIC before writing

**Fixture:**
- 2 approved CDDs exist
- `production/review-mode.txt` contains `full`

**Full mode expected behavior:**
1. Skill drafts both epics
2. PR-EPIC gate spawns and reviews the epic drafts
3. If PR-EPIC returns APPROVE: report actual review outcome; covered writes proceed,
   uncovered effects get concrete "May I write" approval
4. Epic files are written after approval

**Assertions (full mode):**
- [ ] PR-EPIC gate appears in output as an active gate
- [ ] PR-EPIC runs before any "May I write" ask
- [ ] Epic files are NOT written before PR-EPIC completes

**Fixture (lean mode):**
- Same CDDs
- `production/review-mode.txt` contains `lean`

**Lean mode expected behavior:**
1. Epics are drafted
2. PR-EPIC is skipped — noted in output
3. Covered write authority is reused; only uncovered effects get "May I write" approval

**Assertions (lean mode):**
- [ ] "PR-EPIC skipped — lean mode" appears in output
- [ ] PR-EPIC skip is reported; existing write authority persists and new effects require approval

---

### Case 4: Edge Case — Epic already exists for a CDD

**Fixture:**
- `production/epics/[epic-slug]/EPIC.md` already exists for one of the approved CDDs
- The other CDD has no existing EPIC file

**Input:** `/create-epics`

**Expected behavior:**
1. Skill detects the existing EPIC file for the first system
2. Skill offers to update rather than overwrite: "EPIC-[name].md already exists. Update it, or skip?"
3. For the second system: reuses its exact named create scope or asks for uncovered effects

**Assertions:**
- [ ] Skill detects existing EPIC files before writing
- [ ] User is offered "update" or "skip" options — not auto-overwritten
- [ ] The new system's EPIC is created normally without conflict

---

### Case 5: Director Gate — PR-EPIC returns CONCERNS

**Fixture:**
- 2 approved CDDs exist
- `production/review-mode.txt` contains `full`
- PR-EPIC gate returns CONCERNS (e.g., scope of one epic is too large)

**Input:** `/create-epics`

**Expected behavior:**
1. PR-EPIC gate spawns and returns CONCERNS with specific feedback
2. Skill surfaces the concerns to the user before any write ask
3. User is given options: revise epics, accept concerns and proceed, or stop
4. If user revises: updated epic drafts are shown before the "May I write" ask
5. Skill does NOT write epics while CONCERNS are unaddressed

**Assertions:**
- [ ] CONCERNS from PR-EPIC are shown to the user before writing
- [ ] Skill does NOT auto-write epics when CONCERNS are returned
- [ ] User is given a clear choice to revise, proceed, or stop
- [ ] Revised epic drafts are re-shown after revision before final approval

---

## Protocol Compliance

- [ ] Epic drafts shown to user before any "May I write" ask
- [ ] Named epic/index changeset authority persists; only new effects require approval
- [ ] PR-EPIC gate (if active) runs before write asks — not after
- [ ] Skipped gates noted by name and mode in output
- [ ] EPIC.md content sourced only from CDDs, ADRs, and architecture docs — nothing invented
- [ ] Ends with next-step handoff: `/create-stories [epic-slug]` per created epic

---

## Coverage Notes

- Processing of Core, Feature, and Presentation layers follows the same per-epic
  pattern as Foundation — layer-specific ordering is not independently tested.
- Technology Risk assignment (LOW/MEDIUM/HIGH) from governing ADRs is
  validated implicitly via Case 1's fixture structure.
- The `layer: [name]` and `[system-name]` argument modes follow the same approval
  pattern as the default (all systems) mode.

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

### Case 6: Blocked architecture permits authorized planning only

Missing required manifest/TR/Accepted decision or conflict is reported with its
affected dependencies. An explicitly authorized planning epic can be Draft/Blocked,
never Ready for implementation; independent epics continue. Index rows preserve the
actual state and require their own named effect authority. No invented active IDs.

- [ ] Closing written-N output reports actual Draft/Blocked/Ready-for-planning counts
  and pending actions; operation COMPLETE grants no implementation readiness.

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
