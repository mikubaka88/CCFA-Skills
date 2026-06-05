<div align="center">

# CCFA Skills

### 面向 CCF-A 研究流程的實用 skill 集合。

<p>
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong>
</p>

</div>

---

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">
</p>

## 專案定位

CCFA Skills 是一組服務 CCF-A 研究流程的本地 skills。它幫助把粗糙想法推進到可以投稿的論文：先澄清任務，再打磨 idea、查相關工作、設計實驗、寫作和壓縮論文、投稿前審查，並在審稿後組織回應。

這個倉庫不綁定某一個模型或互動介面。文件採用 `SKILL.md` 結構，可用於支援本地 skill 的 agent 環境。核心內容是可複用的 Markdown 工作流、評分標準、檢查表、venue 說明、模板和參考材料。

## 研究前提

許多研究專案在開始寫作前就已經變得難以防守。問題往往出在更早的研究鏈條：

```text
問題 -> 缺口 -> 挑戰 -> 洞察 -> 方法 -> 證據 -> 主張
```

當其中某一環薄弱時，後續潤色常常只是把問題藏起來，而不是解決它。模糊的 gap 會變成模糊的引言；缺少機制的方法會變成元件列表；不能檢驗中心主張的實驗會變得難以解釋。

CCFA Skills 的原則很簡單：儘早找到薄弱環節，把問題說清楚，再轉化為下一步研究行動。整體風格偏克制：新穎性要有依據，方法要有機制，主張要有證據，表達要有邊界。

## 系統架構

這個家族按照研究流程分層組織。

| 層級 | 目的 | Skills |
| --- | --- | --- |
| **Intake Layer** | 澄清目標、約束、工作流選項，並為複雜請求選擇下一步 CCFA skill。 | `ccf-brainstorming` |
| **Idea Layer** | 在寫作前塑形並評估研究方向。 | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| **Evidence Layer** | 檢索相關文獻，並設計不編造結果的實驗方案。 | `ccf-literature-search`, `ccf-experiment-designer` |
| **Manuscript Layer** | 將可行方向發展為連貫的 CCF-A 論文，並按篇幅限制壓縮。 | `ccf-writing-skills`, `ccf-paper-compressor` |
| **Review Layer** | 投稿前審查論文內容，模擬 reviewer 問題，並檢查寫作、格式和 LaTeX。 | `ccf-conference-reviewer`, `ccf-conference-writing-reviewer` |
| **Response Layer** | 將審稿意見轉化為清晰回應和修改承諾。 | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | 建立、改進、校驗和治理 skill 模組。 | `forge-skills`, `ccf-common` |

推薦按任務路由，而不是讓所有模組同時參與。`ccf-common/references/routing.md` 定義每類任務的歸屬，避免 idea 優化、idea 評分、文獻檢索、實驗設計、論文寫作、篇幅壓縮、論文審查、寫作評審、rebuttal 和 skill 維護處理同一類請求。

跨 skill handoff 由 `metadata.ccf_skill_controls.handoff_question_mode` 控制：

- **PARTIAL (Recommended)：** 只在跨研究階段、可能改變 idea scope、進入正式 reviewer/rebuttal 模組、聯網處理敏感材料、或生成可複用文件時詢問。
- **FULL：** 任何可選 sibling-skill handoff 前都詢問。
- **OFF：** 不詢問，按路由自動使用需要的 sibling skill；仍然尊重使用者 denylist 和 writing-only 的 idea-scope 保護。

```text
raw idea
  -> ccf-brainstorming                           ：複雜或多階段請求的可選上游澄清
  -> ccf-idea-optimizer                           ：問題 / 方法 / 證據成形
  -> ccf-idea-reviewer                            ：當使用者要求評分/排序時做聯網檢索支撐的嚴格問題-方法門控
  -> ccf-literature-search                        ：需要當前文獻、資料集或 benchmark 時使用
  -> ccf-experiment-designer                      ：設計 baseline / ablation / 結果填寫表
       如果薄弱但可修復且 handoff 允許            ：回到 optimizer 做定向修復
       如果根本不匹配                            ：換方向或停止投入
       如果已經可發展且 handoff 允許             ：進入寫作模組

writing request
  -> ccf-writing-skills                           ：預設 writing-only
       修改 idea scope 需要明確確認              ：否則只標註 Idea-level risk
       篇幅/頁數壓縮按 handoff mode 執行          ：ccf-paper-compressor
       完整論文評審按 handoff mode 執行           ：ccf-conference-reviewer
       寫作 / LaTeX 評審按 handoff mode 執行      ：ccf-conference-writing-reviewer

使用者明確要求 rebuttal 或真實審稿意見到來
  -> ccf-conference-paper-rebuttal                ：作者回應和修改承諾
       改論文或做 review-risk 診斷               ：按 handoff mode 執行
```

