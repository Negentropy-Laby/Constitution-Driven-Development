---
name: constitute-check
description: "Memory-bank governance audit — checks whether T0 laws/current state, T1 supporting context, T2 execution mirrors, adapter freshness, and T3 archive indexes align. Read-only by default; may record adapter_state.yaml only after explicit approval."
argument-hint: "[optional: 'full' for verbose report, or a specific principle number]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Write, AskUserQuestion
model: haiku
context: |
  !echo "=== Memory Bank Status ===" && echo "T0: $(ls memory_bank/t0_core/ 2>/dev/null | wc -l) files" && echo "T1: $(ls memory_bank/t1_axioms/ 2>/dev/null | wc -l) files" && echo "T2: $(ls memory_bank/t2_execution/ 2>/dev/null | wc -l) files" && echo "T3: $(ls memory_bank/t3_archive/ 2>/dev/null | wc -l) files" && echo "Review mode: $(cat production/review-mode.txt 2>/dev/null || echo 'not set')"
---

## User Guide

- When to use: Memory-bank governance audit — checks whether T0 laws/current state, T1 supporting context, T2 execution mirrors, adapter freshness, and T3 archive indexes align. The audit is read-only by default.
- Inputs: Command arguments: `/constitute-check [optional: 'full' for verbose report, or a specific principle number]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: A T0-T3 health report plus live and recorded adapter freshness. Write only the approved adapter-state record described below.
- Memory-bank writes: At most `memory_bank/t2_execution/adapter_state.yaml`, and only after showing the exact YAML draft and receiving explicit approval. No other file may be written.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

## Purpose before Governance Audit

**Confirm asset ownership before instruction purpose.** Apply
`standards/skill-purpose.md` after establishing actual CDD framework provenance,
ownership and delivery role for the complete package and its required support.
Classify purpose only within that confirmed CDD asset collection. Project-owned
skills, agents/roles, tools, configuration and documents follow their project's
rules, including development capabilities; development use, native instruction
fields and skill-directory placement do not make them CDD assets. Renaming or
tailoring a CDD template does not itself change its ownership. Unresolved ownership
stays pending only for the affected action.

Confirmed CDD developer templates, full platform projections and exclusive support
remain local-only in a Target, excluded from Git tracking/staging/commits/delivery/
publication. Within that CDD collection, inspect complete bodies, conditional
branches and direct/indirect support; split mixed CDD/project content before
submission. Native `developer_instructions` fields and standalone roles receive
the same ownership review even without a skill dependency. Minimal adaptations
and independent configuration must not carry or reconstruct CDD framework
instruction bodies or exclusive support; a native loader alone does not qualify
a copied CDD role as independent configuration. This CDD-related restriction does
not exclude independently established project-owned development skills or roles.
Names/fields such as test or release do not decide ownership or purpose.

Git exclusion does not disable authorized local retention, discovery, loading,
effect or use. Preserve complete required local CDD inputs at usable paths; an
input allowlist does not grant them Git eligibility. Missing/unread required
originals leave the affected CDD workflow pending. A fresh Target clone may need
those inputs provisioned separately. Review Git candidates separately from local
inputs and update-write scope. Ordinary template use must not depend on a local
maintenance toolkit, reader, lock, live Source or Source ADR reader; optional
authorized local maintenance operations remain allowed.

Do not submit a general CDD source mirror, template-maintenance tools/annotations,
tool-only metadata, maintenance locks/caches or actual template-maintenance output.
The designated CDD Source owns general CDD definitions independently of local
storage. Local copies alone do not establish Source authority or authorize moving,
deleting or changing log paths.

Identify the actual project and whether the request uses its delivered functions
or develops/governs it before domain/audit routing. This CDD governance audit is a
local-only Target development template; complete platform copies, bespoke prompts
and exclusive framework overlays do not change its CDD ownership. Source delivers
its templates/projections as framework product assets. Independent product-use
tasks use their real capabilities, without requiring a Memory Bank. Ownership/
purpose review and Git eligibility remain separate from freshness and authorized
local use.

## Phase 0: Domain Routing

Detect the project domain before checking constitution compliance:
- `design/cdd/game-concept.md` -> **[Game]** verify principles against player fantasy, core loop, game pillars, playtest evidence, and game-specific CDDs.
- `design/cdd/product-concept.md` -> **[Product]** verify principles against user promise, JTBD, target workflows, product modules, API/CLI contracts, and product-specific CDDs.
- If neither exists, check only the constitution and report that domain-specific validation is pending.

Do not remove game constitution examples. Product checks are an added validation path.
# Constitution Check — T0-T3 Memory Health Audit

This skill is read-only by default. Its only write exception is an explicitly
approved refresh of `memory_bank/t2_execution/adapter_state.yaml`; every other
project file remains read-only.

This skill checks the health of a project's memory-bank governance plane:
whether T0 laws/current state exist, whether T1 supporting context is present,
whether T2 execution mirrors exist when the project has been initialized, and
whether T3 archive indexes exist once evidence is produced. It is lightweight —
not a full 4-gate CDD audit. For a complete project scan, use
`/project-stage-detect`.

---

## Step 0: Parse Audit Scope

Accept exactly one mode: no argument (all-law summary), `full` (all-law verbose),
or one positive displayed principle number `N` or `#N`. Reject `0`, negatives,
decimals, arbitrary tokens and combinations such as `full 2`; show this usage
and record invalid selection without silently switching to all laws.

