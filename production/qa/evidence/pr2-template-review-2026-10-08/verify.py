#!/usr/bin/env python3
"""Read-only verification of this small template-review record collection."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    inputs_raw = (HERE / "source-inputs.json").read_bytes()
    inputs = json.loads(inputs_raw)
    source = inputs["source_commit"]
    files = {row["path"]: row for row in inputs["files"]}
    for path, row in files.items():
        committed = git("show", source + ":" + path)
        assert len(committed) == row["bytes"] and sha(committed) == row["sha256"], path
        assert (ROOT / path).read_bytes() == committed, path

    checks = json.loads((HERE / "checks.json").read_bytes())
    assert checks["source_commit"] == source
    assert checks["source_inputs_sha256"] == sha(inputs_raw)
    assert all(row["exit_code"] == 0 for row in checks["checks"])
    for row in checks["checks"] + checks.get("earlier_attempts", []):
        log = (HERE / row["log_path"]).read_bytes()
        assert len(log) == row["log_bytes"] and sha(log) == row["log_sha256"]
    assert len(checks["posix_tests"]) == 6
    assert all(row["actual_execution"] and row["result"] == "PASS" for row in checks["posix_tests"])

    for name in ["lint-summary.json", "review-dispositions.json", "spec-structure.json"]:
        data = json.loads((HERE / name).read_bytes())
        assert data["source_commit"] == source and data["source_inputs_sha256"] == sha(inputs_raw)
    review = json.loads((HERE / "review-dispositions.json").read_bytes())
    assert [row["review_item"] for row in review["items"]] == list(range(1, 27))
    for row in review["items"]:
        for path in row["references"]:
            assert (ROOT / path).is_file() or (HERE / path).is_file(), path

    with (HERE / "lint-classification.tsv").open(newline="") as handle:
        warnings = list(csv.DictReader(handle, delimiter="\t"))
    lint = json.loads((HERE / "lint-summary.json").read_bytes())
    assert len(warnings) == lint["scans"]["candidate"]["warnings"]
    for row in warnings:
        bound = files[row["path"]]
        assert row["source_sha256"] == bound["sha256"], row["path"]
        assert int(row["source_bytes"]) == bound["bytes"]
        lines = (ROOT / row["path"]).read_text().splitlines()
        assert lines[int(row["line"]) - 1] == row["source_line"], row["path"]
        for path in row["owner_paths"].split(";"):
            assert path in files and (ROOT / path).is_file(), path
    assert lint["unresolved_new_defects"] == 0

    head = git("rev-parse", "HEAD").decode().strip()
    prefix = HERE.relative_to(ROOT).as_posix() + "/"
    if head != source:
        changed = git("diff", "--name-only", source, head).decode().splitlines()
        assert changed and all(path.startswith(prefix) for path in changed), changed
        assert git("rev-parse", "HEAD^").decode().strip() == source
    tree = git("ls-tree", "-r", "--name-only", "HEAD").decode().splitlines()
    if head != source:
        for path in HERE.rglob("*"):
            if path.is_file():
                relative = path.relative_to(ROOT).as_posix()
                assert relative in tree, "uncommitted/ignored record: " + relative
                assert git("show", head + ":" + relative) == path.read_bytes(), relative
    assert not any(path.startswith("production/qa/evidence/cdd-revision-2026-10-08/") for path in tree)
    assert not any(path.endswith((".tar.gz", ".patch.gz")) and path.startswith(prefix) for path in tree)
    history = json.loads((HERE / "history-rewrite.json").read_bytes())
    reachable = {line.split(" ", 1)[0] for line in git("rev-list", "--objects", head).decode().splitlines()}
    assert not set(history["old_archive_blob_oids"]) & reachable
    print(json.dumps({"result": "PASS", "source_commit": source, "head": head,
                      "source_files": len(files), "warnings": len(warnings),
                      "scope": "byte/reference/source-binding integrity only; no independent or Agent qualification"}))


if __name__ == "__main__":
    main()
