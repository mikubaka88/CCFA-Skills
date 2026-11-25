# ACSAC 2026 Venue Guide

| Field | Value |
| --- | --- |
| Scope | ACSAC 2026 technical papers |
| Area and catalog | Computer Security, CCF-B |
| Source | [Official author policy](https://www.acsac.org/2026/submissions/papers/) and [CCFDDL record](https://github.com/ccfddl/ccf-deadlines/blob/main/conference/SC/acsac.yml) |
| Template | `ccf-latex-templates/ACSAC/2026/main.tex` |
| Verified | 2026-11-25 |

## Template and Stage

Use IEEEtran 1.8b with conference and compsoc, two columns and US Letter. Omit author identities and use third-person citations for earlier public work. Add an Ethical Considerations section where the policy requires it. Verify the camera-ready instructions separately.

Review submissions have at most 11 main-content pages and 16 total pages. The remaining space covers clearly marked references and appendices. This is the 2026 technical-paper policy snapshot. Use the dated bundle and recheck live instructions for other editions.

## Writing and Evidence

Tie each security claim to an explicit threat model, assumptions, realistic conditions, and the actual evidence. Distinguish measured protection from design intent. Record artifact availability, the evaluation environment and limitations.

## Review and Response

Evaluate applied significance, technical correctness, quality of evaluation and reproducibility. Distinguish initial review, additional reviews after the first round, anonymous response and shepherded minor revision. Track formal artifact evaluation separately from the paper decision.

## Local Submission Preflight

From the CCFA root:

```bash
python ccf-submission-checker/scripts/check_venue_profile.py --profile acsac-2026 --tex path/to/main.tex --pdf path/to/main.pdf
```

Pass `--main-pages` after inspecting the rendered boundary. Resolve manual checks in the actual PDF, supplementary package and submission system.

## Reference Papers

[Selected research references](../exemplars/papers/acsac/README.md) provide original papers, verified presentation or award status, and reading cues.
