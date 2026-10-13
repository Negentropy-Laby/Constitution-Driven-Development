# Upgrading Constitution Driven Development

This guide explains how to update an existing project to the current CDD
template contract without overwriting project-owned design, architecture, code,
or production artifacts.

## Current Template Contract

The current template uses `/constitute` as the unified onboarding and governance
entry point. Historical templates may mention `/start`; treat that as a legacy
entry name and use `/constitute` for current projects.

The authoritative workflow source is `workflow/workflow-catalog.yaml`.
Required progression blockers come from catalog steps marked `required: true`.
`/gate-check` may add quality and risk checks, but it should not turn optional
or later-phase artifacts into default blockers unless the issue directly breaks
the current phase goal.

Gate policy is governed advisory:

- Gates must run before normal phase advancement.
- `FAIL` does not update `production/stage.txt`.
- Users may override, but must record a risk note.
- `CONCERNS` may advance only with the risk noted.

## Canonical Paths

Use these paths for new and upgraded projects:

| Artifact type | Current path |
| --- | --- |
| CDDs | `design/cdd/` |
| Architecture | `docs/architecture/architecture.md` |
| ADRs | `docs/architecture/adr-*.md` |
| Control manifest | `docs/architecture/control-manifest.md` |
| Accessibility requirements | `design/accessibility-requirements.md` |
| Epics and stories | `production/epics/[epic-slug]/` |
| Automated evidence | `production/qa/evidence/automated/` |
| Manual evidence | `production/qa/evidence/manual/` |
| Game playtests | `production/qa/evidence/playtests/` |
| Product user tests | `production/qa/evidence/user-tests/` |
| Smoke evidence | `production/qa/evidence/smoke/` |
| Release evidence | `production/qa/evidence/release/` |

Do not create new artifacts in retired evidence directories. Preserve historical
originals and link them from the appropriate QA index; migrate active evidence
only within an approved recoverable scope.

## Art Bible Status

`/art-bible` is a Concept-phase optional skill for game projects. It is not a
Technical Setup required step and is not a default Technical Setup gate blocker.

Use it when visual identity, public brand, art direction, or content production
needs a formal source of truth. Product projects should use the product branch
inside the same skill when brand/style guidance is needed; API-only, CLI-only,
SDK/library, and internal headless projects may record it as not applicable.

## Upgrade Procedure

1. Record the exact current revision and retain recoverable before bytes. Use a
   short-lived branch if the project's trunk-based policy calls for one.
2. Verify the sole CDD Source and establish actual provenance, ownership and delivery
   role for complete packages and their required support. Apply `standards/skill-purpose.md`
   only within the confirmed CDD asset collection, then select Git candidates separately
   from local inputs in `adapters/README.md`. Project-owned development skills, roles,
   tools, configuration and documents remain governed by project rules. CDD instruction
   bodies, projections, exclusive references/overlays, reusable templates/specs and
   generic standards/workflow originals stay outside Target Git tracking, staging,
   commits and delivery/publication while remaining available for authorized local use.
   Renaming, tailoring or native packaging does not change CDD ownership. Do not add
   general CDD `agents/` or `skills/` mirrors to the Target Git delivery set.
3. Preserve project-owned artifacts under `design/`, `docs/architecture/`,
   `production/`, `prototypes/`, `src/`, and `tests/`, including actual test roots,
   valid customizations, production configuration and historical evidence. Preserve
   project-owned skills, roles, tools and configuration wherever they are stored.
4. Run `/project-stage-detect` to determine the current phase.
5. Run `/adopt` if the project already has CDDs, ADRs, epics, stories, or
   sprint artifacts.
6. Run `/help` to get the next required step from the workflow catalog.
7. Run `/gate-check` for the detected phase before normal advancement.

Prefer additive migration over replacement. If a local file has project
decisions, merge the new template structure into it rather than overwriting it.

## Common Migration Fixes

### Platform adapters and project configuration

**Confirm asset ownership before instruction purpose.** First establish actual CDD
framework provenance, ownership and delivery role for the complete package and its
required support. Apply instruction-purpose classification only within that confirmed
CDD asset collection. Project-owned skills, agents/roles, tools, configuration and
documents follow their project's rules; development use, native instruction fields
and skill-directory placement do not make them CDD assets. Renaming or tailoring a
CDD template does not itself change its ownership. Unresolved ownership stays pending.

**Target Git separation preserves authorized local use.** CDD framework assets and
maintenance tools are excluded from Target Git tracking, staging, commits and delivery/
publication contents. This does not prohibit their authorized local retention,
discovery, loading, effect or use. Keep complete required inputs at usable paths.
Ordinary template use must not depend on the local maintenance toolkit. Ignore and
runtime loading are separate; existing tracked content requires separately authorized,
recoverable tracking-only migration that leaves local files and required references intact.

Within confirmed CDD packages, independent portable configuration must neither carry
nor reconstruct CDD instruction bodies or exclusive support, and must have substantive
readers independent of those packages. A native loader alone does not qualify.

