# Customer Acceptance Checklist

Use this page to review a clean template delivery and its intended installed
workflow. Bind the exact delivery revision, scope and observed results before
acceptance; file presence or a static walkthrough does not prove live execution.

## 1. Repository Setup

```bash
git clone https://github.com/Negentropy-Laby/Constitution-Driven-Development.git cdd-source
cd cdd-source
git rev-parse HEAD
git diff --check
```

Expected result:
- The Source-library checkout opens without missing submodules or bootstrap steps.
- Git and the selected AI agent runtime are available. Python is needed only
  for separately supplied, authorized local maintenance diagnostics.
- A Target establishes actual CDD provenance, ownership and delivery role for complete
  packages and support before applying `standards/skill-purpose.md` within that
  confirmed collection. Project-owned development skills, roles, tools, configuration
  and documents retain project rules. Review required local inputs separately from
  Git candidates, following `adapters/README.md`. Required CDD templates/specs,
  generic standards/workflow originals, instruction bodies, complete projections
  and exclusive support stay outside Target Git tracking, staging, commits and
  delivery/publication while remaining available for authorized local use. Minimal
  CDD bindings and independent configuration must neither carry nor reconstruct
  framework instruction bodies or exclusive support. Renaming or tailoring CDD
  content does not change its ownership; split confirmed CDD content/support from
  project-owned candidates in mixed packages. General CDD `agents/` and `skills/`
  definitions remain owned by the designated Source regardless of local placement.
  Source developer templates and complete projections remain its framework product assets.
- Retain exact before bytes and project customizations for any existing Target.
  Ignore does not remove existing tracking; any tracked CDD migration needs the
  applicable governance gate and separate exact-path, recoverable tracking-only
  authority that preserves local files, required references and Git history.

## 2. Delivery Validation

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

Read the installed skill entry and its required references for each reviewed
workflow. For initialization this includes `templates/memory-bank/`,
`templates/game-concept.md` or `templates/product-concept.md` for the chosen
domain, `workflow/workflow-catalog.yaml`, `docs/PHASE-CHECKLISTS.md`,
`workflow/generated/gate-required-artifacts.md`, and the required standards,
instruction and `skill_testing/` originals described in `adapters/README.md`.
Use the actual entry's input closure; a same-name template does not replace a
missing governing project original.

Expected result:
- Required installed originals exist and their complete contents can be read.
  Missing required inputs leave affected use Pending or Incomplete.
- Platform entries and required resources correspond to the reviewed Source
  revision and retain approved project differences.
- T0 boundaries and T2 installed-path/external-Source contracts agree.
- Ownership review establishes actual provenance, ownership and delivery role before
  purpose review within the confirmed CDD collection. That review covers the actual
  product/function/task, complete bodies/effects and exclusive/shared references.
  Names, project paths and test/release labels alone establish neither CDD ownership
  nor product-use; CDD-related independent configuration needs substantive readers
  independent of framework instruction packages. Project-owned development assets
  are not classified as CDD merely because of their development use.
- Required local CDD originals and instruction packages remain complete and usable
  even when ignored in the Target. Git tracking is not a prerequisite for authorized
  retention, discovery, loading, effect or use; ignore rules are not runtime controls.
  A fresh Target clone may need their separate local installation before affected
  workflows can run.
- Ordinary use and T2 mirror synchronization work from the installed local files
  without maintenance scripts, credentials, local locks or host-path records.
- `git diff --check` reports no whitespace errors.
- In a configured project, run its actual test/QA commands and preserve exact
  Story evidence, runner output, configuration and outstanding failures.
  Source diagnostics are not substitutes for project tests.

Separately supplied maintenance diagnostics may provide extra checks when
authorized and available. Their absence is not a normal-use prerequisite;
record any unavailable diagnostic as NotRun instead of fabricating a PASS.

## 3. Release Evidence

Use the actual release and QA contract for the delivery under review. Preserve
the revision, exact inputs, applicable test/CI results, runtime versions and
unresolved checks. A required FAIL, Blocked or NotRun remains unresolved unless
the owning policy has a valid scoped exception; it never becomes PASS by wording.

