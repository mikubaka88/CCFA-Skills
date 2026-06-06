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
| Main TeX source | `paper/attention_neurips_demo.tex` | Present as demo draft. |
| NeurIPS style file | `paper/neurips_2026.sty` | Copied into demo paper folder to mirror scaffold behavior. |
| Compiled PDF | Builds with `pdflatex` during validation; PDF not committed. | Demo compile passes, but real submission must compile in the project environment. |
| Page count | 3 pages in validation build | Real submission must re-check after full content and official policy update. |
| Anonymity | Anonymous author block in TeX | Must still be checked in compiled PDF and metadata. |
| PDF metadata | Not available | Must be checked after compilation. |
| Bibliography | Original paper listed in TeX bibliography | Needs full BibTeX and all related work for real submission. |

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

Real submission gate: fail until PDF compilation, current official policy, artifact package, full related work, and bibliography are checked.
