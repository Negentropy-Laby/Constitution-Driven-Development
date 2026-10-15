# Skill Test Spec: /scope-check

## Skill Summary

`/scope-check [feature-name or sprint-N or milestone-name]` assesses a named
feature, sprint or milestone against its exact original plan and actual delivery
needs, including unnecessary work already in the baseline. Analysis defaults to
read-only with no director gate. Optional report and index effects require their
separate named authority. Assigned Scope Verdicts are PASS, CONCERNS or FAIL.
Unresolved required baseline/applicability produces Assessment Status: Unknown
with no Scope Verdict. Case PASS/FAIL/PARTIAL evaluates this spec, not product
qualification. `model: haiku` is existing platform metadata; it does not switch a
Codex evaluator's model.

## Static Assertions (Structural and Semantic)

Use the eight checks owned by `skills/skill-test/SKILL.md`; keyword checks alone
cannot establish these semantic assertions or runtime behavior.

- [ ] Required frontmatter, multiple phases and a contextual next-step handoff exist.
- [ ] Argument hint, guide, phases and examples use named feature/sprint/milestone targets.
- [ ] The only assigned Scope Verdicts are PASS/CONCERNS/FAIL, independent of percentage thresholds.
- [ ] Unknown is an assessment state; no assigned verdict/index enum is invented.
- [ ] Default analysis is read-only; report-only excludes index/input/state writes.
- [ ] Game player experience and Product workflow/data integrity remain applicable.
- [ ] Original baseline necessity and all six comparison dimensions are assessed.

## Director Gate Checks

None. Producer consultation may be recommended for a specific finding; it is not
an automatically invoked gate in any review mode.

## Test Cases

Each case assumes readable governing inputs and no write authority unless it
explicitly supplies it. Owner references name the canonical skill's phases.
For future execution observe actual output and tool/callback calls; fixture
reasoning and spec presence do not establish those observations.

### Case 1: Named target controls and justified delivery

**Owner:** Phases 1–5.
**Fixture:** `production/sprints/sprint-006.md` binds an approved original five-task
baseline. Relevant current content is unchanged, every blocking task has an actual
delivery consumer, omission failure and governing basis, and no concern is unresolved.
Paired variants use `design/cdd/movement.md` and
`production/milestones/milestone-03.md` with the same complete justification.
**Input:** `/scope-check sprint-006`, `/scope-check movement`,
`/scope-check milestone-03`.
**Expected behavior:** Read the named original; bind its revision and input identity;
assess original/current necessity and present a justified PASS.
**Assertions:**
- [ ] Each target resolves its actual plan; no active target substitution occurs.
- [ ] Business scope, deliverables, dependencies, validation, cost and baseline changes appear with facts/actions.
- [ ] PASS concerns only assessed scope; report and all other writer calls are zero.

### Case 2 (A01): Zero growth can expose an excessive original plan

**Owner:** Phases 1, 3 and 4.
**Fixture:** Original and current plans both demand a global recovery toolkit before
one document edit (10 items unchanged, 0%). Existing direct editing/checking
satisfies delivery and every mandatory requirement. The toolkit has no necessary
delivery consumer or mandatory basis.
**Input:** `/scope-check movement`.
**Expected behavior:** Review baseline necessity, compare the smaller route and
report material unnecessary blocking work.
**Assertions:**
- [ ] The original toolkit is a named finding with evidence, consumer/failure/basis/alternative analysis.
- [ ] Scope Verdict is FAIL on the supplied evidence; 0% cannot cause PASS.
- [ ] A paired baseline with necessary justified blockers and no concern can PASS.

### Case 3 (A02): Justified 50% expansion

**Owner:** Phases 3–4.
**Fixture:** Ten original items become fifteen. All five additions have explicit
scope authority, real delivery consumers and necessary requirements; costs and
dependencies are justified and no material concern remains.
**Input:** `/scope-check sprint-006`.
**Assertions:**
- [ ] Output records +5 / +50% with its counting unit as descriptive evidence.
- [ ] Scope Verdict is PASS on these complete facts; +50% alone cannot cause FAIL.
- [ ] A paired unsupported expansion is FAIL, or a bounded evidenced concern is CONCERNS with owner/action.

### Case 4 (A03): Add/remove cancellation hides lost authority

**Owner:** Phases 1, 3 and 4.
**Fixture:** One required permission check is removed; one unrelated tool
qualification task is added. Net count remains zero; no waiver covers the removal.
**Input:** `/scope-check movement`.
**Assertions:**
- [ ] Additions and removals are separately named; removal's governing conflict is visible.
- [ ] Scope Verdict is FAIL despite 0% net growth; an extension of time cannot erase the conflict.
- [ ] Recommendations neither modify approved scope nor relabel the required gate PASS.

### Case 5 (A04): Missing target or mandatory baseline