Parsing sets requested scope but does not skip global checks. Continue read-only
T0-T3, required-input, tech-context and adapter observations even for invalid,
missing or ambiguous selectors. If the constitution is absent, Step 1 still
reports that original missing, recommends `/constitute` and stops. No selector
itself authorizes a write or offers an adapter-state record.

## Step 1: Verify Constitution Exists

Check for the minimum memory-bank artifacts:

| Artifact | Required? | How to check |
|----------|-----------|--------------|
| `memory_bank/t0_core/basic_law_index.md` | **Yes** | Read if exists |
| `memory_bank/t0_core/active_context.md` | **Yes** | Read if exists |
| `memory_bank/t0_core/current_state.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/tech_context.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/system_patterns.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/behavior_context.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/architecture_context.md` | Recommended | Read if exists |
| `memory_bank/t1_axioms/ux_accessibility_context.md` | Recommended | Read if exists |
| `memory_bank/t1_axioms/qa_context.md` | Recommended | Read if exists |
| `memory_bank/t1_axioms/knowledge_graph.md` | Recommended | Read if exists |
| `memory_bank/t1_axioms/module_support_map.yaml` | Recommended | Read if exists |
| `memory_bank/t2_execution/workflow_contract.md` | Recommended | Read if exists |
| `memory_bank/t2_execution/current_roadmap.md` | Recommended | Read if exists |
| `memory_bank/t2_execution/framework_contract.md` | Recommended | Read if exists |
| `memory_bank/t2_execution/adapter_state.yaml` | Recommended | Read if exists |
| `memory_bank/t3_archive/README.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/gate_runs/README.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/release_evidence/README.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/reviews/README.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/reviews/review-index.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/sprint_snapshots/README.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md` | Recommended | Read if exists |
| `memory_bank/t3_archive/amendments/README.md` | Recommended | Read if exists |
| `memory_bank/README.md` | Recommended | Read if exists |

If `basic_law_index.md` is missing: "No constitution detected. Run `/constitute`
to establish one." Stop here — nothing else to check.

If `basic_law_index.md` exists but older projects only have T0/T1 files, report
`NEEDS ATTENTION` with a migration recommendation. Do not mark old T0/T1-only
projects `CRITICAL` unless a required T0 file or `tech_context.md` is missing.

If `memory_bank/t0_core/knowledge_graph.md` exists, report it as a deprecated compatibility path. The canonical path is now
`memory_bank/t1_axioms/knowledge_graph.md`.

---

## Step 2: Read the Constitution

Read `memory_bank/t0_core/basic_law_index.md` and extract:
- Core thesis (Support ID: BL-01)
- All laws/ principles (Support IDs: BL-02 through BL-06)
- Each law's current-state requirement

Build the selector map from substantive displayed `Law N`/`Principle N` headings
and each entry's actual Support ID. Core Thesis BL-01, unnumbered boundary text,
BL suffixes and list positions do not supply principle numbers. In the normal
fixture, Law 2 maps to BL-03; if only Laws 1 and 3 exist, `3` still maps to Law 3 /
BL-04 rather than the second entry becoming Law 2.

