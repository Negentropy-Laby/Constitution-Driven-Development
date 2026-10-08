---
name: test-helpers
description: "Generate test helper libraries for the project's test suite. Game: engine-specific helpers (Godot, Unity, Unreal). Product: language-appropriate helpers (pytest fixtures, vitest factories, etc.). Reads existing test patterns and produces tests/helpers/ utilities and tests/conftest.py pytest fixtures tailored to the project's systems."
argument-hint: "[system-name | all | scaffold]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write
---

## User Guide

- When to use: Generate test helper libraries for the project's test suite. Game: engine-specific helpers (Godot, Unity, Unreal). Product: language-appropriate helpers, with pytest fixtures in tests/conftest.py and ordinary utilities in tests/helpers/.
- Inputs: Command arguments: `/test-helpers [system-name | all | scaffold]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Test Helpers

Writing test cases is faster and more consistent when common setup, teardown,
and assertion patterns are abstracted into helpers. This skill generates a
`tests/helpers/` library tailored to the project's actual engine/stack, language,
and systems — so every developer writes less boilerplate and more assertions.

**Output:** `tests/helpers/` domain-specific utilities; Python/pytest shared
fixtures in `tests/conftest.py` for tests in that directory and its descendants.

Apply `standards/evidence-lifecycle.md` and existing named path/effect authority.
Read existing originals before proposing create/extend effects. Review-only
produces conversation guidance without invoking a writer; helper generation,
actual usability, test execution and independent acceptance are separate facts.

**When to run:**
- After `/test-setup` scaffolds the framework (first time)
- When multiple test files repeat the same setup boilerplate
- When starting to write tests for a new system

---

## Phase 0: Domain Detection

Resolve Game or Product from substantive concept bodies, configured fields and
explicit project decisions under `standards/technical-preferences.md`. Populated
legacy Product configuration can establish Product without a concept. Filenames
and placeholder fields alone do not establish either domain.

- **Game** → engine-specific helpers below; retain the Game examples.
- **Product** → configured language/framework helpers below.
- **Unknown** → disclose absent or conflicting evidence and ask for the unresolved
  domain decision. Neutral inspection may continue; do not generate domain-dependent
  helpers or silently fall back to Game. Supporting both domains does not create
  a Both project-domain value.

---

## 1. Parse Arguments

**Modes:**
- `/test-helpers [system-name]` — generate helpers for a specific system
  (e.g., `/test-helpers combat`)
- `/test-helpers all` — generate helpers for all systems with test files
- `/test-helpers scaffold` — generate only the base helper library (no
  system-specific helpers); use this on first run
- No argument — run `scaffold` if no helpers exist, else `all`

---

## 2. Detect Engine/Language/Stack

Read `standards/technical-preferences.md` and extract:
- `Engine:` value (if game)
- `Language:` value
- `Framework:` from the Testing section

**[Game]** If engine is not configured: "Engine not configured. Run `/setup-engine` first."
**[Product]** If language is not configured: "Language/stack not configured. Run `/setup-engine` first."

### Test setup prerequisite

Read the actual testing configuration and `/test-setup` output to resolve the
framework, test root and discovery patterns. `tests/` is the default used by the
examples below, not a requirement to replace a valid configured alternative.
For a different root, place utilities beneath that root and pytest shared fixtures
in its applicable parent conftest; preserve the project's actual import layout.

Directly check the resolved test root before any scaffold/create/extend entrypoint.
If it is absent, report:
"Test directory not found — test framework must be set up first".
Name the actual missing path and recommend `/test-setup`. If the testing
framework is unconfigured, disclose that prerequisite too. Stop affected generation
without calling a write tool, creating the test root, installing a framework or
returning COMPLETE. An existing empty root with a configured framework is valid
for an authorized `scaffold`; no existing test file is required for that mode.

---

## 3. Load Existing Test Patterns

Scan the test directory for patterns already in use:

```
Glob pattern="tests/**/*_test.*" (all test files)
```

For a representative sample (up to 5 files), read the test files and extract:
- Setup patterns (how `before_each` / `setUp` / fixtures are written)
- Common assertion patterns (what is being asserted most often)
- Object creation patterns (how game objects or scenes are instantiated in tests)
- Mock/stub patterns (how dependencies are replaced)

For Python/pytest, use the configured test discovery patterns (including
`test_*.py` when selected), rather than only the generic glob above. Directly
read existing `tests/conftest.py` and applicable
nested conftest files, fixture dependencies, hooks and the actual import layout.
Preserve their custom setup/teardown and names. Shared fixtures belong in the
parent `tests/conftest.py`; a conftest inside the sibling helpers directory is
not discovered by tests elsewhere under `tests/`. Ordinary helper functions
need explicit imports through the project's actual supported module layout.

This ensures generated helpers match the project's existing style, not a
generic template.

Also read:
- `design/cdd/module-index.md` — to know which systems exist
- In-scope GDD(s) — to understand what data types and values need testing
- `docs/architecture/tr-registry.yaml` — to map requirements to tested systems

If a required system CDD or implementation is missing, disclose the exact missing
context and leave that system's business defaults/usability Pending. Do not invent
values from the illustrative templates. A separately covered generic `scaffold`
may proceed without system-specific behavior; generation COMPLETE does not make
missing business context, unimplemented fixtures or unexecuted tests pass.

---

## 4. Generate Engine-Specific Helpers

### Godot 4 (GDUnit4 / GDScript)

**Base helper** (`tests/helpers/game_assertions.gd`):

```gdscript
## Game-specific assertion utilities for [Project Name] tests.
## Extends GdUnitAssertions with domain-specific helpers.
##
## Usage:
##   var assert = GameAssertions.new()
##   assert.health_in_range(entity, 0, entity.max_health)

