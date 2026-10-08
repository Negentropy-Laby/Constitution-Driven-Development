"""Read-only verifier regressions with owned files and a legacy codec default."""

from contextlib import redirect_stdout
import csv
import hashlib
from io import StringIO
import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = REPO_ROOT / "production/qa/evidence/pr2-template-review-2026-10-08/verify.py"
SOURCE = "1" * 40
HEAD = "2" * 40
SOURCE_PATH = "skills/fixture/SKILL.md"
SOURCE_TEXT = "# Fixture\n中文证据 —\n"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_verifier():
    # Compile the actual script without leaving a cache in its retained records.
    module = types.ModuleType("template_record_verifier")
    module.__file__ = str(VERIFIER)
    exec(compile(VERIFIER.read_bytes(), str(VERIFIER), "exec"), module.__dict__)
    return module


def make_fixture(root):
    here = root / "production/qa/evidence/fixture"
    here.mkdir(parents=True)
    source_path = root / SOURCE_PATH
    source_path.parent.mkdir(parents=True)
    source_raw = SOURCE_TEXT.encode("utf-8")
    source_path.write_bytes(source_raw)

    def save(name, data):
        raw = (json.dumps(data, ensure_ascii=False) + "\n").encode("utf-8")
        (here / name).write_bytes(raw)
        return raw

    inputs_raw = save("source-inputs.json", {
        "source_commit": SOURCE,
        "scope": "Synthetic decoder fixture; no execution or qualification claim",
        "files": [{"path": SOURCE_PATH, "sha256": digest(source_raw), "bytes": len(source_raw)}],
    })
    binding = {"source_commit": SOURCE, "source_inputs_sha256": digest(inputs_raw)}
    log = b"Synthetic test fixture log\n"
    (here / "check-output").mkdir()
    (here / "check-output/check.txt").write_bytes(log)
    save("checks.json", {
        **binding,
        "checks": [{"exit_code": 0, "log_path": "check-output/check.txt",
                    "log_bytes": len(log), "log_sha256": digest(log)}],
        # These are inert fixture values required by the format, not test results.
        "posix_tests": [{"actual_execution": True, "result": "PASS"} for _ in range(6)],
    })
    save("lint-summary.json", {**binding, "scans": {"candidate": {"warnings": 1}},
                               "unresolved_new_defects": 0})
    save("review-dispositions.json", {**binding, "items": [
        {"review_item": number, "references": [SOURCE_PATH]} for number in range(1, 27)
    ]})
    save("spec-structure.json", binding)
    save("history-rewrite.json", {"old_archive_blob_oids": []})
    with (here / "lint-classification.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", lineterminator="\n", fieldnames=[
            "path", "source_sha256", "source_bytes", "line", "source_line", "owner_paths",
        ])
        writer.writeheader()
        writer.writerow({"path": SOURCE_PATH, "source_sha256": digest(source_raw),
                         "source_bytes": len(source_raw), "line": 2,
                         "source_line": SOURCE_TEXT.splitlines()[1], "owner_paths": SOURCE_PATH})

    retained = {path.relative_to(root).as_posix(): path.read_bytes()
                for path in here.rglob("*") if path.is_file()}
    calls = {
        ("show", SOURCE + ":" + SOURCE_PATH): source_raw,
        ("rev-parse", "HEAD"): (HEAD + "\n").encode(),
        ("rev-parse", "HEAD^"): (SOURCE + "\n").encode(),
        ("diff", "--name-only", SOURCE, HEAD): "\n".join(retained).encode(),
        ("ls-tree", "-r", "--name-only", "HEAD"):
            "\n".join([SOURCE_PATH, *retained]).encode(),
        ("rev-list", "--objects", HEAD): (SOURCE + "\n" + HEAD + "\n").encode(),
    }
    calls.update({("show", HEAD + ":" + path): raw for path, raw in retained.items()})
    return here, calls


class EvidenceVerifierTests(unittest.TestCase):
    def test_utf8_records_pass_with_cp936_default(self):
        # The second scenario reaches the source reader even on the unfixed script.
        for legacy_tsv in (True, False):
            with self.subTest(legacy_tsv=legacy_tsv), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                here, calls = make_fixture(root)
                module = load_verifier()
                reads = set()
                original_open = Path.open
                legacy_paths = {root / SOURCE_PATH}
                if legacy_tsv:
                    legacy_paths.add(here / "lint-classification.tsv")

                def codec_open(path, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
                    if "b" not in mode:
                        reads.add(path)
                        if encoding in (None, "locale"):
                            encoding = "cp936" if path in legacy_paths else "utf-8"
                    return original_open(path, mode, buffering, encoding, errors, newline)

                output = StringIO()
                with mock.patch.object(module, "ROOT", root), mock.patch.object(module, "HERE", here), \
                        mock.patch.object(module, "git", side_effect=lambda *args: calls[args]), \
                        mock.patch.object(Path, "open", codec_open), redirect_stdout(output):
                    module.main()
                result = json.loads(output.getvalue())
                self.assertEqual(result["result"], "PASS")
                self.assertEqual(result["source_files"], 1)
                self.assertEqual(result["warnings"], 1)
                self.assertTrue({root / SOURCE_PATH, here / "lint-classification.tsv"} <= reads)

    def test_changed_source_bytes_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            here, calls = make_fixture(root)
            module = load_verifier()
            source_path = root / SOURCE_PATH
            raw = source_path.read_bytes()
            source_path.write_bytes(raw[:-1] + b"X")  # Same size, different actual bytes.

            with mock.patch.object(module, "ROOT", root), mock.patch.object(module, "HERE", here), \
                    mock.patch.object(module, "git", side_effect=lambda *args: calls[args]), \
                    self.assertRaisesRegex(AssertionError, SOURCE_PATH):
                module.main()


if __name__ == "__main__":
    unittest.main()
