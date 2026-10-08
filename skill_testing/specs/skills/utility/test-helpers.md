# Skill Test Spec: /test-helpers

## Skill Summary

`/test-helpers` generates engine/stack-specific test helper utilities for the project's
test suite. Helpers include factory functions (for creating test entities with
known state), fixture loaders, assertion helpers, and mock stubs for external
dependencies. Generated helpers follow the naming and structure conventions in
`coding-standards.md`. Ordinary utilities are written to `tests/helpers/`;
Python/pytest shared fixtures live in `tests/conftest.py` for its test subtree.

Create/extend effects use exact named authority; ask "May I write/extend" only
for missing or materially new effects after showing their concrete draft. Existing
helpers/conftest originals are preserved by authorized additive extensions. No
director gates apply. COMPLETE describes file generation only; unimplemented
application/database fixtures remain Pending, not runnable or executed PASS.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keyword: COMPLETE
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff (e.g., write a test using the generated helper)

---

## Director Gate Checks

None. `/test-helpers` is a scaffolding utility. No director gates apply.

---

## Test Cases

### Case 1: Happy Path — Godot base factory scaffold

**Fixture:**
Actual Game configuration selects Godot 4/GDScript and its test framework.
The configured tests/ root exists. Player CDD defines health 100; no helpers exist.
Named authority covers the displayed base-helper create effects.

**Input:** `/test-helpers scaffold`

**Expected behavior:**
1. Read actual domain, engine/framework and test-root evidence.
2. Draft the Godot base helpers, including game_factory.gd with GameFactory.make_player(health: int = 100).
3. Apply only covered create effects and report generation separately from execution.

**Assertions:**
- [ ] Godot output uses GameFactory/make_* conventions, not an invented PlayerFactory/create_player API.
- [ ] Defaults have an actual source and no unrequested speed/business property is invented.
- [ ] The generated base factory avoids singleton dependencies and follows actual GDScript naming.
- [ ] COMPLETE describes generation; no passing test execution is implied.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 2: Missing configured test root — redirects to test setup

**Fixture:**
Domain and framework are configured (Game/Godot or Product/pytest). The
resolved test root is tests/ and that exact directory is absent. No write is authorized.

**Input:** `/test-helpers scaffold`

**Expected behavior:**
1. Directly check the resolved tests/ path before any generation/write entrypoint.
2. Report "Test directory not found — test framework must be set up first" and the actual missing path.
3. Recommend /test-setup and stop affected generation without creating the directory.

**Assertions:**
- [ ] The missing-root message identifies the actual tests/ path.
- [ ] /test-setup is recommended; no write tool, installation or scaffold entrypoint is called.
- [ ] The prerequisite failure is not COMPLETE.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 3: Existing helper — authorized additive extension

**Fixture:**
Configured Game tests and enemy CDD exist. tests/helpers/game_factory.gd
contains custom make_player() code. The user chooses its additive make_enemy()
extension and authorizes that exact effect; a variant introduces a name conflict.

**Input:** `/test-helpers enemy` with the stated extension choice

**Expected behavior:**
1. Read the complete existing helper and actual enemy context.
2. Draft the covered make_enemy extension, preserving existing code/imports.
3. Resolve any conflicting name/behavior with real alternatives before that write.

**Assertions:**
- [ ] Existing make_player and custom behavior are preserved, not replaced by a template.
- [ ] Covered additive authority continues; new paths/effects require a concrete scope decision.
- [ ] The name-conflict variant does not silently redefine an existing function.
- [ ] Generation COMPLETE remains separate from actual usability/execution.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 4: Missing system CDD — no invented business defaults

**Fixture:**
Game framework/test root are configured. The inventory system CDD and its
implementation are absent. A separate variant explicitly authorizes only a generic scaffold.

**Input:** `/test-helpers inventory`; then `/test-helpers scaffold` only if separately selected

**Expected behavior:**
1. Attempt the real inventory context paths and disclose the missing requirements.
2. Keep inventory defaults/usability Pending rather than inventing capacity or item behavior.
3. Allow only the separate covered generic scaffold; report its generation independently.

**Assertions:**
- [ ] No capacity=20 or other invented business default is presented as CDD-derived.
- [ ] The system-specific request remains unresolved; missing context is named.
- [ ] A permitted scaffold does not make missing business context or execution pass.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 5: No director gate for scaffold

**Fixture:**
Actual Game domain, engine and test framework are configured; an empty test
root exists and the base-helper create effects are already authorized.

**Input:** `/test-helpers scaffold`

**Expected behavior:**
1. Generate the covered base helper files after prerequisite checks.
2. Report generation COMPLETE without inventing director gate results.

**Assertions:**
- [ ] No director agents or gate IDs/skip messages appear.
- [ ] An existing empty configured root does not block scaffold.
- [ ] The output distinguishes generation from unexecuted tests.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 6: Pytest fixtures are shared with sibling test files

**Fixture:** Product/Python with an actual configured pytest test root under
`tests/`, two sibling tests that request the same fixture, and a real supplied
setup factory/dependency with observable local behavior. The existing import
layout supports ordinary helper imports. No shared conftest exists yet. Named
authority covers `tests/conftest.py` and the selected ordinary helper path only.

**Input:** `/test-helpers [actual system]`, requesting that shared fixture and
an ordinary assertion helper under the named scope.

**Input:** `/test-helpers [actual system]` under the stated scope

**Expected behavior:**
1. Read actual tests, setup dependencies and import layout.
2. Draft only the two covered shared-fixture and ordinary-helper effects.
3. Keep actual configured pytest execution and independent acceptance separate.

