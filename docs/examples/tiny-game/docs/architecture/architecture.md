# Architecture: Tiny Jumper

## Runtime Modules

- `InputState`: captures raw input and timestamps.
- `PlayerController`: consumes input state and owns movement.
- `RoomState`: tracks exit completion.

## Test Boundary

Jump timing is tested in unit tests; room completion is tested in integration.
