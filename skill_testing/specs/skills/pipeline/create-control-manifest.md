# Skill Test Spec: /create-control-manifest

## Skill Summary

`/create-control-manifest` reads all Accepted ADRs from `docs/architecture/` and
generates a control manifest — a summary document that captures all architectural
constraints, required patterns, and forbidden patterns in one place. The manifest
is the reference document that story authors use when writing story files, ensuring
stories inherit the correct architectural rules without having to read all ADRs
individually.

The skill only includes Accepted ADRs; Proposed ADRs are excluded and noted. It
uses TD-MANIFEST in full mode and skips it in lean/solo. The skill asks "May I write"
for new effects, reusing covered authority before writing
`docs/architecture/control-manifest.md`.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end (`/create-epics` or `/create-stories`)
- [ ] Documents that only Accepted ADRs are included (not Proposed)

---

## Director Gate Checks

TD-MANIFEST runs in full mode after the rules preview and before writing. Lean/
solo skip it explicitly. Director approval is neither write authority nor ADR
acceptance. Rules bind actual Accepted sources; Proposed exclusions cannot conceal
unresolved required decisions/conflicts.

---

## Test Cases

### Case 1: Happy Path — 4 Accepted ADRs create a correct manifest

**Fixture:**
- `docs/architecture/` contains 4 ADR files, all with `Status: Accepted`
- Each ADR has a "Required Patterns" and/or "Forbidden Patterns" section
- No existing `docs/architecture/control-manifest.md`
- Required architecture/Accepted-decision/dependency closure and the separate global
  Foundation ADR gate are verified; no prior manifest write authority

**Input:** `/create-control-manifest`

**Expected behavior:**
1. Skill reads all ADR files in `docs/architecture/`
2. Extracts Required Patterns, Forbidden Patterns, and key constraints from each
3. Drafts the manifest with correct section structure
4. Shows the draft manifest to the user
5. Only for uncovered manifest effects asks "May I write `docs/architecture/control-manifest.md`?"
6. Writes the manifest after approval

**Assertions:**
- [ ] All 4 Accepted ADRs are represented in the manifest
- [ ] Manifest includes distinct sections for Required Patterns and Forbidden Patterns
- [ ] Manifest includes the source ADR number for each constraint
- [ ] Existing exact manifest authority is reused; this fixture's uncovered write asks "May I write"
- [ ] Skill does NOT write without approval
- [ ] Active/COMPLETE qualification requires actual required checks; saved/readback operation is reported separately

---

### Case 2: Failure Path — No ADRs found

**Fixture:**
- `docs/architecture/` directory exists but contains no ADR files

**Input:** `/create-control-manifest`

**Expected behavior:**
1. Skill reads `docs/architecture/` and finds no ADR files
2. Skill reports the unsatisfied global Foundation ADR gate and affected required
   governing inputs, recommending `/architecture-decision` through its owning workflow
3. Skill exits without creating any file
4. Verdict is BLOCKED

**Assertions:**
- [ ] Skill outputs a clear error when no ADRs are found
- [ ] No control manifest file is written
- [ ] Skill recommends `/architecture-decision` as the next action
- [ ] Verdict is BLOCKED (not an error crash)

---

### Case 3: Mixed ADR Statuses — Only Accepted ADRs included

**Fixture:**
- `docs/architecture/` contains 3 Accepted ADRs and 2 Proposed ADRs
- Verify whether the Proposed decisions are required for affected rules; exclusion
  is not proof that the required architecture/dependency/global gate is satisfied

**Input:** `/create-control-manifest`

**Expected behavior:**
1. Skill reads all ADR files and filters by Status: Accepted
2. Manifest is drafted from the 3 Accepted ADRs only
3. Output notes: "2 Proposed ADRs were excluded: [adr-NNN-name, adr-NNN-name]"
4. User sees which ADRs were excluded before approving the write
5. Only for uncovered manifest effects asks "May I write `docs/architecture/control-manifest.md`?"

