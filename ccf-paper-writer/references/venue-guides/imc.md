# IMC 2027 Venue Guide

| Field | Value |
| --- | --- |
| Scope | IMC 2027 main technical track |
| Area and catalog | Computer Networks, CCF-B |
| Source | [Official author policy](https://conferences.sigcomm.org/imc/2027/submission-instructions/) and [CCFDDL record](https://github.com/ccfddl/ccf-deadlines/blob/main/conference/NW/imc.yml) |
| Template | `ccf-latex-templates/IMC/2027/main.tex` |
| Verified | 2026-11-25 |

## Template and Stage

Use the double-column 10pt US Letter ACM format. The official review example uses anonymous and nonacm options, with page numbering enabled. Place Ethics, Open Science, and Generative AI in the appendix, and upload the bibliography BBL through HotCRP.

Full/short papers have 13/6 technical-content pages respectively, including figures and excluding references and appendices. Confirm the current camera-ready instructions and the separate Replicability track expression-of-interest workflow. Use the dated bundle and recheck live instructions for other editions.

## Writing and Evidence

Use a well-defined measurement question, observation unit, vantage point, time window and coverage. Distinguish observed traffic from inferred behavior, discuss sampling and vantage-point bias, and give a defensible plan for artifacts that cannot be shared.

## Review and Response

Focus on measurement validity, interpretability, ethical collection and evidence that the results or measurement methods transfer. Check intended artifact availability against the Open Science statement. The brief rebuttal is for clarifying reviewer concerns. Track one-shot revision separately.

## Local Submission Preflight

From the CCFA root:

```bash
python ccf-submission-checker/scripts/check_venue_profile.py --profile imc-2027 --track full --tex path/to/main.tex --pdf path/to/main.pdf
```

Pass `--main-pages` after inspecting the rendered boundary. Resolve manual checks in the actual PDF, supplementary package and submission system.

## Reference Papers

[Selected research references](../exemplars/papers/imc/README.md) provide original papers, verified presentation or award status, and reading cues.
