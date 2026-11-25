# ECOOP 2027 Venue Guide

| Field | Value |
| --- | --- |
| Scope | ECOOP 2027 technical papers |
| Area and catalog | Programming Languages, CCF-B |
| Source | [Official author policy](https://2027.ecoop.org/track/ecoop-2027-technical-papers) and [CCFDDL record](https://github.com/ccfddl/ccf-deadlines/blob/main/conference/SE/ecoop.yml) |
| Template | `ccf-latex-templates/ECOOP/2027/lipics-v2021-sample-article.tex` |
| Verified | 2026-11-25 |

## Template and Stage

Use the official LIPIcs class for camera-ready. For review, the CFP also allows PACMPL and TOPLAS source formats, with mandatory conversion for accepted submissions. Anonymize supplementary artifacts and use third-person self-citations.

The review version has no formal page cap. Select the appropriate author category. The final version has a 25-page limit in LIPIcs, excluding references. Use the dated bundle and recheck live instructions for other editions.

## Writing and Evidence

For a semantics or type-system result, state the language fragment and theorem assumptions, give a witness that shows why the construct matters, and explain where the proof obligations enter. For an experience or tooling contribution, select evidence of behavior in practice and characterize unsupported cases and artifact scope.

## Review and Response

Check correctness, contribution fit, and the reproducibility of evidence appropriate to the paper category. The double-anonymous CFP prohibits using AI tools for assigned reviews or sharing confidential review materials with them. Authors' internal self-review is a separate workflow. Use the four-day author-response window and distinguish revision from immediate resubmission after rejection.

## Local Submission Preflight

From the CCFA root:

```bash
python ccf-submission-checker/scripts/check_venue_profile.py --profile ecoop-2027 --tex path/to/main.tex --pdf path/to/main.pdf
```

Pass `--main-pages` after inspecting the rendered boundary. Resolve manual checks in the actual PDF, supplementary package and submission system.

## Reference Papers

[Selected research references](../exemplars/papers/ecoop/README.md) provide original papers, verified presentation or award status, and reading cues.
