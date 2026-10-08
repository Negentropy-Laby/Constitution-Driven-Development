---
paths:
  - "design/cdd/**"
---

# Design Document Rules

- Every Game module CDD MUST substantively cover these 8 semantic roles, retaining valid section aliases: Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria
- Every Product module CDD MUST substantively cover equivalent semantic roles, retaining valid section aliases: Overview, User Promise / JTBD, Detailed Behavior, Contracts / Data Model, Edge Cases, Dependencies, Configuration Knobs, Acceptance Criteria
- Game formulas must include variable definitions, expected value ranges, and example calculations
- Product contracts must include schemas, inputs, outputs, error behavior, exit codes, state transitions, or migration behavior as relevant
- Edge cases must explicitly state what happens, not just "handle gracefully"
- Dependencies must be bidirectional — if system A depends on B, B's doc must mention A
- Game tuning knobs must specify safe ranges and what gameplay aspect they affect
- Product configuration knobs must specify defaults, valid ranges/enums, environment ownership, rollout behavior, and operational risk
- Acceptance criteria must be testable — a QA tester must be able to verify pass/fail
- No hand-waving: "the system should feel good" or "the workflow should be intuitive" is not a valid specification
- Game balance values must link to their source formula or rationale
- Product limits, quotas, thresholds, retry budgets, migration batch sizes, and pricing/scoring values must link to evidence or rationale
- Resolve document kind and its actual owner set in `design/INSTRUCTIONS.md`;
  use the semantic eight-section contract for module CDDs only. Preserve
  historical section aliases with real substantive bodies and all Game/Product requirements.
- Write incrementally within the approved document/batch/synchronization scope.
  Create a skeleton for a new file only; retrofit preserves existing bodies and
  changes named gaps/approved sections. Ask for unresolved material choices or
  explicit section-by-section preferences, not repeated approval of covered writes.
- Read back the closed changeset and its required evidence; writing or static
  checks alone do not establish semantic correctness or independent review.

Read actual bodies/configuration under `standards/technical-preferences.md`;
path/heading presence alone proves neither domain nor compliance. Apply
`standards/notes-adr-sync.md` and `standards/evidence-lifecycle.md` for decision,
exact-input and review/closure claims.
