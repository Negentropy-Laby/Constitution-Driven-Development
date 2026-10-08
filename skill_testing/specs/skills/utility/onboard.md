# Skill Test Spec: /onboard

## Skill Summary

`/onboard` reads actual root/canonical guidance, technical preferences, declared
stage, active sprint/Story and role-relevant bodies to produce orientation.
Game vision/engine/art/playtests and Product user promise/API/CLI/data/auth/
workflow receive equivalent relevant context. Default output is conversational;
optional saving uses covered `production/onboarding/onboard-[role]-[date].md`
authority. ONBOARDING COMPLETE concerns the produced orientation only; missing
required sources leave affected material BLOCKED with useful partial guidance.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keyword: ONBOARDING COMPLETE
- [ ] Default analysis writes nothing; optional save applies exact named document authority
- [ ] Has a next-step handoff suggesting a relevant follow-on skill

---

## Director Gate Checks

None. `/onboard` is a read-only orientation skill. No director gates apply.

---

## Test Cases

### Case 1: Happy Path — Configured project in Production stage with active sprint

**Fixture:**
- `production/stage.txt` contains `Production`
- `technical-preferences.md` has engine, language, and specialists populated
- `production/sprints/sprint-005.md` exists with stories in progress
- Git log contains 5 recent commits

**Input:** `/onboard`

**Expected behavior:**
1. Skill reads stage.txt, technical-preferences.md, active sprint, and git log
2. Skill uses its actual onboarding shape: Project Summary, Your Role, Project
   Architecture/Key Directories/Files, Conventions, Current Area/Sprint, Dependencies,
   Pitfalls, First Tasks and Questions; stack/stage/activity come from read sources.
3. Summary is formatted for readability (headers, bullet points)
4. Next-step suggestions are appropriate for Production stage (e.g., `/sprint-status`,
   `/dev-story`)
5. Verdict ONBOARDING COMPLETE is stated

**Assertions:**
- [ ] Output includes current stage name from stage.txt
- [ ] Output includes engine and language from technical-preferences.md
- [ ] Active sprint stories are summarized (not just the sprint file name)
- [ ] Recent commit context is present
- [ ] Verdict is ONBOARDING COMPLETE
- [ ] Default conversational invocation writes no files

---

### Case 2: Fresh Project — No engine, no sprint, suggests /constitute

**Fixture:**
- `technical-preferences.md` contains only placeholders (`[TO BE CONFIGURED]`)
- No `production/stage.txt`
- No sprint files
- No CLAUDE.md overrides beyond defaults

**Input:** `/onboard`

**Expected behavior:**
1. Skill reads all config files and detects unconfigured state
2. Skill produces a minimal summary: "This project has not been configured yet"
3. Output explains the onboarding workflow: `/constitute` → `/setup-engine` → `/brainstorm`
4. Skill suggests running `/constitute` as the immediate next step
5. Verdict is ONBOARDING COMPLETE (informational, not a failure)

**Assertions:**
- [ ] Output explicitly mentions the project is not yet configured
- [ ] `/constitute` is recommended as the next step
- [ ] Skill does NOT error out — it gracefully handles an empty project state
- [ ] Verdict is still ONBOARDING COMPLETE

---

### Case 3: No CLAUDE.md Found — Error with remediation

**Fixture:**
- `CLAUDE.md` file does not exist (deleted or never created)
- All other files may or may not exist

**Input:** `/onboard`

**Expected behavior:**
1. Skill attempts to read CLAUDE.md and fails
2. Skill identifies missing guidance precisely and checks available actual root/canonical sources.
3. Skill uses available actual runtime/canonical guidance and discloses omissions;
   missing a runtime copy alone does not require constitution activation.
4. If required guidance is unavailable, retain supported partial orientation and
   report the affected result BLOCKED instead of fabricating project state.

**Assertions:**
- [ ] Missing actual source is identified, without confusing generated-copy absence with absent governance
- [ ] Remediation follows actual source gap; optional Memory Bank is not silently initialized
- [ ] Supported partial guidance remains available; unknown facts are disclosed
- [ ] Unavailable required orientation is BLOCKED; no all-path COMPLETE despite failure

---

### Case 4: Role-Specific Onboarding — User specifies "artist" role

**Fixture:**
- Fully configured project in Production stage
- `art-bible.md` exists in `design/`
- Active sprint has visual story types (animation, VFX)

**Input:** `/onboard artist`

**Expected behavior:**
1. Skill reads all standard files plus any art-relevant docs (art bible, asset specs)
2. Summary is tailored to the artist role: art bible overview, asset pipeline,
   current visual stories in the active sprint
3. Technical architecture details (code structure, ADRs) are de-emphasized
4. Specialist agents for art/audio are highlighted in the summary
5. Verdict is ONBOARDING COMPLETE

**Assertions:**
- [ ] Role argument is acknowledged in the output ("Onboarding for: Artist")
- [ ] Art bible summary is included if the file exists
- [ ] Current visual stories from the active sprint are shown
- [ ] Technical implementation details are not the primary focus
- [ ] Verdict is ONBOARDING COMPLETE

---

### Case 5: Director Gate Check — No gate; onboard is read-only orientation

**Fixture:**
- Any configured project state

**Input:** `/onboard`

**Expected behavior:**
1. Skill completes the full onboarding summary
2. No director agents are spawned at any point
3. No gate IDs appear in the output
4. No save prompts/writes appear for default conversational analysis.

**Assertions:**
- [ ] No director gate is invoked
- [ ] No write tool is called
- [ ] No gate skip messages appear
- [ ] Verdict is ONBOARDING COMPLETE without any gate check

---

## Protocol Compliance

- [ ] Reads all source files before generating output (no hallucinated project state)
- [ ] Adapts output to project stage (Production ≠ Concept)
- [ ] Respects role argument when provided
- [ ] Default analysis writes no files; covered optional save writes only its document
- [ ] ONBOARDING COMPLETE only for produced orientation; unavailable required scope is BLOCKED

---

## Coverage Notes

- The case where `technical-preferences.md` is missing entirely (as opposed to
  having placeholders) is not separately tested; behavior follows the graceful
  error pattern of Case 3.
- Git history reading is assumed available; offline/no-git scenarios are not
  tested here.
- Discipline roles beyond "artist" (e.g., programmer, designer, producer) follow
  the same tailoring pattern as Case 4 and are not separately tested.

## Paired Product and authority cases

**Fixture:** Configured Product CLI/API/data/auth project without game concept;
user promise/contracts, surface profile and stack reference exist. Variant Game
artist keeps art bible/assets and actual Game input/engine guidance.
- [ ] Read substantive relevant bodies and active Story/sprint, including applicable
  user promise/API/CLI/data/auth/workflow or Game art/player/playtest material.
- [ ] Configured references are distinct from installed/runtime execution claims.
- [ ] Preserve artist example; absent Product gamepad/engine is not a blocker.

**Fixture:** A names optional onboarding document authority, B is report-only for
a different path, C is review-only; neither concept/conflicting sources in variant.
- [ ] A saves only named document without another covered-scope question.
- [ ] B/C never update onboarding/checkpoint/index/state outside authority.
- [ ] Unknown/conflict blocks affected domain advice, not supported neutral guidance.
- [ ] Declared/observed/candidate/qualified facts remain distinct.
