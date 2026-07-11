# ADR-0001: Canonical authority sources and generated runtime adapters

- **Status:** Accepted
- **Date:** 2026-07-10
- **Baseline:** `main` @ `43082d4`

> **Superseded in part by [ADR-0002](adr-0002-runtime-parity-and-adapter-governance.md)**
> (2026-07-11): runtime parity (Codex becomes first-class), manifest-declared
> runtimes/targets, canonicalized rules and nested instructions, the
> semantic-collapse guard, and mixed-runtime-root ownership are extended by
> ADR-0002. This ADR's core canonical→generated decision and its rejection of
> fully tokenized prose remain valid.

## Context

CDD supports multiple agent runtimes (Claude Code primary, Codex secondary). Until
this decision, the same authority content was duplicated across hand-maintained
runtime trees and CI only *checked* that the copies agreed — no generator produced
them. Four asset classes were duplicated this way:

| Class | Claude surface | Codex surface |
|---|---|---|
| Skills (74) | `.claude/skills/<n>/SKILL.md` | `.agents/skills/<n>/SKILL.md` |
| Agents (53) | `.claude/agents/<n>.md` | `.codex/agents/<n>.toml` |
| Hooks (12) | `.claude/hooks/<n>.sh` | `.codex/hooks/<n>.sh` |
| Root instructions | `CLAUDE.md` | `AGENTS.md` |

`scripts/workflow_consistency.py` hardcoded `.claude/` as the source of truth and
the duplicated trees were kept in step by hand (recent history shows both skill
trees edited in the same commit). Drift risk is structural: an edit to one runtime
tree can ship without its counterpart, and the Codex agent TOMLs had already
accumulated literal `\r` escape pollution (49 of 53 files) and inconsistent
quoting because no canonical serialization defined them.

## Decision

Establish one committed **canonical** source per asset class and deterministically
**generate** every runtime adapter from it:

```
canonical source (skills/, agents/, hooks/, INSTRUCTIONS.md)
    └── cdd-manifest.toml + scripts/sync_adapters.py
            ├── Claude runtime adapters (.claude/..., CLAUDE.md)
            └── Codex runtime adapters  (.agents/..., .codex/..., AGENTS.md)
```

Specifically:

1. **Canonical roots** are hand-authored: `skills/`, `agents/`, `hooks/`,
   `INSTRUCTIONS.md`. Initial canonical text is copied verbatim from the current
   Claude assets (Codex wording remains a deterministic transform, not a claim of
   runtime-neutral prose).
2. **Generated outputs** (`.claude/skills`, `.agents/skills`, `.claude/agents`,
   `.codex/agents`, `.claude/hooks`, `.codex/hooks`, `CLAUDE.md`, `AGENTS.md`)
   stay committed for clone-and-use behavior and are **never hand-edited** after
   cutover. `python scripts/sync_adapters.py --write` regenerates them; `--check`
   fails CI on drift.
3. **`cdd-manifest.toml`** is the single source/output/transform/ownership
   contract, read by both the generator and `workflow_consistency.py`. TOML is
   used (not YAML) because the unconditional `tomllib` import already makes Python
   3.11 the effective minimum, giving a strict standard-library parser with no
   new dependency.
4. **Managed-tree ownership**: each `owns_tree = true` destination must contain
   exactly the generated file set — `EXTRA`/orphan files fail CI. Root files
   (`CLAUDE.md`, `AGENTS.md`) are individually owned; their parent is never pruned.
5. **Freshness is exact UTF-8/LF bytes plus a 0644 mode contract** — not
   newline-normalized text — so CRLF churn and executable-bit drift are caught.
6. **Full preflight before mutation**: the generator renders every output in
   memory and validates it before any file is written or pruned; writes are
   per-file atomic (`tempfile` + `fsync` + `os.replace`). A typo'd `expected_count`
   or empty glob can therefore never erase usable adapters.
7. **Codex agent metadata loss is intentional**: `agent_md_to_toml` retains only
   `name`, `description`, `developer_instructions` and drops `tools`, `model`,
   `maxTurns`, `memory`, `skills`, `disallowedTools`, `isolation` (Codex's agent
   schema carries no equivalents). Unknown future frontmatter fields **block**
   generation rather than being silently lost. The canonical `agents/*.md` keeps
   the full frontmatter as canonical metadata.

## Alternatives considered

- **Keep manual parity checks (status quo).** Rejected: drift is structural and
  had already produced real corruption (`\r` pollution, inconsistent quoting).
- **Symlinks from runtime trees to canonical roots.** Rejected: cross-platform
  (Windows) and runtime-discovery semantics make symlinks unreliable, and runtimes
  expect real files at the adapter paths.
- **Untracked generated adapters (build on clone).** Rejected: regresses the
  template's clone-and-use UX; every user would need a build step before skills
  exist.
- **Fully tokenized, runtime-neutral source prose** (e.g. `{{ROOT_INSTRUCTIONS}}`
  placeholders). Rejected for now: adds templating syntax to source files and a
  substitution surface for little gain, given Codex's agent schema already cannot
  represent the full Claude frontmatter. Tokenization can be revisited if a third
  runtime with different wording needs is added.

## Consequences

- **Contributors** author only canonical roots, then run
  `python scripts/sync_adapters.py --write` (class-scoped or all). The
  authoring-path cutover (Gate 5) updates `skill-improve`, `skill-test`,
  `setup-engine`, `godot-specialist`, and `validate-skill-change.sh` so no
  supported workflow directs edits at a generated file.
- **Validators** (Gate 6) read canonical roots for semantic checks and generated
  outputs for runtime checks; duplicated Claude/Codex semantic loops are removed.
- **Downstream template users** see no behavior change at clone time; generated
  trees are present and identical in spirit to before. The 49 Codex TOMLs gain a
  one-time, reviewed normalization (literal `\r` escape removal + consistent
  quoting).
- **CI** gains a `sync_adapters.py --check` step and a Python 3.11 baseline.

## Rollback / compatibility

- Generated adapters remain usable until the read-only golden comparison passes,
  so the migration can be aborted before the authoring cutover with no loss.
- The manifest never reads from a destination, so rollback cannot create a
  self-fed authority loop.
- A failed/invalid preflight performs zero writes and zero pruning.
- After cutover, deterministic regeneration plus Git history restore generated
  outputs; no destructive `git checkout` is built into the generator.
