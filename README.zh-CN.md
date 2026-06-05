<div align="center">

# CCFA Skills

### 面向 CCF-A 研究流程的实用 skill 集合。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">
</p>

## 项目定位

CCFA Skills 是一组服务 CCF-A 研究流程的本地 skills。它帮助把粗糙想法推进到可以投稿的论文：先澄清任务，再打磨 idea、查相关工作、设计实验、写作和压缩论文、投稿前审查，并在审稿后组织回应。

这个仓库不绑定某一个模型或交互界面。文件采用 `SKILL.md` 结构，可用于支持本地 skill 的 agent 环境。核心内容是可复用的 Markdown 工作流、评分标准、检查表、venue 说明、模板和参考材料。

## 研究前提

许多研究项目在开始写作前就已经变得难以防守。问题往往出在更早的研究链条：

```text
问题 -> 缺口 -> 挑战 -> 洞察 -> 方法 -> 证据 -> 主张
```

当其中某一环薄弱时，后续润色常常只是把问题藏起来，而不是解决它。模糊的 gap 会变成模糊的引言；缺少机制的方法会变成组件列表；不能检验中心主张的实验会变得难以解释。

CCFA Skills 的原则很简单：尽早找到薄弱环节，把问题说清楚，再转化为下一步研究行动。整体风格偏克制：新颖性要有依据，方法要有机制，主张要有证据，表达要有边界。

## 系统架构

这个家族按照研究流程分层组织。

| 层级 | 目的 | Skills |
| --- | --- | --- |
| **Intake Layer** | 澄清目标、约束、工作流选项，并为复杂请求选择下一步 CCFA skill。 | `ccf-brainstorming` |
| **Idea Layer** | 在写作前塑形并评估研究方向。 | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| **Evidence Layer** | 检索相关文献，并设计不编造结果的实验方案。 | `ccf-literature-search`, `ccf-experiment-designer` |
| **Manuscript Layer** | 将可行方向发展为连贯的 CCF-A 论文，并按篇幅限制压缩。 | `ccf-writing-skills`, `ccf-paper-compressor` |
| **Review Layer** | 投稿前审查论文内容，模拟 reviewer 问题，并检查写作、格式和 LaTeX。 | `ccf-conference-reviewer`, `ccf-conference-writing-reviewer` |
| **Response Layer** | 将审稿意见转化为清晰回应和修改承诺。 | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | 创建、改进、校验和治理 skill 模块。 | `forge-skills`, `ccf-common` |

推荐按任务路由，而不是让所有模块同时参与。`ccf-common/references/routing.md` 定义每类任务的归属，避免 idea 优化、idea 评分、文献检索、实验设计、论文写作、篇幅压缩、论文审查、写作评审、rebuttal 和 skill 维护处理同一类请求。

跨 skill handoff 由 `metadata.ccf_skill_controls.handoff_question_mode` 控制：

- **PARTIAL (Recommended)：** 只在跨研究阶段、可能改变 idea scope、进入正式 reviewer/rebuttal 模块、联网处理敏感材料、或生成可复用文件时询问。
- **FULL：** 任何可选 sibling-skill handoff 前都询问。
- **OFF：** 不询问，按路由自动使用需要的 sibling skill；仍然尊重用户 denylist 和 writing-only 的 idea-scope 保护。

```text
raw idea
  -> ccf-brainstorming                           ：复杂或多阶段请求的可选上游澄清
  -> ccf-idea-optimizer                           ：问题 / 方法 / 证据成形
  -> ccf-idea-reviewer                            ：当用户要求评分/排序时做联网检索支撑的严格问题-方法门控
  -> ccf-literature-search                        ：需要当前文献、数据集或 benchmark 时使用
  -> ccf-experiment-designer                      ：设计 baseline / ablation / 结果填写表
       如果薄弱但可修复且 handoff 允许            ：回到 optimizer 做定向修复
       如果根本不匹配                            ：换方向或停止投入
       如果已经可发展且 handoff 允许             ：进入写作模块

writing request
  -> ccf-writing-skills                           ：默认 writing-only
       修改 idea scope 需要明确确认              ：否则只标注 Idea-level risk
       篇幅/页数压缩按 handoff mode 执行          ：ccf-paper-compressor
       完整论文评审按 handoff mode 执行           ：ccf-conference-reviewer
       写作 / LaTeX 评审按 handoff mode 执行      ：ccf-conference-writing-reviewer

用户明确要求 rebuttal 或真实审稿意见到来
  -> ccf-conference-paper-rebuttal                ：作者回应和修改承诺
       改论文或做 review-risk 诊断               ：按 handoff mode 执行
```

**Writing-only mode。** `ccf-writing-skills` 默认不修改研究主题、核心问题、方法机制、实验设置、结果数值和结论方向。它只改表达、结构、故事线、claim-evidence 对齐和 reviewer-facing 包装。即使 idea 修改看起来有帮助，也必须先得到明确确认。

