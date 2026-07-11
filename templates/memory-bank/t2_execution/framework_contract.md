# Framework Contract

This file records the canonical → generated adapter contract that governs the
project. It is the Memory Bank's index of the framework itself (separate from
project-specific laws in T0 and axioms in T1).

## Authority contract

- **Manifest:** `cdd-manifest.toml` is the single source of truth mapping
  canonical sources to generated runtime adapter outputs.
- **Generator:** `scripts/sync_adapters.py` renders adapters (`--write`) and
  checks freshness (`--check`). Read-only; it never mutates Memory Bank state.
- **Boundary checker:** `scripts/workflow_consistency.py` enforces boundary and
  freshness contracts.

## Canonical source classes

Hand-authored outside adapter runtime trees:

- `INSTRUCTIONS.md` — root instructions (plus nested `src/`, `design/`, `docs/`
  `INSTRUCTIONS.md`).
- `skills/` — slash-command skills (one `<name>/SKILL.md` each).
- `agents/` — agent definitions (flat `<name>.md`).
- `hooks/` — hook scripts.
- `rules/` — path-scoped coding policies.
- Neutral roots: `workflow/`, `templates/`, `standards/`, `skill_testing/`,
  `docs/`, `adapters/`.

## Declared runtimes

| Runtime | Label | Notes |
|---|---|---|
| `claude` | Claude Code | First-class. Native path-glob rules (`.claude/rules/`). |
| `codex` | Codex | First-class. No path-glob equivalent; consults canonical `rules/` via guidance. |

Codex's native `.codex/rules/*.rules` command-approval policy is runtime-owned
and never generator-owned.

## Generated outputs (NEVER hand-edit)

Each canonical source projects to its declared runtime `targets`:

- Root instructions → `CLAUDE.md` + `AGENTS.md`.
- Nested instructions → `src/`/`design/`/`docs/` `CLAUDE.md` + `AGENTS.md`.
- skills → `.claude/skills/` + `.agents/skills/`.
- agents → `.claude/agents/` (Markdown) + `.codex/agents/` (TOML).
- hooks → `.claude/hooks/` + `.codex/hooks/`.
- rules → `.claude/rules/` (Claude only).

## Mixed-ownership roots

`.claude/` and `.codex/` are mixed-ownership: they contain the generated subtrees
above AND hand-authored runtime config (`.claude/settings.json`,
`.claude/statusline.sh`, `.codex/hooks.json`) which the generator never owns.

## Check and regeneration commands

```bash
python scripts/sync_adapters.py --check            # fail if any adapter is stale
python scripts/sync_adapters.py --write            # regenerate every adapter
python scripts/sync_adapters.py --write --class X  # regenerate one class
python scripts/workflow_consistency.py             # boundary + freshness contracts
```

`adapter_state.yaml` is reserved for recorded freshness state but ships
uninitialized. Its `/constitute` and `/constitute-check` lifecycle automation is
planned, not yet implemented; until then, the `--check` result above is the live
freshness evidence.
