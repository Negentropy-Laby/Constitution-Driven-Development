# Skill Test Spec: /skill-test

## Skill Summary

`/skill-test` reads canonical skills/agents, `skill_testing/catalog.yaml`,
`skill_testing/quality-rubric.md` and catalog-resolved `skill_testing/specs/`.
Static/spec/category/audit analysis is read-only. Separately authorized evidence
writes use existing T3 result paths; coverage updates need that effect in scope.
Without Memory Bank use existing report/conversation fallback, never activation.

## Static Assertions (Structural)

These inspect instruction structure; they do not establish runtime behavior.

- [ ] Required frontmatter fields exist: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] At least two phase or numbered section headings exist
- [ ] Declared result vocabulary includes COMPLIANT / NON-COMPLIANT / COMPLETE and PASS / PARTIAL / FAIL
- [ ] Scoped authority/shared-contract references and next-step handoff are present
- [ ] The documented Check 1–8 set includes Dual-Domain Parity

## Director Gate Checks

N/A: this skill does not trigger director gates. Specialist delegation,
where required by the canonical owner, is distinct from a director gate.

## Test Cases

### Case 1: Static Mode — Current checks and both domains

**Fixture:** Canonical brainstorm supplies all current checks and meaningful
Game/Product behavior, not merely domain keywords.

**Input:** `/skill-test static brainstorm`

**Expected behavior:**
1. Read the canonical skill and report the eight current checks individually.
2. Keep structural reasoning, behavior and optional writing separate.

**Assertions:**
- [ ] Read full canonical skill and report every current Check ID (1-8 today),
  including Check 8 in output, with justified PASS/WARN/FAIL.
- [ ] COMPLIANT requires no failures; disclose structural reasoning vs execution.
- [ ] No writes in review-only mode or when evidence writing is declined.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 2: Missing scoped collaborative behavior

**Fixture:** Write/Edit-capable skill lacks authority handling/shared reference;
other checks pass. Variant references and applies the shared scoped protocol.

**Input:** `/skill-test static [fixture skill]`

**Expected behavior:**
1. Inspect actual authority handling and shared-contract application.
2. Report the specific failure or valid continuing authorization without relying on a magic phrase.

**Assertions:**
- [ ] First variant fails collaborative check with specific authority gap.
- [ ] Other passes remain visible; overall NON-COMPLIANT.
- [ ] Shared-contract variant passes without needing per-file repeated questions.
  Phrase presence alone does not overcome contradictory actions.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 3: Spec mode resolves canonical assets

**Fixture:** Catalog resolves `skill_testing/specs/skills/gate/gate-check.md`;
canonical skill/spec exist.

**Input:** `/skill-test spec gate-check`

**Expected behavior:**
1. Resolve and read the actual canonical skill/spec pair.
2. Evaluate every case/assertion as instruction reasoning, disclosing unexecuted behavior.

**Assertions:**
- [ ] Read both full inputs and evaluate every actual case/assertion, without
  hardcoded case count or removed legacy testing paths.
- [ ] Report individual PASS/FAIL/PARTIAL and overall PASS/PARTIAL/FAIL.
- [ ] Detect semantic contradictions despite passing keywords; disclose that
  instruction reasoning does not execute a fixture.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 4: Audit mode with absent optional memory

**Fixture:** Live skill/agent/catalog assets exist; `memory_bank/` is absent.

**Input:** `/skill-test audit`

**Expected behavior:**
1. Enumerate current canonical assets and catalog coverage.
2. Use the existing fallback without initializing optional memory.

**Assertions:**
- [ ] Enumerate all actual skills/agents, resolve specs from catalog, report
  accurate coverage/counts and COMPLETE, not a fixed registry-size snapshot.
- [ ] Missing project history remains unknown; no memory activation/spec copies.
- [ ] Use established report/conversation fallback for authorized evidence.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 5: Category mode reads current rubric

**Fixture:** Canonical rubric defines G1-G5; gate-check is registered as gate.

**Input:** `/skill-test category gate-check`

**Expected behavior:**
1. Read the current registered category and rubric.
2. Report each metric and its mode-specific result.

**Assertions:**
- [ ] Read canonical rubric and score each actual metric; no stale asset path.
- [ ] Recommendation/mode rules are separate from transition/write/acceptance.
- [ ] Report COMPLIANT/WARNINGS/NON-COMPLIANT with individual scores.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 6: Report-only differs from named report-and-index approval

