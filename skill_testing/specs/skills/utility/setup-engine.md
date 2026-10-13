# Skill Test Spec: /setup-engine

## Skill Summary

`/setup-engine` configures the project's engine, language, rendering backend,
physics engine, specialist agent assignments, and naming conventions by
populating `standards/technical-preferences.md`. It accepts an optional engine argument
(e.g., `/setup-engine godot`) to skip the engine-selection step. The skill presents a draft with exact affected paths/effects, reuses matching
named authority, and asks only for missing/new scope before updating.

The skill also populates the specialist routing table (file extension → agent
mappings) based on the chosen engine. It has no director gates — configuration
is a technical utility task. The verdict is always COMPLETE when the file is
fully written.

For root-level project instructions, the skill writes the canonical
`INSTRUCTIONS.md` (never the generated `CLAUDE.md`/`AGENTS.md` directly). When
`INSTRUCTIONS.md` changes, the skill regenerates the runtime root instructions
with the reviewed deterministic root-instruction projections, and
requests any missing authority once for the canonical edit and exact declared
projection outputs. Already covered paths/effects do not require another question.

## Fixture and evidence contract

The cases below describe isolated fixture inputs. Apply the complete current
`/skill-test` owner and `standards/evidence-lifecycle.md`: spec reasoning,
static structure checks, fixture execution and independent review are separate
results. An expected result or fixture description is not a recorded runtime PASS.

Before execution, bind the selected runtime entries, actual governing project
instructions, configuration and required direct/indirect input bytes. Use
`standards/technical-preferences.md` as the canonical preference path.
Read substantive bodies; missing/unread required originals leave the affected
check pending. Optional, example, future-output and inapplicable references are
not required inputs merely because their paths appear in an instruction.

Establish actual CDD provenance, ownership and Source/Target delivery role before
classifying purpose. Source developer templates and complete projections are
framework product assets. In a Target, confirmed CDD packages/support remain
local-only but readable ignored inputs may be discovered, loaded and used within
authority. Project-owned development skills, native roles, tools and documents
retain project rules. A maintenance toolkit is optional for ordinary use.

Reasoning/review-only runs invoke no write entrypoint. Any expected writer action
runs only in an isolated fixture with the exact named paths/effects approved.
Reuse matching authority without repeated per-file/section questions; report-only
covers its assigned new report and excludes inputs/indexes/state. Law/ADR acceptance,
evidence publication, runtime qualification and Story/stage completion remain
separate. Preserve before bytes and disclose unavailable checks.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keyword: COMPLETE
- [ ] Documents actual scoped write authority or the shared-contract owner before
  updating standards/technical-preferences.md; evaluate behavior in the cases
- [ ] Authors root instructions at canonical `INSTRUCTIONS.md` (not `CLAUDE.md`/`AGENTS.md`)
- [ ] References the reviewed deterministic root-instruction projections for regenerating root instructions
- [ ] Has a next-step handoff (e.g., `/brainstorm` or `/constitute` depending on flow)

---

## Director Gate Checks

None. `/setup-engine` is a technical configuration skill. No director gates apply.

---

## Test Cases

### Shared setup fixture inputs

Use an isolated Game project with readable actual canonical `INSTRUCTIONS.md`,
declared plain-copy `AGENTS.md`/`CLAUDE.md` root projections, canonical
`standards/technical-preferences.md`, selected installed setup entry/references
and governing authority/evidence/decision/ownership bodies. Supply the applicable
stack/language preference references and actual specialist definitions, including
their already-present Version Awareness guidance. No role repair is needed.
No Memory Bank exists; setup must not initialize it.

