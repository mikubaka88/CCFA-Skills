<h1 align="center">CCFA Skills</h1>

<p align="center"><strong>A skill family for shaping the research storyline of CCF-A papers.</strong></p>

<p align="center">
  <a href="README.md">简体中文</a> ·
  <a href="README.en.md">English</a> ·
  <strong>繁體中文</strong>
</p>

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills 主視覺" width="100%">
</p>

---

<div align="center">
  <p>
    <span style="color:#334155"><em>"The structure of the prose becomes the structure of the scientific argument."</em></span><br>
    <sub>George D. Gopen and Judith A. Swan, <a href="https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html"><em>The Science of Scientific Writing</em></a></sub>
  </p>
  <p>
    <span style="color:#2563eb"><em>"The very process of science is centered around communication."</em></span><br>
    <sub>Yann LeCun and James M. Manyika, <a href="https://www.amacad.org/publication/daedalus/learning-abstractions-conversation-yann-lecun"><em>Learning Abstractions</em></a></sub>
  </p>
</div>

一篇高水準論文真正重要的，往往不是最後那份 PDF，而是貫穿其後的研究故事線。它從一個尚不穩定的 idea 開始，在文獻中尋找位置，在實驗中接受檢驗，在寫作中被組織成可被審稿人理解的論證，又在審稿和 rebuttal 中繼續被修正。真正困難的地方，不只是寫出某一段 introduction，而是讓 idea、證據、實驗、表達和回應始終指向同一個研究問題。

CCFA Skills 正是從這個觀察出發。它把 CCF-A 論文專案看作一條可以被維護、稽核和反覆推進的研究故事線，而不是一次性的文本生成任務。一個 idea 需要先被塑形，在真正需要取捨時再接受嚴格審稿；一組實驗需要服務於明確 claim，而不是孤立地填滿表格；一篇論文的寫作需要保留證據邊界；一次 rebuttal 也不應只是臨時答辯，而應成為下一輪修改和重投的可追蹤記錄。

這個專案的核心 insight 是：論文品質來自連續決策的品質。寫作、審稿、稽核、投稿檢查和 rebuttal 不應該互相替代，而應該各自保持邊界，並在同一個專案狀態中交接。v0.5 因此將家族收斂為 15 個階段角色，讓每個階段都有清楚的責任，讓每個 artifact 都能找到歸屬，也讓整套系統更像一個圍繞研究故事線展開的協作框架，而不是鬆散的 prompt 集合。

![CCFA 技能家族邏輯](assets/ccfa-skills-architecture.zh-TW.svg)

## 整體鏈路

預設論文專案閉環如下：

```text
專案搭建
  -> 流程編排
  -> idea 優化
  -> idea 審稿
  -> 文獻監控 / 競品追蹤
  -> 文獻檢索
  -> 實驗設計
  -> 寫作範例抽取（可選）
  -> 會議感知寫作
  -> 科學/寫作審稿
  -> 完整性稽核
  -> 投稿包檢查
  -> rebuttal / revision ledger / resubmission
```

每個階段只交給一個 owner skill。這樣做的目的不是減少功能，而是讓觸發條件、輸出格式和 artifact 歸屬更穩定：寫作由 writer 負責，判斷由 reviewer 負責，事實核驗由 auditor 負責，投稿包由 submission checker 負責，回應審稿人由 rebuttal writer 負責。

`ccfa.yaml` 是共享專案狀態檔。它記錄 `target_venue`、`stage`、`artifacts`、`claims`、`experiments`、`reviews`、`revision_ledger` 和 `submission_checks`，讓各個 skill 可以聯動，但不會互相覆蓋正文、實驗表、審稿報告或 rebuttal。

![端到端流程](assets/ccfa-skills-workflow.zh-TW.svg)

## 15 個 Runtime Skills

