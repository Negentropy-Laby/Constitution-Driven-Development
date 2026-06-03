---
name: brainstorm
description: "Guided concept ideation — from zero idea to a structured concept document. Supports both game and general product domains. Uses professional ideation techniques, user psychology frameworks, and structured creative exploration."
argument-hint: "[domain hint, or 'open'] [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, WebSearch, Task, AskUserQuestion
---

When this skill is invoked:

1. **Parse the argument** for an optional hint (e.g., `roguelike`, `developer tools`,
   `space survival`, `productivity`, `cozy farming`, `health tracking`).
   If `open` or no argument, start from scratch.
   Also resolve the review mode (once, store for all gate spawns this run):
   1. If `--review [full|lean|solo]` was passed → use that
   2. Else read `production/review-mode.txt` → use that value
   3. Else → default to `lean`

   See `.claude/docs/director-gates.md` for the full check pattern.

2. **Detect domain context.

** The hint usually reveals the domain — game-specific hints
   (roguelike, platformer, RPG, FPS, puzzle, farming sim) suggest game mode; general
   hints (SaaS, CLI tool, developer tool, mobile app, data pipeline) suggest product
   mode. If ambiguous, ask during Phase 1. The domain choice affects which frameworks
   and terminology apply at each phase — sections below are marked
   **[通用场景]** (both domains), **[游戏专用]** (game-domain), or **[通用产品]** (product-domain).

3. **Check for existing concept work**:
   - Read `design/cdd/game-concept.md` if it exists — game project, resume
   - Read `design/cdd/product-concept.md` if it exists — general project, resume
   - Read `design/cdd/game-pillars.md` or `design/cdd/principles.md` if either exists

4. **Run through ideation phases** interactively, asking the user questions at
   each phase. Do NOT generate everything silently — the goal is **collaborative
   exploration** where the AI acts as a creative facilitator, not a replacement
   for the human's vision.

   **Use `AskUserQuestion`** at key decision points:
   - Constrained preference questions (domain, scope, team size)
   - Concept selection ("Which 2-3 concepts resonate?") after presenting options
   - Direction choices ("Develop further, explore more, or prototype?")
   - Principle/pillar ranking after concepts are refined
   Write full analysis in conversation text first, then use
   `AskUserQuestion` to capture the decision with concise labels.

   Professional ideation principles to follow:
   - Withhold judgment — no idea is bad during exploration
   - Encourage unusual ideas — outside-the-box thinking sparks better concepts
   - Build on each other — "yes, and..." responses, not "but..."
   - Use constraints as creative fuel — limitations often produce the best ideas
   - Time-box each phase — keep momentum, don't over-deliberate early

---

### Phase 1: Creative Discovery

Start by understanding the person, not the project. Ask these questions
conversationally (not as a checklist).

**[通用场景]** Both domains:

**Practical constraints** (shape the sandbox before ideation).
Bundle these into a single multi-tab `AskUserQuestion` with these exact tab labels:
- Tab "Experience" — "What kind of experience do you most want to create?" Options depend on domain context:
  - **游戏专用**: Challenge & Mastery / Story & Discovery / Expression & Creativity / Relaxation & Flow
  - **通用产品**: Efficiency & Speed / Creativity & Expression / Connection & Collaboration / Insight & Understanding
- Tab "Timeline" — "What's your realistic development timeline?" (Weeks / Months / 1-2 years / Multi-year)
- Tab "Dev level" — "Where are you in your dev journey?" (First project / Shipped before / Professional background)

Use exactly these tab names — do not rename or duplicate them.

**[游戏专用]** Game projects:

**Emotional anchors**:
- What's a moment in a game that genuinely moved you, thrilled you, or made
  you lose track of time? What specifically created that feeling?
- Is there a fantasy or power trip you've always wanted in a game but never
  quite found?