**Writing-only mode。** `ccf-writing-skills` 預設不修改研究主題、核心問題、方法機制、實驗設定、結果數值和結論方向。它只改表達、結構、故事線、claim-evidence 對齊和 reviewer-facing 包裝。即使 idea 修改看起來有幫助，也必須先得到明確確認。

**Session denylist。** 如果使用者說不使用某個 skill，該 skill 在目前對話中就被禁用。助手不能繞過這個決定去模擬被禁用模組；只能使用本模組內部的簡短風險掃描、行動列表或 writing-only checklist。

**Task modes。** CCFA Skills 支援 `quick` 和 `standard` 兩種模式。`quick` 用於單段潤色、局部風險檢查、小規模文獻 sanity scan、快速實驗草圖或局部壓縮，不強制完整 checklist。`standard` 是完整章節、整篇論文 review、文獻檢索資料夾、實驗方案、score-risk loop 和可複用文件的預設模式。

因此，第二次出現 `ccf-idea-optimizer` 不是重複。第一次 optimizer 負責把粗糙方向整理到「可以被判斷」的狀態；後續在 reviewer 診斷後，只有 handoff mode 允許時才會進入定向修復。`ccf-conference-paper-rebuttal` 被隔離在預設投稿前閉環之外，只有使用者明確要求 rebuttal、作者回應、response letter 或審稿意見回覆時才使用。

<p align="center">
  <img src="assets/ccfa-skills-architecture.zh-TW.svg" alt="CCFA Skills 工作流門控" width="100%">
</p>

<p align="center">
  <img src="assets/ccfa-skills-workflow.zh-TW.svg" alt="CCFA Skills 逐步工作流" width="100%">
</p>

<p align="center">
  <img src="assets/ccfa-skills-review-boundaries.zh-TW.svg" alt="CCFA Skills 評審邊界圖" width="100%">
</p>

這套結構把投稿前最關鍵的問題拆開處理：新穎性、重要性、可靠性、證據、清晰度、可復現性和 venue fit。每個 skill 負責一類問題，同時保留它們之間的依賴關係。

## Skill 家族

### `ccf-brainstorming`

在進入下游研究工作前澄清複雜請求。它把模糊目標整理成簡短 research brief：需要做的決定、目標受眾、既有輸入、約束、成功標準、工作流選項和推薦的下一步 CCFA skill。

它只在需要時使用。適合頭腦風暴、需求澄清、任務拆解、研究路線討論或 design brief，然後再選擇下游 skill。

### `ccf-idea-optimizer`

將早期研究方向轉化為結構化研究方案：任務、gap、根本挑戰、核心洞察、方法機制、貢獻類型、證據計畫和風險。

它適合處理「有潛力但尚未成形」的想法。這個 skill 會追問：專案真正想證明什麼，方法依賴什麼假設，什麼證據能讓主張可信，以及哪個學術共同體會認為這項工作有意義。

### `ccf-idea-reviewer`

在論文尚未形成之前評價問題和方法。標準模式會先用 public-safe 查詢檢索相近工作，再對照既有工作判斷新穎性，並從領域、方法、實驗、venue 和 prior art 等視角給出意見。

它的目標是給出具體、專業、偏嚴格的評閱意見。它會區分「新穎性確實不足」和「還沒有查清楚」，也會區分可修復問題與需要換方向的問題。主要批評會說明對應的主張、證據依據、潛在 reviewer 關切和具體修復條件。

### `ccf-literature-search`

聯網檢索相關的高品質文獻，篩掉低品質或不合適來源，分類 paper type，評分文章品質，並寫入包含標題、連結、評分、文章類型和備註的 literature-search 資料夾。

它主要聯動 Related Work、Introduction、idea 優化、idea 評審、實驗設計和 reviewer-risk 診斷。純 benchmark 論文會單獨標記，而不是按方法論文標準扣分。

