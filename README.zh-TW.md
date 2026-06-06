<h1 align="center">CCFA Skills</h1>

<p align="center"><strong>A practical skill family set for CCF-A research workflows.</strong></p>

<p align="center">
  <a href="README.md">简体中文</a> ·
  <a href="README.en.md">English</a> ·
  <strong>繁體中文</strong>
</p>

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills 主視覺" width="100%">
</p>

---

CCFA Skills 是一套本地 Codex skill 家族，用來覆蓋 CCF-A/ICLR/NeurIPS 風格論文專案從 idea 到投稿、審稿回覆和重投的閉環流程。它不是一堆互相競爭的寫作提示詞，而是一個有明確 owner、artifact 合約和路由邊界的研究工作流系統。

v0.4.5 的核心設計是把 runtime 入口收斂到 13 個 `ccf-*` owner skills。壓縮、寫作審稿、引用稽核、結果圖表、會議格式、artifact、重投遷移、論文報告和文件 SVG 這些舊 helper 能力仍然保留，但不再作為獨立 runtime skill 觸發，避免名稱衝突和職責重疊。

![CCFA 技能家族邏輯](assets/ccfa-skills-architecture.zh-TW.svg)

## 整體鏈路

預設論文專案閉環如下：

```text
專案搭建
  -> 流程編排
  -> idea 優化
  -> idea 審稿
  -> 文獻檢索
  -> 實驗設計
  -> 會議感知寫作
  -> 科學/寫作審稿
  -> 完整性稽核
  -> 投稿包檢查
  -> rebuttal / revision ledger / resubmission
```

每個階段只交給一個 owner skill。這樣做的目的不是減少功能，而是讓觸發條件、輸出格式和 artifact 歸屬更穩定：寫作由 writer 負責，判斷由 reviewer 負責，事實核驗由 auditor 負責，投稿包由 submission checker 負責，回應審稿人由 rebuttal writer 負責。

`ccfa.yaml` 是共享專案狀態檔。它記錄 `target_venue`、`stage`、`artifacts`、`claims`、`experiments`、`reviews`、`revision_ledger` 和 `submission_checks`，讓各個 skill 可以聯動，但不會互相覆蓋正文、實驗表、審稿報告或 rebuttal。

![端到端流程](assets/ccfa-skills-workflow.zh-TW.svg)

## 13 個 Runtime Skills

| 階段 | Skill | 啟動條件 | 主要產物 | 不應該用於 |
| --- | --- | --- | --- | --- |
| 專案搭建 | `ccf-project-scaffolder` | 使用者要建立論文專案目錄、複製模板、初始化 `ccfa.yaml`。 | 專案目錄、模板檔、初始狀態檔。 | 生成研究內容或替使用者寫 idea。 |
| 流程編排 | `ccf-pipeline-orchestrator` | 使用者要拆任務、排階段、設 gate、決定下一步 owner。 | 階段計畫、gate、handoff、狀態更新建議。 | 直接寫作、審稿、檢索、設計實驗或 rebuttal。 |
| Idea 優化 | `ccf-idea-optimizer` | 使用者有粗 idea、模糊方向、待具體化的問題。 | problem-gap-insight-method-evidence 文件。 | 對多個 idea 排名打分。 |
| Idea 審稿 | `ccf-idea-reviewer` | 使用者明確要求評分、排名、嚴格審稿、判斷創新性或取捨。 | 分數、風險、最近 prior art 風險、修改建議。 | 繼續發散優化單個 idea。 |
| 文獻證據 | `ccf-literature-searcher` | 使用者要查 related work、prior art、資料集、benchmark 或引用證據。 | 文獻列表、篩選理由、相關工作結構、證據缺口。 | 只核驗已經寫進論文的引用。 |
| 實驗設計 | `ccf-experiment-designer` | 使用者要設計 baseline、metric、消融、魯棒性實驗或結果表。 | 實驗協議、baseline 矩陣、結果表模板、真實結果圖表。 | 編造結果或繪製文件架構圖。 |
| 論文寫作 | `ccf-paper-writer` | 使用者要寫、潤飾、壓縮、改寫、從 idea 起草 LaTeX、做 slides/poster/talk。 | 論文正文、保留格式的修改稿、壓縮稿、展示材料。 | 完整審稿、事實稽核、投稿包檢查或 rebuttal。 |
| 論文審稿 | `ccf-paper-reviewer` | 使用者要科學審稿、寫作審稿、評分、AC/meta-review 或投稿風險診斷。 | 科學審稿、寫作審稿、風險表、評分和修改優先級。 | 直接替換正文或寫 rebuttal。 |
| 完整性稽核 | `ccf-integrity-auditor` | 使用者要核驗 claim、數字、圖表、引用、BibTeX 和上下文支撐。 | claim-support 表、數字一致性報告、引用稽核。 | broad literature search 或完整科學審稿。 |
| 投稿檢查 | `ccf-submission-checker` | 使用者要查會議規則、頁數、匿名、PDF metadata、artifact、camera-ready。 | 投稿包檢查、LaTeX/PDF 構建結果、匿名和 artifact checklist。 | 潤飾正文內容。 |
| 審稿回覆 | `ccf-rebuttal-writer` | 使用者要寫 rebuttal、response letter、revision ledger 或重投計畫。 | rebuttal 文案、逐條回應、revision ledger、resubmission plan。 | 普通論文寫作。 |
| 共享治理 | `ccf-common` | 維護路由、隱私/證據策略、source registry、artifact contract。 | 公共規則、路由表、source registry、校驗策略。 | 普通研究任務。 |
| 家族維護 | `ccf-skill-forger` | 維護 skill、命名、docs、SVG、校驗、release。 | 更新後的技能文件、文件、圖、驗證結果和發布提交。 | 研究寫作、審稿或實驗設計。 |

