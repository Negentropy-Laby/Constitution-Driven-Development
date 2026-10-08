# Skill Test Spec: /code-review

## Skill Summary

`/code-review` performs an architectural code review of source files in `src/`,
checking coding standards from `CLAUDE.md` (doc comments on public APIs,
dependency injection over singletons, data-driven values, testability). Findings classify actual choices using exact Accepted/CDD/local dispositions.
Significant unresolved decisions/conflicts require CHANGES REQUIRED. No code edits;
actual specialist/qa-tester reviews run where applicable. Verdicts: APPROVED,
APPROVED WITH SUGGESTIONS, CHANGES REQUIRED.

---

## Static Assertions (Structural)

Structural checks only; semantic assertions below need actual bound fixtures/review evidence.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: APPROVED, APPROVED WITH SUGGESTIONS, CHANGES REQUIRED
- [ ] Review-only writes nothing; new report effects require named authority/"May I write"
- [ ] Has a next-step handoff (what to do with findings)

---

## Director Gate Checks

No separate director gate is invented. Actual configured specialist and qa-tester
reviews apply; delegation inherits review-only authority and exact input scope.

---

## Test Cases

### Case 1: Happy Path — Source file follows all coding standards

**Fixture:**
- `src/gameplay/health_component.gd` exists with:
  - All public methods have doc comments (`##` notation)
  - No singletons used; dependencies injected via constructor
  - No hardcoded values; all constants reference `assets/data/`
  - ADR reference in file header: `# ADR: docs/architecture/adr-004-health.md`
  - Referenced ADR has `Status: Accepted`

**Input:** `/code-review src/gameplay/health_component.gd`

**Expected behavior:**
1. Skill reads the source file
2. Skill checks all coding standards: doc comments, DI, data-driven, ADR status
3. All checks pass
4. Skill outputs findings summary with all checks PASS
5. Verdict is APPROVED

**Assertions:**
- [ ] Each coding standard check is listed in the output
- [ ] All checks show PASS when standards are met
- [ ] Skill reads referenced ADR to confirm its status
- [ ] Verdict is APPROVED
- [ ] No edits are made to any file

---

### Case 2: Needs Changes — Missing doc comment and singleton usage

**Fixture:**
- `src/ui/inventory_ui.gd` has:
  - 2 public methods without doc comments
  - Uses `GameManager.instance` (singleton pattern)
  - All other standards met

**Input:** `/code-review src/ui/inventory_ui.gd`

**Expected behavior:**
1. Skill reads the source file
2. Skill detects: 2 missing doc comments on public methods
3. Skill detects: singleton usage at specific lines (e.g., line 42, line 87)
4. Findings list the exact method names and line numbers
5. Verdict is CHANGES REQUIRED

**Assertions:**
- [ ] Missing doc comments are listed with method names
- [ ] Singleton usage is flagged with file and line number
- [ ] Verdict is CHANGES REQUIRED when BLOCKING-level standard violations exist
- [ ] Skill does not edit the file — findings are for the developer to act on
- [ ] Output suggests replacing singleton with dependency injection

---

### Case 3: Architecture Risk — ADR reference is Proposed, not Accepted

**Fixture:**
- `src/core/save_system.gd` has a header comment: `# ADR: docs/architecture/adr-010-save.md`
- `adr-010-save.md` exists but has `Status: Proposed`
- Code itself follows all other coding standards

**Input:** `/code-review src/core/save_system.gd`

**Expected behavior:**
1. Skill reads the source file
2. Skill reads referenced ADR — finds `Status: Proposed`
3. Skill flags this as ARCHITECTURE RISK (code is implementing an unaccepted ADR)
4. Other coding standard checks pass
5. Verdict is CHANGES REQUIRED for significant required Proposed/unevidenced decisions; green tests cannot accept them

**Assertions:**
- [ ] Skill reads referenced ADR file to check its status
- [ ] ARCHITECTURE RISK is flagged when ADR status is Proposed
- [ ] Significant required Proposed decision yields CHANGES REQUIRED unless an evidenced valid scoped exception applies
- [ ] Output recommends resolving the ADR before affected implementation continues

---

### Case 4: Edge Case — No source files found at specified path

**Fixture:**
- User calls `/code-review src/networking/`
- `src/networking/` directory does not exist

**Input:** `/code-review src/networking/`

**Expected behavior:**
1. Skill attempts to read files in `src/networking/`
2. Directory or files not found
3. Skill outputs an error: "No source files found at `src/networking/`"
4. Skill suggests checking `src/` for valid directories
5. No verdict is emitted (nothing was reviewed)

**Assertions:**
- [ ] Skill does not crash when path does not exist
- [ ] Output names the attempted path in the error message
- [ ] Output suggests checking `src/` for valid file paths
- [ ] No verdict is emitted when there is nothing to review

---

### Case 5: Gate Compliance — No gate; LP may be consulted separately

**Fixture:**
- Source file follows most standards but has 1 CONCERNS-level finding (a magic number)
- `review-mode.txt` contains `full`