Historical `Template Consistency` evidence covers its identified Ubuntu, macOS
and Windows jobs. Historical `Runtime Contract` evidence covers its identified
credential-free CLI checks, not live model behavior. If such evidence is cited,
verify its run ID, job results and `headSha` against the exact historical release
commit. Neither workflow is promised by the current clean template delivery.
New delivery results must be collected for the new exact inputs; an old successful
run cannot certify changed or uncommitted bytes.

## 4. New Project Smoke Path

Use a fresh isolated target and its reviewed installation. With an available
configured runtime, invoke:

```text
Claude Code: /constitute -> /help -> /cdd-status --dry-run
Codex:      $constitute -> $help -> $cdd-status --dry-run
```

Expected result:
- `/constitute` presents governing principles and the exact project write scope.
  Concept agreement and file writes do not independently ratify Proposed laws.
- `/help` selects the next catalog step using the actual Game or Product scope,
  including populated legacy Product configuration without a concept.
- `/cdd-status --dry-run` produces a roadmap draft without writing files.
- The draft follows `docs/examples/project-roadmap.example.md`.
- Installed-file reads continue offline; unavailable external Source checks stay
  unavailable and do not cause a second general CDD source to be installed.

Report file-level materialization, instruction reasoning and actual interactive
runtime execution separately. If no live runtime was used, mark that trial NotRun.

## 5. Brownfield Smoke Path

In a fresh isolated copy containing representative existing source, tests,
design and architecture, invoke:

```text
/project-stage-detect
/adopt
```

Expected result:
- The current stage is assessed from substantive artifacts and actual configuration.
- Required migration work is scoped without inventing completed evidence.
- Existing project code, design, configuration, test roots, valid customizations
  and historical evidence are preserved.
- Import/update uses the unique designated Source, reviewed exact update-write
  paths and required local-input allowlist, separately classified Git submission
  candidates and recoverable before bytes.
- Apply `standards/directory-structure.md`, section "Consumer layout resolution
  for imports and updates": the plan identifies the verified latest applicable
  Source inputs, resolved consumer tree and reasoned old-to-new mapping. An old
  layout receives no automatic exemption merely because its internal checks pass.
- Compare the resulting installation with that target, including current readers,
  discovery/configuration, required offline references and generation/comparison
  chain. Preserve substantive contents and valid changes through migration;
  preserving them does not require preserving their old paths.
- Historical evidence retains its actual old-path identity and recovery witness
  without masquerading as an active dependency. Covered old-path retirement waits
  for migrated active dependencies, passed applicable checks and verified recovery.
  Unresolved layout/ownership/conflicts remain pending for their affected scope;
  neither guesses nor copied Source trees establish conformance.
- Memory Bank initialization, hook activation and project writes need their
  own covered effects; a review does not authorize them.

## 6. Workflow Surface Checks

Review these customer-visible entry points:
- `README.md`
- `docs/START-HERE.md`
- `docs/USER-MANUAL.md`
- `docs/WORKFLOW-GUIDE.md`
- `docs/QUICK-START.md`
- `docs/reference/skills-reference.md`
- `SUPPORT.md`
- `RELEASE_NOTES.md`

Expected result:
- Current setup, use, upgrade and acceptance do not require unshipped local tools
  or historical Source CI.
- Runtime documentation distinguishes Claude `/skill` from Codex `/skills`
  browsing and `$skill` invocation.
- README links to the stable release; counts are checked against actual assets.
- Release order is `/release-checklist` -> `/launch-checklist` -> `/team-release`.
- Product surface N/A decisions identify an owner and reason in
  `design/ux/surface-profile.md`; actual Game/UI requirements remain applicable.

## 7. Known Limits To Accept Explicitly

- This repository supplies development templates and necessary usage guidance.
- Missing future project outputs differ from missing required input originals.
- `/skill-test static all` is an instruction workflow; reasoning through specs,
  executing fixtures and running a live agent are distinct evidence.
- Gates retain the owning workflow's required checks and scoped override rules.
- Local maintenance tools and process records are supplied separately and excluded
  from delivery. Their existence does not establish runtime support or freshness.
