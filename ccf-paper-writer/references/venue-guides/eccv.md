# ECCV 2026 Venue Guide

| Field | Value |
| --- | --- |
| Scope | ECCV 2026 main research |
| Area and catalog | Computer Vision, CCF-B |
| Source | [Official author policy](https://eccv.ecva.net/Conferences/2026/SubmissionPolicies) and [CCFDDL record](https://github.com/ccfddl/ccf-deadlines/blob/main/conference/AI/eccv.yml) |
| Template | `ccf-latex-templates/ECCV/2026/main.tex` |
| Verified | 2026-11-25 |

## Template and Stage

Use the exact year kit based on LNCS, with ECCV review mode, year and the OpenReview submission ID. Keep the official fonts and layout. Do not reuse CVPR class options or assume the 2026 rules for a later edition.

The main paper cap is 14 pages including figures and tables. The main PDF may exceed this cap only for cited references. Keep supplemental material separate and recheck the edition's actual instructions. Use the dated bundle and recheck live instructions for other editions.

## Writing and Evidence

State the selected contribution type and its strongest visual claim. Pair fair comparisons with examples under comparable conditions. Separately report benchmark performance, mechanism evidence, failure cases and costs when they support the actual contribution.

## Review and Response

Use evidence appropriate to the primary contribution type and inspect the manuscript's main qualitative and quantitative support. Official assigned reviewers must keep the submissions confidential and must not process them with LLMs. Use the author-side internal workflow only for author-owned drafts.

## Local Submission Preflight

From the CCFA root:

```bash
python ccf-submission-checker/scripts/check_venue_profile.py --profile eccv-2026 --tex path/to/main.tex --pdf path/to/main.pdf
```

Pass `--main-pages` after inspecting the rendered boundary. Resolve manual checks in the actual PDF, supplementary package and submission system.

## Reference Papers

[Selected research references](../exemplars/papers/eccv/README.md) provide original papers, verified presentation or award status, and reading cues.
