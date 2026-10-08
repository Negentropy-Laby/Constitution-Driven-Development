# Skill Test Spec: /propagate-design-change

## Skill Summary

`/propagate-design-change` handles GDD revision cascades. When a GDD is updated,
the skill traces all downstream artifacts that reference it: ADRs, TR-registry
entries, stories, and epics. It produces a structured impact report showing what
needs to change and why. The skill does NOT automatically apply changes — it
proposes a concrete path/effect list and reuses the approved changeset scope;
uncovered effects require "May I write" before modification.

Analysis is read-only; updates require their named scope. The TD-CHANGE-IMPACT
gate runs after impact analysis in full mode and is skipped in lean/solo. Gate
approval is neither file authority nor ADR acceptance.

---

## Static Assertions (Structural)

Verified automatically by `/skill-test static` — no fixture needed.

- [ ] Has required frontmatter fields: `name`, `description`, `argument-hint`, `user-invocable`, `allowed-tools`
- [ ] Has ≥2 phase headings
- [ ] Contains verdict keywords: COMPLETE, BLOCKED, NO IMPACT
- [ ] Documents scoped write authority or its shared-contract owner; behavioral compliance is evaluated in fixture cases
- [ ] Has a next-step handoff at the end
- [ ] Documents that changes are proposed, not applied automatically

---

## Director Gate Checks

Resolve `--review`, `production/review-mode.txt` or lean once. Full runs actual
TD-CHANGE-IMPACT after analysis; lean/solo record it skipped. Missing required
delegation remains incomplete; no fabricated gate verdict.

---

## Test Cases

### Case 1: Happy Path — GDD revision affects 2 stories and 1 epic

**Fixture:**
- `design/cdd/[system].md` exists and has been recently revised (git diff shows changes)
- `production/epics/[layer]/EPIC-[system].md` references this GDD
- 2 story files reference TR-IDs from this GDD
- The changed GDD section affects the acceptance criteria of both stories

**Input:** `/propagate-design-change design/cdd/[system].md`

**Expected behavior:**
1. Skill reads the revised GDD and identifies what changed (git diff or content comparison)
2. Skill scans ADRs, TR-registry, epics, and stories for references to this GDD
3. Skill produces an impact report: 1 epic affected, 2 stories affected
4. Skill shows the proposed change for each artifact
5. Presents a concrete draft/path/effect list; reuses complete existing batch
   authority, otherwise asks "May I update this named changeset?"
6. Applies only authorized artifact effects; preserves original revisions

**Assertions:**
- [ ] Impact report identifies all 3 affected artifacts (1 epic + 2 stories)
- [ ] Each affected artifact's proposed change is shown before asking to write
- [ ] Complete approved changesets persist across covered artifact writes
- [ ] Skill does NOT apply uncovered artifact/status effects
- [ ] Report execution COMPLETE is separate from actual required actions/acceptance

---

### Case 2: No Impact — Changed GDD has no downstream references

**Fixture:**
- `design/cdd/[system].md` exists and has been revised
- No ADRs, stories, or epics reference this GDD's TR-IDs or GDD path

**Input:** `/propagate-design-change design/cdd/[system].md`

**Expected behavior:**
1. Skill reads the revised GDD
2. Skill scans all ADRs, stories, and epics for references
3. No references found
4. Skill outputs: "No downstream impact found for [system].md — no artifacts reference this GDD."
5. No write operations are performed

**Assertions:**
- [ ] Skill outputs the "No downstream impact found" message
- [ ] Verdict is NO IMPACT
- [ ] No "May I write" asks are issued (nothing to update)
- [ ] Skill does NOT error or crash when no references are found

---

### Case 3: In-Progress Story Warning — Referenced story is currently being developed

**Fixture:**
- A story referencing this GDD has `Status: In Progress`
- The developer has already started implementing this story

**Input:** `/propagate-design-change design/cdd/[system].md`

**Expected behavior:**
1. Skill identifies the In Progress story as an affected artifact
2. Skill outputs an elevated warning: "CAUTION: [story-file] is currently In Progress — a developer may be working on this. Coordinate before updating."
3. The warning appears in the impact report before the "May I write" ask for that story
4. User can still approve or skip the update for that story

