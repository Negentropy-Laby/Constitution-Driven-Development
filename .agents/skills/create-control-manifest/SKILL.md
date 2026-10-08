---
name: create-control-manifest
description: "Use this skill when accepted ADRs and technical standards must be converted into a concise programmer-facing control manifest after architecture approval."
argument-hint: "[update — regenerate from current ADRs]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Task
agent: technical-director
---

## Scope, decisions and exact evidence

Read `standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md` from the
project root. Reuse original authorization only for its exact named paths, effects
and limits across roles/retries. Content agreement, writes, independent review,
ADR acceptance and Story/phase completion remain separate. Show a concrete draft
before asking about unresolved material choices or new effects; covered writes
need no repeated per-file or per-role permission.

Read/review-only never invokes a write entrypoint, including in memory. Report-only
may write its assigned new report, not inputs, indexes, session state, logs or T3
pointers. Each other effect needs existing scope or separate changeset authority.
No Memory Bank means the existing Story/review/conversation fallback, not activation.

Bind claims to original paths, full SHA-256 (64 hex), byte sizes, collection time
with timezone, source commit plus exact uncommitted/ignored/external identities.
Read actual bodies and minimum required direct/indirect evidence closure; retain
recoverable originals and disclose missing inputs. Resolve CDD DocKind/required
owner set and module semantic eight through `design/INSTRUCTIONS.md`, preserving
substantive aliases; headings, counts or existence cannot establish PASS.

Classify each meaningful choice as `covered`, `cdd-layer`, `no-adr`,
`documentation-update`, `adr-required` or `conflict`, with named requirement/owner,
existing TR-ID if assigned, exact Accepted ADR revision/section/scope or justified
no-ADR reason, affected paths/dependencies, evidence and action/owner/due phase.
Trust boundaries, public contracts, durable formats, state ownership and governing
architectural constraints require an Accepted decision or valid scoped exception
under existing governance before affected implementation starts/continues. Continue
independent work. Proposed, implemented, green tests, write approval and director
recommendations do not establish acceptance; historical approval needs exact input
and authority/scope match. Justified `cdd-layer`/`no-adr` waives no other readiness,
manifest or evidence prerequisite. The existing global Technical Setup minimum of
three Foundation ADRs in `workflow/workflow-catalog.yaml` remains a separate gate:
do not bypass it or manufacture ADRs to meet a count.

Absent, conflicting or ambiguous concept/domain evidence means Unknown. Continue
domain-independent checks; resolve the domain before applying its Game/Product
rules. Do not silently default to Game.

## User Guide

- When to use: After architecture is complete, produces a flat actionable rules sheet for programmers — what you must do, what you must never do, per module and per layer. Extracted from all Accepted ADRs, technical preferences, and reference docs. Supports both game and general product domains.
- Inputs: Command arguments: `/create-control-manifest [update — regenerate from current ADRs]`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: None.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

# Create Control Manifest

The Control Manifest is a flat, actionable rules sheet for programmers. It
answers "what do I do?" and "what must I never do?" — organized by architectural
layer, extracted from all Accepted ADRs, technical preferences, and engine
reference docs. Where ADRs explain *why*, the manifest tells you *what*.

**Output:** `docs/architecture/control-manifest.md`

**When to run:** After `/architecture-review` passes and ADRs are in Accepted
status. Re-run whenever new ADRs are accepted or existing ADRs are revised.

**Domain detection.** The concept document at `design/cdd/` reveals the domain.
Sections below are marked **[通用场景]**, **[游戏专用]**, or **[通用产品]**.

---

## 1. Load All Inputs

### ADRs
- Glob `docs/architecture/adr-*.md` and read every file
- Filter to only Accepted ADRs (Status: Accepted) — skip Proposed, Deprecated,
  Superseded; report excluded decisions and affected scope
- Verify actual Accepted authority/revision/scope and required decision dependencies,
  not status text alone. Required Proposed/conflict remains incomplete, not satisfied
  by omission.
- Note exact ADR revision/section/source identity for each sourced rule

### Technical Preferences
- Read `standards/technical-preferences.md`
- Extract: naming conventions, performance budgets, approved libraries/addons,
  forbidden patterns

