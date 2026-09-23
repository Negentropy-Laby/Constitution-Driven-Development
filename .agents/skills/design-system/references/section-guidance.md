# CDD Section Guidance

> Loaded on demand from `design-system/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

### Section-Specific Guidance

Each section has unique design considerations and may benefit from specialist agents:

---

### Section A: Overview

**Goal**: One paragraph a stranger could read and understand.

**Derive recommended options before building the widget**: Read the module's
category, layer, and detected domain from the module index (already in context
from Phase 2), then determine the recommended option for each tab:
- **[游戏专用] Framing tab**: Foundation/Infrastructure layer → `[A]`
  recommended. Player-facing categories (Combat, UI, Dialogue, Character,
  Animation, Visual Effects, Audio) → `[C] Both` recommended.
- **[通用产品] Framing tab**: Foundation/Infrastructure layer → `[A]`
  recommended. User-facing categories (API, CLI, Workflow, UI, Integration)
  → `[C] Both` recommended.
- **ADR ref tab**: Glob `docs/architecture/adr-*.md` and grep for the system
  or module name in the CDD Requirements section of any ADR. If a matching ADR
  is found → `[A] Yes — cite the ADR` recommended. If none found → `[B] No`
  recommended.
- **[游戏专用] Fantasy tab**: Foundation/Infrastructure layer → `[B] No`
  recommended. All other categories → `[A] Yes` recommended.
- **[通用产品] User promise tab**: Foundation/Infrastructure layer → `[B] No`
  recommended. User-facing modules → `[A] Yes` recommended.

Append `(Recommended)` to the appropriate option text in each tab.

**Framing questions (ask BEFORE drafting)**: Use `AskUserQuestion` with a
multi-tab widget selected by domain:

**[游戏专用] Game widget:**
- Tab "Framing" — "How should the overview frame this system?" Options:
  [A] As a data/infrastructure layer (technical framing) / [B] Through its
  player-facing effect (design framing) / [C] Both — describe the data layer
  and its player impact
- Tab "ADR ref" — "Should the overview reference the existing ADR for this
  system?" Options: [A] Yes — cite the ADR for implementation details /
  [B] No — keep the CDD at pure design level
- Tab "Fantasy" — "Does this system have a player fantasy worth stating?"
  Options: [A] Yes — players feel it directly / [B] No — pure
  infrastructure, players feel what it enables

**[通用产品] Product widget:**
- Tab "Framing" — "How should the overview frame this module?" Options:
  [A] As a data/infrastructure layer (technical framing) / [B] Through its
  user-facing value (product framing) / [C] Both — describe the data layer
  and the user value it enables
- Tab "ADR ref" — "Should the overview reference the existing ADR for this
  module?" Options: [A] Yes — cite the ADR for implementation details /
  [B] No — keep the CDD at pure design level
- Tab "User Promise" — "Does this module have a user promise worth stating?"
  Options: [A] Yes — users experience it directly / [B] No — pure
  infrastructure, users experience what it enables

Use the user's answers to shape the draft. Do NOT answer these questions yourself and auto-draft.

**Questions to ask**:
- What is this system in one sentence?
- **[游戏专用]** How does a player interact with it? (active/passive/automatic)
- **[通用产品]** How does a user interact with this module? (API call / UI interaction / CLI command / automated process)
- **[游戏专用]** Why does this system exist — what would the game lose without it?
- **[通用产品]** Why does this module exist — what user value, workflow, API, CLI,
  or operational promise would the product lose without it?

**Cross-reference**: Check that the description aligns with how the module index
describes it. Flag discrepancies.

**Design vs. implementation boundary**: Overview questions must stay at the behavior
level — what the system *does*, not *how it is built*. If implementation questions
arise during the Overview (e.g., "Should this use an Autoload singleton or a signal
bus?"), note them as "→ becomes an ADR" and move on. Implementation patterns belong
in `/architecture-decision`, not the CDD. The CDD describes behavior; the ADR
describes the technical approach used to achieve it.

---

### Section B: Player Fantasy

**Goal**: The emotional target — what the player should *feel*.

**Derive recommended option before building the widget**: Read the system's category and layer from Phase 2 context:
- Player-facing categories (Combat, UI, Dialogue, Character, Animation, Audio, Level/World) → `[A] Direct` recommended
- Foundation/Infrastructure layer → `[B] Indirect` recommended
- Mixed categories (Camera/input, Economy, AI with visible player effects) → `[C] Both` recommended

Append `(Recommended)` to the appropriate option text.

**Framing question (ask BEFORE drafting)**: Use `AskUserQuestion`:
- Prompt: "Is this system something the player engages with directly, or infrastructure they experience indirectly?"
- Options: `[A] Direct — player actively uses or feels this system` / `[B] Indirect — player experiences the effects, not the system` / `[C] Both — has a direct interaction layer and infrastructure beneath it`

Use the answer to frame the Player Fantasy section appropriately. Do NOT assume the answer.

**Questions to ask**:
- What emotion or power fantasy does this serve?
- What reference games nail this feeling? What specifically creates it?
- Is this a "system you love engaging with" or "infrastructure you don't notice"?

**Cross-reference**: Must align with the game pillars. If the system serves a pillar,
quote the relevant pillar text.

**Agent delegation (MANDATORY)**: After the framing answer is given but before drafting,
spawn `creative-director` via Task:
- Provide: system name, framing answer (direct/indirect/both), game pillars, any reference games the user mentioned, the game concept summary
- Ask: "Shape the Player Fantasy for this system. What emotion or power fantasy should it serve? What player moment should we anchor to? What tone and language fits the game's established feeling? Be specific — give me 2-3 candidate framings."
- Collect the creative-director's framings and present them to the user alongside the draft.

**Do NOT draft Section B without first consulting `creative-director`.** The framing
answer tells us *what kind* of fantasy it is; the creative-director shapes *how it's
described* — tone, language, the specific player moment to anchor to.

---

**[通用产品] Section B: User Promise**

**Goal**: The value target — what problem the user hires this module to solve, and
what emotional or functional payoff they receive.

**Framing question (ask BEFORE drafting)**: Use `AskUserQuestion`:
- Prompt: "Is this module something the user engages with directly, or infrastructure they experience indirectly?"
- Options: `[A] Direct — user actively uses or values this module` / `[B] Indirect — user experiences the effects, not the module` / `[C] Both — has a direct interaction layer and infrastructure beneath it`

Use the answer to frame the User Promise section appropriately. Do NOT assume the answer.

**Questions to ask**:
- What job is the user hiring this module to do? (JTBD: "When [situation], I want to [motivation], so I can [outcome].")
- What reference products nail this capability? What specifically creates the experience?
- Is this a "feature users love" or "infrastructure they don't notice"?
- What would the user lose if this module didn't exist?

**Cross-reference**: Must align with the project principles. If the module serves a
principle, quote the relevant principle text.

**Agent delegation (MANDATORY)**: After the framing answer is given but before drafting,
spawn `creative-director` via Task:
- Provide: module name, framing answer (direct/indirect/both), project principles, any reference products the user mentioned, the product concept summary
- Ask: "Shape the User Promise for this module. What value or experience should it deliver? What user moment should we anchor to? Be specific — give me 2-3 candidate framings."
- Collect the creative-director's framings and present them to the user alongside the draft.

**Do NOT draft Section B (User Promise) without first consulting `creative-director`.**

---

### Section C: Detailed Design (Core Rules, States, Interactions)

**Goal**: Unambiguous specification a programmer could implement without questions.

This is usually the largest section. Break it into sub-sections:

**[游戏专用]** Game sub-sections:
1. **Core Rules**: The fundamental mechanics. Use numbered rules for sequential
   processes, bullets for properties.
2. **States and Transitions**: If the system has states, map every state and
   every valid transition. Use a table.
3. **Interactions with Other Systems**: For each dependency (upstream and downstream),
   specify what data flows in, what flows out, and who owns the interface.

**[通用产品]** Product sub-sections:
1. **Core Specification**: The fundamental behavior. Use numbered rules for sequential
   processes, bullets for properties. Describe what the module does, not how it's built.
2. **States and Transitions**: If the module has stateful behavior (e.g., order lifecycle,
   auth session, workflow steps), map every state and every valid transition. Use a table.
3. **Interactions with Other Modules**: For each dependency (upstream and downstream),
   specify what data flows in, what flows out, and who owns the interface.

**[通用场景]** **Questions to ask**:
- Walk me through a typical use of this system, step by step
- **[游戏专用]** What are the decision points the player faces? **[通用产品]** What are the decision points the user faces?
- What can the user NOT do? (Constraints are as important as capabilities)

**Agent delegation (MANDATORY)**: Before drafting Section C, spawn specialist agents via Task in parallel:

**[游戏专用]** Look up the system category in the routing table in [specialist routing](specialist-routing.md). Spawn the Primary Agent AND Supporting Agent(s) listed for this category. Provide each agent: system name, game concept summary, pillar set, dependency CDD excerpts, the specific section being worked on. A `systems-designer` reviewing rules and mechanics will catch design gaps the main session cannot.

**[通用产品]** Look up the module category in the product routing table in [specialist routing](specialist-routing.md). Spawn the Primary Agent (`lead-programmer`) AND the appropriate language specialist. Provide each agent: module name, product concept summary, principle set, dependency CDD excerpts. Collect their findings before drafting. Surface any disagreements between agents to the user via `AskUserQuestion`. Draft only after receiving specialist input.

**Do NOT draft Section C without first consulting the appropriate specialists.**

**Cross-reference**: For each interaction listed, verify it matches what the
dependency CDD specifies. If a dependency defines a value or data structure and this
module expects something different, flag the conflict.

---

### Section D: Formulas

**Goal**: Every mathematical formula, with variables defined, ranges specified,
and edge cases noted.

**Completion Steering — always begin each formula with this exact structure:**

```
The [formula_name] formula is defined as:

`[formula_name] = [expression]`

**Variables:**
| Variable | Symbol | Type | Range | Description |
|----------|--------|------|-------|-------------|
| [name] | [sym] | float/int | [min–max] | [what it represents] |

**Output Range:** [min] to [max] under normal play; [behaviour at extremes]
**Example:** [worked example with real numbers]
```

Do NOT write `[Formula TBD]` or describe a formula in prose without the variable
table. A formula without defined variables cannot be implemented without guesswork.

**Questions to ask**:
- What are the core calculations this system performs?
- Should scaling be linear, logarithmic, or stepped?
- What should the output ranges be at early/mid/late game?

**Agent delegation (MANDATORY)**: Before proposing any formulas or balance values, spawn specialist agents via Task in parallel:
- **Always spawn `systems-designer`**: provide Core Rules from Section C, tuning goals from user, balance context from dependency CDDs. Ask them to propose formulas with variable tables and output ranges.
- **For economy/cost systems, also spawn `economy-designer`**: provide placement costs, upgrade cost intent, and progression goals. Ask them to validate cost curves and ratios.
- Present the specialists' proposals to the user for review via `AskUserQuestion`
- The user decides; the main session writes to file
- **Do NOT invent formula values or balance numbers without specialist input.** A user without balance design expertise cannot evaluate raw numbers — they need the specialists' reasoning.

**Cross-reference**: If a dependency CDD defines a formula whose output feeds into
this system, reference it explicitly. Don't reinvent — connect.

---

---

**[通用产品] Section D: Data Model**

**Goal**: Every data structure, with fields defined, types specified, constraints
noted, and relationships mapped. A programmer should be able to implement the
schema without guessing.

**Completion Steering — always begin each data structure with this exact structure:**

```
The [entity_name] entity is defined as:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| [name] | [string / int / float / bool / uuid / datetime / enum] | Yes / No | [min–max, pattern, enum values] | [what it represents] |