**Assertions:**
- [ ] In Progress story is flagged with an elevated warning (distinct from regular affected-artifact entries)
- [ ] Warning appears before the "May I write" ask for that story
- [ ] Skill still offers to update the story — the warning does not block the option
- [ ] Other (non-In-Progress) artifacts are not affected by this warning

---

### Case 4: Edge Case — No argument provided

**Fixture:**
- Multiple GDDs exist in `design/cdd/`

**Input:** `/propagate-design-change` (no argument)

**Expected behavior:**
1. Skill detects no argument is provided
2. Skill outputs a usage error: "No GDD specified. Usage: /propagate-design-change design/cdd/[system].md"
3. Skill lists recently modified GDDs as suggestions (git log)
4. No analysis is performed

**Assertions:**
- [ ] Skill outputs a usage error when no argument is given
- [ ] Usage example is shown with the correct path format
- [ ] No impact analysis is performed without a target GDD
- [ ] Skill does NOT silently pick a GDD without user input

---

### Case 5: Director Gate — Mode controls technical impact review

Verify actual gate owner: `skills/propagate-design-change/SKILL.md` Phase 6b owns
TD-CHANGE-IMPACT criteria and APPROVE/CONCERNS/REJECT outcomes. Shared
`standards/director-gates.md` governs mode/authority but defines no TD-CHANGE-IMPACT.
A reviewer must not invent a shared catalog definition or use a different verdict
interface; CONCERNS and REJECT follow the actual inline handling.

**Fixture:** A Game CDD revision has downstream references; `production/review-mode.txt`
is full and an actual technical-director reviewer is available.

**Input:** `/propagate-design-change design/cdd/[system].md`

**Expected behavior:** Resolve full once, perform complete impact tracing, then
run TD-CHANGE-IMPACT on the exact report inputs. Surface objections and revise
affected analysis; a gate pass does not mark any Proposed ADR Accepted or authorize
status/index changes. Repeat in lean/solo and observe the documented skip.

**Assertions:**
- [ ] Full runs TD-CHANGE-IMPACT; lean/solo report skipped accurately
- [ ] Gate inputs/actual actor recorded; unavailable review is incomplete
- [ ] No pending successor is written into a Superseded status
- [ ] Read-only/report-only runs do not repair ADRs, Stories or indexes

---

## Protocol Compliance

- [ ] Reads revised GDD and all potentially affected artifacts before producing impact report
- [ ] Impact report shown in full before any "May I write" ask
- [ ] Existing concrete batch authorization reused; new effects presented for approval
- [ ] In Progress stories flagged with elevated warning before their approval ask
- [ ] TD-CHANGE-IMPACT obeys one resolved full/lean/solo director mode
- [ ] Ends with next-step handoff appropriate to verdict (COMPLETE or NO IMPACT)

---

## Coverage Notes

- ADR impact (when a GDD change requires an ADR update or new ADR) follows the
  same concrete path/effect scope as Story/Epic updates and the shared
  Notes/ADR disposition; acceptance/retained-history counterexamples appear below.
- TR-registry impact (when changed GDD requires new or updated TR-IDs) is part
  of the analysis phase but not independently fixture-tested.
- Fixtures bind fixed old/new source identities including uncommitted/ignored
  dependencies; report mtime or current HEAD alone is not an exact prior baseline.

---

### Semantic case: New/ignored inputs and preserved acceptance history

A new CDD has no Git history but is referenced by an In Progress Story and Epic;
an ignored contract attachment also changes. Expect declared closure and elevated
Story warning, not "nothing to propagate." An older Accepted ADR's public/durable
choice conflicts: record `conflict`/`adr-required` and preserve its accepted bytes.
Drafting a Proposed successor cannot mark it Superseded by pending ID. Batch
authority covers only listed artifacts; report-only writes its new assigned
report and no ADR/TR/Story/Epic/index. Missing old bytes narrows the delta claim.


**Observation requirements:** Fixtures are constructed only in isolated test
workspaces. Record real actions/reads, actor and exact before/after input/report
identities. Compare excluded input/index/session paths for unchanged bytes.
Static assertions or expected source counts alone cannot qualify semantic verdict,
reading depth, runtime execution, independent review or write authority.


### Invalid mode/depth input

Supply an invalid explicit mode/depth (or invalid global director mode where
used). Expect a named corrective error and no silent fallback, reviewer spawn
or write. Absent settings retain the documented default. Analysis depth,
director mode and write authority remain distinct.
