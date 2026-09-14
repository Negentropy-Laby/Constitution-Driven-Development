# Engine and Stack Selection

> Loaded on demand from `setup-engine/SKILL.md`. Follow these requirements as part of the parent skill; do not treat this file as a separately invocable skill.

### [游戏专用] Engine Decision Matrix

Only if no prior engine experience. Ask in this order:

**Platform** (ask second, always — platform eliminates engines before any other factor):
- Prompt: "What platforms are you targeting?"
- Options: `PC (Steam/Epic)` / `Mobile (iOS/Android)` / `Console` / `Web` / `Multiple`
- Platform rules that feed directly into the recommendation:
  - Mobile → Unity strongly preferred; Unreal is a poor fit; Godot is viable for simple mobile
  - Console → Unity or Unreal; Godot console support requires third-party publishers or significant extra work
  - Web → Godot exports cleanly to web; Unity WebGL is functional; Unreal has poor web support
  - PC only → all engines viable; other factors decide
  - Multiple → Unity is the most portable across PC/mobile/console

1. **What kind of game?** (2D, 3D, or both?)
2. **Primary input method?** (keyboard/mouse, gamepad, touch, or mixed?)
3. **Team size and experience?** (solo beginner, solo experienced, small team?)
4. **Any strong language preferences?** (GDScript, C#, C++, visual scripting?)
5. **Budget for engine licensing?** (free only, or commercial licenses OK?)

**Engine honest tradeoffs** (identical to original):

**Godot 4**
- Genuine strengths: 2D (best in class), stylized/indie 3D, rapid iteration, free forever (MIT), open source, gentlest learning curve, best for solo devs who want full control
- Real limitations: 3D ecosystem is thin compared to Unity/Unreal (fewer tutorials, assets, community answers for 3D-specific problems); large open-world 3D is very hard and largely untested in Godot; console export requires third-party publishers or significant extra work; smaller professional job market
- Licensing reality: Truly free with no revenue thresholds ever. MIT license means you own everything.
- Best fit: 2D games of any scope; stylized/atmospheric 3D; contained 3D worlds (not open-world); first game projects where learning curve matters; projects where budget is a hard constraint at any scale

**Unity**
- Genuine strengths: Industry standard for mid-scope 3D and mobile; massive asset store and tutorial ecosystem; C# is a professional language; best console certification support for indie; strong community for almost every genre
- Real limitations: Licensing controversy in 2023 damaged trust (runtime fee was proposed then walked back — the risk of policy changes remains real); C# has a steeper initial curve than GDScript; heavier editor than Godot for simple projects
- Licensing reality: Free under $200K revenue AND 200K installs (Unity Personal/Plus). Only becomes costly if the game is genuinely successful — most indie games never hit this threshold. The 2023 controversy is worth knowing about but the actual current terms are reasonable for most indie developers.
- Best fit: Mobile games; mid-scope 3D; games targeting console; developers with C# background; projects needing large asset store; teams of 2-5

**Unreal Engine 5**
- Genuine strengths: Best-in-class 3D visuals (Lumen, Nanite, Chaos physics); industry standard for AAA and photorealistic 3D; large open-world support is mature and production-tested; Blueprint visual scripting lowers C++ barrier; strong for games targeting high-end PC or console
- Real limitations: Steepest learning curve; heaviest editor (slow compile times, large project sizes); overkill for stylized/2D/small-scope games; C++ is genuinely hard; not suitable for mobile or web; 5% royalty past $1M gross revenue
- Licensing reality: 5% royalty only applies AFTER $1M gross revenue per title. For a first game or any game that doesn't reach $1M, it costs nothing. This threshold is high enough that most indie developers will never pay it.
- Best fit: AAA-quality 3D; large open-world games; photorealistic visuals; developers with C++ experience or willing to use Blueprint; games targeting high-end PC/console where visual fidelity is a core selling point

**Genre-specific guidance** (factor this into the recommendation):
- 2D any style → Godot strongly preferred
- 3D stylized / atmospheric / contained world → Godot viable, Unity solid alternative
- 3D open world (large, seamless) → Unity or Unreal; Godot is not production-proven for this
- 3D photorealistic / AAA-quality → Unreal
- Mobile-first → Unity strongly preferred
- Console-first → Unity or Unreal; Godot console support requires extra work
- Horror / narrative / walking sim → any engine; match to art style and team experience
- Action RPG / Soulslike → Unity or Unreal for 3D; community support and assets matter here
- Platformer 2D → Godot
- Strategy / top-down / RTS → Godot or Unity depending on 2D vs 3D

**Recommendation format:**
1. Show a comparison table with the user's specific factors as rows
2. Give a primary recommendation with honest reasoning
3. Name the best alternative and when to choose it instead
4. Explicitly state: "This is a starting point, not a verdict — you can always migrate engines, and many developers switch between projects."
5. Use `AskUserQuestion` to confirm: "Does this recommendation feel right, or would you like to explore a different engine?"
   - Options: `[Primary engine] (Recommended)` / `[Alternative engine]` / `[Third engine]` / `Explore further` / `Type something`

**If the user picks "Explore further":**
Use `AskUserQuestion` with concept-specific deep-dive topics. Always generate these options from the user's actual concept — do not use generic options. Always include at minimum:
- The primary engine's specific limitations for this concept (e.g., "How far can Godot 3D actually go for [genre]?")
- The alternative engine's specific tradeoffs for this concept
- Language choice impact on this concept's technical challenges
- Any concept-specific technical concern (e.g., adaptive audio, open-world streaming, multiplayer netcode)

The user can select multiple topics. Answer each selected topic in depth before returning to the engine confirmation question.

---

### [通用产品] Stack Decision Matrix

Only if no prior stack experience. Ask in this order:

**Platform** (ask second, always — platform eliminates or heavily weights stacks before any other factor):
- Prompt: "What platforms are you targeting?"
- Options: `Web (browser)` / `Desktop (Windows/macOS/Linux)` / `Mobile (iOS/Android)` / `CLI / Server` / `Multiple platforms`
- Platform rules that feed directly into the recommendation:
  - Web → JS/TS ecosystem most mature for frontend; Python (Django/Flask) strong for server-rendered; Rust/Wasm viable for performance-critical browser workloads
  - Mobile → React Native or Flutter for cross-platform; Swift/Kotlin for native; PWA for simple mobile web
  - Desktop → Electron (JS) for rapid cross-platform; Tauri (Rust) for lightweight; native (Swift/C#/C++) for single-platform
  - CLI → Python, Go, or Rust depending on performance needs and distribution model (single binary vs pip install)
  - Server → Python, Go, Rust, or Node depending on throughput, concurrency model, and ecosystem needs
  - Multiple → JS/TS with React/React Native covers web+mobile; Go or Rust for CLI+server portability

**Question 3 — Project type** (ask this third):
- Prompt: "What kind of project is this?"
- Options: `Web app / SaaS` / `REST API / Backend` / `CLI tool` / `Desktop app` / `Mobile app` / `Data pipeline / ETL` / `AI/ML product` / `Library / SDK`

**Question 4 — Performance needs** (ask this fourth):
- Prompt: "What are the performance requirements?"
- Options: `Not a concern — developer speed matters more` / `Moderate — responsive is enough` / `High — low latency or high throughput` / `Critical — every millisecond counts`

**Question 5 — Team size and experience** (ask this fifth):
- Prompt: "What's your team setup?"
- Options: `Solo developer` / `Small team (2-5)` / `Medium team (6-20)` / `Large team (20+)`
- Team notes: Solo/small → prioritize ecosystem maturity and iteration speed. Medium+ → can invest in Rust/Go for performance-critical paths. Large → hiring pool and onboarding matter.

**Question 6 — Language preferences** (ask this sixth):
- Prompt: "Any strong language preferences or aversions?"
- Options: `Prefer dynamically typed (Python, JS)` / `Prefer statically typed (TypeScript, Rust, Go)` / `No preference` / `I'll describe`
- Reality notes: If the user hates async patterns, Python's asyncio may frustrate them. If they love type safety, Rust or TypeScript will feel more natural.

**Question 7 — Budget and licensing** (ask this seventh):
- Prompt: "Any licensing or cost constraints?"
- Options: `Free / open-source only` / `Commercial OK but prefer free` / `No constraints`

**Ecosystem honest tradeoffs:**

**Python (Django / FastAPI / Flask)**
- Strengths: Fastest iteration speed, massive library coverage (web, data, AI/ML), gentle learning curve, huge community
- Limitations: Slower runtime, GIL limits CPU concurrency, async story fragmented, dynamic typing
- Performance reality: Fast enough for 90% of products. Instagram/Spotify/Dropbox run on Python.
- Best fit: APIs, web backends, data tools, AI/ML, internal tools, rapid prototyping

**JavaScript/TypeScript (React / Next.js / Node)**
- Strengths: One language full-stack, best web UI ecosystem, Vercel/Netlify near-zero ops, TypeScript type safety, React Native extends to mobile
- Limitations: NPM churn, bundler/config complexity, Node overhead vs compiled languages
- Performance reality: Node fast for I/O-bound work. Not for CPU-bound. V8 JIT excellent for web workloads.
- Best fit: Web apps, SaaS, interactive UIs, real-time features, full-stack products

**Rust**
- Strengths: Best-in-class performance+safety, zero-cost abstractions, excellent CLI/Wasm, Cargo, fearless concurrency, single binary
- Limitations: Steepest learning curve, slower iteration (compile times), smaller web ecosystem, smaller hiring pool
- Performance reality: Right choice when performance is a hard requirement. Overkill for CRUD APIs.
- Best fit: Performance-critical systems, CLIs, Wasm, infrastructure, network services

**Go**
- Strengths: Simple language, excellent concurrency, fast compile, single binary, first-class cloud-native (K8s, Docker, Terraform)
- Limitations: Verbose error handling, limited generics, smaller web framework ecosystem
- Performance reality: Sweet spot between Python's speed and Rust's performance. Excellent for networked services.
- Best fit: Cloud services, APIs, CLIs, DevOps tooling, microservices, infrastructure

**Project type guidance**: Web app→JS/TS UI + Python/Go/TS backend; REST API→Python(FastAPI)/Go/Rust; CLI→Go/Rust; Desktop→Electron(JS)/Tauri(Rust); Mobile→React Native/Flutter; Data/ETL→Python; AI/ML→Python; Library→match target audience ecosystem

### [通用产品] Framework Sub-Selection

Once ecosystem is determined, narrow to a specific framework. This mirrors Godot's GDScript vs C# language selection — the ecosystem is the engine, the framework is the dialect.

Use `AskUserQuestion` with options from the user's project type:

**Python**: `FastAPI (APIs, async)` / `Django (full-featured)` / `Flask (minimal)` / `Litestar (typed FastAPI alt)` / `No framework — pure Python`

**JS/TS**: `Next.js (full-stack React, SSR)` / `React + Vite (SPA)` / `Vue / Nuxt` / `Express / Fastify (backend only)` / `Node — no frontend framework`

**Rust**: `Axum (async, Tokio-native)` / `Actix Web (mature)` / `Rocket (ergonomic)` / `CLI only — clap + anyhow` / `Library — no framework`

**Go**: `stdlib + chi router (minimal)` / `Gin (popular)` / `Echo (high-perf)` / `Fiber (Express-like)` / `CLI only — cobra + viper`

Record the framework choice. It drives the INSTRUCTIONS.md template, default dependencies, and agent routing.

**Recommendation format**: Same as game mode — comparison table, primary recommendation, alternative, confirmation via `AskUserQuestion`.

**If the user picks "Explore further":**
Use `AskUserQuestion` with concept-specific deep-dive topics. Always generate these options from the user's actual concept — do not use generic options. Always include at minimum:
- The primary stack's specific limitations for this project type (e.g., "How far can FastAPI scale for [use case]?")
- The alternative stack's specific tradeoffs for this concept
- Language choice impact on this concept's technical challenges
- Any concept-specific technical concern (e.g., real-time collaboration, offline support, data sync, multi-tenancy)

The user can select multiple topics. Answer each selected topic in depth before returning to the stack confirmation question.

---
