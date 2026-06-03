# Story 001: Jump Buffer

## Type

Logic

## CDD Trace

- `design/cdd/jump-loop.md` Acceptance Criteria 1-2

## ADR Trace

- `docs/architecture/adr-0001-input-state.md`

## Acceptance Criteria

- [ ] Jump input within 120 ms before landing triggers a jump on landing.
- [ ] Expired buffered input does not trigger.

## Test Evidence

- `tests/unit/jump_loop/test_jump_buffer.*`