### `ccf-experiment-designer`

設計 CCF-A 實驗方案：資料集、benchmark、baseline、ablation、metric、robustness test、failure analysis 和結果填寫表。

它不會替使用者生成實驗數值。缺少數值時，只提供給使用者填寫的表格模板，並標註每個實驗回答哪個 reviewer 問題。

### `ccf-writing-skills`

將成熟 idea 發展為論文級論證。它處理故事線、章節規劃、段落角色、claim-evidence map、venue 適配、寫作樣例和修改優先級。

它最重視一致性：摘要、引言、方法、實驗、侷限性和結論應該以不同解析度講述同一個研究故事。

### `ccf-paper-compressor`

按照頁數或字數目標壓縮論文段落、章節或全文，同時保護故事線、主張、證據、結果數值和侷限性。

它可以用 quick mode 做局部壓縮，也可以用 standard mode 做整節或整篇壓縮。涉及「放附錄還是刪除」的策略選擇時，它會詢問一次，然後一致執行。

### `ccf-conference-reviewer`

負責完整論文評審。它執行 desk check、public-safe 相關工作搜尋、新穎性/可靠性/證據評審、多 reviewer 模擬、AC/meta-review、校準分數和問題表，並在 standard 模式生成固定格式 Markdown 審稿報告。

報告格式參考本地 CSPaper 風格，並擴展 claim-evidence audit、實驗/可復現性檢查、reviewer panel、AC 綜合、分數調整條件和後續行動建議。

### `ccf-conference-writing-reviewer`

這是寫作與格式審查模組。它逐段閱讀論文，檢查故事線、LaTeX/格式、claim-evidence 展示、全文一致性、圖表敘事和貢獻展示，並把每個問題轉化為帶位置的修改建議。

它不負責完整論文評審、AC/meta-review 或論文評分；這些請求路由到 `ccf-conference-reviewer`。

### `ccf-conference-paper-rebuttal`

支援審稿後的作者回應。它整理審稿意見，合併重複關切，選擇回應策略，起草簡潔回覆，並可配合 TeX response templates。

它的原則很直接：回答關切，澄清誤解，承認合理邊界，避免不可兌現的承諾。

### `forge-skills`

提供構建和維護 skills 的工程層。它覆蓋命名、結構、資源組織、校驗和觸發設計。

它讓這個家族保持可擴展：新的領域 skill 可以被加入，而不需要把整個倉庫變成一個巨大的說明文件。

### `ccf-common`

提供 CCFA 家族的共享控制層，包括路由、handoff 模式、私有材料安全、source registry 和 venue-family map。它不是普通研究寫作 skill，而是由維護者和兄弟 skill 載入，用來保持行為一致。

## 這個家族優化什麼

| 目標 | 含義 |
| --- | --- |
| **問題精度** | 論文應命名真實瓶頸，而不只是說明現有方法不足。 |
| **機制清晰度** | 方法應解釋為什麼有效，而不只是列出元件。 |
| **新穎性校準** | 原創性主張應與相近工作對照；未檢索時應標記不確定性。 |
| **證據對齊** | 實驗、證明、使用者研究或系統評估應檢驗中心主張。 |
| **Venue fit** | 論證方式應能被目標學術共同體理解和評價。 |
| **修改連續性** | 批評應轉化為清晰行動列表，而不是零散建議。 |

## 安裝

請複製完整 skill 目錄，而不只是複製 `SKILL.md`。多個模組依賴 `references/`、`assets/`、模板以及跨 skill 的相對路徑引用。可安裝的目錄包括：

```text
ccf-brainstorming
ccf-idea-optimizer
ccf-idea-reviewer
ccf-literature-search
ccf-experiment-designer
ccf-writing-skills
ccf-paper-compressor
ccf-conference-reviewer
ccf-conference-writing-reviewer
ccf-conference-paper-rebuttal
ccf-conference-skills
ccf-latex-templates
ccf-common
forge-skills
```

### 1. Codex

Codex-style 本地 skill 環境通常從 `~/.codex/skills/` 讀取 skills。如果你使用自訂 `$CODEX_HOME`，請把這些目錄放到 `$CODEX_HOME/skills/` 下面。

