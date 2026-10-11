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
- `docs/QUICK-START.md`
- `docs/WORKFLOW-GUIDE.md`
- `workflow/workflow-catalog.yaml`
- `skills/gate-check/SKILL.md`

## Known Limits

- The template provides process, documentation, and agent orchestration. It does
  not replace project-specific engineering review.
- Required project outputs may be absent before their owning workflow creates them.
- `/skill-test static all` is a skill workflow, not a CI-enforced command unless
  a project adds non-interactive automation for it.
- Local maintenance tools and historical Source CI are supplied separately,
  excluded from template delivery and not ordinary-use requirements.

## Platform Support

- Current acceptance uses `docs/CUSTOMER-ACCEPTANCE.md` and the actual project's
  configured tests/QA; unavailable live trials remain NotRun.
- Windows 10/11 local hook execution requires Git Bash on PATH.
- Hook scripts use POSIX-compatible shell patterns; verify applicable hooks within authorized scope.
- Windows toast notifications are optional and fall back to plain hook output when unavailable.

## Getting Help

For workflow questions, start with `/help` inside the project. It reads
`workflow/workflow-catalog.yaml` and reports the next required step for the
current phase.

In Codex, browse CDD skills with `/skills` or explicitly invoke `$help`; project
documentation keeps `/help` as the runtime-neutral logical command name.

For repository issues, include:

- Your current phase.
- The command or document you were using.
- The actual check output and required input paths; include separately supplied
  local diagnostic results only when such tools were available and used.
- Whether the project is Game or Product.
