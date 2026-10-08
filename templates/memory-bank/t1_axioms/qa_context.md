# QA Context

This file indexes validation rules and evidence requirements without replacing
`production/qa/evidence/`.

## Test Baseline

- Test setup source: [path]
- CI workflow source: [path]
- Current status: [missing / partial / current]

## Evidence Model

| Evidence type | Source directory | Required by |
|---------------|------------------|-------------|
| Playtest or user validation | `production/qa/evidence/` | Polish / Verification |
| Smoke evidence | `production/qa/evidence/` | Release readiness |
| Customer acceptance | `docs/CUSTOMER-ACCEPTANCE.md` | Release |

## Selected QA Scope Record

Record actual catalog/domain/current phase and established user/project policy
source, authority, timezone-qualified time and exact applicable required checks.
These are evidence fields, not a new CLI/config schema or activation protocol.
QA orchestration is optional by default; explicit strict obligations need actual
provenance. Unknown/missing context cannot invent strict or passing qualification.
Required Story AC/DoD/evidence is never waived by optional orchestration.

Record each required AC → method/evidence/actual PASS/FAIL/NotRun/Blocked/Pending,
required reviewer/independence and remaining action/owner/due phase. Keep plans,
sufficiency, execution, independent review, risk acceptance and closure authority
separate. Permitted historical results retain exact inputs/scope/runtime/observer
and historical label. Preserve minimum dependency closure, full SHA-256/byte sizes
and recoverable originals/witnesses under `standards/evidence-lifecycle.md`.
This template does not activate memory.
