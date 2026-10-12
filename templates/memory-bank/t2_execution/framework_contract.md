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
- **Installed CDD paths:** [exact approved local-use files/references; Git eligibility separate]
- **Required local neutral inputs:** [reviewed per-file local-input allowlist and required closure]
- **Project customizations:** [existing differences; developer overlays stay local-only]
- **Instruction purpose:** [existing scoped review: product-use / development-only / mixed / unresolved]

Reuse the project's established portable configuration and decisions. Keep
unknown bindings unconfigured; do not invent pins or add host-specific paths.
An unavailable Source does not prevent authorized offline use of complete
installed entries and their required inputs. Missing required installed originals
leave only their affected workflow pending.

## Authority contract

For a consumer, installed platform paths and approved neutral inputs are the
normal-use readers. Required local inputs do not gain Target Git eligibility:
reusable templates, generic standards/workflow originals and testing definitions
remain local-only. Review CDD candidates separately, retaining minimal required
adaptations and independent configuration without development-instruction bodies/exclusive support.
Qualified product-use skills are separate project product assets.

**Classify instruction purpose first.** Apply `standards/skill-purpose.md` to
skills, agent/role definitions, native configuration containing instructions and
equivalent templates with their complete reference/support closure. In a Target,
content used only to develop this project is a local-only template, excluded from
Git tracking/staging/commits/publication: requirements, design, coding, code review,
development verification and release/maintenance. This includes independent roles
and `developer_instructions` bodies without any skill dependency. Project-specific
names/paths/prompts/overlays, TOML/native loading, platform directories and complete
projections give no exception. Exclusive development support follows the body.
Minimal adaptations/configuration must not carry or reconstruct it; independent
configuration needs real readers independent of development instructions/role packages,
not merely a native agent loader. Split mixed bodies/dependencies before submission.
Product-use skills or agents call this project's delivered functions for user tasks
and may be product capabilities under project rules. Names/fields such as test,
release or developer_instructions do not decide purpose. Unknown content remains
pending. Preserve complete required local development inputs separately from Git.
The designated CDD Source owns general root `skills/` and
`agents/`. Exclude general source mirrors and template-maintenance tools from
project Git submission/publication; local storage inside or outside the project
is allowed and grants no Source authority or move/delete/log-path authority.
Common CDD updates require the actual Source,
a separately approved isolated update stage and independent review of exact
update-write paths and the required local-input allowlist. Review Git submission
candidates separately; required reads and approved writes are not Git eligibility.
Preserve project customizations, runtime-owned settings, business documents and
recoverable before bytes; conflicts stop affected updates.

**Existing tracked neutral inputs.** When a boundary change affects reusable
neutral template/standard/workflow/spec originals or development-instruction packages
already tracked under earlier
guidance, record reconciliation as pending until the applicable governance gate
closes. Earlier tracking is neither automatically grandfathered as compliant nor
judged a violation under an unaccepted rule. Keep local originals and Git history.
After acceptance or a valid scoped exception under existing governance, obtain
separate exact-path project migration authority before removing reviewed reusable
originals or development-only skill/support content from Git tracking. Retain their local files, required-reference closure,
project customizations and recoverable before bytes; review the actual index/diff
and separately eligible Git candidates. Commit/publication still require their
own authority. This differs from already-tracked maintenance content and grants
no untracking, deletion, relocation or migration authority by itself.

The designated CDD Source owns the canonical-to-platform mapping.
Canonical `INSTRUCTIONS.md`, `skills/`, `agents/`, `hooks/` and `rules/`
belong to that Source. Source reproduction and generation have separate
maintenance authority and are not prerequisites for ordinary consumer use.
Locally installed templates, generic standards, workflow views and reusable
`skill_testing/` assets are neutral local-use inputs excluded from Target Git
submission/publication, not another general skill/agent source tree. A fresh
Target checkout may need neutral originals and complete local-only development
packages/references installed separately for affected use.

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

Skills project verbatim to Claude. Codex uses the Accepted `runtime_substitute`
contract's Source-declared literal pairs: blind deterministic substitution, not
contextual rewriting. ADR-0002 D2's guard rejects a repeated token across
`and`/`or`/`,` only when the token contains a replacement target; residual
forbidden source literals also fail. These limits do not imply equivalent native
capabilities. Agent Markdown projects to Claude; Codex TOML retains `name`,
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
