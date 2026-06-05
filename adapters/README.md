# Adapter Boundaries

This directory documents runtime adapter boundaries for CDD.

Common CDD source assets live outside adapter runtime trees:

| Root | Role |
|------|------|
| `workflow/` | Canonical workflow catalog and generated workflow views |
| `templates/` | Canonical document and memory-bank templates |
| `standards/` | Shared coding, coordination, context, and setup standards |
| `skill_testing/` | Cross-project skill and agent testing catalog, specs, rubric, and spec templates |
| `docs/` | User manuals, references, examples, and acceptance documentation |

Runtime adapter roots expose the same governance system to specific agent
surfaces:

| Root | Role |
|------|------|
| `.claude/` | Claude Code runtime-facing settings, hooks, rules, agents, skills, and compatibility pointers |
| `.agents/` | Codex or generic agent slash-command adapter copy |
| `.codex/` | Codex runtime configuration, agents, hooks, and local adapter support |

Do not move canonical workflow catalogs, templates, standards, or skill testing
assets into adapter runtime trees. Adapter directories may contain wrappers,
settings, generated copies, or compatibility pointers only.