**Session denylist。** 如果用户说不使用某个 skill，该 skill 在当前对话中就被禁用。助手不能绕过这个决定去模拟被禁用模块；只能使用本模块内部的简短风险扫描、行动列表或 writing-only checklist。

**Task modes。** CCFA Skills 支持 `quick` 和 `standard` 两种模式。`quick` 用于单段润色、局部风险检查、小规模文献 sanity scan、快速实验草图或局部压缩，不强制完整 checklist。`standard` 是完整章节、整篇论文 review、文献检索文件夹、实验方案、score-risk loop 和可复用文件的默认模式。

因此，第二次出现 `ccf-idea-optimizer` 不是重复。第一次 optimizer 负责把粗糙方向整理到“可以被判断”的状态；后续在 reviewer 诊断后，只有 handoff mode 允许时才会进入定向修复。`ccf-conference-paper-rebuttal` 被隔离在默认投稿前闭环之外，只有用户明确要求 rebuttal、作者回应、response letter 或审稿意见回复时才使用。

<p align="center">
  <img src="assets/ccfa-skills-architecture.zh-CN.svg" alt="CCFA Skills 工作流门控" width="100%">
</p>

<p align="center">
  <img src="assets/ccfa-skills-workflow.zh-CN.svg" alt="CCFA Skills 逐步工作流" width="100%">
</p>

<p align="center">
  <img src="assets/ccfa-skills-review-boundaries.zh-CN.svg" alt="CCFA Skills 评审边界图" width="100%">
</p>

这套结构把投稿前最关键的问题拆开处理：新颖性、重要性、可靠性、证据、清晰度、可复现性和 venue fit。每个 skill 负责一类问题，同时保留它们之间的依赖关系。

## Skill 家族

### `ccf-brainstorming`

在进入下游研究工作前澄清复杂请求。它把模糊目标整理成简短 research brief：需要做的决定、目标受众、已有输入、约束、成功标准、工作流选项和推荐的下一步 CCFA skill。

它只在需要时使用。适合头脑风暴、需求澄清、任务拆解、研究路线讨论或 design brief，然后再选择下游 skill。

### `ccf-idea-optimizer`

将早期研究方向转化为结构化研究方案：任务、gap、根本挑战、核心洞察、方法机制、贡献类型、证据计划和风险。

它适合处理“有潜力但尚未成形”的想法。这个 skill 会追问：项目真正想证明什么，方法依赖什么假设，什么证据能让主张可信，以及哪个学术共同体会认为这项工作有意义。

### `ccf-idea-reviewer`

在论文尚未形成之前评价问题和方法。标准模式会先用 public-safe 查询检索相近工作，再对照已有工作判断新颖性，并从领域、方法、实验、venue 和 prior art 等视角给出意见。

它的目标是给出具体、专业、偏严格的评阅意见。它会区分“新颖性确实不足”和“还没有查清楚”，也会区分可修复问题与需要换方向的问题。主要批评会说明对应的主张、证据依据、潜在 reviewer 关切和具体修复条件。

### `ccf-literature-search`

联网检索相关的高质量文献，筛掉低质量或不合适来源，分类 paper type，评分文章质量，并写入包含标题、链接、评分、文章类型和备注的 literature-search 文件夹。

它主要联动 Related Work、Introduction、idea 优化、idea 评审、实验设计和 reviewer-risk 诊断。纯 benchmark 论文会单独标记，而不是按方法论文标准扣分。

### `ccf-experiment-designer`

设计 CCF-A 实验方案：数据集、benchmark、baseline、ablation、metric、robustness test、failure analysis 和结果填写表。

它不会替用户生成实验数值。缺少数值时，只提供给用户填写的表格模板，并标注每个实验回答哪个 reviewer 问题。

### `ccf-writing-skills`

将成熟 idea 发展为论文级论证。它处理故事线、章节规划、段落角色、claim-evidence map、venue 适配、写作样例和修改优先级。

它最重视一致性：摘要、引言、方法、实验、局限性和结论应该以不同分辨率讲述同一个研究故事。

### `ccf-paper-compressor`

按照页数或字数目标压缩论文段落、章节或全文，同时保护故事线、主张、证据、结果数值和局限性。

它可以用 quick mode 做局部压缩，也可以用 standard mode 做整节或整篇压缩。涉及“放附录还是删除”的策略选择时，它会询问一次，然后一致执行。

### `ccf-conference-reviewer`

负责完整论文评审。它执行 desk check、public-safe 相关工作搜索、新颖性/可靠性/证据评审、多 reviewer 模拟、AC/meta-review、校准分数和问题表，并在 standard 模式生成固定格式 Markdown 审稿报告。

报告格式参考本地 CSPaper 风格，并扩展 claim-evidence audit、实验/可复现性检查、reviewer panel、AC 综合、分数调整条件和后续行动建议。

