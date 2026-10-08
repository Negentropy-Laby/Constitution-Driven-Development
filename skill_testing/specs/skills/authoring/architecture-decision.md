# Skill Test Spec: /architecture-decision

## Skill Summary

`/architecture-decision` guides the user through section-by-section authoring of
a new Architecture Decision Record (ADR). Required sections are: Status, Context,
Decision, Consequences, Alternatives, and Related ADRs. The skill also stamps the
engine version reference from `docs/engine-reference/` into the ADR for traceability.

Configured technology specialist validation precedes TD-ADR in full mode. Lean/
solo skip TD-ADR as documented. New ADRs are written Proposed in every mode.
Director recommendations and write approval never accept an ADR; a separate
existing-governance authority must accept exact retained original/revision/scope.
Writes go to `docs/architecture/adr-NNNN-[name].md` within named authorization.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: ACCEPTED, PROPOSED, CONCERNS
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end
- [ ] Documents configured specialist validation followed by TD-ADR in full; lean/solo skip TD-ADR
- [ ] New ADR remains Proposed until a separate evidenced exact-scope acceptance
- [ ] Mentions engine version stamp from `docs/engine-reference/`

---

## Director Gate Checks

Configured specialist validation runs where technology is configured; TD-ADR runs
after it in full mode and is skipped in lean/solo. This skill has no LP-FEASIBILITY
gate. Every new ADR starts Proposed. Approval/skip of gates does not create an
Acceptance Record. Acceptance needs actual authority/time, retained original,
full SHA-256/size, exact scope and separately authorized status effect.

---

## Test Cases

### Case 1: Happy Path — New ADR for rendering approach, full mode, gates approve

**Fixture:**
- `docs/architecture/` exists with no existing ADR for rendering
- `docs/engine-reference/[engine]/VERSION.md` exists
- `production/review-mode.txt` contains `full`

**Input:** `/architecture-decision rendering-approach`

**Expected behavior:**
1. Skill guides user through each required section (Status, Context, Decision, Consequences, Alternatives, Related ADRs)
2. Engine version is stamped into the ADR from `docs/engine-reference/`
3. Draft shown; reuse covered changeset authority, ask "May I write" only for new effects
4. Configured specialist validates the draft, then TD-ADR runs in full mode
5. TD-ADR returns APPROVE; its recommendation is reported separately
6. ADR Status remains Proposed pending separate exact-scope acceptance
7. Skill writes `docs/architecture/adr-NNN-rendering-approach.md`
8. Registry/TR updates run only through their owning workflow with named effect authority

**Assertions:**
- [ ] All 6 required sections are authored and written
- [ ] Engine version reference is stamped in the ADR
- [ ] Configured specialist validation precedes TD-ADR; no invented LP-FEASIBILITY gate
- [ ] ADR remains Proposed despite director approval unless separate exact acceptance is evidenced
- [ ] Existing exact write scope is reused; new effects have concrete draft approval
- [ ] File is written to `docs/architecture/adr-NNN-[name].md`

---

### Case 2: Failure Path — TD-ADR returns CONCERNS

**Fixture:**
- ADR draft is complete (all sections filled)
- `production/review-mode.txt` contains `full`
- TD-ADR gate returns CONCERNS: "The decision does not address [specific concern]"

**Input:** `/architecture-decision [topic]`

**Expected behavior:**
1. TD-ADR gate spawns and returns CONCERNS with specific feedback
2. Skill surfaces the concerns to the user
3. ADR Status remains Proposed (not Accepted)
4. User is asked: revise the decision to address concerns, or accept as Proposed
5. ADR is written with Status: Proposed if concerns are not resolved

**Assertions:**
- [ ] TD-ADR concerns are shown to the user verbatim
- [ ] ADR Status is Proposed (not Accepted) when TD-ADR returns CONCERNS
- [ ] Skill does NOT set Status: Accepted while CONCERNS are unresolved
- [ ] User is given the option to revise and re-run the gate

---

### Case 3: Lean Mode — TD-ADR skipped; ADR written as Proposed

