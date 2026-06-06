<div align="center">

# CCFA Skills

### 面向 CCF 论文项目的 `ccf-*` 技能家族。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

CCFA Skills 是一组本地 Codex skills，用于 CCF 风格论文项目的构建、审计、投稿、返修、重投和汇报。v0.4.0 将仓库从“写作技能集合”升级为“论文项目工作流家族”：新增路由治理、artifact 合约、venue guide 分支、结构校验、插件清单和发布文档。

设计参考了 ARS、nature-skills 和 ARIS，但 CCFA 更强调职责边界：idea 优化不是完整审稿，引用审计不是文献检索，会议格式查询不是论文写作，投稿检查不是正文润色。

![架构](assets/ccfa-skills-architecture.zh-CN.svg)

## 安装

保留手动安装方式：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cp -r CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

已有本地仓库时：

```bash
git pull origin main
cp -r ccf-* "$CODEX_HOME/skills/"
```

仓库也提供 `.codex-plugin/plugin.json` 和 `.claude-plugin/plugin.json`，供支持插件安装的客户端使用。手动复制方式仍保留，因为它能清楚显示本地实际安装了哪些 skills。

## v0.4 架构

| 层级 | 作用 | 主要文件 |
| --- | --- | --- |
| 治理层 | 路由、触发注册表、隐私与证据策略、source registry、artifact 归属、校验。 | `ccf-common/`, `docs/SKILLS_CATALOG.md`, `AGENT_GUIDE.md` |
| 项目状态层 | 创建并维护论文项目结构和 `ccfa.yaml`。 | `ccf-paper-project-scaffold`, `ccf-pipeline-orchestrator` |
| 研究链路层 | idea、文献、实验、写作、压缩、审稿、rebuttal、重投和汇报。 | `ccf-*` skills |
| Venue 分支 | 会议 LaTeX、template、page limit、匿名和 camera-ready 规则。 | `ccf-conference-guides`, `ccf-writing-skills/references/venue-guides/` |
| 发布校验层 | 前缀、frontmatter、shared controls、registry、venue index、SVG、source、路径隐私。 | `.github/workflows/validate.yml`, `ccf-common/scripts/` |

## 核心链路

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

完整触发条件、排除边界和联动关系见 `docs/SKILLS_CATALOG.md`。

## Venue 分支

`ccf-conference-skills/<venue>/SKILL.md` 不再作为可安装 runtime skill 层存在。原 109 个会议 skill 已迁移到：

```text
ccf-writing-skills/references/venue-guides/index.md
ccf-writing-skills/references/venue-guides/<venue>.md
```

以下任务使用 `ccf-conference-guides`：

- CVPR page limit
- NeurIPS LaTeX template
- SIGMOD 匿名模式
- camera-ready checklist
- supplementary material 规则

论文正文写作使用 `ccf-writing-skills`，写作/格式审查使用 `ccf-conference-writing-reviewer`，投稿包构建和合规检查使用 `ccf-submission-checker`。最终投稿前仍必须核对当年官方 venue policy。

![流程](assets/ccfa-skills-workflow.zh-CN.svg)

## `ccfa.yaml`

v0.4 引入共享项目状态文件，固定顶层字段为：

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

`ccf-paper-project-scaffold` 负责创建，`ccf-pipeline-orchestrator` 可以更新阶段和 gate，其他 skills 按 `ccf-common/references/artifact-contracts.md` 读取或提出更新建议。

## 校验

发布前运行：

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_path_privacy.py .
python ccf-common/scripts/check_sources.py
rg -nP "^name: (?!ccf-)" -g "SKILL.md"
```

GitHub Actions 会在 push 和 pull request 上运行同类结构校验。

![评审边界](assets/ccfa-skills-review-boundaries.zh-CN.svg)

## 兼容变化

- 所有可安装 skill 名称均使用 `ccf-` 前缀。
- `forge-skills` 已重命名为 `ccf-forge-skills`。
- 核心研究链路名称保持稳定。
- 旧 venue runtime skills 已移除；使用 `ccf-conference-guides` 和 venue-guide reference 分支。
- `SKILL.md` 是最高优先级。如果文档、catalog 或 routing 与 skill body 冲突，应修正文档索引。
