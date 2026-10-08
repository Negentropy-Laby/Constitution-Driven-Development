# Skill Test Spec: /security-audit

## Skill Summary

Use actual `[full | network | save | input | quick]` Game/Product surfaces and
scope-delegate assessment to security-engineer. Preserve severity and actual
verification. Optional new `production/security/security-audit-[date].md` report
needs covered authority; no director gate or universal SECURE certification.

## Static Assertions (Structural)

These inspect instruction structure; they do not establish runtime behavior.

- [ ] Required frontmatter fields exist: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] At least two phase or numbered section headings exist
- [ ] Declared result vocabulary includes scoped recommendations and PASS / FAIL / NotRun / Blocked / Pending
- [ ] Scoped authority/shared-contract references and next-step handoff are present
- [ ] Frontmatter names `security-engineer`; the five documented modes are present

## Director Gate Checks

N/A: this skill does not trigger director gates. Specialist delegation,
where required by the canonical owner, is distinct from a director gate.

## Test Cases

### Case 1: Game save/network boundaries

**Fixture:**
Configured Game source validates save bounds and network ownership. Encryption
exists; a public version string is displayed. No runtime exploit run is supplied.

**Input:** `/security-audit full`

**Expected behavior:**
1. Read the actual save/network data paths, configuration and governing scope.
2. Delegate the covered assessment to security-engineer and collect actual findings.
3. Report scoped findings and unexecuted verification separately.

**Assertions:**
- [ ] Encryption alone does not prove safety; plain JSON or a public version alone does not prove a vulnerability.
- [ ] Findings identify the actual trust boundary, severity and remediation basis.
- [ ] Static assessment provides no universal SECURE or platform qualification; runtime stays NotRun.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 2: Product permission/input/log/deployment finding

**Fixture:**
Configured Product API/CLI source contains a demonstrable permission or input
boundary issue and a sensitive logging path. Deployment/dependency context is supplied.

**Input:** `/security-audit input`

**Expected behavior:**
1. Resolve actual Product surfaces and inspect relevant caller/data/config paths.
2. Bind each finding to its source, scenario, governing requirement and severity.
3. Report remediation without executing an exploit or exposing secrets.

**Assertions:**
- [ ] Product checks use actual API/CLI/auth/config scope, without routing through Game-only categories.
- [ ] No project schema, legal ID or runtime exploit result is invented.
- [ ] The report omits credential contents and distinguishes discovery from observed verification.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 3: Prior finding resolution requires originals

**Fixture:**
A prior HIGH finding has original scenario and remediation/result attachments.
Current code contains the suggested keyword but the original scenario remains vulnerable.
Variant: one required original is unavailable.

**Input:** `/security-audit full`

**Expected behavior:**
1. Read the complete prior finding, required attachments and actual change/results.
2. Compare the original scenario with current verification before deciding resolution.
3. Preserve the historical finding and disclose missing required inputs.

**Assertions:**
- [ ] Keyword presence, a status label or risk acceptance does not mark the issue Resolved.
- [ ] Observed continuing failure remains Open/FAIL.
- [ ] Unavailable required originals or execution leave the affected assessment incomplete.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 4: Risk acceptance and partial/quick audit

**Fixture:**
A quick audit observes a HIGH failure; the user separately accepts a named risk.
Some release surfaces are explicitly excluded.

**Input:** `/security-audit quick`

**Expected behavior:**
1. Keep the observed finding and the exact risk-acceptance record separate.
2. Report inspected/excluded scope and unresolved dependent readiness.
3. Continue independent work within the authorized scope.

**Assertions:**
- [ ] Risk acceptance does not convert the finding or unexecuted checks to PASS.
- [ ] A partial/quick assessment is not CLEAR TO SHIP or full-scope qualification.
- [ ] Excluded surfaces and remaining owner/action are explicit.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 5: Report-only, delegated repair and unavailable role/source

**Fixture:**
Authority covers only one new audit report. A delegated security-engineer
proposes editing auth configuration, source input or a stage/index. Variant: the
role or required source is unavailable. Write counterexamples use isolated copies.

**Input:** `/security-audit full` with the stated report-only scope

**Expected behavior:**
1. Pass the original report-only scope and exclusions to the security-engineer.
2. Inspect actual delegated tools/results; reject unapproved remediation effects.
3. Write only the covered new report and disclose unavailable assessment inputs/roles.

**Assertions:**
- [ ] No auth/config/source/index/stage repair entrypoint is invoked under report-only authority.
- [ ] An actual delegated unauthorized repair is reported as a boundary failure; unchanged files alone do not prove compliance.
- [ ] Only the assigned report may be written, without inventing an independent review or SECURE verdict.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Actual source/prior finding/minimum attachment closure retains full SHA/size/originals.
- [ ] Actor/reviewer/authority roles and actual runtime state honest and separate.
- [ ] No implicit repair/acceptance/publication/completion or universal artifact gate.

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

**Input:** `/security-audit [actual supported scope/mode]` with each stated policy/evidence variant

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

**Input:** `/security-audit [actual supported scope/mode]`

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

**Input:** `/security-audit [actual supported scope/mode]` under the stated authority

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

**Input:** `/security-audit [actual supported scope/mode]`

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

Document fixtures are not penetration tests or runtime/platform/Product qualification.
Pattern review claims no legal compliance.
