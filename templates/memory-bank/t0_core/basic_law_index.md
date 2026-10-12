# Basic Law Index

## CDD Source and Target Project Boundaries

These rules distinguish the CDD Source library from a business project using its
installed platform files; Source-only restrictions do not govern the business
project's own code, documents or delivery evidence.

“严格分离”“不混入”“仅保留”约束的是 Git 跟踪、暂存、提交及发布的文件内容集合，与本地存放目录无关。
In these CDD boundaries, "strict separation", "must not mix" and "only retain"
constrain the content selected for Git tracking, staging, commits and publication,
not directory layout or local disk presence. Maintenance material may remain
locally inside or outside either repository. Its presence alone is not a violation
and must not trigger moving, deleting or relocating logs.

Before submission or publication, review the actual changed content, Git index
and intended delivery set. Use precise shared `.gitignore` rules against accidental
addition of untracked maintenance files; they do not remove tracked/staged content
or prevent forced addition or separate publication. Already-tracked maintenance
content needs separately authorized exclusion from tracking/delivery while keeping
recoverable originals. This rule alone grants no such action.

### CDD source library

The Source library submits development templates and necessary template-use
instructions/support. Exclude template-maintenance tools, checkers, maintenance
fixtures, maintenance-only annotations (including hidden comments), actual
maintenance reports/logs and other maintenance-process records from that set.
Substantive template-use rules and reusable report/test templates remain eligible;
they are distinct from maintenance notes and actual execution records. Ordinary
template use must not depend on the local maintenance toolkit.

### Target business project

A target project submits its business code and substantive project documents.
The CDD portion of its Git submission/publication set contains only required
installed platform adaptations and portable project-specific configuration.
Reusable CDD development templates, generic standards/workflow originals and
`skill_testing/` catalog/spec/rubric/template assets stay local-only in a target.
A required local read or input allowlist does not grant Git tracking, staging,
commit or publication eligibility. Keep actual required originals locally; missing
or unread originals leave the affected workflow pending. A fresh target clone may
need these inputs installed separately before the affected CDD workflow can run.
Review Target Git candidates separately from the local required-input allowlist.
Do not submit a general CDD source mirror, template-maintenance tools/annotations, tool-only
metadata, maintenance locks/caches or actual template-maintenance process output.
The designated CDD Source owns general agent/skill definitions; that ownership
is independent of the location of any local copy. Local copies alone do not
establish Source authority or justify an automatic move or deletion.

**Existing tracked neutral inputs.** When a boundary change affects reusable
neutral template/standard/workflow/spec originals already tracked under earlier
guidance, record reconciliation as pending until the applicable governance gate
closes. Earlier tracking is neither automatically grandfathered as compliant nor
judged a violation under an unaccepted rule. Keep local originals and Git history.
After acceptance or a valid scoped exception under existing governance, obtain
separate exact-path project migration authority before removing reviewed reusable
originals from Git tracking. Retain their local files, required-reference closure,
project customizations and recoverable before bytes; review the actual index/diff
and separately eligible Git candidates. Commit/publication still require their
own authority. This differs from already-tracked maintenance content and grants
no untracking, deletion, relocation or migration authority by itself.

Business build/runtime files, tests, control manifests, design/production documents
and genuine business QA, acceptance and historical evidence remain governed by
the project's own rules. Classify by purpose and delivery role, not words such as
"maintenance", a hash or selector. Ordinary installed-platform use must work
without a local CDD maintenance reader, tool or lock. Updates still require the
actual Source identity, covered write authority, independent review of the exact
delivery and preservation of project customizations and recoverable before bytes.

These boundaries grant no moving, deletion, untracking, history-rewrite, log-path,
commit, push or publication authority. Existing collaboration, approval and
safety rules remain controlling. They do not ratify project laws, accept ADRs,
initialize governance, advance stages or establish execution/qualification evidence.

## Core Thesis

Support ID: BL-01

- The project's core thesis is: [one-sentence thesis]
- Current truth for that thesis lives in the T0 current-state law surface and is
  supported by the T1 context files.

## Foundational Current-State Laws

### Law 1

Support ID: BL-02
Status: [Proposed / Accepted / Accepted (amended YYYY-MM-DD) / Superseded by BL-XX (YYYY-MM-DD) / Deprecated (YYYY-MM-DD)]

- **Law:** [The principle statement]
- **Current-state requirement:** [What must be true right now for this to hold]
- **Design test:** [A concrete decision scenario this law resolves]
- **Supported by T1:** `../t1_axioms/system_patterns.md#`,
  `../t1_axioms/behavior_context.md#`, `../t1_axioms/tech_context.md#`
- **Validated or executed through T2:** `../t2_execution/`

### Law 2

Support ID: BL-03
Status: [Proposed / Accepted / Accepted (amended YYYY-MM-DD) / Superseded by BL-XX (YYYY-MM-DD) / Deprecated (YYYY-MM-DD)]

- **Law:** [The principle statement]
- **Current-state requirement:** [What must be true right now]
- **Design test:** [Concrete decision scenario]
- **Supported by T1:** `../t1_axioms/system_patterns.md#`,
  `../t1_axioms/behavior_context.md#`, `../t1_axioms/tech_context.md#`
- **Validated or executed through T2:** `../t2_execution/`

### Law 3

Support ID: BL-04
Status: [Proposed / Accepted / Accepted (amended YYYY-MM-DD) / Superseded by BL-XX (YYYY-MM-DD) / Deprecated (YYYY-MM-DD)]

- **Law:** [The principle statement]
- **Current-state requirement:** [What must be true right now]
- **Design test:** [Concrete decision scenario]
- **Supported by T1:** `../t1_axioms/system_patterns.md#`,
  `../t1_axioms/behavior_context.md#`, `../t1_axioms/tech_context.md#`
- **Validated or executed through T2:** `../t2_execution/`

## Acceptance and Evidence References

For accepted laws/amendments link exact source revision/baseline, acceptance
authority/scope, T1/T2 support, retained evidence and remaining owner/due phase.
Draft/content/write approval does not accept laws. Use full hashes/recoverable
bytes under `standards/evidence-lifecycle.md`. Preserve legacy IDs/sections;
unknown evidence stays unknown. Do not import another project's laws/dates.
