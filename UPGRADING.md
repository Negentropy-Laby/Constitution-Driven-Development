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
2. Verify the unique designated Source and independently review the
   exact platform/configuration and necessary neutral-support delivery allowlist
   from `adapters/README.md`. Do not add general root `agents/` or `skills/`
   mirrors to the target Git submission/publication set.
3. Preserve project-owned artifacts under `design/`, `docs/architecture/`,
   `production/`, `prototypes/`, `src/`, and `tests/`, including actual test roots,
   valid customizations, production configuration and historical evidence.
4. Run `/project-stage-detect` to determine the current phase.
5. Run `/adopt` if the project already has CDDs, ADRs, epics, stories, or
   sprint artifacts.
6. Run `/help` to get the next required step from the workflow catalog.
7. Run `/gate-check` for the detected phase before normal advancement.

Prefer additive migration over replacement. If a local file has project
decisions, merge the new template structure into it rather than overwriting it.

## Common Migration Fixes

### Platform adapters and project configuration

A consuming project keeps its approved platform adapters, neutral inputs and
project-specific configuration. The designated Source owns general CDD definitions;
exclude general source mirrors and template-maintenance tools from target Git
submission/publication. Local copies may remain inside or outside the repository;
the boundary does not require moving them or changing log locations. Back up complete project customizations and
review the exact changed delivery before applying an authorized update.

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
