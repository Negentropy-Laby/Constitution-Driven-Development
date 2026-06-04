# Support

## Support Scope

This template supports Constitution Driven Development workflows for:

- Game projects using the existing Game command branches.
- Product projects such as APIs, CLIs, web apps, SDKs, data pipelines, and
  internal tools using the Product branches inside the same commands.
- Brownfield adoption through `/project-stage-detect`, `/adopt`, and
  `/reverse-document`.

The supported workflow contract is defined by:

- `README.md`
- `docs/START-HERE.md`
- `.claude/docs/quick-start.md`
- `docs/WORKFLOW-GUIDE.md`
- `.claude/docs/workflow-catalog.yaml`
- `.claude/skills/gate-check/SKILL.md`

## Known Limits

- The template provides process, documentation, and agent orchestration. It does
  not replace project-specific engineering review.
- Generated artifact path warnings from `skill_lint.py` are expected before a
  consuming project has created those files.
- `/skill-test static all` is a skill workflow, not a CI-enforced command unless
  a project adds non-interactive automation for it.

## Platform Support

- CI currently verifies the repository on Ubuntu.
- Windows 10/11 with Git Bash has been manually tested.
- macOS and Linux are designed to work with POSIX-compatible shell tools, but
  full matrix CI is not yet enabled.

## Getting Help

For workflow questions, start with `/help` inside the project. It reads
`.claude/docs/workflow-catalog.yaml` and reports the next required step for the
current phase.

For repository issues, include:

- Your current phase.
- The command or document you were using.
- The validation command output, especially `workflow_consistency.py` or
  `skill_lint.py` results.
- Whether the project is Game or Product.
