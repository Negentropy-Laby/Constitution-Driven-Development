---
paths:
  - "tests/**"
---

# Test Standards

- Test naming follows the configured language/framework convention;
  `test_[system]_[scenario]_[expected_result]` remains the Game/Python example.
- Every test must have a clear arrange/act/assert structure
- Unit tests must not depend on external state (filesystem, network, database)
- Integration tests use isolated owned fixtures; cleanup targets only authorized
  fixture resources and preserves relied-on originals/history.
- Performance tests must specify acceptable thresholds and fail if exceeded
- Test data must be defined in the test or in dedicated fixtures, never shared mutable state
- Mock external dependencies — tests should be fast and deterministic
- Behavioral fixes need a regression check exposing the original defect, using
  automated or target/manual evidence appropriate to the capability. Document-only
  repairs do not need synthetic behavior tests.

## Examples

**Correct** (proper naming + Arrange/Act/Assert):

```gdscript
func test_health_system_take_damage_reduces_health() -> void:
    # Arrange
    var health := HealthComponent.new()
    health.max_health = 100
    health.current_health = 100

    # Act
    health.take_damage(25)

    # Assert
    assert_eq(health.current_health, 75)
```

**Incorrect**:

```gdscript
func test1() -> void:  # VIOLATION: no descriptive name
    var h := HealthComponent.new()
    h.take_damage(25)  # VIOLATION: no arrange step, no clear assert
    assert_true(h.current_health < 100)  # VIOLATION: imprecise assertion
```

## Product evidence

Verify applicable API/SDK success/validation/auth/compatibility, CLI flags/output/
exit codes, data/migration failure/rollback and UI/workflow states. Keep Game
GDScript examples above. Required evidence and coverage targets follow owning
CDD/Story and configured stack, not file counts or blanket per-file percentages.
Read `standards/evidence-lifecycle.md`: planning, review sufficiency, execution and
independence are separate. Write counterexamples/restore checks use isolated copies.