### Technology Reference

**[游戏专用]** Engine reference:
- Read `docs/engine-reference/[engine]/VERSION.md` for engine + version
- Read `docs/engine-reference/[engine]/deprecated-apis.md` — these become
  forbidden API entries
- Read `docs/engine-reference/[engine]/current-best-practices.md` if it exists

**[通用产品]** Stack reference:
- Read `docs/reference/[stack]/VERSION.md` for stack + version
- Read `docs/reference/[stack]/deprecated-apis.md` — these become
  forbidden API entries
- Read `docs/reference/[stack]/current-best-practices.md` if it exists

Report: "Loaded [N] Accepted ADRs, technology: [name + version]."
If required governing decisions/architecture review are incomplete, report BLOCKED
for affected rules; do not label the result Active/complete. With no ADRs the separate
global Technical Setup minimum is unsatisfied; recommend its owning decision workflow.
An explicitly authorized Draft/Blocked preview does not bypass those prerequisites.
Retain this qualification through every later phase: incomplete required architecture,
Accepted decisions, global Technical Setup gate or dependencies mean Draft/Blocked,
with named findings/actions; only a verified complete required closure may be Active.
A skipped/approved director review or preview write cannot change that qualification.

---

## 2. Extract Rules from Each ADR

For each Accepted ADR, extract:

### Required Patterns (from "Implementation Guidelines" section)
- Every "must", "should", "required to", "always" statement
- Every specific pattern or approach mandated

### Forbidden Approaches (from "Alternatives Considered" sections)
- Every alternative that was explicitly rejected — *why* it was rejected becomes
  the rule ("never use X because Y")
- Any anti-patterns explicitly called out

### Performance Guardrails (from "Performance Implications" section)
- **[游戏专用]** Budget constraints: "max N ms per frame for this system"
- **[通用产品]** Budget constraints: "max N ms p95 for this endpoint" or
  "max N seconds cold start for this CLI command"
- Memory limits: "this system must not exceed N MB"

### Technology API Constraints (from compatibility sections)

**[游戏专用] Engine API Constraints** (from "Engine Compatibility" section):
- Post-cutoff engine APIs that require verification
- Verified behaviours that differ from default LLM assumptions
- API fields or methods that behave differently in the pinned engine version

**[通用产品] Stack API Constraints** (from "Technology Compatibility" or "Stack Compatibility" section):
- Post-cutoff framework, runtime, database, or SDK APIs that require verification
- Verified behaviours that differ from default LLM assumptions
- API fields, methods, decorators, middleware, or configuration options that
  behave differently in the pinned stack version

### Layer Classification
Classify each rule by the architectural layer of the module it governs:

**[游戏专用]** Game layers:
- **Foundation**: Scene management, event architecture, save/load, engine init
- **Core**: Core gameplay loops, main player systems, physics/collision
- **Feature**: Secondary systems, secondary mechanics, AI
- **Presentation**: Rendering, audio, UI, VFX, shaders

**[通用产品]** Product layers:
- **Foundation**: Framework integration, ORM/database, message queue, storage abstraction
- **Core**: Auth, data access, config, logging, API framework
- **Feature**: Business logic, integrations, user-facing features
- **Presentation**: UI components, API endpoints, CLI commands

If an ADR spans multiple layers, duplicate the rule into each relevant layer.

---

## 3. Add Global Rules

Combine rules that apply to all layers:

### From technical-preferences.md:
- Naming conventions (classes, variables, signals/events, files, constants)

### Performance Budgets:
- **[游戏专用]** Target framerate, frame budget, draw call limits, memory ceiling
- **[通用产品]** API latency p95, memory ceiling, cold start time, throughput

### From deprecated-apis.md:
- All deprecated APIs → Forbidden API entries

### From current-best-practices.md (if available):
- Technology-recommended patterns → Required entries

### From technical-preferences.md forbidden patterns:
- Copy any "Forbidden Patterns" entries directly

---

## 4. Present Rules Summary Before Writing

Before writing the manifest, present a summary to the user:

