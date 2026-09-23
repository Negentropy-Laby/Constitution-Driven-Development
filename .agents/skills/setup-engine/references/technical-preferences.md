# Technology Preference Templates and Agent Routing

> Loaded on demand from `setup-engine/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

## 5. Populate Technical Preferences

After updating INSTRUCTIONS.md, create or update `standards/technical-preferences.md`.
Read the existing template first, then fill in.

### [通用场景] Language & Framework Section
Fill from the stack choice made in Section 2.

### [通用场景] Naming Conventions

**[游戏专用]** Engine defaults:

**Godot GDScript:**
- Classes: PascalCase (e.g., `PlayerController`)
- Variables/functions: snake_case (e.g., `move_speed`)
- Signals: snake_case past tense (e.g., `health_changed`)
- Files: snake_case matching class (e.g., `player_controller.gd`)
- Scenes: PascalCase matching root node (e.g., `PlayerController.tscn`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_HEALTH`)

**Godot C#:**
- Classes: PascalCase (`PlayerController`) — must also be `partial`
- Public properties/fields: PascalCase (`MoveSpeed`, `JumpVelocity`)
- Private fields: `_camelCase` (`_currentHealth`, `_isGrounded`)
- Methods: PascalCase (`TakeDamage()`, `GetCurrentHealth()`)
- Signal delegates: PascalCase + `EventHandler` suffix (`HealthChangedEventHandler`)
- Files: PascalCase matching class (`PlayerController.cs`)
- Scenes: PascalCase matching root node (`PlayerController.tscn`)
- Constants: PascalCase (`MaxHealth`, `DefaultMoveSpeed`)

**Godot Both — GDScript + C#:**
Use GDScript conventions for `.gd` files and C# conventions for `.cs` files. Mixed-language files do not exist — the boundary is per-file. When in doubt about which language a new system should use, ask the user and record the decision in `technical-preferences.md`.

