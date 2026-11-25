"""Exercise the ACL 2027 local preflight without external programs."""
from hashlib import sha256
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from check_acl2027 import POLICY
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

    def test_acl_reads_nested_section_and_ignores_includegraphics(self):
        (self.root / "limits.tex").write_text(r"\section*{Limitations} No test on dialect shifts.", encoding="utf-8")
        self.write("[review]{acl}", r"\includegraphics{example}\input{limits}\bibliography{refs}")
        status = self.statuses("short")
        self.assertEqual(status["template_mode"], "pass")
        self.assertEqual(status["source_inputs"], "pass")
        self.assertEqual(status["limitations"], "pass")

    def test_acl_sections_and_modes(self):
        self.write("[preprint]{acl}", r"\bibliography{refs}\section*{Limitations} Limited scope.")
        status = self.statuses("long")
        self.assertEqual(status["template_mode"], "fail")
        self.assertEqual(status["limitations"], "fail")
        self.write("[final]{acl}", r"\section*{Limitations} TODO\relax\bibliography{refs}")
        final = self.statuses("long", "camera-ready")
        self.assertEqual(final["template_mode"], "pass")
        self.assertEqual(final["limitations"], "fail")


    def test_acl_limitations_follow_main_text_and_require_content(self):
        self.write("[review]{acl}", r"""
\section*{Limitations} Limited scope.
\section{Conclusion} Final main-text section.
\bibliography{refs}
""")
        self.assertEqual(self.statuses("long")["limitations"], "fail")
        self.write("[review]{acl}", r"\section*{Limitations}\label{sec:limits}\bibliography{refs}")
        self.assertEqual(self.statuses("long")["limitations"], "fail")


    def test_conditional_source_needs_rendered_inspection(self):
        self.write("[review]{acl}", r"\iftrue\section*{Limitations} Limited scope.\fi")
        status = self.statuses("short")
        self.assertEqual(status["source_declarations"], "not_verified")
        self.assertNotIn("limitations", status)

    def test_acl_inspected_boundary_and_review_or_final_cap(self):
        self.write("[review]{acl}", r"\section*{Limitations} Limited scope.\bibliography{refs}")
        info = b"Pages: 9\nPage size: 595.276 x 841.89 pts (A4)\nAuthor: Anonymous\n"
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), \
             patch.object(checker.subprocess, "run") as run:
            run.return_value.stdout = info
            self.assertEqual(self.statuses("short", pdf=self.pdf)["main_pages"], "not_verified")
            self.assertEqual(self.statuses("short", pdf=self.pdf, main_pages=4)["main_pages"], "pass")
            self.assertEqual(self.statuses("short", pdf=self.pdf, main_pages=5)["main_pages"], "fail")
            self.assertEqual(self.statuses("short", "camera-ready", pdf=self.pdf,
                                           main_pages=5)["main_pages"], "pass")


    def test_later_page_geometry_and_author_metadata_checked(self):
        self.write("[review]{acl}", r"\section*{Limitations} Limited scope.\bibliography{refs}")
        info = (b"Pages: 2\nPage    1 size: 595.276 x 841.89 pts (A4)\n"
                b"Page    2 size: 612 x 792 pts (letter)\nAuthor: Example Author\n")
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), \
             patch.object(checker.subprocess, "run") as run:
            run.return_value.stdout = info
            status = self.statuses("long", pdf=self.pdf)
            self.assertEqual(status["first_page_size"], "pass")
            self.assertEqual(status["page_geometry"], "fail")
            self.assertEqual(status["pdf_author_metadata"], "fail")
            self.assertEqual(status["arr_submission"], "not_verified")


if __name__ == "__main__":
    unittest.main()
