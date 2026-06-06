#!/usr/bin/env python3
"""Generate CCFA documentation SVG diagrams.

The generator is the source of truth. Do not hand-edit generated SVG files
without backporting the change here.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
W = 1800

BG = "#F6F8FB"
PANEL = "#FFFFFF"
INK = "#15202B"
MUTED = "#5A6775"
SOFT = "#E5ECF3"
NAVY = "#102033"
BLUE = "#1F6F8B"

COLORS = {
    "setup": "#1F7A8C",
    "idea": "#D2673D",
    "evidence": "#6657A8",
    "writing": "#2D3742",
    "review": "#B58B2A",
    "audit": "#8A4F86",
    "submission": "#BA4C5E",
    "post": "#477AA6",
    "gov": "#5D6977",
}

SKILL_STAGE = {
    "ccf-project-scaffolder": "setup",
    "ccf-pipeline-orchestrator": "setup",
    "ccf-idea-optimizer": "idea",
    "ccf-idea-reviewer": "idea",
    "ccf-literature-searcher": "evidence",
    "ccf-experiment-designer": "evidence",
    "ccf-paper-writer": "writing",
    "ccf-paper-reviewer": "review",
    "ccf-integrity-auditor": "audit",
    "ccf-submission-checker": "submission",
    "ccf-rebuttal-writer": "post",
    "ccf-common": "gov",
    "ccf-skill-forger": "gov",
}

SKILLS = list(SKILL_STAGE)

LANG = {
    "en": {
        "suffix": "",
        "font": "Inter, Segoe UI, Arial, sans-serif",
        "tag": "v0.4.5 · 13 owner skills · one paper-project loop",
        "architecture": ("CCFA Skill Family Logic", "Main research chain, shared state, governance, and revision loop."),
        "workflow": ("End-to-End Paper Workflow", "Every stage leaves a concrete artifact and hands off to one owner."),
        "catalog": ("Installable Runtime Skills", "The consolidated 13-skill surface after helper modes were merged."),
        "routing": ("Routing Boundaries", "Similar prompts route to one owner skill to avoid trigger conflicts."),
        "artifacts": ("Artifact Contract", "ccfa.yaml and files connect idea, evidence, manuscript, reviews, package, and rebuttal."),
        "review": ("Review, Audit, And Action Boundaries", "Judgment, factual integrity, package readiness, rewriting, and response stay separate."),
        "installation": ("Installation Sets", "Partial installs are supported, but ccf-common is always required."),
        "demo": ("Attention Demo Loop", "Original Transformer paper to ICLR-style writing, review, rebuttal, and checks."),
    },
    "zh-CN": {
        "suffix": ".zh-CN",
        "font": "Microsoft YaHei, Segoe UI, Arial, sans-serif",
        "tag": "v0.4.5 · 13 个 owner skills · 一个论文项目闭环",
        "architecture": ("CCFA 技能家族逻辑", "主研究链路、共享状态、治理层和修改回路。"),
        "workflow": ("端到端论文流程", "每个阶段都留下具体 artifact，并交给唯一 owner。"),
        "catalog": ("可安装 Runtime Skills", "helper 能力合并后的 13 个可安装入口。"),
        "routing": ("路由边界", "相似请求只进入一个 owner skill，避免触发冲突。"),
        "artifacts": ("Artifact 合约", "ccfa.yaml 与文件串联 idea、证据、正文、评审、投稿包和 rebuttal。"),
        "review": ("评审、审计与行动边界", "判断、事实完整性、投稿检查、改写和回应分开处理。"),
        "installation": ("安装组合", "支持部分安装，但任何组合都必须包含 ccf-common。"),
        "demo": ("Attention Demo 闭环", "从 Transformer 原文到 ICLR 风格写作、评审、rebuttal 与检查。"),
    },
    "zh-TW": {
        "suffix": ".zh-TW",
        "font": "Microsoft JhengHei, Segoe UI, Arial, sans-serif",
        "tag": "v0.4.5 · 13 個 owner skills · 一個論文專案閉環",
        "architecture": ("CCFA 技能家族邏輯", "主研究鏈路、共享狀態、治理層和修改回路。"),
        "workflow": ("端到端論文流程", "每個階段都留下具體 artifact，並交給唯一 owner。"),
        "catalog": ("可安裝 Runtime Skills", "helper 能力合併後的 13 個可安裝入口。"),
        "routing": ("路由邊界", "相似請求只進入一個 owner skill，避免觸發衝突。"),
        "artifacts": ("Artifact 合約", "ccfa.yaml 與檔案串聯 idea、證據、正文、審稿、投稿包和 rebuttal。"),
        "review": ("審稿、稽核與行動邊界", "判斷、事實完整性、投稿檢查、改寫和回應分開處理。"),
        "installation": ("安裝組合", "支援部分安裝，但任何組合都必須包含 ccf-common。"),
        "demo": ("Attention Demo 閉環", "從 Transformer 原文到 ICLR 風格寫作、審稿、rebuttal 與檢查。"),
    },
}

ROLE = {
    "en": {
        "ccf-project-scaffolder": "project folders, template, ccfa.yaml",
        "ccf-pipeline-orchestrator": "stage plan, gates, handoffs",
        "ccf-idea-optimizer": "problem, gap, insight, method",
        "ccf-idea-reviewer": "score, rank, reject risk",
        "ccf-literature-searcher": "prior art, datasets, benchmarks",
        "ccf-experiment-designer": "baselines, ablations, real tables",
        "ccf-paper-writer": "draft, revise, compress, present",
        "ccf-paper-reviewer": "science and writing review",
        "ccf-integrity-auditor": "claims, numbers, citations",
        "ccf-submission-checker": "venue, PDF, anonymity, artifacts",
        "ccf-rebuttal-writer": "response, ledger, resubmission",
        "ccf-common": "routing, policy, source registry",
        "ccf-skill-forger": "skills, docs, diagrams, release",
    },
    "zh-CN": {
        "ccf-project-scaffolder": "目录、模板、ccfa.yaml",
        "ccf-pipeline-orchestrator": "阶段计划、gate、handoff",
        "ccf-idea-optimizer": "问题、gap、insight、方法",
        "ccf-idea-reviewer": "评分、排序、拒稿风险",
        "ccf-literature-searcher": "prior art、数据集、benchmark",
        "ccf-experiment-designer": "baseline、消融、真实结果表",
        "ccf-paper-writer": "起草、润色、压缩、展示",
        "ccf-paper-reviewer": "科学评审和写作评审",
        "ccf-integrity-auditor": "claim、数字、引用",
        "ccf-submission-checker": "会议、PDF、匿名、artifact",
        "ccf-rebuttal-writer": "回应、ledger、重投",
        "ccf-common": "路由、策略、source registry",
        "ccf-skill-forger": "skills、文档、图、release",
    },
    "zh-TW": {
        "ccf-project-scaffolder": "目錄、模板、ccfa.yaml",
        "ccf-pipeline-orchestrator": "階段計畫、gate、handoff",
        "ccf-idea-optimizer": "問題、gap、insight、方法",
        "ccf-idea-reviewer": "評分、排序、拒稿風險",
        "ccf-literature-searcher": "prior art、資料集、benchmark",
        "ccf-experiment-designer": "baseline、消融、真實結果表",
        "ccf-paper-writer": "起草、潤飾、壓縮、展示",
        "ccf-paper-reviewer": "科學審稿和寫作審稿",
        "ccf-integrity-auditor": "claim、數字、引用",
        "ccf-submission-checker": "會議、PDF、匿名、artifact",
        "ccf-rebuttal-writer": "回應、ledger、重投",
        "ccf-common": "路由、策略、source registry",
        "ccf-skill-forger": "skills、文件、圖、release",
    },
}


def esc(value: str) -> str:
    return escape(value, quote=False)


def rect(x: int, y: int, w: int, h: int, fill: str, stroke: str = "none", rx: int = 18, extra: str = "") -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" {extra}/>'


def line(x1: int, y1: int, x2: int, y2: int, color: str = "#94A3B8", width: int = 3, arrow: bool = True) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{marker}/>'


def path(d: str, color: str = "#94A3B8", width: int = 3, arrow: bool = True) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{marker}/>'


def text(x: int, y: int, value: str, size: int, weight: int = 500, fill: str = INK, anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(value)}</text>'


def wrap_lines(value: str, width: int) -> list[str]:
    if not value:
        return []
    if " " not in value and len(value) > width:
        return [value[i : i + width] for i in range(0, len(value), width)]
    return textwrap.wrap(value, width=width, break_long_words=False) or [value]


def wrapped_text(x: int, y: int, value: str, size: int, weight: int = 500, fill: str = INK, width: int = 30, line_gap: int = 22) -> list[str]:
    return [text(x, y + i * line_gap, line, size, weight, fill) for i, line in enumerate(wrap_lines(value, width))]


def start(height: int, lang: str, key: str) -> list[str]:
    title, subtitle = LANG[lang][key]
    font = LANG[lang]["font"]
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">',
        "<defs>",
        '<linearGradient id="header" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#102033"/><stop offset="0.58" stop-color="#1F6F8B"/><stop offset="1" stop-color="#7A4E9B"/></linearGradient>',
        '<filter id="shadow" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#0B1826" flood-opacity="0.13"/></filter>',
        '<marker id="arrow" markerWidth="13" markerHeight="13" refX="11" refY="6.5" orient="auto"><path d="M2,2 L11,6.5 L2,11 Z" fill="#7B8794"/></marker>',
        "</defs>",
        f'<style>text{{font-family:{font};dominant-baseline:auto}} .mono{{font-family:Consolas,Menlo,monospace}}</style>',
        rect(0, 0, W, height, BG, "none", 0),
        rect(0, 0, W, 158, "url(#header)", "none", 0),
        text(72, 66, title, 44, 850, "#FFFFFF"),
        text(72, 108, subtitle, 20, 500, "#D8E6F2"),
        text(W - 72, 132, LANG[lang]["tag"], 16, 650, "#D8E6F2", "end"),
    ]


def finish(parts: list[str], name: str, lang: str) -> None:
    parts.append("</svg>")
    suffix = LANG[lang]["suffix"]
    (ASSETS / f"ccfa-skills-{name}{suffix}.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")


def chip(parts: list[str], x: int, y: int, label: str, color: str, w: int = 210) -> None:
    parts.append(rect(x, y, w, 38, color, "none", 19))
    parts.append(text(x + w // 2, y + 25, label, 15, 760, "#FFFFFF", "middle"))


def skill_card(parts: list[str], x: int, y: int, skill: str, lang: str, w: int = 260, h: int = 92) -> None:
    color = COLORS[SKILL_STAGE[skill]]
    parts.append(rect(x, y, w, h, PANEL, "none", 18, 'filter="url(#shadow)"'))
    parts.append(rect(x, y, 8, h, color, "none", 18))
    parts.append(text(x + 24, y + 34, skill, 15, 820, INK))
    wrap_width = max(27, (w - 72) // 9)
    for line_i, line_text in enumerate(wrap_lines(ROLE[lang][skill], wrap_width)):
        parts.append(text(x + 24, y + 59 + line_i * 18, line_text, 13, 520, MUTED))


def stage_panel(parts: list[str], x: int, y: int, title: str, skills: list[str], lang: str, color: str, w: int = 260) -> None:
    h = 82 + len(skills) * 82
    parts.append(rect(x, y, w, h, "#FFFFFF", "none", 24, 'filter="url(#shadow)"'))
    parts.append(rect(x, y, w, 52, color, "none", 24))
    parts.append(text(x + 22, y + 34, title, 18, 820, "#FFFFFF"))
    for i, skill in enumerate(skills):
        skill_card(parts, x + 18, y + 70 + i * 82, skill, lang, w - 36, 66)


def build_architecture(lang: str) -> None:
    parts = start(1400, lang, "architecture")
    labels = {
        "en": ["Setup", "Idea Gate", "Evidence", "Manuscript", "Assurance", "Submit / Respond", "Revision loop", "shared project state", "Governance"],
        "zh-CN": ["搭建", "选题 Gate", "证据", "正文", "质量保障", "投稿 / 回应", "修改回路", "共享项目状态", "治理层"],
        "zh-TW": ["搭建", "選題 Gate", "證據", "正文", "品質保障", "投稿 / 回應", "修改回路", "共享專案狀態", "治理層"],
    }[lang]
    groups = [
        (labels[0], 70, 228, ["ccf-project-scaffolder", "ccf-pipeline-orchestrator"], COLORS["setup"]),
        (labels[1], 650, 228, ["ccf-idea-optimizer", "ccf-idea-reviewer"], COLORS["idea"]),
        (labels[2], 1230, 228, ["ccf-literature-searcher", "ccf-experiment-designer"], COLORS["evidence"]),
        (labels[3], 70, 560, ["ccf-paper-writer"], COLORS["writing"]),
        (labels[4], 650, 560, ["ccf-paper-reviewer", "ccf-integrity-auditor"], COLORS["review"]),
        (labels[5], 1230, 560, ["ccf-submission-checker", "ccf-rebuttal-writer"], COLORS["submission"]),
    ]
    for title, x, y, skills, color in groups:
        stage_panel(parts, x, y, title, skills, lang, color, 500)
    parts.append(line(570, 370, 650, 370))
    parts.append(line(1150, 370, 1230, 370))
    parts.append(path("M1480 492 C1480 530 320 530 320 560", "#94A3B8", 3))
    parts.append(line(570, 680, 650, 680))
    parts.append(line(1150, 680, 1230, 680))
    parts.append(path("M1480 828 C1420 910 390 910 320 828", COLORS["post"], 4))
    parts.append(text(900, 890, labels[6], 20, 820, COLORS["post"], "middle"))

    parts.append(rect(350, 930, 1100, 118, NAVY, "none", 30, 'filter="url(#shadow)"'))
    parts.append(text(900, 980, "ccfa.yaml", 36, 850, "#FFFFFF", "middle"))
    parts.append(text(900, 1015, labels[7], 18, 500, "#D8E6F2", "middle"))
    for i, item in enumerate(["idea", "literature", "experiments", "manuscript", "reviews", "submission", "ledger"]):
        chip(parts, 410 + i * 150, 1068, item, BLUE, 128)

    stage_panel(parts, 420, 1120, labels[8], ["ccf-common", "ccf-skill-forger"], lang, COLORS["gov"], 960)
    finish(parts, "architecture", lang)


def build_workflow(lang: str) -> None:
    parts = start(1040, lang, "workflow")
    steps = {
        "en": [
            ("Scaffold", "project tree + ccfa.yaml", "ccf-project-scaffolder"),
            ("Plan", "stage gates + owners", "ccf-pipeline-orchestrator"),
            ("Shape Idea", "problem-gap-insight", "ccf-idea-optimizer"),
            ("Stress Test", "score + risks", "ccf-idea-reviewer"),
            ("Evidence", "prior art + protocol", "ccf-literature-searcher"),
            ("Experiment", "baselines + tables", "ccf-experiment-designer"),
            ("Write", "venue-aware manuscript", "ccf-paper-writer"),
            ("Review", "scientific + writing report", "ccf-paper-reviewer"),
            ("Audit", "claims + citations", "ccf-integrity-auditor"),
            ("Submit", "PDF + anonymity + artifacts", "ccf-submission-checker"),
            ("Respond", "rebuttal + ledger", "ccf-rebuttal-writer"),
        ],
        "zh-CN": [
            ("搭建", "目录 + ccfa.yaml", "ccf-project-scaffolder"),
            ("规划", "阶段 gate + owner", "ccf-pipeline-orchestrator"),
            ("优化 idea", "问题-gap-insight", "ccf-idea-optimizer"),
            ("压力测试", "评分 + 风险", "ccf-idea-reviewer"),
            ("证据", "prior art + 协议", "ccf-literature-searcher"),
            ("实验", "baseline + 表格", "ccf-experiment-designer"),
            ("写作", "会议感知正文", "ccf-paper-writer"),
            ("评审", "科学 + 写作报告", "ccf-paper-reviewer"),
            ("审计", "claim + 引用", "ccf-integrity-auditor"),
            ("投稿", "PDF + 匿名 + artifact", "ccf-submission-checker"),
            ("回应", "rebuttal + ledger", "ccf-rebuttal-writer"),
        ],
        "zh-TW": [
            ("搭建", "目錄 + ccfa.yaml", "ccf-project-scaffolder"),
            ("規劃", "階段 gate + owner", "ccf-pipeline-orchestrator"),
            ("優化 idea", "問題-gap-insight", "ccf-idea-optimizer"),
            ("壓力測試", "評分 + 風險", "ccf-idea-reviewer"),
            ("證據", "prior art + 協議", "ccf-literature-searcher"),
            ("實驗", "baseline + 表格", "ccf-experiment-designer"),
            ("寫作", "會議感知正文", "ccf-paper-writer"),
            ("審稿", "科學 + 寫作報告", "ccf-paper-reviewer"),
            ("稽核", "claim + 引用", "ccf-integrity-auditor"),
            ("投稿", "PDF + 匿名 + artifact", "ccf-submission-checker"),
            ("回應", "rebuttal + ledger", "ccf-rebuttal-writer"),
        ],
    }[lang]
    for i, (title, artifact, skill) in enumerate(steps):
        col = i % 4
        row = i // 4
        x = 90 + col * 430
        y = 235 + row * 250
        color = COLORS[SKILL_STAGE[skill]]
        parts.append(rect(x, y, 360, 168, PANEL, "none", 24, 'filter="url(#shadow)"'))
        parts.append(f'<circle cx="{x + 45}" cy="{y + 45}" r="28" fill="{color}"/>')
        parts.append(text(x + 45, y + 55, str(i + 1), 24, 850, "#FFFFFF", "middle"))
        parts.append(text(x + 84, y + 42, title, 22, 840, INK))
        parts.append(text(x + 84, y + 73, artifact, 15, 560, MUTED))
        parts.append(text(x + 28, y + 128, skill, 15, 760, color))
        if i < len(steps) - 1:
            if col < 3:
                parts.append(line(x + 368, y + 84, x + 420, y + 84))
            else:
                parts.append(path(f"M{x + 180} {y + 178} C{x + 180} {y + 220}, 180 {y + 220}, 180 {y + 244}"))
    finish(parts, "workflow", lang)


def build_catalog(lang: str) -> None:
    parts = start(1100, lang, "catalog")
    group_defs = {
        "en": [
            ("Project Control", ["ccf-project-scaffolder", "ccf-pipeline-orchestrator", "ccf-common"]),
            ("Research Formation", ["ccf-idea-optimizer", "ccf-idea-reviewer", "ccf-literature-searcher"]),
            ("Evidence To Paper", ["ccf-experiment-designer", "ccf-paper-writer", "ccf-paper-reviewer"]),
            ("Delivery And Governance", ["ccf-integrity-auditor", "ccf-submission-checker", "ccf-rebuttal-writer", "ccf-skill-forger"]),
        ],
        "zh-CN": [
            ("项目控制", ["ccf-project-scaffolder", "ccf-pipeline-orchestrator", "ccf-common"]),
            ("研究成型", ["ccf-idea-optimizer", "ccf-idea-reviewer", "ccf-literature-searcher"]),
            ("证据到正文", ["ccf-experiment-designer", "ccf-paper-writer", "ccf-paper-reviewer"]),
            ("交付与治理", ["ccf-integrity-auditor", "ccf-submission-checker", "ccf-rebuttal-writer", "ccf-skill-forger"]),
        ],
        "zh-TW": [
            ("專案控制", ["ccf-project-scaffolder", "ccf-pipeline-orchestrator", "ccf-common"]),
            ("研究成型", ["ccf-idea-optimizer", "ccf-idea-reviewer", "ccf-literature-searcher"]),
            ("證據到正文", ["ccf-experiment-designer", "ccf-paper-writer", "ccf-paper-reviewer"]),
            ("交付與治理", ["ccf-integrity-auditor", "ccf-submission-checker", "ccf-rebuttal-writer", "ccf-skill-forger"]),
        ],
    }[lang]
    for i, (title, skills) in enumerate(group_defs):
        x = 70 + i * 435
        color = COLORS[SKILL_STAGE[skills[0]]]
        stage_panel(parts, x, 235, title, skills, lang, color, 380)
    finish(parts, "catalog", lang)


def build_routing(lang: str) -> None:
    parts = start(980, lang, "routing")
    pairs = {
        "en": [
            ("rough idea", "ccf-idea-optimizer", "rank or score ideas", "ccf-idea-reviewer"),
            ("find new papers", "ccf-literature-searcher", "audit cited papers", "ccf-integrity-auditor"),
            ("design experiments", "ccf-experiment-designer", "write manuscript text", "ccf-paper-writer"),
            ("judge paper quality", "ccf-paper-reviewer", "check submission package", "ccf-submission-checker"),
            ("answer reviewers", "ccf-rebuttal-writer", "maintain skills / SVG", "ccf-skill-forger"),
        ],
        "zh-CN": [
            ("优化粗 idea", "ccf-idea-optimizer", "给 idea 排名评分", "ccf-idea-reviewer"),
            ("找新文献", "ccf-literature-searcher", "审计已引用文献", "ccf-integrity-auditor"),
            ("设计实验", "ccf-experiment-designer", "写正文", "ccf-paper-writer"),
            ("判断论文质量", "ccf-paper-reviewer", "检查投稿包", "ccf-submission-checker"),
            ("回复审稿人", "ccf-rebuttal-writer", "维护 skills / SVG", "ccf-skill-forger"),
        ],
        "zh-TW": [
            ("優化粗 idea", "ccf-idea-optimizer", "給 idea 排名評分", "ccf-idea-reviewer"),
            ("找新文獻", "ccf-literature-searcher", "稽核已引用文獻", "ccf-integrity-auditor"),
            ("設計實驗", "ccf-experiment-designer", "寫正文", "ccf-paper-writer"),
            ("判斷論文品質", "ccf-paper-reviewer", "檢查投稿包", "ccf-submission-checker"),
            ("回覆審稿人", "ccf-rebuttal-writer", "維護 skills / SVG", "ccf-skill-forger"),
        ],
    }[lang]
    for i, (left, left_skill, right, right_skill) in enumerate(pairs):
        y = 230 + i * 135
        for x, label, skill in [(90, left, left_skill), (1000, right, right_skill)]:
            color = COLORS[SKILL_STAGE[skill]]
            parts.append(rect(x, y, 650, 104, PANEL, "none", 22, 'filter="url(#shadow)"'))
            chip(parts, x + 24, y + 24, label, color, 230)
            parts.append(text(x + 285, y + 47, skill, 20, 820, INK))
            parts.append(text(x + 285, y + 76, ROLE[lang][skill], 14, 520, MUTED))
        parts.append(text(900, y + 62, "vs", 28, 850, "#94A3B8", "middle"))
    finish(parts, "routing", lang)


def build_artifacts(lang: str) -> None:
    parts = start(920, lang, "artifacts")
    center = {
        "en": ("ccfa.yaml", "version · stage · target_venue · artifacts · claims · reviews · checks"),
        "zh-CN": ("ccfa.yaml", "version · stage · target_venue · artifacts · claims · reviews · checks"),
        "zh-TW": ("ccfa.yaml", "version · stage · target_venue · artifacts · claims · reviews · checks"),
    }[lang]
    parts.append(rect(570, 365, 660, 150, NAVY, "none", 32, 'filter="url(#shadow)"'))
    parts.append(text(900, 423, center[0], 40, 860, "#FFFFFF", "middle"))
    parts.append(text(900, 468, center[1], 16, 520, "#D8E6F2", "middle"))
    nodes = [
        ("idea_brief.md", "ccf-idea-optimizer", 90, 250),
        ("literature.md", "ccf-literature-searcher", 500, 230),
        ("experiments.md", "ccf-experiment-designer", 1220, 230),
        ("manuscript.tex", "ccf-paper-writer", 90, 610),
        ("review.md", "ccf-paper-reviewer", 500, 640),
        ("submission/", "ccf-submission-checker", 910, 640),
        ("rebuttal.tex", "ccf-rebuttal-writer", 1320, 610),
    ]
    for title, owner, x, y in nodes:
        color = COLORS[SKILL_STAGE[owner]]
        parts.append(rect(x, y, 330, 108, PANEL, "none", 22, 'filter="url(#shadow)"'))
        parts.append(text(x + 28, y + 42, title, 24, 820, INK))
        parts.append(text(x + 28, y + 75, owner, 14, 650, color))
        parts.append(line(900, 515 if y > 520 else 365, x + 165, y + 54, "#A7B2C0", 2))
    finish(parts, "artifacts", lang)


def build_review(lang: str) -> None:
    parts = start(900, lang, "review")
    rows = {
        "en": [
            ("Rewrite text", "ccf-paper-writer", "changes manuscript wording, structure, compression, slides"),
            ("Judge quality", "ccf-paper-reviewer", "scores novelty, soundness, clarity, reviewer risk"),
            ("Audit facts", "ccf-integrity-auditor", "verifies claims, numbers, citations, BibTeX support"),
            ("Check package", "ccf-submission-checker", "venue rules, PDF build, anonymity, metadata, artifact"),
            ("Answer reviews", "ccf-rebuttal-writer", "response letter, revision ledger, conservative resubmission"),
        ],
        "zh-CN": [
            ("改写正文", "ccf-paper-writer", "修改措辞、结构、压缩和展示材料"),
            ("判断质量", "ccf-paper-reviewer", "评估创新性、正确性、清晰度和审稿风险"),
            ("审计事实", "ccf-integrity-auditor", "核验 claim、数字、引用和 BibTeX 支撑"),
            ("检查投稿包", "ccf-submission-checker", "会议规则、PDF、匿名、metadata、artifact"),
            ("回应评审", "ccf-rebuttal-writer", "response letter、revision ledger、保守重投"),
        ],
        "zh-TW": [
            ("改寫正文", "ccf-paper-writer", "修改措辭、結構、壓縮和展示材料"),
            ("判斷品質", "ccf-paper-reviewer", "評估創新性、正確性、清晰度和審稿風險"),
            ("稽核事實", "ccf-integrity-auditor", "核驗 claim、數字、引用和 BibTeX 支撐"),
            ("檢查投稿包", "ccf-submission-checker", "會議規則、PDF、匿名、metadata、artifact"),
            ("回應審稿", "ccf-rebuttal-writer", "response letter、revision ledger、保守重投"),
        ],
    }[lang]
    for i, (action, skill, note) in enumerate(rows):
        y = 225 + i * 130
        color = COLORS[SKILL_STAGE[skill]]
        parts.append(rect(120, y, 1560, 96, PANEL, "none", 24, 'filter="url(#shadow)"'))
        chip(parts, 150, y + 26, action, color, 230)
        parts.append(text(440, y + 43, skill, 22, 840, INK))
        parts.append(text(440, y + 72, note, 16, 520, MUTED))
    finish(parts, "review-boundaries", lang)


def build_installation(lang: str) -> None:
    parts = start(900, lang, "installation")
    sets = {
        "en": [
            ("Required core", ["ccf-common", "routing, policies, artifact contract"], COLORS["gov"]),
            ("Full paper loop", ["all 13 runtime skills", "best for end-to-end research projects"], COLORS["setup"]),
            ("Writing subset", ["common + writer + reviewer + submission", "for draft, polish, format checks"], COLORS["writing"]),
            ("Early research subset", ["common + idea + literature + experiments", "for project planning before drafting"], COLORS["idea"]),
            ("Submission subset", ["common + writer + integrity + submission", "for final package readiness"], COLORS["submission"]),
            ("Do not install", ["merged helper skill names", "compression, talks, citation audit, venue guide"], COLORS["review"]),
        ],
        "zh-CN": [
            ("必装核心", ["ccf-common", "路由、策略、artifact 合约"], COLORS["gov"]),
            ("完整论文闭环", ["全部 13 个 runtime skills", "适合端到端研究项目"], COLORS["setup"]),
            ("写作子集", ["common + writer + reviewer + submission", "用于起草、润色、格式检查"], COLORS["writing"]),
            ("早期研究子集", ["common + idea + literature + experiments", "用于写稿前规划"], COLORS["idea"]),
            ("投稿子集", ["common + writer + integrity + submission", "用于最终投稿包检查"], COLORS["submission"]),
            ("不要安装", ["已合并 helper skill 名称", "压缩、报告、引用审计、venue guide"], COLORS["review"]),
        ],
        "zh-TW": [
            ("必裝核心", ["ccf-common", "路由、策略、artifact 合約"], COLORS["gov"]),
            ("完整論文閉環", ["全部 13 個 runtime skills", "適合端到端研究專案"], COLORS["setup"]),
            ("寫作子集", ["common + writer + reviewer + submission", "用於起草、潤飾、格式檢查"], COLORS["writing"]),
            ("早期研究子集", ["common + idea + literature + experiments", "用於寫稿前規劃"], COLORS["idea"]),
            ("投稿子集", ["common + writer + integrity + submission", "用於最終投稿包檢查"], COLORS["submission"]),
            ("不要安裝", ["已合併 helper skill 名稱", "壓縮、報告、引用稽核、venue guide"], COLORS["review"]),
        ],
    }[lang]
    for i, (title, lines, color) in enumerate(sets):
        x = 90 + (i % 3) * 560
        y = 245 + (i // 3) * 260
        parts.append(rect(x, y, 480, 172, PANEL, "none", 26, 'filter="url(#shadow)"'))
        chip(parts, x + 28, y + 28, title, color, 220)
        parts.append(text(x + 32, y + 98, lines[0], 23, 820, INK))
        parts.append(text(x + 32, y + 132, lines[1], 16, 520, MUTED))
    finish(parts, "installation", lang)


def build_demo(lang: str) -> None:
    parts = start(950, lang, "demo")
    metrics = [
        ("28.4", "WMT14 EN-DE BLEU", COLORS["idea"]),
        ("41.0", "WMT14 EN-FR BLEU", COLORS["evidence"]),
        ("8×P100", "official training hardware", COLORS["setup"]),
        ("ICLR", "demo target venue", COLORS["submission"]),
    ]
    for i, (num, label, color) in enumerate(metrics):
        x = 90 + i * 420
        parts.append(rect(x, 235, 350, 155, PANEL, "none", 28, 'filter="url(#shadow)"'))
        parts.append(text(x + 34, 302, num, 42, 860, color))
        for line_i, line_text in enumerate(wrap_lines(label, 24)):
            parts.append(text(x + 34, 340 + line_i * 22, line_text, 17, 560, MUTED))
    flow = {
        "en": [("Read", "source paper"), ("Extract", "motivation / problem / insight"), ("Review", "idea score"), ("Write", "full ICLR-style TeX"), ("Critique", "writing + science + integrity"), ("Respond", "rebuttal + submission check")],
        "zh-CN": [("读取", "原文"), ("提炼", "动机 / 问题 / insight"), ("评审", "idea 评分"), ("写作", "完整 ICLR 风格 TeX"), ("批评", "写作 + 科学 + 完整性"), ("回应", "rebuttal + 投稿检查")],
        "zh-TW": [("讀取", "原文"), ("提煉", "動機 / 問題 / insight"), ("審稿", "idea 評分"), ("寫作", "完整 ICLR 風格 TeX"), ("批評", "寫作 + 科學 + 完整性"), ("回應", "rebuttal + 投稿檢查")],
    }[lang]
    for i, (title, detail) in enumerate(flow):
        x = 92 + i * 285
        y = 555
        color = [COLORS["setup"], COLORS["idea"], COLORS["review"], COLORS["writing"], COLORS["audit"], COLORS["post"]][i]
        parts.append(f'<circle cx="{x}" cy="{y}" r="42" fill="{color}" filter="url(#shadow)"/>')
        parts.append(text(x, y + 10, str(i + 1), 28, 850, "#FFFFFF", "middle"))
        parts.append(text(x - 62, y + 92, title, 22, 820, INK))
        for line_i, line_text in enumerate(wrap_lines(detail, 22)):
            parts.append(text(x - 62, y + 123 + line_i * 19, line_text, 14, 520, MUTED))
        if i < len(flow) - 1:
            parts.append(line(x + 52, y, x + 225, y))
    parts.append(rect(360, 805, 1080, 72, NAVY, "none", 22, 'filter="url(#shadow)"'))
    parts.append(text(900, 850, "demo/attention-is-all-you-need/paper/attention_iclr_submission.tex", 21, 780, "#FFFFFF", "middle"))
    finish(parts, "demo-attention", lang)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    builders = [
        build_architecture,
        build_workflow,
        build_catalog,
        build_routing,
        build_artifacts,
        build_review,
        build_installation,
        build_demo,
    ]
    for lang in LANG:
        for builder in builders:
            builder(lang)


if __name__ == "__main__":
    main()