Version choices are user-confirmed fixture pins, not current-release claims:
Godot 4.3, Unity 2022.3, Unreal Engine 5.3. Where the stack-only mode needs a
version lookup, provide a retained read-only official-source response and the
user's exact pin confirmation. Optional post-cutoff libraries are not required
merely to fill reference directories; actual required compatibility originals
remain necessary. The fixture approves the displayed preference/root/declared
projection/version-reference writes once, excluding Source generators, imports,
hooks/runtime activation, package installation and state/index writes.
Case 4 overrides this scope with only the selected preference section effect.
For the missing-authority variant of Cases 1-3, remove only the named write
approval: show the draft/scope and ask before any write. Pending or declined
approval leaves all bytes unchanged; approval covers only the displayed effects.

### Case 1: Godot 4 + GDScript — Full engine configuration

**Fixture:**
- `standards/technical-preferences.md` contains only placeholders
- Engine argument provided: `godot`; user confirms fixture version 4.3,
  chooses GDScript, PC keyboard/mouse input, shared defaults and GUT testing.
- Required Godot language/preference originals are complete/readable; no
  additional reference library or absent T1 mirror is implicitly written.

**Input:** `/setup-engine godot`

**Expected behavior:**
1. Skill skips engine-selection step (argument provided)
2. Skill presents language options for Godot: GDScript or C#
3. User selects GDScript
4. Skill drafts all engine sections: engine/language/rendering/physics fields,
   naming conventions (snake_case for GDScript), specialist assignments
   (godot-specialist, godot-gdscript-specialist, godot-shader-specialist, etc.)
5. Skill populates the routing table: `.gd` → godot-gdscript-specialist, `.gdshader` →
   godot-shader-specialist, `.tscn` → godot-specialist
6. Skill reuses the matching named authority; only missing/new write effects
   require "May I write to `standards/technical-preferences.md`?" after the draft.
7. File is written after approval; verdict is COMPLETE

**Assertions:**
- [ ] Engine field is set to Godot 4 (not a placeholder)
- [ ] Language field is set to GDScript
- [ ] Naming conventions are GDScript-appropriate (snake_case)
- [ ] Routing table includes `.gd`, `.gdshader`, and `.tscn` entries
- [ ] Specialists are assigned (not placeholders)
- [ ] Matching named write authority is reused; missing/new effects ask after
  the draft and before writing. Pending/declined approval produces no writes.
- [ ] Verdict is COMPLETE

---

### Case 2: Unity + C# — Unity-specific configuration

**Fixture:**
- `standards/technical-preferences.md` contains only placeholders
- Engine argument provided: `unity`; user confirms fixture version 2022.3,
  C#, PC input, shared defaults and NUnit testing. Applicable Unity preference
  originals and actual specialist entries are complete/readable.

**Input:** `/setup-engine unity`

**Expected behavior:**
1. Skill sets engine to Unity, language to C#
2. Naming conventions are C#-appropriate (PascalCase for classes, camelCase for fields)
3. Specialist assignments use actual Unity owner routing: unity-specialist for
   primary/C# code, plus the applicable Unity shader/UI and additional specialists
4. Routing table follows the actual preference owner: `.cs` and `.unity`
   (scene) route to unity-specialist, preserving applicable additional file types
5. Skill reuses matching named authority; missing/new effects ask after the
   draft and before writing. Writes remain limited to approved effects.

**Assertions:**
- [ ] Engine field is set to Unity (not Godot or Unreal)
- [ ] Language field is set to C#
- [ ] Naming conventions reflect C# conventions
- [ ] Routing table includes `.cs` and `.unity` entries
- [ ] Verdict is COMPLETE

---

### Case 3: Unreal + Blueprint — Unreal-specific configuration

**Fixture:**
- `standards/technical-preferences.md` contains only placeholders
- Engine argument provided: `unreal`; user confirms fixture version 5.3,
  C++ with Blueprint prototyping, PC input, default budgets and UE Automation.
- Applicable Unreal preference/routing originals and actual specialist entries
  are complete/readable; Blueprint routing remains a required part of the fixture.

**Input:** `/setup-engine unreal`

**Expected behavior:**
1. Skill sets engine to Unreal Engine 5 with the actual C++/Blueprint language
   configuration; Blueprint graph routing is preserved
2. Specialist assignments include unreal-specialist and actual
   ue-blueprint-specialist for Blueprint graph work
