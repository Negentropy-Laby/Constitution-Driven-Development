# Claude Adapter

This directory documents Claude Code adapter boundaries.

Common CDD assets live in neutral roots such as `workflow/`, `templates/`,
`standards/`, and `skill_testing/`. Canonical skills, agents, hooks, and root
instructions live in `skills/`, `agents/`, `hooks/`, and `INSTRUCTIONS.md`.

The `.claude/` directory is runtime-facing: settings, hooks, rules, agents,
skills, and small compatibility pointers needed by Claude Code. The
`.claude/skills/`, `.claude/agents/`, `.claude/hooks/`, `.claude/rules/`, and
`CLAUDE.md` files are generated from the canonical roots in the designated Source.
Source changes use separately supplied authorized rendering; do not hand-edit
generated copies. An installed target reads its reviewed platform files directly,
retains project differences and does not need a local maintenance kit. Per-directory nested guidance also
generates `CLAUDE.md` siblings under `src/`, `design/`, and `docs/`.

Do not add canonical workflow catalogs, document templates, shared standards, or
skill testing specs under `.claude/`.
