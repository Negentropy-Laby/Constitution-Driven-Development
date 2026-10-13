---
name: setup-engine
description: "Use this skill when selecting, pinning, refreshing, or upgrading a game engine or software stack and updating project technology references and specialist routing."
argument-hint: "[engine | framework | stack] [version] | refresh | upgrade [old-ver] [new-ver] | no args for guided selection"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, Edit, Bash, WebSearch, WebFetch, Task, AskUserQuestion
---

## User Guide

- When to use: Configure the project's technology foundation — game engine or general product stack. Pins the stack in INSTRUCTIONS.md, detects knowledge gaps, and populates reference docs via WebSearch when versions are beyond the LLM's training data.
- Inputs: Command arguments: `/setup-engine [engine | framework | stack] [version] | refresh | upgrade [old-ver] [new-ver] | no args for guided selection`; project artifacts referenced below; user decisions and approvals before writes.
- Outputs: Primary artifacts, reports, or conversation guidance described below; write files only after user approval.
- Memory-bank writes: `memory_bank/t1_axioms/tech_context.md`.
- Next steps: Follow the workflow hand-off or next-step guidance below; recommendations do not auto-run and require explicit user command/approval.

## Asset Ownership and Local Use before Technology Setup

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

This CDD technology-setup skill and its exclusive framework support remain local
Target inputs; Source delivers its templates/full projections as framework product
assets. Project-owned specialist roles, tools, configuration and generated technical
documents follow project rules even when they support development. This boundary
changes no runtime discovery/loading configuration and grants no import, untracking,
move/delete or state authority.

When this skill is invoked:

## 1. Parse Arguments

Five modes:

- **Full spec**: `/setup-engine godot 4.6` or `/setup-engine django 5.1` — stack and version provided
- **Stack only**: `/setup-engine unity` or `/setup-engine react` — stack provided, version will be looked up
- **No args**: `/setup-engine` — fully guided mode (domain detection, then recommendation + version)
- **Refresh**: `/setup-engine refresh` — update reference docs (see Section 10)
- **Upgrade**: `/setup-engine upgrade [old-ver] [new-ver]` — migrate to a new version (see Section 11)

**Domain detection.** The argument usually reveals the domain:
- **游戏专用 hints**: godot, unity, unreal, ue5, game engine → game mode
- **通用产品 hints**: python, django, fastapi, react, nextjs, node, rust, go, postgres, redis, docker → product mode
- **Ambiguous**: ask during guided mode

Sections below are marked **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

---

## 1a. Existing Configuration and Section Scope

Before guided selection, read the actual `standards/technical-preferences.md`
and project settings. Resolve populated Game fields or valid Product aliases
under the preference owner; placeholders do not establish configuration. Report
the configured engine/stack and language, or exact incomplete/conflicting fields.

For an already configured project with no explicit reconfiguration choice, use
`AskUserQuestion` to offer: reconfigure all; reconfigure specific sections; or
keep the configuration and stop. Section choices include Engine/Language or
Language & Framework, Naming Conventions, Specialists/Agent Routing, Performance
Budgets, Input & Platform/Platform & Deployment, and Testing. Reuse a supplied
section choice and matching authority without asking again.

For **section-only reconfiguration**:
1. Resolve each selected heading and its exact byte range through the next heading
   of the same or higher level, excluding headings inside fenced examples. Keep
   nested content such as File Extension Routing with its owning section. Missing
   or duplicate target headings require clarification before a write.
2. Read the complete existing file and relevant preference/reference branch.
   Gather only decisions needed for selected sections. A Performance Budgets
   request does not restart engine, version, language, platform or testing selection.
3. Retain recoverable before bytes for this file and any other named output; show
   the selected-section draft/diff and exact paths/effects. Default templates do
   not reset configured values, custom prose, comments or unrelated sections.
4. Reuse exact section-write authority or request only missing/new scope. If a
   choice needs dependent routing, root, version or other changes, explain those
   effects and obtain their scope before expanding. Do not silently add them.
5. Patch only approved section ranges. Preserve all bytes outside those ranges,
   including heading order, whitespace and project additions. A declined or pending
   write changes no bytes. Do not recreate the file from the full default template.
6. Read back the result and compare preserved prefix, inter-section spans and
   suffix against before bytes; verify every other output is unchanged. A
   mismatch leaves INCOMPLETE and must not be called COMPLETE.
7. Skip Sections 3-4, 6-9 and 11b unless their specific effects belong to the
   approved changeset. Budgets-only writes no root instructions/projections,
   version references, specialist definitions or T1 mirror. Proceed to Section 12
   with the selected scope and readback result.

