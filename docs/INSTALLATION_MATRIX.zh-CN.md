# CCFA 安装矩阵

可以只安装部分 skills，但任何子集都必须包含 `ccf-humanization` 和 `ccf-common`。下表列出任务负责人；还需保留所用模式读取的相邻资源：审稿、实验、脚手架和投稿模式可能读取 `ccf-paper-writer/references/`，模板模式需要安装根目录下相邻的 `ccf-latex-templates/`，旧版写作转换命令依赖 `ccf-paper-to-exemplar/scripts/convert.py`。资源依赖不代表授权运行对应 skill。完整仓库或插件布局保留这些路径；仅复制 skill 的安装器还需同步所需资源树。

各子集只提供列出的能力，不保证包含所有条件协作者。当前任务若需要尚未安装的审计、检索或审稿能力，应补齐该依赖或明确受影响结果的限制，不能省略必要检查或声称未安装的技能已运行。写作子集遇到来源或数字冲突可能需要 `ccf-integrity-auditor`；图表呈现与投稿子集遇到实质性论证改动可能需要 `ccf-paper-reviewer`。

## 硬规则

- 一定安装 `ccf-common`：它保存共享路由、handoff、隐私、source registry 和 artifact 合约。
- 复制 Common 时保留 `scripts/preferences.py` 和 `assets/configurator/`。可选的本地配置页只需要 Python 3.10+，无需额外依赖；个人 JSON 设置位于安装目录之外。没有配置文件也能按默认设置运行。
- 同时保留 Common 内的连续性参考文档与 `scripts/continuity.py`。可选的只读检查器同样使用 Python 3.10+，无需额外依赖；普通 skill 启动不会创建任务状态文件或自动运行检查器。
- 所有子集均须安装 `ccf-humanization`：任何具体技能执行前先启用它，再启用 `ccf-common`。交接复用已生效规则，详细写作与实验检查按任务需要执行。
- 不要安装已经合并的旧 runtime 名称：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。
- `ccf-experiment-designer` 只负责实验证据、真实结果表和 evidence-bound 图表规格；`ccf-visual-composer` 负责发表级图表排版、内置 Python 绘图配方、配色、caption、正文嵌入和渲染 QA。
- `ccf-skill-forger` 负责 CCFA 文档 SVG，必须走 `tools/build_ccfa_diagrams.py` 和截图/渲染验收。

## 推荐组合

| 使用场景 | 安装 | 不安装会缺什么 |
| --- | --- | --- |
| 全流程 | 17 个 runtime skills 全部安装 | 完整 CCFA 流程。 |
| NeurIPS 论文路径 | `ccf-common`, `ccf-humanization`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | 只缺家族维护能力。 |
| 写作子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 没有 idea、文献、实验和 rebuttal 流程；视觉任务仍需要已提供结果。 |
| 审稿/审计子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | 可以诊断问题，但不能写作、广泛检索、设计实验或检查投稿包。 |
| 监控子集 | `ccf-common`, `ccf-humanization`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 能追踪新论文和竞品信号，但不能写作或投稿。 |
| 早期研究子集 | `ccf-common`, `ccf-humanization`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 没有正文写作、图表视觉整合、投稿检查和 rebuttal。 |
| 图表/正文呈现子集 | `ccf-common`, `ccf-humanization`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 能基于真实结果制作论文图表、Python SVG 绘图、配色、caption、正文嵌入和一致性检查，但不能做完整文献检索或完整审稿。 |
| 投稿子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-submission-checker`, `ccf-integrity-auditor` | 能查格式、投稿包、artifact 和图表展示，但不能完整审稿。 |
| 维护子集 | `ccf-common`, `ccf-humanization`, `ccf-skill-forger` | 只做家族维护和文档 SVG 生成。 |

## 部分安装示例

在仓库 clone 的根目录执行以下命令，先复制写作子集，再补齐下一节的相邻资源。更新前先比较个人修改。重复复制会合并目录内容，不会多嵌一层；上游已删除的旧文件不会自动清除，需要根据差异单独处理。

默认目标依据本地核对的 `skills` CLI 1.5.22：Codex 全局安装使用 `$CODEX_HOME/skills`，未设置或为空时回退到 `~/.codex/skills`；项目安装使用 `.agents/skills`。先用 `npx skills list --global --agent codex` 确认实际位置。其他客户端、项目安装或新版安装器，请把下面两组命令中的 `ccfa_skills_dir` / `$ccfaSkillsDir` 改为对应安装根目录，不要把资源补到另一个 Codex 目录。

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

## 补齐相邻资源

`npx skills add ... --skill '*' --copy` 安装全部 17 个 skills，但不会复制没有 `SKILL.md` 的根目录 `ccf-latex-templates/`。请从与安装 skills 相同版本的仓库执行以下命令。这组资源同时补齐部分安装所需的参考文件和旧版转换脚本。仅复制资源不代表安装或调用资源所属 skill；任务需要它的能力时，仍需单独安装对应技能。完整仓库或插件布局已保留这些相邻路径。

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