class_name GameAssertions
extends RefCounted

## Assert a value is within the inclusive range [min_val, max_val].
## Use for any formula output that has defined bounds in a CDD.
static func assert_in_range(
    value: float,
    min_val: float,
    max_val: float,
    label: String = "value"
) -> void:
    assert(
        value >= min_val and value <= max_val,
        "%s %.2f is outside expected range [%.2f, %.2f]" % [label, value, min_val, max_val]
    )

## Assert a signal was emitted during a callable block.
## Usage: assert_signal_emitted(entity, "health_changed", func(): entity.take_damage(10))
static func assert_signal_emitted(
    obj: Object,
    signal_name: String,
    action: Callable
) -> void:
    var emitted := false
    obj.connect(signal_name, func(_args): emitted = true)
    action.call()
    assert(emitted, "Expected signal '%s' to be emitted, but it was not." % signal_name)

## Assert that a callable does NOT emit a signal.
static func assert_signal_not_emitted(
    obj: Object,
    signal_name: String,
    action: Callable
) -> void:
    var emitted := false
    obj.connect(signal_name, func(_args): emitted = true)
    action.call()
    assert(not emitted, "Expected signal '%s' NOT to be emitted, but it was." % signal_name)

## Assert a node exists at path within a parent.
static func assert_node_exists(parent: Node, path: NodePath) -> void:
    assert(
        parent.has_node(path),
        "Expected node at path '%s' to exist." % str(path)
    )
```

**Factory helper** (`tests/helpers/game_factory.gd`):

```gdscript
## Factory functions for creating test game objects.
## Returns minimal objects configured for unit testing (no scene tree required).
##
## Usage: var player = GameFactory.make_player(health: 100)

class_name GameFactory
extends RefCounted

## Create a minimal player-like object for testing.
## Override fields as needed.
static func make_player(health: int = 100) -> Node:
    var player = Node.new()
    player.set_meta("health", health)
    player.set_meta("max_health", health)
    return player
```

**Scene helper** (`tests/helpers/scene_runner_helper.gd`):

```gdscript
## Utilities for scene-based integration tests.
## Wraps GdUnitSceneRunner for common patterns.

class_name SceneRunnerHelper
extends GdUnitTestSuite

## Load a scene and wait one frame for _ready() to complete.
func load_scene_and_wait(scene_path: String) -> Node:
    var scene = load(scene_path).instantiate()
    add_child(scene)
    await get_tree().process_frame
    return scene
```

---

### Unity (NUnit / C#)

**Base helper** (`tests/helpers/GameAssertions.cs`):

```csharp
using NUnit.Framework;
using UnityEngine;