```
## Control Manifest Preview
Technology: [name + version]
ADRs covered: [list ADR numbers]
Total rules extracted:
  - Foundation layer: [N] required, [M] forbidden, [P] guardrails
  - Core layer: [N] required, [M] forbidden, [P] guardrails
  - Feature layer: ...
  - Presentation layer: ...
  - Global: [N] naming conventions, [M] forbidden APIs, [P] approved libraries
```

Ask: "Does this look complete? Any rules to add or remove before I write the manifest?"

---

## 4b. Director Gate — Technical Review

Resolve mode once: explicit `--review full|lean|solo`, else
`production/review-mode.txt`, else lean. Validate supplied/global values; invalid
values require correction, never silent fallback. Retain the existing update command.

**Review mode check** — apply before spawning TD-MANIFEST:
- `solo` → skip. Note: "TD-MANIFEST skipped — Solo mode." Proceed to Phase 5.
- `lean` → skip. Note: "TD-MANIFEST skipped — Lean mode." Proceed to Phase 5.
- `full` → spawn as normal.

Spawn `technical-director` via Task using **TD-MANIFEST**, whose criteria/verdicts
are defined inline in this Phase 4b of `skills/create-control-manifest/SKILL.md`.
`standards/director-gates.md` supplies shared mode/authority guidance, not this gate definition.

Pass: the Control Manifest Preview from Phase 4 (rule counts per layer, full extracted rule list), the list of ADRs covered, engine version, and any rules sourced from technical-preferences.md or engine reference docs.

The technical-director reviews whether:
- All mandatory ADR patterns are captured and accurately stated
- Forbidden approaches are complete and correctly attributed
- No rules were added that lack a source ADR or preference document
- Performance guardrails are consistent with the ADR constraints

Apply the verdict:
- **APPROVE** → proceed to Phase 5
- **CONCERNS** → surface via `AskUserQuestion` with options: `Revise flagged rules` / `Accept and proceed` / `Discuss further`
- **REJECT** → do not write the manifest; fix the flagged rules and re-present the summary

---

## 5. Write the Control Manifest

Reuse existing authority for this exact manifest create/overwrite effect. Only
for uncovered effects show the qualified draft and ask:
"May I write this to `docs/architecture/control-manifest.md`?"

Before writing, enforce Phase 1's qualification. Use Active only when all required
architecture/Accepted-decision/global-gate/dependency checks actually pass.
An authorized incomplete preview keeps Draft/Blocked and its findings in the file;
never fall through to Active because Phase 4b approved or skipped review.

Format:

```markdown
# Control Manifest

> **[游戏专用] Engine**: [name + version] / **[通用产品] Stack**: [language + framework + version]
> **Last Updated**: [date]
> **Manifest Version**: [date]
> **ADRs Covered**: [ADR-NNNN, ADR-MMMM, ...]
> **Status**: [Active only after required checks pass / Draft or Blocked preview]
> **Qualification Findings**: [None with evidence / missing inputs, affected rules, action and owner]
> **Regeneration**: `/create-control-manifest update` when governing inputs change

`Manifest Version`/`Last Updated` retain readable dates for legacy consumers.
Dates are descriptive, not content identity. After an authorized write, read the
complete saved raw bytes and compute full SHA-256 and byte size. Store this
`Manifest SHA-256`/`Manifest Bytes` with original path/time in Story/review/consumer
records, outside this manifest's own hashed bytes. Do not put its full-file hash
inside itself or normalize/omit bytes before hashing. Consumers compare complete
digests even on the same date. Existing date-only records are `LegacyRecheck`:
inspect current rules/dependencies and resolve affected Stories before an authorized
identity upgrade. Historical equality cannot be inferred from dates; invent no old hash.

This manifest is a programmer's quick-reference extracted from all Accepted ADRs,
technical preferences, and engine reference docs. For the reasoning behind each
rule, see the referenced ADR.

---

## Foundation Layer Rules

**[游戏专用]** *Applies to: scene management, event architecture, save/load, engine initialisation*

**[通用产品]** *Applies to: framework integration, ORM/database, message queue, storage abstraction, container runtime*

### Required Patterns
- **[rule]** — source: [ADR-NNNN]
- **[rule]** — source: [ADR-NNNN]

### Forbidden Approaches
- **Never [anti-pattern]** — [brief reason] — source: [ADR-NNNN]

### Performance Guardrails
- **[module]**: max [N]ms / [N]MB — source: [ADR-NNNN]

---

## Core Layer Rules

**[游戏专用]** *Applies to: core gameplay loop, main player systems, physics, collision*

**[通用产品]** *Applies to: auth, data access, config, logging, API framework*

### Required Patterns
...

### Forbidden Approaches
...

### Performance Guardrails
...

---

## Feature Layer Rules

**[游戏专用]** *Applies to: secondary mechanics, AI systems, secondary features*

**[通用产品]** *Applies to: business logic, integrations, user-facing features*

### Required Patterns
...

### Forbidden Approaches
...

---

## Presentation Layer Rules

**[游戏专用]** *Applies to: rendering, audio, UI, VFX, shaders, animations*

**[通用产品]** *Applies to: UI components, API endpoints, CLI commands*

### Required Patterns
...

### Forbidden Approaches
...

---

## Global Rules (All Layers)

### Naming Conventions
| Element | Convention | Example |
|---------|-----------|---------|
| Classes | [from technical-preferences] | [example] |
| Variables | [from technical-preferences] | [example] |
| Signals/Events | [from technical-preferences] | [example] |
| Files | [from technical-preferences] | [example] |
| Constants | [from technical-preferences] | [example] |

### Performance Budgets

**[游戏专用]** Game budgets:
| Target | Value |
|--------|-------|
| Framerate | [from technical-preferences] |
| Frame budget | [from technical-preferences] |
| Draw calls | [from technical-preferences] |
| Memory ceiling | [from technical-preferences] |

**[通用产品]** Product budgets:
| Target | Value |
|--------|-------|
| API latency (p95) | [from technical-preferences] |
| Memory ceiling | [from technical-preferences] |
| Cold start time | [from technical-preferences] |
| Throughput | [from technical-preferences] |

### Approved Libraries / Addons
- [library] — approved for [purpose]

### Forbidden APIs ([technology version])
These APIs are deprecated or unverified for [technology + version]:
- `[api name]` — deprecated since [version] / unverified post-cutoff
- Source: `docs/[engine-]reference/[name]/deprecated-apis.md`

### Cross-Cutting Constraints
- [constraint that applies everywhere, regardless of layer]
```

---

## 6. Suggest Next Steps

After writing the manifest, read back exact bytes and report path, full SHA-256,
byte size and collection time. Consumer identity remains outside the manifest.
This write does not automatically update Stories, registry, indexes or session state.


- If Active and epics/stories don't exist yet: "Run `/create-epics layer: foundation`
  then `/create-stories [epic-slug]`; validate each Story's remaining readiness checks."
- If Draft/Blocked: report the preview status, unresolved findings/action/owner and
  affected scope. Recommend the owning repair workflow; the preview grants no readiness.
- If this is a regeneration (manifest already existed): report the actual status and
  changed rules — especially new Forbidden entries. Any team notification needs its
  own explicit authority.

---

## Collaborative Protocol

1. **Load silently** — read all inputs before presenting anything
2. **Show the summary first** — let the user see the scope before writing
3. **Scope before writing** — reuse exact covered authority; otherwise show the draft
   and ask before creating/overwriting. Report saved-path/readback as an operation
   outcome separately from qualification. **COMPLETE** qualification requires all
   required checks to pass and an Active manifest. A saved Draft/Blocked preview
   remains **BLOCKED/INCOMPLETE** with findings; writing never establishes readiness.
   On decline: **BLOCKED** — user declined write.
4. **Source every rule** — never add a rule that doesn't trace to an ADR, a
   technical preference, or an engine reference doc
5. **No interpretation** — extract rules as stated in ADRs; do not paraphrase
   in ways that change meaning

## Exact-byte check availability

Use available read-only tools to collect complete raw-file SHA-256/byte size without
normalizing line endings. If exact bytes/digest or a required dependency cannot be
read, report the affected check incomplete; do not substitute a date, text rendering,
short hash or file existence. Analysis invokes no write entrypoint.