**Taste profile**:
- What 3 games have you spent the most time with? What kept you coming back?
  *(Ask this as plain text — the user must be able to type specific game names freely.
  Do NOT put this in an AskUserQuestion with preset options.)*
- Are there genres you love? Genres you avoid? Why?
- Do you prefer games that challenge you, relax you, tell you stories,
  or let you express yourself? *(Use `AskUserQuestion` for this — constrained choice.)*

**[通用产品]** General product projects:

**Frustration anchors**:
- What's a moment using a tool, app, or service where you thought "this should
  be so much better than this"? What specifically frustrated you?
- Is there a capability or workflow you've always wanted from a tool but never
  quite found?

**Usage profile**:
- What 3 products or tools do you use most heavily? What keeps you loyal?
  *(Ask this as plain text — the user must be able to type specific product names freely.
  Do NOT put this in an AskUserQuestion with preset options.)*
- Are there product categories you love? Categories you avoid? Why?
- Do you prefer tools that make you efficient, help you create, connect you to
  others, or give you insight? *(Use `AskUserQuestion` for this — constrained choice.)*

**Synthesize** the answers into a brief — 3-5 sentences summarizing what you
learned. Read it back and confirm it captures their intent.

- **游戏专用**: Produce a **Creative Brief** — a 3-5 sentence summary of the
  person's emotional goals, taste profile, and constraints.
- **通用产品**: Produce a **Discovery Brief** — a 3-5 sentence summary of the
  person's frustration anchors, usage profile, and constraints.

---

### Phase 2: Concept Generation

Using the discovery brief as a foundation, generate **3 distinct concepts**
that each take a different creative direction.

**[通用场景]** Both domains use the **Mashup Method**:

Combine two unexpected elements. The tension between the two creates the unique hook.

- **游戏专用**: [Genre A] + [Theme B] (e.g., "farming sim + cosmic horror",
  "roguelike + dating sim", "city builder + real-time combat")
- **通用产品**: [Domain A] + [Capability B] (e.g., "spreadsheet + real-time chat",
  "task manager + habit tracker", "note-taking + knowledge graph")

**[游戏专用]** Two additional game-specific techniques:

**Technique: Verb-First Design**
Start with the core player verb (build, fight, explore, solve, survive,
create, manage, discover) and build outward from there. The verb IS the game.

**Technique: Experience-First Design (MDA Backward)**
Start from the desired player emotion (the MDA aesthetic goal: sensation,
fantasy, narrative, challenge, fellowship, discovery, expression, submission)
and work backward to the dynamics and mechanics that produce it.

**[通用产品]** Two additional product-specific techniques:

**Technique: Action-First Design**
Start with the core user action (create, manage, discover, communicate, analyze,
automate, connect, protect) and build outward from there. The action IS the product.

**Technique: Problem-First Design (JTBD backward)**
Start from the user's deepest pain point or unmet need and work backward to the
features and interactions that resolve it. "What job is the user hiring this
product to do? What are they firing?"