**Assertions:**
- [ ] Only the 3 Accepted ADRs appear in the manifest content
- [ ] Excluded Proposed ADRs are listed by name in the output
- [ ] User sees the exclusion list before approving the write
- [ ] Skill does NOT silently omit Proposed ADRs without noting them

---

### Case 4: Edge Case — Manifest already exists

**Fixture:**
- `docs/architecture/control-manifest.md` already exists (version 1, dated last week)
- `docs/architecture/` contains Accepted ADRs (some new since last manifest)

**Input:** `/create-control-manifest`

**Expected behavior:**
1. Skill detects existing manifest and reads its version number / date
2. Skill offers to regenerate: "control-manifest.md already exists (v1, [date]). Regenerate with current ADRs?"
3. If user confirms: skill drafts updated manifest, retains readable date and reports complete raw-byte SHA-256/size outside the manifest
4. Reuses exact overwrite authority; otherwise asks "May I write `docs/architecture/control-manifest.md`?"
5. Writes updated manifest after approval

**Assertions:**
- [ ] Skill reads and reports the existing manifest version before offering to regenerate
- [ ] User is offered a regenerate/skip choice — not auto-overwritten
- [ ] Updated manifest has exact raw-byte identity reported outside itself; dates remain readable
- [ ] Covered overwrite authority is reused; uncovered overwrite has concrete draft approval

---

### Case 5: TD-MANIFEST and exact content identity

**Fixture:** Accepted source rules; production/review-mode.txt selects full or lean;
existing manifest and Story both have the same readable date.

**Expected:** Full invokes TD-MANIFEST before write; lean skips it. After authorized
write, read complete saved raw bytes and report full SHA-256/size/path/time in
consumer metadata, outside the manifest itself. A one-byte/same-date rule change
invalidates the Story identity; date-only Story is LegacyRecheck, not PASS.

**Assertions:**
- [ ] Complete digest uses all raw bytes including line endings.
- [ ] No self-referential manifest hash; no invented historical digest.
- [ ] Unavailable raw bytes/hash means incomplete check, never date fallback.
- [ ] No automatic Story/status/session/index update from manifest write.

---

## Protocol Compliance

- [ ] Reads all ADR files before drafting manifest
- [ ] Only Accepted ADRs included — Proposed ones noted as excluded
- [ ] Manifest draft shown to user before "May I write" ask
- [ ] Exact named create/overwrite authority persists; "May I write" is asked only for new effects
- [ ] Full TD-MANIFEST / lean-solo skip follows actual workflow
- [ ] Ends with next-step handoff: `/create-epics` or `/create-stories`

---

## Coverage Notes

- The exact section structure of the generated manifest (constraint tables, pattern
  lists) is defined by the skill body and not re-enumerated in test assertions.
- Case 4 retains legacy readable date fields; SHA-256/byte size of complete raw
  bytes is the actual identity, stored outside the manifest.
- ADR parsing (extracting Required/Forbidden Patterns) depends on consistent ADR
  structure — tested implicitly via Case 1's fixture.

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

### Case 7: Gate owner is the inline skill contract

TD-MANIFEST criteria and APPROVE/CONCERNS/REJECT outcomes belong to Phase 4b of
`skills/create-control-manifest/SKILL.md`. Shared director-gates provides mode/
authority guidance, not a TD-MANIFEST definition. Read the actual inline owner;
REJECT repairs before writing, CONCERNS follows its stated user-choice interface.

### Case 8: Authorized preview cannot become Active

**Fixture:** Required architecture review or Accepted governing decision is missing;
the user authorizes a Draft/Blocked manifest preview. Full gate approves the extraction,
or lean skips the gate.

**Expected:** Save only the authorized preview with actual Draft/Blocked status and
missing-input/action/owner findings. Report the saved operation separately; no
Active/qualified COMPLETE, Story Ready or implementation handoff. An Active/COMPLETE
fixture requires verified required architecture, decisions, global gate and dependencies.

- [ ] Phase 5 preserves qualification from input checks; gate skip/approval cannot clear it.
- [ ] Consumer digest is full raw-file SHA-256/size outside the preview itself.
- [ ] Existing exact preview write scope is reused without another permission ask.
