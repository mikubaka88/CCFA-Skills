# CCFA 安装矩阵

可以只安装部分 skills，但任何子集都必须包含 `ccf-common`。

## 硬规则

- 一定安装 `ccf-common`：它保存共享路由、handoff、隐私、source registry 和 artifact 合约。
- 不要安装已经合并的旧 runtime 名称：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。
- `ccf-experiment-designer` 只负责实验证据、真实结果表和 evidence-bound 图表规格；`ccf-visual-composer` 负责发表级图表排版、内置 Python 绘图配方、配色、caption、正文嵌入和渲染 QA。
- `ccf-skill-forger` 负责 CCFA 文档 SVG，必须走 `tools/build_ccfa_diagrams.py` 和截图/渲染验收。

## 推荐组合

| 使用场景 | 安装 | 不安装会缺什么 |
| --- | --- | --- |
| 全流程 | 16 个 runtime skills 全部安装 | 完整 CCFA 流程。 |
| NeurIPS 论文路径 | `ccf-common`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | 只缺家族维护能力。 |
| 写作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 没有 idea、文献、实验和 rebuttal 流程；视觉任务仍需要已提供结果。 |
| 审稿/审计子集 | `ccf-common`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | 可以诊断问题，但不能写作、广泛检索、设计实验或检查投稿包。 |
| 监控子集 | `ccf-common`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 能追踪新论文和竞品信号，但不能写作或投稿。 |
| 早期研究子集 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 没有正文写作、图表视觉整合、投稿检查和 rebuttal。 |
| 图表/正文呈现子集 | `ccf-common`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 能基于真实结果制作论文图表、Python SVG 绘图、配色、caption、正文嵌入和一致性检查，但不能做完整文献检索或完整审稿。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-submission-checker`, `ccf-integrity-auditor` | 能查格式、投稿包、artifact 和图表展示，但不能完整审稿。 |
| 维护子集 | `ccf-common`, `ccf-skill-forger` | 只做家族维护和文档 SVG 生成。 |

## 部分安装示例

Bash:

```bash
skills=(ccf-common ccf-paper-writer ccf-visual-composer ccf-paper-reviewer ccf-submission-checker)
mkdir -p "$CODEX_HOME/skills"
for s in "${skills[@]}"; do cp -R "$s" "$CODEX_HOME/skills/"; done
```

PowerShell:

```powershell
$skills = @("ccf-common", "ccf-paper-writer", "ccf-visual-composer", "ccf-paper-reviewer", "ccf-submission-checker")
New-Item -ItemType Directory -Force "$env:CODEX_HOME\skills" | Out-Null
foreach ($s in $skills) { Copy-Item -Recurse -Force $s "$env:CODEX_HOME\skills\" }
```