macOS / Linux：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.codex/skills
cp -R ccf-* forge-skills ccf-conference-skills ccf-latex-templates ~/.codex/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.codex\skills\"
Copy-Item -Recurse -Force .\ccf-conference-skills "$HOME\.codex\skills\"
Copy-Item -Recurse -Force .\ccf-latex-templates "$HOME\.codex\skills\"
```

複製完成後建議重新開啟一個會話。可以用這句話快速測試：`Use ccf-idea-optimizer to refine this rough research idea...`

### 2. Claude Code

Claude Code 可以從使用者級 skills 目錄或專案級 skills 目錄載入 skills。希望所有專案都能使用時，推薦使用者級安裝；如果某個論文專案希望自帶固定研究流程，則使用專案級安裝。

使用者級安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.claude/skills
cp -R ccf-* forge-skills ccf-conference-skills ccf-latex-templates ~/.claude/skills/
```

專案級安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p your-paper-repo/.claude/skills
cp -R CCFA-Skills/ccf-* CCFA-Skills/forge-skills CCFA-Skills/ccf-conference-skills CCFA-Skills/ccf-latex-templates your-paper-repo/.claude/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\ccf-conference-skills "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\ccf-latex-templates "$HOME\.claude\skills\"
```

安裝後可以直接按名稱呼叫，例如 `/ccf-idea-reviewer`，也可以用自然語言要求 Claude Code 使用對應的 CCFA skill。如果新加入的 skill 目錄沒有被識別，重啟 Claude Code 即可。

如果你希望使用更強的 subagent 隔離，也可以建立 Claude Code subagent wrapper 指向這些已安裝 skill 目錄，但 `SKILL.md` 和對應的 `references/` 應保持為唯一的知識源。

### 3. Cursor

Cursor 專案級 skills 可以放在 `.cursor/skills/` 下。

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p your-project/.cursor/skills
cp -R CCFA-Skills/ccf-* CCFA-Skills/forge-skills CCFA-Skills/ccf-conference-skills CCFA-Skills/ccf-latex-templates your-project/.cursor/skills/
```

如果你希望在專案裡同時保留 venue-specific 論文模板，也可以把 `ccf-latex-templates/` 複製到論文倉庫中，並讓對應 venue skill 指向本地模板目錄。

### 4. 其他 agents 或手動使用

對於其他 agent 框架，請將同樣的目錄複製到該框架的 skill、tool、memory 或 instruction 目錄，並保持相對路徑不變。每個模組都應以對應目錄下的 `SKILL.md` 作為入口文件。

如果框架沒有原生 skill 系統，也可以手動使用：

```text
1. 根據任務選擇對應目錄。
2. 先閱讀該目錄下的 SKILL.md。
3. 當 SKILL.md 提到 references/... 或 assets/... 時，在同一個 skill 目錄內解析路徑。
4. 當它提到 ../ccf-writing-skills/... 或其他同級 skill 時，保持倉庫原有目錄結構。
5. 只載入當前任務真正需要的引用文件。
```

後續更新時，在本地 clone 目錄中執行 `git pull`，然後重新複製這些 skill 目錄即可。

## 範例請求

```text
Use ccf-brainstorming to clarify this broad research workflow and choose the next CCFA skill.
Use ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use ccf-idea-reviewer to rank these NeurIPS directions with closest-work search and strict fatal-risk diagnosis.
Use ccf-literature-search to find and score high-quality related work for my Introduction.
Use ccf-experiment-designer to design datasets, baselines, ablations, and result-fill tables.
Use ccf-writing-skills to rebuild my introduction around the actual contribution.
Use ccf-paper-compressor to reduce this Related Work section to 800 words.
Use ccf-conference-reviewer to run a full NeurIPS-style scientific review and write a fixed Markdown report.
Use ccf-conference-writing-reviewer to review my manuscript paragraph by paragraph for writing logic, LaTeX/format, and consistency before submission.
Use ccf-conference-paper-rebuttal to draft a concise response from these reviews.
```

## 邊界

CCFA Skills 不保證錄用，不替代真實實驗，不偽造證據，也不能代替領域專家判斷。它更像一個結構化研究伴侶：幫助研究者暴露薄弱假設，組織決策，校準主張，並讓工作持續對目標學術共同體的標準負責。

## 交流

更多更新、範例和研究札記會整理到小紅書號：`8994074380`。
