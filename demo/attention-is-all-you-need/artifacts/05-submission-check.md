# 05 - Submission Check

Owner: `ccf-submission-checker`

Target: NeurIPS-style demo.

## Venue Format Check

This demo does not claim current NeurIPS submission compliance. For a real submission, the checker must browse and verify the current official NeurIPS author instructions, template, page limit, anonymity policy, supplementary policy, and camera-ready rules.

Local reference path:

- `ccf-paper-writer/references/venue-guides/neurips.md`
- `ccf-latex-templates/NeurIPS/`

## Package Check

| Item | Demo status | Result |
| --- | --- | --- |
| Main TeX source | Not provided | Cannot pass. |
| Compiled PDF | Not provided | Cannot pass. |
| Page count | Not available | Must be checked after compilation. |
| Anonymity | Not applicable to demo markdown | Must be checked in PDF/TeX. |
| PDF metadata | Not available | Must be checked after compilation. |
| Bibliography | Primary source named only | Needs full BibTeX for real submission. |

## Artifact / Reproducibility Check

| Item | Demo status | Required for real submission |
| --- | --- | --- |
| Code | Not included | Training/inference code or clear non-release explanation. |
| Data | WMT tasks named | Dataset access instructions and preprocessing. |
| Model checkpoints | Not included | Release plan or limitation. |
| Environment | Not included | Hardware/software versions. |
| Seeds | Not included | Training/evaluation seeds when available. |
| License | Not included | Code/data/model license notes. |

## Gate Decision

Demo gate: pass as a workflow demonstration.

Real submission gate: fail until TeX/PDF, current official policy, artifact package, and bibliography are checked.
