# 05 - ICLR Submission Check

Owner: `ccf-submission-checker`

Target: ICLR 2026-style demo.

## Venue Format Check

| Item | Demo status | Result |
| --- | --- | --- |
| Venue guide | `ccf-paper-writer/references/venue-guides/iclr.md` | Updated to ICLR 2026 Author Guide basics. |
| Review mode | Double-blind during review | Author block anonymized by ICLR style. |
| Main text page limit | 9 pages for submission, excluding references and appendix | Demo PDF is 6 pages. |
| Discussion/camera-ready limit | 10 pages, excluding references and appendix | Not applicable to current demo stage. |
| Style file | `paper/iclr2026_conference.sty` | Present. |
| Main TeX | `paper/attention_iclr_submission.tex` | Present. |

## Build Check

| Check | Result |
| --- | --- |
| Command | `pdflatex -interaction=nonstopmode -halt-on-error -output-directory <temp> attention_iclr_submission.tex` run twice. |
| Build status | Pass. |
| PDF page count | 6 pages in temporary build. |
| Known environment warning | MiKTeX reports administrator update warnings; not a manuscript failure. |
| PDF committed? | No. The demo keeps source files only. |

## Anonymity Check

| Surface | Status |
| --- | --- |
| Author block | `Anonymous Authors`; ICLR style prints anonymous review block. |
| Acknowledgments | None in submission text. |
| Project URLs | None. |
| Self-citation | No identifying self-citation in demo. |
| PDF metadata | Not committed; must be checked on final generated PDF. |

## Artifact And Reproducibility Check

| Artifact | Current status | Required for real submission |
| --- | --- | --- |
| Code | Absent | Training and inference code or explicit non-release reason. |
| Data | WMT tasks named | Dataset download/preprocessing instructions. |
| Model checkpoints | Absent | Release plan or access limitation. |
| Seeds | Absent | Training/evaluation seeds where available. |
| Hardware | Official P100 setup stated | Full environment and runtime notes. |
| Ablations | Planned but incomplete | Full values from official source or reproduction logs. |
| Appendix | Checklist placeholder present | Expand with implementation, decoding, preprocessing, and artifact details. |

## Gate Decision

Demo gate: pass as a closed-loop CCFA demonstration because the ICLR LaTeX source builds, the manuscript is complete enough to review, and all unsupported evidence is marked.

Real submission gate: fail until current official policy is rechecked, full ablation values are filled, related work is updated, PDF metadata is inspected, and artifact/reproducibility materials are prepared.
