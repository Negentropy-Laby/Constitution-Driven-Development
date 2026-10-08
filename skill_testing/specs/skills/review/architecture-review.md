# Skill Test Spec: /architecture-review

## Skill Summary

`/architecture-review` is an Opus-tier skill that validates a technical architecture
document against its actual architecture/CDD owner requirements and checks that it
is internally consistent, non-contradictory with existing ADRs, and correctly
targeting pinned Game/Product technology. It reads substantive CDD/decision owner
bodies and exact evidence, and produces PASS / CONCERNS / FAIL.

Technology specialist consultation follows the compatibility audit when configured;
there is no invented TD-ARCHITECTURE/LP-FEASIBILITY gate in this skill. Review-only
never writes. A separately authorized report may be saved; registry/index/log/
session/T3 effects remain separate. Existing focus, engine/rtm and path calls work.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: PASS, CONCERNS, FAIL
- [ ] Review-only writes nothing; new report effects require named authority/"May I write"
- [ ] Has a next-step handoff at the end
- [ ] Documents actual technology specialist consultation; no invented director gates

---

## Director Gate Checks

Technology consultation uses configured specialists after the actual audit.
No director review-mode gate is introduced. Record actual consultation completion/
absence, scope and limits; unavailable required checks are incomplete, not PASS.

---

## Test Cases

### Case 1: Happy Path — Complete architecture doc in full mode

**Fixture:**
- `docs/architecture/architecture.md` has substantive owner requirements, mapped CDD/TR
  dispositions, exact accepted sources/justified CDD-local choices and required evidence
- All sections reference the correct engine version from `docs/engine-reference/`
- No contradictions with existing Accepted ADRs in `docs/architecture/`
- `production/review-mode.txt` contains `full`

**Input:** `/architecture-review docs/architecture/architecture.md`

**Expected behavior:**
1. Skill reads the architecture document
2. Skill reads existing ADRs for cross-reference
3. Skill reads engine version reference
4. Configured technology specialist consultation reviews actual compatibility findings
5. Actual evidence supports the findings; no invented director gate approval
6. Skill outputs actual requirement/disposition traceability, conflicts, technology
   findings and architecture coverage against CDD layers/data flow/API boundaries
7. Verdict: PASS

**Assertions:**
- [ ] Actual architecture/CDD owners and substantive bodies are checked, not fixed eight headings
- [ ] Actual configured specialist consultation is reported
- [ ] PASS requires justified current dispositions and complete required evidence, no unresolved required conflict/decision
- [ ] Review-only writes no files; report-only saves only its new report
- [ ] Next-step handoff to `/create-control-manifest` or `/create-epics` is present

---

### Case 2: Failure Path — Missing required architecture/CDD evidence

**Fixture:**
- `docs/architecture/architecture.md` exists but omits required data model/error
  handling ownership for affected CDD requirements; material decisions/evidence remain unresolved
- `production/review-mode.txt` contains `full`

**Input:** `/architecture-review docs/architecture/architecture.md`

**Expected behavior:**
1. Skill reads actual architecture/CDD bodies and identifies unresolved required owners
2. Disposition/evidence matrix shows missing inputs and affected dependencies
3. Required repairs are named with actual owner/action and specific remediation
4. Verdict: FAIL because required decisions/evidence remain incomplete, not a section count

**Assertions:**
- [ ] Verdict is FAIL for the fixture's incomplete required architecture/decision evidence
- [ ] Each missing required owner/input is named explicitly with affected scope
- [ ] Remediation guidance is specific (what to add, not just "add missing sections")
- [ ] Skill does NOT pass a document missing required sections

---

### Case 3: Partial Path — Architecture contradicts an existing ADR

**Fixture:**
- `docs/architecture/architecture.md` has substantive required architecture owners
- One Accepted ADR in `docs/architecture/` establishes a constraint that the architecture doc contradicts
  (e.g., ADR-001 mandates ECS pattern; architecture.md describes a different pattern for the same system)

