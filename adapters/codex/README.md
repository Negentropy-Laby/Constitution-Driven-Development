# Codex Adapter

This directory documents Codex and generic agent adapter boundaries.

Common CDD assets live in neutral roots such as `workflow/`, `templates/`,
`standards/`, and `skill_testing/`. Canonical skills, agents, hooks, and root
instructions live in `skills/`, `agents/`, `hooks/`, and `INSTRUCTIONS.md`.

The `.agents/` and `.codex/` directories are runtime-facing adapter copies or
configuration surfaces. The `.agents/skills/`, `.codex/agents/`, `.codex/hooks/`,
and `AGENTS.md` files are GENERATED from the canonical roots by
`scripts/sync_adapters.py --write`; do not hand-edit them.

The Markdown → TOML transform for `.codex/agents/` (`agent_md_to_toml`) retains
only `name`, `description`, and `developer_instructions`. It intentionally drops
`tools`, `model`, `maxTurns`, `memory`, `skills`, `disallowedTools`, and
`isolation` (Codex's agent schema carries no equivalents), and blocks generation
on any unknown frontmatter field. The canonical `agents/*.md` keeps the full
frontmatter as canonical metadata.

Nested per-directory guidance generates `AGENTS.md` siblings under `src/`,
`design/`, and `docs/` (Codex discovers them along the repository-root to
working-directory chain at session start). Codex's native `.codex/rules/*.rules`
files are unrelated command-approval policy, never generated, and never owned by
the generator; CDD path policies live in canonical `rules/` and Codex consults
them through root guidance rather than automatic path-glob loading.

Do not add canonical workflow catalogs, document templates, shared standards, or
skill testing specs under `.agents/` or `.codex/`.