3. Routing table: `.uasset` → ue-blueprint-specialist or unreal-specialist,
   `.umap` → unreal-specialist
4. Performance budgets are pre-set with Unreal defaults (e.g., higher draw call budget)
5. Skill reuses matching named authority; only missing/new effects require a
   write-permission question after the draft. Writes remain within approved
   effects; verdict is COMPLETE for the completed configuration.

**Assertions:**
- [ ] Engine field is set to Unreal Engine 5
- [ ] Routing table includes `.uasset` and `.umap` entries
- [ ] Blueprint specialist is assigned
- [ ] Verdict is COMPLETE

---

### Case 4: Engine Already Configured — Offers to reconfigure specific sections

**Fixture:**
- `standards/technical-preferences.md` has fully populated applicable Godot 4.3 /
  GDScript configuration, naming, specialists, input/platform and testing values.
  Budget values are 60 FPS, 16.6 ms, 1000 draw calls and 512 MB; extra project
  prose/comments and routing are retained. Product-only fields are explicitly N/A.
- No engine argument provided. User selects `Performance Budgets only`, requests
  30 FPS / 33.3 ms / 1800 draw calls / 512 MB, and approves only that section effect
  at the canonical preference path. Retain exact before bytes for comparison.

**Input:** `/setup-engine`

**Expected behavior:**
1. Skill reads `standards/technical-preferences.md` and detects fully configured engine (Godot 4)
2. Skill reports: "Engine already configured as Godot 4 + GDScript"
3. Skill presents options: reconfigure all, reconfigure specific section only
   (Engine/Language, Naming Conventions, Specialists, Performance Budgets)
4. User selects "Reconfigure Performance Budgets only"
5. Only the performance budget section is updated; all other fields unchanged
6. Skill shows the selected-section diff and reuses its exact named authority;
   if that authority is absent, asks before writing. No unrelated root/version/
   specialist/T1 output is included in this section-only changeset.
7. Declined-write variant changes no bytes; matching already-approved section
   scope is reused without repeating the permission question.

**Assertions:**
- [ ] Skill does NOT overwrite all fields when only a section update was requested
- [ ] User is offered section-specific reconfiguration
- [ ] Only the selected section is modified in the written file; other sections,
  extra project prose and other output files retain their exact before bytes
- [ ] Verdict is COMPLETE

---

### Case 5: Director Gate Check — No gate; setup-engine is a utility skill

**Fixture:**
- Use Case 1 complete applicable inputs, explicit responses and exact approved
  write scope; no engine is configured before the invocation.

**Input:** `/setup-engine godot`

**Expected behavior:**
1. Skill completes full engine configuration
2. No director agents are spawned at any point
3. No gate IDs appear in output

**Assertions:**
- [ ] No director gate is invoked
- [ ] No gate skip messages appear
- [ ] Verdict is COMPLETE without any gate check

---

## Protocol Compliance

- [ ] Presents draft configuration before asking to write
- [ ] Reuses exact named preference-write authority; missing/new effects ask
  after a concrete draft/scope, with no per-section repetition
- [ ] Writes root instructions to canonical `INSTRUCTIONS.md` and regenerates via the reviewed deterministic root-instruction projections; does not hand-edit `CLAUDE.md`/`AGENTS.md`
- [ ] Respects engine argument when provided (skips selection step)
- [ ] Detects existing config and offers partial reconfigure
- [ ] Routing table is populated for all key file types for the chosen engine
- [ ] Verdict is COMPLETE after file is written

---

## Coverage Notes

- Godot 4 + C# (instead of GDScript) follows the same flow as Case 1 with
  different naming conventions and the godot-csharp-specialist assignment.
  This variant is not separately tested.
- The engine-version-specific guidance (e.g., Godot 4.6 knowledge gap warning
  from VERSION.md) is surfaced by the skill but not assertion-tested here.
- Performance budget defaults per engine are noted as engine-specific but
  exact default values are not assertion-tested.