**Input:** `/architecture-review docs/architecture/architecture.md`

**Expected behavior:**
1. Skill reads the architecture doc and all existing ADRs
2. Conflict is detected between the architecture doc and the named ADR
3. Conflict entry names: the ADR number/title, the contradicting sections, and impact
4. Verdict: FAIL (conflict exists but structure is otherwise sound)

**Assertions:**
- [ ] Verdict is FAIL for an unresolved conflict with exact governing Accepted scope
- [ ] The specific ADR number and title are named in the conflict entry
- [ ] The contradicting sections in both documents are identified
- [ ] Skill does NOT auto-resolve the contradiction

---

### Case 4: Edge Case — File not found

**Fixture:**
- The path provided does not exist in the project

**Input:** `/architecture-review docs/architecture/nonexistent.md`

**Expected behavior:**
1. Skill attempts to read the file
2. File not found
3. Skill outputs a clear error naming the missing file
4. Skill suggests checking `docs/architecture/` or running `/create-architecture`
5. Skill does NOT produce a verdict

**Assertions:**
- [ ] Skill outputs a clear error when the file is not found
- [ ] No verdict for the missing target is produced (PASS / CONCERNS / FAIL);
  independently completed checks may be reported with limits
- [ ] Skill suggests a corrective action
- [ ] Skill reports missing input clearly and may report completed independent checks with limits

---

### Case 5: Exact dispositions, evidence and report scope

**Fixture:** Game hitbox and combo requirements; Accepted ADR covers exact hitbox
choice, combo timing is a CDD-owned detailed rule, persistent storage choice changes
without Accepted scope, and a test file exists with no execution evidence.

**Expected:** covered/cdd-layer/adr-required classified distinctly; no ADR generated
for combo timing. Changed significant storage choice blocks affected implementation.
Test path is LINKED / NOT RUN, never PASS. Report-only approval saves only its new
report and does not update TR registry, indexes, consistency log, session or T3.

**Assertions:**
- [ ] All six dispositions have current named owners/reasons/evidence.
- [ ] No missing-link shortcut or automatic no-ADR gap.
- [ ] No test PASS from file existence.
- [ ] Actual old engine/rtm/path invocations retain their legal routing.

---

## Protocol Compliance

- [ ] Review-only invokes no write entrypoint; report-only never extends to inputs/indexes/state
- [ ] Presents actual traceability/disposition/evidence and architecture coverage before verdict
- [ ] No invented TD-ARCHITECTURE/LP-FEASIBILITY gate; actual configured specialist is reported
- [ ] Actual consultation absence/unavailability and incomplete checks are reported
- [ ] Verdict is one of exactly: PASS, CONCERNS, FAIL
- [ ] Ends with next-step handoff appropriate to verdict

---

## Coverage Notes

- Actual architecture owner requirements come from create-architecture and this
  skill's Phase 6 CDD coverage checks; no universal eight-section architecture schema.
  Module CDD semantic eight and other DocKinds follow `design/INSTRUCTIONS.md`.
- Engine version compatibility checking (cross-referencing `docs/engine-reference/`)
  is part of Case 1's happy path but not independently fixture-tested.
- RTM (requirement traceability matrix) mode is a separate concern covered by
  the `/architecture-review` skill's own `rtm` argument mode, not tested here.

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
- Content agreement, report/write permission or director PASS: no automatic
  ADR acceptance, Story readiness/completion or phase advancement.
- Historical approval with changed raw bytes/scope: retain history, do not reuse it
  as current approval. Preserve originals, full hashes/sizes/paths and UTC collection.
- Report-only saves only its new report; inputs/index/session/log/T3 effects require
  separate named scope. Review-only invokes no write entrypoint, including in memory.
- Unknown/both/neither domain: common checks continue, domain-specific findings
  remain incomplete until resolved; no silent Game fallback.
- Separate global Technical Setup min-three Foundation ADR rule remains in force;
  local no-ADR classifications neither waive it nor justify fabricated ADRs.
