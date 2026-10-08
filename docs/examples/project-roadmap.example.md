# Project Roadmap

> Example output from `/cdd-status --dry-run`.
> Real project roadmaps are generated from `workflow/workflow-catalog.yaml`
> and saved to `production/project-roadmap.md` only after approval.

## Snapshot

- Domain: Product
- Declared phase: Architecture (illustrative fixture declaration)
- Observed work / candidate: architecture artifacts / Architecture (advisory)
- Qualified state: unverified; this example supplies no bound completion evidence
- Catalog structural observations: illustrative 13 / 42, not live catalog counts
- Qualified required progress: unknown; actual denominator/evidence must be checked
- Current blocker: Accessibility Requirements

## Next Commands

1. Create `design/accessibility-requirements.md` from `templates/accessibility-requirements.md`
2. `/test-setup`
3. `/gate-check technical-setup`

## Phase Progress

| Phase | Required (illustrative) | Observed | Missing | Observation |
| ----- | ---------------------- | -------- | ------- | ----------- |
| Concept | 3 | 3 | 0 | OBSERVED |
| Specification | 4 | 4 | 0 | OBSERVED |
| Architecture | 7 | 5 | 2 | BLOCKED |
| Pre-Implementation | 9 | 1 | 8 | UPCOMING |
| Implementation | 7 | 0 | 7 | UPCOMING |
| Verification | 2 | 0 | 2 | UPCOMING |
| Release | 3 | 0 | 3 | UPCOMING |

## Current Phase Checklist

| Step | Required | Evidence | Status |
| ---- | -------- | -------- | ------ |
| Technology Setup | Yes | `standards/technical-preferences.md` | OBSERVED |
| Architecture Document | Yes | `docs/architecture/architecture.md` | OBSERVED |
| Architecture Decisions | Yes | `docs/architecture/adr-001.md`, `adr-002.md`, `adr-003.md` | OBSERVED |
| Architecture Review | Yes | `docs/architecture/architecture-review-2026-06-04.md` | OBSERVED |
| Control Manifest | Yes | `docs/architecture/control-manifest.md` | OBSERVED |
| Accessibility Requirements | Yes | `design/accessibility-requirements.md` | MISSING |
| Test Framework Baseline | Yes | `tests/unit/`, `tests/integration/`, `.github/workflows/tests.yml` | MISSING |

## Product Surface Decisions

| Artifact | Status | Source |
| -------- | ------ | ------ |
| `design/ux/interaction-patterns.md` | REQUIRED | Product has CLI and API consumer flows |
| `design/design-system.md` | N/A | `design/ux/surface-profile.md`: CLI/API only, no UI component surface |
| `design/brand/style-guide.md` | OPTIONAL | No public brand, docs imagery, screenshots, diagrams, or release visuals in MVP scope |

## After This Phase You Should Have

- `standards/technical-preferences.md`
- `docs/architecture/architecture.md`
- `docs/architecture/adr-*.md` with at least 3 accepted decisions
- `docs/architecture/architecture-review-*.md`
- `docs/architecture/control-manifest.md`
- `design/accessibility-requirements.md`
- `tests/unit/`, `tests/integration/`, `.github/workflows/tests.yml`, and one example test

## Risks

- `design/accessibility-requirements.md` is missing; downstream UX and gate checks cannot verify the committed accessibility tier.
- Test framework baseline is missing; story implementation would start without a runnable verification contract.
- `design/ux/interaction-patterns.md` will be required in Pre-Implementation because the product has CLI/API consumer workflows.

## Notes

- Catalog is authoritative.
- Risk acceptance/exception is separate; it does not convert required FAIL/NotRun/
  Blocked/Pending/Unknown into PASS or qualified transition/completion.

Observed rows name locators only. Read actual substantive bodies, required
checks/decisions/reviews and authority before qualified completion; file counts/
paths/recorded statuses alone are insufficient. Exact runtime/support evidence
is not supplied by this illustrative example. No initialization or state write
occurs under `--dry-run`.
