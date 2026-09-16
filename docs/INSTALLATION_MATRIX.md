# CCFA Installation Matrix

Partial installation is supported, but both `ccf-humanization` and `ccf-common` must be installed with every subset. The sets below describe task owners. Also retain the sibling resource directories read by the selected modes: reviewer, experiment, scaffolding, and submission modes can read `ccf-paper-writer/references/`; template modes need `ccf-latex-templates/` beside the installed skills. The legacy writer converter uses `ccf-paper-to-exemplar/scripts/convert.py`. A resource dependency does not authorize running its owning skill. A full repository/plugin layout preserves these paths; a skill-only installer may need the resource trees copied as well.

These subsets provide the listed capabilities, not every possible helper. If the current task needs an absent audit, retrieval, or reviewer capability, resolve that dependency or explicitly limit the dependent result; do not skip a necessary check or claim an uninstalled skill ran. Writing-only subsets may need `ccf-integrity-auditor` for source/number conflicts; presentation and submission subsets may need `ccf-paper-reviewer` for substantial argument changes.

## Hard Rules

- Always install `ccf-common`; it carries shared routing, handoff, privacy, source, and artifact rules.
- Always install `ccf-humanization`; activate it first, then `ccf-common`, before every specialist. Reuse their active rules; detailed prose/experiment modes remain task-dependent.
- Do not install merged helper names as runtime skills: `ccf-workflow-planner`, `ccf-paper-compressor`, `ccf-writing-reviewer`, `ccf-citation-auditor`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-venue-format-guide`, `ccf-resubmission-adapter`, `ccf-paper-presenter`, `ccf-doc-diagram-designer`.
- `ccf-experiment-designer` is only for experiment evidence and real paper-result tables/figure specs; `ccf-visual-composer` owns publication visual layout, bundled Python plotting recipes, palettes, captions, and render QA.
- `ccf-skill-forger` owns CCFA docs SVG diagrams through `tools/build_ccfa_diagrams.py` and screenshot QA.

## Recommended Sets

| Use case | Install | Missing impact |
| --- | --- | --- |
| Full workflow | All 17 runtime skills | Complete CCFA flow. |
| NeurIPS paper path | `ccf-common`, `ccf-humanization`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | Omits only family maintenance. |
| Writing subset | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-paper-reviewer`, `ccf-submission-checker` | No idea/literature/experiment pipeline or rebuttal; visual work still requires supplied results. |
| Review/audit subset | `ccf-common`, `ccf-humanization`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | Can diagnose but cannot write, search broadly, design experiments, or check packages. |
| Monitoring subset | `ccf-common`, `ccf-humanization`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | Tracks new overlap signals and routes deeper search or idea repair, but cannot write or submit. |
| Early research subset | `ccf-common`, `ccf-humanization`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | No manuscript, submission, or rebuttal support. |
| Visual/manuscript presentation subset | `ccf-common`, `ccf-humanization`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | Can turn supplied results into paper-ready visuals, Python SVG plots, and consistency checks, but cannot search literature or run full review. |
| Submission subset | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-submission-checker`, `ccf-integrity-auditor` | Can check format/package/artifacts and visual placement, but not run full review. |
| Maintenance subset | `ccf-common`, `ccf-humanization`, `ccf-skill-forger` | Only family maintenance and docs/SVG generation. |

## Partial Install Example

Bash:

```bash
skills=(ccf-common ccf-humanization ccf-paper-writer ccf-visual-composer ccf-paper-reviewer ccf-submission-checker)
mkdir -p "$CODEX_HOME/skills"
for s in "${skills[@]}"; do cp -R "$s" "$CODEX_HOME/skills/"; done
```

PowerShell:

```powershell
$skills = @("ccf-common", "ccf-humanization", "ccf-paper-writer", "ccf-visual-composer", "ccf-paper-reviewer", "ccf-submission-checker")
New-Item -ItemType Directory -Force "$env:CODEX_HOME\skills" | Out-Null
foreach ($s in $skills) { Copy-Item -Recurse -Force $s "$env:CODEX_HOME\skills\" }
```
