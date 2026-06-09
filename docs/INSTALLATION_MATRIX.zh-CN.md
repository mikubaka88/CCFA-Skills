# CCFA 安装矩阵

可以只安装一部分 skills，但任何子集都必须包含 `ccf-common`。

## 硬规则

- 一定安装 `ccf-common`：它保存共享路由、handoff、隐私、source registry 和 artifact 合约。
- 不要安装已经合并的旧 runtime 名称：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。
- `ccf-experiment-designer` 只用于实验设计和真实论文结果图表，不能拿来画文档流程图或编造数据图。
- `ccf-skill-forger` 负责 CCFA 文档 SVG，必须走 `tools/build_ccfa_diagrams.py` 和截图验收。

## 推荐组合

| 使用场景 | 安装 | 不装会缺什么 |
| --- | --- | --- |
| 全流程 | 15 个 runtime skills 全部安装 | 完整 CCFA 流程。 |
| NeurIPS 论文路径 | `ccf-common`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | 只缺家族维护能力。 |
| 写作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 没有 idea、文献、实验和 rebuttal 流程。 |
| 审稿/审计子集 | `ccf-common`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | 可以诊断问题，但不能写作、广泛检索、设计实验或检查投稿包。 |
| 监控子集 | `ccf-common`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 能追踪新论文和竞品信号，但不能写作或投稿。 |
| 早期研究子集 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 没有正文写作、投稿检查和 rebuttal。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-submission-checker`, `ccf-integrity-auditor` | 能查格式、投稿包和 artifact，但不能完整审稿。 |
| 维护子集 | `ccf-common`, `ccf-skill-forger` | 只做家族维护和文档/SVG 生成。 |

## 部分安装示例

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