/// <summary>
/// Game-specific assertion utilities for [Project Name] tests.
/// Extends NUnit's Assert with domain-specific helpers.
/// </summary>
public static class GameAssertions
{
    /// <summary>
    /// Assert a value is within an inclusive range [min, max].
    /// Use for any formula output defined in CDD Formulas sections.
    /// </summary>
    public static void AssertInRange(float value, float min, float max, string label = "value")
    {
        Assert.That(value, Is.InRange(min, max),
            $"{label} ({value:F2}) is outside expected range [{min:F2}, {max:F2}]");
    }

    /// <summary>Assert a UnityEvent or C# event was raised during an action.</summary>
    public static void AssertEventRaised(ref bool wasCalled, System.Action action, string eventName)
    {
        wasCalled = false;
        action();
        Assert.IsTrue(wasCalled, $"Expected event '{eventName}' to be raised, but it was not.");
    }

    /// <summary>Assert a component exists on a GameObject.</summary>
    public static void AssertHasComponent<T>(GameObject obj) where T : Component
    {
        var component = obj.GetComponent<T>();
        Assert.IsNotNull(component,
            $"Expected GameObject '{obj.name}' to have component {typeof(T).Name}.");
    }
}
```

**Factory helper** (`tests/helpers/GameFactory.cs`):

```csharp
using UnityEngine;

/// <summary>
/// Factory methods for creating minimal test objects without loading scenes.
/// </summary>
public static class GameFactory
{
    /// <summary>Create a minimal GameObject with a named component for testing.</summary>
    public static GameObject MakeGameObject(string name = "TestObject")
    {
        var go = new GameObject(name);
        return go;
    }

    /// <summary>
    /// Create a ScriptableObject of type T for data-driven tests.
    /// Dispose with Object.DestroyImmediate after test.
    /// </summary>
    public static T MakeScriptableObject<T>() where T : ScriptableObject
    {
        return ScriptableObject.CreateInstance<T>();
    }
}
```

---

### Unreal Engine (C++)

**Base helper** (`tests/helpers/GameTestHelpers.h`):

```cpp
#pragma once

#include "CoreMinimal.h"
#include "Misc/AutomationTest.h"

/**
 * Game-specific assertion macros and helpers for [Project Name] automation tests.
 * Include in any test file that needs domain-specific assertions.
 *
 * Usage:
 *   GAME_TEST_ASSERT_IN_RANGE(TestName, DamageValue, 10.0f, 50.0f, TEXT("Damage"));
 */

// Assert a float value is within inclusive range [Min, Max]
#define GAME_TEST_ASSERT_IN_RANGE(TestName, Value, Min, Max, Label) \
    TestTrue( \
        FString::Printf(TEXT("%s (%.2f) in range [%.2f, %.2f]"), Label, Value, Min, Max), \
        (Value) >= (Min) && (Value) <= (Max) \
    )

// Assert a UObject pointer is valid (not null, not garbage collected)
#define GAME_TEST_ASSERT_VALID(TestName, Ptr, Label) \
    TestTrue( \
        FString::Printf(TEXT("%s is valid"), Label), \
        IsValid(Ptr) \
    )