A consuming project keeps its approved platform adapters, required local CDD inputs
and project-owned configuration. Only minimal required bindings and independent
portable configuration that neither carry nor reconstruct CDD instruction bodies or
exclusive support enter its CDD-related Git candidates. Project-owned development
skills, roles and product-use capabilities retain project rules. Within confirmed
CDD packages, development instruction bodies and exclusive support remain excluded
from Target Git even when tailored or projected; split them from project-owned
candidates in mixed packages. Required CDD templates/specs and generic standards/
workflow originals remain available locally. The designated Source delivers its
developer templates and complete projections as framework product assets, excluding
maintenance tools and records; a Target copy gains no Source authority. General CDD
source mirrors and template-maintenance tools stay outside Target Git delivery.
Local copies may remain inside or outside the repository and be discovered, loaded,
take effect and be used under existing authorization. The boundary does not require
moving them or changing log locations. Back up complete project customizations and
review the exact changed delivery before applying an authorized update.

Ignore rules prevent accidental addition of untracked content; they do not remove
tracked/staged content or prevent forced addition or separate publication. Existing
tracked CDD content needs the applicable governance gate and separate exact-path,
recoverable tracking-only migration authority. Preserve actual local files, required
references, project customizations, before bytes and Git history. Project-owned
assets must not be selected for CDD untracking solely because they support development.
An upgrade supplies no automatic untracking, move/delete, commit or publication authority.

Preserve target-owned policies and runtime settings. Codex native
`.codex/rules/*.rules` command-approval files are independent of CDD path policies.
Changed business hooks follow the runtime's actual trust requirements and separate
activation authority; an upgrade does not enable a maintenance hook.

### v0.2 adapter freshness state

1. Read the installed `/constitute` entry and its required neutral originals.
   Initialize T2 only within covered project-write authority; retain existing
   project-owned memory files.
2. Bind `framework_contract.md` to the actual installed paths and unique designated
   Source. `adapter_state.yaml` starts uninitialized; file reads alone are not
   Source freshness evidence.
3. Run `/constitute-check`. Ordinary installed-file observations work without
   maintenance tools. A live Source check requires the actual Source and a
   valid applicable read-only comparison; unavailable checks retain the last
   recorded state and are reported unavailable, never fresh.
4. Review the complete state draft and permit only covered writes. `/cdd-status`
   reads recorded state and does not run generation or impose a new phase gate.

### Runtime-native skill invocation

CDD documentation retains `/skill-name` as its runtime-neutral logical command
notation. Claude Code invokes that form directly. In Codex, use `/skills` to
browse or `$skill-name` for explicit invocation, including in `codex exec`.

### Old entry command

If project notes mention `/start`, replace the operational instruction with
`/constitute`. Keep historical notes only if they are clearly labeled as legacy.

### Story files

Move new story work to:

```text
production/epics/[epic-slug]/story-NNN-[slug].md
```

If an older project has a separate story directory, leave a short migration note
and move active stories under their owning epic.

### Evidence files

Create new evidence in the canonical QA evidence schema. Keep historical
originals recoverable and index their existing paths; any active migration needs
its own exact approved scope:

```text
production/qa/evidence/automated/
production/qa/evidence/manual/
production/qa/evidence/playtests/
production/qa/evidence/user-tests/
production/qa/evidence/smoke/
production/qa/evidence/release/
```

### Technical Setup

The current Technical Setup baseline is:

```text
/setup-engine
/create-architecture
/architecture-decision
/architecture-review
/create-control-manifest
create design/accessibility-requirements.md
/test-setup
/gate-check technical-setup
```

`/test-setup` must create the baseline test directories, CI test workflow, and
one runnable example test. `/test-helpers` remains optional.

### Release

The current Release chain is:

```text
/release-checklist
/launch-checklist
/team-release
```

Run the Polish / Verification gate before entering Release. Do not require a
second phase gate between release checklist and launch checklist unless the
project explicitly opts into a stricter local policy.

## Validation After Upgrade

Run `git diff --check`, then read back every installed path in the approved
allowlist and its required reference closure. Compare actual bytes and project
differences with the reviewed Source inputs. Check T0/T2 agreement, installed
workflow/catalog mirrors, configured language/runtime/testing facts, and preserved
business/design/QA history.

In an isolated target, verify initialization, additive adoption, setup and an
incremental update while retaining project customizations. Run the project's real
test commands where configured; required failures or unavailable checks remain
unresolved. Preserve evidence of what actually ran, distinguishing file-level
simulation from live agent execution.

Source generators and maintenance checks are local-only and supplied separately.
Use them only when available and authorized; their absence is not an ordinary
installed-use dependency. Do not add general Source mirrors or maintenance tools
to target Git delivery to make an upgrade appear complete. Sync project documentation after
meaningful batches or at the user's request, while retaining required decision
and safety checks; do not add a per-code-baseline synchronization gate.

## Legacy Migration Notes

Older templates may use different entry names, evidence directories, or phase
labels. Treat those notes as historical context only. The current catalog,
START-HERE, quick-start, Workflow Guide, and `/gate-check` skill define the
active contract.