**Owner:** Phase 1 and Phase 4.
**Fixture:** Variant A has no argument despite an active sprint. B targets movement
whose mandatory original is absent; C's selected alternate matching design file is
unreadable; D has an unresolved required applicability fact.
**Input:** A: `/scope-check`; B–D: `/scope-check movement`.
**Assertions:**
- [ ] A requests a named feature/sprint/milestone before target-dependent reads; no default comparison or verdict.
- [ ] B–D name the actual unresolved original/fact and affected decision, report Assessment Status: Unknown and assign no Scope Verdict.
- [ ] Selecting an alternate locator does not make the original optional; no invented replacement or passing comparison.
- [ ] Independent known defects may be observations without certifying the incomplete comparison.

### Case 6 (A05): Tool dependency cannot prove its own necessity

**Owner:** Phase 1 and six-dimensional Phase 3.
**Fixture:** A proposed tool is needed only because the plan chose that same tool
to validate a document. Existing direct validation satisfies the delivery assertion.
Paired control has a real consumer with a failure the smaller route cannot prevent.
**Input:** `/scope-check movement`.
**Assertions:**
- [ ] Circular necessity is exposed via actual consumer, omission failure, basis and alternative.
- [ ] Supplied material false cycle gives FAIL and targeted Cut/Defer/Resolve recommendation.
- [ ] The justified control can Keep/PASS without inventing a universal tool ban.

### Case 7 (A06): Real mandatory gate truth survives re-scoping

**Owner:** Phases 3–5 and Rules.
**Fixture:** Separate variants have required security/AC/DoD/review/execution checks
FAIL, NotRun, Blocked or Pending; a user accepts risk or proposes smaller work.
A control marks an actually inapplicable check with a governing applicability reason.
**Input:** `/scope-check sprint-006`.
**Assertions:**
- [ ] Each required check retains its actual status; no scope recommendation turns it PASS/Complete/N/A.
- [ ] The inapplicable control may use justified NotApplicable; unmeasured cost stays Unknown.
- [ ] Zero/meaningless count denominator reports NotApplicable with reason, not invented percentage/cost.

### Case 8 (A07): Actual content controls evidence impact

**Owner:** Phases 1–2; `standards/coordination-rules.md`.
**Fixture:** Variant A moves main through an unrelated commit while relevant bytes,
dependencies and authority remain the same. B changes an actual relied-on behavior
or required input. Evidence records bind exact original inputs.
**Input:** `/scope-check movement`.
**Assertions:**
- [ ] A compares actual content/context and labels any permitted evidence reuse historical; no SHA-only invalidation.
- [ ] B assesses affected dependants and verification needs; unrelated observations remain usable.
- [ ] Matching patches/hashes or count alone cannot transfer tests, reviews or approval.

### Case 9 (A12): Report-only and review-only boundaries

**Owner:** Default behavior and Phase 5b; evidence lifecycle.
**Fixture:** A permits a new named report only with Memory Bank initialized.
B is review-only and offers an in-memory writer receiver.
C separately covers report and existing index effects, with an assessed verdict;
D has the same index authority but Unknown assessment.
**Input:** `/scope-check movement` under each scope.
**Assertions:**
- [ ] A writes only the report; input/index/state/snapshot writer calls are zero.
- [ ] B invokes no write entrypoint, including the in-memory writer; disk diff alone is insufficient proof.
- [ ] C reads the saved report revision and exact identities before its separately covered index effect.
- [ ] D keeps Unknown/no-verdict in report/conversation without an index row or new enum.
- [ ] Existing matching named authority is reused; only missing/materially new effects ask after the draft.

### Case 10 (A14): Optional absence and actual conflicting policy

**Owner:** Phases 1, 4 and 5b.
**Fixture:** A has no optional Memory Bank/QA Context but a complete readable
baseline and requirements. B has conflicting required scope/applicability.
**Input:** `/scope-check milestone-03`.
**Assertions:**
- [ ] A uses conversation/authorized report fallback without initialization or invented Unknown baseline.
- [ ] B retains Unknown only for the affected comparison/decision and no Scope Verdict.
- [ ] Neither optional absence nor report saving creates passing QA, review or closure facts.

## Protocol Compliance

- [ ] Read the actual named original before comparison; retain exact input identities and original bytes.
- [ ] Evaluate baseline necessity as well as original/current additions and removals.
- [ ] No director gate; follow-up is advisory and specific to findings.
- [ ] Assigned verdict vocabulary and Unknown/no-verdict behavior match every case.
- [ ] Reuse exact named authority; report/index/state and qualification remain separate.
- [ ] Re-run after authorized changes without assuming verdict improvement.
- [ ] Preserve Game and Product priorities; native model selection follows actual host configuration.

## Coverage Notes

Cases A01–A07, A12 and A14 and their controls cover written instructions, output
claims and future side-effect observations. A complete static/spec reasoning
report states each actual result and any ambiguity. Actual model behavior,
in-memory callback observations and native host loading require separately
recorded execution; they remain NotRun when not performed. These cases introduce
no single-Story interface or automatic target selection.
