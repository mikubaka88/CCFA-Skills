"""Regression cases for the shared edition-specific submission checker."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import check_venue_profile as checker


class SubmissionProfiles(unittest.TestCase):
    def checks(self):
        rows = []
        return rows, lambda key, state, detail: rows.append((key, state, detail))

    def test_selected_profiles_have_year_and_tracks(self):
        profiles = sorted(checker.PROFILE_ROOT.glob("*.json"))
        self.assertTrue(profiles)
        for source in profiles:
            profile = json.loads(source.read_text(encoding="utf-8"))
            self.assertTrue(source.stem.endswith(str(profile["year"])))
            self.assertTrue(profile["tracks"])
            self.assertTrue(profile["manual_checks"])

    def test_required_appendix_section_must_follow_appendix(self):
        profile = {"stage_checks": {}, "required_appendix_sections": ["Test"]}
        with TemporaryDirectory() as directory:
            tex = Path(directory) / "main.tex"
            text = r"\begin{document}\section{Test} Sample statement.\appendix\end{document}"
            tex.write_text(text, encoding="utf-8")
            rows, add = self.checks()
            checker.audit_source(tex, profile, "review", add)
        self.assertIn(("Test", "fail", "Required section belongs in the appendix."), rows)

    def test_total_cap_is_independent_of_body(self):
        profile = {"total_pages": {"review": 16}, "page_limits": {"review": {"research": 11}}}
        rows, add = self.checks()
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), \
             patch.object(checker.subprocess, "run") as run:
            run.return_value.stdout = "Pages: 17\nAuthor:\n"
            checker.audit_pdf(Path("main.pdf"), profile, "review", "research", 11, add)
        self.assertEqual({key: state for key, state, _ in rows}["total_pages"], "fail")
        self.assertEqual({key: state for key, state, _ in rows}["main_pages"], "pass")

    def test_mixed_geometry_and_identifying_metadata(self):
        profile = {"letter": True, "page_limits": {"review": {"research": 11}}}
        rows, add = self.checks()
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), \
             patch.object(checker.subprocess, "run") as run:
            run.return_value.stdout = ("Pages: 2\nPage 1 size: 612 x 792 pts\n"
                                       "Page 2 size: 595 x 842 pts\nAuthor: Test Name\n")
            checker.audit_pdf(Path("main.pdf"), profile, "review", "research", None, add)
        values = {key: state for key, state, _ in rows}
        self.assertEqual(values["page_size"], "fail")
        self.assertEqual(values["author_metadata"], "fail")


if __name__ == "__main__":
    unittest.main()
