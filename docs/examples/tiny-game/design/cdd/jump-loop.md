# CDD: Jump Loop

## Overview

Defines player jump input, jump buffering, landing, and goal completion.

## Player Fantasy

The player feels that missed jumps are fair and recoverable.

## Detailed Rules

- Press jump while grounded to jump immediately.
- Press jump up to 120 ms before landing to buffer the next jump.
- Touching the exit completes the room.

## Edge Cases

- Buffered jump expires if the player does not land within 120 ms.
- Holding jump does not create repeated jumps.

## Acceptance Criteria

- Jump starts on the first frame after valid input.
- Buffered jump triggers after landing.
- Exit completion fires once.
