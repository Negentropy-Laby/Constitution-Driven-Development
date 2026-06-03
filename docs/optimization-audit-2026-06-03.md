# Optimization Audit - 2026-06-03

This note records the closure check for the next-round CDD template
optimization. It is intentionally a summary artifact, not a new workflow source
of truth.

## Implemented Batches

1. Phase diagrams and story paths now use the canonical early-stage boundary:
   `/setup-engine` and `/test-setup` belong in Technical Setup, and story files
   live under `production/epics/[epic-slug]/story-NNN-[slug].md`.
2. `/test-setup` now promises a runnable example test file as part of the
   required Technical Setup baseline, while `/test-helpers` remains optional.
3. Entry and gate wording has been cleaned of known damaged text and
   unsupported statistical claims.
4. Product long-form examples now pair with the main game teaching examples in
   `docs/examples/README.md`.
5. CI and `scripts/workflow_consistency.py` now guard story-path drift and
   examples phase-boundary drift.

## Final Verification

These checks passed after the implementation batches:

Validation covered whitespace, skill lint self-test, strict entry skill lint,
workflow consistency, known damaged terms, unsupported gate statistics, and
legacy story-path drift.

`skill_lint.py --strict .claude\skills\constitute\SKILL.md` still reports
artifact-path warnings for generated project files such as
`production/review-mode.txt` and `production/stage.txt`; it reports zero errors.

## Current Contract

- Canonical story path: `production/epics/[epic-slug]/story-NNN-[slug].md`.
- Required test baseline: `tests/unit/`, `tests/integration/`,
  `.github/workflows/tests.yml`, and one runnable example test.
- Optional test enhancement: `/test-helpers`.
- Gate policy: governed advisory; FAIL does not update `production/stage.txt`
  without explicit override and risk note.

## Final Consistency Pass - 2026-06-04

This pass closes the remaining gate/catalog drift found after the initial
optimization batches:

1. `quick-start.md` now includes `/architecture-review` and
   `/gate-check technical-setup` before UX work in both Game and Product paths.
2. The Polish / Verification gate now treats `/qa-plan`, `/team-qa`, smoke
   checks, balance review, and Release checklists as strict-QA blockers only
   when strict QA is explicitly enabled; otherwise they are CONCERNS or
   Release-phase follow-up.
3. Pre-Production validation now requires one report containing at least one
   unguided core-loop or core-workflow session. Cumulative three-session
   validation remains a Polish / Verification requirement.
4. Workflow Guide Phase 4 now stops at `/story-readiness` and
   `/gate-check pre-production`; formal `/dev-story` implementation begins in
   Phase 5.
5. `scripts/workflow_consistency.py` now guards quick-start Technical Setup
   closure, Phase 4 `/dev-story` drift, Release gate required-section drift,
   and validation quantity drift.

Final verification commands passed:

```powershell
git diff --check
python scripts\skill_lint.py --self-test
python scripts\workflow_consistency.py
python scripts\skill_lint.py --strict .claude\skills\constitute\SKILL.md
python scripts\skill_lint.py --strict .claude\skills\gate-check\SKILL.md
python scripts\skill_lint.py --strict .claude\skills\test-setup\SKILL.md
python scripts\skill_lint.py --strict .claude\skills\project-stage-detect\SKILL.md
python scripts\skill_lint.py --strict .claude\skills\help\SKILL.md
```

Legacy story-path, old architecture-path, old accessibility-command, and old
Release Required Artifact phrase scans also passed. The strict skill lint
commands still report artifact-path warnings for generated project files, but
all reported summaries contain zero errors.