JTBD forces to consider:
- **Push** (what's pushing them away from the current solution? — frustration, cost, complexity)
- **Pull** (what's pulling them toward a new solution? — simplicity, speed, integration)
- **Anxiety** (what worries them about switching? — data loss, learning curve, downtime)
- **Habit** (what keeps them with the current solution? — muscle memory, ecosystem lock-in)

**[通用场景]** For each concept, present:

- **Working Title**
- **Elevator Pitch** (1-2 sentences — must pass the "10-second test")
- **Core Action** — **游戏专用**: Core Verb (single most common player action) / **通用产品**: Core Action (single most common user action)
- **Core Promise** — **游戏专用**: Core Fantasy (the emotional promise) / **通用产品**: Core Promise (the emotional/functional payoff)
- **Unique Hook** (passes the "and also" test)
- **Primary Driver** — **游戏专用**: Primary MDA Aesthetic (which emotion dominates?) / **通用产品**: Primary User Need (which user motivation dominates?)
- **Estimated Scope** (small / medium / large)
- **Why It Could Work** (1 sentence on market/audience fit)
- **Biggest Risk** (1 sentence on the hardest unanswered question)

Present all three. Then use `AskUserQuestion` to capture the selection.

**CRITICAL**: This MUST be a plain list call — no tabs, no form fields. Use exactly this structure:

```
AskUserQuestion(
  prompt: "Which concept resonates with you? You can pick one, combine elements, or ask for fresh directions.",
  options: [
    "Concept 1 — [Title]",
    "Concept 2 — [Title]",
    "Concept 3 — [Title]",
    "Combine elements across concepts",
    "Generate fresh directions"
  ]
)
```

Do NOT use a `tabs` field here. This is a plain `prompt` + `options` call.
Never pressure toward a choice — let them sit with it.

---

### Phase 3: Core Experience Design

For the chosen concept, use structured questioning to build the experience
architecture. This is the backbone — if it isn't satisfying in isolation,
no amount of features or content will save it.

**[通用场景]** Ask these as `AskUserQuestion` calls — derive the options from the
chosen concept, don't hardcode them:

1. **Core action feel** — prompt: "What's the primary feel of the core action/interaction?"
   Generate 3-4 options that fit the concept's domain and tone, plus a free-text escape.

2. **Key design dimension** — identify the most important design variable for this
   specific concept and ask about it. Generate options that match. Always include a
   free-text escape.

   - **游戏专用示例**: world reactivity, pacing, player agency, skill ceiling
   - **通用产品示例**: information density, workflow speed, collaboration depth, learning curve

After capturing answers, analyze what makes the core experience satisfying:
- **游戏专用**: Audio feedback, visual juice, timing satisfaction, tactical depth?
- **通用产品**: Responsiveness, visual clarity, feedback quality, friction removal?

**[游戏专用]** Core Loop Design:

**30-Second Loop** (moment-to-moment):
- What structures each moment of play?
- Where does "one more turn" / "one more run" psychology kick in?

**5-Minute Loop** (short-term goals):
- What choices does the player make at this level?
- How do micro-actions chain into completions?

**Session Loop** (30-120 minutes):
- What does a complete play session look like?
- Where are the natural stopping points?
- What's the "hook" that makes them think about the game when not playing?

**Progression Loop** (days/weeks):
- How does the player grow? (Power? Knowledge? Options? Story?)
- What's the long-term goal? When is the game "done"?

**[通用产品]** User Journey Design:

**Micro-Interaction** (seconds):
- What does the user do in the first few seconds of opening the product?
- What single action happens most frequently?

**Task Completion** (minutes):
- What structures micro-interactions into completed tasks?
- Where does "let me just do one more thing" psychology kick in?

**Workflow** (hours):
- What does a complete use session look like? Natural stopping points?
- What's the "hook" that makes them think about the product when not using it?

**Relationship** (days/weeks/months):
- How does the user grow? (Efficiency? Knowledge? Network? Output quality?)
- What's the long-term value? When does the product become indispensable?

**[通用场景]** User Motivation Analysis (based on Self-Determination Theory):

- **Autonomy**: How much meaningful choice does the user have?
  - **游戏专用**: Can the player approach challenges their own way?
  - **通用产品**: Can the user shape the product to their workflow, or does the product dictate it?
- **Competence**: How does the user feel their skill growing?
  - **游戏专用**: Is mastery visible and rewarded?
  - **通用产品**: Is there a visible trajectory from novice to power user?
- **Relatedness**: How does the user feel connected?
  - **游戏专用**: To characters, other players, or the world?
  - **通用产品**: To collaborators, a community, or the work itself?

---

### Phase 4: Principles and Boundaries

**[通用场景]** Both game and product projects use non-negotiable principles to keep
decisions aligned as the project grows. Game studios call them **pillars**; product
teams call them **principles**. The structure is identical.

**[游戏专用]** Game pillars are used by real AAA studios (God of War, Hades, The Last of
Us) to keep hundreds of team members making decisions that all point the
same direction. Even for solo developers, pillars prevent scope creep and
keep the vision sharp.

**[通用产品]** Product principles are used by successful product teams (Linear,
Notion, Figma, Vercel) to keep features aligned with the core promise as
the product grows from MVP to platform. Even for solo builders, principles
prevent "wouldn't it be cool if..." features from diluting the product's
identity.

Collaboratively define **3-5 principles**:
- Each has a **name** and **one-sentence definition**
- Each has a **design test**: "If we're debating between X and Y, this principle
  says we choose __"
- Principles should feel like they create tension with each other — if all
  principles point the same way, they're not doing enough work

Real-world examples:
- **游戏专用**: God of War's "visceral combat", Hades' "every run teaches something new",
  Celeste's "tough but fair"
- **通用产品**: "Local-first: everything works offline by default", "Progressive
  disclosure: complexity is earned, not inflicted", "API stability: no breaking
  changes without a documented migration path"

Then define **3+ anti-principles** (what this project is NOT):
- Format: "We will NOT do [thing] because it would compromise [principle]"
- Anti-principles prevent scope creep — "wouldn't it be cool if..."

**Principle confirmation**: After presenting the full principle set, use `AskUserQuestion`:
- Prompt: "Do these principles feel right for your project?"
- Options: `[A] Lock these in` / `[B] Rename or reframe one` / `[C] Swap one out` / `[D] Something else`

If the user selects B, C, or D, make the revision, then use `AskUserQuestion` again:
- Prompt: "Principles updated. Ready to lock these in?"
- Options: `[A] Lock these in` / `[B] Revise another principle` / `[C] Something else`

Repeat until the user selects [A] Lock these in.

**Review mode check** — apply before spawning CD-PILLARS and AD-CONCEPT-VISUAL:
- `solo` → skip both. Proceed to Phase 5.
- `lean` → skip both (not PHASE-GATEs). Proceed to Phase 5.
- `full` → spawn as normal.

**After principles are agreed, spawn BOTH `creative-director` AND `art-director` via Task in parallel.

**

- **`creative-director`** — gate **CD-PILLARS** (`.claude/docs/director-gates.md`)
  - **游戏专用**: Pass: full pillar set, anti-pillars, core fantasy, unique hook.
  - **通用产品**: Pass: full principle set, anti-principles, core promise, unique hook.
    Frame: "Review these product principles for coherence, tension, and falsifiability."

- **`art-director`** — gate **AD-CONCEPT-VISUAL** (`.claude/docs/director-gates.md`)
  - **游戏专用**: Pass: game concept elevator pitch, pillars, target platform, reference games.
  - **通用产品**: Pass: product elevator pitch, principles, target platform, reference products.
    Frame: "Propose 2-3 named visual/brand identity directions with visual rules."

Collect both verdicts, present together using a two-tab `AskUserQuestion`:
- Tab **"Principles"**: creative-director feedback. Options: `Lock in as-is` / `Revise [specific]` / `Discuss further`.
- Tab **"Visual anchor"**: art-director's 2-3 named visual directions. Options: each direction + `Combine elements` + `Describe my own`.

The user's selected visual anchor (the named direction or their custom
description) is stored as the **Visual Identity Anchor** — it will be written
into the concept document. **游戏专用**: becomes the foundation of the
**art bible**. **通用产品**: becomes the foundation of the **design system**.

If creative-director returns CONCERNS or REJECT, resolve before visual selection.

---

### Phase 5: Audience Validation

Validate who this is actually for.

**[游戏专用]** Player Type Validation:

Using the Bartle taxonomy and Quantic Foundry motivation model:
- **Primary player type**: Who will LOVE this game? (Achievers, Explorers,
  Socializers, Competitors, Creators, Storytellers)
- **Secondary appeal**: Who else might enjoy it?
- **Who is this NOT for**: Being clear about who won't like this game is as
  important as knowing who will
- **Market validation**: Are there successful games that serve a similar
  player type? What can we learn from their audience size?

**[通用产品]** User Validation:

Using user persona and Jobs-to-be-Done frameworks:
- **Primary user**: Who will LOVE this product? Describe concretely — not
  "developers" but the specific person, context, and frustration.
- **The Job they're hiring for** (JTBD): "When [situation], I want to [motivation],
  so I can [outcome]."
- **Secondary appeal**: Who else might find value?
- **Who is this NOT for**: Prevents building for the wrong user.
- **Switching trigger**: What event or frustration would make the target user
  switch from their current solution to this product?
- **Market validation**: Successful products serving a similar user? What do their
  users complain about most?

---

### Phase 6: Scope and Feasibility

Ground the concept in reality.

**[通用场景]** Both domains:

- **MVP definition**: What's the absolute minimum build that tests the core hypothesis?
  - **游戏专用**: "Is the core loop fun?"
  - **通用产品**: "Does the core interaction solve the user's job?"
- **Biggest risks**: Technical, design, market — **通用产品 adds**: adoption risks
- **Scope tiers**: Full vision vs. what ships if time runs out

**[游戏专用]** Game-specific feasibility:

- **Target platform**: Use `AskUserQuestion` — "What platforms are you targeting for this game?"
  Options: `PC (Steam / Epic)` / `Mobile (iOS / Android)` / `Console` / `Web / Browser` / `Multiple platforms`
  Record the answer — it directly shapes the engine recommendation and will be passed to `/setup-engine`.
  Note platform implications if relevant (e.g., mobile means Unity is strongly preferred; console means Godot has limitations; web means Godot exports cleanly).
- **Engine experience**: Use `AskUserQuestion` — "Do you already have an engine you work in?"
  Options: `Godot` / `Unity` / `Unreal Engine 5` / `No preference — help me decide`
  - If they pick an engine → record it as their preference and move on. Do NOT second-guess it.
  - If "No preference" → tell them: "Run `/setup-engine` after this session — it will walk you through the full decision based on your concept and platform target." Do not make a recommendation here.
- **Art pipeline**: What's the art style and how labor-intensive is it?
- **Content scope**: Level/area count, item count, gameplay hours

**[通用产品]** Product-specific feasibility:

- **Target platform**: Use `AskUserQuestion` — "What platforms are you targeting for this product?"
  Options: `Web (browser)` / `Desktop (Windows/macOS/Linux)` / `Mobile (iOS/Android)` / `CLI / Server` / `Multiple platforms`
  Record the answer — it directly shapes the stack recommendation and will be passed to `/setup-engine`.
  Note platform implications if relevant (e.g., mobile-first means offline support and battery impact matter; web means accessibility and SEO are critical; CLI means composability and scripting matter; server means throughput and concurrency model matter).
- **Tech stack experience**: Use `AskUserQuestion` — "Do you already have a tech stack you work in?"
  Options: `Python ecosystem (Django, FastAPI, Flask)` / `JavaScript/TypeScript (React, Next.js, Node)` / `Rust` / `Go` / `No preference — help me decide`
  - If they pick a stack → record it as their preference and move on. Do NOT second-guess it.
  - If "No preference" → tell them: "Run `/setup-engine` after this session — it will walk you through the full decision based on your concept and platform target." Do not make a recommendation here.
- **Design system**: What's the visual complexity and labor intensity?
- **Feature scope**: Screen count, integration count, user personas served

**[通用场景]** Review mode checks and gates:

**Review mode check** — apply before spawning TD-FEASIBILITY:
- `solo` → skip. Note: "TD-FEASIBILITY skipped — Solo mode." Proceed directly to scope tier definition.
- `lean` → skip (not a PHASE-GATE). Note: "TD-FEASIBILITY skipped — Lean mode." Proceed directly to scope tier definition.
- `full` → spawn as normal.

**After identifying biggest technical risks, spawn `technical-director` via Task using gate TD-FEASIBILITY (`.claude/docs/director-gates.md`) before scope tiers are defined.

**

- **游戏专用**: Pass core loop description, platform, engine choice, technical risks.
- **通用产品**: Pass core user journey, platform, tech stack choice, technical risks.

Present the assessment to the user. If HIGH RISK, offer to revisit scope before finalising. If CONCERNS, note them and continue.

**Review mode check** — apply before spawning PR-SCOPE:
- `solo` → skip. Note: "PR-SCOPE skipped — Solo mode." Proceed to document generation.
- `lean` → skip (not a PHASE-GATE). Note: "PR-SCOPE skipped — Lean mode." Proceed to document generation.
- `full` → spawn as normal.

**After scope tiers are defined, spawn `producer` via Task using gate PR-SCOPE (`.claude/docs/director-gates.md`).

**

Pass: full vision scope, MVP definition, timeline estimate, team size.

Present the assessment to the user. If UNREALISTIC, offer to adjust the MVP definition or scope tiers before writing the document.

---

4. **Generate the concept document**.

   - **游戏专用**: Template `.claude/docs/templates/game-concept.md` → write `design/cdd/game-concept.md`
   - **通用产品**: Template `.claude/docs/templates/product-concept.md` → write `design/cdd/product-concept.md`

   Include a **Visual Identity Anchor** section with the selected visual direction,
   one-line visual rule, supporting principles, and design philosophy summary.

   Fill in ALL sections from the ideation conversation. **游戏专用**: including the
   MDA analysis, player motivation profile, and flow state design sections.

5. Use `AskUserQuestion` for write approval:
- Prompt: "Concept is ready. May I write it?"
- Options: `[A] Yes — write it` / `[B] Not yet — revise a section first`

If [B]: ask which section to revise using `AskUserQuestion`. **游戏专用** options: `Elevator Pitch` / `Core Fantasy & Unique Hook` / `Pillars` / `Core Loop` / `MVP Definition` / `Scope Tiers` / `Risks` / `Something else — I'll describe`. **通用产品** options: `Elevator Pitch` / `Core Promise & Unique Hook` / `Principles` / `User Journey` / `MVP Definition` / `Scope Tiers` / `Risks` / `Something else — I'll describe`.

After revising, show the updated section as a diff or clear before/after, then use `AskUserQuestion` — "Ready to write the updated concept document?"
Options: `[A] Yes — write it` / `[B] Revise another section`
Repeat until the user selects [A].

**Scope consistency rule**: The "Estimated Scope" field must match the full-vision
timeline from Scope Tiers — not just "Large (9+ months)". Write as "Large (X–Y months,
solo)" or "Large (X–Y months, team of N)".

