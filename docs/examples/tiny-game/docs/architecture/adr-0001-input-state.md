# ADR-0001: Input State Owns Jump Buffer Timing

## Status

Accepted

## Decision

Store jump buffer timestamps in `InputState`, not in the room or UI layer.

## CDD Requirements Addressed

- `jump-loop.md`: buffered jump triggers after landing.

## Consequences

Movement code can test buffering without rendering or room dependencies.