Initial setup and explicitly selected full reconfiguration continue below,
preserving project customizations and writing only covered paths/effects.

## 2. Guided Mode (No Arguments)

For initial setup or selected full reconfiguration, if no stack is specified,
run interactive selection. Section-only requests use Section 1a.

### [通用场景] Check for existing concept

- **游戏专用**: Read `design/cdd/game-concept.md` if it exists — extract genre, scope, platform targets, art style, team size, and any engine recommendation from `/brainstorm`
- **通用产品**: Read `design/cdd/product-concept.md` if it exists — extract platform targets, stack preferences, performance needs, and any tech recommendation from `/brainstorm`. Also read `memory_bank/t1_axioms/tech_context.md` if it exists.

If no concept exists, inform the user:
- **游戏专用**: "No game concept found. Consider running `/brainstorm` first — it will recommend an engine."
- **通用产品**: "No product concept found. Consider running `/brainstorm` first — it will help identify stack requirements."

### [通用场景] Prior experience (ask first, always)

Use `AskUserQuestion`:
- Prompt: "Have you worked in any of these before?"

- **游戏专用** Options: `Godot` / `Unity` / `Unreal Engine 5` / `Multiple — I'll explain` / `None of them`
- **通用产品** Options: `Python (Django, FastAPI, Flask)` / `JavaScript/TypeScript (React, Next.js, Node)` / `Rust` / `Go` / `Multiple — I'll explain` / `None of them`

If they pick a specific stack → recommend it. Prior experience outweighs all other factors. Confirm with them and skip the matrix.

---

### Technology Selection Reference

When guided mode needs an engine, language, framework, or deployment-stack decision, read the matching domain section in [stack selection](references/stack-selection.md). Load only the options relevant to the detected project domain and user constraints.

## 3. Look Up Current Version

[通用场景] Once the stack is chosen:

- If version provided → use it
- If no version → WebSearch: `"[stack] latest stable version [current year]"`
- Confirm: "The latest stable [stack] is [version]. Use this?"

---

## 4. Update INSTRUCTIONS.md Technology Stack

Read `INSTRUCTIONS.md` and the actual runtime root-instruction files already
used by this project. Show the proposed Technology Stack changes together with
the exact affected root-instruction paths, preserving the CDD source/target
boundary sections, project customizations and existing approval rules.
These boundary sections constrain the Target Git tracking/staging/commit/delivery/
publication set for confirmed CDD assets. They preserve authorized local retention,
discovery, loading, effect and use; ignore rules are not runtime loading controls.
Project-owned development skills/roles, tools, configuration and documents retain
project rules. Preserve local CDD inputs, maintenance files and log locations;
optional authorized maintenance is allowed and ordinary setup must not require
that toolkit. Their presence alone is not a compliance gap, and this setup grants
no migration/untracking or relocation authority.
Ask for any missing authority for that complete changeset.

After approval, update the canonical project settings and their declared
root-instruction projections using normal file tools. A declared plain-copy
projection receives the same complete approved bytes; preserve separately owned
runtime guidance and compatibility rules. If a projection needs an unknown
transform or owner decision, leave that projection pending and explain the
specific missing input. Ordinary target-project setup does not require a local
maintenance script, checker, profile or lock, and never invokes a source-library
generator main/write against the target.

Update the Technology Stack section, replacing the `[CHOOSE]` placeholders with the actual values:

**[游戏专用]** Engine templates:

### Language Selection (Godot only)

If Godot was chosen, ask the user which language to use **before** showing the proposed Technology Stack:

> "Godot supports two primary languages:
>
>   **A) GDScript** — Python-like, Godot-native, fastest iteration. Best for beginners, solo devs, and teams coming from Python or Lua.
>   **B) C#** — .NET 8+, familiar to Unity developers, stronger IDE tooling (Rider / Visual Studio), slight performance advantage on heavy logic.
>   **C) Both** — GDScript for gameplay/UI scripting, C# for performance-critical systems. Advanced setup — requires .NET SDK alongside Godot.
>
> Which will this project primarily use?"

Record the choice. It determines the INSTRUCTIONS.md template, naming conventions, specialist routing, and which agent is spawned for code files throughout the project.

