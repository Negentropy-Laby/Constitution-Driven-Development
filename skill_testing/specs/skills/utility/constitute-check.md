# Skill Test Spec: /constitute-check

## Skill Summary

`/constitute-check` is a read-only-by-default constitutional health audit. It
verifies the memory bank, compares principles against current code and docs,
and observes actual installed inputs offline. It runs a machine-readable live
freshness check only when the verified Source/comparison scope and separately
provided checker are available. Its sole write exception is an applicable exact
`adapter_state.yaml` record within approval; unavailable checks preserve prior state.

---

## Static Assertions (Structural)

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] `allowed-tools` supports the checker and the single approved state-record write
- [ ] Detects Game via `design/cdd/game-concept.md`
- [ ] Detects Product via `design/cdd/product-concept.md`
- [ ] Mentions User Promise, JTBD, target workflows, API/CLI contracts, and product CDDs
- [ ] Produces health verdicts: HEALTHY / NEEDS ATTENTION / CRITICAL
- [ ] Runs `python scripts/sync_adapters.py --check --state-json` in a verified CDD Source-library checkout when the optional checker and diagnostic scope are available
- [ ] Consumer checks bind actual installed paths, neutral inputs, sole Source and approved customizations; local file presence alone does not establish Source identity

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
- Applicable live state JSON reports `fresh` for the exact checked owner/inputs; a consumer includes its installed allowlist/customization comparison proof

**Expected behavior:**
- Reports live `FRESH` and recorded `UNINITIALIZED` separately
- Shows the complete proposed YAML record
- Leaves every file unchanged when approval is declined

### Case 5: Fresh result approved for recording

**Fixture:**
- Live state JSON is valid and reports `fresh` for the verified checked owner/inputs; a consumer includes its installed allowlist/customization comparison proof
- User explicitly approves the displayed record

**Expected behavior:**
- Writes only `memory_bank/t2_execution/adapter_state.yaml`
- Records schema/manifest versions, both digests, commit, UTC timestamp, and check command
- Does not regenerate adapters or change any other memory-bank file

### Case 6: Stale or invalid adapter evidence

**Expected behavior:**
- A valid stale result lists non-zero counts and drift paths and may be recorded as `stale` after approval
- Missing or invalid JSON from a check that actually ran reports INVALID, preserves the prior state and offers no write
- No applicable check because Source/binding/checker is unavailable reports NOT AVAILABLE rather than fabricated fresh/stale evidence
- Missing framework files route to `/constitute` rather than creating `memory_bank/`

---

### Case 7: Offline consumer with unavailable external Source

**Fixture:**
- Actual installed platform files, portable sole-Source binding and required neutral inputs exist
- No local general source trees or maintenance checker
- External Source is unavailable
- Existing adapter state is either uninitialized or a historical fresh/stale record

**Expected behavior:**
- Reads complete selected installed entries and required originals offline
- Reports live NOT AVAILABLE with the exact Source/comparison limitation
- Reports UNINITIALIZED or historical UNVERIFIED separately; neither becomes a live freshness result
- Preserves adapter-state bytes and completes independent constitution/input observations
- Does not invoke JSON parsing/state writing for a check that never ran, install tools or recreate general sources
- Variant missing a required reference names that original and affected pending scope; optional/same-name files do not replace it

### Case 8: Source-only freshness is insufficient for a consumer record

**Fixture:**
- A valid Source-library state JSON reports fresh
- The consumer installed allowlist/customization comparison has not been verified

**Expected behavior:**
- Treats Source identity/freshness as a separate observation
- Consumer live freshness remains NOT AVAILABLE; prior recorded state remains unchanged
- Does not offer a consumer state write from the Source-only result
- Only a complete applicable comparison plus exact state-file write authority can record fresh/stale values

---

## Protocol Compliance

- [ ] Read-only by default; only the explicitly approved adapter-state record may use Write
- [ ] Declined, invalid or unavailable checks produce no writes
- [ ] Source-only results do not certify consumer installed freshness or runtime execution
- [ ] Reports evidence paths rather than vague status
- [ ] Keeps Game and Product checks parallel
- [ ] Recommends `/constitute` for missing constitution and `/project-stage-detect` for deeper audits