Default and `full` assess all applicable laws. Numeric focus assesses only its
unique matching law. No match reports `NOT FOUND`; duplicate displayed numbers
report `AMBIGUOUS` with actual candidates and no arbitrary selection. Invalid,
no-match or ambiguous requests assess no principle alignment. Label unselected
laws `NotAssessed`, preserving existing evidence/history; do not infer ALIGNED
or all-law HEALTHY from focused/unresolved scope. Global findings and severity
remain visible in every mode.

Read `memory_bank/t0_core/active_context.md` and extract:
- Current working state (State A-E)
- Module status summaries
- Active risks and open decisions

Read `memory_bank/t0_core/current_state.md` when present and extract:
- Current phase
- Current blocker
- Next command
- Stage source

Read `memory_bank/t1_axioms/tech_context.md` and extract:
- Language, framework, platform
- Performance budgets
- External dependencies

Read T2 files when present:
- `memory_bank/t2_execution/workflow_contract.md`
- `memory_bank/t2_execution/current_roadmap.md`
- `memory_bank/t2_execution/framework_contract.md`
- `memory_bank/t2_execution/adapter_state.yaml`

Read T3 indexes when present:
- `memory_bank/t3_archive/qa_evidence_index.md`
- `memory_bank/t3_archive/gate_runs/`
- `memory_bank/t3_archive/release_evidence/`
- `memory_bank/t3_archive/reviews/`
- `memory_bank/t3_archive/reviews/review-index.md`
- `memory_bank/t3_archive/sprint_snapshots/`
- `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md`
- `memory_bank/t3_archive/amendments/`

---

## Step 3: Adapter Freshness Check

For the submission boundary, inspect actual diffs, the Git index and intended
delivery/publication contents under the governing Source/Target rules. Establish
CDD framework provenance, ownership and delivery role before classifying complete
CDD bodies and required support. Project-owned development skills, independent
roles, tools, documents, configuration, business code/tests/QA retain project rules;
a CDD reference does not change their ownership. Split mixed CDD/project content
per its actual parts and support. Required local inputs and Target Git candidates
are separate: confirmed CDD templates, generic standards/workflow originals,
skill-testing definitions and maintenance tools stay outside Target Git but may
remain locally and be discovered, loaded, take effect and be used under existing
authorization. Locally readable ignored inputs are not missing Git deliverables
and gain no Git eligibility merely because a workflow requires them. Optional
authorized maintenance is allowed; ordinary installed-input use needs no toolkit.
Ignore rules are not runtime loading controls and do not remove tracked/staged
content. Existing tracked CDD reconciliation needs its governance gate, separate
exact-path tracking-only migration authority and preservation of local originals,
required closure, customizations, recoverable before bytes and Git history.
Location/presence alone is not a finding. This audit does not authorize moving/
deleting files, untracking or changing log locations.

First read `memory_bank/t2_execution/framework_contract.md` when it exists.
Its project/Source binding section records the actual project role, sole Source,
installed revision and runtime, exact installed paths, required neutral inputs
and project-owned customizations. Unknown values remain unconfigured.

When this audit includes import/update or layout reconciliation, read the
existing scoped plan/report and apply `standards/directory-structure.md`, section
"Consumer layout resolution for imports and updates". Bind the latest applicable
Source inputs and compare actual installed paths, active readers/references,
discovery/configuration and generation/comparison chain with the resolved tree
and mapping. Internal agreement between legacy inputs and their own adapters
does not prove current alignment. Do not treat a planned destination as installed
or automatically retain an old path as a customization exemption.
Distinguish historical identifiers with actual recoverable originals/witnesses
from current dependencies: do not fail mere historical path text or silently
waive a stale live reader. Local copy presence alone is not a layout violation.
Unresolved layout/ownership/conflicts leave affected alignment pending; only valid
applicable comparison evidence can establish fresh/stale. Unselected layout
alignment is NotAssessed; ordinary offline installed-input observations still
work and do not imply a Source update or new global gate.

If that control-plane file is absent or lacks a binding, use only existing
project-owned documentation/configuration selected by the project's governing
instructions and defining those same fields and their owners. Do not invent a
configuration path/schema, restore a maintenance profile/lock, or create the
Memory Bank for this audit. Without a documented binding, report its affected
scope as Unknown/NOT AVAILABLE and continue independent installed-input checks;
no freshness state write is available. A local manifest or copied script alone
does not establish that this is the CDD Source library.

