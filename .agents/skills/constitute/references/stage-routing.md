# Constitution Stage Routing

> Loaded on demand from `constitute/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## Phase 2: Route Based on Detected Stage

Present findings to the user and route based on stage.

### Stage 0: Empty (nothing exists)

The user has no concept and no artifacts. Discovery must come before principles.

Two questions establish the user's context. Ask the domain question FIRST so the
path options can use domain-appropriate examples. Use two sequential
`AskUserQuestion` calls:

**Question 1 — Domain:**

- **Prompt**: "Welcome to Constitution Driven Development! Before I suggest anything, two quick questions. First: what kind of project is this?"
- **Options**:
  - `A game` — 2D/3D interactive experience (any genre, any engine)
  - `A general product` — web app, CLI tool, API, library, mobile app, data pipeline, or something else
  - `I'm not sure yet` — still exploring, haven't decided

Record the domain choice. If "I'm not sure yet", note that the domain can be
clarified later — use generic terminology for now.

**Question 2 — Starting point:**

Use the domain answer to tailor the examples in parentheses. If "not sure",
show both game and product examples for each option.

- **Prompt**: "Where are you starting from?"
- **Options**:
  - `A) Starting fresh` — No code, no specs, no concrete plan. I want to explore what to build. ([domain examples])
  - `B) Rough idea` — I have a domain, problem, or direction in mind, but nothing formalized. ([domain examples])
  - `C) Clear spec` — I know the core problem, approach, and constraints. ([domain examples])
  - `D) Existing project` — I already have code, docs, or significant work done. I want to establish constitutional governance on top of it.
  - `E) Just browsing` — I want to see what's available without committing to a path. Show me the pipeline and let me decide later.

**Domain-specific examples for options:**
- **Game examples**: A) no genre picked yet. B) "something with space" or "a cozy farming game." C) know the genre, core mechanic, target platform.
- **Product examples**: A) no problem domain chosen. B) "a developer tool" or "a health tracking app." C) know the user need, core workflow, target platform.
- **Not sure yet**: show both game and product examples.

Wait for the user's selection. Do not proceed until they respond.

#### If A: Starting fresh

The user needs discovery before anything else. Domain was already established in
Question 1 — do not ask again.

1. Acknowledge that starting from zero is completely fine
2. Explain what `/brainstorm` does — guided ideation using professional frameworks.
   Mention it supports both game (MDA, verb-first, player psychology) and product
   (JTBD, action-first, user psychology) domains. It has two modes:
   `/brainstorm open` for fully open exploration, or `/brainstorm [hint]` if the
   user has even a vague theme (e.g., "space", "cozy", "developer tools").
3. Recommend running `/brainstorm open` as the next step, but invite them to use
   a hint if something comes to mind
4. Note: "Return to `/constitute` after `/brainstorm` — it will detect your new
   concept and derive a constitution from it."
5. Show the recommended path from Phase 7 (full pipeline with all commands for
   their domain). If the user answered "I'm not sure yet" for domain, show both
   game and product pipelines and note that the domain will be clarified during
   `/brainstorm`.
6. **Phase 3d — Review Mode.** Check if `production/review-mode.txt` exists.
   If not, use `AskUserQuestion`: Full / Lean (recommended) / Solo. Write choice.
   Create `production/` directory if needed.
7. **Phase 7 — Confirmation.** Use `AskUserQuestion`: "Which step would you like
   to start with?" Options: `Run /brainstorm open (recommended)` / `Something else — I'll tell you`.
8. When confirmed: "Type `/brainstorm open` to begin."

#### If B: Rough idea

Domain was already established in Question 1 — do not ask again.

