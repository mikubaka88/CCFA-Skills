# CVPR Venue Guide

| Field | Value |
| --- | --- |
| Venue / track | CVPR 2027 main research track, submission/review; rebuttal below |
| Template | `ccf-latex-templates/CVPR/2027/main.tex`, with its entire sibling bundle |
| Historical template | `ccf-latex-templates/CVPR/main.tex` remains the unmodified 2026 example |
| Official author rules | https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines |
| Checked | 2026-11-12; recheck official rules for the actual submission stage |
| Source | Official linked archive, release `CVPR2027-v1`; file hashes in `CVPR/2027/template-source.json` |

## Select The Year And Complete Bundle

For 2027, copy the complete `CVPR/2027/` source bundle, including `cvpr.sty`, `ieeenat_fullname.bst`, `preamble.tex`, bibliography and `sec/`. Preserve upstream comments and credits. The official conference download omits the optional teaser found in the GitHub tag; provenance records this small archive variant rather than claiming byte identity. Both verified 2027 style hashes are recognized by the checker. The entry is an `article` document using the `cvpr` package, not a `cvpr.cls` class. Choose exactly one mode:

```latex
\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}  % submission
% \usepackage{cvpr}       % camera-ready, instead of review
% \usepackage[rebuttal]{cvpr} % author response, instead of review
\input{preamble}
\def\confName{CVPR}
\def\confYear{2027}
```

The 2027 kit removes the Paper ID field; do not restore the old placeholder or rename a 2026 style. Existing 2026 projects keep their historical bundle. ICCV and workshops require their own year/track rules.

## CVPR 2027 Submission Checks

- Main content: at most eight pages, including figures/tables. Additional pages may contain cited references and the required AI-use statement; appendices are not an automatic exemption.
- Insert `\section*{LLM Usage Statement}` after the main text and before references. Describe actual tools, affected research/writing parts and extent, including editing; keep identity private. Declare no use only when true. Do not generate a disclosure from guesses.
- Review copies are anonymous, including PDF metadata, supplement, acknowledgments and identifying links. Content-expanding external links are disallowed; ordinary scholarly links need contextual review.
- Confirm every author's enrollment/profile/COI and quotas: at most 25 submissions per author; at most one without an eligible reciprocal reviewer. Local files cannot establish these facts.
- Rebuttal: anonymous, one page including references/figures, matching kit, no external material links. No unsolicited new contributions or experiments.
- Official assigned reviewers/ACs use only conference-approved OpenReview AI tools for confidential material. Author-side internal pre-review is a distinct role.

The supplied sample omits the mandatory section required by the current online instructions: keep the upstream mirror unchanged, but add the truthful statement to the actual manuscript. Final/Findings-specific instructions must be checked when that stage applies; a sample final-mode switch is not a final-package approval.

## Lightweight Local Check

When submission checking is requested and `ccf-submission-checker` is installed, run:

```bash
python ccf-submission-checker/scripts/check_cvpr2027.py --tex path/to/main.tex --stage review --pdf path/to/main.pdf
```

The checker follows local TeX inputs, tests mode/year/style, statement presence/order and available PDF properties. For a PDF exceeding eight pages, provide `--main-pages` only after inspecting the true main-text boundary; references/statement pages alone do not prove an overlength paper. Its report distinguishes failures and facts that local inspection cannot establish. It neither uploads nor submits files. Keep logs under the existing task build directory.

Formatting checks do not prescribe a fixed scientific outline, invented results or generic contribution prose. Writing remains with `ccf-paper-writer`; results/protocol questions remain with their scientific owner.

Source records: `cvpr-2027-author-guidelines`, `cvpr-2027-author-kit`, and `cvpr-2027-dates` in the shared registry. Official release: https://github.com/cvpr-org/author-kit/releases/tag/CVPR2027-v1 .
