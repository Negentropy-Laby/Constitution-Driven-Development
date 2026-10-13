# Skill Test Spec: /help

## Skill Summary

`/help` analyzes what has been done and what comes next in the project workflow.
Its canonical Claude metadata requests Haiku; actual runtime model support is
observed or disclosed unverified. It reads `production/stage.txt`,
the active sprint file, and recent session state to produce a concise situational
guidance summary. The skill optionally accepts a context query (e.g., `/help testing`)
to surface relevant skills for a specific topic.

The output is always informational — no files are written and no director gates
are invoked. The verdict is always HELP COMPLETE. The skill serves as a workflow
navigator, giving one primary recommendation with relevant optional/coming-up guidance.

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
- [ ] Contains verdict keyword: HELP COMPLETE
- [ ] Does NOT contain "May I write" language (skill is read-only)
- [ ] Has one primary next-step handoff, with relevant optional/coming-up guidance

---

## Director Gate Checks

None. `/help` is a read-only navigation skill. No director gates apply.

---

## Test Cases

### Shared navigation fixture inputs

The selected runtime is Codex. Supply the actual catalog, root/ownership/evidence/
decision/domain guidance, complete selected installed skill entries and the required
direct/indirect originals for the recommendations in each fixture. Enumerate actual
frontmatter, then completely read relevant candidate bodies; no full-tree pre-read
or maintenance toolkit is required. Readable ignored CDD inputs remain usable and
project-owned uncataloged capabilities remain project-owned. Missing required
bodies/inputs leave the affected recommendation pending, without installing tools
or substituting an unrelated installed command.

The catalog is authoritative for phase order, required/optional status and domain
applicability. A declared stage and YAML/Markdown status are observations, not
qualified completion. These default/topic invocations are read-only and cover no
report/state/index write, gate invocation or automatic next-skill execution.

### Case 1: Happy Path — Production stage with active sprint

**Fixture:**
- `production/stage.txt` contains `Production`
- Consistent actual root/configuration evidence selects Game with Godot 4.3 +
  GDScript. Governance supports independent Production advice; optional Memory
  Bank absence does not force initialization.
- `production/sprint-status.yaml` is absent deliberately, exercising Markdown
  fallback. The sole active `production/sprints/sprint-004.md` body contains:
  ```markdown
  # Sprint 004
  Status: Active
  ## Tasks
  | ID | Task | Story | Status |
  |---|---|---|---|
  | S4-001 | Combat hitbox | production/epics/combat/story-001-hitbox.md | In Progress |
  | S4-002 | Movement dash | production/epics/movement/story-002-dash.md | In Progress |
  | S4-003 | Stamina HUD | production/epics/stamina/story-003-hud.md | Ready for Dev |
  ```
- Linked Story bodies have matching actual status/governing AC/context and
  retained identities. Execution/closure remains unqualified where NotRun.
- `production/session-state/active.md` identifies the active combat hitbox task.
- Preferred-YAML variant instead adds an actual owner-format projection with
  `sprint: 6`, two linked rows (`in-progress`, `ready-for-dev`), goal/dates,
  generated/updated fields, priority, owner, estimate, blocker and completed
  fields. The older Markdown body remains sprint 004 with three stories, so the
  source preference cannot pass by reporting its stale number/count.

**Input:** `/help`

**Expected behavior:**
1. Skill reads stage.txt and active sprint
2. With absent YAML, skill reads the full active Markdown/linked Story bodies and
   reports sprint 004, 3 total stories and 2 In Progress. With the preferred-YAML
   variant it reports sprint 6, 2 total and 1 In Progress from that projection,
   disclosing conflicting older Markdown without treating either as closure proof.
3. Skill outputs current stage, sprint summary and one primary relevant command
   with secondary optional/coming-up guidance from completely read inputs
4. Suggestions are ranked by relevance to current sprint state
5. Verdict is HELP COMPLETE

