<div align="center">

# CCFA Skills

### 面向 CCF / ICLR / NeurIPS 风格论文项目的 `ccf-*` 技能家族。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<img src="assets/ccfaskills.png" alt="CCFA Skills 主视觉" width="100%">

</div>

---

CCFA Skills 是一套本地 Codex skill 家族，用来管理论文项目从 idea 到投稿、审稿回复和重投的完整闭环。v0.4.5 不再把每个小功能拆成独立 runtime，而是用 13 个 owner skills 承担清晰职责；压缩、写作评审、引用审计、会议格式、artifact、报告展示等能力都归入对应 owner，减少触发冲突和歧义。

![技能家族逻辑](assets/ccfa-skills-architecture.zh-CN.svg)

## 家族逻辑

默认闭环是：

```text
项目搭建
  -> 流程编排
  -> idea 优化与 idea 评审
  -> 文献证据与实验设计
  -> 按目标会议写作正文
  -> 科学/写作评审与完整性审计
  -> 投稿包检查
  -> rebuttal、revision ledger 与可能的重投
```

`ccfa.yaml` 是共享项目状态。它记录目标会议、阶段、artifacts、claims、experiments、reviews、submission checks 和 revision ledger，让各个 skill 能联动，但不互相覆盖。

![流程](assets/ccfa-skills-workflow.zh-CN.svg)

## 13 个 Runtime Skills

| 阶段 | Skill | 负责什么 | 常见下游 |
| --- | --- | --- | --- |
| 搭建 | `ccf-project-scaffolder` | 创建项目目录、复制 LaTeX 模板、初始化 `ccfa.yaml`。 | `ccf-pipeline-orchestrator`, `ccf-paper-writer` |
| 规划 | `ccf-pipeline-orchestrator` | 排阶段、定 gate、维护 artifact 状态、选择下一个 owner。 | 任意阶段 owner |
| Idea | `ccf-idea-optimizer` | 把粗 idea 变成 problem-gap-insight-method-evidence。 | `ccf-idea-reviewer`, `ccf-literature-searcher` |
| Idea gate | `ccf-idea-reviewer` | 严格评分、排序、判断拒稿风险和取舍。 | `ccf-idea-optimizer`, `ccf-experiment-designer` |
| 证据 | `ccf-literature-searcher` | 检索 prior art、related work、数据集和 benchmark。 | `ccf-experiment-designer`, `ccf-paper-writer` |
| 证据 | `ccf-experiment-designer` | 设计 baseline、metric、消融、真实结果表和图。 | `ccf-paper-writer`, `ccf-integrity-auditor` |
| 正文 | `ccf-paper-writer` | 起草、润色、压缩、展示材料、按会议 LaTeX 写稿。 | `ccf-paper-reviewer`, `ccf-submission-checker` |
| 评审 | `ccf-paper-reviewer` | 科学评审、写作评审、评分、AC/meta-review 风险。 | `ccf-paper-writer`, `ccf-integrity-auditor` |
| 审计 | `ccf-integrity-auditor` | 核验 claim、数字、图表、引用、BibTeX 和上下文支撑。 | `ccf-paper-writer`, `ccf-literature-searcher` |
| 投稿 | `ccf-submission-checker` | 检查会议规则、PDF/LaTeX、匿名、metadata、artifact。 | `ccf-paper-writer`, `ccf-rebuttal-writer` |
| 回应 | `ccf-rebuttal-writer` | rebuttal、response letter、revision ledger、保守重投。 | `ccf-paper-writer`, `ccf-submission-checker` |
| 治理 | `ccf-common` | 路由、隐私/证据策略、source registry、artifact 合约。 | 全部 CCFA skills |
| 维护 | `ccf-skill-forger` | 维护 skill、文档、生成式 SVG、验证和 release。 | `ccf-common` |

![Skill 总览](assets/ccfa-skills-catalog.zh-CN.svg)

## 安装

完整安装：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

支持部分安装，但任何子集都必须包含 `ccf-common`：

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

部分安装前请看 [INSTALLATION_MATRIX.zh-CN.md](docs/INSTALLATION_MATRIX.zh-CN.md)。

![安装组合](assets/ccfa-skills-installation.zh-CN.svg)

## 已合并的 Helper 能力

不要再安装这些旧 runtime 名称：`ccf-workflow-planner`、`ccf-paper-compressor`、`ccf-writing-reviewer`、`ccf-citation-auditor`、`ccf-figure-table-builder`、`ccf-artifact-packager`、`ccf-venue-format-guide`、`ccf-resubmission-adapter`、`ccf-paper-presenter`、`ccf-doc-diagram-designer`。

能力仍然保留，只是归属更明确：

| 旧 helper 能力 | 当前 owner |
| --- | --- |
| 压缩、talk、poster、slides、Q&A | `ccf-paper-writer` |
| 写作评审 | `ccf-paper-reviewer` |
| 引用审计 | `ccf-integrity-auditor` |
| 结果图表 | `ccf-experiment-designer` |
| artifact 和会议格式检查 | `ccf-submission-checker` |
| 重投迁移 | `ccf-rebuttal-writer` |
| 文档 SVG 维护 | `ccf-skill-forger` |

![路由边界](assets/ccfa-skills-routing.zh-CN.svg)

## Venue Guides

会议 LaTeX/template 信息是 reference，不是 runtime skill：

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

正文写作走 `ccf-paper-writer`。会议合规、页数、匿名、PDF metadata、camera-ready 和 artifact 检查走 `ccf-submission-checker`。从 0 写稿时，如果用户指定目标会议，writer 会先读对应 venue guide；如果没有指定或找不到目标会议，则回退 NeurIPS 模板。

## Demo

`demo/attention-is-all-you-need/` 是完整 ICLR 风格闭环 demo：读取 Transformer 原文，提炼动机、问题、insight、方法和结果，进行 idea 评审，写出可编译的完整 LaTeX 论文，完成写作/科学评审、完整性审计、投稿检查、rebuttal，并记录家族剩余问题。

![Attention Demo](assets/ccfa-skills-demo-attention.zh-CN.svg)

## 图与文档

![Artifacts](assets/ccfa-skills-artifacts.zh-CN.svg)

![评审边界](assets/ccfa-skills-review-boundaries.zh-CN.svg)

详细文档：[SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md)、[ARCHITECTURE.md](docs/ARCHITECTURE.md)、[INSTALLATION_MATRIX.zh-CN.md](docs/INSTALLATION_MATRIX.zh-CN.md)、[NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md)。
