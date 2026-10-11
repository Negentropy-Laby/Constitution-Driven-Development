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
- A target separately reviews required local inputs and its Git candidates,
  following `adapters/README.md`. Required templates/specs and generic standards/
  workflow originals remain readable local-only inputs. Its CDD Git candidates
  contain only required platform adaptations and portable project configuration.
  General root `agents/` and `skills/` remain owned by the designated Source and
  are excluded from Target Git submission/publication regardless of local placement.
- Retain exact before bytes and project customizations for any existing target.

## 2. Delivery Validation

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
- Required local originals remain readable even when ignored in the Target. Git
  tracking is not a prerequisite for these reads; a fresh Target clone may need
  their separate local installation before affected workflows can run.
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
- Import/update uses the unique designated Source, an independently reviewed
  delivery allowlist and recoverable before bytes.
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
