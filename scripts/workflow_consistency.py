#!/usr/bin/env python3
"""Consistency checks for workflow catalog, docs, gates, and skills.

The parser is intentionally lightweight and dependency-free so it can run in a
template repository without installing PyYAML.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
TEMPLATES_DIR = REPO_ROOT / ".claude" / "docs" / "templates"
CATALOG = REPO_ROOT / ".claude" / "docs" / "workflow-catalog.yaml"
GATE_CHECK = REPO_ROOT / ".claude" / "skills" / "gate-check" / "SKILL.md"
FLOW_DIAGRAMS = REPO_ROOT / "docs" / "examples" / "skill-flow-diagrams.md"
WORKFLOW_GUIDE = REPO_ROOT / "docs" / "WORKFLOW-GUIDE.md"
QUICK_START = REPO_ROOT / ".claude" / "docs" / "quick-start.md"
DOC_COMMAND_FILES = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "START-HERE.md",
    QUICK_START,
]
DRIFT_SCAN_ROOTS = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "UPGRADING.md",
    REPO_ROOT / "docs",
    REPO_ROOT / ".claude" / "skills",
    REPO_ROOT / ".claude" / "docs",
]

COMMAND_REF = re.compile(r"(?<![\w.:-])/[a-z][a-z0-9-]*\b")
BACKTICK_PATH = re.compile(r"`([^`\n]+)`")
PATH_HINT = re.compile(
    r"^(?:\.claude|\.github|assets|config|db|design|docs|memory_bank|migrations|production|prototypes|schema|src|tests|tools)(?:/|$)"
)

IGNORED_COMMAND_LIKE = {
    "/api",
    "/cli",
    "/config",
    "/contracts",
    "/dev",
    "/docs",
    "/schema",
    "/src",
    "/tests",
    "/tmp",
}

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml"}
REQUIRED_GATE_HEADINGS = {
    "**Required Artifacts:**",
    "**Catalog Required Artifacts:**",
    "**Catalog Required Step Evidence:**",
}


@dataclass
class Finding:
    severity: str
    message: str


@dataclass
class CatalogStep:
    step_id: str
    command: str | None = None
    required: bool = False
    globs: list[str] = field(default_factory=list)
    note: str | None = None


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def collect_known_commands() -> set[str]:
    commands: set[str] = set()
    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        commands.add("/" + skill_file.parent.name)
    return commands


def template_exists_for(path_text: str) -> bool:
    if not TEMPLATES_DIR.exists():
        return False
    path = Path(path_text)
    name = path.name
    stem = path.stem
    return any(candidate.name == name or candidate.stem == stem for candidate in TEMPLATES_DIR.rglob("*") if candidate.is_file())


def existing_or_template(path_text: str) -> bool:
    normalized = path_text.rstrip("/").replace("\\", "/")
    if not normalized:
        return False
    if any(ch in normalized for ch in "*[]"):
        return template_exists_for(normalized)
    return (REPO_ROOT / normalized).exists() or template_exists_for(normalized)


def parse_catalog() -> list[CatalogStep]:
    steps: list[CatalogStep] = []
    current: CatalogStep | None = None
    in_artifact = False

    for raw in CATALOG.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- id:"):
            if current:
                steps.append(current)
            current = CatalogStep(step_id=line.split(":", 1)[1].strip().strip('"'))
            in_artifact = False
            continue
        if current is None:
            continue
        if line.startswith("artifact:"):
            in_artifact = True
            continue
        if re.match(r"^[a-zA-Z_-]+:", line) and not line.startswith(("glob:", "note:", "min_count:", "pattern:")):
            in_artifact = False
        if line.startswith("command:"):
            current.command = line.split(":", 1)[1].strip()
        elif line.startswith("required:"):
            current.required = line.split(":", 1)[1].strip().lower() == "true"
        elif in_artifact and line.startswith("glob:"):
            current.globs.append(line.split(":", 1)[1].strip().strip('"').strip("'"))
        elif in_artifact and line.startswith("note:"):
            current.note = line.split(":", 1)[1].strip().strip('"').strip("'")

    if current:
        steps.append(current)
    return steps


def check_catalog_commands(steps: list[CatalogStep], known_commands: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for step in steps:
        if step.command and step.command not in known_commands:
            findings.append(Finding("ERROR", f"catalog step {step.step_id} references missing skill command {step.command}"))
    return findings


def check_doc_commands(known_commands: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for path in DOC_COMMAND_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"https?://\S+", "", text)
        for match in COMMAND_REF.finditer(text):
            if match.start() > 0 and text[match.start() - 1] == "<":
                continue
            command = match.group(0)
            if command in IGNORED_COMMAND_LIKE:
                continue
            if command not in known_commands:
                findings.append(Finding("ERROR", f"{rel(path)} references missing skill command {command}"))
    return findings


def check_required_catalog_artifacts(steps: list[CatalogStep], known_commands: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for step in steps:
        if not step.required:
            continue
        if not step.globs and not step.note:
            continue
        if step.command and step.command in known_commands:
            continue
        missing = [glob for glob in step.globs if not existing_or_template(glob)]
        if missing and not step.note:
            findings.append(
                Finding(
                    "ERROR",
                    f"required catalog step {step.step_id} has artifacts without command/template trace: {', '.join(missing)}",
                )
            )
    return findings


def extract_required_gate_paths() -> set[str]:
    paths: set[str] = set()
    in_required = False
    for raw in GATE_CHECK.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line in REQUIRED_GATE_HEADINGS:
            in_required = True
            continue
        if in_required and line.startswith("**") and line not in REQUIRED_GATE_HEADINGS:
            in_required = False
        if not in_required:
            continue
        for match in BACKTICK_PATH.finditer(line):
            candidate = match.group(1).replace("\\", "/")
            if PATH_HINT.match(candidate):
                paths.add(candidate)
    return paths


def parent_prefix(path_text: str) -> str:
    normalized = path_text.rstrip("/").replace("\\", "/")
    if not normalized:
        return normalized
    if normalized.endswith("*.md"):
        normalized = normalized[:-4]
    if "/" not in normalized:
        return normalized
    return normalized.rsplit("/", 1)[0] + "/"


def check_gate_artifact_trace(steps: list[CatalogStep]) -> list[Finding]:
    findings: list[Finding] = []
    catalog_artifacts = [glob.replace("\\", "/") for step in steps for glob in step.globs]
    catalog_notes = [step.note or "" for step in steps]

    for path in sorted(extract_required_gate_paths()):
        if path.startswith(("docs/engine-reference/", "docs/reference/")) and any(
            step.command == "/setup-engine" for step in steps
        ):
            continue
        if existing_or_template(path):
            continue
        prefix = parent_prefix(path)
        traced = False
        for artifact in catalog_artifacts:
            artifact_prefix = parent_prefix(artifact)
            if path == artifact or path in artifact or artifact in path:
                traced = True
            if path.startswith("production/epics/") and artifact.startswith("production/epics/"):
                traced = True
            if prefix and (prefix == artifact_prefix or prefix.startswith(artifact_prefix) or artifact_prefix.startswith(prefix)):
                traced = True
        if not traced and any(path in note or prefix in note for note in catalog_notes):
            traced = True
        if not traced:
            findings.append(Finding("ERROR", f"gate-check required artifact has no catalog/template trace: {path}"))
    return findings


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
        elif path.is_dir():
            files.extend(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES
            )
    return files


def check_story_path_drift() -> list[Finding]:
    findings: list[Finding] = []
    pattern = re.compile(r"production/stories(?:/|\b)")
    for path in iter_text_files(DRIFT_SCAN_ROOTS):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                findings.append(
                    Finding(
                        "ERROR",
                        f"{rel(path)}:{line_no} uses legacy production/stories path; use production/epics/[epic-slug]/story-NNN-[slug].md",
                    )
                )
    return findings


def block_between(text: str, start: str, end: str) -> str:
    start_index = text.find(start)
    if start_index == -1:
        return ""
    end_index = text.find(end, start_index)
    if end_index == -1:
        return text[start_index:]
    return text[start_index:end_index]


def check_example_phase_boundaries() -> list[Finding]:
    findings: list[Finding] = []
    if not FLOW_DIAGRAMS.exists():
        findings.append(Finding("ERROR", f"missing examples flow diagram: {rel(FLOW_DIAGRAMS)}"))
        return findings

    text = FLOW_DIAGRAMS.read_text(encoding="utf-8", errors="replace")
    concept = block_between(text, "PHASE 1: CONCEPT", "PHASE 2: SYSTEMS DESIGN")
    pre_production = block_between(text, "PHASE 4: PRE-PRODUCTION", "PHASE 5: PRODUCTION")
    release = block_between(text, "PHASE 7: RELEASE", "```")

    if "/setup-engine" in concept:
        findings.append(
            Finding("ERROR", "docs/examples/skill-flow-diagrams.md places /setup-engine in Concept; it belongs in Technical Setup")
        )
    if "/test-setup" in pre_production:
        findings.append(
            Finding("ERROR", "docs/examples/skill-flow-diagrams.md places /test-setup in Pre-Production; it belongs in Technical Setup")
        )
    release_index = release.find("/release-checklist")
    launch_index = release.find("/launch-checklist")
    team_index = release.find("/team-release")
    if not (0 <= release_index < launch_index < team_index):
        findings.append(
            Finding("ERROR", "docs/examples/skill-flow-diagrams.md must order Release as /release-checklist -> /launch-checklist -> /team-release")
        )
    return findings


def check_accessibility_entry_paths() -> list[Finding]:
    findings: list[Finding] = []
    required_docs = [
        REPO_ROOT / "docs" / "START-HERE.md",
        REPO_ROOT / ".claude" / "docs" / "quick-start.md",
        REPO_ROOT / ".claude" / "skills" / "constitute" / "SKILL.md",
    ]
    for path in required_docs:
        text = path.read_text(encoding="utf-8", errors="replace")
        if "design/accessibility-requirements.md" not in text:
            findings.append(Finding("ERROR", f"{rel(path)} omits Technical Setup accessibility requirements"))
        if "/create-control-manifest" in text and re.search(r"/create-control-manifest[^\n]*/test-setup", text):
            findings.append(
                Finding(
                    "ERROR",
                    f"{rel(path)} places /create-control-manifest and /test-setup in one chain without a separate accessibility step",
                )
            )
    return findings


def check_quick_start_technical_setup_paths() -> list[Finding]:
    findings: list[Finding] = []
    text = QUICK_START.read_text(encoding="utf-8", errors="replace")
    path_blocks = [
        ("Game Path A", "### Path A:", "### Path B:"),
        ("Game Path B", "### Path B:", "### Path C:"),
        ("Product Path A", "### Product Path A:", "### Product Path B:"),
        ("Product Path B", "### Product Path B:", "### Product Path C:"),
    ]
    required_commands = ["/architecture-review", "/gate-check technical-setup"]

    for label, start, end in path_blocks:
        block = block_between(text, start, end)
        if not block:
            findings.append(Finding("ERROR", f".claude/docs/quick-start.md missing {label} block"))
            continue
        for command in required_commands:
            if command not in block:
                findings.append(Finding("ERROR", f".claude/docs/quick-start.md {label} omits {command}"))
        gate_index = block.find("/gate-check technical-setup")
        ux_index = block.find("/ux-design")
        if gate_index == -1 or ux_index == -1:
            continue
        if not gate_index < ux_index:
            findings.append(
                Finding(
                    "ERROR",
                    f".claude/docs/quick-start.md {label} starts UX before /gate-check technical-setup",
                )
            )
    return findings


def check_old_workflow_drift() -> list[Finding]:
    findings: list[Finding] = []
    banned = [
        ("docs/architecture/master.md", "use docs/architecture/architecture.md"),
        ("/ux-design accessibility", "create design/accessibility-requirements.md from the template"),
        ("production/validation/", "use production/qa/evidence/"),
        ("production/user-testing/", "use production/qa/evidence/user-tests/"),
        ("production/playtests/", "use production/qa/evidence/playtests/"),
        ("tests/evidence/", "use production/qa/evidence/"),
    ]
    for path in iter_text_files(DRIFT_SCAN_ROOTS):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for needle, replacement in banned:
                if needle in line:
                    findings.append(Finding("ERROR", f"{rel(path)}:{line_no} uses {needle}; {replacement}"))
    return findings


def check_art_bible_phase_drift() -> list[Finding]:
    findings: list[Finding] = []
    pattern = re.compile(
        r"(?:art-bible.*Technical Setup.*(?:required|blocker)|Technical Setup.*art-bible)",
        re.IGNORECASE,
    )
    for path in iter_text_files(DRIFT_SCAN_ROOTS):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                findings.append(
                    Finding(
                        "ERROR",
                        f"{rel(path)}:{line_no} treats /art-bible as a Technical Setup requirement; it is Concept optional",
                    )
                )
    return findings


def check_workflow_guide_phase_boundaries() -> list[Finding]:
    findings: list[Finding] = []
    text = WORKFLOW_GUIDE.read_text(encoding="utf-8", errors="replace")
    phase4 = block_between(text, "## Phase 4: Pre-Production", "## Phase 5: Production")
    phase5 = block_between(text, "## Phase 5: Production", "## Phase 6:")

    if "/dev-story" in phase4:
        findings.append(Finding("ERROR", "docs/WORKFLOW-GUIDE.md Phase 4 contains /dev-story; implementation belongs in Phase 5"))
    if "/dev-story" not in phase5:
        findings.append(Finding("ERROR", "docs/WORKFLOW-GUIDE.md Phase 5 must document /dev-story implementation"))
    return findings


def check_validation_quantity_boundaries() -> list[Finding]:
    findings: list[Finding] = []
    guide_text = WORKFLOW_GUIDE.read_text(encoding="utf-8", errors="replace")
    phase4 = block_between(guide_text, "## Phase 4: Pre-Production", "## Phase 5: Production")
    phase5_plus = block_between(guide_text, "## Phase 5: Production", "## Quick Reference:")

    banned_phase4_patterns = [
        r"Played unguided in at least 3 sessions",
        r"Vertical Slice played in 3\+ sessions",
        r"3\+ sessions",
        r"3 unguided sessions",
        r"at least 3 [^\n]*sessions",
    ]
    for pattern in banned_phase4_patterns:
        if re.search(pattern, phase4, flags=re.IGNORECASE):
            findings.append(
                Finding(
                    "ERROR",
                    "docs/WORKFLOW-GUIDE.md Phase 4 makes 3 sessions a Pre-Production gate condition",
                )
            )
            break

    catalog_text = CATALOG.read_text(encoding="utf-8", errors="replace")
    if catalog_text.count("min_count: 3") < 2:
        findings.append(Finding("ERROR", "workflow-catalog.yaml must keep cumulative 3-session validation in Polish / Verification"))
    if "3 sessions" not in phase5_plus and "3-session" not in phase5_plus:
        findings.append(Finding("ERROR", "docs/WORKFLOW-GUIDE.md must keep cumulative 3-session validation after Pre-Production"))

    gate_text = GATE_CHECK.read_text(encoding="utf-8", errors="replace")
    release_gate = block_between(gate_text, "### Gate: Polish → Release", "## 3. Run the Gate Check")
    if "At least 3 playtest reports" not in release_gate:
        findings.append(Finding("ERROR", "gate-check Polish → Release gate must require cumulative 3 game playtest reports"))
    if "At least 3 product validation reports" not in release_gate:
        findings.append(Finding("ERROR", "gate-check Verification → Release gate must require cumulative 3 product validation reports"))
    return findings


def check_gate_required_semantics() -> list[Finding]:
    findings: list[Finding] = []
    in_required = False
    banned_required_patterns = [
        "Art bible exists at `design/art/art-bible.md`",
        "At least 3 distinct user testing sessions",
        "QA plan exists in `production/qa/` (generated by `/qa-plan`)",
        "QA sign-off report exists in `production/qa/`",
        "QA test plan exists",
        "QA sign-off report exists",
        "Smoke check passes cleanly",
        "Release checklist completed",
        "Launch checklist completed",
        "`/release-checklist` run before `/launch-checklist`",
    ]
    for line_no, raw in enumerate(GATE_CHECK.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        line = raw.strip()
        if line in REQUIRED_GATE_HEADINGS:
            in_required = True
            continue
        if in_required and line.startswith("**") and line not in REQUIRED_GATE_HEADINGS:
            in_required = False
        if not in_required:
            continue
        for pattern in banned_required_patterns:
            if pattern in line:
                findings.append(Finding("ERROR", f"{rel(GATE_CHECK)}:{line_no} keeps old non-catalog blocker: {pattern}"))
    return findings


def check_release_phase_contract() -> list[Finding]:
    findings: list[Finding] = []
    catalog_text = CATALOG.read_text(encoding="utf-8", errors="replace")
    release_block = block_between(catalog_text, "  release:", "\n\nquality_gates:")
    required_commands: dict[str, bool] = {}
    current_command: str | None = None
    for raw in release_block.splitlines():
        line = raw.strip()
        if line.startswith("command: "):
            current_command = line.split(":", 1)[1].strip()
            continue
        if line.startswith("required: ") and current_command:
            required_commands[current_command] = line.endswith("true")
            current_command = None

    expected = ["/release-checklist", "/launch-checklist", "/team-release"]
    for command in expected:
        if required_commands.get(command) is not True:
            findings.append(Finding("ERROR", f"workflow-catalog.yaml Release phase must require {command}"))

    order_positions = [release_block.find(command) for command in expected]
    if not all(position >= 0 for position in order_positions) or order_positions != sorted(order_positions):
        findings.append(
            Finding(
                "ERROR",
                "workflow-catalog.yaml must order Release as /release-checklist -> /launch-checklist -> /team-release",
            )
        )

    phase_gate_phrases = [
        "before proceeding to release",
        "before launch",
    ]
    for skill_path in [
        SKILLS_DIR / "release-checklist" / "SKILL.md",
        SKILLS_DIR / "launch-checklist" / "SKILL.md",
    ]:
        text = skill_path.read_text(encoding="utf-8", errors="replace")
        for phrase in phase_gate_phrases:
            if phrase in text:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{rel(skill_path)} must not require a repeated phase gate {phrase}",
                    )
                )
    return findings


def check_template_count_contract() -> list[Finding]:
    findings: list[Finding] = []
    actual = sum(1 for path in TEMPLATES_DIR.rglob("*") if path.is_file())
    checks = [
        (
            REPO_ROOT / "README.md",
            [
                re.compile(r"\|\s*\*\*Templates\*\*\s*\|\s*(\d+)\s*\|"),
                re.compile(r"(\d+)\s+document templates"),
            ],
        ),
        (
            QUICK_START,
            [
                re.compile(r"(\d+)\s+document templates"),
            ],
        ),
    ]
    for path, patterns in checks:
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in patterns:
            matches = list(pattern.finditer(text))
            if not matches:
                findings.append(Finding("ERROR", f"{rel(path)} must state the current template count ({actual})"))
                continue
            for match in matches:
                documented = int(match.group(1))
                if documented != actual:
                    findings.append(
                        Finding(
                            "ERROR",
                            f"{rel(path)} documents {documented} templates, but .claude/docs/templates contains {actual}",
                        )
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warnings-as-errors", action="store_true", help="Treat WARN findings as errors.")
    args = parser.parse_args()

    known_commands = collect_known_commands()
    steps = parse_catalog()
    findings: list[Finding] = []
    findings.extend(check_catalog_commands(steps, known_commands))
    findings.extend(check_doc_commands(known_commands))
    findings.extend(check_required_catalog_artifacts(steps, known_commands))
    findings.extend(check_gate_artifact_trace(steps))
    findings.extend(check_story_path_drift())
    findings.extend(check_example_phase_boundaries())
    findings.extend(check_accessibility_entry_paths())
    findings.extend(check_quick_start_technical_setup_paths())
    findings.extend(check_old_workflow_drift())
    findings.extend(check_art_bible_phase_drift())
    findings.extend(check_workflow_guide_phase_boundaries())
    findings.extend(check_validation_quantity_boundaries())
    findings.extend(check_gate_required_semantics())
    findings.extend(check_release_phase_contract())
    findings.extend(check_template_count_contract())

    errors = sum(1 for item in findings if item.severity == "ERROR")
    warnings = sum(1 for item in findings if item.severity == "WARN")
    for item in findings:
        print(f"{item.severity}: {item.message}")
    print(f"workflow-consistency summary: {errors} error(s), {warnings} warning(s)")
    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
