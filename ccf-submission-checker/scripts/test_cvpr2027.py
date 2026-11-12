"""Policy regressions for the bounded CVPR 2027 local checker."""
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import check_cvpr2027 as checker


class CVPRChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ccfa-cvpr2027-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(checker.KIT / "cvpr.sty", self.root / "cvpr.sty")
        self.tex = self.root / "main.tex"
        self.base = r"""\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}
\def\confYear{2027}
\author{Example Author}
\begin{document}
Main scientific content.
\section*{LLM Usage Statement}
An AI assistant helped draft this synthetic fixture.
\begin{thebibliography}{1}\bibitem{a} A cited work.\end{thebibliography}
\end{document}
"""

    def run_source(self, value=None, **kwargs):
        self.tex.write_text(value or self.base, encoding="utf-8")
        report = checker.audit(self.tex, **kwargs)
        return report, {r["id"]: r for r in report["checks"]}

    def test_valid_local_source_keeps_nonlocal_facts_unverified(self):
        report, rows = self.run_source()
        self.assertEqual(report["failures"], 0)
        for key in ["year", "mode", "style", "llm_statement"]:
            self.assertEqual(rows[key]["status"], "pass")
        for key in ["disclosure_truth", "anonymity", "administration", "pdf"]:
            self.assertEqual(rows[key]["status"], "not_verified")

    def test_historical_style_and_year_are_not_relabelled_as_2027(self):
        shutil.copy2(checker.ROOT / "ccf-latex-templates/CVPR/cvpr.sty", self.root / "cvpr.sty")
        _, rows = self.run_source(self.base.replace("{2027}", "{2026}"))
        self.assertEqual(rows["style"]["status"], "fail")
        self.assertEqual(rows["year"]["status"], "fail")

    def test_official_github_style_variant_is_also_recognized(self):
        path=self.root/"cvpr.sty"
        value=path.read_text(encoding="utf-8")
        before=r"        \def\pid{\parbox"
        self.assertIn(before,value)
        path.write_text(value.replace(before,r"    \def\pid{\parbox"),encoding="utf-8",newline="\n")
        _,rows=self.run_source()
        self.assertEqual(rows["style"]["status"],"pass")

    def test_comment_and_verbatim_titles_do_not_supply_statement(self):
        for fake in ["% \\section*{LLM Usage Statement}", r"\begin{verbatim}\section*{LLM Usage Statement}\end{verbatim}"]:
            _, rows = self.run_source(self.base.replace(r"\section*{LLM Usage Statement}", fake))
            self.assertEqual(rows["llm_statement"]["status"], "fail")

    def test_empty_placeholder_and_post_reference_sections_fail(self):
        for body in ["", "TODO", r"\label{statement}\clearpage"]:
            _, rows = self.run_source(self.base.replace("An AI assistant helped draft this synthetic fixture.", body))
            self.assertEqual(rows["llm_statement"]["status"], "fail")
        wrong = self.base.replace(r"\section*{LLM Usage Statement}", "").replace(r"\end{thebibliography}", r"\end{thebibliography}\section*{LLM Usage Statement}An AI assistant helped.")
        _, rows = self.run_source(wrong)
        self.assertEqual(rows["llm_statement"]["status"], "fail")

    def test_statement_must_follow_main_text(self):
        value=self.base.replace(r"\begin{thebibliography}",r"\section{Conclusion}More main text.\begin{thebibliography}")
        _,rows=self.run_source(value)
        self.assertEqual(rows["llm_statement"]["status"],"fail")

    def test_duplicate_modes_fail_without_rejecting_hidden_author_command(self):
        _, rows = self.run_source(self.base.replace(r"\usepackage[review]{cvpr}", r"\usepackage{cvpr}\usepackage[review]{cvpr}"))
        self.assertEqual(rows["mode"]["status"], "fail")
        self.assertNotIn("author_command", rows)

    def test_page_numbers_are_orthogonal_to_stage_and_conflicts_still_fail(self):
        for stage,options,expected in [
            ("review","review,pagenumbers","pass"),
            ("rebuttal","rebuttal,pagenumbers","pass"),
            ("camera-ready","pagenumbers","pass"),
            ("review","review,rebuttal","fail"),
            ("review","review,unknown-option","fail"),
        ]:
            with self.subTest(stage=stage,options=options):
                value=self.base.replace("[review]","["+options+"]")
                _,rows=self.run_source(value,stage=stage)
                self.assertEqual(rows["mode"]["status"],expected)
                if stage=="camera-ready":
                    self.assertEqual(rows["final_page_numbering"]["status"],"not_verified")

    def test_transitive_input_statement_and_missing_input(self):
        section = self.root / "statement.tex"
        section.write_text(r"\section*{LLM Usage Statement}An AI assistant helped.", encoding="utf-8")
        value = self.base.replace(r"\section*{LLM Usage Statement}", r"\input{statement}")
        _, rows = self.run_source(value)
        self.assertEqual(rows["llm_statement"]["status"], "pass")
        _, rows = self.run_source(value.replace(r"\input{statement}", "\\input statement.tex\n"))
        self.assertEqual(rows["llm_statement"]["status"], "pass")
        section.unlink()
        _, rows = self.run_source(value)
        self.assertEqual(rows["source_inputs"]["status"], "fail")

    def test_cyclic_and_outside_input_paths_fail_locally(self):
        for value in [r"\input{main}", r"\input{../outside}"]:
            _, rows = self.run_source(value)
            self.assertEqual(rows["source_inputs"]["status"], "fail")

    def test_custom_style_and_conditional_tex_need_rendered_verification(self):
        with (self.root / "cvpr.sty").open("a", encoding="utf-8") as file:
            file.write("\n% local modification\n")
        _, rows = self.run_source(self.base.replace(r"\usepackage[review]{cvpr}", r"\iftrue\usepackage[review]{cvpr}\else\usepackage{cvpr}\fi"))
        self.assertEqual(rows["style"]["status"], "not_verified")
        self.assertEqual(rows["mode"]["status"], "not_verified")

    def test_scholarly_url_requires_context_not_blanket_rejection(self):
        _, rows = self.run_source(self.base.replace("A cited work.", "A cited work. https://arxiv.org/abs/example"))
        self.assertEqual(rows["external_links"]["status"], "not_verified")

    def test_total_pages_do_not_equal_main_text_budget(self):
        pdf = self.root / "paper.pdf"; pdf.write_bytes(b"fixture")
        result = type("Result", (), {"stdout": b"Pages: 10\nPage size: 612 x 792 pts\nAuthor:\nCreator: LaTeX with hyperref\n"})()
        with patch.object(checker.shutil, "which", return_value="pdfinfo"), patch.object(checker.subprocess, "run", return_value=result):
            _, rows = self.run_source(pdf=pdf)
            self.assertEqual(rows["page_budget"]["status"], "not_verified")
            self.assertEqual(rows["pdf_author_metadata"]["status"], "pass")
            _, rows = self.run_source(pdf=pdf, main_pages=8)
            self.assertEqual(rows["page_budget"]["status"], "pass")
            _, rows = self.run_source(pdf=pdf, main_pages=9)
            self.assertEqual(rows["page_budget"]["status"], "fail")
            _, rows = self.run_source(self.base.replace("[review]", "[rebuttal]"), stage="rebuttal", pdf=pdf)
            self.assertEqual(rows["page_budget"]["status"], "fail")

    def test_pdf_info_controls_windows_dates_and_preserves_unicode_metadata(self):
        pdf=self.root/"paper.pdf";pdf.write_bytes(b"fixture")
        output="CreationDate: 2026-11-12T22:55:17+08\nPages: 1\nPage size: 612 x 792 pts\nAuthor: 研究作者\n"
        def inspect(args,**kwargs):
            self.assertEqual(args[1:4],["-enc","UTF-8","-isodates"])
            return type("Result",(),{"stdout":output.encode("utf-8")})()
        with patch.object(checker.shutil,"which",return_value="pdfinfo"),patch.object(checker.subprocess,"run",side_effect=inspect):
            _,rows=self.run_source(pdf=pdf)
        self.assertEqual(rows["pdf"]["status"],"pass")
        self.assertEqual(rows["paper_size"]["status"],"pass")
        self.assertEqual(rows["page_budget"]["status"],"pass")
        self.assertEqual(rows["pdf_author_metadata"]["status"],"fail")


if __name__ == "__main__":
    unittest.main(verbosity=2)
