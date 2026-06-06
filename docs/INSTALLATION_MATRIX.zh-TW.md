# CCFA 安裝矩陣

可以只安裝一部分 skills，但任何子集都必須包含 `ccf-common`。

## 硬規則

- 一定安裝 `ccf-common`：它保存共享路由、handoff、隱私、source registry 和 artifact 合約。
- 不要安裝已經合併的舊 runtime 名稱：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。
- `ccf-experiment-designer` 只用於實驗設計和真實論文結果圖表，不能拿來畫文件流程圖或編造數據圖。
- `ccf-skill-forger` 負責 CCFA 文件 SVG，必須走 `tools/build_ccfa_diagrams.py` 和截圖驗收。

## 推薦組合

| 使用場景 | 安裝 | 不裝會缺什麼 |
| --- | --- | --- |
| 全流程 | 13 個 runtime skills 全部安裝 | 完整 CCFA 流程。 |
| NeurIPS 論文路徑 | `ccf-common`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | 只缺家族維護能力。 |
| 寫作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 沒有 idea、文獻、實驗和 rebuttal 流程。 |
| 審稿/稽核子集 | `ccf-common`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | 可以診斷問題，但不能寫作、廣泛檢索、設計實驗或檢查投稿包。 |
| 早期研究子集 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-searcher`, `ccf-experiment-designer` | 沒有正文寫作、投稿檢查和 rebuttal。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-submission-checker`, `ccf-integrity-auditor` | 能查格式、投稿包和 artifact，但不能完整審稿。 |
| 維護子集 | `ccf-common`, `ccf-skill-forger` | 只做家族維護和文件/SVG 生成。 |

## 部分安裝示例

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
