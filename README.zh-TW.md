<div align="center">

# CCFA Skills

### 面向 CCF / ICLR / NeurIPS 風格論文專案的 `ccf-*` 技能家族。

<p>
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong>
</p>

<img src="assets/ccfaskills.png" alt="CCFA Skills 主視覺" width="100%">

</div>

---

CCFA Skills 是一套本地 Codex skill 家族，用來管理論文專案從 idea 到投稿、審稿回覆和重投的完整閉環。v0.4.5 不再把每個小功能拆成獨立 runtime，而是用 13 個 owner skills 承擔清楚職責；壓縮、寫作審稿、引用稽核、會議格式、artifact、報告展示等能力都歸入對應 owner，降低觸發衝突和歧義。

![技能家族邏輯](assets/ccfa-skills-architecture.zh-TW.svg)

## 家族邏輯

預設閉環是：

```text
專案搭建
  -> 流程編排
  -> idea 優化與 idea 審稿
  -> 文獻證據與實驗設計
  -> 按目標會議寫作正文
  -> 科學/寫作審稿與完整性稽核
  -> 投稿包檢查
  -> rebuttal、revision ledger 與可能的重投
```

`ccfa.yaml` 是共享專案狀態。它記錄目標會議、階段、artifacts、claims、experiments、reviews、submission checks 和 revision ledger，讓各個 skill 能聯動，但不互相覆蓋。

![流程](assets/ccfa-skills-workflow.zh-TW.svg)

## 13 個 Runtime Skills

| 階段 | Skill | 負責什麼 | 常見下游 |
| --- | --- | --- | --- |
| 搭建 | `ccf-project-scaffolder` | 建立專案目錄、複製 LaTeX 模板、初始化 `ccfa.yaml`。 | `ccf-pipeline-orchestrator`, `ccf-paper-writer` |
| 規劃 | `ccf-pipeline-orchestrator` | 排階段、定 gate、維護 artifact 狀態、選擇下一個 owner。 | 任意階段 owner |
| Idea | `ccf-idea-optimizer` | 把粗 idea 變成 problem-gap-insight-method-evidence。 | `ccf-idea-reviewer`, `ccf-literature-searcher` |
| Idea gate | `ccf-idea-reviewer` | 嚴格評分、排序、判斷拒稿風險和取捨。 | `ccf-idea-optimizer`, `ccf-experiment-designer` |
| 證據 | `ccf-literature-searcher` | 檢索 prior art、related work、資料集和 benchmark。 | `ccf-experiment-designer`, `ccf-paper-writer` |
| 證據 | `ccf-experiment-designer` | 設計 baseline、metric、消融、真實結果表和圖。 | `ccf-paper-writer`, `ccf-integrity-auditor` |
| 正文 | `ccf-paper-writer` | 起草、潤飾、壓縮、展示材料、按會議 LaTeX 寫稿。 | `ccf-paper-reviewer`, `ccf-submission-checker` |
| 審稿 | `ccf-paper-reviewer` | 科學審稿、寫作審稿、評分、AC/meta-review 風險。 | `ccf-paper-writer`, `ccf-integrity-auditor` |
| 稽核 | `ccf-integrity-auditor` | 核驗 claim、數字、圖表、引用、BibTeX 和上下文支撐。 | `ccf-paper-writer`, `ccf-literature-searcher` |
| 投稿 | `ccf-submission-checker` | 檢查會議規則、PDF/LaTeX、匿名、metadata、artifact。 | `ccf-paper-writer`, `ccf-rebuttal-writer` |
| 回應 | `ccf-rebuttal-writer` | rebuttal、response letter、revision ledger、保守重投。 | `ccf-paper-writer`, `ccf-submission-checker` |
| 治理 | `ccf-common` | 路由、隱私/證據策略、source registry、artifact 合約。 | 全部 CCFA skills |
| 維護 | `ccf-skill-forger` | 維護 skill、文件、生成式 SVG、驗證和 release。 | `ccf-common` |

![Skill 總覽](assets/ccfa-skills-catalog.zh-TW.svg)

## 安裝

完整安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

支援部分安裝，但任何子集都必須包含 `ccf-common`：

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

部分安裝前請看 [INSTALLATION_MATRIX.zh-TW.md](docs/INSTALLATION_MATRIX.zh-TW.md)。

![安裝組合](assets/ccfa-skills-installation.zh-TW.svg)

## 已合併的 Helper 能力

不要再安裝這些舊 runtime 名稱：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。

能力仍然保留，只是歸屬更明確：

| 舊 helper 能力 | 目前 owner |
| --- | --- |
| 壓縮、talk、poster、slides、Q&A | `ccf-paper-writer` |
| 寫作審稿 | `ccf-paper-reviewer` |
| 引用稽核 | `ccf-integrity-auditor` |
| 結果圖表 | `ccf-experiment-designer` |
| artifact 和會議格式檢查 | `ccf-submission-checker` |
| 重投遷移 | `ccf-rebuttal-writer` |
| 文件 SVG 維護 | `ccf-skill-forger` |

![路由邊界](assets/ccfa-skills-routing.zh-TW.svg)

## Venue Guides

會議 LaTeX/template 資訊是 reference，不是 runtime skill：

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

正文寫作走 `ccf-paper-writer`。會議合規、頁數、匿名、PDF metadata、camera-ready 和 artifact 檢查走 `ccf-submission-checker`。從 0 寫稿時，如果使用者指定目標會議，writer 會先讀對應 venue guide；如果沒有指定或找不到目標會議，則回退 NeurIPS 模板。

## Demo

`demo/attention-is-all-you-need/` 是完整 ICLR 風格閉環 demo：讀取 Transformer 原文，提煉動機、問題、insight、方法和結果，進行 idea 審稿，寫出可編譯的完整 LaTeX 論文，完成寫作/科學審稿、完整性稽核、投稿檢查、rebuttal，並記錄家族剩餘問題。

![Attention Demo](assets/ccfa-skills-demo-attention.zh-TW.svg)

## 圖與文件

![Artifacts](assets/ccfa-skills-artifacts.zh-TW.svg)

![審稿邊界](assets/ccfa-skills-review-boundaries.zh-TW.svg)

詳細文件：[SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md)、[ARCHITECTURE.md](docs/ARCHITECTURE.md)、[INSTALLATION_MATRIX.zh-TW.md](docs/INSTALLATION_MATRIX.zh-TW.md)、[NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md)。
