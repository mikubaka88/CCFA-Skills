<div align="center">

# CCFA Skills

### 面向 CCF 论文项目的 `ccf-*` 技能家族

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

CCFA Skills 是一组本地 Codex skills，用来支撑 CCF 风格论文从立项到投稿后的完整流程：建项目、定路线、打磨 idea、检索文献、设计实验、写作、审稿、审计、检查投稿包、写 rebuttal、重投适配和汇报展示。

这次命名整理后，runtime skills 都采用 `ccf-<对象>-<职责>` 的单数风格；`ccf-common` 是唯一例外，因为它是治理模块，不直接处理普通研究任务。`ccf-revision-ledger` 已合并到 `ccf-rebuttal-writer`，这样审稿意见、回复承诺、修改位置和完成状态不会分裂在两个触发入口里。

![架构](assets/ccfa-skills-architecture.zh-CN.svg)

## 安装

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cp -r CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

已有本地仓库时：

```bash
git pull origin main
cp -r ccf-* "$CODEX_HOME/skills/"
```

仓库同时提供 `.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json`。

## 当前 Skills

- `ccf-project-scaffolder`：脚手架：建目录、选模板、初始化 ccfa.yaml。
- `ccf-pipeline-orchestrator`：编排阶段、gate、artifact 与 handoff。
- `ccf-workflow-planner`：澄清目标、范围、成功标准与下一步 skill。
- `ccf-idea-optimizer`：把粗 idea 具象化成问题、gap、insight、方法和证据计划。
- `ccf-idea-reviewer`：严格评分、排序、比较早期 idea。
- `ccf-literature-searcher`：检索相关工作、prior art、数据集和 benchmark。
- `ccf-experiment-designer`：设计数据集、baseline、指标、消融、鲁棒性和结果表模板。
- `ccf-paper-writer`：写作、润色、重组论文正文，并保护既有 idea 和证据边界。
- `ccf-paper-compressor`：在不改 claims/results 的前提下压缩篇幅。
- `ccf-scientific-reviewer`：做完整科学审稿、评分、模拟 reviewer 和 AC/meta-review。
- `ccf-writing-reviewer`：评审段落逻辑、表达清晰度、一致性、LaTeX/格式和展示风险。
- `ccf-integrity-auditor`：审计 claim-support、结果到 claim、数字、术语和图表一致性。
- `ccf-citation-auditor`：核验已有引用、BibTeX 元数据、文献存在性和引用上下文支撑。
- `ccf-figure-table-builder`：基于真实结果构建和审计图、表、caption、SVG/PDF。
- `ccf-artifact-packager`：准备 artifact/reproducibility 包、环境、seed、license 和 README。
- `ccf-venue-format-guide`：回答会议 LaTeX、template、页数、匿名和 camera-ready 格式问题。
- `ccf-submission-checker`：检查 LaTeX/PDF、页数、匿名、字体、metadata、template 和 policy freshness。
- `ccf-rebuttal-writer`：写 rebuttal、作者回复、response letter、修改说明和 revision ledger。
- `ccf-resubmission-adapter`：把已有论文保守迁移到新 venue，默认不新增实验、不改 bib。
- `ccf-paper-presenter`：把论文转成 slides、poster、talk script、图表讲解和 Q&A。
- `ccf-common`：共享路由、触发注册、handoff、source registry、隐私策略和 artifact 合约。
- `ccf-skill-forger`：创建、更新、校验和审计 CCFA/Codex skills 及家族治理。

## 家族关系

```text
ccf-project-scaffolder -> ccf-pipeline-orchestrator -> ccf-workflow-planner
  -> ccf-idea-optimizer -> ccf-idea-reviewer
  -> ccf-literature-searcher -> ccf-experiment-designer
  -> ccf-paper-writer -> ccf-paper-compressor
  -> ccf-scientific-reviewer / ccf-writing-reviewer
  -> ccf-integrity-auditor / ccf-citation-auditor
  -> ccf-figure-table-builder / ccf-artifact-packager
  -> ccf-venue-format-guide / ccf-submission-checker
  -> ccf-rebuttal-writer / ccf-resubmission-adapter / ccf-paper-presenter
```

![流程](assets/ccfa-skills-workflow.zh-CN.svg)

## Venue 分支

旧的逐会议 runtime skills 已迁移为参考资料：

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

会议格式问题交给 `ccf-venue-format-guide`；正文写作交给 `ccf-paper-writer`；写作/格式评审交给 `ccf-writing-reviewer`；真实投稿包检查交给 `ccf-submission-checker`。

## 重命名与合并

- `ccf-brainstorming` -> `ccf-workflow-planner`：突出“规划与路由”职责，避免和通用 brainstorming 混在一起。
- `ccf-literature-search` -> `ccf-literature-searcher`：从动作名改为职责名，和 auditor/designer/writer 的风格一致。
- `ccf-writing-skills` -> `ccf-paper-writer`：去掉泛化的 `skills` 尾缀，明确它是论文正文写作入口。
- `ccf-conference-reviewer` -> `ccf-scientific-reviewer`：强调这是科学审稿，不再把 venue 层误认为审稿边界。
- `ccf-conference-writing-reviewer` -> `ccf-writing-reviewer`：保留写作评审职责，并与科学审稿分开。
- `ccf-conference-paper-rebuttal` -> `ccf-rebuttal-writer`：直接命名为 rebuttal/author response 的产出职责。
- `ccf-conference-guides` -> `ccf-venue-format-guide`：明确它只处理会议格式、模板、匿名和页数规则。
- `ccf-paper-project-scaffold` -> `ccf-project-scaffolder`：改为清晰的项目脚手架职责名。
- `ccf-artifact-reproducibility` -> `ccf-artifact-packager`：突出 artifact/reproducibility 包的准备与交付。
- `ccf-revision-ledger` -> `merged into ccf-rebuttal-writer`：ledger 属于审后回复追踪，合并后能避免 rebuttal 触发冲突。
- `ccf-paper-talk` -> `ccf-paper-presenter`：突出 slides、poster、talk 和 Q&A 的展示产出。
- `ccf-forge-skills` -> `ccf-skill-forger`：避免 `skills` 尾缀造成“技能家族本身”的歧义。

## 图谱

![目录](assets/ccfa-skills-catalog.zh-CN.svg)

![路由](assets/ccfa-skills-routing.zh-CN.svg)

![Artifact](assets/ccfa-skills-artifacts.zh-CN.svg)

![评审边界](assets/ccfa-skills-review-boundaries.zh-CN.svg)

更完整的触发边界、架构关系和合并理由见 `docs/SKILLS_CATALOG.md`、`docs/ARCHITECTURE.md`、`docs/NAMING_AND_MERGE_AUDIT.md`。