**For Godot** — use the template matching the language chosen above. Read [Godot language configuration](references/godot-language-configuration.md) for all three variants (GDScript, C#, Both).

**Unity:**
```markdown
- **Engine**: Unity [version]
- **Language**: C#
- **Build System**: Unity Build Pipeline
- **Asset Pipeline**: Unity Asset Import Pipeline + Addressables
```

**Unreal:**
```markdown
- **Engine**: Unreal Engine [version]
- **Language**: C++ (primary), Blueprint (gameplay prototyping)
- **Build System**: Unreal Build Tool (UBT)
- **Asset Pipeline**: Unreal Content Pipeline
```

**[通用产品]** Stack template:
```markdown
- **Language**: [Python / TypeScript / Rust / Go / ...] [version]
- **Framework**: [FastAPI / React / Django / ...] [version]
- **Runtime**: [CPython 3.12 / Node.js 22 / ...]
- **Database**: [PostgreSQL / SQLite / DuckDB / ...]
- **Build System**: [pip / npm / cargo / make / ...]
- **CI/CD**: [GitHub Actions / GitLab CI / ...]
```

---

## 5. Populate Technical Preferences

Read [technology preference templates](references/technical-preferences.md) after the stack is selected. Load the shared sections plus only the chosen engine/language/framework branch. Preserve its collaborative approval boundary before writing project instructions. For section-only work, apply only relevant guidance within Section 1a; remaining defaults are not additional write effects. Preserve configured values and project additions outside approved ranges.

## 6. Determine Knowledge Gap

[通用场景] Check whether the version is beyond LLM training data.

**Known approximate coverage** (update as models change): LLM cutoff: **May 2025**

**[游戏专用]** Engine baselines: Godot ~4.3, Unity ~2023.x/early 6000.x, Unreal ~5.3/early 5.4

**[通用产品]** Framework baselines: Python ~3.12, Django ~5.0, FastAPI ~0.111, React ~18.3, Next.js ~14, Node ~22, TS ~5.4, Rust ~1.78, Go ~1.22

Compare chosen version against baselines:
- **Within training data** → LOW RISK — reference docs optional
- **Near the edge** → MEDIUM RISK — reference docs recommended
- **Beyond training data** → HIGH RISK — reference docs required

---

## 7. Populate Reference Docs

[通用场景]

### If WITHIN training data (LOW RISK):

Create a minimal `docs/engine-reference/<engine>/VERSION.md`:

```markdown
# [Engine] — Version Reference

| Field | Value |
|-------|-------|
| **Engine Version** | [version] |
| **Project Pinned** | [today's date] |
| **LLM Knowledge Cutoff** | May 2025 |
| **Risk Level** | LOW — version is within LLM training data |

## Note

This engine version is within the LLM's training data. Engine reference
docs are optional but can be added later if agents suggest incorrect APIs.

Run `/setup-engine refresh` to populate full reference docs at any time.
```

Do not create the additional reference library merely for a valid LOW-risk baseline.
A governing requirement, migration or concrete compatibility question can still make
an applicable reference necessary; establish and Read that original within the
approved scope. Never use LOW to waive required safety or compatibility checks.

**[通用产品]** For general stacks, create the equivalent file at `docs/reference/<stack>/VERSION.md`:

```markdown
# [Stack] — Version Reference

| Field | Value |
|-------|-------|
| **Stack Version** | [version] |
| **Project Pinned** | [today's date] |
| **LLM Knowledge Cutoff** | May 2025 |
| **Risk Level** | LOW — version is within LLM training data |

## Note

This stack version is within the LLM's training data. Stack reference
docs are optional but can be added later if agents suggest incorrect APIs.

Run `/setup-engine refresh` to populate full reference docs at any time.
```

For a valid LOW-risk Product baseline, do not create the additional library merely
to fill directories. The same governing requirement and actual compatibility rules
above apply; a missing required reference leaves its dependent check Incomplete.

### If BEYOND training data (MEDIUM or HIGH RISK):

Create the full reference doc set by searching the web:

1. **Search for the official migration/upgrade guide**:
   - `"[stack] [old version] to [new version] migration guide"`
   - `"[stack] [version] breaking changes"`
   - `"[stack] [version] changelog"`
   - `"[stack] [version] deprecated API"`

2. **Fetch and extract** from official documentation:
   - Breaking changes between each version from the training cutoff to current
   - Deprecated APIs with replacements
   - New features and best practices

Ask: "May I create the reference docs under `docs/[engine-]reference/<stack>/`?"

Wait for confirmation before writing any files.

3. **Create the full reference directory**:
   ```
   docs/engine-reference/<engine>/
   ├── VERSION.md              # Version pin + knowledge gap analysis
   ├── breaking-changes.md     # Version-by-version breaking changes
   ├── deprecated-apis.md      # "Don't use X → Use Y" tables
   ├── current-best-practices.md  # New practices since training cutoff
   └── modules/                # Per-subsystem references (create as needed)
   ```

4. **Populate each file** using real data from the web searches, following
   the format established in existing reference docs. Every file must have
   a "Last verified: [date]" header.

5. **For module files**: Only create modules for subsystems where significant
   changes occurred. Don't create empty or minimal module files.

**[通用产品]** For general stacks, use `docs/reference/<stack>/` as the root path instead of `docs/engine-reference/`.

---

## 8. Update INSTRUCTIONS.md Import

Show the proposed `@` import change and the exact declared root-instruction
projections affected. Ask for any missing approval for that complete changeset,
then update it using the normal-file procedure in Section 4. Preserve the CDD
source/target boundary sections and separately owned project guidance; no local
maintenance command is a prerequisite.

```markdown
## Version Reference

@docs/engine-reference/<engine>/VERSION.md
```

If the previous import pointed to a different engine (e.g., switching from
Godot to Unity), update it.

**[通用产品]** For general stacks, the import points to `docs/reference/<stack>/VERSION.md` instead.

---

## 9. Update Agent Instructions

[通用场景] Ask before editing. Verify agents have a "Version Awareness" section:
1. Read VERSION.md
2. Check deprecated APIs before suggesting code
3. Check breaking changes for version transitions
4. Use WebSearch to verify uncertain APIs

---

## 10. Refresh Subcommand

[通用场景] `/setup-engine refresh`:

1. Read existing VERSION.md
2. WebSearch for new releases since last verification
3. Update all reference docs with new findings
4. Update "Last verified" dates
5. Report what changed

---

## 11. Upgrade Subcommand

[通用场景] `/setup-engine upgrade [old-ver] [new-ver]`:

### Step 1 — Read Current Version State

Read the VERSION.md to confirm the current pinned version, risk level, and any
migration note URLs already recorded. If `old-ver` was not provided as an
argument, use the pinned version from this file.

- **游戏专用**: `docs/engine-reference/<engine>/VERSION.md`
- **通用产品**: `docs/reference/<stack>/VERSION.md`

### Step 2 — Fetch Migration Guide

Use WebSearch and WebFetch to locate the official migration guide between
`old-ver` and `new-ver`:

- Search: `"[stack] [old-ver] to [new-ver] migration guide"`
- Search: `"[stack] [new-ver] breaking changes changelog"`
- Fetch the migration guide URL from VERSION.md if one is already recorded,
  or use the URL found via search.

Extract: renamed APIs, removed APIs, changed defaults, behavior changes, and
any "must migrate" items.

### Step 3 — Pre-Upgrade Audit

Scan `src/` for code that uses APIs known to be deprecated or changed in the
target version. File types depend on domain:
- **游戏专用**: `.gd`, `.cs`, `.cpp`, `.h`
- **通用产品**: `.py`, `.ts`, `.tsx`, `.rs`, `.go`

Use Grep to search for deprecated API names extracted from the migration
guide (e.g., old function names, removed modules, changed imports).
List each file that matches, with the specific API reference found.

Present the audit results as a table:

```
Pre-Upgrade Audit: [stack] [old-ver] → [new-ver]
==================================================

Files requiring changes:
  File                    | Deprecated API Found    | Effort
  ----------------------- | ----------------------- | ------
  src/api/users.py        | deprecated_function()   | Low
  src/models/base.py      | removed_decorator       | Medium

Breaking changes to watch for:
  - [change description from migration guide]
  - [change description from migration guide]

Recommended migration order (dependency-sorted):
  1. [module with fewest dependencies first]
  2. [next module]
  ...
```

If no deprecated APIs are found in `src/`, report: "No deprecated API usage
found in src/ — upgrade may be low-risk."

### Step 4 — Confirm Before Updating

Ask the user before making any changes:

> "Pre-upgrade audit complete. Found [N] files using deprecated APIs.
> Proceed with upgrading VERSION.md to [new-ver]?
> (This will update the pinned version and add migration notes — it does NOT
> change any source files. Source migration is done manually or via stories.)"

Wait for explicit confirmation before continuing.

### Step 5 — Update VERSION.md

After confirmation:

1. Update `docs/[engine-]reference/<stack>/VERSION.md`:
   - `Version` → `[new-ver]`
   - `Project Pinned` → today's date
   - `Last Docs Verified` → today's date
   - Re-evaluate and update the `Risk Level`
   - Add a `## Migration Notes — [old-ver] → [new-ver]` section
     containing: migration guide URL, key breaking changes, deprecated APIs
     found in this project, and recommended migration order from the audit

2. If `breaking-changes.md` or `deprecated-apis.md` exist in the reference
   directory, append the new version's changes to those files.

### Step 6 — Post-Upgrade Reminder

After updating VERSION.md, output:

```
VERSION.md updated: [stack] [old-ver] → [new-ver]

Next steps:
1. Migrate deprecated API usages in the [N] files listed above
2. Run /setup-engine refresh after upgrading the actual package to
   verify no new deprecations were missed
3. Run /architecture-review — the version upgrade may invalidate ADRs that
   reference specific APIs or framework capabilities
4. If any ADRs are invalidated, run /propagate-design-change to update
   downstream stories
```

---

## 11b. Sync T1 Technical Context

Only when the exact changeset also covers `memory_bank/t1_axioms/tech_context.md`,
and `memory_bank/` exists, update that T1 mirror. Preference-write approval alone
does not cover this separate output; section-only scope follows Section 1a.

Do not create `memory_bank/` from `/setup-engine`. If it does not exist, keep
the normal writes and tell the user to run `/constitute` to establish the
memory_bank governance control plane.

Record these fields in `memory_bank/t1_axioms/tech_context.md`:

- Selected engine, language, framework, runtime, and database as applicable
- Pinned version for each selected technology
- Reason chosen
- Alternatives rejected
- Compatibility constraints
- Knowledge risk
- Reference docs generated
- Last verified date

This T1 context is a memory mirror of the technical decision. `INSTRUCTIONS.md`,
`standards/technical-preferences.md`, and the generated reference docs remain
the detailed working sources.

---

## 12. Output Summary

For section-only work, report `Section Reconfiguration: COMPLETE / INCOMPLETE`,
selected sections, actual changed paths, readback comparison and pending dependent
effects. COMPLETE means the approved edit and byte-preservation checks succeeded;
it does not claim full stack setup or stage qualification. Use full summaries below
only for their full setup scope. Do not label skipped/unexecuted outputs updated
or verified. Recommend the next action for the actual current workflow without
automatically advancing or running it.

**[游戏专用]** Game summary:
```
Engine Setup Complete
=====================
Engine:          [name] [version]
Language:        [GDScript | C# | GDScript + C# | C# | C++ + Blueprint]
Knowledge Risk:  [LOW/MEDIUM/HIGH]
Reference Docs:  [created/skipped]
INSTRUCTIONS.md:       [updated]
Tech Prefs:      [created/updated]
Agent Config:    [verified]

Next Steps:
1. Review docs/engine-reference/<engine>/VERSION.md
2. Continue Technical Setup: run /create-architecture
3. Run /architecture-decision for Foundation-layer decisions
4. Run /architecture-review, then /create-control-manifest
5. Run /test-setup to create the required test baseline
6. Run /gate-check technical-setup before normal advancement to Pre-Production
7. If this was run early from Concept or Systems Design, return to the current phase boundary first: /gate-check concept or /gate-check systems-design as appropriate
```

**[通用产品]** Product summary:
```
Stack Setup Complete
=====================
Stack:           [language] [version] + [framework] [version]
Platform:        [Web / Desktop / Mobile / CLI / Server]
Database:        [PostgreSQL / SQLite / DuckDB / ...]
Knowledge Risk:  [LOW/MEDIUM/HIGH]
Reference Docs:  [created/skipped]
INSTRUCTIONS.md:       [updated]
Tech Prefs:      [created/updated]
Agent Config:    [verified]

Next Steps:
1. Review docs/reference/<stack>/VERSION.md
2. Continue Architecture: run /create-architecture
3. Run /architecture-decision for Foundation-layer decisions
4. Run /architecture-review, then /create-control-manifest
5. Run /test-setup to create the required test baseline
6. Run /gate-check technical-setup before normal advancement to Pre-Implementation
7. If this was run early from Concept or Specification, return to the current phase boundary first: /gate-check concept or /gate-check systems-design as appropriate
```

Verdict: **COMPLETE** — stack configured and reference docs populated.

---

## Guardrails

[通用场景]
- NEVER guess a version — verify via WebSearch or user confirmation
- NEVER overwrite existing reference docs without asking
- If reference docs exist for a different stack, ask before replacing
- Always show the user what you're about to change before making INSTRUCTIONS.md edits
- If WebSearch returns ambiguous results, show the user and let them decide
- Never add speculative dependencies to Allowed Libraries

**[游戏专用]** Godot GDScript guardrail: When user chose GDScript, write Language as exactly "GDScript" — no additions. Do NOT append "C++ via GDExtension".

---

## Appendix A — Godot Language Configuration

For Godot projects only, read [Godot language configuration](references/godot-language-configuration.md) before updating language-specific instructions or specialist routing. Skip this reference for every other stack.
