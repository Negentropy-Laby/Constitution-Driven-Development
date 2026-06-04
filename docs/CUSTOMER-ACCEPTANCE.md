# Customer Acceptance Checklist

Use this page to validate that the template is ready for a customer pilot or
delivery review. Run these checks from a clean clone before marking a release as
accepted.

## 1. Repository Setup

```bash
git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git
cd Constitution-Driven-Development
python --version
```

Expected result:
- Python 3 is available.
- The repository opens without missing submodules or generated bootstrap steps.

## 2. Local Validation

```bash
python scripts/skill_lint.py --self-test
python scripts/skill_lint.py --strict .claude/skills
python scripts/skill_lint.py --strict .agents/skills
python scripts/workflow_consistency.py
```

Expected result:
- `skill_lint.py --self-test` passes.
- Strict skill lint reports `0 error(s)` for `.claude/skills`.
- Strict skill lint reports `0 error(s)` for `.agents/skills`.
- Workflow consistency reports `0 error(s), 0 warning(s)`.

Warnings about placeholder artifact paths are acceptable in strict skill lint
for a template repository, because consuming projects create those artifacts
later.

## 3. CI Validation

Confirm the `Template Consistency` workflow has passed on:
- `ubuntu-latest`
- `macos-latest`
- `windows-latest`

For the 2026-06-04 customer-delivery candidate, the validation run is:

```bash
gh run view 26934894349 --json jobs
```

Expected result:
- `consistency (ubuntu-latest)` is `success`.
- `consistency (macos-latest)` is `success`.
- `consistency (windows-latest)` is `success`.

## 4. New Project Smoke Path

In a fresh test project, run:

```text
/constitute
/help
/cdd-status --dry-run
```

Expected result:
- `/constitute` establishes governing principles.
- `/help` identifies the next required catalog step.
- `/cdd-status --dry-run` produces a roadmap draft without writing files.
- The draft follows the structure shown in `docs/examples/project-roadmap.example.md`.

## 5. Brownfield Smoke Path

In a repository with existing `src/`, `tests/`, `design/`, or
`docs/architecture/` artifacts, run:

```text
/project-stage-detect
/adopt
```

Expected result:
- The current stage is detected from artifacts.
- Missing template-format artifacts are listed as migration work.
- Existing project files are not overwritten without approval.

## 6. Workflow Surface Checks

Review these customer-visible entry points:
- `README.md`
- `docs/START-HERE.md`
- `docs/WORKFLOW-GUIDE.md`
- `.claude/docs/quick-start.md`
- `.claude/docs/skills-reference.md`
- `SUPPORT.md`
- `RELEASE_NOTES.md`

Expected result:
- Platform support consistently says Template Consistency CI is configured for
  Ubuntu, macOS, and Windows.
- Skill and template counts match the repository.
- Release order is `/release-checklist` -> `/launch-checklist` ->
  `/team-release`.
- Product surface N/A decisions point to `design/ux/surface-profile.md`.

## 7. Known Limits To Accept Explicitly

- This repository is a template and governance system, not an application build.
- Generated artifact path warnings can appear before a consuming project creates
  project-specific files.
- `/skill-test static all` is a skill workflow, not a CI-enforced command unless
  a project adds automation for it.
- Gate checks are governed advisory. A `FAIL` blocks normal advancement, but the
  user may explicitly override it with a documented risk note.