**Input:** `/code-review src/gameplay/loot_system.gd`

**Expected behavior:**
1. Skill reads and reviews the source file
2. No director gate is invoked; findings are required or permitted advisory according
   to actual code/decision/evidence scope, never all advisory by default
3. Skill presents permitted advisory findings as APPROVED WITH SUGGESTIONS
4. Output notes: "Consider requesting a Lead Programmer review for architecture concerns"
5. Skill invokes applicable configured specialist/qa-tester reviews within exact read-only scope

**Assertions:**
- [ ] No director gate is invoked in any review mode
- [ ] LP consultation is suggested (not mandated) in the output
- [ ] No source/status/session/index edits; report-only may save its new report
- [ ] Verdict is APPROVED WITH SUGGESTIONS only for permitted advisory findings

---

## Protocol Compliance

- [ ] Reads source file(s) and coding standards before reviewing
- [ ] Lists each coding standard check in findings output
- [ ] Does not edit any source files (read-only skill)
- [ ] No director gates are invoked
- [ ] Verdict is one of: APPROVED, APPROVED WITH SUGGESTIONS, CHANGES REQUIRED

---

## Coverage Notes

- Batch review of all files in a directory is not explicitly tested; behavior
  is assumed to apply the same checks file by file and aggregate the verdict.
- Test coverage checks (verifying corresponding test files exist) are a stretch
  goal not tested here; that is primarily the domain of `/test-evidence-review`.

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
- Unknown/conflicting/mixed domain: common checks continue, domain-specific findings
  remain incomplete until resolved; no silent Game fallback.
- Separate global Technical Setup min-three Foundation ADR rule remains in force;
  local no-ADR classifications neither waive it nor justify fabricated ADRs.

### Case 6: No link / Unknown domain / narrow report scope

A local helper without ADR link is classified no-adr with reason/owner. A new
trust-boundary/durable-format/state-ownership decision without a link is still
adr-required/CHANGES REQUIRED before affected continuation. Completed/green code
cannot establish covered. Missing concept files alone do not establish Unknown:
read configured legacy Product facts and actual owners first, never silent Game.

### Case 7: Legacy Product configuration without a concept

**Fixture:** Neither concept file exists. Populated `Language & Framework` selects
Python/stdlib and `Platform & Deployment` selects a Linux CLI. `Agent Routing` and
`File Extension Routing` select python-specialist; newer Product Stack fields are
unconfigured placeholders. A local Python source and its requirements are present.

- [ ] Resolve Product and the configured Python specialist from substantive legacy
  fields without requiring a concept, renamed headings or repeated domain approval.
- [ ] Read the actual source and applicable Product CLI rules; invoke required
  reviews only through supported runtime metadata, reporting unavailable execution.
- [ ] Keep placeholders from overriding actual configured facts. A conflicting
  real concept/configuration variant leaves only the affected route unresolved.
- [ ] Review-only invokes no write entrypoint and makes no acceptance/closure claim.
A saved report binds exact raw input identities and retained originals; report-only
approval does not authorize T3 index, session, source or status writes.

### Case 8: Review-only and report-only exclude non-dry-run writer callbacks

**Fixture:** A Product CLI validator accepts an injected writer. Valid-only and
mixed valid/invalid inputs can invoke `calls.append` before complete validation
when the actual public call supplies `dry_run=False`. Source, input and state
bytes are retained. The reviewed CDD requires validation before any writer call.

- [ ] Trace the actual public caller, arguments and callback receiver before
  diagnostics; a private helper signature does not prove the public default.
- [ ] Report the source-order conflict without invoking the non-dry-run writer.
  `calls.append` is still a target write entrypoint even with no disk effect.
- [ ] Review-only invokes neither a constructor/factory entering the target write
  path nor a non-dry-run callback for valid-only or mixed input, in any actor.
- [ ] Three existing checks explicitly use `dry_run=True` and a fresh inert spy.
  Obtaining its bound callback without invoking it is allowed; inspect the real
  branch and confirm the spy remains empty. Do not falsely label their successful
  zero-call execution a scope breach. An unexpected call is still a real breach,
  regardless of the spy name, green summary or absence of disk changes.
- [ ] Named report-only authority allows the one assigned new report/readback,
  not either non-dry-run writer probe, source repair, indexes or status updates.
- [ ] Each specialist receives the original exact paths/effects/prohibitions;
  inspect actual diagnostic commands and receivers. No file changes, later
  stopping or exclusion never relabels a real callback breach as PASS.
- [ ] Missing actual diagnostic traces leave the affected assertion incomplete.
- [ ] The Game counterpart's indirectly referenced 47-byte `assumptions.txt`
  exists under an ignored input directory. Directly read and bind its original
  path and full bytes; `rg --files` omitting it cannot establish missing. A
  separately absent-path variant records the real direct attempt/result; unread
  or inaccessible inputs remain incomplete without a false absence verdict.
- [ ] A separately authorized write counterexample runs on an isolated copy
  within its named effects. It remains a different scope; do not use that
  authority or result to qualify the original review-only invocation.
