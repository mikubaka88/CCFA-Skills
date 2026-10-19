# CCFA 安裝矩陣

可以只安裝部分 skills，但任何子集都必須包含 `ccf-humanization` 和 `ccf-common`。 下表列出任務負責人；還需保留所用模式讀取的相鄰資源：審稿、實驗、腳手架與投稿模式可能讀取 `ccf-paper-writer/references/`，模板模式需要安裝根目錄下相鄰的 `ccf-latex-templates/`，舊版寫作轉換命令依賴 `ccf-paper-to-exemplar/scripts/convert.py`。資源依賴不代表授權執行對應 skill。完整倉庫或外掛保留這些路徑；僅複製 skill 的安裝器還需同步所需資源樹。

各子集只提供列出的能力，不保證包含所有條件協作者。目前任務若需要尚未安裝的審計、檢索或審稿能力，應補齊該依賴或明確受影響結果的限制，不能省略必要檢查或聲稱未安裝的技能已執行。寫作子集遇到來源或數字衝突可能需要 `ccf-integrity-auditor`；圖表呈現與投稿子集遇到實質性論證改動可能需要 `ccf-paper-reviewer`。

## 硬規則

- 一定安裝 `ccf-common`：它保存共享路由、handoff、隱私、source registry 和 artifact 合約。
- 複製 Common 時保留 `scripts/preferences.py` 與 `assets/configurator/`。可選的本機設定頁只需要 Python 3.10+，無需額外依賴；個人 JSON 設定位於安裝目錄之外。沒有設定檔也能依預設設定運作。
- 同時保留 Common 內的連續性參考文件與 `scripts/continuity.py`。可選的唯讀檢查器同樣使用 Python 3.10+，無需額外依賴；一般 skill 啟動不會建立任務狀態檔或自動執行檢查器。
- 所有子集均須安裝 `ccf-humanization`：任何具體技能執行前先啟用它，再啟用 `ccf-common`。交接重用已生效規則，詳細寫作與實驗檢查依任務需要執行。
- 不要安裝已經合併的舊 runtime 名稱：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。
- `ccf-experiment-designer` 只負責實驗證據、真實結果表和 evidence-bound 圖表規格；`ccf-visual-composer` 負責發表級圖表排版、內建 Python 繪圖配方、配色、caption、正文嵌入和渲染 QA。
- `ccf-skill-forger` 負責 CCFA 文件 SVG，必須走 `tools/build_ccfa_diagrams.py` 和截圖/渲染驗收。

## 推薦組合

| 使用場景 | 安裝 | 不安裝會缺什麼 |
| --- | --- | --- |
| 全流程 | 17 個 runtime skills 全部安裝 | 完整 CCFA 流程。 |
| NeurIPS 論文路徑 | `ccf-common`, `ccf-humanization`, `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` | 只缺家族維護能力。 |
| 寫作子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 沒有 idea、文獻、實驗和 rebuttal 流程；視覺任務仍需要已提供結果。 |
| 審稿/審計子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-reviewer`, `ccf-integrity-auditor` | 可以診斷問題，但不能寫作、廣泛檢索、設計實驗或檢查投稿包。 |
| 監控子集 | `ccf-common`, `ccf-humanization`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 能追蹤新論文和競品訊號，但不能寫作或投稿。 |
| 早期研究子集 | `ccf-common`, `ccf-humanization`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 沒有正文寫作、圖表視覺整合、投稿檢查和 rebuttal。 |
| 圖表/正文呈現子集 | `ccf-common`, `ccf-humanization`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 能基於真實結果製作論文圖表、Python SVG 繪圖、配色、caption、正文嵌入和一致性檢查，但不能做完整文獻檢索或完整審稿。 |
| 投稿子集 | `ccf-common`, `ccf-humanization`, `ccf-paper-writer`, `ccf-visual-composer`, `ccf-submission-checker`, `ccf-integrity-auditor` | 能查格式、投稿包、artifact 和圖表展示，但不能完整審稿。 |
| 維護子集 | `ccf-common`, `ccf-humanization`, `ccf-skill-forger` | 只做家族維護和文件 SVG 生成。 |

## 部分安裝示例

在倉庫 clone 的根目錄執行以下命令，先複製寫作子集，再補齊下一節的相鄰資源。更新前先比較個人修改。重複複製會合併目錄內容，不會多嵌一層；上游已刪除的舊檔案不會自動清除，需要依差異個別處理。

預設目標依據本機核對的 `skills` CLI 1.5.22：Codex 全域安裝使用 `$CODEX_HOME/skills`，未設定或為空時回退到 `~/.codex/skills`；專案安裝使用 `.agents/skills`。先用 `npx skills list --global --agent codex` 確認實際位置。其他用戶端、專案安裝或新版安裝器，請將以下兩組命令中的 `ccfa_skills_dir` / `$ccfaSkillsDir` 改為對應安裝根目錄，不要將資源補到另一個 Codex 目錄。

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

## 補齊相鄰資源

`npx skills add ... --skill '*' --copy` 安裝全部 17 個 skills，但不會複製沒有 `SKILL.md` 的根目錄 `ccf-latex-templates/`。請從與安裝 skills 相同版本的倉庫執行以下命令。這組資源同時補齊部分安裝所需的參考檔案與舊版轉換腳本。僅複製資源不代表安裝或呼叫資源所屬 skill；任務需要它的能力時，仍需另外安裝對應技能。完整倉庫或外掛已保留這些相鄰路徑。

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
