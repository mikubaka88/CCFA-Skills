<h1 align="center">CCFA Skills</h1>

<p align="center"><strong>A skill family for shaping the research storyline of CCF-A papers.</strong></p>

<p align="center">
  <strong>简体中文</strong> ·
  <a href="README.en.md">English</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills 主视觉" width="100%">
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

一篇高水平论文真正重要的，往往不是最后那份 PDF，而是贯穿其后的研究故事线。它从一个尚不稳定的 idea 开始，在文献中寻找位置，在实验中接受检验，在写作中被组织成可被审稿人理解的论证，又在评审和 rebuttal 中继续被修正。真正困难的地方，不只是写出某一段 introduction，而是让 idea、证据、实验、表达和回应始终指向同一个研究问题。

CCFA Skills 正是从这个观察出发。它把 CCF-A 论文项目看作一条可以被维护、审计和反复推进的研究故事线，而不是一次性的文本生成任务。一个 idea 需要先被塑形，在真正需要取舍时再接受严格评审；一组实验需要服务于明确 claim，而不是孤立地填满表格；一篇论文的写作需要保留证据边界；一次 rebuttal 也不应只是临时答辩，而应成为下一轮修改和重投的可追踪记录。

这个项目的核心 insight 是：论文质量来自连续决策的质量。写作、评审、审计、投稿检查和 rebuttal 不应该互相替代，而应该各自保持边界，并在同一个项目状态中交接。v0.5 因此将家族收敛为 15 个阶段角色，让每个阶段都有清楚的责任，让每个 artifact 都能找到归属，也让整套系统更像一个围绕研究故事线展开的协作框架，而不是松散的 prompt 集合。

![CCFA 技能家族逻辑](assets/ccfa-skills-architecture.zh-CN.svg)

## 整体链路

默认论文项目闭环如下：

```text
项目搭建
  -> 流程编排
  -> idea 优化
  -> idea 评审
  -> 文献监控 / 竞品跟踪
  -> 文献检索
  -> 实验设计
  -> 写作范例抽取（可选）
  -> 会议感知写作
  -> 科学/写作评审
  -> 完整性审计
  -> 投稿包检查
  -> rebuttal / revision ledger / resubmission
```

每个阶段只交给一个 owner skill。这样做的目的不是减少功能，而是让触发条件、输出格式和 artifact 归属更稳定：写作由 writer 负责，判断由 reviewer 负责，事实核验由 auditor 负责，投稿包由 submission checker 负责，回应审稿人由 rebuttal writer 负责。

`ccfa.yaml` 是共享项目状态文件。它记录 `target_venue`、`stage`、`artifacts`、`claims`、`experiments`、`reviews`、`revision_ledger` 和 `submission_checks`，让各个 skill 可以联动，但不会互相覆盖正文、实验表、审稿报告或 rebuttal。

![端到端流程](assets/ccfa-skills-workflow.zh-CN.svg)

## 15 个 Runtime Skills