6. **Suggest next steps** (in order). List ALL steps — do not abbreviate:

   **[游戏专用]** Game pipeline:
   1. "Run `/constitute` — derive your constitution from this concept (if you haven't already). It reads your concept doc, extracts core thesis and principles, and writes them to the memory bank."
   2. "Run `/setup-engine` to configure the engine"
   3. "Run `/art-bible` to define visual identity before CDDs"
   4. "Run `/design-review design/cdd/game-concept.md` to validate"
   5. "Refine pillars with `creative-director` agent"
   6. "Run `/map-systems` — decompose into systems with dependencies"
   7. "Run `/design-system` — per-system CDDs"
   8. "Run `/design-review design/cdd/[system].md` after each CDD"
   9. "Run `/review-all-gdds` — holistic cross-CDD review before architecture"
   10. "Run `/gate-check` — validate Systems Design readiness"
   11. "Run `/create-architecture` — master architecture blueprint"
   12. "Run `/architecture-decision (×N)` — record technical decisions"
   13. "Run `/create-control-manifest` — extract implementation rules from accepted ADRs"
   14. "Run `/architecture-review` — validate traceability and technology compatibility"
   15. "Run `/prototype [core-mechanic]` — validate the core loop before full implementation"
   16. "Run `/playtest-report` after the prototype to validate the core hypothesis"
   17. "If validated, plan the first sprint with `/sprint-plan new`"

   **[通用产品]** Product pipeline:
   1. "Run `/constitute` — derive your constitution from this concept (if you haven't already)"
   2. "Run `/setup-engine [framework]` to configure your technology stack"
   3. "Run `/design-review design/cdd/product-concept.md` to validate"
   4. "Refine principles with `creative-director` agent"
   5. "Run `/map-systems` — decompose into modules with dependencies"
   6. "Run `/design-system [module]` — per-module specs"
   7. "Run `/design-review design/cdd/[module].md` after each CDD"
   8. "Run `/review-all-gdds` — holistic cross-CDD review before architecture"
   9. "Run `/gate-check` — validate Specification readiness"
   10. "Run `/create-architecture` — master architecture blueprint"
   11. "Run `/architecture-decision (×N)` — record technical decisions"
   12. "Run `/create-control-manifest` — extract implementation rules from accepted ADRs"
   13. "Run `/architecture-review` — validate traceability and technology compatibility"
   14. "Run `/prototype [core-interaction]` — validate the core user journey before full implementation"
   15. "Run user testing sessions after the prototype to validate the core hypothesis"
   16. "If validated, plan the first sprint with `/sprint-plan new`"

