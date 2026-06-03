---
name: constitute-check
description: "Lightweight constitutional audit — checks whether the project constitution exists, whether principles are aligned with current code and docs, and identifies gaps. Read-only."
argument-hint: "[optional: 'full' for verbose report, or a specific principle number]"
user-invocable: true
allowed-tools: Read, Glob, Grep
model: haiku
context: |
  !echo "=== Constitution Status ===" && echo "T0: $(ls memory_bank/t0_core/ 2>/dev/null | wc -l) files" && echo "T1: $(ls memory_bank/t1_axioms/ 2>/dev/null | wc -l) files" && echo "Review mode: $(cat production/review-mode.txt 2>/dev/null || echo 'not set')"
---

## Phase 0: Domain Routing

Detect the project domain before checking constitution compliance:
- `design/cdd/game-concept.md` -> **[Game]** verify principles against player fantasy, core loop, game pillars, playtest evidence, and game-specific CDDs.
- `design/cdd/product-concept.md` -> **[Product]** verify principles against user promise, JTBD, target workflows, product modules, API/CLI contracts, and product-specific CDDs.
- If neither exists, check only the constitution and report that domain-specific validation is pending.

Do not remove game constitution examples. Product checks are an added validation path.
# Constitution Check — Constitutional Health Audit

This skill is read-only — it reports findings but writes no files.

This skill checks the health of a project's constitution: whether it exists,
whether the principles are still aligned with the codebase, and what gaps
need attention. It is lightweight — not a full 4-gate CDD audit. For a
complete project scan, use `/project-stage-detect`.

---

## Step 1: Verify Constitution Exists

Check for the minimum constitutional artifacts:

| Artifact | Required? | How to check |
|----------|-----------|--------------|
| `memory_bank/t0_core/basic_law_index.md` | **Yes** | Read if exists |
| `memory_bank/t0_core/active_context.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/tech_context.md` | **Yes** | Read if exists |
| `memory_bank/t1_axioms/system_patterns.md` | Recommended | Read if exists |
| `memory_bank/t1_axioms/behavior_context.md` | Recommended | Read if exists |
| `memory_bank/t0_core/knowledge_graph.md` | Optional | Read if exists |
| `memory_bank/README.md` | Recommended | Read if exists |
| `memory_bank/module_support_map.yaml` | Optional | Read if exists |

If `basic_law_index.md` is missing: "No constitution detected. Run `/constitute`
to establish one." Stop here — nothing else to check.

If `basic_law_index.md` exists but `active_context.md` or `tech_context.md`
is missing: flag as a gap. "Your constitution exists but is incomplete."

---

## Step 2: Read the Constitution

Read `memory_bank/t0_core/basic_law_index.md` and extract:
- Core thesis (Support ID: BL-01)
- All laws/ principles (Support IDs: BL-02 through BL-06)
- Each law's current-state requirement

Read `memory_bank/t0_core/active_context.md` and extract:
- Current working state (State A-E)
- Module status summaries
- Active risks and open decisions

Read `memory_bank/t1_axioms/tech_context.md` and extract:
- Language, framework, platform
- Performance budgets
- External dependencies

---

## Step 3: Alignment Check

For each constitutional principle, check alignment with the codebase:

### 3a: Principle → Code Alignment

For each law in `basic_law_index.md`, perform a quick alignment scan:

1. Read the law's current-state requirement
2. Check whether the codebase respects it
3. Flag violations or uncertainties

Example checks:
- Law requires "no function over 20 lines" → grep for functions, check length
- Law requires "API stability: no breaking changes" → check for deprecation markers
- Law requires "all public APIs documented" → check docstring coverage in `src/`
- Law requires "tests before merge" → check test file count vs source file count

For each law, produce one of:
- **ALIGNED** — evidence found that the law is being followed
- **CONCERN** — potential violation or insufficient evidence
- **UNABLE TO CHECK** — law is abstract or can't be auto-verified (e.g., "prioritize user experience")

### 3b: Tech Context → Reality Check

Compare `tech_context.md` against actual project state:
- Is the declared language actually used? (Glob `src/**` for language files)
- Are declared dependencies actually in the project? (Check config files)
- Are performance budgets plausible given the codebase size?

---

## Step 4: Gap Detection

Identify what's missing or stale:

| Gap | Detection |
|-----|-----------|
| **Missing T1 docs** | `t1_axioms/` has fewer than 3 files |
| **Missing knowledge graph** | `knowledge_graph.md` does not exist |
| **Missing README** | `memory_bank/README.md` does not exist |
| **Stale tech context** | Tech context mentions old versions or unused dependencies |
| **Drifted principles** | Law says X, code does Y |
| **Missing module support map** | No `module_support_map.yaml` but T2 docs exist |
| **No review mode set** | `production/review-mode.txt` does not exist |

---

## Step 5: Present Report

Keep it concise. Use this format:

```
## Constitutional Health: [Project Name]

**Core thesis:** [from BL-01, one line]
**Constitution established:** [date from active_context.md or file timestamp]

### ✓ Principles (N/M aligned)
- [Support ID]: ALIGNED — [brief evidence]
- [Support ID]: ALIGNED — [brief evidence]
- [Support ID]: CONCERN — [what's wrong, suggestion]

### ✓ Tech Stack
- Language: [X] ✓
- Framework: [Y] ✓
- Platform: [Z] ✓
- [Any concerns]

### → Gaps
- [Gap 1 — with concrete fix, e.g. "Run /constitute-check to regenerate"]
- [Gap 2]

### → Recommendations
1. [Highest priority action]
2. [Secondary action]

---
**Overall:** [HEALTHY / NEEDS ATTENTION / CRITICAL]
```

**Severity levels:**
- **HEALTHY**: All required artifacts present, all checkable laws ALIGNED
- **NEEDS ATTENTION**: 1-2 CONCERNs or minor gaps
- **CRITICAL**: Missing required artifacts, 3+ CONCERNs, or stale constitution

If verbosity argument is `full`, add a detailed per-law analysis section with
the specific evidence found for each alignment check.

---

## Edge Cases

- **No constitution**: "No constitution detected. Run `/constitute` to establish your project's governing principles." Stop.
- **Constitution exists but is very old**: Note the date — "Your constitution was established [N months] ago. Much may have changed. Consider running `/constitute` to refresh it."
- **Path D project (existing code, new constitution)**: Flag likely drift — "Your constitution was recently established. Some existing code may not yet align. This is normal for brownfield adoption — prioritize alignment iteratively."
- **All laws are abstract (can't auto-check)**: "Your principles are abstract — they can't be automatically verified. Consider adding falsifiable current-state requirements to each law for future audits."

---

## Collaborative Protocol

- **Read-only.

** This skill never writes files.
- **Be honest.

** Don't sugarcoat drift or gaps.
- **Be specific.

** Every gap must come with a concrete fix suggestion.
- **One primary recommendation.

** The user should leave knowing exactly one thing to do next.