![Runtime skill 總覽](assets/ccfa-skills-catalog.zh-TW.svg)

## 觸發邊界

| 使用者真正要做的事 | 使用 | 不使用 |
| --- | --- | --- |
| 把模糊 idea 變成可做的研究方案 | `ccf-idea-optimizer` | `ccf-idea-reviewer` |
| 對多個 idea 打分、排序、取捨 | `ccf-idea-reviewer` | `ccf-idea-optimizer` |
| 找新文獻、找 benchmark、找資料集 | `ccf-literature-searcher` | `ccf-integrity-auditor` |
| 核驗論文裡已引用文獻是否支撐 claim | `ccf-integrity-auditor` | `ccf-literature-searcher` |
| 設計實驗和結果表 | `ccf-experiment-designer` | `ccf-paper-writer` |
| 寫正文、潤飾、壓縮、保持原格式改寫 | `ccf-paper-writer` | `ccf-paper-reviewer` |
| 判斷論文能否被接收、哪裡會被拒 | `ccf-paper-reviewer` | `ccf-paper-writer` |
| 檢查頁數、匿名、PDF、metadata、artifact | `ccf-submission-checker` | `ccf-paper-writer` |
| 回覆審稿人和維護 revision ledger | `ccf-rebuttal-writer` | `ccf-paper-reviewer` |
| 改文件圖、維護 skill、發 release | `ccf-skill-forger` | `ccf-experiment-designer` |

![路由邊界](assets/ccfa-skills-routing.zh-TW.svg)

## 已合併的 Helper 能力

這些舊名稱不要再作為獨立 runtime skills 安裝：

```text
ccf-workflow-planner
ccf-paper-compressor
ccf-writing-reviewer
ccf-citation-auditor
ccf-figure-table-builder
ccf-artifact-packager
ccf-venue-format-guide
ccf-resubmission-adapter
ccf-paper-presenter
ccf-doc-diagram-designer
```

| 已合併能力 | 目前 owner | 原因 |
| --- | --- | --- |
| workflow planning | `ccf-pipeline-orchestrator` | 規劃和編排必須共享同一個階段狀態。 |
| compression、slides、poster、talk、Q&A | `ccf-paper-writer` | 都屬於論文文本或論文派生文本。 |
| writing review | `ccf-paper-reviewer` | 它是審稿模式，不是寫作模式。 |
| citation audit | `ccf-integrity-auditor` | 核驗引用屬於事實完整性。 |
| figure/table builder | `ccf-experiment-designer` | 結果圖表必須綁定真實實驗結果。 |
| artifact packager、venue format guide | `ccf-submission-checker` | 都屬於投稿包 readiness。 |
| resubmission adapter | `ccf-rebuttal-writer` | 重投需要基於 reviewer response 和 revision ledger。 |
| docs SVG designer | `ccf-skill-forger` | 文件圖是家族維護，不是論文實驗圖。 |

## Artifact 合約

CCFA 的 artifact 設計是為了避免 skill 互相覆蓋。

