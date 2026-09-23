# Godot Language Configuration

> Loaded on demand from `setup-engine/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## Appendix A — Godot Language Configuration

[游戏专用] GDScript/C#/Both variants — INSTRUCTIONS.md templates, naming conventions, and specialist routing tables. Referenced only when Godot is the chosen engine.

### A1. INSTRUCTIONS.md Technology Stack Templates

**GDScript:**
```markdown
- **Engine**: Godot [version]
- **Language**: GDScript
- **Build System**: SCons (engine), Godot Export Templates
- **Asset Pipeline**: Godot Import System + custom resource pipeline
```

> **Guardrail**: When using this GDScript template, write the Language field as exactly "`GDScript`" — no additions. Do NOT append "C++ via GDExtension" or any other language. The C# template below includes GDExtension because C# projects commonly wrap native code; GDScript projects do not.

**C#:**
```markdown
- **Engine**: Godot [version]
- **Language**: C# (.NET 8+, primary), C++ via GDExtension (native plugins only)
- **Build System**: .NET SDK + Godot Export Templates
- **Asset Pipeline**: Godot Import System + custom resource pipeline
```

**Both — GDScript + C#:**
```markdown
- **Engine**: Godot [version]
- **Language**: GDScript (gameplay/UI scripting), C# (performance-critical systems), C++ via GDExtension (native only)
- **Build System**: .NET SDK + Godot Export Templates
- **Asset Pipeline**: Godot Import System + custom resource pipeline
```

### A2. Naming Conventions

**GDScript:** Classes: PascalCase, Variables/functions: snake_case, Signals: snake_case past tense, Files: snake_case, Scenes: PascalCase, Constants: UPPER_SNAKE_CASE

**C#:** Classes: PascalCase (partial), Public: PascalCase, Private: _camelCase, Methods: PascalCase, Files: PascalCase, Constants: PascalCase

**Both:** Use GDScript conventions for `.gd` files, C# conventions for `.cs` files.

### A3. Engine Specialists Routing

**GDScript:**
```markdown
## Engine Specialists
- **Primary**: godot-specialist
- **Language/Code Specialist**: godot-gdscript-specialist (all .gd files)
- **Shader Specialist**: godot-shader-specialist (.gdshader files, VisualShader resources)
- **UI Specialist**: godot-specialist (no dedicated UI specialist — primary covers all UI)
- **Additional Specialists**: godot-gdextension-specialist (GDExtension / native C++ bindings only)
- **Routing Notes**: Invoke primary for architecture decisions, ADR validation, and cross-cutting code review. Invoke GDScript specialist for code quality, signal architecture, static typing enforcement, and GDScript idioms. Invoke shader specialist for material design and shader code. Invoke GDExtension specialist only when native extensions are involved.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.gd files) | godot-gdscript-specialist |
| Shader / material (.gdshader, VisualShader) | godot-shader-specialist |
| UI / screen (Control nodes, CanvasLayer) | godot-specialist |
| Scene / prefab / level (.tscn, .tres) | godot-specialist |
| Native extension (.gdextension, C++) | godot-gdextension-specialist |
| General architecture review | godot-specialist |
```

**C#:**
```markdown
## Engine Specialists
- **Primary**: godot-specialist
- **Language/Code Specialist**: godot-csharp-specialist (all .cs files)
- **Shader Specialist**: godot-shader-specialist (.gdshader files, VisualShader resources)
- **UI Specialist**: godot-specialist (no dedicated UI specialist — primary covers all UI)
- **Additional Specialists**: godot-gdextension-specialist (GDExtension / native C++ bindings only)
- **Routing Notes**: Invoke primary for architecture decisions, ADR validation, and cross-cutting code review. Invoke C# specialist for code quality, [Signal] delegate patterns, [Export] attributes, .csproj management, and C#-specific Godot idioms. Invoke shader specialist for material design and shader code. Invoke GDExtension specialist only when native C++ plugins are involved.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.cs files) | godot-csharp-specialist |
| Shader / material (.gdshader, VisualShader) | godot-shader-specialist |
| UI / screen (Control nodes, CanvasLayer) | godot-specialist |
| Scene / prefab / level (.tscn, .tres) | godot-specialist |
| Project config (.csproj, NuGet) | godot-csharp-specialist |
| Native extension (.gdextension, C++) | godot-gdextension-specialist |
| General architecture review | godot-specialist |
```

**Both — GDScript + C#:**
```markdown
## Engine Specialists
- **Primary**: godot-specialist
- **GDScript Specialist**: godot-gdscript-specialist (.gd files — gameplay/UI scripts)
- **C# Specialist**: godot-csharp-specialist (.cs files — performance-critical systems)
- **Shader Specialist**: godot-shader-specialist (.gdshader files, VisualShader resources)
- **UI Specialist**: godot-specialist (no dedicated UI specialist — primary covers all UI)
- **Additional Specialists**: godot-gdextension-specialist (GDExtension / native C++ bindings only)
- **Routing Notes**: Invoke primary for cross-language architecture decisions and which systems belong in which language. Invoke GDScript specialist for .gd files. Invoke C# specialist for .cs files and .csproj management. Prefer signals over direct cross-language method calls at the boundary.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.gd files) | godot-gdscript-specialist |
| Game code (.cs files) | godot-csharp-specialist |
| Cross-language boundary decisions | godot-specialist |
| Shader / material (.gdshader, VisualShader) | godot-shader-specialist |
| UI / screen (Control nodes, CanvasLayer) | godot-specialist |
| Scene / prefab / level (.tscn, .tres) | godot-specialist |
| Project config (.csproj, NuGet) | godot-csharp-specialist |
| Native extension (.gdextension, C++) | godot-gdextension-specialist |
| General architecture review | godot-specialist |
```