7. **Output a summary** with the chosen concept's elevator pitch, principles,
   primary audience, biggest risk, and file path.
   - **游戏专用**: include engine recommendation in the summary.
   - **通用产品**: include tech stack recommendation in the summary.

Verdict: **COMPLETE** — concept created and handed off for next steps.

---

## Context Window Awareness

This is a multi-phase skill. If context reaches or exceeds 70% during any phase,
append this notice:

> **Context is approaching the limit (≥70%).

** The concept document is saved
> to disk. **游戏专用**: `design/cdd/game-concept.md`. **通用产品**: `design/cdd/product-concept.md`.
> Open a fresh Claude Code session to continue — progress is not lost.

---

## Recommended Next Steps

**[游戏专用]** After the game concept is written:
1. `/constitute` — derive your constitution from this concept
2. `/setup-engine` — configure the engine
3. `/art-bible` — establish visual identity before CDDs
4. `/design-review design/cdd/game-concept.md` — validate concept completeness
5. `/map-systems` — decompose into systems
6. `/design-system [first-system]` — per-system CDDs
7. `/design-review design/cdd/[system].md` — validate each completed CDD
8. `/review-all-gdds` — holistic cross-CDD review before architecture
9. `/gate-check` — validate Systems Design readiness
10. `/create-architecture` — master architecture blueprint
11. `/architecture-decision (×N)` — record technical decisions
12. `/create-control-manifest` — extract implementation rules from accepted ADRs
13. `/architecture-review` — validate traceability and compatibility

**[通用产品]** After the product concept is written:
1. `/constitute` — derive your constitution from this concept
2. `/setup-engine [framework]` — configure the technology stack
3. `/design-review design/cdd/product-concept.md` — validate concept completeness
4. `/map-systems` — decompose into modules
5. `/design-system [first-module]` — per-module specs
6. `/design-review design/cdd/[module].md` — validate each completed CDD
7. `/review-all-gdds` — holistic cross-CDD review before architecture
8. `/gate-check` — validate Specification readiness
9. `/create-architecture` — master architecture blueprint
10. `/architecture-decision (×N)` — record technical decisions
11. `/create-control-manifest` — extract implementation rules from accepted ADRs
12. `/architecture-review` — validate traceability and compatibility
