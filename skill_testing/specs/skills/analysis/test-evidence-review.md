# Skill Test Spec: /test-evidence-review

## Skill Summary

Use `[story-path | sprint | system-name]` to review Game/Product Story evidence
sufficiency ADEQUATE / INCOMPLETE / MISSING. Keep execution and closure separate.
Analysis is read-only; optional new report under `production/qa/` needs covered
scope. No director gate or input repair is implied.

## Static Assertions (Structural)

These inspect instruction structure; they do not establish runtime behavior.

- [ ] Required frontmatter fields exist: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] At least two phase or numbered section headings exist
- [ ] Declared result vocabulary includes ADEQUATE / INCOMPLETE / MISSING
- [ ] Scoped authority/shared-contract references and next-step handoff are present
- [ ] Story/sprint/system inputs and the optional report destination are documented

## Director Gate Checks

N/A: this skill does not trigger director gates. Specialist delegation,
where required by the canonical owner, is distinct from a director gate.

## Test Cases

### Case 1: Game evidence with one decisive assertion

**Fixture:**
A Game combat Story requires damage clamping. Its test has Arrange/Act/Assert
and one decisive `assert_eq(health.current_health, 0)` for the bound scenario.
Retained result, build and fixture identities match; all selected evidence is supplied.

**Input:** `/test-evidence-review [owning story path]`

**Expected behavior:**
1. Read the Story/CDD/test/helpers/results and map the actual behavioral oracle.
2. Assess evidence sufficiency against the selected AC/DoD and sign-offs.
3. Report ADEQUATE sufficiency separately from execution and independence.

**Assertions:**
- [ ] One decisive assertion is not automatically thin.
- [ ] Three vacuous assertions do not prove required AC coverage.
- [ ] ADEQUATE does not grant runtime PASS, independent review or Story closure.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 2: Unit timing or external API isolation gap

**Fixture:**
Required unit evidence uses `create_timer(1.0)` or a direct HTTPRequest
without needed mock/isolation and cannot reliably prove its AC. A separate variant
is an explicitly configured integration test with its own appropriate environment.

**Input:** `/test-evidence-review [owning story path]`

**Expected behavior:**
1. Read the oracle, timing/isolation and governing test scope.
2. Report the unit fixture INCOMPLETE with exact findings and remediation.
3. Evaluate the integration variant under its own declared requirements.

**Assertions:**
- [ ] The finding identifies the actual failure to prove the AC; no test edit occurs.
- [ ] Unit-only assumptions are not imposed blindly on configured integration evidence.
- [ ] Unavailable runtime remains separate from the sufficiency judgment.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 3: Product contract/CLI/migration evidence

**Fixture:**
A Product Story names actual contract paths, CLI exit/output, migration and
permission requirements. Variants lack evidence or have unreadable required dependencies.

**Input:** `/test-evidence-review [owning story path]`

**Expected behavior:**
1. Resolve explicit evidence paths and read substantive AC/error/boundary oracles.
2. Compare matching results and actual dependency identities.
3. Report MISSING for absent evidence and INCOMPLETE for unreadable required dependencies.

**Assertions:**
- [ ] Product scope is not replaced by Game path defaults.
- [ ] No SQL/schema/project coverage is invented.
- [ ] Filename/keyword presence alone does not yield ADEQUATE.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 4: Selected sign-off and historical results

**Fixture:**
QA orchestration is optional by default, but the Story explicitly requires
independent manual review. The author self-reviews; reviewer approval is Pending.
Historical execution is retained; a variant changes or loses an original input.

**Input:** `/test-evidence-review [owning story path]`

**Expected behavior:**
1. Resolve the actual selected sign-offs and their policy/authority/scope.
2. Keep required independent review Pending and dependent sufficiency incomplete.
3. Assess historical reuse against retained exact inputs and workflow permission.

**Assertions:**
- [ ] Self-review or gate skips do not satisfy required independence.
- [ ] Matching historical results retain their original label, never current-run execution.
- [ ] Changed/missing originals make affected evidence incomplete; no evidence yields MISSING.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 5: Report-only and separate completion

**Fixture:**
A named report-only approval covers one new report; initialized T3 indexes
and existing Story/test/state files are present but excluded.

**Input:** `/test-evidence-review sprint`

**Expected behavior:**
1. Read the covered evidence and prepare its scoped sufficiency findings.
2. Write only the assigned new report revision.
3. Keep execution, acceptance, indexes and completion separate.

**Assertions:**
- [ ] Tests, Story, indexes and state remain untouched and no repair entrypoint is invoked.
- [ ] Finished analysis/ADEQUATE confers no Complete, runtime PASS, publication or phase advancement.
- [ ] Required missing evidence/reviews retain their actual status and next owner/action.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Findings bind actual named inputs/attachments, full SHA/size and recoverable originals.
- [ ] Reading omissions, actual scope/actors/independence are recorded honestly.
- [ ] No gates/repair/implicit index writes; required gaps block dependent closure.

