<div align="center">

# CCFA Skills

### 面向 CCF 論文專案的 `ccf-*` 技能家族。

<p>
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong>
</p>

</div>

---

CCFA Skills 是一組本地 Codex skills，用於 CCF 風格論文專案的建構、稽核、投稿、修訂、重投和簡報。v0.4.0 將倉庫從「寫作技能集合」升級為「論文專案工作流家族」：新增路由治理、artifact 合約、venue guide 分支、結構校驗、插件清單和發布文件。

設計參考了 ARS、nature-skills 和 ARIS，但 CCFA 更強調職責邊界：idea 優化不是完整審稿，引用稽核不是文獻檢索，會議格式查詢不是論文寫作，投稿檢查不是正文潤飾。

![架構](assets/ccfa-skills-architecture.zh-TW.svg)

## 安裝

保留手動安裝方式：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cp -r CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

已有本地倉庫時：

```bash
git pull origin main
cp -r ccf-* "$CODEX_HOME/skills/"
```

倉庫也提供 `.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json`，供支援插件安裝的客戶端使用。手動複製方式仍保留，因為它能清楚顯示本地實際安裝了哪些 skills。

## v0.4 架構

| 層級 | 作用 | 主要文件 |
| --- | --- | --- |
| 治理層 | 路由、觸發註冊表、隱私與證據策略、source registry、artifact 歸屬、校驗。 | `ccf-common/`, `docs/SKILLS_CATALOG.md`, `AGENT_GUIDE.md` |
| 專案狀態層 | 建立並維護論文專案結構和 `ccfa.yaml`。 | `ccf-paper-project-scaffold`, `ccf-pipeline-orchestrator` |
| 研究鏈路層 | idea、文獻、實驗、寫作、壓縮、審稿、rebuttal、重投和簡報。 | `ccf-*` skills |
| Venue 分支 | 會議 LaTeX、template、page limit、匿名和 camera-ready 規則。 | `ccf-conference-guides`, `ccf-writing-skills/references/venue-guides/` |
| 發布校驗層 | 前綴、frontmatter、shared controls、registry、venue index、SVG、source、路徑隱私。 | `.github/workflows/validate.yml`, `ccf-common/scripts/` |

## 核心鏈路

```text
ccf-brainstorming
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-search
  -> ccf-experiment-designer
  -> ccf-writing-skills
  -> ccf-paper-compressor
  -> ccf-conference-reviewer
  -> ccf-conference-writing-reviewer
  -> ccf-conference-paper-rebuttal
```

v0.4 新增：

```text
ccf-pipeline-orchestrator
ccf-paper-project-scaffold
ccf-integrity-auditor
ccf-citation-auditor
ccf-submission-checker
ccf-figure-table-builder
ccf-artifact-reproducibility
ccf-revision-ledger
ccf-resubmission-adapter
ccf-paper-talk
ccf-conference-guides
ccf-forge-skills
```

完整觸發條件、排除邊界和聯動關係見 `docs/SKILLS_CATALOG.md`。

## Venue 分支

`ccf-conference-skills/<venue>/SKILL.md` 不再作為可安裝 runtime skill 層存在。原 109 個會議 skill 已遷移到：

```text
ccf-writing-skills/references/venue-guides/index.md
ccf-writing-skills/references/venue-guides/<venue>.md
```

以下任務使用 `ccf-conference-guides`：

- CVPR page limit
- NeurIPS LaTeX template
- SIGMOD 匿名模式
- camera-ready checklist
- supplementary material 規則

論文正文寫作使用 `ccf-writing-skills`，寫作/格式審查使用 `ccf-conference-writing-reviewer`，投稿包建構和合規檢查使用 `ccf-submission-checker`。最終投稿前仍必須核對當年官方 venue policy。

![流程](assets/ccfa-skills-workflow.zh-TW.svg)

## `ccfa.yaml`

v0.4 引入共享專案狀態文件，固定頂層欄位為：

```text
version
project
target_venue
stage
artifacts
claims
experiments
reviews
revision_ledger
submission_checks
```

`ccf-paper-project-scaffold` 負責建立，`ccf-pipeline-orchestrator` 可以更新階段和 gate，其他 skills 按 `ccf-common/references/artifact-contracts.md` 讀取或提出更新建議。

## 校驗

發布前執行：

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_path_privacy.py .
python ccf-common/scripts/check_sources.py
rg -nP "^name: (?!ccf-)" -g "SKILL.md"
```

GitHub Actions 會在 push 和 pull request 上執行同類結構校驗。

![評審邊界](assets/ccfa-skills-review-boundaries.zh-TW.svg)

## 相容變更

- 所有可安裝 skill 名稱均使用 `ccf-` 前綴。
- `forge-skills` 已重命名為 `ccf-forge-skills`。
- 核心研究鏈路名稱保持穩定。
- 舊 venue runtime skills 已移除；使用 `ccf-conference-guides` 和 venue-guide reference 分支。
- `SKILL.md` 是最高優先級。如果文件、catalog 或 routing 與 skill body 衝突，應修正文件索引。