| 阶段 | Skill | 启动条件 | 主要产物 | 不应该用于 |
| --- | --- | --- | --- | --- |
| 项目搭建 | `ccf-project-scaffolder` | 用户要创建论文项目目录、复制模板、初始化 `ccfa.yaml`。 | 项目目录、模板文件、初始状态文件。 | 生成研究内容或替用户写 idea。 |
| 流程编排 | `ccf-pipeline-orchestrator` | 用户要拆任务、排阶段、设 gate、决定下一步 owner。 | 阶段计划、gate、handoff、状态更新建议。 | 直接写作、审稿、检索、设计实验或 rebuttal。 |
| Idea 优化 | `ccf-idea-optimizer` | 用户有粗 idea、模糊方向、想找方向或救方向。 | problem-gap-insight-method-evidence 文档、救援路线、最小可验证问题。 | 对多个 idea 排名打分。 |
| Idea 评审 | `ccf-idea-reviewer` | 用户明确要求评分、排名、严格评审、判断创新性或取舍。 | 分数、风险、stage-aware 发展潜力、修改建议。 | 继续发散优化单个 idea。 |
| 文献监控 | `ccf-literature-monitor` | 用户要追踪新论文、竞品、arXiv/OpenReview/会议动态，或问最近有没有类似 idea。 | 监控报告、overlap level、RELAX/RESEARCH/FOLLOW-UP 标记、跨 skill handoff。 | 系统性 related work 检索、引用审计或最终 idea 打分。 |
| 文献证据 | `ccf-literature-searcher` | 用户要查 related work、prior art、数据集、benchmark、open gap 或引用证据。 | 文献列表、筛选理由、相关工作结构、机会图、证据缺口。 | 只核验已经写进论文的引用，或把 related work 当成最终否决。 |
| 实验设计 | `ccf-experiment-designer` | 用户要设计 baseline、metric、消融、鲁棒性实验或结果表。 | 实验协议、baseline 矩阵、结果表模板、真实结果图表。 | 编造结果或绘制文档架构图。 |
| 写作范例 | `ccf-paper-to-exemplar` | 用户提供论文 PDF，希望抽取成可复用写作范例或个人 exemplar 库。 | exemplar card、写作 pattern、venue 标签、writer 可用索引。 | 直接写论文或进行审稿。 |
| 论文写作 | `ccf-paper-writer` | 用户要写、润色、压缩、改写、从 idea 起草 LaTeX、按目标会议篇幅成稿、做 slides/poster/talk。 | 论文正文、保留格式的修改稿、压缩稿、篇幅预算、展示材料。 | 完整审稿、事实审计、投稿包检查或 rebuttal。 |
| 论文评审 | `ccf-paper-reviewer` | 用户要科学审稿、写作评审、评分、AC/meta-review 或投稿风险诊断。 | 科学评审、写作评审、风险表、评分和修改优先级。 | 直接替换正文或写 rebuttal。 |
| 完整性审计 | `ccf-integrity-auditor` | 用户要核验 claim、数字、图表、引用、BibTeX 和上下文支撑。 | claim-support 表、数字一致性报告、引用审计。 | broad literature search 或完整科学审稿。 |
| 投稿检查 | `ccf-submission-checker` | 用户要查会议规则、页数、匿名、PDF metadata、artifact、camera-ready。 | 投稿包检查、LaTeX/PDF 构建结果、匿名和 artifact checklist。 | 润色正文内容。 |
| 审稿回复 | `ccf-rebuttal-writer` | 用户要写 rebuttal、response letter、revision ledger 或重投计划。 | rebuttal 文案、逐条回应、revision ledger、resubmission plan。 | 普通论文写作。 |
| 共享治理 | `ccf-common` | 维护路由、隐私/证据策略、source registry、artifact contract。 | 公共规则、路由表、source registry、校验策略。 | 普通研究任务。 |
| 家族维护 | `ccf-skill-forger` | 维护 skill、命名、docs、SVG、校验、release。 | 更新后的技能文件、文档、图、验证结果和发布提交。 | 研究写作、审稿或实验设计。 |

![Runtime skill 总览](assets/ccfa-skills-catalog.zh-CN.svg)

## 触发边界

触发边界是这个家族最重要的治理点。相似任务必须进入不同 owner，避免一个请求同时触发多个 skill。