**Assertions:**
- [ ] Current stage is shown (Production)
- [ ] Actual active sprint number, total story count and In Progress count are
  reported from the read source: Markdown 004/3/2 without YAML; YAML 6/2/1 when
  present. File-name discovery or session snippets alone do not satisfy this.
- [ ] One primary recommendation is clear; optional/coming-up advice is relevant
- [ ] Suggestions are appropriate for Production stage
- [ ] Verdict is HELP COMPLETE
- [ ] No files are written

---

### Case 2: Concept Stage — Shows concept-to-systems-design workflow path

**Fixture:**
- `production/stage.txt` contains `Concept`
- No sprint files, no GDD files
- `standards/technical-preferences.md` has actual Godot 4.3/GDScript Game values;
  no concept or law set exists. The actual catalog and relevant installed owners
  are complete/readable; setup alone does not qualify Concept completion.

**Input:** `/help`

**Expected behavior:**
1. Skill reads stage.txt — detects Concept stage
2. Skill reads the current catalog and presents its selected Game Concept steps
   in order with their required/optional status, including constitution, concept
   creation and concept review. The current first required gap is primary.
3. `/brainstorm` is relevant discovery/concept guidance after the selected
   `/constitute` route; `/map-systems` and `/design-system` belong to later
   Systems Design, after the actual Concept boundary, rather than a fabricated
   fixed three-command Concept sequence.
4. Current observations are "Engine configured, concept not yet created";
   neither the engine values nor an absent optional Memory Bank imply qualification.

**Assertions:**
- [ ] Stage is identified as Concept
- [ ] Workflow path follows the actual catalog order, required/optional flags
  and selected domain; later Systems Design steps are labelled coming up, not
  substituted for missing Concept constitution/review requirements
- [ ] Suggestions do not include Production-stage skills (e.g., `/dev-story`)
- [ ] Verdict is HELP COMPLETE

---

### Case 3: No stage.txt — Shows full workflow overview

**Fixture:**
- No `production/stage.txt`
- No sprint files
- `standards/technical-preferences.md` has placeholders; neither concept,
  substantive source/Story work nor accepted project law evidence establishes a
  concrete domain or qualified phase. Required neutral guidance is readable.
- An advisory candidate such as Concept does not establish the Unknown declared/
  qualified stage or resolve Game/Product applicability.

**Input:** `/help`

**Expected behavior:**
1. Skill cannot determine stage from stage.txt
2. Skill applies read-only project-stage-detect indicators as advisory reasoning,
   without invoking another skill or inferring qualification from absent artifacts
3. If stage cannot be inferred: outputs the full workflow overview from
   Concept through Release as a reference map
4. Neutral primary suggestion is `/constitute` for the fresh governance request
   or `/project-stage-detect` for unresolved phase; domain-limited actions remain
   pending. The reference overview does not accept laws or advance a phase.

**Assertions:**
- [ ] Skill does not crash when stage.txt is absent
- [ ] Full workflow overview is shown when stage cannot be determined
- [ ] `/constitute` or `/project-stage-detect` is a top suggestion
- [ ] Verdict is HELP COMPLETE

---

### Case 4: Context Query — User asks for help with testing

**Fixture:**
- `production/stage.txt` contains `Production`
- Use Case 1 substantive Game/context and sprint inputs; the active combat Story
  has actual `Status: In Review`, testable combat AC and pending test execution.
- Complete relevant installed definitions and required branch inputs for
  `/qa-plan`, `/smoke-check`, `/regression-suite`, `/test-setup` and
  `/test-evidence-review` are readable. At least three are suitable to this actual
  testing task; their full instructions and required input bodies must be read.
- Limited-candidate variant leaves only two suitable complete-read candidates;
  unavailable required originals are named and affected advice stays pending.
  Installation or an unrelated available skill cannot replace topical relevance.

**Input:** `/help testing`

