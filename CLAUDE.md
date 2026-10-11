# Constitution Driven Development

A coordinated AI agent architecture for software projects — game development,
web applications, CLI tools, libraries, and more. 53 specialized agents organized
into a studio hierarchy, each owning a specific domain.

## Technology Stack

**[游戏专用]** Game projects:
- **Engine**: [CHOOSE: Godot 4 / Unity / Unreal Engine 5]
- **Language**: [CHOOSE: GDScript / C# / C++ / Blueprint]

**[通用产品]** General product projects:
- **Language**: [CHOOSE: Python / TypeScript / Rust / Go / ...]
- **Framework**: [CHOOSE: FastAPI / React / Django / ...]

**All projects:**
- **Version Control**: Git with trunk-based development
- **Build System**: [SPECIFY after choosing stack]
- **Asset Pipeline**: [SPECIFY after choosing stack]

> **Note**: Engine-specialist agents exist for Godot, Unity, and Unreal for game
> projects. Language-specialist agents exist for Python, TypeScript, Rust, and Go
> for general product projects. Use the set matching your project.

## Project Structure

@standards/directory-structure.md

## Version Reference

After `/setup-engine`, use the version reference matching the configured project:

- Game: `docs/engine-reference/[engine]/VERSION.md`
- Product: `docs/reference/[stack]/VERSION.md`

## Technical Preferences

@standards/technical-preferences.md

## Coordination Rules

@standards/coordination-rules.md

## Collaboration Protocol

**User-driven collaboration with scoped, continuing authorization.**
For unresolved decisions use: **Question -> Options -> Decision -> Draft -> Approval**.
Read existing decisions and authorization first; continue within that scope
without asking again for every role, file, section, retry or context recovery.

- Show a draft or path-and-effect summary before new write authority:
  "May I write this to [filepath]?" A named multi-file changeset may be approved
  together. Ask again only for material new scope or authority.
- Separate content agreement, file-write authority, independent review, ADR
  acceptance, evidence publication and stage/story completion. None implies
  the others. Report-only authority covers a new report, not inputs/indexes/state.
- Review-only never invokes a write entrypoint, even in memory. Authorized
  write counterexamples run on isolated copies.
- Delegated roles inherit original scope and limits; delegation does not expand
  them. No commits without user instruction.

Shared contracts: `standards/evidence-lifecycle.md` and `standards/notes-adr-sync.md`.
They apply to Game and Product and do not install enforcement or activate Memory Bank.

See `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md` for full protocol and examples.

> **First session?** Run `/constitute` to establish governing principles.
> It works for both game and general product projects — just answer the
> domain question when asked.

## Coding Standards

@standards/coding-standards.md

## Path Policy Rules

Canonical path-scoped coding policies live in `rules/*.md`. Each file's
frontmatter `paths:` lists the globs it governs. Before editing files in a path,
consult the matching rule file(s). (Claude Code auto-loads these per path; Codex
has no path-glob equivalent, so consult them manually there.)

## Context Management

@standards/context-management.md

## Source Repository Submission Scope

This section applies only to the actual CDD Source library. Importing these
instructions does not apply Source-only submission restrictions to a business
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

The Source library submits development templates and necessary template-use
instructions/support. Exclude template-maintenance tools, checkers, maintenance
fixtures, maintenance-only annotations (including hidden comments), actual
maintenance reports/logs and other maintenance-process records from that set.
Substantive template-use rules and reusable report/test templates remain eligible;
they are distinct from maintenance notes and actual execution records. Ordinary
template use must not depend on the local maintenance toolkit.

These boundaries grant no moving, deletion, untracking, history-rewrite, log-path,
commit, push or publication authority. Existing collaboration, approval and
safety rules remain controlling. They do not ratify project laws, accept ADRs,
initialize governance, advance stages or establish execution/qualification evidence.

## CDD Target Project Separation

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

A target project submits its business code and project documents, required CDD
platform adaptations, portable project-specific configuration and the neutral
templates, standards, workflow views and reusable `skill_testing/` assets required
by enabled workflows and their actual reference closure. Review an exact per-file
delivery allowlist; missing required originals remain pending. Do not submit a
general CDD source mirror, template-maintenance tools/annotations, tool-only
metadata, maintenance locks/caches or actual template-maintenance process output.
The designated CDD Source owns general agent/skill definitions; that ownership
is independent of the location of any local copy. Local copies alone do not
establish Source authority or justify an automatic move or deletion.

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