| Artifact | 主要 owner | 其他 skill 如何使用 |
| --- | --- | --- |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | 讀取階段、目標會議、產物狀態和 gate。 |
| idea brief | `ccf-idea-optimizer` | reviewer 評分，writer 用於正文 story。 |
| idea review | `ccf-idea-reviewer` | optimizer 和 experiment designer 用於修正方向。 |
| literature notes | `ccf-literature-searcher` | writer 寫 related work，auditor 檢查引用支撐。 |
| experiment plan/results | `ccf-experiment-designer` | writer 寫實驗，auditor 查數字一致性。 |
| manuscript | `ccf-paper-writer` | reviewer/auditor/submission checker 只診斷或檢查。 |
| review report | `ccf-paper-reviewer` | writer 修稿，rebuttal writer 提取回應點。 |
| integrity report | `ccf-integrity-auditor` | writer 修 claim，literature searcher 補證據。 |
| submission check | `ccf-submission-checker` | writer 修格式，rebuttal writer 準備後續版本。 |
| revision ledger | `ccf-rebuttal-writer` | orchestrator 追蹤 reviewer comment 到 action 的閉環。 |

![Artifact 合約](assets/ccfa-skills-artifacts.zh-TW.svg)

## 寫作與審稿輸出原則

- 寫作、潤飾、壓縮、presentation 任務應服從使用者要求的輸出格式。
- 使用者給 LaTeX 就保持 LaTeX，給 Markdown 就保持 Markdown。
- 使用者只有 idea 且要求從 0 寫文章時，`ccf-paper-writer` 先讀取目標會議 venue guide；如果沒有目標會議或找不到 guide，回退 NeurIPS 模板。
- 非 review 類 skill 應該靈活、資訊密度高，產出具體 artifact，而不是空泛流程說明。
- review、audit、submission gate 可以保持嚴格結構，因為它們的價值是可追蹤的判斷、風險和 pass/fail 檢查。
- 所有 skill 都不能編造實驗結果、引用、官方規則或 reviewer 結論。

![審稿、稽核與行動邊界](assets/ccfa-skills-review-boundaries.zh-TW.svg)

## Venue Guides

會議 LaTeX/template 資訊是 reference，不是 runtime skill：

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

| 場景 | 使用 |
| --- | --- |
| 按 ICLR/NeurIPS/CVPR 等目標會議寫正文 | `ccf-paper-writer` 先讀 venue guide，再寫正文。 |
| 檢查頁數、匿名、PDF metadata、camera-ready、artifact | `ccf-submission-checker`。 |
| 只問某會議 LaTeX/template/page limit | `ccf-submission-checker`，必要時讀取 venue guide。 |
| 找不到目標會議 guide | `ccf-paper-writer` 預設回退 NeurIPS 模板，並提示最終投稿前需重新核驗。 |

## 安裝

完整安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

部分安裝必須包含 `ccf-common`：

```bash
skills=(ccf-common ccf-paper-writer ccf-paper-reviewer ccf-submission-checker)
mkdir -p "$CODEX_HOME/skills"
for s in "${skills[@]}"; do cp -R "$s" "$CODEX_HOME/skills/"; done
```

PowerShell：

```powershell
$skills = @("ccf-common", "ccf-paper-writer", "ccf-paper-reviewer", "ccf-submission-checker")
New-Item -ItemType Directory -Force "$env:CODEX_HOME\skills" | Out-Null
foreach ($s in $skills) { Copy-Item -Recurse -Force $s "$env:CODEX_HOME\skills\" }
```

| 組合 | 包含 | 適合 |
| --- | --- | --- |
| 全流程 | 13 個 runtime skills | 從 idea 到 rebuttal 的完整論文專案。 |
| 寫作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 起草、潤飾、寫作審稿、格式檢查。 |
| 早期研究子集 | `ccf-common`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-searcher`, `ccf-experiment-designer` | 寫正文前的 idea、文獻和實驗設計。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 已有稿件的完整性和投稿包檢查。 |
| 維護子集 | `ccf-common`, `ccf-skill-forger` | 維護技能、文件、SVG 和 release。 |

![安裝組合](assets/ccfa-skills-installation.zh-TW.svg)

## Demo

`demo/attention-is-all-you-need/` 是一個 ICLR 風格閉環 demo，用原始 Transformer 論文展示 CCFA 家族如何從原文思路提煉、idea 審稿、LaTeX 寫作、寫作/科學審稿、完整性稽核、投稿檢查走到 rebuttal。demo 是示例，不是必須閱讀的入口。

![Attention demo](assets/ccfa-skills-demo-attention.zh-TW.svg)

## 維護與驗證

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_markdown_links.py
python ccf-common/scripts/check_sources.py
python ccf-common/scripts/check_path_privacy.py .
python tools/build_ccfa_diagrams.py
```