**Expected behavior:**
1. Skill reads context query: "testing"
2. Skill surfaces the suitable completely read testing candidates above: one
   primary recommendation and relevant secondary choices, at least three when
   those suitable complete inputs are available; disclose a smaller actual set
   in the limited-candidate variant rather than padding or installing.
3. Output is focused on testing workflow, not general sprint navigation
4. Currently in-review story is highlighted as a testing candidate

**Assertions:**
- [ ] Context query is acknowledged in output ("Help topic: testing")
- [ ] At least 3 suitable testing-relevant, complete-read commands are listed
  for the base fixture, with one primary; the limited-candidate variant discloses
  its actual supported count/gaps without padding, unrelated replacements or install
- [ ] General sprint skills (e.g., `/sprint-plan`) are not the primary suggestions
- [ ] Verdict is HELP COMPLETE

---

### Case 5: Director Gate Check — No gate; help is read-only navigation

**Fixture:**
- Use Case 1 complete navigation inputs, actual selected scope and read-only
  invocation; missing unrelated optional state is disclosed.

**Input:** `/help`

**Expected behavior:**
1. Skill produces workflow guidance summary
2. No director agents are spawned
3. No gate IDs appear in output
4. No write tool is called

**Assertions:**
- [ ] No director gate is invoked
- [ ] No write tool is called
- [ ] No gate skip messages appear
- [ ] Verdict is HELP COMPLETE without any gate check

---

## Protocol Compliance

- [ ] Reads actual available stage, selected sprint/Story and session bodies
  before suggestions, using YAML first and complete Markdown fallback when absent;
  missing/ambiguous required sources are disclosed, not fabricated from snippets
- [ ] Suggestions are specific to the current project state (not generic)
- [ ] Context query (if provided) narrows the suggestion set
- [ ] Does not write any files
- [ ] Verdict is HELP COMPLETE in all cases

---

## Coverage Notes

- The case where the active sprint is complete (all stories Done) is not
  separately tested; the skill would suggest `/sprint-plan` for the next sprint.
- Actual runtime support is verified or disclosed unverified; canonical definitions
  do not prove installed/invocable skills.
- Stage detection fallback (when stage.txt is absent) delegates to the same
  logic as `/project-stage-detect` and is not re-tested here in detail.

## False completion and domain cases

**Fixture:** A Product module has artifact paths/min_count and YAML `done` but
required AC remains NotRun; user says “just finished”. Variant retains valid
Game combat/engine/player evidence. Optional Memory Bank is absent.
- [ ] Both branches read applicable substantive contracts/context; neither absent
  concept nor optional memory defaults Game or forces initialization.
- [ ] Paths/counts/keywords are observed, YAML/user statement is declared; required
  NotRun stays unqualified. No checkmark/phase advance from these alone.
- [ ] A copied basic-law template does not establish constitutional ratification.
- [ ] Existing accepted project governance supports independent neutral advice.

**Fixture:** Catalog and canonical skill definitions exist; runtime discovery/
execution is unobserved, and both concept bodies contradict.
- [ ] Conflict/Unknown blocks affected domain advice; neutral guidance continues.
- [ ] Definitions are labeled canonical, not installed; model/tools/memory/loading/
  execution claims need actual runtime evidence.
- [ ] No write entrypoint/state/index repair or automatic next-skill invocation.

### Concrete domain scope and legacy Product aliases

**Fixture:** Two substantive concepts conflict; variant explicitly has mixed
domains but no concrete Game or Product selection. Another variant has no concept
but populated legacy `Language & Framework`, `Platform & Deployment` and
`Agent Routing` with its `File Extension Routing`; new Product Stack is absent.
- [ ] Conflict/mixed variants remain unresolved for dependent catalog filtering
  and single-domain recommendations; do not emit Both as a project route or
  infer completed phases. Neutral guidance continues.
- [ ] Valid legacy Product values route the selected Product scope without
  rewriting/moving them or requiring a new concept/Product Stack.
- [ ] Placeholder aliases do not establish a domain; conflicting new/legacy
  values block only the affected route until clarified.
