# Skill Test Spec: /constitute-check

## Skill Summary

`/constitute-check` is a read-only-by-default constitutional health audit. It
verifies the memory bank, compares principles against current code and docs,
and observes actual installed inputs offline. It establishes live freshness only
through an actually available authorized read-only comparison with complete valid
evidence for the verified owner, Source and compared scope. Its sole write exception is an applicable exact
`adapter_state.yaml` record within approval; unavailable checks preserve prior state.

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

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] `allowed-tools` supports the applicable read-only comparison and the single approved state-record write
- [ ] Detects Game via `design/cdd/game-concept.md`
- [ ] Detects Product via `design/cdd/product-concept.md`
- [ ] Mentions User Promise, JTBD, target workflows, API/CLI contracts, and product CDDs
- [ ] Produces health verdicts: HEALTHY / NEEDS ATTENTION / CRITICAL
- [ ] Runs an applicable authorized read-only comparison with valid complete schema1 evidence for the verified owner and complete installed/Source scope when the comparison and diagnostic authority are available
- [ ] Consumer checks bind actual installed paths, neutral inputs, sole Source and approved customizations; local file presence alone does not establish Source identity

---

## Test Cases

### Shared initialized-audit fixture inputs

Except Case 1, supply substantive fixture T0 `basic_law_index.md`,
`active_context.md`, `current_state.md` and T1 `tech_context.md`,
`system_patterns.md`, `behavior_context.md`, plus stage-appropriate T2/T3
bodies/indexes and actual selected installed inputs with required reference closure.
Any case-specific omission overrides this baseline and stays a real global gap.
The project-owned binding identifies its actual role, portable sole Source/revision,
selected runtime, installed paths, required neutral inputs and retained differences.
Unavailable comparison is explicit; no fixture description or Source-only result
manufactures consumer freshness.

Principle selectors use the displayed `Law N`/`Principle N` number and its
actual Support ID. Core Thesis BL-01 and the unnumbered CDD boundary section are
not numbered principles. A BL suffix or list position is not a selector mapping.
Default and `full` analyze all applicable laws; a numeric focus limits principle
alignment, not global T0-T3/input/adapter checks. No selector variant below has
state-record write authority unless Case 5 separately provides the exact record.
Examples and fixture acceptance records apply only to the isolated fixture.

### Case 1: No constitution

**Fixture:**
- No `memory_bank/t0_core/basic_law_index.md`
- Run default plus `full` and valid numeric `2` variants against the same missing
  original; no new control plane or replacement law set may be created.

**Input:** `/constitute-check` (variants: `full`, `2`)

**Expected behavior:**
- Stops after reporting no constitution detected
- Recommends `/constitute`
- Does not attempt domain-specific validation
- Writes no files

### Case 2: Game constitution drift

**Fixture:**
- Use the initialized-audit baseline with substantive Game concept/pillars,
  combat CDD/source and applicable playtest context; Law 1 evidence is stale.
- Law 1 has Support ID BL-02, Law 2 has BL-03, and Law 3 has BL-04, with actual
  lifecycle/fixture-acceptance metadata. Law 2 has current alignment evidence.
- Numeric-focus variant requests `2` (and equivalent `#2`); deliberately omit
  required T0 `current_state.md`. Source/comparison is unavailable and prior
  adapter state is uninitialized. No state-record or repair authority exists.

**Expected behavior:**
- Checks principles against Player Fantasy, Game pillars, CDDs, source code, and playtest evidence
- Reports concern with concrete paths
- Recommends the next audit or reverse-document action
- Numeric-focus variant selects only Law 2 / BL-03 for principle alignment and
  labels Law 1 / BL-02 and Law 3 / BL-04 alignment `NotAssessed`; it does not
  relabel their stale/unverified evidence ALIGNED or imply all-law HEALTHY.
