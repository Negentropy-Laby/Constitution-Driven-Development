# Basic Law Index

## CDD Source and Target Project Boundaries

These rules apply to two distinct owners: the CDD development-template source
library and a business project using its installed platform files. Source-library
submission restrictions do not become restrictions on the business project's
own code, project documents or delivery evidence.

### CDD source library

Only development templates and necessary template-use instructions belong in
the CDD source library's submission. Development templates must remain strictly
separate from maintenance tools, maintenance annotations and process data used
only to maintain the template library. Keep those materials in separate local
files with precise shared ignore rules; never embed them in development templates
or replace them with hidden comments. Template use must not require that local
maintenance toolkit.

### Target business project

Keep business code and project documents separate from the general CDD template
sources and template-maintenance tools. Deliver approved CDD platform-adapter
files, portable project-specific configuration, and the neutral templates,
standards, workflow views and reusable skill-testing assets required by the
selected workflows. Resolve actual required references into a reviewed per-file
allowlist; missing required originals remain pending. General CDD source trees,
including root `agents/` and `skills/`, remain in the designated external source
library and are not copied into the target as another source.

Keep template-maintenance scripts, checkers, annotations, tool-only metadata,
host-path records, maintenance locks, caches and maintenance-process artifacts
outside the target's delivery. Ordinary use of installed platform files must
work without them. The target retains its business build/runtime files, business
tests, project design and production documents, control manifests and genuine
QA, acceptance and historical project evidence under its own project rules.

These boundaries grant no write, deletion, commit or push authority and do not
ratify project laws, accept ADRs or establish execution or qualification evidence.

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
