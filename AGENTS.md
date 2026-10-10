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

This section applies only to the actual `Constitution-Driven-Development` Source
repository as the shared development-template library. Importing these instructions
into a consuming Game or Product project does not make it a template-source
repository or apply this Source-only submission restriction.

本项目提交的内容仅限开发模板。

开发模板与维护工具必须严格分离，哪怕是维护用注释也不得写入开发模板文件。

Necessary instructions explaining template use may accompany the development
templates. Maintenance tools, checkers, test fixtures and maintenance-process
artifacts must remain in separate local files and must not be submitted. Do not
write unrelated comments, maintenance metadata or maintenance-process records into
development-template files, or substitute other hidden comments for them. Use
precise exclusions in the shared repository `.gitignore`, not `.git/info/exclude`;
do not use blanket exclusions for business, template or platform trees. For affected
already-tracked maintenance files, remove only the explicitly approved Git tracking
entries while preserving complete local working copies; ignore rules alone do not
remove tracked entries. Shared template usage must not depend on these local-only
maintenance files. This restriction is limited to the actual Source repository;
consumer projects retain their own submission rules and existing approval and safety
requirements. It grants no commit or deletion authority.

## CDD Target Project Separation

A CDD target project retains its business code, project design and production
documents, business control manifests and genuine QA evidence, preserving historical
records. Platform-adapter files and portable project-specific configuration needed
for normal use may be delivered under the project's rules. General CDD agent and
skill sources remain in the designated external Source repository; do not keep root
source copies as a second general CDD source. Normal use of templates and installed
platform adapters must not depend on a local CDD maintenance toolkit.

Tools, checkers, maintenance test fixtures, annotations, metadata, host-path records,
maintenance locks, caches and process materials used only for local CDD template
maintenance must remain in separate local files, with precise shared `.gitignore`
exclusions, and must not be submitted with the target project. Do not embed this
maintenance material in development-template files or replace it with hidden
comments. This boundary does not classify business build or runtime files, business
tests, business control manifests or genuine project QA records as local-only CDD
maintenance. For an import or update, verify the actual external Source and
independently review the exact delivery allowlist, preserving project customizations
and recoverable before bytes. Existing collaboration, approval, safety and commit
requirements remain controlling; this section grants no new execution authority or
permission to remove files.