### `ccf-conference-writing-reviewer`

这是写作与格式审查模块。它逐段阅读论文，检查故事线、LaTeX/格式、claim-evidence 展示、全文一致性、图表叙事和贡献展示，并把每个问题转化为带位置的修改建议。

它不负责完整论文评审、AC/meta-review 或论文评分；这些请求路由到 `ccf-conference-reviewer`。

### `ccf-conference-paper-rebuttal`

支持审稿后的作者回应。它整理审稿意见，合并重复关切，选择回应策略，起草简洁回复，并可配合 TeX response templates。

它的原则很直接：回答关切，澄清误解，承认合理边界，避免不可兑现的承诺。

### `forge-skills`

提供构建和维护 skills 的工程层。它覆盖命名、结构、资源组织、校验和触发设计。

它让这个家族保持可扩展：新的领域 skill 可以被加入，而不需要把整个仓库变成一个巨大的说明文档。

### `ccf-common`

提供 CCFA 家族的共享控制层，包括路由、handoff 模式、私有材料安全、source registry 和 venue-family map。它不是普通研究写作 skill，而是由维护者和兄弟 skill 加载，用来保持行为一致。

## 这个家族优化什么

| 目标 | 含义 |
| --- | --- |
| **问题精度** | 论文应命名真实瓶颈，而不只是说明现有方法不足。 |
| **机制清晰度** | 方法应解释为什么有效，而不只是列出组件。 |
| **新颖性校准** | 原创性主张应与相近工作对照；未检索时应标记不确定性。 |
| **证据对齐** | 实验、证明、用户研究或系统评估应检验中心主张。 |
| **Venue fit** | 论证方式应能被目标学术共同体理解和评价。 |
| **修改连续性** | 批评应转化为清晰行动列表，而不是零散建议。 |

## 安装

请复制完整 skill 目录，而不只是复制 `SKILL.md`。多个模块依赖 `references/`、`assets/`、模板以及跨 skill 的相对路径引用。可安装的目录包括：

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

Codex-style 本地 skill 环境通常从 `~/.codex/skills/` 读取 skills。如果你使用自定义 `$CODEX_HOME`，请把这些目录放到 `$CODEX_HOME/skills/` 下面。

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

复制完成后建议重新开启一个会话。可以用这句话快速测试：`Use ccf-idea-optimizer to refine this rough research idea...`

### 2. Claude Code

Claude Code 可以从用户级 skills 目录或项目级 skills 目录加载 skills。希望所有项目都能使用时，推荐用户级安装；如果某个论文项目希望自带固定研究流程，则使用项目级安装。

用户级安装：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.claude/skills
cp -R ccf-* forge-skills ccf-conference-skills ccf-latex-templates ~/.claude/skills/
```

项目级安装：

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

安装后可以直接按名称调用，例如 `/ccf-idea-reviewer`，也可以用自然语言要求 Claude Code 使用对应的 CCFA skill。如果新加入的 skill 目录没有被识别，重启 Claude Code 即可。

如果你希望使用更强的 subagent 隔离，也可以创建 Claude Code subagent wrapper 指向这些已安装 skill 目录，但 `SKILL.md` 和对应的 `references/` 应保持为唯一的知识源。

### 3. Cursor

Cursor 项目级 skills 可以放在 `.cursor/skills/` 下。

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p your-project/.cursor/skills
cp -R CCFA-Skills/ccf-* CCFA-Skills/forge-skills CCFA-Skills/ccf-conference-skills CCFA-Skills/ccf-latex-templates your-project/.cursor/skills/
```

如果你希望在项目里同时保留 venue-specific 论文模板，也可以把 `ccf-latex-templates/` 复制到论文仓库中，并让对应 venue skill 指向本地模板目录。

### 4. Other agents or manual use

对于其他 agent 框架，请将同样的目录复制到该框架的 skill、tool、memory 或 instruction 目录，并保持相对路径不变。每个模块都应以对应目录下的 `SKILL.md` 作为入口文件。

如果框架没有原生 skill 系统，也可以手动使用：

```text
1. 根据任务选择对应目录。
2. 先阅读该目录下的 SKILL.md。
3. 当 SKILL.md 提到 references/... 或 assets/... 时，在同一个 skill 目录内解析路径。
4. 当它提到 ../ccf-writing-skills/... 或其他同级 skill 时，保持仓库原有目录结构。
5. 只加载当前任务真正需要的引用文件。
```

后续更新时，在本地 clone 目录中执行 `git pull`，然后重新复制这些 skill 目录即可。

## 示例请求

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

## 边界

CCFA Skills 不保证录用，不替代真实实验，不伪造证据，也不能代替领域专家判断。它更像一个结构化研究伴侣：帮助研究者暴露薄弱假设，组织决策，校准主张，并让工作持续对目标学术共同体的标准负责。

## 交流

更多更新、示例和研究札记会整理到小红书号：`8994074380`。
