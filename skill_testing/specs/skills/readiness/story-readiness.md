# Skill Test Spec: /story-readiness

## Skill Summary

`/story-readiness` validates that a story file is ready for a developer to
pick up and implement. It checks four dimensions: Design (embedded CDD
requirements), Architecture (ADR references and status), Scope (clear
boundaries and DoD), and Definition of Done (testable criteria). It produces
a READY / NEEDS WORK / BLOCKED verdict. It is a read-only skill and runs
before any developer picks up a story.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings or numbered check sections
- [ ] Contains verdict keywords: READY, NEEDS WORK, BLOCKED
- [ ] Does NOT require "May I write" language (read-only skill)
- [ ] Has a next-step handoff (what to do after verdict)

---

## Test Cases

### Case 1: Happy Path — Fully ready story

**Fixture:**
- Story file exists at `production/epics/core/story-light-pickup.md`
- Story contains:
  - `TR-ID: TR-light-001` (CDD requirement reference)
  - `ADR: docs/architecture/adr-003-inventory.md`
  - Referenced ADR exists and has status `Accepted`
  - Referenced TR-ID exists in `docs/architecture/tr-registry.yaml`
  - Story has `## Acceptance Criteria` with ≥3 testable items
  - Story has `## Definition of Done` section
  - Story has `Status: Ready for Dev`
  - Full Manifest SHA-256/Bytes/path from raw bytes match current `docs/architecture/control-manifest.md`

**Input:** `/story-readiness production/epics/core/story-light-pickup.md`

**Expected behavior:**
1. Skill reads the story file
2. Skill reads the referenced ADR — verifies status is `Accepted`
3. Skill reads `docs/architecture/tr-registry.yaml` — verifies TR-ID exists
4. Skill reads `docs/architecture/control-manifest.md` — compares complete manifest raw-byte SHA-256/size/path, retaining date separately
5. Skill evaluates all 4 dimensions (Design, Architecture, Scope, DoD)
6. Skill outputs READY verdict with all checks passing

**Assertions:**
- [ ] Skill reads the referenced ADR file (not just the story)
- [ ] Skill verifies ADR status is `Accepted` (not `Proposed`)
- [ ] Skill reads `tr-registry.yaml` to verify TR-ID exists
- [ ] Output includes check results for all 4 dimensions
- [ ] Verdict is READY when all checks pass
- [ ] Skill does not write any files

---

### Case 2: Blocked Path — Referenced ADR is Proposed (not Accepted)

**Fixture:**
- Story file exists with `ADR: docs/architecture/adr-005-light-system.md`
- `adr-005-light-system.md` exists but has `Status: Proposed`
- All other story content is otherwise complete

**Input:** `/story-readiness production/epics/core/story-light-system.md`

**Expected behavior:**
1. Skill reads the story
2. Skill reads `adr-005-light-system.md` — finds `Status: Proposed`
3. Skill flags this as a BLOCKING issue (cannot implement against unaccepted ADR)
4. Skill outputs BLOCKED verdict
5. Skill recommends: accept or reject the ADR before picking up the story

**Assertions:**
- [ ] Verdict is BLOCKED (not NEEDS WORK or READY) when ADR is Proposed
- [ ] Output explicitly names the Proposed ADR as the blocker
- [ ] Output recommends resolving ADR status before proceeding
- [ ] Skill does not output READY regardless of other checks passing

---

### Case 3: Needs Work — Missing Acceptance Criteria

**Fixture:**
- Story file exists but has no `## Acceptance Criteria` section
- ADR reference exists and is `Accepted`
- TR-ID exists in registry
- Complete raw-byte manifest identity matches

**Input:** `/story-readiness production/epics/core/story-oxygen-drain.md`

**Expected behavior:**
1. Skill reads the story
2. Skill finds no Acceptance Criteria section
3. Skill flags this as a NEEDS WORK issue (story is incomplete, not blocked)
4. Skill outputs NEEDS WORK verdict
5. Skill names the missing section and suggests adding measurable criteria

**Assertions:**
- [ ] Verdict is NEEDS WORK (not BLOCKED or READY) when Acceptance Criteria section is absent
- [ ] Output identifies the missing Acceptance Criteria section specifically
- [ ] Output suggests adding testable/measurable criteria
- [ ] Skill distinguishes NEEDS WORK (fixable without external dependencies) from BLOCKED (requires outside action)

