"""Exercise the ICML 2027 local preflight without external programs."""
from hashlib import sha256
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from check_icml2027 import POLICY
import yearly_submission as checker


class PreflightTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.tex = self.root / "main.tex"
        self.pdf = self.root / "main.pdf"
        self.pdf.touch()

    def write(self, package, body):
        self.tex.write_text(
            "\\documentclass{article}\n\\usepackage" + package
            + "\n\\begin{document}\n" + body + "\n\\end{document}\n",
            encoding="utf-8",
        )

    def statuses(self, track, stage="review", **kwargs):
        report = checker.audit(POLICY, track, stage, self.tex, **kwargs)
        return {item["id"]: item["status"] for item in report["checks"]}

    def test_bundled_sources_match_official_manifests(self):
        kit = checker.TEMPLATES / POLICY.name / "2027"
        manifest = json.loads((kit / "template-source.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["venue"], POLICY.name)
        for item in manifest["files"]:
            with self.subTest(file=item["path"]):
                data = (kit / item["path"]).read_bytes().replace(b"\r\n", b"\n")
                self.assertEqual(sha256(data).hexdigest(), item["sha256"])

    def test_icml_disclosure_may_follow_references(self):
        self.write("[nohyperref]{icml2027}", r"""
\section*{Impact Statement} The work has limited scope.
\bibliography{refs}
\section*{AI Disclosure Statement} Routine editing only.
\appendix
""")
        status = self.statuses("research")
        for key in ("template_mode", "impact_statement", "ai_disclosure", "appendix_order"):
            self.assertEqual(status[key], "pass")

    def test_icml_old_style_and_comment_only_disclosure(self):
        self.write("{amsmath,icml2026}", r"""
% \section*{AI Use Statement} Comment only.
\bibliography{refs}
\section*{Impact Statement} Too late.
""")
        status = self.statuses("research")
        self.assertEqual(status["template_mode"], "fail")
        self.assertEqual(status["impact_statement"], "fail")
        self.assertEqual(status["ai_disclosure"], "not_verified")

    def test_icml_rejects_loading_both_years(self):
        self.write("{icml2027,icml2026}", r"\section{Introduction} Main text.")
        self.assertEqual(self.statuses("research")["template_mode"], "fail")


    def test_icml_flags_impact_and_disclosure_inside_main_text(self):
        self.write("{icml2027}", r"""
\section{Method} Main text.
\section*{Impact Statement} Limited effects.
\section*{AI Use Statement} Routine editing.
\section{Conclusion} More main text.
\bibliography{refs}
""")
        status = self.statuses("research")
        self.assertEqual(status["impact_statement"], "fail")
        self.assertEqual(status["ai_disclosure"], "fail")


    def test_icml_final_cap_and_letter_geometry(self):
        self.write("[accepted]{icml2027}", r"\section*{AI Use Statement} Routine edits.\bibliography{refs}")
        info = b"Pages: 10\nPage size: 612 x 792 pts (letter)\n"
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), \
             patch.object(checker.subprocess, "run") as run:
            run.return_value.stdout = info
            status = self.statuses("research", "camera-ready", pdf=self.pdf, main_pages=9)
            self.assertEqual(status["first_page_size"], "pass")
            self.assertEqual(status["main_pages"], "pass")
            self.assertEqual(self.statuses("research", pdf=self.pdf, main_pages=9)["main_pages"], "fail")
            self.assertEqual(self.statuses("research", "camera-ready", pdf=self.pdf,
                                           main_pages=11)["main_pages"], "fail")


if __name__ == "__main__":
    unittest.main()