**Unity (C#):**
- Classes: PascalCase (e.g., `PlayerController`)
- Public fields/properties: PascalCase (e.g., `MoveSpeed`)
- Private fields: _camelCase (e.g., `_moveSpeed`)
- Methods: PascalCase (e.g., `TakeDamage()`)
- Files: PascalCase matching class (e.g., `PlayerController.cs`)
- Constants: PascalCase or UPPER_SNAKE_CASE

**Unreal (C++):**
- Classes: Prefixed PascalCase (`A` for Actor, `U` for UObject, `F` for struct)
- Variables: PascalCase (e.g., `MoveSpeed`)
- Functions: PascalCase (e.g., `TakeDamage()`)
- Booleans: `b` prefix (e.g., `bIsAlive`)
- Files: Match class without prefix (e.g., `PlayerController.h`)

**[通用产品]** Language defaults:

**Python:**
- Classes: PascalCase (e.g., `UserService`, `OrderRepository`)
- Variables/functions: snake_case (e.g., `get_user_by_id`, `calculate_total`)
- Files/modules: snake_case (e.g., `user_service.py`, `order_repository.py`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`)
- Private members: `_leading_underscore` (e.g., `_cache`, `_db_pool`)

**TypeScript:**
- Classes/components: PascalCase (e.g., `UserProfile`, `DashboardView`)
- Variables/functions: camelCase (e.g., `fetchUserData`, `handleSubmit`)
- Files: kebab-case for components (e.g., `user-profile.tsx`), camelCase for utilities (e.g., `apiClient.ts`)
- Constants: UPPER_SNAKE_CASE for global (e.g., `API_BASE_URL`), camelCase for local
- Types/interfaces: PascalCase (e.g., `User`, `OrderStatus`), prefix with `I` only if team convention requires

**Rust:**
- Types/traits/enums: PascalCase (e.g., `UserRepository`, `ConnectionPool`)
- Variables/functions: snake_case (e.g., `get_user`, `handle_request`)
- Files/modules: snake_case (e.g., `user_repository.rs`, `connection_pool.rs`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_CONNECTIONS`, `DEFAULT_PORT`)
- Macros: snake_case or `macro_rules!` convention

**Go:**
- Exported: PascalCase (e.g., `UserService`, `GetUser`, `HTTPClient`)
- Unexported: camelCase (e.g., `userService`, `getUser`, `httpClient`)
- Files: snake_case or lowercase (e.g., `user_service.go`, `httpclient.go`)
- Constants: PascalCase if exported (e.g., `MaxRetries`), camelCase if not
- Acronyms: all-caps (e.g., `HTTPServer`, `userID`, `parseURL`)

### [通用场景] Platform & Configuration

**[游戏专用]** Input & Platform section.

Populate `## Input & Platform` using the answers gathered in Section 2 (or extracted from the game concept). Derive the values using this mapping:

| Platform target | Gamepad Support | Touch Support |
|-----------------|-----------------|---------------|
| PC only | Partial (recommended) | None |
| Console | Full | None |
| Mobile | None | Full |
| PC + Console | Full | None |
| PC + Mobile | Partial | Full |
| Web | Partial | Partial |

For **Primary Input**, use the dominant input for the game genre:
- Action/RPG/platformer targeting console → Gamepad
- Strategy/point-and-click/RTS → Keyboard/Mouse
- Mobile game → Touch
- Cross-platform → ask the user

Present the derived values and ask the user to confirm or adjust before writing.

Example filled section:
```markdown
## Input & Platform
- **Target Platforms**: PC, Console
- **Input Methods**: Keyboard/Mouse, Gamepad
- **Primary Input**: Gamepad
- **Gamepad Support**: Full
- **Touch Support**: None
- **Platform Notes**: All UI must support d-pad navigation. No hover-only interactions.
```

**[通用产品]** Platform & Deployment section.

Populate `## Platform & Deployment` using the platform answers from Section 2. Derive the values using this mapping:

| Platform target | Deployment strategy | Key concerns |
|-----------------|---------------------|-------------|
| Web | Vercel/Netlify (JS), Docker + cloud (Python/Go/Rust) | CDN, SSR/CSR, SEO, accessibility |
| Desktop | Electron-builder (JS), Tauri bundler (Rust) | Installer format, auto-update, OS compatibility |
| Mobile | App Store/Google Play, Expo (React Native) | Offline support, battery, push notifications |
| CLI | pip/npm/cargo/brew distribution | Single binary (Go/Rust), PATH installation |
| Server | Docker + Kubernetes, cloud-specific (ECS/Lambda/Cloud Run) | Scaling strategy, health checks, graceful shutdown |

Present the derived values and ask the user to confirm or adjust before writing.

Example filled section:
```markdown
## Platform & Deployment
- **Target Platforms**: Web, Mobile
- **Deployment**: Vercel (web frontend), Fly.io (API backend)
- **Containerization**: Docker for backend services
- **Platform Notes**: Mobile uses React Native with Expo. Offline-first with local SQLite + server sync.
```

### [通用场景] Remaining Sections

- **Performance Budgets**: Use `AskUserQuestion`:
  - Prompt: "Should I set default performance budgets now, or leave them for later?"
  - **游戏专用** Options: `[A] Set defaults now (60fps, 16.6ms frame budget, engine-appropriate draw call limit)` / `[B] Leave as [TO BE CONFIGURED] — I'll set these when I know my target hardware`
  - **通用产品** Options: `[A] Set defaults now (API latency <200ms p95, memory <512MB, cold start <5s)` / `[B] Leave as [TO BE CONFIGURED] — I'll set these when I know my target scale`
  - If [A]: populate with the suggested defaults. If [B]: leave as placeholder.
- **Testing**: Suggest stack-appropriate framework — ask before adding.
  - **游戏专用**: GUT for Godot, NUnit for Unity, UE Automation for Unreal
  - **通用产品**: pytest for Python, Vitest/Jest for JS/TS, `cargo test` for Rust, `go test` for Go
- **Forbidden Patterns**: Leave as placeholder
- **Allowed Libraries**: Leave as placeholder. **Guardrail**: Never add speculative dependencies.

### [通用场景] Agent Routing

**[游戏专用]** Engine Specialists Routing

Also populate the `## Engine Specialists` section in `technical-preferences.md` with the correct routing for the chosen engine:

**For Godot** — see [Godot language configuration](godot-language-configuration.md) Appendix A (A3. Engine Specialists Routing) for the routing table matching the language chosen.

**For Unity:**
```markdown
## Engine Specialists
- **Primary**: unity-specialist
- **Language/Code Specialist**: unity-specialist (C# review — primary covers it)
- **Shader Specialist**: unity-shader-specialist (Shader Graph, HLSL, URP/HDRP materials)
- **UI Specialist**: unity-ui-specialist (UI Toolkit UXML/USS, UGUI Canvas, runtime UI)
- **Additional Specialists**: unity-dots-specialist (ECS, Jobs system, Burst compiler), unity-addressables-specialist (asset loading, memory management, content catalogs)
- **Routing Notes**: Invoke primary for architecture and general C# code review. Invoke DOTS specialist for any ECS/Jobs/Burst code. Invoke shader specialist for rendering and visual effects. Invoke UI specialist for all interface implementation. Invoke Addressables specialist for asset management systems.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.cs files) | unity-specialist |
| Shader / material files (.shader, .shadergraph, .mat) | unity-shader-specialist |
| UI / screen files (.uxml, .uss, Canvas prefabs) | unity-ui-specialist |
| Scene / prefab / level files (.unity, .prefab) | unity-specialist |
| Native extension / plugin files (.dll, native plugins) | unity-specialist |
| General architecture review | unity-specialist |
```

**For Unreal:**
```markdown
## Engine Specialists
- **Primary**: unreal-specialist
- **Language/Code Specialist**: ue-blueprint-specialist (Blueprint graphs) or unreal-specialist (C++)
- **Shader Specialist**: unreal-specialist (no dedicated shader specialist — primary covers materials)
- **UI Specialist**: ue-umg-specialist (UMG widgets, CommonUI, input routing, widget styling)
- **Additional Specialists**: ue-gas-specialist (Gameplay Ability System, attributes, gameplay effects), ue-replication-specialist (property replication, RPCs, client prediction, netcode)
- **Routing Notes**: Invoke primary for C++ architecture and broad engine decisions. Invoke Blueprint specialist for Blueprint graph architecture and BP/C++ boundary design. Invoke GAS specialist for all ability and attribute code. Invoke replication specialist for any multiplayer or networked systems. Invoke UMG specialist for all UI implementation.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.cpp, .h files) | unreal-specialist |
| Shader / material files (.usf, .ush, Material assets) | unreal-specialist |
| UI / screen files (.umg, UMG Widget Blueprints) | ue-umg-specialist |
| Scene / prefab / level files (.umap, .uasset) | unreal-specialist |
| Native extension / plugin files (Plugin .uplugin, modules) | unreal-specialist |
| Blueprint graphs (.uasset BP classes) | ue-blueprint-specialist |
| General architecture review | unreal-specialist |
```

**[通用产品]** Agent Routing — populate with language specialist + general agents:

```markdown
## Agent Routing
- **Primary**: lead-programmer
- **Language Specialist**: [python-specialist / typescript-specialist / rust-specialist / go-specialist]
- **Performance**: performance-analyst
- **Security**: security-engineer
- **DevOps**: devops-engineer
- **QA**: qa-tester / qa-lead
- **Accessibility**: accessibility-specialist (if UI)
- **UX**: ux-designer (if UI)
- **Analytics**: analytics-engineer (if data-heavy)
```

### File Extension Routing

**For Python:**
```markdown
### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Source code (.py files) | python-specialist |
| Test files (test_*.py) | qa-tester |
| CI/CD config (.github/workflows/) | devops-engineer |
| Infrastructure (Dockerfile, docker-compose.yml) | devops-engineer |
| Config / typing (.pyi, pyproject.toml) | python-specialist |
| Security-sensitive paths (auth, permissions) | security-engineer |
| Performance-critical paths | performance-analyst |
| General architecture review | lead-programmer |
```

**For TypeScript:**
```markdown
### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Source code (.ts, .tsx files) | typescript-specialist |
| Test files (*.test.ts, *.spec.ts) | qa-tester |
| CI/CD config (.github/workflows/) | devops-engineer |
| Infrastructure (Dockerfile, docker-compose.yml) | devops-engineer |
| UI / styling (.css, .scss, .tsx components) | ui-programmer |
| Config (tsconfig.json, next.config.*, vite.config.*) | typescript-specialist |
| Security-sensitive paths (auth, permissions) | security-engineer |
| Performance-critical paths | performance-analyst |
| General architecture review | lead-programmer |
```

**For Rust:**
```markdown
### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Source code (.rs files) | rust-specialist |
| Test files (*_test.rs) | qa-tester |
| CI/CD config (.github/workflows/) | devops-engineer |
| Build config (Cargo.toml, build.rs) | rust-specialist |
| Infrastructure (Dockerfile) | devops-engineer |
| Unsafe blocks / FFI boundaries (.rs with `unsafe`) | rust-specialist + security-engineer |
| Performance-critical paths | performance-analyst |
| General architecture review | lead-programmer |
```

**For Go:**
```markdown
### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Source code (.go files) | go-specialist |
| Test files (*_test.go) | qa-tester |
| CI/CD config (.github/workflows/) | devops-engineer |
| Build config (go.mod, go.sum, Makefile) | go-specialist |
| Infrastructure (Dockerfile) | devops-engineer |
| Security-sensitive paths (auth, permissions) | security-engineer |
| Performance-critical paths | performance-analyst |
| General architecture review | lead-programmer |
```

### [通用场景] Collaborative Step

Present the filled-in preferences to the user.

**[游戏专用]** For Godot, include the chosen language and note where the full naming conventions and routing tables live:
> "Here are the default technical preferences for [engine] ([language if Godot]). The naming conventions and specialist routing are in [Godot language configuration](godot-language-configuration.md) — I'll apply the [GDScript/C#/Both] variant. Want to customize any of these, or shall I save the defaults?"

For all other engines, present the defaults directly without referencing the appendix.

**[通用产品]** For general stacks:
> "Here are the default technical preferences for [stack]. Want to customize any of these, or shall I save the defaults?"

Wait for approval before writing the file.

---
