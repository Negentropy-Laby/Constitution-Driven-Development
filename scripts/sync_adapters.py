#!/usr/bin/env python3
"""Generate Claude/Codex runtime adapters from canonical authority sources.

Canonical sources (skills/, agents/, hooks/, INSTRUCTIONS.md) are hand-authored.
Every runtime adapter tree (.claude/skills, .agents/skills, .claude/agents,
.codex/agents, .claude/hooks, .codex/hooks, CLAUDE.md, AGENTS.md) is generated
from those sources per cdd-manifest.toml and must never be hand-edited.

Design invariants (see docs/architecture/adr-0001-generated-runtime-adapters.md):
  * one canonical source per generated path; deterministic transform pipeline;
  * canonical sources never overlap a generated destination;
  * full preflight before any mutation; per-file atomic replacement;
  * freshness = exact UTF-8/LF bytes plus mode contract;
  * managed directory roots contain exactly the expected file set.

The module exposes a side-effect-free planning/checking API that
scripts/workflow_consistency.py imports directly. It never forges sys.argv.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import fnmatch
import hashlib
import json
import os
import re
import stat
import string
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "cdd-manifest.toml"

ALL_TOKEN = "all"  # CLI --class value meaning every declared source
BUILTIN_TRANSFORMS = {"agent_md_to_toml"}
MANIFEST_TRANSFORMS = {"runtime_substitute"}

# Agent frontmatter fields intentionally dropped by agent_md_to_toml (Codex's
# agent schema only carries name/description/developer_instructions).
DROP_AGENT_FIELDS = {
    "tools",
    "model",
    "maxTurns",
    "memory",
    "skills",
    "disallowedTools",
    "isolation",
}
RETAINED_AGENT_FIELDS = {"name", "description"}
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")

OK, STALE, MISSING, EXTRA, INVALID = "OK", "STALE", "MISSING", "EXTRA", "INVALID"
ERROR, WARN = "ERROR", "WARN"
IS_WINDOWS = os.name == "nt"
GENERATED_MODE = 0o644
FILE_ATTRIBUTE_REPARSE_POINT = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Drift:
    status: str
    path: str
    diff_preview: str = ""


@dataclass(frozen=True)
class Diagnostic:
    severity: str
    path: str
    message: str


@dataclass
class CheckReport:
    drifts: list[Drift] = field(default_factory=list)
    diagnostics: list[Diagnostic] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        if any(d.severity == ERROR for d in self.diagnostics):
            return False
        return all(d.status == OK for d in self.drifts)

    def counts(self) -> dict[str, int]:
        out = {OK: 0, STALE: 0, MISSING: 0, EXTRA: 0, INVALID: 0}
        for d in self.drifts:
            out[d.status] = out.get(d.status, 0) + 1
        return out


# ---------------------------------------------------------------------------
# Manifest model
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Runtime:
    name: str
    label: str


@dataclass(frozen=True)
class Source:
    name: str
    root: str | None
    include: str | None
    file: str | None
    expected_count: int
    targets: tuple[str, ...]


@dataclass(frozen=True)
class OutputSpec:
    source: str
    runtime: str
    transforms: tuple[str, ...]
    dest_root: str | None
    dest_pattern: str | None
    dest_file: str | None
    owns_tree: bool


@dataclass(frozen=True)
class Manifest:
    version: int
    runtimes: dict[str, Runtime]
    sources: dict[str, Source]
    outputs: tuple[OutputSpec, ...]
    replacements: tuple[tuple[str, str], ...]
    forbidden_literals: tuple[str, ...]


@dataclass(frozen=True)
class RenderedOutput:
    dest: str  # repo-relative POSIX destination
    expected: bytes  # exact UTF-8/LF
    owns_tree: bool


@dataclass(frozen=True)
class RenderContext:
    """Source identity used by transforms and destination expansion."""

    source_path: str
    relative: str
    name: str
    stem: str


@dataclass
class SyncPlan:
    manifest: Manifest
    repo_root: Path
    asset_class: str
    rendered: list[RenderedOutput] = field(default_factory=list)
    diagnostics: list[Diagnostic] = field(default_factory=list)
    # dest_root -> set of expected repo-relative dest paths (for owns_tree EXTRA scan)
    managed_roots: dict[str, set[str]] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------


def rel_posix(repo_root: Path, path: Path) -> str:
    try:
        return path.absolute().relative_to(repo_root.absolute()).as_posix()
    except ValueError:
        return path.as_posix()


def _validate_posix_rel(value: str, label: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a string")
    if value == "" or value == "." or value == "..":
        raise ValueError(f"{label} must be a non-empty relative POSIX path, got {value!r}")
    if "\x00" in value:
        raise ValueError(f"{label} must not contain NUL")
    if "\\" in value:
        raise ValueError(f"{label} must use POSIX slashes, got {value!r}")
    # A colon creates an alternate data stream on NTFS even when it is not a
    # drive prefix. Reject it so one manifest denotes the same file graph on
    # Windows, macOS, and Linux.
    if ":" in value:
        raise ValueError(f"{label} must not contain ':' path segments, got {value!r}")
    # This check is intentionally host-independent: PurePath/os.path on POSIX
    # do not consider a Windows drive or UNC path absolute.
    if value.startswith("/") or re.match(r"^[A-Za-z]:", value):
        raise ValueError(f"{label} must be relative, got {value!r}")
    parts = value.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise ValueError(f"{label} must not contain empty, '.' or '..' segments, got {value!r}")
    return value


def _validate_glob(value: str, label: str) -> str:
    """Validate a repository-relative glob without interpreting it."""

    value = _validate_posix_rel(value, label)
    if "{" in value or "}" in value:
        raise ValueError(f"{label} must not contain placeholders, got {value!r}")
    return value


def _validate_dest_pattern(value: str, label: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a string")
    formatter = string.Formatter()
    allowed = {"relative", "name", "stem"}
    try:
        parsed = list(formatter.parse(value))
    except ValueError as exc:
        raise ValueError(f"{label} has malformed placeholder syntax: {exc}") from exc
    fields: list[str] = []
    skeleton = ""
    for literal, field_name, format_spec, conversion in parsed:
        skeleton += literal
        if field_name is None:
            continue
        if field_name not in allowed:
            raise ValueError(f"{label} uses unknown placeholder {{{field_name}}}")
        if format_spec or conversion:
            raise ValueError(f"{label} placeholders may not use conversion or format specs")
        fields.append(field_name)
        skeleton += "placeholder"
    _validate_posix_rel(skeleton, label)
    return value


def _parts_overlap(left: str, right: str, *, casefold: bool = False) -> bool:
    if casefold:
        left, right = left.casefold(), right.casefold()
    return left == right or left.startswith(right + "/") or right.startswith(left + "/")


def _is_linklike_stat(st: os.stat_result) -> bool:
    return stat.S_ISLNK(st.st_mode) or bool(
        getattr(st, "st_file_attributes", 0) & FILE_ATTRIBUTE_REPARSE_POINT
    )


def _lstat_or_none(path: Path) -> os.stat_result | None:
    try:
        return path.lstat()
    except FileNotFoundError:
        return None


def _validate_existing_chain(repo_root: Path, path: Path, *, final_kind: str | None = None) -> None:
    """Reject links/reparse points and impossible existing path components.

    ``final_kind`` is ``"file"`` or ``"dir"`` when an existing final path
    must have that type. Missing final paths are allowed for destinations.
    """

    root = repo_root.absolute()
    candidate = path.absolute()
    try:
        relative = candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes repository root: {path}") from exc

    current = root
    for index, part in enumerate(relative.parts):
        current /= part
        st = _lstat_or_none(current)
        if st is None:
            # Once one component is absent, all descendants are absent too.
            return
        if _is_linklike_stat(st):
            raise ValueError(f"path component is a symlink/reparse point: {rel_posix(root, current)}")
        is_final = index == len(relative.parts) - 1
        if not is_final and not stat.S_ISDIR(st.st_mode):
            raise ValueError(f"path parent is not a directory: {rel_posix(root, current)}")
        if is_final and final_kind == "file" and not stat.S_ISREG(st.st_mode):
            raise ValueError(f"expected a regular file: {rel_posix(root, current)}")
        if is_final and final_kind == "dir" and not stat.S_ISDIR(st.st_mode):
            raise ValueError(f"expected a directory: {rel_posix(root, current)}")


# ---------------------------------------------------------------------------
# Manifest loading + strict validation
# ---------------------------------------------------------------------------


def load_manifest(path: Path) -> Manifest:
    """Load and strictly validate a version-2 adapter manifest."""

    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("manifest must not contain a UTF-8 BOM")
    text = raw.decode("utf-8")
    if "\r" in text:
        raise ValueError("manifest must use physical LF line endings")
    data = tomllib.loads(text)
    return _coerce_manifest(data)


def _coerce_manifest(data: dict) -> Manifest:
    if not isinstance(data, dict):
        raise ValueError("manifest root must be a table")
    known_top = {"version", "runtimes", "sources", "transforms", "outputs"}
    unknown_top = set(data) - known_top
    if unknown_top:
        raise ValueError(f"unknown manifest keys: {sorted(unknown_top)}")
    version = data.get("version")
    if type(version) is not int or version != 2:
        if type(version) is int and version == 1:
            raise ValueError(
                "manifest version 1 is unsupported; see UPGRADING.md \"Manifest v2\": "
                "add [runtimes.*] sections and a 'targets' list per source, then set version = 2"
            )
        raise ValueError(f"unsupported manifest version: {version!r} (expected 2)")

    runtimes = _coerce_runtimes(data.get("runtimes", {}))

    sources_raw = data.get("sources", {})
    if not isinstance(sources_raw, dict) or not sources_raw:
        raise ValueError("manifest must declare at least one source")
    sources: dict[str, Source] = {}
    for name, body in sources_raw.items():
        sources[name] = _coerce_source(name, body, runtimes)

    transforms_raw = data.get("transforms", {})
    replacements, forbidden = _coerce_transforms(transforms_raw)

    outputs_raw = data.get("outputs", [])
    if not isinstance(outputs_raw, list) or not outputs_raw:
        raise ValueError("manifest must declare at least one output")
    outputs = tuple(_coerce_output(o, sources, runtimes) for o in outputs_raw)

    _validate_output_topology(sources, outputs)
    return Manifest(
        version=2,
        runtimes=runtimes,
        sources=sources,
        outputs=outputs,
        replacements=replacements,
        forbidden_literals=forbidden,
    )


def _coerce_runtimes(raw: dict) -> dict[str, Runtime]:
    if not isinstance(raw, dict) or not raw:
        raise ValueError("manifest must declare at least one [runtimes.*] table")
    runtimes: dict[str, Runtime] = {}
    seen_casefold: set[str] = set()
    for name, body in raw.items():
        if not isinstance(name, str) or not NAME_RE.match(name):
            raise ValueError(f"runtime id {name!r} must match {NAME_RE.pattern!r}")
        if name.casefold() in seen_casefold:
            raise ValueError(f"runtime id {name!r} collides case-insensitively with another runtime")
        seen_casefold.add(name.casefold())
        if not isinstance(body, dict):
            raise ValueError(f"runtime {name!r} must be a table")
        bad = set(body) - {"label"}
        if bad:
            raise ValueError(f"runtime {name!r} has unknown keys: {sorted(bad)}")
        label = body.get("label")
        if not isinstance(label, str) or not label:
            raise ValueError(f"runtime {name!r} label must be a non-empty string")
        runtimes[name] = Runtime(name=name, label=label)
    return runtimes


def _coerce_source(name: str, body: dict, runtimes: dict[str, Runtime]) -> Source:
    if not isinstance(name, str) or not NAME_RE.match(name):
        raise ValueError(f"source id {name!r} must match {NAME_RE.pattern!r}")
    if name == ALL_TOKEN:
        raise ValueError(f"source id {name!r} is reserved for the CLI --class selector")
    if not isinstance(body, dict):
        raise ValueError(f"source {name!r} must be a table")
    known = {"root", "include", "file", "expected_count", "targets"}
    unknown = set(body) - known
    if unknown:
        raise ValueError(f"source {name!r} has unknown keys: {sorted(unknown)}")
    root = body.get("root")
    include = body.get("include")
    file = body.get("file")
    expected = body.get("expected_count")
    if isinstance(expected, bool) or not isinstance(expected, int) or expected <= 0:
        raise ValueError(f"source {name!r} expected_count must be a positive int")
    if file is not None and (root is not None or include is not None):
        raise ValueError(f"source {name!r}: use either 'file' or 'root'+'include', not both")
    if file is None and (root is None or include is None):
        raise ValueError(f"source {name!r}: must declare 'file' or both 'root' and 'include'")
    if root is not None:
        _validate_posix_rel(root, f"source {name!r} root")
        _validate_glob(include, f"source {name!r} include")
    if file is not None:
        _validate_posix_rel(file, f"source {name!r} file")
        if expected != 1:
            raise ValueError(f"single-file source {name!r} expected_count must equal 1")
    targets = _coerce_targets(body.get("targets"), runtimes, name)
    return Source(name=name, root=root, include=include, file=file, expected_count=expected, targets=targets)


def _coerce_targets(raw, runtimes: dict[str, Runtime], source_name: str) -> tuple[str, ...]:
    if raw is None:
        return tuple(runtimes)  # default: every declared runtime
    if not isinstance(raw, list) or not raw or not all(isinstance(t, str) for t in raw):
        raise ValueError(f"source {source_name!r} targets must be a non-empty list of strings")
    seen: set[str] = set()
    for target in raw:
        if target not in runtimes:
            raise ValueError(f"source {source_name!r} target {target!r} is not a declared runtime")
        if target in seen:
            raise ValueError(f"source {source_name!r} target {target!r} is duplicated")
        seen.add(target)
    return tuple(raw)


def _coerce_transforms(transforms_raw: dict) -> tuple[tuple[tuple[str, str], ...], tuple[str, ...]]:
    if not isinstance(transforms_raw, dict):
        raise ValueError("transforms must be a table")
    unknown = set(transforms_raw) - MANIFEST_TRANSFORMS
    if unknown:
        raise ValueError(f"unknown transform names: {sorted(unknown)}")
    sub = transforms_raw.get("runtime_substitute")
    if sub is None:
        return tuple(), tuple()
    if not isinstance(sub, dict):
        raise ValueError("transforms.runtime_substitute must be a table")
    known = {"replacements", "forbidden_literals"}
    bad = set(sub) - known
    if bad:
        raise ValueError(f"runtime_substitute has unknown keys: {sorted(bad)}")
    reps_raw = sub.get("replacements", [])
    if not isinstance(reps_raw, list):
        raise ValueError("runtime_substitute.replacements must be a list of [find, replace] pairs")
    reps: list[tuple[str, str]] = []
    for pair in reps_raw:
        if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(x, str) for x in pair):
            raise ValueError("each replacement must be a [find, replace] string pair")
        if pair[0] == "":
            raise ValueError("replacement find literal must not be empty")
        reps.append((pair[0], pair[1]))
    forb_raw = sub.get("forbidden_literals", [])
    if not isinstance(forb_raw, list) or not all(isinstance(x, str) for x in forb_raw):
        raise ValueError("runtime_substitute.forbidden_literals must be a list of strings")
    if any(x == "" for x in forb_raw):
        raise ValueError("forbidden literals must not be empty")
    return tuple(reps), tuple(forb_raw)


def _coerce_output(body: dict, sources: dict[str, Source], runtimes: dict[str, Runtime]) -> OutputSpec:
    if not isinstance(body, dict):
        raise ValueError("each output must be a table")
    known = {"source", "runtime", "transforms", "dest_root", "dest_pattern", "dest_file", "owns_tree"}
    unknown = set(body) - known
    if unknown:
        raise ValueError(f"output has unknown keys: {sorted(unknown)}")
    source = body.get("source")
    runtime = body.get("runtime")
    if not isinstance(source, str):
        raise ValueError("output source must be a string")
    if not isinstance(runtime, str):
        raise ValueError("output runtime must be a string")
    if source not in sources:
        raise ValueError(f"output references unknown source {source!r}")
    if runtime not in runtimes:
        raise ValueError(f"output runtime must be a declared runtime, got {runtime!r}")
    if runtime not in sources[source].targets:
        raise ValueError(f"output runtime {runtime!r} is not targeted by source {source!r}")
    transforms = body.get("transforms", [])
    if not isinstance(transforms, list) or not all(isinstance(t, str) for t in transforms):
        raise ValueError("output transforms must be a list of strings")
    for t in transforms:
        if t not in MANIFEST_TRANSFORMS and t not in BUILTIN_TRANSFORMS:
            raise ValueError(f"output references unknown transform {t!r}")

    dest_root = body.get("dest_root")
    dest_pattern = body.get("dest_pattern")
    dest_file = body.get("dest_file")
    if "owns_tree" not in body or not isinstance(body["owns_tree"], bool):
        raise ValueError("output owns_tree must be a bool")
    owns_tree = body["owns_tree"]

    has_tree = dest_root is not None
    has_file = dest_file is not None
    if has_tree == has_file:
        raise ValueError("output must declare exactly one of dest_root (+dest_pattern) or dest_file")
    if has_tree:
        if dest_pattern is None:
            raise ValueError("output with dest_root must declare dest_pattern")
        if not owns_tree:
            raise ValueError("output with dest_root must set owns_tree = true")
        _validate_posix_rel(dest_root, "output dest_root")
        _validate_dest_pattern(dest_pattern, "output dest_pattern")
    if has_file:
        if owns_tree:
            raise ValueError("output with dest_file must set owns_tree = false")
        if dest_pattern is not None:
            raise ValueError("output with dest_file must not declare dest_pattern")
        _validate_posix_rel(dest_file, "output dest_file")
    return OutputSpec(
        source=source,
        runtime=runtime,
        transforms=tuple(transforms),
        dest_root=dest_root,
        dest_pattern=dest_pattern,
        dest_file=dest_file,
        owns_tree=owns_tree,
    )


def _validate_output_topology(sources: dict[str, Source], outputs: tuple[OutputSpec, ...]) -> None:
    expected_pairs = {(name, target) for name, src in sources.items() for target in src.targets}
    actual_pairs = [(o.source, o.runtime) for o in outputs]
    if len(actual_pairs) != len(expected_pairs) or set(actual_pairs) != expected_pairs:
        missing = sorted(expected_pairs - set(actual_pairs))
        duplicates = sorted({pair for pair in actual_pairs if actual_pairs.count(pair) > 1})
        extra = sorted(set(actual_pairs) - expected_pairs)
        raise ValueError(
            "manifest outputs must cover each declared source target exactly once; "
            f"missing={missing}, duplicates={duplicates}, extra={extra}"
        )

    seen_exact: dict[str, str] = {}
    seen_casefold: dict[str, str] = {}
    roots: list[tuple[str, str]] = []  # (root, owner_label)
    files: list[str] = []
    for o in outputs:
        owner = f"{o.source}/{o.runtime}"
        if o.dest_file:
            files.append(o.dest_file)
            _claim(seen_exact, o.dest_file, owner)
            _claim(seen_casefold, o.dest_file.casefold(), owner)
        else:
            assert o.dest_root is not None
            roots.append((o.dest_root, owner))
            _claim(seen_exact, o.dest_root, owner)
            _claim(seen_casefold, o.dest_root.casefold(), owner)
    # No root/file may be an exact, ancestor, descendant, or case-insensitive
    # collision with another destination.
    for i, (r_i, _) in enumerate(roots):
        for r_j, _ in roots[i + 1 :]:
            if _parts_overlap(r_i, r_j) or _parts_overlap(r_i, r_j, casefold=True):
                raise ValueError(f"managed roots overlap: {r_i!r} and {r_j!r}")
    for i, f in enumerate(files):
        for other in files[i + 1 :]:
            if _parts_overlap(f, other) or _parts_overlap(f, other, casefold=True):
                raise ValueError(f"destination files collide: {f!r} and {other!r}")
        for r, _ in roots:
            if _parts_overlap(f, r) or _parts_overlap(f, r, casefold=True):
                raise ValueError(f"dest_file {f!r} collides with managed root {r!r}")

    source_paths: list[tuple[str, str]] = []
    for source in sources.values():
        source_path = source.file if source.file is not None else source.root
        assert source_path is not None
        source_paths.append((source_path, source.name))
    for i, (left, left_name) in enumerate(source_paths):
        for right, right_name in source_paths[i + 1 :]:
            if _parts_overlap(left, right) or _parts_overlap(left, right, casefold=True):
                raise ValueError(
                    f"canonical sources overlap: {left_name}={left!r} and {right_name}={right!r}"
                )
        for dest in files + [root for root, _ in roots]:
            if _parts_overlap(left, dest) or _parts_overlap(left, dest, casefold=True):
                raise ValueError(
                    f"canonical source {left_name}={left!r} overlaps generated destination {dest!r}"
                )


def _claim(seen: dict[str, str], key: str, owner: str) -> None:
    if key in seen:
        raise ValueError(f"output destination {key!r} declared twice ({seen[key]} and {owner})")
    seen[key] = owner


# ---------------------------------------------------------------------------
# Canonical source reading (strict UTF-8 / LF)
# ---------------------------------------------------------------------------


def _read_canonical(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("BOM is not allowed in a canonical source")
    text = raw.decode("utf-8")  # strict: raises UnicodeDecodeError on bad bytes
    if "\r" in text:
        raise ValueError("CR/CRLF is not allowed in a canonical source; expected physical LF")
    return text


# ---------------------------------------------------------------------------
# Transforms
# ---------------------------------------------------------------------------


# Adjacent-token collapse detection. runtime_substitute is a blind sequential
# replace, so two distinct source tokens can collapse into one (e.g.
# "CLAUDE.md and AGENTS.md" -> the AGENTS.md token repeated). The forbidden-literal
# sweep cannot see that (no Claude token survives). A collapse can only duplicate
# a substitution *target* token (two sources mapping to one output), so we compare
# source and rendered lines and flag only a newly introduced target duplication.
# This preserves pre-existing target prose while still catching source vocabulary
# that collapses after replacement. Markdown inline-code delimiters and balanced
# per-token parentheses are ignored for comparison.
_ADJACENT_DUPLICATE = re.compile(
    r"(?<!\S)\(?(?P<token>[^\s,()]+)\)?\s*"
    r"(?:and|or|,(?:\s+(?:and|or))?)\s*\(?(?P=token)\)?(?=$|[\s.,;:])"
)


def _adjacent_target_duplicates(line: str, targets: tuple[str, ...]) -> Counter[str]:
    """Count adjacent duplicate tokens containing a replacement target."""
    duplicates: Counter[str] = Counter()
    if not targets:
        return duplicates
    view = line.replace("`", "")
    for match in _ADJACENT_DUPLICATE.finditer(view):
        token = match.group("token")
        if any(target and target in token for target in targets):
            duplicates[token] += 1
    return duplicates


def _detect_adjacent_collapse(
    source_line: str,
    rendered_line: str,
    targets: tuple[str, ...],
) -> str | None:
    """Return a diagnostic when substitution creates a new target duplication."""
    before = _adjacent_target_duplicates(source_line, targets)
    after = _adjacent_target_duplicates(rendered_line, targets)
    for token, count in after.items():
        if count > before[token]:
            return f"duplicate adjacent token {token!r}"
    return None


def _runtime_substitute(text: str, replacements: tuple[tuple[str, str], ...], forbidden: tuple[str, ...]) -> str:
    targets = tuple(dict.fromkeys(replace for _, replace in replacements))
    source_lines = text.split("\n")
    for find, replace in replacements:
        text = text.replace(find, replace)
    # Scan per line for accurate line numbers in diagnostics.
    for lineno, line in enumerate(text.split("\n"), start=1):
        for lit in forbidden:
            if lit in line:
                raise SubstitutionError(
                    f"forbidden residual literal {lit!r} after substitution (line {lineno})"
                )
        source_line = source_lines[lineno - 1] if lineno <= len(source_lines) else ""
        collapse = _detect_adjacent_collapse(source_line, line, targets)
        if collapse is not None:
            raise SubstitutionError(
                f"semantic collapse after substitution: {collapse} (line {lineno})"
            )
    return text


class SubstitutionError(ValueError):
    """Raised when runtime substitution violates an output integrity guard."""


def _agent_md_to_toml(text: str, context: RenderContext) -> str:
    fields, body = _split_frontmatter_strict(text)
    allowed = RETAINED_AGENT_FIELDS | DROP_AGENT_FIELDS
    unknown = set(fields) - allowed
    if unknown:
        raise ValueError(f"unknown agent frontmatter field(s): {sorted(unknown)}")
    name = _decode_name(fields)
    if name != context.stem:
        raise ValueError(
            f"agent frontmatter name {name!r} must match source filename stem {context.stem!r}"
        )
    description = _decode_description(fields)
    body_value = _extract_body(body)
    toml = _serialize_agent_toml(name, description, body_value)
    # Semantic round-trip: the rendered file must parse back to the same values.
    parsed = tomllib.loads(toml)
    if (
        parsed.get("name") != name
        or parsed.get("description") != description
        or parsed.get("developer_instructions") != body_value
    ):
        raise ValueError("agent_md_to_toml round-trip mismatch")
    return toml


def _split_frontmatter_strict(text: str) -> tuple[dict[str, str], str]:
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        raise ValueError("agent source must start with a '---' frontmatter fence")
    close_index = None
    for idx in range(1, len(lines)):
        if lines[idx] == "---":
            close_index = idx
            break
    if close_index is None:
        raise ValueError("agent source frontmatter is not closed with a '---' fence")
    fm_lines = lines[1:close_index]
    fields: dict[str, str] = {}
    for fm in fm_lines:
        if fm.strip() == "" or fm.lstrip().startswith("#"):
            continue
        if ":" not in fm:
            raise ValueError(f"unparseable frontmatter line: {fm!r}")
        key, value = fm.split(":", 1)
        key = key.strip()
        if key in fields:
            raise ValueError(f"duplicate frontmatter field: {key!r}")
        fields[key] = value  # keep raw (with leading space) for decoder
    body = "\n".join(lines[close_index + 1 :])
    return fields, body


def _decode_name(fields: dict[str, str]) -> str:
    if "name" not in fields:
        raise ValueError("agent frontmatter missing 'name'")
    raw = fields["name"].strip()
    # Bare scalar only: reject surrounding quotes.
    if len(raw) >= 2 and raw[0] in "'\"" and raw[-1] == raw[0]:
        raise ValueError("agent 'name' must be a bare scalar, not quoted")
    if not NAME_RE.match(raw):
        raise ValueError(f"agent 'name' {raw!r} does not match required pattern")
    return raw


def _decode_description(fields: dict[str, str]) -> str:
    if "description" not in fields:
        raise ValueError("agent frontmatter missing 'description'")
    raw = fields["description"].strip()
    if len(raw) < 2 or raw[0] != '"' or raw[-1] != '"':
        raise ValueError("agent 'description' must be a single-line double-quoted scalar")
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"agent 'description' is not a valid JSON string: {exc}") from exc
    if not isinstance(decoded, str):
        raise ValueError("agent 'description' must decode to a string")
    if decoded == "":
        raise ValueError("agent 'description' must not be empty")
    if "\n" in decoded or "\r" in decoded:
        raise ValueError("agent 'description' must be single-line")
    return decoded


def _extract_body(body: str) -> str:
    # Remove at most one optional structural leading LF (blank line after fence).
    if body.startswith("\n"):
        body = body[1:]
    # Require and remove exactly one file-terminating LF.
    if not body.endswith("\n"):
        raise ValueError("agent source body must end with exactly one LF")
    body = body[:-1]
    if body.endswith("\r"):
        raise ValueError("agent source body contains a stray CR")
    return body


def _serialize_agent_toml(name: str, description: str, body: str) -> str:
    return (
        f'name = {_encode_toml_basic(name)}\n'
        f'description = {_encode_toml_basic(description)}\n'
        f'developer_instructions = """\n{_encode_toml_multiline(body)}"""\n'
    )


def _encode_toml_basic(value: str) -> str:
    # json.dumps produces a valid TOML basic string literal (same escape set).
    return json.dumps(value, ensure_ascii=False)


def _encode_toml_multiline(value: str) -> str:
    # Multiline basic string: preserve physical LF, escape backslashes/control
    # characters, then neutralize any run of 3+ quotes so it cannot close the
    # delimiter. The common corpus remains byte-identical to the original
    # serializer; the extra escapes only affect otherwise-invalid TOML input.
    chunks: list[str] = []
    for char in value:
        codepoint = ord(char)
        if char == "\\":
            chunks.append("\\\\")
        elif char == "\n":
            chunks.append("\n")
        elif char == "\b":
            chunks.append("\\b")
        elif char == "\t":
            chunks.append("\\t")
        elif char == "\f":
            chunks.append("\\f")
        elif codepoint < 0x20 or codepoint == 0x7F:
            chunks.append(f"\\u{codepoint:04X}")
        else:
            chunks.append(char)
    encoded = "".join(chunks)
    encoded = re.sub(r'"{3,}', lambda m: "".join('\\"' for _ in m.group(0)), encoded)
    return encoded


def _render(
    text: str,
    transforms: tuple[str, ...],
    manifest: Manifest,
    context: RenderContext,
) -> str:
    for transform in transforms:
        if transform == "runtime_substitute":
            text = _runtime_substitute(text, manifest.replacements, manifest.forbidden_literals)
        elif transform == "agent_md_to_toml":
            text = _agent_md_to_toml(text, context)
        else:  # pragma: no cover - validated at load
            raise ValueError(f"unknown transform {transform!r}")
    return text


# ---------------------------------------------------------------------------
# Plan building (preflight + in-memory render)
# ---------------------------------------------------------------------------


def build_sync_plan(manifest: Manifest, repo_root: Path, asset_class: str = "all") -> SyncPlan:
    """Render a complete, non-mutating sync plan after source/destination preflight."""

    valid_classes = set(manifest.sources) | {ALL_TOKEN}
    if asset_class not in valid_classes:
        raise ValueError(f"asset_class must be one of {sorted(valid_classes)}, got {asset_class!r}")
    plan = SyncPlan(manifest=manifest, repo_root=repo_root, asset_class=asset_class)

    outputs = [
        o for o in manifest.outputs
        if asset_class == "all" or o.source == asset_class
    ]

    # Preflight: sources must exist, contain no links/special files, match the
    # manifest count, and be readable. Discovery never follows a link.
    source_files: dict[str, list[Path]] = {}
    for src_name in sorted({o.source for o in outputs}):
        src = manifest.sources[src_name]
        files = _discover_source(repo_root, src, plan.diagnostics)
        source_files[src_name] = files

    if any(d.severity == ERROR for d in plan.diagnostics):
        return plan

    # Render every expected output in memory before any caller writes.
    for output in outputs:
        _render_output(plan, repo_root, output, source_files[output.source])
    _validate_rendered_graph(plan)
    _validate_destination_preflight(plan)
    return plan


def _discover_source(repo_root: Path, src: Source, diagnostics: list[Diagnostic]) -> list[Path]:
    if src.file is not None:
        path = repo_root / src.file
        label = rel_posix(repo_root, path)
        try:
            st = _lstat_or_none(path)
            if st is None:
                diagnostics.append(Diagnostic(ERROR, label, "canonical source file missing"))
                return []
            _validate_existing_chain(repo_root, path, final_kind="file")
        except (OSError, ValueError) as exc:
            diagnostics.append(Diagnostic(ERROR, label, f"invalid canonical source path: {exc}"))
            return []
        files = [path]
    else:
        assert src.root is not None and src.include is not None
        root = repo_root / src.root
        label_root = rel_posix(repo_root, root)
        try:
            st = _lstat_or_none(root)
            if st is None:
                diagnostics.append(Diagnostic(ERROR, label_root, "canonical source root missing"))
                return []
            _validate_existing_chain(repo_root, root, final_kind="dir")
        except (OSError, ValueError) as exc:
            diagnostics.append(Diagnostic(ERROR, label_root, f"invalid canonical source root: {exc}"))
            return []
        if src.name == "skills":
            files = _discover_skill_packages(repo_root, root, src.include, diagnostics)
        else:
            files = _discover_glob_no_links(repo_root, root, src.include, diagnostics)
    if len(files) != src.expected_count:
        diagnostics.append(
            Diagnostic(
                ERROR,
                label_root if src.file is None else label,
                f"expected {src.expected_count} source file(s), found {len(files)}; "
                "update expected_count in cdd-manifest.toml (and catalogs/docs) to change the asset set",
            )
        )
    return files


def _glob_matches(relative: str, pattern: str) -> bool:
    path_parts = tuple(relative.split("/"))
    pattern_parts = tuple(pattern.split("/"))

    def match(path_index: int, pattern_index: int) -> bool:
        if pattern_index == len(pattern_parts):
            return path_index == len(path_parts)
        token = pattern_parts[pattern_index]
        if token == "**":
            return match(path_index, pattern_index + 1) or (
                path_index < len(path_parts) and match(path_index + 1, pattern_index)
            )
        return (
            path_index < len(path_parts)
            and fnmatch.fnmatchcase(path_parts[path_index], token)
            and match(path_index + 1, pattern_index + 1)
        )

    return match(0, 0)


def _scandir_sorted(path: Path) -> list[os.DirEntry[str]]:
    with os.scandir(path) as entries:
        return sorted(entries, key=lambda entry: entry.name)


def _discover_glob_no_links(
    repo_root: Path,
    root: Path,
    include: str,
    diagnostics: list[Diagnostic],
) -> list[Path]:
    matches: list[Path] = []

    def visit(directory: Path, relative_dir: str = "") -> None:
        try:
            entries = _scandir_sorted(directory)
        except OSError as exc:
            diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, directory), f"cannot scan canonical source: {exc}")
            )
            return
        for entry in entries:
            path = Path(entry.path)
            relative = f"{relative_dir}/{entry.name}" if relative_dir else entry.name
            try:
                st = entry.stat(follow_symlinks=False)
            except OSError as exc:
                diagnostics.append(
                    Diagnostic(ERROR, rel_posix(repo_root, path), f"cannot inspect canonical source: {exc}")
                )
                continue
            if _is_linklike_stat(st):
                diagnostics.append(
                    Diagnostic(ERROR, rel_posix(repo_root, path), "canonical source contains a symlink/reparse point")
                )
            elif stat.S_ISDIR(st.st_mode):
                visit(path, relative)
            elif stat.S_ISREG(st.st_mode):
                if _glob_matches(relative, include):
                    matches.append(path)
            else:
                diagnostics.append(
                    Diagnostic(ERROR, rel_posix(repo_root, path), "canonical source contains a special file")
                )

    visit(root)
    return sorted(matches, key=lambda path: rel_posix(repo_root, path))


def _discover_skill_packages(
    repo_root: Path,
    root: Path,
    include: str,
    diagnostics: list[Diagnostic],
) -> list[Path]:
    files: list[Path] = []
    try:
        packages = _scandir_sorted(root)
    except OSError as exc:
        diagnostics.append(Diagnostic(ERROR, rel_posix(repo_root, root), f"cannot scan skills root: {exc}"))
        return files

    for package_entry in packages:
        package = Path(package_entry.path)
        try:
            package_stat = package_entry.stat(follow_symlinks=False)
        except OSError as exc:
            diagnostics.append(Diagnostic(ERROR, rel_posix(repo_root, package), f"cannot inspect skill package: {exc}"))
            continue
        if _is_linklike_stat(package_stat):
            diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, package), "skill package is a symlink/reparse point")
            )
            continue
        if not stat.S_ISDIR(package_stat.st_mode):
            diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, package), "skills root may contain only package directories")
            )
            continue
        try:
            children = _scandir_sorted(package)
        except OSError as exc:
            diagnostics.append(Diagnostic(ERROR, rel_posix(repo_root, package), f"cannot scan skill package: {exc}"))
            continue
        found_skill = False
        for child_entry in children:
            child = Path(child_entry.path)
            try:
                child_stat = child_entry.stat(follow_symlinks=False)
            except OSError as exc:
                diagnostics.append(Diagnostic(ERROR, rel_posix(repo_root, child), f"cannot inspect skill asset: {exc}"))
                continue
            if _is_linklike_stat(child_stat):
                diagnostics.append(
                    Diagnostic(ERROR, rel_posix(repo_root, child), "skill package contains a symlink/reparse point")
                )
                continue
            if child_entry.name != "SKILL.md" or not stat.S_ISREG(child_stat.st_mode):
                diagnostics.append(
                    Diagnostic(
                        ERROR,
                        rel_posix(repo_root, child),
                        f"skill package {package.name!r} may contain only a regular SKILL.md",
                    )
                )
                continue
            found_skill = True
            relative = f"{package.name}/SKILL.md"
            if _glob_matches(relative, include):
                files.append(child)
        if not found_skill:
            diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, package), f"skill package {package.name!r} is missing SKILL.md")
            )
    return sorted(files, key=lambda path: rel_posix(repo_root, path))


def _render_output(plan: SyncPlan, repo_root: Path, output: OutputSpec, source_files: list[Path]) -> None:
    for src_path in source_files:
        context = _render_context(repo_root, output, src_path, plan.manifest)
        try:
            text = _read_canonical(src_path)
        except (OSError, ValueError, UnicodeDecodeError) as exc:
            plan.diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, src_path), f"invalid canonical source: {exc}")
            )
            continue
        try:
            rendered = _render(text, output.transforms, plan.manifest, context)
            if rendered.startswith("\ufeff"):
                raise ValueError("rendered output must not start with a UTF-8 BOM")
            if "\r" in rendered:
                raise ValueError("rendered output must use physical LF and contain no CR")
            rendered_bytes = rendered.encode("utf-8")
        except (ValueError, SubstitutionError) as exc:
            plan.diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, src_path), f"transform failed: {exc}")
            )
            continue
        try:
            dest_rel = _dest_rel(output, context)
        except ValueError as exc:
            plan.diagnostics.append(
                Diagnostic(ERROR, rel_posix(repo_root, src_path), f"invalid destination expansion: {exc}")
            )
            continue
        plan.rendered.append(
            RenderedOutput(dest=dest_rel, expected=rendered_bytes, owns_tree=output.owns_tree)
        )
        if output.owns_tree:
            assert output.dest_root is not None
            plan.managed_roots.setdefault(output.dest_root, set()).add(dest_rel)


def _render_context(
    repo_root: Path,
    output: OutputSpec,
    src_path: Path,
    manifest: Manifest,
) -> RenderContext:
    src = manifest.sources[output.source]
    if src.file is not None:
        relative = src.file
        name = Path(src.file).name
        stem = Path(src.file).stem
    else:
        assert src.root is not None
        relative = src_path.relative_to(repo_root / src.root).as_posix()
        name = src_path.name
        stem = src_path.stem
    return RenderContext(
        source_path=rel_posix(repo_root, src_path),
        relative=relative,
        name=name,
        stem=stem,
    )


def _dest_rel(output: OutputSpec, context: RenderContext) -> str:
    if output.dest_file is not None:
        return _validate_posix_rel(output.dest_file, "expanded destination")
    assert output.dest_root is not None and output.dest_pattern is not None
    expanded = output.dest_pattern.format(
        relative=context.relative,
        name=context.name,
        stem=context.stem,
    )
    _validate_posix_rel(expanded, "expanded destination pattern")
    return _validate_posix_rel(f"{output.dest_root}/{expanded}", "expanded destination")


def _validate_rendered_graph(plan: SyncPlan) -> None:
    rendered = sorted(plan.rendered, key=lambda item: item.dest)
    for index, current in enumerate(rendered):
        for other in rendered[index + 1 :]:
            if _parts_overlap(current.dest, other.dest) or _parts_overlap(
                current.dest, other.dest, casefold=True
            ):
                plan.diagnostics.append(
                    Diagnostic(
                        ERROR,
                        current.dest,
                        f"rendered destination collides with {other.dest!r}",
                    )
                )


def _validate_destination_preflight(plan: SyncPlan) -> None:
    for dest_root in sorted(plan.managed_roots):
        path = plan.repo_root / dest_root
        try:
            _validate_existing_chain(plan.repo_root, path, final_kind="dir")
        except (OSError, ValueError) as exc:
            plan.diagnostics.append(Diagnostic(ERROR, dest_root, f"invalid managed root: {exc}"))

    for rendered in sorted(plan.rendered, key=lambda item: item.dest):
        path = plan.repo_root / rendered.dest
        try:
            _validate_existing_chain(plan.repo_root, path)
            st = _lstat_or_none(path)
            if st is not None and not stat.S_ISREG(st.st_mode):
                raise ValueError("destination exists but is not a regular file")
            if st is not None and st.st_nlink != 1:
                raise ValueError("destination is a hardlink; expected link count 1")
        except (OSError, ValueError) as exc:
            plan.diagnostics.append(Diagnostic(ERROR, rendered.dest, f"invalid destination: {exc}"))


# ---------------------------------------------------------------------------
# Freshness check (read-only)
# ---------------------------------------------------------------------------


def check_plan(plan: SyncPlan) -> CheckReport:
    """Compare a preflighted plan with disk without modifying repository state."""

    report = CheckReport(diagnostics=list(plan.diagnostics))
    if any(d.severity == ERROR for d in plan.diagnostics):
        # A failed preflight blocks freshness analysis and is visible in both
        # diagnostics and the machine-countable INVALID bucket.
        for path in sorted({d.path for d in plan.diagnostics if d.severity == ERROR}):
            report.drifts.append(Drift(INVALID, path, "preflight failed"))
        return report

    for r in sorted(plan.rendered, key=lambda x: x.dest):
        drift, diagnostic = _check_one(plan.repo_root, r)
        report.drifts.append(drift)
        if diagnostic is not None:
            report.diagnostics.append(diagnostic)

    for dest_root, expected_paths in plan.managed_roots.items():
        report.drifts.extend(
            _scan_extras(plan.repo_root, dest_root, expected_paths, report.diagnostics)
        )
    # A race or I/O failure can cause the same invalid path to be found by the
    # per-file check and the managed-tree scan. Report it once deterministically.
    unique: dict[tuple[str, str], Drift] = {}
    for drift in report.drifts:
        unique.setdefault((drift.status, drift.path), drift)
    report.drifts = sorted(unique.values(), key=lambda drift: (drift.path, drift.status))
    return report


def _check_one(repo_root: Path, r: RenderedOutput) -> tuple[Drift, Diagnostic | None]:
    dest = repo_root / r.dest
    try:
        _validate_existing_chain(repo_root, dest)
        st = _lstat_or_none(dest)
    except (OSError, ValueError) as exc:
        return Drift(INVALID, r.dest, str(exc)), None
    if st is None:
        return Drift(MISSING, r.dest), None
    if not stat.S_ISREG(st.st_mode):
        return Drift(INVALID, r.dest, "generated destination is not a regular file"), None
    if st.st_nlink != 1:
        return Drift(INVALID, r.dest, "generated destination is a hardlink"), None
    try:
        on_disk = dest.read_bytes()
    except OSError as exc:
        return (
            Drift(INVALID, r.dest, "cannot read generated output"),
            Diagnostic(ERROR, r.dest, f"cannot read generated output: {exc}"),
        )
    if on_disk != r.expected:
        if on_disk.startswith(b"\xef\xbb\xbf"):
            preview = "generated output has a UTF-8 BOM"
        else:
            try:
                actual_text = on_disk.decode("utf-8")
            except UnicodeDecodeError as exc:
                preview = f"generated output is not valid UTF-8: {exc}"
            else:
                if "\r" in actual_text:
                    preview = "generated output contains CR/CRLF; expected physical LF\n"
                    diff_lines = 19
                else:
                    preview = ""
                    diff_lines = 20
                preview += _diff_preview(
                    r.expected.decode("utf-8"),
                    actual_text,
                    max_lines=diff_lines,
                )
                preview = preview.rstrip("\n")
        return Drift(STALE, r.dest, preview), None
    if not IS_WINDOWS:
        mode = stat.S_IMODE(st.st_mode)
        if mode != GENERATED_MODE:
            return Drift(STALE, r.dest, f"generated output mode is {mode:04o}; expected 0644"), None
    return Drift(OK, r.dest), None


def _scan_extras(
    repo_root: Path,
    dest_root: str,
    expected_paths: set[str],
    diagnostics: list[Diagnostic],
) -> list[Drift]:
    root = repo_root / dest_root
    drifts: list[Drift] = []
    try:
        st = _lstat_or_none(root)
        if st is None:
            return drifts  # MISSING per-output entries already reported
        _validate_existing_chain(repo_root, root, final_kind="dir")
    except (OSError, ValueError) as exc:
        drifts.append(Drift(INVALID, dest_root, str(exc)))
        return drifts

    structural_dirs: set[str] = set()
    for expected in expected_paths:
        relative = expected[len(dest_root) + 1 :]
        parts = relative.split("/")[:-1]
        for index in range(1, len(parts) + 1):
            structural_dirs.add(f"{dest_root}/{'/'.join(parts[:index])}")

    def visit(directory: Path) -> None:
        try:
            entries = _scandir_sorted(directory)
        except OSError as exc:
            rel = rel_posix(repo_root, directory)
            diagnostics.append(Diagnostic(ERROR, rel, f"cannot scan managed root: {exc}"))
            drifts.append(Drift(INVALID, rel, "cannot scan managed root"))
            return
        for entry in entries:
            path = Path(entry.path)
            rel = rel_posix(repo_root, path)
            try:
                entry_stat = entry.stat(follow_symlinks=False)
            except OSError as exc:
                diagnostics.append(Diagnostic(ERROR, rel, f"cannot inspect managed output: {exc}"))
                drifts.append(Drift(INVALID, rel, "cannot inspect managed output"))
                continue
            if _is_linklike_stat(entry_stat):
                drifts.append(Drift(INVALID, rel, "symlink/reparse point inside managed root"))
            elif stat.S_ISDIR(entry_stat.st_mode):
                visit(path)
                if rel not in structural_dirs:
                    try:
                        is_empty = not _scandir_sorted(path)
                    except OSError as exc:
                        diagnostics.append(Diagnostic(ERROR, rel, f"cannot inspect managed directory: {exc}"))
                        drifts.append(Drift(INVALID, rel, "cannot inspect managed directory"))
                    else:
                        if is_empty:
                            drifts.append(Drift(EXTRA, rel, "non-structural empty directory"))
            elif stat.S_ISREG(entry_stat.st_mode):
                if rel not in expected_paths:
                    drifts.append(Drift(EXTRA, rel))
            else:
                drifts.append(Drift(INVALID, rel, "special file inside managed root"))
    visit(root)
    return drifts


def _diff_preview(expected: str, actual: str, max_lines: int = 20) -> str:
    import difflib

    diff = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        "expected",
        "actual",
        n=1,
    )
    out = "".join(diff)
    if len(out.splitlines()) > max_lines:
        kept = max(max_lines - 1, 0)
        out = "\n".join(out.splitlines()[:kept] + ["... (truncated)"])
    return out.rstrip("\n")


# ---------------------------------------------------------------------------
# Apply (write) — full preflight, then per-file atomic replacement
# ---------------------------------------------------------------------------


def apply_plan(plan: SyncPlan) -> CheckReport:
    """Apply repairable drift atomically after a complete blocking preflight."""

    pre = check_plan(plan)
    # Block all mutation on any preflight/INVALID diagnostic.
    if any(d.severity == ERROR for d in pre.diagnostics) or any(
        drift.status == INVALID for drift in pre.drifts
    ):
        return pre

    for r in sorted(plan.rendered, key=lambda x: x.dest):
        dest = plan.repo_root / r.dest
        try:
            _atomic_write_if_needed(plan.repo_root, dest, r.expected)
        except (OSError, ValueError) as exc:
            pre.diagnostics.append(Diagnostic(ERROR, r.dest, f"write failed: {exc}"))
            pre.drifts.append(Drift(INVALID, r.dest, "write failed"))
            return pre

    approved_extras = {drift.path for drift in pre.drifts if drift.status == EXTRA}
    for dest_root, expected_paths in plan.managed_roots.items():
        try:
            _prune_extras(plan.repo_root, dest_root, expected_paths, approved_extras)
        except (OSError, ValueError) as exc:
            pre.diagnostics.append(Diagnostic(ERROR, dest_root, f"prune failed: {exc}"))
            pre.drifts.append(Drift(INVALID, dest_root, "prune failed"))
            return pre

    return check_plan(plan)


def _atomic_write_if_needed(repo_root: Path, dest: Path, expected: bytes) -> None:
    _validate_existing_chain(repo_root, dest)
    st = _lstat_or_none(dest)
    if st is not None and not stat.S_ISREG(st.st_mode):
        raise ValueError("generated destination is not a regular file")
    if st is not None and st.st_nlink != 1:
        raise ValueError("generated destination is a hardlink; refusing in-place mutation")
    if st is not None and dest.read_bytes() == expected:
        if _mode_ok(dest):
            return  # preserve mtime; nothing to do
        # Mode-only repair preserves content bytes and its mtime.
        os.chmod(dest, GENERATED_MODE)
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    _validate_existing_chain(repo_root, dest.parent, final_kind="dir")
    fd, tmp_name = tempfile.mkstemp(
        dir=dest.parent,
        prefix=f".{dest.name}.",
        suffix=".tmp",
    )
    tmp = Path(tmp_name)
    fd_open = True
    try:
        with os.fdopen(fd, "wb") as fh:
            fd_open = False
            written = fh.write(expected)
            if written != len(expected):
                raise OSError(
                    f"short write to temporary file: wrote {written} of {len(expected)} bytes"
                )
            if not IS_WINDOWS:
                os.fchmod(fh.fileno(), GENERATED_MODE)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, dest)
    finally:
        if fd_open:
            os.close(fd)
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def _mode_ok(dest: Path) -> bool:
    if IS_WINDOWS:
        return True
    return stat.S_IMODE(dest.lstat().st_mode) == GENERATED_MODE


def _prune_extras(
    repo_root: Path,
    dest_root: str,
    expected_paths: set[str],
    approved_extras: set[str],
) -> None:
    root = repo_root / dest_root
    if _lstat_or_none(root) is None:
        return
    _validate_existing_chain(repo_root, root, final_kind="dir")

    structural_dirs: set[str] = set()
    for expected in expected_paths:
        relative = expected[len(dest_root) + 1 :]
        parts = relative.split("/")[:-1]
        for index in range(1, len(parts) + 1):
            structural_dirs.add(f"{dest_root}/{'/'.join(parts[:index])}")

    candidates = {
        path for path in approved_extras
        if path.startswith(dest_root + "/") and path != dest_root
    }
    parent_candidates: set[str] = set()
    for relative in candidates:
        _validate_posix_rel(relative, "approved extra path")
        parent = relative.rsplit("/", 1)[0]
        while parent != dest_root and parent.startswith(dest_root + "/"):
            if parent not in structural_dirs:
                parent_candidates.add(parent)
            parent = parent.rsplit("/", 1)[0]

    for relative in sorted(candidates, key=lambda item: (item.count("/"), item), reverse=True):
        path = repo_root / relative
        st = _lstat_or_none(path)
        if st is None:
            continue
        _validate_existing_chain(repo_root, path)
        if stat.S_ISREG(st.st_mode):
            path.unlink()
        elif stat.S_ISDIR(st.st_mode):
            path.rmdir()
        else:
            raise ValueError(f"refusing to prune non-regular path {relative!r}")

    # Remove only parent chains that were proven to contain approved extras.
    for relative in sorted(parent_candidates, key=lambda item: (item.count("/"), item), reverse=True):
        path = repo_root / relative
        st = _lstat_or_none(path)
        if st is None:
            continue
        _validate_existing_chain(repo_root, path, final_kind="dir")
        try:
            path.rmdir()
        except OSError:
            # A non-empty directory contains an unapproved or racing entry and
            # must be preserved. Other rmdir failures surface to the caller.
            with os.scandir(path) as entries:
                if next(entries, None) is not None:
                    continue
            raise


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _format_report(report: CheckReport) -> list[str]:
    lines: list[str] = []
    for diag in sorted(report.diagnostics, key=lambda d: (d.path, d.message)):
        lines.append(f"{diag.severity}: {diag.path}: {diag.message}")
    previews_shown = 0
    previews_omitted = 0
    for drift in sorted(report.drifts, key=lambda d: (d.status, d.path)):
        if drift.status == OK:
            continue
        if drift.diff_preview and previews_shown < 10:
            suffix = f"\n{drift.diff_preview}"
            previews_shown += 1
        else:
            suffix = ""
            if drift.diff_preview:
                previews_omitted += 1
        lines.append(f"{drift.status}: {drift.path}{suffix}")
    if previews_omitted:
        lines.append(f"... diff previews omitted for {previews_omitted} additional file(s)")
    counts = report.counts()
    lines.append(
        "sync-adapters summary: "
        f"{counts[OK]} ok, {counts[STALE]} stale, {counts[MISSING]} missing, "
        f"{counts[EXTRA]} extra, {counts[INVALID]} invalid"
    )
    return lines


def compute_manifest_digest(manifest_path: Path) -> str:
    """Return the SHA-256 digest of the manifest's exact bytes."""

    return hashlib.sha256(manifest_path.read_bytes()).hexdigest()


