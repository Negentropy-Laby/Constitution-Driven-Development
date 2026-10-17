# Adoption Summary and Plan Formats

## Phase 5: Summary

```
## Adoption Audit Summary
Phase detected: [phase]
Domain / engine or stack: [evidence-backed; configured / NOT CONFIGURED]
CDDs audited: [N] ([X] format-compliant, [Y] with gaps, [Z] unverified)
ADRs audited: [N] ([X] format-compliant, [Y] with gaps, [Z] unverified)
Stories audited: [N] ([X] format-compliant, [Y] with gaps, [Z] unverified)
Unaudited artifact types: [actual subset / none]
Unverified required inputs: [paths and affected scope / none]

Gap counts:
  BLOCKING: [N] — template skills will malfunction without these fixes
  HIGH:     [N] — unsafe to run /create-stories or /story-readiness
  MEDIUM:   [N] — quality degradation
  LOW:      [N] — optional improvements

Estimated remediation: [X blocking items × ~Y min each = roughly Z hours]
```

## Phase 6: Plan

```markdown
# Adoption Plan

> **Generated**: [date]
> **Project phase**: [phase]
> **Domain / Engine or Stack**: [actual source + configured reference; installed state unverified]
> **Template version**: v0.2.0

Work through these steps in order. Check off each item as you complete it.
Re-run `/adopt` anytime to check remaining gaps.

---

## Audit Summary

[Actual per-artifact format tallies, severity counts and unverified input paths]

## Resolved Consumer Layout [only for selected import/update/layout migration]

[Apply standards/directory-structure.md, Consumer layout resolution for imports
and updates. Record the actual Source identity, verified latest applicable
revision and exact input identities; project role, runtime/workflow scope,
governing consumer contracts and unresolved choices. Show the complete resolved
target tree. A partial or unresolved tree is labeled pending, never the final
installed result. Omit this section for a standalone artifact-format audit.]

## Path and Ownership Mapping [same selected scope only]

| Source/input identity and owner | Old path | Target path | Action and reason | Active readers/references and generation/configuration effects | Local-input / Git-candidate disposition | Write authority, before bytes and recovery | Verification / unresolved owner |
|---|---|---|---|---|---|---|---|
| [actual input and provenance] | [actual old path or absent] | [resolved path or pending] | [import / generate / retain / migrate / archive / exclude / unresolved; reason] | [actual affected dependencies and deterministic outputs] | [separate decisions, not inferred from required reads] | [covered effects and recoverable original-byte witness] | [required check, actual result or pending decision] |

[Preserve content and valid changes through the mapping. History-only path
identifiers stay distinguished from current dependencies. Retire old paths only
after migrated live readers, passed applicable checks and verified recovery within
authority. Plan-only approval does not execute the mapping. Omit this section
when no import/update/layout migration was selected.]

## Recommended Next Action

[One concrete primary command/input action, reason, scope and limits]

## Step [N]: [Nonempty action group, in Phase 4 order]

[Actual gap, owning path, fix command/manual steps, estimate and checkbox]
[Repeat only for actual actions; omit this section entirely if none]

---

## What to Expect from Existing Stories

Preserve existing bodies and historical status. Missing legacy TR/manifest fields
need current owning-workflow recheck, not automatic PASS or regeneration. Format
audits cannot certify qualified Story/project state.

---

## Re-run

Run `/adopt` again after completing applicable actions to recheck selected format
scope. A zero-gap audit needs no invented repair step; its broader health check
remains a separate invocation.
```