**Assertions:**
- [ ] Read the actual tests, required setup and import layout before drafting.
- [ ] Put the implemented shared fixture in `tests/conftest.py`, not the sibling
      helpers directory; both sibling tests request it by fixture argument.
- [ ] Put ordinary assertions in `tests/helpers/assertions.py` or an existing
      equivalent project module, and show an explicit supported import.
- [ ] Do not claim ordinary functions are pytest auto-discovered or import
      conftest as an ordinary utility module.
- [ ] Preserve original tests/config/source and reuse the two covered file
      effects; absent extra package/config authority does not permit those writes.
- [ ] Actual configured pytest execution by an authorized test operator, with
      retained full input/output identity, demonstrates both tests resolve the
      shared fixture and explicit ordinary-helper import. Authoring/file presence
      alone does not establish this execution or independent acceptance.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 7: Existing conftest is extended without replacing custom behavior

**Fixture:** `tests/conftest.py` contains a custom fixture, hook, setup/teardown,
imports and a retained sentinel. A needed new fixture name does not conflict.
The user has authorized its exact additive extension in the current scope.

**Input:** `/test-helpers [actual system]` under the stated scope

**Expected behavior:**
1. Read the complete original conftest and match exact additive authority.
2. Resolve conflicts before adding only the covered fixture/dependencies.
3. Preserve existing setup/hooks/teardown and distinguish authoring from execution.

**Assertions:**
- [ ] Directly read the complete original and append only the approved new
      fixture/dependencies, preserving existing custom content and behavior.
- [ ] Do not skip an approved necessary extension solely because the file
      exists, replace it with a template, delete it or redefine an existing name.
- [ ] A conflicting name/behavior is surfaced with real alternatives before
      that write; independent covered new files can continue.
- [ ] Actual configured pytest probes retain existing fixture/hook/teardown
      behavior while sibling tests can resolve the new fixture. The test operator
      must record results; unchanged sentinel text alone is not behavior PASS.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 8: App/database scaffold stays explicitly unimplemented

**Fixture:** Product/Python needs app/database fixtures, but their actual factory
or session setup is absent. Exact authority allows only an explicit scaffold;
no application implementation, installation or database activation is authorized.

**Input:** `/test-helpers [actual system]` under the stated scope

**Expected behavior:**
1. Disclose the actual missing factory/session dependencies.
2. Generate only explicitly authorized unimplemented scaffolds.
3. Report generation, usability and actual execution separately.

**Assertions:**
- [ ] Disclose each missing concrete implementation/dependency; do not invent a
      fake client/session or label it usable.
- [ ] Authorized placeholders retain `NotImplementedError` in the proper
      conftest location and are described as scaffolds with usability Pending.
- [ ] Generation COMPLETE, if the covered files are written, stays separate
      from usability, actual test execution and independent acceptance.
- [ ] If an authorized operator requests an unimplemented fixture, retain the
      actual setup error/result, never relabel it runnable or passing.
- [ ] No unrequested app/db fixture, source/config write or Memory Bank activation
      is added merely because the template contains an example.

---

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 9: Configured alternative test root

**Fixture:**
Product/pytest configuration selects checks/; it exists and tests/ does not.
Existing checks/conftest.py and a supported helper import layout are supplied.

**Input:** `/test-helpers [actual system]` with named checks/ extension effects

**Expected behavior:**
1. Resolve checks/ from actual configuration, without replacing it with tests/.
2. Read and extend its applicable conftest/helper module within the exact named scope.

**Assertions:**
- [ ] Absence of the illustrative tests/ root does not cause a false setup failure.
- [ ] Shared fixtures use the applicable checks/conftest.py; ordinary helpers use explicit supported imports.
- [ ] No unrequested tests/ tree or package/config rewrite is created.

**Case Verdict:** PASS / FAIL / PARTIAL

### Case 10: Unknown and configured legacy Product domain

**Fixture:**
A lacks substantive domain evidence. B has populated legacy Python CLI Product
configuration without a concept; newer fields are placeholders. C conflicts with
an actual Game concept. A/B/C use separate fixture roots.

**Input:** `/test-helpers scaffold`

**Expected behavior:**
1. Read substantive concept/configuration/decision owners for each fixture.
2. Resolve B as Product; leave A/C Unknown and stop their domain-dependent generation.

**Assertions:**
- [ ] No missing-concept Game fallback or invented Both domain occurs.
- [ ] B follows its actual language/framework; A/C may continue neutral inspection only.
- [ ] Unresolved routing invokes no domain-dependent writer or COMPLETE claim.

**Case Verdict:** PASS / FAIL / PARTIAL


---

## Protocol Compliance

- [ ] Resolves actual Game engine or Product language/framework before domain-dependent generation
- [ ] Reads required system CDD/context before assigning business defaults
- [ ] Missing system context leaves affected defaults/usability Pending; a covered generic scaffold is separate
- [ ] Detects existing helper files and offers extend rather than replace
- [ ] Reuses exact named create/extend scope; asks "May I write/extend" only for
      missing or materially new effects after showing the concrete draft
- [ ] Verdict COMPLETE describes generation, with usability/execution/acceptance
      separately reported; unimplemented fixtures stay Pending
- [ ] Pytest shared fixtures are in tests/conftest.py; ordinary utilities use
      explicit verified imports, and existing custom conftest content is preserved

---

## Coverage Notes

- Mock/stub helper generation (for dependencies like save systems or audio buses)
  follows the same pattern as factory helpers and is not separately tested.
- Unity C# helper generation (using NSubstitute or custom mocks) follows the
  same logic as Case 1 with language-appropriate output.
- The case where the requested helper type is not recognized is not tested;
  the skill would ask the user to clarify the helper type.