def compute_source_digest(manifest: Manifest, repo_root: Path) -> str:
    """Hash every manifest-declared canonical source path and exact bytes.

    Each path and content blob is framed with an unsigned eight-byte big-endian
    length. This keeps the digest unambiguous while remaining deterministic
    across platforms and filesystem enumeration order.
    """

    diagnostics: list[Diagnostic] = []
    files: list[Path] = []
    for source_name in sorted(manifest.sources):
        files.extend(_discover_source(repo_root, manifest.sources[source_name], diagnostics))
    errors = [diagnostic for diagnostic in diagnostics if diagnostic.severity == ERROR]
    if errors:
        detail = "; ".join(f"{item.path}: {item.message}" for item in errors)
        raise ValueError(f"cannot compute canonical source digest: {detail}")

    digest = hashlib.sha256()
    for path in sorted(files, key=lambda item: rel_posix(repo_root, item)):
        path_bytes = rel_posix(repo_root, path).encode("utf-8")
        content = path.read_bytes()
        digest.update(len(path_bytes).to_bytes(8, "big"))
        digest.update(path_bytes)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def _checked_commit(repo_root: Path) -> str:
    """Return the current HEAD commit, or an empty string outside Git."""

    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError:
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


def build_state_payload(
    manifest_path: Path,
    manifest: Manifest,
    repo_root: Path,
    report: CheckReport,
) -> dict[str, object]:
    """Build the schema-v1 read-only adapter freshness record."""

    counts = report.counts()
    return {
        "schema_version": 1,
        "status": "fresh" if report.ok else "stale",
        "manifest_digest": compute_manifest_digest(manifest_path),
        "source_digest": compute_source_digest(manifest, repo_root),
        "checked_commit": _checked_commit(repo_root),
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "counts": {
            "ok": counts[OK],
            "stale": counts[STALE],
            "missing": counts[MISSING],
            "extra": counts[EXTRA],
            "invalid": counts[INVALID],
        },
        "check_command": "python scripts/sync_adapters.py --check",
        "drifts": [
            {"status": drift.status.lower(), "path": drift.path}
            for drift in sorted(report.drifts, key=lambda item: (item.status, item.path))
            if drift.status != OK
        ],
        "diagnostics": [
            {
                "severity": diagnostic.severity.lower(),
                "path": diagnostic.path,
                "message": diagnostic.message,
            }
            for diagnostic in sorted(report.diagnostics, key=lambda item: (item.path, item.message))
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate Claude/Codex runtime adapters from canonical sources."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Write generated adapters to disk.")
    mode.add_argument("--check", action="store_true", help="Fail if any adapter is stale (default).")
    parser.add_argument(
        "--class",
        dest="asset_class",
        default=ALL_TOKEN,
        help="Restrict to one declared source class (default: all).",
    )
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Path to cdd-manifest.toml.")
    parser.add_argument(
        "--state-json",
        action="store_true",
        help="Emit schema-v1 adapter freshness state as JSON (read-only, all classes only).",
    )
    args = parser.parse_args(argv)

    if args.state_json and args.write:
        parser.error("--state-json is read-only and cannot be combined with --write")
    if args.state_json and args.asset_class != ALL_TOKEN:
        parser.error("--state-json covers all canonical sources and cannot be combined with --class")

    manifest_path = Path(args.manifest)
    if not manifest_path.is_file():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1
    try:
        manifest = load_manifest(manifest_path)
    except (OSError, UnicodeError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"ERROR: invalid manifest: {exc}", file=sys.stderr)
        return 1

    valid_classes = set(manifest.sources) | {ALL_TOKEN}
    if args.asset_class not in valid_classes:
        print(
            f"ERROR: --class {args.asset_class!r} must be one of {sorted(valid_classes)}",
            file=sys.stderr,
        )
        return 1

    repo_root = REPO_ROOT if manifest_path.resolve() == DEFAULT_MANIFEST.resolve() else manifest_path.resolve().parent
    try:
        plan = build_sync_plan(manifest, repo_root, args.asset_class)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    report = apply_plan(plan) if args.write else check_plan(plan)
    if args.state_json:
        try:
            payload = build_state_payload(manifest_path, manifest, repo_root, report)
        except (OSError, ValueError) as exc:
            print(f"ERROR: cannot build adapter state: {exc}", file=sys.stderr)
            return 1
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    else:
        for line in _format_report(report):
            print(line)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
