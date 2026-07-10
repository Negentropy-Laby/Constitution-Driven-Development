# Claude Adapter

This directory documents Claude Code adapter boundaries.

Common CDD assets live in neutral roots such as `workflow/`, `templates/`,
`standards/`, and `skill_testing/`. Canonical skills, agents, hooks, and root
instructions live in `skills/`, `agents/`, `hooks/`, and `INSTRUCTIONS.md`.

The `.claude/` directory is runtime-facing: settings, hooks, rules, agents,
skills, and small compatibility pointers needed by Claude Code. The
`.claude/skills/`, `.claude/agents/`, `.claude/hooks/`, and `CLAUDE.md` files are
GENERATED from the canonical roots by `scripts/sync_adapters.py --write`. Edit
the canonical source, then regenerate; do not hand-edit these generated copies.

Do not add canonical workflow catalogs, document templates, shared standards, or
skill testing specs under `.claude/`.
