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
DOC_COMMAND_FILES = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "START-HERE.md",
    REPO_ROOT / ".claude" / "docs" / "quick-start.md",
]
DRIFT_SCAN_ROOTS = [
    REPO_ROOT / "README.md",
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
        if line == "**Required Artifacts:**":
            in_required = True
            continue
        if in_required and line.startswith("**") and line != "**Required Artifacts:**":
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

    if "/setup-engine" in concept:
        findings.append(
            Finding("ERROR", "docs/examples/skill-flow-diagrams.md places /setup-engine in Concept; it belongs in Technical Setup")
        )
    if "/test-setup" in pre_production:
        findings.append(
            Finding("ERROR", "docs/examples/skill-flow-diagrams.md places /test-setup in Pre-Production; it belongs in Technical Setup")
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
