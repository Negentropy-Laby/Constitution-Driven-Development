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

@.claude/docs/directory-structure.md

## Version Reference

After `/setup-engine`, use the version reference matching the configured project:

- Game: `docs/engine-reference/[engine]/VERSION.md`
- Product: `docs/reference/[stack]/VERSION.md`

## Technical Preferences

@.claude/docs/technical-preferences.md

## Coordination Rules

@.claude/docs/coordination-rules.md

## Collaboration Protocol

**User-driven collaboration, not autonomous execution.**
Every task follows: **Question -> Options -> Decision -> Draft -> Approval**

- Agents MUST ask "May I write this to [filepath]?" before using Write/Edit tools
- Agents MUST show drafts or summaries before requesting approval
- Multi-file changes require explicit approval for the full changeset
- No commits without user instruction

See `docs/COLLABORATIVE-DESIGN-PRINCIPLE.md` for full protocol and examples.

> **First session?** Run `/constitute` to establish governing principles.
> It works for both game and general product projects — just answer the
> domain question when asked.

## Coding Standards

@.claude/docs/coding-standards.md

## Context Management

@.claude/docs/context-management.md
