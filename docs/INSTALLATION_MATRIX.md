# CCFA Installation Matrix

## Lean release installation (recommended)

Download `ccfa-skills-0.12.1-lean.zip` and `SHA256SUMS` from the [0.12.1 release](https://github.com/mikubaka88/CCFA-Skills/releases/tag/v0.12.1). Check the archive's SHA-256 (`Get-FileHash -Algorithm SHA256` in PowerShell or `shasum -a 256` on macOS/Linux), then extract it. The extracted directory contains `tools/install_release.py`; it requires Python 3.10+ and no network or extra packages. Replace both quoted paths below with your extracted folder and the client's actual skills root:

```text
python -B "<lean-dir>/tools/install_release.py" --source "<lean-dir>" --target "<skills-root>" --dry-run
python -B "<lean-dir>/tools/install_release.py" --source "<lean-dir>" --target "<skills-root>"
```

The default installs all 18 skills, their sibling templates and required resources. For a subset, repeat `--skill`, for example `--skill ccf-paper-reviewer --skill ccf-integrity-auditor`. Humanization and Common are always included. Required writer references/scripts, legacy converter resources and template resources are copied where applicable, without adding an unselected owner's `SKILL.md`. Root README and release tools are not copied into the skills root. Existing client discovery rules still apply; start a new session after installation.

The lean archive keeps original Markdown passages, exemplar cards, all figure examples and templates. Complete writing-example PDFs are in the optional `ccfa-skills-0.12.1-papers.zip`. To add those explicitly, check and extract that archive separately, then run:

```text
python -B "<papers-dir>/tools/install_release.py" --source "<papers-dir>" --target "<skills-root>"
```

Install the matching lean release first. Alternatively supply `--papers "<papers-dir>"` during its installation. No PDF download occurs automatically. Original-text learning remains available in lean mode; install the optional pack or use an authorized original source when the selected passage needs visual PDF inspection. Git clones and `npx skills` still obtain the full source, including its PDFs; the repository itself has not been made lean.

Both profiles use the same release identity, version and manifest format, with relative paths, skill inventory, file sizes and SHA-256 hashes. The installer validates the source before copying, rejects unsafe paths and symlinks, and records its own managed hashes in `.ccfa-release-receipt.json`. Later installations replace only matching old managed files or adopt identical files. Personal edits stop the preflight for reconciliation; extra user files, saved preferences and removed-upstream files are retained. There is no force-overwrite or cleanup option. For an older manual/npx installation, compare and reconcile differing files before adoption. See [updates](getting-started/AUTO_UPDATE.md).

Partial installation is supported, but both `ccf-humanization` and `ccf-common` must be installed with every subset. The sets below describe task owners. Also retain the sibling resource directories read by the selected modes: reviewer, experiment, scaffolding, and submission modes can read `ccf-paper-writer/references/`; template modes need `ccf-latex-templates/` beside the installed skills. The legacy writer converter uses `ccf-paper-to-exemplar/scripts/convert.py`. A resource dependency does not authorize running its owning skill. A full repository/plugin layout preserves these paths; a skill-only installer may need the resource trees copied as well.

These subsets provide the listed capabilities, not every possible helper. If the current task needs an absent audit, retrieval, or reviewer capability, resolve that dependency or explicitly limit the dependent result; do not skip a necessary check or claim an uninstalled skill ran. Writing-only subsets may need `ccf-integrity-auditor` for source/number conflicts; presentation and submission subsets may need `ccf-paper-reviewer` for substantial argument changes.

## Hard Rules

- Always install `ccf-common`; it carries shared routing, handoff, privacy, source, and artifact rules.
- Retain `ccf-common/scripts/preferences.py` and `ccf-common/assets/configurator/` when copying Common. The optional local configurator needs Python 3.10+ and no extra packages; personal JSON settings stay outside installed skills. No preference file is required for default operation.
- Keep Common's bundled continuity reference and `scripts/continuity.py` with the same installation. The optional read-only checker also uses Python 3.10+ with no extra packages; ordinary skill activation does not create a task-state file or launch checks.
- Always install `ccf-humanization`; activate it first, then `ccf-common`, before every specialist. Reuse their active rules; detailed prose/experiment modes remain task-dependent.
- Do not install merged helper names as runtime skills: `ccf-workflow-planner`, `ccf-paper-compressor`, `ccf-writing-reviewer`, `ccf-citation-auditor`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-venue-format-guide`, `ccf-resubmission-adapter`, `ccf-paper-presenter`, `ccf-doc-diagram-designer`.
- `ccf-experiment-designer` is only for experiment evidence and real paper-result tables/figure specs; `ccf-visual-composer` owns publication visual layout, bundled Python plotting recipes, palettes, captions, and render QA.
- `ccf-skill-forger` owns CCFA docs SVG diagrams through `tools/build_ccfa_diagrams.py` and screenshot QA.

## Recommended Sets

| Use case | Install | Missing impact |
| --- | --- | --- |
| Full workflow | All 18 runtime skills | Complete CCFA flow. |
| Research implementation and training | `ccf-humanization`, `ccf-common`, `ccf-research-engineer` | Implementation, reproduction, and training diagnosis; add designer for comparison protocols and orchestrator for repeated campaigns. |
| NeurIPS paper path | `ccf-common`, `ccf-humanization`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-research-engineer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | Omits only family maintenance. |
| Writing subset | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-paper-reviewer`, `ccf-submission-checker` | No idea/literature/experiment pipeline or rebuttal; visual work still requires supplied results. |
| Review/audit subset | `ccf-common`, `ccf-humanization`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | Can diagnose but cannot write, search broadly, design experiments, or check packages. |
| Monitoring subset | `ccf-common`, `ccf-humanization`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | Tracks new overlap signals and routes deeper search or idea repair, but cannot write or submit. |
| Early research subset | `ccf-common`, `ccf-humanization`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | No manuscript, submission, or rebuttal support. |
| Visual/manuscript presentation subset | `ccf-common`, `ccf-humanization`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | Can turn supplied results into paper-ready visuals, Python SVG plots, and consistency checks, but cannot search literature or run full review. |
| Submission subset | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-submission-checker`, `ccf-integrity-auditor` | Can check format/package/artifacts and visual placement, but not run full review. |
| Maintenance subset | `ccf-common`, `ccf-humanization`, `ccf-skill-forger` | Only family maintenance and docs/SVG generation. |

## Partial Install Example

Run these commands from a clone of the repository root. They copy the writing subset, then the sibling resources below. Compare any personal edits before updating. Repeated copies merge contents without nesting directories; files removed upstream are not deleted automatically, so review those removals separately.

The default target matches the locally inspected `skills` CLI 1.5.22: Codex global installs use `$CODEX_HOME/skills`, falling back to `~/.codex/skills`; project installs use `.agents/skills`. Verify your actual destination with `npx skills list --global --agent codex`. For a different client, project install, or newer installer, replace `ccfa_skills_dir` / `$ccfaSkillsDir` with that installation's root in both examples. Do not copy resources into an unrelated Codex directory.

Bash:

```bash
ccfa_codex_home="${CODEX_HOME:-}"
ccfa_codex_home="${ccfa_codex_home#"${ccfa_codex_home%%[![:space:]]*}"}"
ccfa_codex_home="${ccfa_codex_home%"${ccfa_codex_home##*[![:space:]]}"}"
ccfa_skills_dir="${ccfa_codex_home:-$HOME/.codex}/skills"
ccfa_paths=(ccf-common ccf-humanization ccf-paper-writer ccf-visual-composer ccf-paper-reviewer ccf-submission-checker)
for ccfa_path in "${ccfa_paths[@]}"; do
  mkdir -p "$ccfa_skills_dir/$ccfa_path"
  cp -R "$ccfa_path/." "$ccfa_skills_dir/$ccfa_path/"
done
```

PowerShell:

```powershell
$ccfaCodexHome = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) { Join-Path $HOME ".codex" } else { $env:CODEX_HOME.Trim() }
$ccfaSkillsDir = Join-Path $ccfaCodexHome "skills"
$ccfaPaths = @("ccf-common", "ccf-humanization", "ccf-paper-writer", "ccf-visual-composer", "ccf-paper-reviewer", "ccf-submission-checker")
foreach ($ccfaPath in $ccfaPaths) {
  $ccfaDestination = Join-Path $ccfaSkillsDir $ccfaPath
  New-Item -ItemType Directory -Force -Path $ccfaDestination | Out-Null
  Get-ChildItem -LiteralPath $ccfaPath -Force | Copy-Item -Destination $ccfaDestination -Recurse -Force
}
```

<a id="sibling-resources"></a>

## Sibling resources

`npx skills add ... --skill '*' --copy` installs all 18 skills, but does not copy the root-level `ccf-latex-templates/` directory, which has no `SKILL.md`. Run the following from the same repository revision used for the skills. This resource bundle also covers partial-install references and legacy conversion scripts. Copying these resources does not install or authorize their owning skills; add a specialist separately when the task needs its capability. Full repository/plugin layouts already retain the sibling paths.

Bash:

```bash
ccfa_codex_home="${CODEX_HOME:-}"
ccfa_codex_home="${ccfa_codex_home#"${ccfa_codex_home%%[![:space:]]*}"}"
ccfa_codex_home="${ccfa_codex_home%"${ccfa_codex_home##*[![:space:]]}"}"
ccfa_skills_dir="${ccfa_codex_home:-$HOME/.codex}/skills"
ccfa_paths=(ccf-paper-writer/references ccf-paper-writer/scripts ccf-paper-to-exemplar/scripts ccf-latex-templates)
for ccfa_path in "${ccfa_paths[@]}"; do
  mkdir -p "$ccfa_skills_dir/$ccfa_path"
  cp -R "$ccfa_path/." "$ccfa_skills_dir/$ccfa_path/"
done
```

PowerShell:

```powershell
$ccfaCodexHome = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) { Join-Path $HOME ".codex" } else { $env:CODEX_HOME.Trim() }
$ccfaSkillsDir = Join-Path $ccfaCodexHome "skills"
$ccfaPaths = @("ccf-paper-writer/references", "ccf-paper-writer/scripts", "ccf-paper-to-exemplar/scripts", "ccf-latex-templates")
foreach ($ccfaPath in $ccfaPaths) {
  $ccfaDestination = Join-Path $ccfaSkillsDir $ccfaPath
  New-Item -ItemType Directory -Force -Path $ccfaDestination | Out-Null
  Get-ChildItem -LiteralPath $ccfaPath -Force | Copy-Item -Destination $ccfaDestination -Recurse -Force
}
```

Interrupted installs retain a pending receipt. Resume with the same package, selection and target; intervening personal edits stop replacement and remain intact. Release builds default to indexed Git paths; development builds can explicitly use `--include-untracked`. The manifest records the source commit and dirty state.