**Relationships:** [Entity A] → [Entity B] (1:1 / 1:N / N:M) via [foreign key / join table / reference field]
**Indexes:** [field] (unique), [field] (range query), [composite: field_a + field_b]
**Example:** [worked example with real data]
```

Do NOT write `[Data model TBD]` or describe data structures in prose without the
field table. A schema without defined types and constraints cannot be implemented
without guesswork — the same principle as the game Formulas section.

**Questions to ask**:
- What are the core data structures this module manages?
- What are the relationships between entities? (1:1, 1:N, N:M)
- What validation rules apply? What are the boundary values?
- Are there any migration concerns? (existing data, schema evolution, backward compatibility)
- What are the access patterns? (read-heavy, write-heavy, mixed — this drives indexing)

**Agent delegation (MANDATORY)**: Before proposing any data models, spawn specialists via Task:
- **Always spawn the language specialist**: provide Core Specification from Section C, tech stack context. Ask them to propose data structures with field tables, types, constraints, and relationships.
- **For data-heavy modules, also spawn `performance-analyst`**: provide the proposed schema. Ask them to flag potential performance issues (N+1 queries, missing indexes, denormalization needs, query patterns against the schema).
- Present the specialists' proposals to the user for review via `AskUserQuestion`
- The user decides; the main session writes to file
- **Do NOT invent data models without specialist input.** Schema design has long-term consequences — the specialist's reasoning about types, constraints, and performance is essential.

**Cross-reference**: If a dependency CDD defines a data structure whose output feeds
into this module, reference it explicitly. Connect, don't reinvent. If this module
owns data that other modules consume, define the contract here.

---

### Section E: Edge Cases

**[通用场景]** **Goal**: Explicitly handle unusual situations so they don't become bugs.

**Completion Steering — format each edge case as:**
- **If [condition]**: [exact outcome]. [rationale if non-obvious]

**[游戏专用]** Examples:
- **If [resource] reaches 0 while [protective condition] is active**: hold at minimum until condition ends, then apply consequence.
- **If two [triggers/events] fire simultaneously**: resolve in [defined priority order]; ties use [defined tiebreak rule].

**[通用产品]** Examples:
- **If [external API] returns 5xx during [operation]**: retry up to [N] times with exponential backoff, then return [fallback response / cached value / error to caller].
- **If [entity] is deleted while [referencing entity] still references it**: [cascade delete / set null / restrict — specify the chosen behavior].

Do NOT write vague entries like "handle appropriately" — each must name the exact
condition and the exact resolution. An edge case without a resolution is an open
design question, not a specification.

**[通用场景]** **Questions to ask**:
- What happens at zero? At maximum? At out-of-range values?
- What happens when two rules apply at the same time?
- **[游戏专用]** What happens if a player finds an unintended interaction? (Identify degenerate strategies) **[通用产品]** What happens if a user finds an unintended workflow? (Identify edge-case paths through the system)

**Agent delegation (MANDATORY)**: **[游戏专用]** Spawn `systems-designer` via Task before finalising edge cases. **[通用产品]** Spawn the language specialist via Task before finalising edge cases. Provide: the completed Sections C and D, and ask them to identify edge cases that the main session may have missed. Present their findings and ask the user which to include.

**Cross-reference**: Check edge cases against dependency CDDs. If a dependency
defines a floor, cap, or resolution rule that this system could violate, flag it.

---

### Section F: Dependencies

**[通用场景]** **Goal**: Map every module connection with direction and nature.

This section is partially pre-filled from the context gathering phase. Present the
known dependencies from the module index and ask:
- Are there dependencies I'm missing?
- For each dependency, what's the specific data interface?
- Which dependencies are hard (module cannot function without it) vs. soft
  (enhanced by it but works without it)?

**[游戏专用]** **Cross-reference**: If this system lists "depends on Combat", then the Combat CDD should list "depended on by [this system]".

**[通用产品]** **Cross-reference**: If this module lists "depends on AuthService", then the Auth CDD should list "depended on by [this module]".

**[通用场景]** Flag any one-directional dependencies for correction.

---

### Section G: Tuning Knobs

**Goal**: Every designer-adjustable value, with safe ranges and extreme behaviors.

**Questions to ask**:
- What values should designers be able to tweak without code changes?
- For each knob, what breaks if it's set too high? Too low?
- Which knobs interact with each other? (Changing A makes B irrelevant)

**Agent delegation**: If formulas are complex, delegate to `systems-designer`
to derive tuning knobs from the formula variables.

**Cross-reference**: If a dependency CDD lists tuning knobs that affect this system,
reference them here. Don't create duplicate knobs — point to the source of truth.

---

---

**[通用产品] Section G: Configuration**

**Goal**: Every configurable parameter, with safe ranges, default values, and
documented behavior at extremes. Operations and developers should be able to
configure this module without reading source code.

**Questions to ask**:
- What values should be configurable without code changes? (environment variables, config files, feature flags, admin panel settings)
- For each parameter, what breaks if it's set too high? Too low? Wrong type?
- Which parameters interact with each other? (Changing A makes B irrelevant, or requires B to also change)
- What are the default values? Why those defaults?
- Which parameters are runtime-configurable vs. require restart/redeploy?
- Are there any secrets (API keys, tokens, passwords) that need special handling?

**Agent delegation**: If configuration is complex or security-sensitive, delegate to the language specialist to validate the configuration design:
- Provide: Core Specification from Section C, dependency list, tech stack context
- Ask: "Validate the configuration parameters. Are the defaults sensible? Are the safe ranges accurate? Are any parameters missing? For secrets, recommend the appropriate vault or environment variable pattern."

**Cross-reference**: If a dependency CDD lists configuration parameters that affect
this module, reference them. Don't create duplicate parameters — point to the source
of truth. If this module's configuration affects downstream modules, note the contract.

---

### Section H: Acceptance Criteria

**[通用场景]** **Goal**: Testable conditions that prove the module works as designed.

**Completion Steering — format each criterion as Given-When-Then:**
- **GIVEN** [initial state], **WHEN** [action or trigger], **THEN** [measurable outcome]

**[游戏专用]** Examples:
- **GIVEN** [initial state], **WHEN** [player action or system trigger], **THEN** [specific measurable outcome].
- **GIVEN** [a constraint is active], **WHEN** [player attempts an action], **THEN** [feedback shown and action result].

**[通用产品]** Examples:
- **GIVEN** a user with [role/permission], **WHEN** they [perform action], **THEN** [specific API response or UI state].
- **GIVEN** [external service] is unavailable, **WHEN** [operation] is attempted, **THEN** [graceful degradation behavior with specific error code].

**[通用场景]** Include at least: one criterion per core rule from Section C, and one per
formula/data structure from Section D. Do NOT write "the system works as designed" —
every criterion must be independently verifiable by a QA tester without reading the CDD.

**Agent delegation (MANDATORY)**: Spawn `qa-lead` via Task before finalising acceptance criteria. Provide: the completed CDD sections C, D, E, and ask them to validate that the criteria are independently testable and cover all core rules and formulas. Surface any gaps or untestable criteria to the user.

**Questions to ask**:
- What's the minimum set of tests that prove this works?
- What performance budget does this system get? (frame time, memory)
- What would a QA tester check first?

**Cross-reference**: Include criteria that verify cross-system interactions work,
not just this system in isolation.

---

### Optional Sections: Visual/Audio, UI Requirements, Open Questions

These sections are included in the template. Visual/Audio is **REQUIRED** for visual system categories — not optional. Determine the requirement level before asking:

**Visual/Audio is REQUIRED (mandatory — do not offer to skip) for these system categories:**
- Combat, damage, health
- UI systems (HUD, menus)
- Animation, character movement
- Visual effects, particles, shaders
- Character systems
- Dialogue, quests, lore
- Level/world systems

For required systems: **spawn `art-director` via Task** before drafting this section. Provide: system name, game concept, game pillars, art bible sections 1–4 if they exist. Ask them to specify: (1) VFX and visual feedback requirements for this system's events, (2) any animation or visual style constraints, (3) which art bible principles most directly apply to this system. Present their output; do NOT leave this section as `[To be designed]` for visual systems.

For **all other system categories** (Foundation/Infrastructure, Economy, AI/pathfinding, Camera/input), offer the optional sections after the required sections:

Use `AskUserQuestion`:
- "The 8 required sections are complete. Do you want to also define Visual/Audio
  requirements, UI requirements, or capture open questions?"
  - Options: "Yes, all three", "Just open questions", "Skip — I'll add these later"

**[游戏专用]** For **Visual/Audio** (non-required systems): Coordinate with `art-director` and `audio-director` if detail is needed. Often a brief note suffices at the CDD stage.

> **Asset Spec Flag**: After the Visual/Audio section is written with real content, output this notice:
> "📌 **Asset Spec** — Visual/Audio requirements are defined. After the art bible is approved, run `/asset-spec system:[system-name]` to produce per-asset visual descriptions, dimensions, and generation prompts from this section."

**[通用产品] Section: Integration Requirements**

**Goal**: External system interfaces, API contracts, and communication patterns.
A developer integrating this module with external services should know exactly
what contracts to implement and what failure modes to handle.

**Determine the requirement level before asking:**

Integration is **REQUIRED (mandatory — do not offer to skip) for these module categories:**
- API modules (REST, GraphQL, gRPC endpoints)
- Data pipeline modules (ETL, stream processing)
- Auth modules (OAuth, SSO, session management)
- Third-party integration modules (payment, email, notifications, external APIs)
- Message queue / event bus modules

For required modules: **spawn `devops-engineer` or `lead-programmer` via Task** before drafting this section. Provide: module name, dependency list, tech stack context. Ask them to specify: (1) API contracts needed (request/response shapes, error codes, rate limits), (2) failure modes that must be handled (timeout, unavailability, data inconsistency), (3) monitoring and alerting requirements. Present their output; do NOT leave this section as `[To be designed]` for integration-heavy modules.

For **all other module categories** (pure logic, utility, internal library), offer Integration as optional after the required sections are complete.

**Questions to ask**:
- What external systems or services does this module integrate with?
- What are the API contracts? (request/response shapes, error codes, rate limits, authentication)
- What happens when the external system is unavailable? (graceful degradation, retry strategy, circuit breaker, fallback behavior)
- What authentication/authorization does the integration require?
- What monitoring or alerting should be in place for this integration?

> **Integration Spec Flag**: After the Integration section is written with real content, output this notice:
> "📌 **Integration Spec** — External integration requirements are defined. Run `/architecture-decision [integration-name]` to record the integration contract as an ADR before implementation begins."

**[通用场景]** For **UI Requirements**: Coordinate with `ux-designer` for complex UI systems.
After writing this section, check whether it contains real content (not just
`[To be designed]` or a note that this system has no UI). If it does have real
UI requirements, output this flag immediately:

> **📌 UX Flag — [System Name]**: This system has UI requirements. In Phase 4
> (Pre-Production), run `/ux-design` to create a UX spec for each screen or
> HUD element this system contributes to **before** writing epics. Stories that
> reference UI should cite `design/ux/[screen].md`, not the CDD directly.
>
> Note this in the module index for this system if you update it.

For **Open Questions**: Capture anything that came up during design that wasn't
fully resolved. Each question should have an owner and target resolution date.

---