## Shared Contract Cases

Owners: project-root `standards/evidence-lifecycle.md`,
`standards/notes-adr-sync.md` and the canonical skill's QA policy.
Evaluate this skill's own actions/findings/recommendations in each fixture;
uninvoked closure workflows do not become runtime evidence.

### Case 6: Exact QA policy and closure counterexamples

**Fixture:**
Separate variants: default optional orchestration with actual required PASS;
explicit strict check unavailable; one required AC untested or Must Have blocked;
legacy RISKS label with passing vs failing required facts; report-only/self-review/
stale or missing originals/Unknown scope; exact permitted historical results.

**Input:** `/test-evidence-review [actual supported scope/mode]` with each stated policy/evidence variant

**Expected behavior:**
1. Read the actual catalog, owning requirements and each variant's policy/authority/evidence.
2. Keep sufficiency, operation finish, execution, risk acceptance and completion separate.
3. Report only eligible scope and remaining required owner/actions.

**Assertions:**
- [ ] Default optional plan/team orchestration, every required AC/check actual PASS: no invented strict gate; optional follow-up retains owner/due phase.
- [ ] Explicit selected strict check unavailable: actual source/authority/scope recorded; NotRun/Blocked/Pending prevents dependent qualification/closure. Review mode or missing QA Context cannot silently invent/waive strict or passing status.
- [ ] One required AC untested (even below 50%) or Blocked Must Have: no eligible Story COMPLETE/COMPLETE WITH NOTES/done or all-complete message. Optional orchestration waives no required behavior. Planning cases/ADEQUATE review is not execution.
- [ ] Legacy COMPLETE WITH RISKS aliases NOTES only after every required actual PASS/ decision/review/completion authority fact verified; original label preserved. Failed/unexecuted scope stays BLOCKED with separate risk acceptance.
- [ ] Report-only authority, self-review, explicit gate skip, unbound/stale evidence, missing original or Unknown scope leaves required dependent findings incomplete; no index/state/phase repair or broadened partial-scope approval.
- [ ] Exact permitted historical results retain original runtime/observer/inputs/scope and historical label, never this run's execution. Performance, required distinct sessions, target-platform/Product qualification need actual bound observations; file counts/keywords/line quotes/assumptions do not prove them.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 7: Optional context absence

**Fixture:**
No Memory Bank/QA Context exists; no strict selection is recorded. A variant
has actual conflicting policy or unresolved required applicability.

**Input:** `/test-evidence-review [actual supported scope/mode]`

**Expected behavior:**
1. Read actual catalog/defaults and required owning inputs.
2. Continue unaffected work without initializing optional context.

**Assertions:**
- [ ] No Memory Bank/QA Context exists and no explicit strict selection is recorded: use actual catalog default optional orchestration, disclose optional absence and continue required Story/DoD/evidence checks. Do not invent Unknown policy, a strict gate, passing execution, initialization or stage/closure authority. Actual conflicting policy or unresolved required applicability remains Unknown for dependent claims.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 8: Continuing named authority

**Fixture:**
Existing user approval names the exact output path and create/update effect.
A variant names only a report, excluding inputs/indexes/status/closure; another
introduces a materially new effect.

**Input:** `/test-evidence-review [actual supported scope/mode]` under the stated authority

**Expected behavior:**
1. Match current inputs and planned effects to the retained approval.
2. Execute covered effects and request only the missing material scope.

**Assertions:**
- [ ] An existing user-authorized changeset already names this exact output path and create/update effect. Reuse that authority through roles/retries and proceed after required facts/reviews pass; do not ask "May I write" again for the same scope. Missing authority or a materially new path/effect asks once after a concrete draft. A new report alone does not cover input/index/status/closure effects; director or content approval does not independently authorize writes.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 9: Configured legacy Product and conflicting domain

**Fixture:**
No concept document; actual populated `Language & Framework`,
`Platform & Deployment` and `Agent Routing` establish a Python CLI Product.
Newer Product Stack fields remain placeholders. Variant introduces a real
contradictory Game concept/configuration.

**Input:** `/test-evidence-review [actual supported scope/mode]`

**Expected behavior:**
1. Read actual populated legacy configuration and relevant concept bodies.
2. Resolve consistent Product scope; keep contradictory dependent routing Unknown.

**Assertions:**
- [ ] Resolve the consistent legacy fixture as Product before asking a domain question; use actual Product contracts/workflows and configured routing.
- [ ] Read substantive bodies/configuration, not filenames or keyword counts.
- [ ] Conflicting real owners leave affected routing Unknown; neutral checks continue without a silent Game fallback or an invented Both project enum.
- [ ] No Memory Bank initialization or completion claim follows from routing.

**Case Verdict:** PASS / FAIL / PARTIAL

## Coverage Notes

Instructed semantic fixtures are not actual workflow execution. Runtime and
independent verification remain NotRun until performed and exactly recorded.