**Fixture:**
- `production/review-mode.txt` contains `lean`
- ADR draft is authored for a new technical decision

**Input:** `/architecture-decision [topic]`

**Expected behavior:**
1. Skill guides user through all 6 sections
2. After configured specialist validation: TD-ADR is skipped
3. Output notes: "TD-ADR skipped — Lean mode"
4. ADR is written Proposed; gate skip/approval cannot accept the decision
5. Existing exact write authority is reused; ask "May I write" only for uncovered effects

**Assertions:**
- [ ] TD-ADR skip note appears; configured specialist behavior is separate
- [ ] ADR Status is Proposed (not Accepted) in lean mode
- [ ] Exact named write scope is reused; uncovered effects get draft/path/effect approval
- [ ] Skill writes the ADR after user approval

---

### Case 4: Edge Case — ADR already exists for this topic

**Fixture:**
- `docs/architecture/` contains an existing ADR covering the same topic
- The existing ADR has Status: Accepted

**Input:** `/architecture-decision [same-topic]`

**Expected behavior:**
1. Skill detects an existing ADR covering the same topic
2. Skill asks: "An ADR for [topic] already exists ([filename]). Update it, or create a new superseding ADR?"
3. User selects update or supersede
4. Skill does NOT silently create a duplicate ADR

**Assertions:**
- [ ] Skill detects the existing ADR before authoring begins
- [ ] User is offered update or supersede options — no silent duplicate
- [ ] If update: skill opens the existing ADR for section-by-section revision
- [ ] If supersede: new ADR references the superseded one in Related ADRs section

---

### Case 5: Acceptance is separate from review/write authority

**Fixture:** Rendering ADR draft, full/lean/solo review outcomes, approved file write
and no acceptance authority for the exact retained revision.

**Expected:** New file is Proposed in all modes; reviews/write approval cannot
produce Accepted or automatically unlock blocked Stories. With separately evidenced
acceptance authority, preserve the reviewed Proposed original and record actual
revision/path/full SHA-256/size, time and exact Accepted scope before an authorized
status transition. Changed Accepted choices require revision/successor history.

**Assertions:**
- [ ] Missing retrofit status does not invent historical Accepted status.
- [ ] TD-ADR recommendation does not accept a decision.
- [ ] Existing Accepted exact scope may be reused; changed bytes/scope may not.
- [ ] No automatic Blocked-to-Ready Story writes.

---

### Case 6: Domain-specific compatibility template preserves both branches

**Fixture:**
Separate Game and Product fixtures supply actual configured versions and
references. Game selects an engine; Product selects Python/runtime/framework and
a CLI/API contract. Variant has conflicting/Unknown domain or unverified version.

**Input:** `/architecture-decision [fixture topic]`

**Expected behavior:**
1. Resolve actual domain/version sources and select the matching template branch.
2. Draft Engine Compatibility for Game or Stack Compatibility for Product.
3. Keep Proposed status and disclose unresolved version/domain facts.

**Assertions:**
- [ ] Game retains its engine-specific fields and examples.
- [ ] Product records actual runtime/framework/library/surface/reference/verification fields without
      Game engine placeholders.
- [ ] Writing or gate approval does not accept the ADR; Unknown/version gaps are not guessed.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] All 6 required sections authored before gate review
- [ ] Engine version stamped in ADR from `docs/engine-reference/`
- [ ] Covered section writes continue under original named authority; only new effects need approval
- [ ] Configured specialist then TD-ADR follow actual full-mode workflow
- [ ] Skipped gates noted by name and mode in lean/solo output
- [ ] Accepted only with separate evidenced authority for exact retained revision/scope
- [ ] Ends with next-step handoff: `/architecture-review` or `/create-control-manifest`

---

## Coverage Notes

- ADR numbering (auto-incrementing NNN) is not independently fixture-tested —
  the skill reads existing ADR filenames to assign the next number.
- Related ADRs section linking (supersedes / related-to) is tested structurally
  via Case 4 but not all link types are individually verified.
- TR registration belongs to its owning workflow and separately authorized effect;
  an ADR file write does not implicitly update that input.

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