For a consumer, directly read the selected installed entries and their actual
required references. Report missing/unread originals with their affected scope.
These observations work offline and need no local maintenance toolkit. They do
not establish live Source freshness. A consumer freshness comparison must bind
its exact installed allowlist against the actual sole Source revision/expected
outputs and approved project differences; a Source-only check is insufficient.

If the Source is unavailable, the binding is unresolved, or no valid comparison
covers the consumer's installed files, report `Live adapter freshness: NOT AVAILABLE`
with the exact limitation. Preserve any recorded state and continue
independent constitution/installed-input checks. Do not add general source
mirrors/checkers to consumer Git delivery or label an uninitialized record fresh.

Use only an actually available, authorized read-only comparison that covers the
applicable owner and exact installed paths. Without such a comparison, keep
NOT AVAILABLE and continue at Step 4 without offering a state write. A missing
optional checker does not hide a failed comparison that actually ran.

For an applicable comparison, bind the actual owner, Source revision, full input
identities, complete compared paths, approved project differences, result and
verification time. A consumer comparison must include its installed allowlist;
a Source-library result alone is insufficient. Record the real comparison
method without inventing an invocation. Missing, malformed or mismatched evidence
is INVALID or NOT AVAILABLE for its affected scope; preserve recorded state and
offer no state write. Valid evidence may establish fresh/stale only for its
declared scope. Evidence used with the existing adapter-state schema must include
`schema_version: 1`, a `status` of `fresh` or `stale`, full 64-character
lowercase hexadecimal `manifest_digest` and `source_digest`, ISO-8601 UTC
`checked_at`, the actual `checked_commit`, `counts` and `check_command`.
Validate all fields and complete input scope; record the actual comparison method
in `check_command`, never a fabricated invocation. Missing, malformed or
scope-mismatched fields are INVALID and offer no state write. Manual observations
that do not supply this valid record remain separate from CURRENT/OUTDATED and
the optional YAML-record branch below.

Compare an applicable valid live result with
`memory_bank/t2_execution/adapter_state.yaml`:

| Recorded state | Meaning |
|----------------|---------|
| `MISSING` | The memory bank exists but the adapter-state template was not initialized |
| `UNINITIALIZED` | The deterministic template exists and has no recorded evidence |
| `CURRENT` | Applicable checked owner/scope, recorded status and both digests match the live result |
| `OUTDATED` | A prior record exists but status or either digest differs |
| `UNVERIFIED` | A prior record exists but no applicable live comparison is available |

Report both values separately: `Live adapter freshness: FRESH/STALE/INVALID/NOT AVAILABLE`
and `Recorded adapter state: CURRENT/OUTDATED/UNINITIALIZED/MISSING/UNVERIFIED`. Include
all non-zero counts and drift paths. A clean `checked_commit` is contextual;
the two digests are the authoritative identity of the checked inputs.

### Optional approved state record

Only for default/full or a resolved numeric scope, and a valid live result
covering the actual checked owner/inputs, prepare
the complete YAML draft with this field order and actual live values. Use its
actual portable check description; do not store host-specific paths in a target
project. No unavailable or Source-only consumer check is recordable:

```yaml
schema_version: 1
status: fresh
manifest_version: 2
manifest_digest: "[live manifest_digest]"
source_digest: "[live source_digest]"
checked_commit: "[live checked_commit]"
checked_at: "[live checked_at]"
check_command: "[actual live portable check command/description]"
```

Use `stale` instead of `fresh` when the live check reports drift. Show the
entire draft. Reuse existing matching authority for this exact record; otherwise
ask exactly:

`May I write this adapter freshness record to memory_bank/t2_execution/adapter_state.yaml?`

If approved, write only that file. If declined, leave the repository unchanged
and state that the report was read-only. Never create `memory_bank/` from this
skill; when the control plane or `framework_contract.md` is missing, recommend
`/constitute`.

## Step 4: Alignment Check

Check alignment only for principles selected at Step 2. Unselected principles
remain NotAssessed; invalid/no-match/ambiguous scope runs no alignment scan.
Continue independent global health and tech-context checks in every mode:

### 3a: Principle → Code Alignment

For each selected law in `basic_law_index.md`, perform a quick alignment scan:

1. Read the law's current-state requirement
2. Check whether the codebase respects it
3. Flag violations or uncertainties

Example checks:
- Law requires "no function over 20 lines" → grep for functions, check length
- Law requires "API stability: no breaking changes" → check for deprecation markers
- Law requires "all public APIs documented" → check docstring coverage in `src/`
- Law requires "tests before merge" → check test file count vs source file count

For each law, produce one of:
- **ALIGNED** — evidence found that the law is being followed
- **CONCERN** — potential violation or insufficient evidence
- **UNABLE TO CHECK** — law is abstract or can't be auto-verified (e.g., "prioritize user experience")

### 3b: Tech Context → Reality Check

Compare `tech_context.md` against actual project state:
- Is the declared language actually used? (Glob `src/**` for language files)
- Are declared dependencies actually in the project? (Check config files)
- Are performance budgets plausible given the codebase size?

---

## Step 5: Gap Detection

Identify what's missing or stale:

| Gap | Detection |
|-----|-----------|
| **Missing T0 current state** | `memory_bank/t0_core/current_state.md` does not exist |
| **Missing T1 required docs** | `tech_context.md`, `system_patterns.md`, or `behavior_context.md` missing |
| **Missing T1 recommended docs** | `architecture_context.md`, `ux_accessibility_context.md`, `qa_context.md`, `knowledge_graph.md`, or `module_support_map.yaml` missing |
| **Deprecated knowledge graph path** | `memory_bank/t0_core/knowledge_graph.md` exists |
| **Missing T2 workflow contract** | `memory_bank/t2_execution/workflow_contract.md` does not exist |
| **Missing T2 current roadmap** | Project has roadmap evidence but `memory_bank/t2_execution/current_roadmap.md` is missing |
| **Missing framework contract** | `memory_bank/t2_execution/framework_contract.md` does not exist |
| **Missing adapter state** | `memory_bank/t2_execution/adapter_state.yaml` does not exist |
| **Uninitialized adapter state** | State exists with `status: uninitialized`; only valid applicable live evidence can initialize the record |
| **Unavailable live comparison** | Exact Source/binding/check evidence unavailable; preserve recorded state and continue independent checks |
| **Stale adapters** | Valid live comparison evidence reports `status: stale` or non-zero stale/missing/extra/invalid counts |
| **Outdated adapter record** | Recorded status or digests differ from the live result |
| **Missing T3 archive README** | `memory_bank/t3_archive/README.md` does not exist |
| **Missing T3 gate archive** | Gate evidence exists but `memory_bank/t3_archive/gate_runs/README.md` is missing |
| **Missing QA evidence index** | QA evidence exists but `memory_bank/t3_archive/qa_evidence_index.md` is missing |
| **Missing release evidence archive** | Release evidence exists but `memory_bank/t3_archive/release_evidence/README.md` is missing |
| **Missing review index** | Review artifacts exist but `memory_bank/t3_archive/reviews/review-index.md` is missing |
| **Missing story closure index** | Completed stories exist but `memory_bank/t3_archive/sprint_snapshots/story-closure-index.md` is missing |
| **Missing README** | `memory_bank/README.md` does not exist |
| **Stale tech context** | Tech context mentions old versions or unused dependencies |
| **Drifted principles** | Law says X, code does Y |
| **No review mode set** | `production/review-mode.txt` does not exist |

---

## Step 6: Present Report

Keep it concise. Use this format:

