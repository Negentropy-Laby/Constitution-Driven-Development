# Skill Test Spec: /constitute-check

## Skill Summary

`/constitute-check` is a read-only-by-default constitutional health audit. It
verifies the memory bank, compares principles against current code and docs,
and runs the machine-readable adapter freshness check. Its sole write exception
is an exact `adapter_state.yaml` record after explicit approval.

---

## Static Assertions (Structural)

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] `allowed-tools` supports the checker and the single approved state-record write
- [ ] Detects Game via `design/cdd/game-concept.md`
- [ ] Detects Product via `design/cdd/product-concept.md`
- [ ] Mentions User Promise, JTBD, target workflows, API/CLI contracts, and product CDDs
- [ ] Produces health verdicts: HEALTHY / NEEDS ATTENTION / CRITICAL
- [ ] Runs `python scripts/sync_adapters.py --check --state-json`

---

## Test Cases

### Case 1: No constitution

**Fixture:**
- No `memory_bank/t0_core/basic_law_index.md`

**Input:** `/constitute-check`

**Expected behavior:**
- Stops after reporting no constitution detected
- Recommends `/constitute`
- Does not attempt domain-specific validation
- Writes no files

### Case 2: Game constitution drift

**Fixture:**
- Memory bank exists
- `design/cdd/game-concept.md` exists
- `src/gameplay/combat/` exists but principle evidence is stale

**Expected behavior:**
- Checks principles against Player Fantasy, Game pillars, CDDs, source code, and playtest evidence
- Reports concern with concrete paths
- Recommends the next audit or reverse-document action

### Case 3: Product constitution drift

**Fixture:**
- Memory bank exists
- `design/cdd/product-concept.md` exists
- API or CLI code exists with missing product CDD evidence

**Expected behavior:**
- Checks principles against User Promise, JTBD, target workflows, product modules, API/CLI contracts, and product CDDs
- Reports concern with concrete paths
- Does not require engine-specific artifacts for the product project

### Case 4: Uninitialized state, approval declined

**Fixture:**
- Framework contract exists
- `adapter_state.yaml` has `status: uninitialized`
- Live state JSON reports `fresh`

**Expected behavior:**
- Reports live `FRESH` and recorded `UNINITIALIZED` separately
- Shows the complete proposed YAML record
- Leaves every file unchanged when approval is declined

### Case 5: Fresh result approved for recording

**Fixture:**
- Live state JSON is valid and reports `fresh`
- User explicitly approves the displayed record

**Expected behavior:**
- Writes only `memory_bank/t2_execution/adapter_state.yaml`
- Records schema/manifest versions, both digests, commit, UTC timestamp, and check command
- Does not regenerate adapters or change any other memory-bank file

### Case 6: Stale or invalid adapter evidence

**Expected behavior:**
- A valid stale result lists non-zero counts and drift paths and may be recorded as `stale` after approval
- Missing or invalid JSON preserves the prior state and offers no write
- Missing framework files route to `/constitute` rather than creating `memory_bank/`

---

## Protocol Compliance

- [ ] Read-only by default; only the explicitly approved adapter-state record may use Write
- [ ] Declined or invalid checks produce no writes
- [ ] Reports evidence paths rather than vague status
- [ ] Keeps Game and Product checks parallel
- [ ] Recommends `/constitute` for missing constitution and `/project-stage-detect` for deeper audits