| 用户真正要做的事 | 使用 | 不使用 |
| --- | --- | --- |
| 把一个模糊 idea 变成可做的研究方案，或找救援路线 | `ccf-idea-optimizer` | `ccf-idea-reviewer` |
| 明确要对多个 idea 打分、排序、取舍 | `ccf-idea-reviewer` | `ccf-idea-optimizer` |
| 监控新论文、竞品、最近是否有类似 idea | `ccf-literature-monitor` | `ccf-literature-searcher` |
| 找新文献、找 benchmark、找数据集、找 open gap | `ccf-literature-searcher` | `ccf-integrity-auditor` |
| 核验论文里已经引用的文献是否真实支撑 claim | `ccf-integrity-auditor` | `ccf-literature-searcher` |
| 设计实验和结果表 | `ccf-experiment-designer` | `ccf-paper-writer` |
| 把 PDF 论文转成写作范例 | `ccf-paper-to-exemplar` | `ccf-paper-writer` |
| 写正文、润色、压缩、保持原格式改写 | `ccf-paper-writer` | `ccf-paper-reviewer` |
| 判断论文能否被接收、哪里会被拒 | `ccf-paper-reviewer` | `ccf-paper-writer` |
| 检查页数、匿名、PDF、metadata、artifact | `ccf-submission-checker` | `ccf-paper-writer` |
| 回复审稿人和维护 revision ledger | `ccf-rebuttal-writer` | `ccf-paper-reviewer` |
| 改文档图、维护 skill、发 release | `ccf-skill-forger` | `ccf-experiment-designer` |

![路由边界](assets/ccfa-skills-routing.zh-CN.svg)

## 已合并的 Helper 能力

这些旧名称不要再作为独立 runtime skills 安装：

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

能力仍然存在，只是归属到更合适的 owner：

| 已合并能力 | 当前 owner | 原因 |
| --- | --- | --- |
| workflow planning | `ccf-pipeline-orchestrator` | 规划和编排必须共享同一个阶段状态。 |
| compression、slides、poster、talk、Q&A | `ccf-paper-writer` | 都属于论文文本或论文派生文本。 |
| writing review | `ccf-paper-reviewer` | 它是评审模式，不是写作模式。 |
| citation audit | `ccf-integrity-auditor` | 核验引用属于事实完整性。 |
| figure/table builder | `ccf-experiment-designer` | 结果图表必须绑定真实实验结果。 |
| artifact packager、venue format guide | `ccf-submission-checker` | 都属于投稿包 readiness。 |
| resubmission adapter | `ccf-rebuttal-writer` | 重投需要基于 reviewer response 和 revision ledger。 |
| docs SVG designer | `ccf-skill-forger` | 文档图是家族维护，不是论文实验图。 |

## Artifact 合约

CCFA 的 artifact 设计是为了避免 skill 互相覆盖。

| Artifact | 主要 owner | 其他 skill 如何使用 |
| --- | --- | --- |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | 读取阶段、目标会议、产物状态和 gate。 |
| idea brief | `ccf-idea-optimizer` | reviewer 评分，writer 用于正文 story。 |
| idea review | `ccf-idea-reviewer` | optimizer 和 experiment designer 用于修正方向。 |
| literature notes | `ccf-literature-searcher` | writer 写 related work，auditor 检查引用支撑。 |
| experiment plan/results | `ccf-experiment-designer` | writer 写实验，auditor 查数字一致性。 |
| manuscript | `ccf-paper-writer` | reviewer/auditor/submission checker 只诊断或检查。 |
| review report | `ccf-paper-reviewer` | writer 修稿，rebuttal writer 提取回应点。 |
| integrity report | `ccf-integrity-auditor` | writer 修 claim，literature searcher 补证据。 |
| submission check | `ccf-submission-checker` | writer 修格式，rebuttal writer 准备后续版本。 |
| revision ledger | `ccf-rebuttal-writer` | orchestrator 跟踪 reviewer comment 到 action 的闭环。 |

![Artifact 合约](assets/ccfa-skills-artifacts.zh-CN.svg)

## 写作与评审输出原则

- 写作、润色、压缩、presentation 任务应服从用户要求的输出格式。用户给 LaTeX 就保持 LaTeX，给 Markdown 就保持 Markdown。
- 用户只有 idea 且要求从 0 写文章时，`ccf-paper-writer` 先读取目标会议 venue guide 和篇幅预算；如果没有目标会议或找不到 guide，回退 NeurIPS 模板。
- 投稿式完整稿件不能只求可编译：应接近目标会议主文篇幅，短太多要扩写，超出篇幅再由 writer 的 compression 模式压缩，最后交给 `ccf-submission-checker` 检查页数。
- 非 review 类 skill 应该灵活、信息密度高，产出具体 artifact，而不是空泛流程说明。
- review、audit、submission gate 可以保持严格结构，因为它们的价值是可追踪的判断、风险和 pass/fail 检查。
- 所有 skill 都不能编造实验结果、引用、官方规则或 reviewer 结论。缺证据时应标明 `TBD`、`needs evidence` 或交给对应 owner。

