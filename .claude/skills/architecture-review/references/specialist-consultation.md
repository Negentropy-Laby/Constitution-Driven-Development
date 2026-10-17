# Technology Specialist Consultation

After completing the Phase 5 audit, spawn the appropriate specialist via Task for a domain-expert second opinion:

**[游戏专用]** **Engine Specialist Consultation**:
- Read `standards/technical-preferences.md` `Engine Specialists` section to get the primary specialist
- If no engine is configured, skip this consultation
- Spawn `subagent_type: [primary specialist]` with: all ADRs that contain engine-specific decisions or `Post-Cutoff APIs Used` fields, the engine reference docs, and the Phase 5 audit findings. Ask them to:
  1. Confirm or challenge each audit finding — specialists may know of engine nuances not captured in the reference docs
  2. Identify engine-specific anti-patterns in the ADRs that the audit may have missed (e.g., using the wrong Godot node type, Unity component coupling, Unreal subsystem misuse)
  3. Flag ADRs that make assumptions about engine behaviour that differ from the actual pinned version

**[通用产品]** **Language Specialist Consultation**:
- Read `standards/technical-preferences.md` to determine the primary language specialist
- If no stack is configured, skip this consultation
- Spawn the language specialist with: all ADRs that contain stack-specific decisions or `Post-Cutoff APIs Used` fields, the stack reference docs, and the Phase 5 audit findings. Ask them to:
  1. Confirm or challenge each audit finding
  2. Identify stack-specific anti-patterns in the ADRs (e.g., N+1 queries, blocking I/O in async context, missing connection pooling)
  3. Flag ADRs that make assumptions about framework behaviour that differ from the actual pinned version

Incorporate additional findings under `### Specialist Findings` in the Phase 5 output. These feed into the final verdict — specialist-identified issues carry the same weight as audit-identified issues.
