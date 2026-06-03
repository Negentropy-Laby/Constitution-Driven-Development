# Control Manifest

- Input timestamps are owned by `InputState`.
- `PlayerController` may consume but not mutate room completion state.
- Jump buffer duration must come from configuration, not literals in gameplay code.
