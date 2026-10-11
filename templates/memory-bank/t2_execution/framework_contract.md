# Framework Contract

This file binds the project's installed CDD platform files and required neutral
inputs to their sole CDD Source. It indexes framework ownership separately from
project-specific laws in T0 and axioms in T1. Installed-file observations,
Source comparison, runtime execution and law acceptance remain distinct facts.

## Project and Source binding

- **Project role:** [consumer / CDD Source library / Unknown; actual evidence]
- **Sole CDD Source:** [portable repository identity/locator / unconfigured]
- **Installed Source revision:** [verified revision/pin / unknown]
- **Selected runtime:** [actual installed runtime / unconfigured]
- **Installed CDD paths:** [exact approved platform files and their references]
- **Required neutral inputs:** [reviewed per-file allowlist and required closure]
- **Project customizations:** [existing project-owned differences/configuration]

Reuse the project's established portable configuration and decisions. Keep
unknown bindings unconfigured; do not invent pins or add host-specific paths.
An unavailable Source does not prevent authorized offline use of complete
installed entries and their required inputs. Missing required installed originals
leave only their affected workflow pending.

## Authority contract

For a consumer, installed platform paths and approved neutral inputs are the
normal-use readers. The designated CDD Source owns general root `skills/` and
`agents/`. Exclude general source mirrors and template-maintenance tools from
project Git submission/publication; local storage inside or outside the project
is allowed and grants no Source authority or move/delete/log-path authority.
Common CDD updates require the actual Source,
a separately approved isolated update stage and independent review of the exact
delivery allowlist. Preserve project customizations, runtime-owned settings,
business documents and recoverable before bytes; conflicts stop affected updates.

The designated CDD Source owns the canonical-to-platform mapping. Canonical `INSTRUCTIONS.md`, `skills/`, `agents/`, `hooks/` and `rules/`
belong to that Source. Source reproduction and generation have separate
maintenance authority and are not prerequisites for ordinary consumer use.
Delivered templates, standards, workflow views and reusable `skill_testing/`
assets are neutral support, not another general skill/agent source tree.

## Installed platform ownership

Record the actual selected paths above; the following mappings describe the
Source contract and do not require both runtimes in every consumer:

| Runtime | Platform readers | Rules |
|---|---|---|
| `claude` | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/`, approved `.claude/hooks/` | `.claude/rules/` path-glob projections |
| `codex` | `AGENTS.md`, `.agents/skills/`, `.codex/agents/`, approved `.codex/hooks/` | Read delivered `rules/` manually; `.codex/rules/*.rules` is runtime-owned |

Nested project guidance may supply the corresponding `src/`, `design/` and
`docs/` instruction files where needed. `.claude/` and `.codex/` are
mixed-ownership roots: settings, status-line configuration, hook wiring and
native command policies remain with their actual owners. Installed adapters
do not authorize hook activation or overwrite project-specific configuration.

Skills project verbatim to Claude and by platform-specific wording to
Codex. Agent Markdown projects to Claude; Codex TOML retains `name`,
`description` and `developer_instructions`, not all operational metadata.
Read `adapters/README.md` and actual runtime metadata before behavior claims.
No copied definition establishes autoload, execution or qualification.

## Recorded and live state

`/constitute` copies `adapter_state.yaml` as the deterministic `uninitialized`
template. It does not fabricate digests, a commit, timestamp or check result.
`/constitute-check` observes installed files read-only and reports live freshness
as unavailable when the exact Source/comparison evidence is unavailable.
Source-only freshness does not establish that a consumer's installed allowlist
matches Source plus its approved customizations.

Only a valid comparison covering the actual checked owner/inputs can support a
fresh/stale record. After presenting that live result and complete YAML draft,
`/constitute-check` may write the exact state file within matching approval.
Unavailable/invalid checks preserve the previous state, including uninitialized.
`/cdd-status` reads the historical record and never owns or recomputes it.
Linked neutral inputs need their own exact identities; Source digests cover only
the manifest-declared classes. Neither freshness nor a state write accepts laws,
publishes evidence or completes a workflow.
