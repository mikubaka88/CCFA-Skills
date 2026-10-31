#!/usr/bin/env python3
"""Bounded, lazy inventory search and truthful coverage regression tests."""
from pathlib import Path
import gzip
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "resources/python/ccfa_figure_corpus.py"
spec = importlib.util.spec_from_file_location("ccfa_figure_corpus", MODULE_PATH)
corpus = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corpus)


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.rows = [
            {"title": "Scaling Visual Models", "url": "https://example.test/a", "venue": "CVPR", "year": 2025, "track": "main", "pdf": None},
            {"title": "Scaling 中文模型", "url": "https://example.test/b", "venue": "NeurIPS", "year": 2026, "track": "main", "pdf": None},
            {"title": "Visual Calibration", "url": "https://example.test/c", "venue": "CVPR", "year": 2026, "track": "main", "pdf": None},
            {"title": "Clinical Calibration", "url": "https://example.test/d", "venue": "Nature Machine Intelligence", "year": 2025, "track": None, "pdf": None},
        ]
        self.write_rows(self.rows)
        self.manifest = {"version": 1, "record_count": 4, "all_figures_reproduced": False,
                         "coverage": [{"venue": "CVPR", "year": 2025, "record_count": 1},
                                      {"venue": "CVPR", "year": 2026, "record_count": 1},
                                      {"venue": "NeurIPS", "year": 2026, "record_count": 1}]}
        (self.directory / "corpus.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def write_rows(self, rows):
        with gzip.open(self.directory / "papers.jsonl.gz", "wt", encoding="utf-8") as stream:
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")

    def test_casefolded_terms_and_conjunctive_title_search(self):
        result = corpus.search("VISUAL scaling", directory=self.directory)
        self.assertEqual([r["title"] for r in result["matches"]], ["Scaling Visual Models"])
        self.assertFalse(result["has_more"])
        self.assertFalse(result["all_figures_reproduced"])

    def test_unicode_search_and_venue_aliases(self):
        self.assertEqual(corpus.search("中文", venue="nips", directory=self.directory)["returned"], 1)
        self.assertEqual(corpus.search(venue="NMI", directory=self.directory)["matches"][0]["title"], "Clinical Calibration")

    def test_filters_apply_before_limit(self):
        result = corpus.search(venue="CVPR", year=2026, limit=1, directory=self.directory)
        self.assertEqual(result["matches"][0]["title"], "Visual Calibration")
        self.assertFalse(result["has_more"])

    def test_limit_reports_more_without_materializing_whole_inventory(self):
        seen = []
        def rows(_):
            for i in range(100):
                seen.append(i)
                yield self.rows[0]
        with patch.object(corpus, "iter_papers", rows):
            result = corpus.search(limit=2, directory=self.directory)
        self.assertEqual(result["returned"], 2)
        self.assertTrue(result["has_more"])
        self.assertEqual(seen, [0, 1, 2])
        self.assertNotIn("total_hits", result)

    def test_exact_limit_does_not_claim_more(self):
        self.assertFalse(corpus.search(limit=4, directory=self.directory)["has_more"])

    def test_limit_and_query_validation(self):
        for limit in [0, 51, True, 1.5]:
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                corpus.search(limit=limit, directory=self.directory)
        with self.assertRaises(ValueError):
            corpus.search(" ! ", directory=self.directory)

    def test_coverage_keeps_global_totals_distinct_from_filters(self):
        self.manifest["harvest_inputs"] = [{"large_debug_record": "not needed by a normal query"}]
        (self.directory / "corpus.json").write_text(json.dumps(self.manifest), encoding="utf-8")
        result = corpus.coverage(self.directory, venue="cvpr", year=2026)
        self.assertEqual(len(result["coverage"]), 1)
        self.assertEqual(result["record_count"], 4)
        self.assertTrue(result["filtered"])
        self.assertFalse(result["all_figures_reproduced"])
        self.assertNotIn("harvest_inputs", result)

    def test_invalid_inventory_is_not_treated_as_empty(self):
        with gzip.open(self.directory / "papers.jsonl.gz", "wt", encoding="utf-8") as stream:
            stream.write('{broken}\n')
        with self.assertRaises(corpus.CorpusError):
            corpus.search(directory=self.directory)
        (self.directory / "papers.jsonl.gz").unlink()
        with self.assertRaises(corpus.CorpusError):
            corpus.search(directory=self.directory)

    def test_import_is_lazy_and_does_not_require_plotting_packages(self):
        command = [sys.executable, "-S", "-c", "import runpy; runpy.run_path(" + repr(str(MODULE_PATH)) + ", run_name='inventory_import')"]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")

    def test_truncated_compressed_inventory_reports_a_corpus_error(self):
        path = self.directory / "papers.jsonl.gz"
        path.write_bytes(path.read_bytes()[:-12])
        with self.assertRaises(corpus.CorpusError):
            list(corpus.iter_papers(self.directory))

    def test_invalid_coverage_shape_does_not_claim_success(self):
        (self.directory / "corpus.json").write_text('{"coverage":[42]}', encoding="utf-8")
        with self.assertRaises(corpus.CorpusError):
            corpus.coverage(self.directory)

    def test_cli_returns_bounded_json_and_preserves_chinese(self):
        command = [sys.executable, str(MODULE_PATH), "--corpus-dir", str(self.directory), "--query", "中文", "--limit", "1"]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["matches"][0]["title"], "Scaling 中文模型")


if __name__ == "__main__":
    unittest.main()
