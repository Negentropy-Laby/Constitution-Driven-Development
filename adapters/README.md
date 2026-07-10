# Adapter Boundaries

This directory documents runtime adapter boundaries for CDD.

## Common canonical source assets

Canonical authority assets are hand-authored outside adapter runtime trees:

| Root | Role |
|------|------|
| `workflow/` | Canonical workflow catalog and generated workflow views |
| `templates/` | Canonical document and memory-bank templates |
| `standards/` | Shared coding, coordination, context, and setup standards |
| `skill_testing/` | Cross-project skill and agent testing catalog, specs, rubric, and spec templates |
| `docs/` | User manuals, references, examples, and acceptance documentation |
| `skills/` | Canonical slash-command skills (one `<name>/SKILL.md` each) |
| `agents/` | Canonical agent definitions (flat `<name>.md`) |
| `hooks/` | Canonical hook scripts |
| `INSTRUCTIONS.md` | Canonical root project instructions |
| `cdd-manifest.toml` | Source → output → transform contract for adapter generation |

## Runtime adapter roots (generated)

Runtime adapter trees expose the governance system to specific agent surfaces.
They are GENERATED from the canonical roots by `scripts/sync_adapters.py` and
must never be hand-edited after cutover:

| Root | Role |
|------|------|
| `.claude/` | Claude Code runtime-facing settings, hooks, rules, agents, skills, and compatibility pointers |
| `.agents/` | Codex slash-command skill adapter copy (generated) |
| `.codex/` | Codex runtime configuration, agents, hooks, and local adapter support (generated) |

Regenerate after editing a canonical source:

- `python scripts/sync_adapters.py --write` — regenerate every generated tree
- `python scripts/sync_adapters.py --check` — fail if any generated tree is stale

The manifest at `cdd-manifest.toml` and the generator at `scripts/sync_adapters.py`
own the canonical → generated mapping.

Do not move canonical workflow catalogs, templates, standards, or skill testing
assets into adapter runtime trees. Adapter directories may contain wrappers,
settings, generated copies, or compatibility pointers only.
