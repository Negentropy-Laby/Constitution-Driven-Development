# Claude Adapter

This directory documents Claude Code adapter boundaries.

Common CDD assets live in neutral roots such as `workflow/`, `templates/`,
`standards/`, and `skill_testing/`. The `.claude/` directory is runtime-facing:
settings, hooks, rules, agents, skills, and small compatibility pointers needed
by Claude Code.

Do not add canonical workflow catalogs, document templates, shared standards, or
skill testing specs under `.claude/`.