- Still reports the missing T0 current-state original, T1/T2/T3 health and live
  NOT AVAILABLE/recorded UNINITIALIZED separately. The global required-input
  gap retains CRITICAL regardless of selected Law 2 alignment.
- Selection, unavailable comparison and global health reporting invoke no write
  entrypoint or state-record offer without separate valid record authority.

### Case 3: Product constitution drift

**Fixture:**
- Use the initialized-audit baseline with substantive Product User Promise,
  JTBD and API/CLI contracts; actual API/CLI code lacks its required CDD evidence.
- Law 1 / BL-02 and Law 3 / BL-04 exist, with no displayed Law 2. Numeric `3`
  must select Law 3 / BL-04 despite its second list position; numeric `2` is missing.
- Invalid variants: `0`, `-1`, `2.5`, `nonsense` and `full 2`.
- Duplicate-number variant contains two distinct displayed Law 2 entries with
  different actual IDs; selector `2` must not silently choose either.
- T2 workflow contract is missing, the actual initialized T3 review evidence
  lacks its required review index, and no writer/state-record authority exists.

**Expected behavior:**
- Checks principles against User Promise, JTBD, target workflows, product modules, API/CLI contracts, and product CDDs
- Reports concern with concrete paths
- Does not require engine-specific artifacts for the product project
- Numeric `3` selects displayed Law 3 with BL-04; core thesis, boundary text and
  array position never become principle numbers.
- Missing `2` and duplicate `2` report no-match/ambiguity; invalid tokens report
  accepted usage/modes. None silently falls back to an all-law alignment audit.
- Global T0-T3 health observations still report the missing workflow contract
  and review index. Unselected principle alignment is NotAssessed, and invalid
  selection cannot manufacture an all-law HEALTHY verdict.
- All these variants remain read-only; no fixture repair, index/state update or
  acceptance is inferred from the selector or diagnostic result.

### Case 4: Uninitialized state, approval declined

**Fixture:**
- Use the initialized-audit baseline and its complete actual binding/reference
  closure; `adapter_state.yaml` retains the deterministic uninitialized bytes.
- An actually available authorized read-only comparison covers the exact owner,
  verified Source revision, installed allowlist and approved customizations.
  Its valid schema-1 JSON supplies real full digests, UTC time, commit, counts
  and portable check description from retained fixture input/output bytes.
- User declines the exact displayed state-record write. These are execution
  preconditions, not a claim that this spec calibration ran the comparison.

**Expected behavior:**
- Reports live `FRESH` and recorded `UNINITIALIZED` separately
- Shows the complete proposed YAML record
- Leaves every file unchanged when approval is declined

### Case 5: Fresh result approved for recording

**Fixture:**
- Use Case 4 complete compared input/output scope and valid schema-1 live result.
- User explicitly approves the complete displayed record and exact
  `memory_bank/t2_execution/adapter_state.yaml` write effect; no other write is
  covered. Matching existing authority is reused without a repeated question.

**Expected behavior:**
- Writes only `memory_bank/t2_execution/adapter_state.yaml`
- Records schema/manifest versions, both digests, commit, UTC timestamp, and check command
- Does not regenerate adapters or change any other memory-bank file

### Case 6: Stale or invalid adapter evidence

**Fixture:**
- Use Case 4 actual bound input scope. Separate variants supply a valid stale
  result with non-zero drift counts/paths, malformed or scope-mismatched JSON
  from a comparison that ran, and an unavailable comparison that never ran.
- Only the valid stale variant approves the displayed exact state record. Other
  variants have no state-record write authority and preserve prior bytes.
- Missing-framework variant removes the actual framework originals/binding;
  no substitute placeholder may satisfy the affected scope.

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
- [ ] Default, full and numeric modes honor displayed law numbers/actual IDs;
  invalid/missing/duplicate selection stays read-only with no silent all-law fallback
- [ ] Numeric focus preserves global T0-T3/input/adapter health checks and their
  severity; unselected law alignment is NotAssessed, never certified ALIGNED