// Assert an Actor is in the world (spawned successfully)
#define GAME_TEST_ASSERT_SPAWNED(TestName, ActorPtr, ClassName) \
    TestNotNull( \
        FString::Printf(TEXT("Spawned actor of class %s"), TEXT(#ClassName)), \
        ActorPtr \
    )

/**
 * Helper to create a minimal test world.
 * Remember to call World->DestroyWorld(false) in teardown.
 */
namespace GameTestHelpers
{
    inline UWorld* CreateTestWorld(const FString& WorldName = TEXT("TestWorld"))
    {
        UWorld* World = UWorld::CreateWorld(EWorldType::Game, false);
        FWorldContext& WorldContext = GEngine->CreateNewWorldContext(EWorldType::Game);
        WorldContext.SetCurrentWorld(World);
        return World;
    }
}
```

---

### [Product] Language-Specific Helpers

#### Python (pytest)

**Shared fixtures** (`tests/conftest.py` — discovered for its test subtree):

Read the real application/database setup before implementing these fixtures.
The examples below are **unimplemented scaffolds**, not runnable clients or
database sessions. Generate only fixtures needed by the selected test scope.
If their actual factory/session dependency is unavailable, disclose the missing
implementation and keep usability Pending; preserve `NotImplementedError` in
an explicitly authorized scaffold instead of inventing a working dependency.

```python
"""Application-specific fixture scaffolds for [Project Name] tests.

Pytest discovers these names under tests/ without fixture imports.
app_client/db_session remain unimplemented until real setup is supplied.
"""
import pytest


@pytest.fixture
def app_client():
    """Create a test client for the application.
    Override in your own conftest.py for app-specific setup.
    """
    # Import your app factory here
    # from myapp import create_app
    # app = create_app(testing=True)
    # return app.test_client()
    raise NotImplementedError("Implement app_client for your application")


@pytest.fixture
def db_session():
    """Create a clean database session for a test, rolled back after.
    Use for any test that reads/writes to the database.
    """
    # Import your DB session here
    raise NotImplementedError("Implement db_session for your database")
```

**Ordinary assertion helpers** (`tests/helpers/assertions.py`):

```python
"""Explicitly imported assertions; these are not pytest fixtures."""
def assert_response_ok(response, status_code: int = 200):
    """Assert response has expected status code and valid JSON body."""
    assert response.status_code == status_code, \
        f"Expected {status_code}, got {response.status_code}: {response.data[:200]}"


def assert_validation_error(response, field: str):
    """Assert response is a 422 with validation error for the given field."""
    assert response.status_code == 422
    data = response.get_json()
    assert "errors" in data or "detail" in data
    error_str = str(data)
    assert field in error_str, f"Expected error about '{field}', got: {error_str[:200]}"


def assert_paginated(response, expected_total: int = None):
    """Assert response contains pagination metadata."""
    data = response.get_json()
    assert "items" in data or "data" in data, "Response missing paginated items"
    if expected_total is not None:
        meta = data.get("meta", data)
        assert meta.get("total") == expected_total or len(data.get("items", data.get("data", []))) <= expected_total
```

**Factory helper** (`tests/helpers/factories.py`):

```python
"""Minimal factory functions for creating test objects.

Use these instead of constructing objects manually in every test.
"""
from datetime import datetime, timezone


def make_user(**overrides) -> dict:
    """Create a minimal user dict for API tests."""
    return {
        "id": overrides.get("id", 1),
        "email": overrides.get("email", "test@example.com"),
        "name": overrides.get("name", "Test User"),
        **overrides
    }


def make_timestamp() -> str:
    """Return a consistent ISO timestamp for test data."""
    return datetime(2025, 1, 1, tzinfo=timezone.utc).isoformat()
```

#### TypeScript / Node (Vitest / Jest)

**Base helper** (`tests/helpers/test-utils.ts`):

```typescript
/**
 * Shared test utilities for [Project Name].
 *
 * Usage: import { createTestApp, assertOk } from '../helpers/test-utils';
 */
import { expect } from 'vitest'; // or '@jest/globals'

/** Minimal type for a HTTP response in tests. */
interface TestResponse {
  status: number;
  body: unknown;
  headers?: Record<string, string>;
}

/** Assert response has expected status code. */
export function assertOk(res: TestResponse, expectedStatus = 200): void {
  if (res.status !== expectedStatus) {
    const bodyStr = JSON.stringify(res.body).slice(0, 200);
    throw new Error(`Expected ${expectedStatus}, got ${res.status}: ${bodyStr}`);
  }
}

/** Assert response is a validation error (422). */
export function assertValidationError(res: TestResponse, field: string): void {
  expect(res.status).toBe(422);
  const body = JSON.stringify(res.body);
  expect(body).toContain(field);
}

/** Assert response is paginated with items array. */
export function assertPaginated(res: TestResponse, maxItems?: number): void {
  const body = res.body as Record<string, unknown>;
  const items = body.items ?? body.data;
  expect(Array.isArray(items)).toBe(true);
  if (maxItems !== undefined) {
    expect((items as unknown[]).length).toBeLessThanOrEqual(maxItems);
  }
}
```

**Factory helper** (`tests/helpers/factories.ts`):

```typescript
/** Minimal factory functions for creating test objects. */

export interface TestUser {
  id: number;
  email: string;
  name: string;
}

export function makeUser(overrides: Partial<TestUser> = {}): TestUser {
  return {
    id: 1,
    email: 'test@example.com',
    name: 'Test User',
    ...overrides,
  };
}
```

#### Rust (cargo test)

**Base helper** (`tests/helpers/mod.rs`):

```rust
/// Shared test utilities for [Project Name].
/// Include with: `mod helpers;` in tests or `#[path = "helpers/mod.rs"] mod helpers;`

use std::fmt::Debug;

/// Assert that a Result is Ok and return the inner value.
/// Use in tests where you need the value immediately on success.
pub fn assert_ok<T, E: Debug>(result: Result<T, E>) -> T {
    match result {
        Ok(val) => val,
        Err(e) => panic!("Expected Ok, got Err({:?})", e),
    }
}

/// Assert that two values are within epsilon of each other.
/// Useful for floating-point comparisons in formula tests.
pub fn assert_near(a: f64, b: f64, epsilon: f64) {
    assert!(
        (a - b).abs() < epsilon,
        "assertion failed: `(left ≈ right)`\n  left: `{}`,\n right: `{}`,\n epsilon: `{}`",
        a, b, epsilon
    );
}

/// Assert a string contains a substring, with a helpful panic message.
pub fn assert_contains(haystack: &str, needle: &str) {
    assert!(
        haystack.contains(needle),
        "assertion failed: string does not contain expected substring\n  string: `{}`\n  expected substring: `{}`",
        haystack, needle
    );
}
```

**Factory helper** (`tests/helpers/factories.rs`):

```rust
/// Minimal factory functions for creating test structs.
/// Add per-system factory modules as the project grows.

// Example structure — replace with your actual types:
// pub fn make_user(id: u64, email: &str) -> User { ... }
```

#### Go (go test)

**Base helper** (`tests/helpers/helpers.go`):

```go
// Package helpers provides shared test utilities for [Project Name].
// Import with: import "myproject/tests/helpers"
package helpers

import (
	"fmt"
	"testing"
)

// AssertEqual fails the test if expected != actual, with a formatted message.
func AssertEqual[T comparable](t *testing.T, expected, actual T, msg ...string) {
	t.Helper()
	if expected != actual {
		label := ""
		if len(msg) > 0 {
			label = msg[0] + ": "
		}
		t.Errorf("%sexpected %v, got %v", label, expected, actual)
	}
}

// AssertContains fails the test if the string does not contain the substring.
func AssertContains(t *testing.T, haystack, needle string) {
	t.Helper()
	// Avoid false positive on empty needle
	if len(needle) > 0 && len(haystack) == 0 {
		t.Errorf("expected string to contain %q, but it was empty", needle)
		return
	}
	// Use a simple contains check that works for any substring
	found := false
	for i := 0; i <= len(haystack)-len(needle); i++ {
		if haystack[i:i+len(needle)] == needle {
			found = true
			break
		}
	}
	if !found {
		t.Errorf("string does not contain %q:\n  %s", needle, haystack)
	}
}

// AssertNoError fails the test if err is not nil.
func AssertNoError(t *testing.T, err error) {
	t.Helper()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
}

// AssertStatusOK fails the test if the HTTP status code is not 2xx.
func AssertStatusOK(t *testing.T, statusCode int) {
	t.Helper()
	if statusCode < 200 || statusCode >= 300 {
		t.Errorf("expected 2xx status, got %d", statusCode)
	}
}
```

**Factory helper** (`tests/helpers/factories.go`):

```go
package helpers

// MakeTestUser returns a minimal user struct for testing.
// Override fields as needed.
type TestUser struct {
	ID    int
	Email string
	Name  string
}

func MakeTestUser(overrides ...func(*TestUser)) TestUser {
	u := TestUser{
		ID:    1,
		Email: "test@example.com",
		Name:  "Test User",
	}
	for _, fn := range overrides {
		fn(&u)
	}
	return u
}
```

---

## 5. Generate System-Specific Helpers

For `[system-name]` or `all` modes, generate a helper per system:

Read the system's CDD to extract:
- Data types (entity types, component names)
- Formula variables and their bounds
- Common test scenarios mentioned in Edge Cases

Generate `tests/helpers/[system]_factory.[ext]` with factory functions
specific to that system's objects.

Example pattern for a `combat` system (Godot/GDScript):

```gdscript
## Factory and assertion helpers for Combat system tests.
## Generated by /test-helpers combat on [date].
## Based on: design/cdd/combat.md

class_name CombatTestFactory
extends RefCounted

const DAMAGE_MIN := 0
const DAMAGE_MAX := 999  # From CDD: damage formula upper bound

## Create a minimal attacker object for damage formula tests.
static func make_attacker(attack: float = 10.0, crit_chance: float = 0.0) -> Node:
    var attacker = Node.new()
    attacker.set_meta("attack", attack)
    attacker.set_meta("crit_chance", crit_chance)
    return attacker

## Create a minimal target object for damage receive tests.
static func make_target(defense: float = 0.0, health: float = 100.0) -> Node:
    var target = Node.new()
    target.set_meta("defense", defense)
    target.set_meta("health", health)
    target.set_meta("max_health", health)
    return target

## Assert damage output is within GDD-specified bounds.
static func assert_damage_in_bounds(damage: float) -> void:
    GameAssertions.assert_in_range(damage, DAMAGE_MIN, DAMAGE_MAX, "damage")
```

---

## 6. Write Output

Present a summary of what will be created:

```
## Test Helpers to Create

**[Game]**
Base helpers (engine: [engine]):
- tests/helpers/game_assertions.[ext]
- tests/helpers/game_factory.[ext]
[engine-specific extras]

**[Product]**
Base helpers (language: [language]):
- Python/pytest: tests/conftest.py fixtures; tests/helpers/assertions.py utilities
- Other stacks: tests/helpers/test-utils.ts / helpers.go / mod.rs
- tests/helpers/factories.[ext]

System helpers ([mode]):
- tests/helpers/[system]_factory.[ext]  ← from [system] CDD
```

Show every actual output path and its create/extend effect, including
`tests/conftest.py` when selected. Reuse existing exact named authority; only
missing or materially new effects ask "May I write/extend these named files?"

**Preserve existing files.** Read the complete file before an authorized
extension. Add only the approved missing fixtures/functions; retain existing
imports, fixtures, hooks, setup/teardown and custom helper code. Never replace
the file with a template, delete it for regeneration or silently redefine an
existing name. On a name/behavior conflict, present actual alternatives and
resolve the affected extension before writing; continue independent new files
within their existing authority.

After writing, report **COMPLETE** only for the exact generation operation.
List created/extended paths and preserved content separately from usability:
unimplemented application/database fixtures stay Pending, and tests stay
NotRun until actual configured execution is observed. A written scaffold is
not a runnable fixture, passing test or independently accepted result.

**[Game]** "Helper files created. To use them in a test:
- Godot: `class_name` is auto-imported — no explicit import needed
- Unity: Add `using` directive or reference the test assembly
- Unreal: `#include \"tests/helpers/GameTestHelpers.h\"`"

**[Product]** "Helper files created. To use them in a test:
- Python/pytest: request fixtures from tests/conftest.py as test arguments;
  explicitly import ordinary assertions/factories through the verified project
  module layout. For an existing tests/helpers package, for example:
  `from tests.helpers.assertions import assert_response_ok`. Do not import
  conftest as a utility module or claim ordinary functions are auto-discovered.
  Missing package/import configuration remains disclosed; any new package
  markers or configuration need their own covered named effects
- TypeScript: use `import { assertOk } from '../helpers/test-utils'`
- Rust: add `mod helpers;` to test module or use `#[path = \"helpers/mod.rs\"]`
- Go: import `\"module/tests/helpers\"` in test files"

---

## Collaborative Protocol

- **Preserve existing helpers and conftest** — create new files or perform only
  authorized additive extensions after reading originals; no template replacement
  or silent fixture/function redefinition
- **Generated code is a starting point** — the generated factory functions use
  metadata patterns for simplicity; adapt to the actual class structure once
  the code exists
- **Helpers should reflect the CDD** — **[Game]** bounds and constants in helpers should
  trace to CDD Formulas sections. **[Product]** test data and assertions should trace to CDD Data Model and acceptance criteria. Not invented values.
- **Use scoped write authority** — reuse named create/extend approval and ask
  only for missing or materially new file effects after showing their draft

## Next Steps

- Run `/test-setup` if the test framework has not been scaffolded yet.
- Use `/dev-story` to implement stories — helpers reduce boilerplate in new test files.
- Run `/skill-test` to validate other skills that may need helper coverage.