---

### Case 4: Edge Case — Stale manifest version

**Fixture:**
- Story file has `Manifest Version: 2026-01-15` in its header
- `docs/architecture/control-manifest.md` has `Manifest Version: 2026-03-10`
- Versions do not match (story was created before manifest was updated)

**Input:** `/story-readiness production/epics/core/story-mirror-rotation.md`

**Expected behavior:**
1. Skill reads Story/complete current manifest bytes and detects legacy date-only identity
2. LegacyRecheck reports that historical identity cannot be proved from dates
3. Current rules/decision/dependencies are inspected; no old digest invented
4. Verdict is NEEDS WORK pending authorized Story identity repair; required missing
   inputs/material decision blockers remain BLOCKED
5. No writes occur, including no in-memory write entrypoint

**Assertions:**
- [ ] Skill reads `docs/architecture/control-manifest.md` to get current version
- [ ] Skill compares complete raw-byte SHA-256/size/path; date-only records require LegacyRecheck
- [ ] This legacy-only fixture is NEEDS WORK; required missing input/material blockers still make affected scope BLOCKED
- [ ] Output explains that the story's embedded guidance may be outdated

---

---

### Case 5: Director Gate — QL-STORY-READY behavior across review modes

**Fixture:**
- Story file exists and is READY (all 4 dimensions pass, ADR Accepted, criteria present)
- `production/review-mode.txt` exists

**Case 5a — full mode:**
- `review-mode.txt` contains `full`

**Input:** `/story-readiness production/epics/core/story-light-pickup.md` (full mode)

**Expected behavior:**
1. Skill reads review mode — determines `full`
2. After completing its own 4-dimension check, skill invokes QL-STORY-READY gate
3. QA lead reviews the story for readiness
4. If QA verdict is GAPS/INADEQUATE, report actual gaps and the current workflow's
   user-choice interface; required decision/input/dependency blockers stay BLOCKED
5. If QA lead verdict is ADEQUATE → verdict proceeds normally

**Assertions (5a):**
- [ ] Skill reads review mode before deciding whether to invoke QL-STORY-READY
- [ ] QL-STORY-READY gate is invoked in full mode after the 4-dimension check completes
- [ ] QA feedback is reported; required decision/input blockers remain regardless of QA ADEQUATE or user preference
- [ ] Gate invocation is noted in output: "Gate: QL-STORY-READY — [result]"

**Case 5b — lean or solo mode:**
- `review-mode.txt` contains `lean` or `solo`

**Expected behavior:**
1. Skill reads review mode — determines `lean` or `solo`
2. QL-STORY-READY gate is SKIPPED
3. Output notes the skip: "[QL-STORY-READY] skipped — Lean/Solo mode"
4. Verdict is based on 4-dimension check only

**Assertions (5b):**
- [ ] QL-STORY-READY gate does NOT spawn in lean or solo mode
- [ ] Skip is explicitly noted in output
- [ ] Verdict is based on 4-dimension check alone

---

## Protocol Compliance

- [ ] Does NOT use Write or Edit tools (read-only skill)
- [ ] Presents complete check results before verdict
- [ ] Does not ask for approval (no file writes)
- [ ] Ends with recommended next step (fix issues or proceed to implementation)
- [ ] Distinguishes three verdict levels clearly (READY vs NEEDS WORK vs BLOCKED)

---

## Coverage Notes

- Case where TR-ID is missing from the registry entirely is not explicitly
  tested here; it follows the same NEEDS WORK pattern as Case 3.
- The "no argument" path (skill auto-detecting the current story) is not
  tested because it depends on `production/session-state/active.md` content,
  which is hard to fixture reliably.
- Stories with multiple ADR references are not tested; behavior is assumed to
  be additive (all ADRs must be Accepted for READY verdict).

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

### Case 6: Missing prerequisite is not automatic success

Missing required TR registry/manifest or absent digest never auto-passes. No ADR
link with local reason requires classification and evidence, not blanket N/A.
Exact Accepted scope or valid cdd-layer/no-adr passes only the ADR-specific check;
missing criteria, active TR, dependency, evidence or manifest remains unmet.
Readiness never writes Stories/statuses/indexes/state, even with a repair offer.

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
