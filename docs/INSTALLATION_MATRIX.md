# CCFA Installation Matrix

Partial installation is supported, but `ccf-common` must be installed with every subset.

## Hard Rules

- Always install `ccf-common`; it carries shared routing, handoff, privacy, source, and artifact rules.
- Do not install merged helper names as runtime skills: `ccf-workflow-planner`, `ccf-paper-compressor`, `ccf-writing-reviewer`, `ccf-citation-auditor`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-venue-format-guide`, `ccf-resubmission-adapter`, `ccf-paper-presenter`, `ccf-doc-diagram-designer`.
- `ccf-experiment-designer` is only for experiment evidence and real paper-result tables/figures.
- `ccf-skill-forger` owns CCFA docs SVG diagrams through `tools/build_ccfa_diagrams.py` and screenshot QA.

## Recommended Sets

| Use case | Install | Missing impact |
| --- | --- | --- |
| Full workflow | All 13 runtime skills | Complete CCFA flow. |
| NeurIPS paper path | `ccf-common`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | Omits only governance maintenance. |
| Writing subset | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | No idea/literature/experiment pipeline or rebuttal. |
| Review/audit subset | `ccf-common`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | Can diagnose but cannot write, search broadly, design experiments, or check packages. |
| Early research subset | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-searcher`, `ccf-experiment-designer` | No manuscript, submission, or rebuttal support. |
| Submission subset | `ccf-common`, `ccf-paper-writer`, `ccf-submission-checker`, `ccf-integrity-auditor` | Can check format/package/artifacts but not run full review. |
| Maintenance subset | `ccf-common`, `ccf-skill-forger` | Only family maintenance and docs/SVG generation. |

## Partial Install Example

Bash:

```bash
skills=(ccf-common ccf-paper-writer ccf-paper-reviewer ccf-submission-checker)
mkdir -p "$CODEX_HOME/skills"
for s in "${skills[@]}"; do cp -R "$s" "$CODEX_HOME/skills/"; done
```

PowerShell:

```powershell
$skills = @("ccf-common", "ccf-paper-writer", "ccf-paper-reviewer", "ccf-submission-checker")
New-Item -ItemType Directory -Force "$env:CODEX_HOME\skills" | Out-Null
foreach ($s in $skills) { Copy-Item -Recurse -Force $s "$env:CODEX_HOME\skills\" }
```
