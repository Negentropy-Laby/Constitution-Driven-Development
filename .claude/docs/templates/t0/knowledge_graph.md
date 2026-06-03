# Knowledge Graph

## Core Technical Chain

```
[Module A] → [Module B] → [Module C]
     ↓
[Module D]
```

## Module Dependency Map

| Module | Depends On | Depended By | Status |
|--------|-----------|-------------|--------|
| `[module-a]` | — | `[module-b]` | stable |
| `[module-b]` | `[module-a]` | `[module-c]` | in-development |
| `[module-c]` | `[module-b]` | — | planned |

## Cross-Cutting Concerns

- **[Concern name]:** Affects [modules]. [Description of the concern and how it
  is addressed.]
- **[Concern name]:** Affects [modules]. [Description.]

## Integration Points

- **[Integration name]:** Between [module A] and [module B]. Protocol: [REST /
  gRPC / message queue / direct call]. Contract: [link to spec or ADR].

## Graph Notes

- This graph is derived from `T0` laws and `T1` system patterns.
- It is a current-state view — update when module boundaries change.
- For machine routing, see `memory_bank/module_support_map.yaml`.