```
## Memory Bank Health: [Project Name]

**Core thesis:** [from BL-01, one line]
**Constitution established:** [date from active_context.md or file timestamp]
**Current phase:** [from current_state.md or production/stage.txt]
**Principle scope:** [all / Law N and actual Support ID / invalid / not found / ambiguous]
**Alignment coverage:** [assessed / total; unselected NotAssessed]

### T0 Current Truth
- Laws: [present/missing/stale]
- Active context: [present/missing/stale]
- Current state: [present/missing/stale]

### T1 Supporting Context
- Tech context: [present/missing/stale]
- System patterns: [present/missing/stale]
- Behavior context: [present/missing/stale]
- Recommended context: [summary]

### T2 Execution Control
- Workflow contract: [present/missing]
- Current roadmap: [present/missing/not started]
- Framework contract: [present/missing]
- Live adapter freshness: [fresh/stale/invalid/not available]
- Installed inputs: [observed complete / affected missing or unread paths]
- Recorded adapter state: [current/outdated/uninitialized/missing/unverified]

### T3 Archive Indexes
- Archive README: [present/missing]
- QA evidence index: [present/missing/not applicable yet]
- Release evidence: [present/missing/not applicable yet]

### Principles ([aligned]/[assessed] aligned; [unselected] NotAssessed)
- [Support ID]: ALIGNED — [brief evidence]
- [Support ID]: ALIGNED — [brief evidence]
- [Support ID]: CONCERN — [what's wrong, suggestion]

### ✓ Tech Stack
- Language: [X] ✓
- Framework: [Y] ✓
- Platform: [Z] ✓
- [Any concerns]

### → Gaps
- [Gap 1 — with concrete fix, e.g. "Run /constitute-check for a read-only audit; updates need separate authority"]
- [Gap 2]

### → Recommendations
1. [Highest priority action]
2. [Secondary action]

---
**Global T0-T3/input health:** [HEALTHY / NEEDS ATTENTION / CRITICAL]
**Overall:** [HEALTHY / NEEDS ATTENTION / CRITICAL / PARTIAL — actual alignment scope]
```

**Severity levels:**
- **HEALTHY**: Required T0/T1 artifacts present, T2/T3 indexes appropriate for stage, all checkable laws ALIGNED
- **NEEDS ATTENTION**: Old T0/T1-only memory bank, stale/uninitialized/outdated adapter state, 1-2 CONCERNs, or missing recommended T1/T2/T3 indexes
- **CRITICAL**: Missing `basic_law_index.md`, missing required T0/T1 files, 3+ CONCERNs, or stale constitution

Numeric focus shows the displayed number/actual ID, selected evidence and
unselected NotAssessed entries. Global required-input gaps keep their severity,
including CRITICAL, regardless of selected alignment. If global observations
have no concerns but laws remain unassessed, report Overall PARTIAL for alignment
scope; never certify all-law HEALTHY. Invalid/no-match/ambiguous selection retains
its unresolved finding and cannot offer a state write. `full` adds detail for
all assessed laws; default summarizes all. Neither mode waives a global gap.

---

## Edge Cases

- **No constitution**: "No constitution detected. Run `/constitute` to establish your project's governing principles." Stop.
- **Old T0/T1-only memory bank**: "Your constitution exists, but the T2/T3 governance control plane is not initialized. Run `/constitute` to refresh the memory-bank skeleton." Continue with `NEEDS ATTENTION`.
- **Missing adapter templates in an older memory bank**: Recommend `/constitute` to initialize both framework files; do not create the control plane from this audit.
- **Unavailable Source/comparison**: Report NOT AVAILABLE and any historical recorded state separately; preserve it. Complete installed-input and constitution observations offline without requiring Source trees or tools.
- **Stale live check**: Report every drift class for the actual compared owner/paths and offer to record `status: stale`; regeneration remains a separate, explicitly requested action.
- **Invalid comparison evidence**: Report `INVALID`, preserve any prior state file, and do not write partial or fabricated values.
- **Constitution exists but is very old**: Note the date — "Your constitution was established [N months] ago. Much may have changed. Consider running `/constitute` to refresh it."
- **Path D project (existing code, new constitution)**: Flag likely drift — "Your constitution was recently established. Some existing code may not yet align. This is normal for brownfield adoption — prioritize alignment iteratively."
- **All laws are abstract (can't auto-check)**: "Your principles are abstract — they can't be automatically verified. Consider adding falsifiable current-state requirements to each law for future audits."

---

## Collaborative Protocol

- **Read-only by default.** The sole exception is an exact adapter-state YAML record after explicit approval.
- **No hidden writes.** Running the comparison, declining the draft, or encountering invalid comparison evidence must leave the repository unchanged.
- **Be honest.** Don't sugarcoat drift or gaps.
- **Be specific.** Every gap must come with a concrete fix suggestion.
- **One primary recommendation.** The user should leave knowing exactly one thing to do next.
