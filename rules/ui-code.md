---
paths:
  - "src/ui/**"
  - "src/app/**"
  - "src/web/**"
---

# UI Code Rules

- [Game] UI must NEVER own or directly modify game state — display only, use commands/events to request changes
- All UI text must go through the localization system — no hardcoded user-facing strings
- [Game] Support keyboard/mouse AND gamepad where both are configured targets;
  verify touch/other inputs where configured.
- All animations must be skippable and respect user motion/accessibility preferences
- [Game] UI sounds use the configured audio event system, not direct playback
- [Game] UI never blocks the game thread; Product UI preserves responsiveness
  under its configured browser/app/event-loop model.
- Visual UI needs scalable text and non-color-only meaning; configured Game
  colorblind modes and Product accessibility criteria remain testable.
- Test visual screens at supported minimum/maximum resolutions; headless/API/CLI
  scope records its applicable interaction/accessibility evidence.
- Product UI must not own server/domain state directly — use typed commands, API clients, or service adapters.
- Product screens must document loading, empty, error, permission, offline, and partial-success states.
- Product forms and workflows must preserve user input on recoverable errors and expose actionable validation messages.
- Public user flows need interaction, component, or E2E evidence before story completion.

Read `standards/technical-preferences.md` and the actual surface profile for
input/platform constraints. Retain Product state/auth/workflow requirements;
do not invent gamepad/audio/game-thread dependencies for absent capabilities.
Apply `standards/evidence-lifecycle.md` to verification/completion claims.
