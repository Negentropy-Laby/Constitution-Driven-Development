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