| 階段 | Skill | 啟動條件 | 主要產物 | 不應該用於 |
| --- | --- | --- | --- | --- |
| 專案搭建 | `ccf-project-scaffolder` | 使用者要建立論文專案目錄、複製模板、初始化 `ccfa.yaml`。 | 專案目錄、模板檔、初始狀態檔。 | 生成研究內容或替使用者寫 idea。 |
| 流程編排 | `ccf-pipeline-orchestrator` | 使用者要拆任務、排階段、設 gate、決定下一步 owner。 | 階段計畫、gate、handoff、狀態更新建議。 | 直接寫作、審稿、檢索、設計實驗或 rebuttal。 |
| Idea 優化 | `ccf-idea-optimizer` | 使用者有粗 idea、模糊方向、想找方向或救方向。 | problem-gap-insight-method-evidence 文件、救援路線、最小可驗證問題。 | 對多個 idea 排名打分。 |
| Idea 審稿 | `ccf-idea-reviewer` | 使用者明確要求評分、排名、嚴格審稿、判斷創新性或取捨。 | 分數、風險、stage-aware 發展潛力、修改建議。 | 繼續發散優化單個 idea。 |
| 文獻監控 | `ccf-literature-monitor` | 使用者要追蹤新論文、競品、arXiv/OpenReview/會議動態，或問最近有沒有類似 idea。 | 監控報告、overlap level、RELAX/RESEARCH/FOLLOW-UP 標記、跨 skill handoff。 | 系統性 related work 檢索、引用稽核或最終 idea 打分。 |
| 文獻證據 | `ccf-literature-searcher` | 使用者要查 related work、prior art、資料集、benchmark、open gap 或引用證據。 | 文獻列表、篩選理由、相關工作結構、機會圖、證據缺口。 | 只核驗已經寫進論文的引用，或把 related work 當成最終否決。 |
| 實驗設計 | `ccf-experiment-designer` | 使用者要設計 baseline、metric、消融、魯棒性實驗或結果表。 | 實驗協議、baseline 矩陣、結果表模板、真實結果圖表。 | 編造結果或繪製文件架構圖。 |
| 寫作範例 | `ccf-paper-to-exemplar` | 使用者提供論文 PDF，希望抽取成可複用寫作範例或個人 exemplar 庫。 | exemplar card、寫作 pattern、venue 標籤、writer 可用索引。 | 直接寫論文或進行審稿。 |
| 論文寫作 | `ccf-paper-writer` | 使用者要寫、潤飾、壓縮、改寫、從 idea 起草 LaTeX、按目標會議篇幅成稿、做 slides/poster/talk。 | 論文正文、保留格式的修改稿、壓縮稿、篇幅預算、展示材料。 | 完整審稿、事實稽核、投稿包檢查或 rebuttal。 |
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
| 把模糊 idea 變成可做的研究方案，或找救援路線 | `ccf-idea-optimizer` | `ccf-idea-reviewer` |
| 明確要對多個 idea 打分、排序、取捨 | `ccf-idea-reviewer` | `ccf-idea-optimizer` |
| 監控新論文、競品、最近是否有類似 idea | `ccf-literature-monitor` | `ccf-literature-searcher` |
| 找新文獻、找 benchmark、找資料集、找 open gap | `ccf-literature-searcher` | `ccf-integrity-auditor` |
| 核驗論文裡已引用文獻是否支撐 claim | `ccf-integrity-auditor` | `ccf-literature-searcher` |
| 設計實驗和結果表 | `ccf-experiment-designer` | `ccf-paper-writer` |
| 把 PDF 論文轉成寫作範例 | `ccf-paper-to-exemplar` | `ccf-paper-writer` |
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
- 使用者只有 idea 且要求從 0 寫文章時，`ccf-paper-writer` 先讀取目標會議 venue guide 和篇幅預算；如果沒有目標會議或找不到 guide，回退 NeurIPS 模板。
- 投稿式完整稿件不能只求可編譯：應接近目標會議主文篇幅，短太多要擴寫，超出篇幅再由 writer 的 compression 模式壓縮，最後交給 `ccf-submission-checker` 檢查頁數。
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
| 全流程 | 15 個 runtime skills | 從 idea 到 rebuttal 的完整論文專案。 |
| 寫作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 起草、潤飾、寫作審稿、格式檢查。 |
| 監控子集 | `ccf-common`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 追蹤新論文、競品和 novelty 風險。 |
| 早期研究子集 | `ccf-common`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 寫正文前的 idea、文獻監控、文獻檢索和實驗設計。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 已有稿件的完整性和投稿包檢查。 |
| 維護子集 | `ccf-common`, `ccf-skill-forger` | 維護技能、文件、SVG 和 release。 |

![安裝組合](assets/ccfa-skills-installation.zh-TW.svg)

## 進一步閱讀

如果你想理解這個家族為什麼這樣設計，建議按下面順序閱讀：

| 文件 | 適合什麼時候看 |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | 想理解主鏈路、治理層、artifact 狀態和 revision loop。 |
| [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md) | 想查每個 skill 的啟動條件、邊界和容易誤觸發的場景。 |
| [docs/INSTALLATION_MATRIX.zh-TW.md](docs/INSTALLATION_MATRIX.zh-TW.md) | 想只安裝部分 skills，判斷哪些必須裝、哪些不能單獨裝。 |
| [docs/NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md) | 想理解為什麼合併 helper skills，以及命名如何減少衝突。 |
| [AGENT_GUIDE.md](AGENT_GUIDE.md) | 給 agent 使用的操作指南，說明如何選擇 owner、交接 artifact、避免覆蓋。 |
| [demo/attention-is-all-you-need/](demo/attention-is-all-you-need/) | 想看一個完整 ICLR 風格閉環示例。 |

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