**Fixture:** Exact input bytes/digests retained. A authorizes only one new result
at its assigned path; B also lists coverage index. C is review-only.

**Input:** `/skill-test spec [fixture skill]` with the stated scope

**Expected behavior:**
1. Resolve each variant's exact paths/effects and retained inputs.
2. Perform only its authorized effects; preserve excluded inputs and historical links.

**Assertions:**
- [ ] A writes only new report, leaving inputs/coverage/state unchanged.
- [ ] B writes named report/index within continuing approval, no repeated question.
- [ ] C invokes no write entrypoint, even in-memory publication/resealing.
- [ ] Bind report to input manifest/full digests, retained bytes, scope/omissions,
  author/reviewer; distinguish verdict, approval and completion.
- [ ] Preserve historical revisions in index and prevent self-hash cycles.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 7: Changed indirect attachment and claimed independence

**Fixture:** Previously approved result relies on an ignored attachment now changed.
Filename and source commit unchanged; author provides green self-checks.

**Input:** `/skill-test spec [fixture skill]`

**Expected behavior:**
1. Read the minimum attachment closure and compare exact current identities.
2. Separate valid partial findings, stale approval and unavailable independent review.

**Assertions:**
- [ ] Follow minimum direct/indirect closure; retain attachment original-path
  witness/full digest/size/bytes rather than trust mutable path.
- [ ] Historical approval needs exact input/authority match; affected old claim
  is stale and cannot establish current approval.
- [ ] Writer checks are not independent review; disclose unavailable verification.
  Extra reading/line counts alone do not justify FAIL or certify behavior.
- [ ] Preserve valid partial findings and block only affected claims/work.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 8: Four-mode interface and genuine reading parity

**Fixture:** No argument; missing `static` target; a dual-domain skill implements
both complete branches before line 50; variant adds Product keywords but a later
body routes API/auth work through engine/player-only behavior.

**Input:** `/skill-test`; `/skill-test static`; `/skill-test static [fixture skill]` variants

**Expected behavior:**
1. Resolve the four-mode interface from actual arguments.
2. Evaluate substantive early/late Game/Product behavior and disclose unread owners.

**Assertions:**
- [ ] No argument performs existing audit; only missing required mode target/unknown
  mode returns usage. Preserve all four existing modes and eight reported checks.
- [ ] Complete early branch can PASS; line position alone does not fail it.
- [ ] Keyword-only/contradictory variant fails the specific behavior; inaccessible
  owner bodies are disclosed incomplete, not falsely fully read.
- [ ] Last-line quotation/hash/count proves neither full reading nor execution.
- [ ] Structural lint/CLI help, semantic eight/spec/category reasoning, fixture
  execution and independent review are separately reported.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 9: Legacy report format is inventory, not execution coverage

**Fixture:** The explicitly illustrative legacy block declares 74 sources and 74
specs with no execution records. Actual audit inputs instead contain two skill
definitions and one substantive spec, with no bound execution records.

**Input:** `/skill-test audit`

**Expected behavior:**
1. Use the actual fixture inventory rather than illustrative report literals.
2. Keep missing execution history unknown and project-domain routing concrete.

**Assertions:**
- [ ] Live counts reflect the actual two definitions/one spec inventory; do not
  substitute the fixture's 74, 100% or 74/74 as live or executed coverage.
- [ ] Absent raw execution history stays unknown; fixture literals certify no
  behavior/runtime checks, publication, acceptance or completion.
- [ ] Meta `[Both]` means the target artifact supports two domains; conflicting/
  mixed project scope needs concrete Game or Product routing, not a new enum.
- [ ] Spec reasoning reads actual job/body/configuration/inputs; concept existence,
  placeholders and keywords alone cannot pass parity or claim fixture execution.

**Case Verdict:** PASS / FAIL / PARTIAL

## Protocol Compliance

- [ ] Analyze read-only; optional writes apply shared scoped authority.
- [ ] Canonical test assets stay `skill_testing/`; project histories stay T3.
- [ ] Current checks/cases evaluated, unexecuted fixtures/reading omissions disclosed.
- [ ] No director gates/automatic acceptance/publication/completion.
- [ ] Recommend `/skill-improve` for verified gaps with evidence identity.

## Coverage Notes

These are behavioral expectations, not proof live automation passed. Execute
appropriate supported fixtures; disclose remaining semantic/runtime verification.
Counts and keywords support structure, not behavioral correctness.
