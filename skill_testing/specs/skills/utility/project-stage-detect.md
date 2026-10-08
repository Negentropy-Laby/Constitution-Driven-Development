# Skill Test Spec: /project-stage-detect

## Skill Summary

`/project-stage-detect` diagnoses actual Game/Product bodies and capability
evidence, separating declared, observed, advisory candidate and qualified state.
It never advances stage/current state. Default output is conversational; optional
report save needs covered report-only authority. Confidence reflects actual
diagnostic evidence/omissions, not existence-based qualification.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains all seven stage names: Concept, Systems Design, Technical Setup, Pre-Production, Production, Polish, Release
- [ ] Diagnosis writes nothing; optional report save requires exact covered authority
- [ ] Has a next-step handoff (e.g., `/gate-check` to formally advance stage)

---

## Director Gate Checks

None. `/project-stage-detect` is a read-only detection utility. No director
gates apply.

---

## Test Cases

### Case 1: stage.txt Exists — Reads directly and cross-checks artifacts

**Fixture:**
- `production/stage.txt` contains `Production`
- `design/cdd/` has 4 GDD files
- `src/` has source code files
- `production/sprints/sprint-002.md` exists

**Input:** `/project-stage-detect`

**Expected behavior:**
1. Skill reads `production/stage.txt` — detects stage `Production`
2. Skill cross-checks artifacts: GDDs present, source code present, sprint present
3. Artifacts are consistent with Production stage
4. Reports declared Production and observed artifacts; candidate/qualification
   evidence remains separate. HIGH diagnostic confidence needs actual body evidence.
5. Next step: continue with `/sprint-plan` or `/dev-story`

**Assertions:**
- [ ] Detected stage is Production
- [ ] stage.txt is declared evidence only; confidence needs actual body/evidence support
- [ ] Cross-check result (consistent vs. discrepant) is noted
- [ ] No files are written
- [ ] Verdict clearly states the detected stage

---

### Case 2: No stage.txt but GDDs and Epics Exist — Infers Production

**Fixture:**
- No `production/stage.txt`
- `design/cdd/` has 3 GDD files
- `production/epics/` has 2 epic files
- `src/` has source code files
- `production/sprints/sprint-001.md` exists

**Input:** `/project-stage-detect`

**Expected behavior:**
1. Skill finds no stage.txt — switches to artifact inference mode
2. Skill observes GDDs, epics, source and sprint bodies without claiming prior
   phases complete from their presence.
3. Skill suggests candidate Production from actual ongoing work, not counts.
4. Confidence is MEDIUM (inferred from artifacts, not from stage.txt)
5. Skill recommends running `/gate-check` to formalize and write stage.txt

**Assertions:**
- [ ] Candidate Production is advisory; qualified transition stays unverified
- [ ] Confidence is MEDIUM (not HIGH, since stage.txt is absent)
- [ ] Recommendation to run `/gate-check` is present
- [ ] No stage.txt is written by this skill

---

### Case 3: No stage.txt, No Docs, No Source — Infers Concept

**Fixture:**
- No `production/stage.txt`
- `design/` directory exists but is empty
- `src/` exists but contains no code files
- `technical-preferences.md` has placeholders only

**Input:** `/project-stage-detect`

**Expected behavior:**
1. Skill finds no stage.txt
2. Artifact scan: no GDDs, no source, no epics, no sprints, engine unconfigured
3. Skill infers: Stage = Concept
4. Confidence is MEDIUM
5. Skill suggests `/constitute` to begin the onboarding workflow

**Assertions:**
- [ ] Inferred stage is Concept
- [ ] Output lists the artifacts that were checked (and found absent)
- [ ] `/constitute` is suggested as the next step
- [ ] No files are written

---

### Case 4: Discrepancy — stage.txt says Production but no source code

**Fixture:**
- `production/stage.txt` contains `Production`
- `design/cdd/` has GDD files
- `src/` directory exists but contains no source code files
- No sprint files exist

**Input:** `/project-stage-detect`

**Expected behavior:**
1. Skill reads stage.txt — detects `Production`
2. Cross-check finds: no source code, no sprints — inconsistent with Production
3. Skill flags discrepancy: "stage.txt says Production but no source code or sprints found"
4. Skill reports detected stage as Production (honoring stage.txt) but
   confidence drops to LOW due to artifact mismatch
5. Skill suggests reviewing stage.txt manually or running `/gate-check`

**Assertions:**
- [ ] Discrepancy is flagged explicitly in the output
- [ ] Confidence is LOW when artifacts contradict stage.txt
- [ ] stage.txt value is not silently overridden
- [ ] User is advised to verify the discrepancy manually

---

### Case 5: Director Gate Check — No gate; detection is advisory

**Fixture:**
- Any project state with or without stage.txt

**Input:** `/project-stage-detect`

**Expected behavior:**
1. Skill completes full stage detection
2. No director agents are spawned at any point
3. No gate IDs appear in output
4. No write tool is called

**Assertions:**
- [ ] No director gate is invoked
- [ ] No write tool is called
- [ ] Detection output is purely advisory
- [ ] Verdict names the detected stage without triggering any gate

---

## Protocol Compliance

- [ ] Reads stage.txt if present; falls back to artifact inference if absent
- [ ] Always reports a confidence level (HIGH / MEDIUM / LOW)
- [ ] Cross-checks stage.txt against artifacts and flags discrepancies
- [ ] Does not write stage.txt (that is `/gate-check`'s responsibility)
- [ ] Ends with a next-step recommendation appropriate to the detected stage

---

## Coverage Notes

- The Technical Setup stage (engine configured, no GDDs yet) and Pre-Production
  stage (GDDs complete, no epics yet) follow the same artifact-inference pattern
  as Cases 2 and 3 and are not separately fixture-tested.
- Declared Polish/Verification/Release labels still require exact actual evidence
  for qualified transitions; file presence/inference cannot qualify them.
- Confidence levels are advisory — the skill does not gate any actions on them.

## Paired domain and authority cases

**Fixture A:** No concept, placeholder engine/stack, 100 source/test files.
B has configured Product API/CLI/data/auth/workflow contracts without game concept.
C has actual legacy Game engine/domain and gameplay evidence.
- [ ] A stays Unknown domain; counts describe scale and coverage stays unknown.
- [ ] B uses actual Product branch; C preserves actual Game compatibility/examples.
- [ ] Configured VERSION reference does not establish installed/executed runtime.
- [ ] Conflicting concepts remain conflict/Unknown, never first-filename wins.

**Fixture D:** stage declares Release while a required governing check is NotRun;
a named report-write approval exists, without transition/index/state authority.
- [ ] Preserve declaration, report actual evidence/candidate and unqualified state.
- [ ] Required NotRun remains incomplete; no false confidence/percentage/qualified PASS.
- [ ] Reuse report authority for its report only; no repeated request or stage write.
- [ ] Review-only invokes no write entrypoint. Actual report is not publication,
  acceptance, runtime activation or project completion.

### Declared-stage file omitted by discovery filters

Paired Game/Product fixtures contain an ignored `production/stage.txt` with
actual `Production`/`Implementation` content. Extension-filtered discovery lists
only Markdown/YAML/source files. Separate fixtures truly omit the stage file.
- [ ] Directly read and preserve the existing declared-stage body before
  candidate classification; never report "no explicit stage found" for it.
- [ ] A truly absent file needs a direct path-specific absence observation;
  unread/inaccessible remains unverified, and advisory inference stays separate.
- [ ] No stage/report/index writes under review-only; neither a declaration nor
  its absence establishes qualified transition or platform acceptance.