![评审、审计与行动边界](assets/ccfa-skills-review-boundaries.zh-CN.svg)

## Venue Guides

会议 LaTeX/template 信息是 reference，不是 runtime skill：

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

使用规则：

| 场景 | 使用 |
| --- | --- |
| 按 ICLR/NeurIPS/CVPR 等目标会议写正文 | `ccf-paper-writer` 先读 venue guide，再写正文。 |
| 检查页数、匿名、PDF metadata、camera-ready、artifact | `ccf-submission-checker`。 |
| 只问某会议 LaTeX/template/page limit | `ccf-submission-checker`，必要时读取 venue guide。 |
| 找不到目标会议 guide | `ccf-paper-writer` 默认回退 NeurIPS 模板，并提示最终投稿前需重新核验。 |

## 安装

完整安装：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

部分安装必须包含 `ccf-common`：

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

推荐安装组合：

| 组合 | 包含 | 适合 |
| --- | --- | --- |
| 全流程 | 15 个 runtime skills | 从 idea 到 rebuttal 的完整论文项目。 |
| 写作子集 | `ccf-common`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-submission-checker` | 起草、润色、写作评审、格式检查。 |
| 监控子集 | `ccf-common`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-idea-reviewer`, `ccf-idea-optimizer` | 追踪新论文、竞品和 novelty 风险。 |
| 早期研究子集 | `ccf-common`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer` | 写正文前的 idea、文献监控、文献检索和实验设计。 |
| 投稿子集 | `ccf-common`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 已有稿件的完整性和投稿包检查。 |
| 维护子集 | `ccf-common`, `ccf-skill-forger` | 维护技能、文档、SVG 和 release。 |

![安装组合](assets/ccfa-skills-installation.zh-CN.svg)

## 进一步阅读

如果你想理解这个家族为什么这样设计，建议按下面顺序阅读：

| 文档 | 适合什么时候看 |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | 想理解主链路、治理层、artifact 状态和 revision loop。 |
| [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md) | 想查每个 skill 的启动条件、边界和容易误触发的场景。 |
| [docs/INSTALLATION_MATRIX.zh-CN.md](docs/INSTALLATION_MATRIX.zh-CN.md) | 想只安装部分 skills，判断哪些必须装、哪些不能单独装。 |
| [docs/NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md) | 想理解为什么合并 helper skills，以及命名如何减少冲突。 |
| [AGENT_GUIDE.md](AGENT_GUIDE.md) | 给 agent 使用的操作指南，说明如何选择 owner、交接 artifact、避免覆盖。 |
| [demo/attention-is-all-you-need/](demo/attention-is-all-you-need/) | 想看一个完整 ICLR 风格闭环示例。 |

## Demo

`demo/attention-is-all-you-need/` 是一个 ICLR 风格闭环 demo，用原始 Transformer 论文展示 CCFA 家族如何从原文思路提炼、idea 评审、LaTeX 写作、写作/科学评审、完整性审计、投稿检查走到 rebuttal。demo 是示例，不是必须阅读的入口。

![Attention demo](assets/ccfa-skills-demo-attention.zh-CN.svg)

## 维护与验证

常用验证命令：

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_markdown_links.py
python ccf-common/scripts/check_sources.py
python ccf-common/scripts/check_path_privacy.py .
```

生成 SVG：

```bash
python tools/build_ccfa_diagrams.py
```

发布前应保证 runtime skill 数量、frontmatter、venue guide 路径、SVG 文件、Markdown 链接、路径隐私和插件 manifest 都通过检查。