1. Ask them to share their rough idea — a domain, a problem, a direction. Use
   plain text, not AskUserQuestion (it's an open response).
2. Validate the idea as a starting point (don't judge or redirect)
3. Recommend running `/brainstorm [their hint]` to develop it
4. Note: "Return to `/constitute` after `/brainstorm`."
5. Show the pipeline from Phase 7 (full pipeline with all commands for their domain).
6. **Phase 3d — Review Mode.** Check `production/review-mode.txt`. If not set,
   use `AskUserQuestion`: Full / Lean (recommended) / Solo. Write choice.
7. **Phase 7 — Confirmation.** Use `AskUserQuestion`: "Which step would you like
   to start with?" Options: `Run /brainstorm [hint] (recommended)` / `Something else`.
8. When confirmed: "Type `/brainstorm [hint]` to begin."

#### If C: Clear spec

1. Ask them to describe the project in one sentence — what it does and for whom.
   Use plain text, not AskUserQuestion (it's an open response).
2. Acknowledge the concept, then use `AskUserQuestion` to offer the choice —
   jump straight to domain tools or formalize the constitution first:
   - **Prompt**: "How would you like to proceed?"
   - **Options**:
     - `Formalize your constitution first` — Establish governing principles before diving into design. Recommended for teams, first-time projects, or when you want clear guardrails before creative work.
     - `Jump straight to your domain workflow` — Skip constitution legislation. Go directly to Phase 3d (Review Mode), then see the pipeline. You can establish principles later.
3. If "Formalize": proceed to Phase 3a (Core Thesis) — domain was already established
   in Question 1. After Phase 3e ratification, proceed to Phase 3f handoff.
   If "Jump straight": write a minimal concept document FIRST. Use the appropriate
   template: game → `design/cdd/game-concept.md`, product → `design/cdd/product-concept.md`.
   Fill core identity fields from the user's description. Mark remaining sections as
   `[To be designed]`. Note: "This is a minimal concept. Run `/brainstorm` later to
   expand it." Then proceed to Phase 3d (Review Mode), then Phase 7 (Pipeline).

#### If D: Existing project

Validate against Phase 1 findings:
- If artifacts DO exist: route to the appropriate Stage (1-4) based on what was found.
- If NO artifacts found (user selected D but project is empty): gently redirect —
  "It looks like the project is a fresh template with no artifacts yet. Would
  Path A or B be a better fit?"

Share what you found in Phase 1: "I can see [X source files / Y design docs /
Z production artifacts]. Your project already has [code / docs / structure]."

#### If E: Just browsing

The user wants to explore without committing. No constitution work, no routing
to a specific skill.

1. Present a high-level overview of the entire pipeline for their domain (or
   both domains if "not sure yet").
2. List the key skills and what each one does, organized by phase.
3. Note: "When you're ready, type the command for any phase. `/constitute` will
   always be here if you want to establish a constitution later."
4. Use `AskUserQuestion`:
   - **Prompt**: "That's the full pipeline. What would you like to know more about?"
   - **Options**:
     - `Tell me more about [first phase skill]` — Explain one skill in detail
     - `I'll explore on my own` — Stop here
     - `Actually, I'm ready to start — take me to Path [A/B/C/D]`
   If "Actually ready": re-run the path selection as if the user had picked
   that path originally.

### Edge Cases (Stage 0)

- **User picks D but project is empty**: Gently redirect — "It looks like the
  project is a fresh template with no artifacts yet. Would Path A or B be a
  better fit?"
- **User picks A but project has code**: Mention what you found — "I noticed
  there's already code in `src/`. Did you mean to pick D (existing project)?"
- **User doesn't fit any option**: Let them describe their situation in their
  own words and adapt.
- **Domain is "I'm not sure yet"**: Use generic terminology throughout. Show
  both game and product pipelines when presenting the path. Note that the domain
  will be clarified during `/brainstorm`. If the user later invokes
  `/constitute` after clarifying their domain, Stage 1 will detect the concept
  doc and derive the constitution with the correct domain context.
- **User picks E then wants to start a path**: Re-run the path selection
  from Path A/B/C/D as if the user had picked it originally. Do not ask the
  domain question again — it was already established in Question 1.

### Stage 1: Concept only (concept doc exists, no constitution)

The ideal moment — concept doc has all the raw material.

Read the concept document fully. Extract:
- **Core thesis** ← elevator pitch / core identity section
- **Principles** ← pillars / product principles section
- **Domain** ← from document content (game-concept → game, product-concept → product)
- **Tech direction** ← platform targets, engine/stack preferences

Present the extracted summary:
```
## Constitution Derivation from Concept

Core thesis: [extracted from concept doc]
Principles found: [N]
  [list each pillar/principle with its design test]
Domain: [game / product]
Tech direction: [extracted platform/engine preferences]
```

Use `AskUserQuestion`:
- **Prompt**: "I've read your concept document. Here's what I can derive. How would you like to proceed?"
- **Options**:
  - `Derive from concept — review each section` — Show each section for approval before writing. (Recommended)
  - `Customize first` — I want to refine the extracted content before we start the approval flow.
  - `Start from scratch` — Ignore the concept doc. I'll define the constitution manually.

If "Derive": proceed to Phase 4 (Derivation Workflow).
If "Customize": show each extracted section for user editing, then Phase 4.
If "Start from scratch": proceed to Phase 3 (Interactive Legislation).

### Stage 2: Designed (module index + CDDs exist)

"Your project has [N] CDDs. I can derive a constitution and validate it
against your design decisions."

Read: concept doc, module index, all CDDs.
Additionally, run a **principle alignment check**: for each principle derived
from the concept, check whether existing CDDs follow it. Flag contradictions.

Present the extracted summary with alignment notes. Same `AskUserQuestion`
options as Stage 1, plus:
- `Skip — just show the pipeline`

### Stage 3: Architected (ADRs exist)

"Your project has [N] CDDs and [M] ADRs. I can derive a constitution and
validate it against your architecture decisions."

Read: concept doc, module index, all CDDs, all ADRs.
For each principle derived, check:
- Which ADRs support it → ✓ ALIGNED
- Which ADRs are silent → ⚠ UNVALIDATED
- Which ADRs potentially conflict → ⚠ CONCERN

Present the derivation summary with ADR-level alignment. Same options as Stage 2.

### Stage 4a: Source only (source code, no production artifacts)

"Your project has source code but no production artifacts. Let's figure out
where you are before establishing governance."

Run a lightweight audit (concept doc + CDDs + ADRs + source, if available).
Present findings, then use `AskUserQuestion`:
- **Prompt**: "Your project is in development but not formally tracked. What would you like to do?"
- **Options**:
  - `Assess my phase` — Run `/project-stage-detect` to determine where you are in the pipeline
  - `Audit constitution` — Run `/constitute-check` to check alignment between code and principles (if constitution exists)
  - `Derive constitution now` — Establish governance from existing artifacts (Phase 4)
  - `Skip — just show the pipeline`

### Stage 4b: Implemented (source code + production artifacts)

"Your project is in active development. I can audit your existing constitution
(or derive one) and check whether your code follows your principles."

Read: everything (concept, CDDs, ADRs, source code).

If constitution exists: run a **full alignment audit**:
- For each principle, grep `src/` for evidence
- Compare constitution date against latest CDD/ADR dates
- Flag: ALIGNED / CONCERN / STALE / GAP per principle

If no constitution: derive from concept + CDDs + ADRs as in Stage 3.

Present the audit report. Use `AskUserQuestion`:
- **Prompt**: "Audit complete. What would you like to do?"
- **Options**:
  - `Amend constitution` — Update principles to reflect current reality (Phase 6)
  - `Derive new constitution` — Create from scratch using existing artifacts (Phase 4)
  - `Skip — just show the pipeline`

### Stage 5: Constitution exists (returning user)

Read the existing constitution and `active_context.md` for version/changelog.

Present current status:
```
## Constitution Status
Version: [N]
Last amended: [date]
Last sign-off: [date] by [author]
Principles: [N] active, [M] superseded, [K] deprecated
Last concept update: [date]
Last ADR: [date]
```

Use `AskUserQuestion`:
- **Prompt**: "Your constitution exists. What would you like to do?"
- **Options**:
  - `Audit alignment` — Run /constitute-check to verify principles against code/ADRs
  - `Amend constitution` — Guided amendment workflow (Phase 6)
  - `Revise from source` — Re-derive from concept doc/CDDs (if they've changed). Routes to Phase 6 amendment workflow.
  - `Show pipeline` — Just show me the recommended path from here

---
