# System Patterns

## Architectural Style

**Primary style:** [e.g., Layered Architecture / Hexagonal / Microservices /
Event-Driven / Monolith with well-defined modules]

**Rationale:** [Why this style was chosen — reference the core principles from
T0 that drove this decision.]

## Core Patterns

### Pattern 1: [Name]

- **What it is:** [Description of the pattern]
- **Where it applies:** [Modules or layers that use it]
- **Why it exists:** [Which T0 law(s) it supports]
- **Anti-pattern:** [What to avoid — what would violate this pattern]

### Pattern 2: [Name]

- **What it is:** [Description]
- **Where it applies:** [Modules or layers]
- **Why it exists:** [T0 law support]
- **Anti-pattern:** [What to avoid]

## Module Boundaries

| Module | Responsibility | Owns | Communicates via |
|--------|---------------|------|-----------------|
| `[module-a]` | [What it does] | [Data/state it owns] | [Interface type] |
| `[module-b]` | [What it does] | [Data/state it owns] | [Interface type] |

## Data Ownership Rules

- Each module owns its own data store / schema
- Cross-module access is via [API / events / shared read models] only
- [Any specific policies about data flow direction]

## Pattern Notes

- This file is a `T1` support artifact — it explains HOW the architecture works.
- It does not replace `T0` laws — it supports them with structural detail.
- Update when architectural patterns change, not just when code changes.
