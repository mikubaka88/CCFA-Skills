#!/usr/bin/env python3
"""Generate CCFA documentation SVG diagrams.

The generator is the source of truth. Do not hand-edit generated SVG files
without backporting the change here.
"""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
W = 1800

NAVY = "#102033"
BG = "#F3F6F9"
INK = "#17212B"
MUTED = "#536171"
LINE = "#CAD4DE"
WHITE = "#FFFFFF"

COLORS = {
    "setup": "#1E7894",
    "idea": "#C05C35",
    "evidence": "#6F5AA6",
    "writing": "#333B46",
    "review": "#A78328",
    "audit": "#854B82",
    "submission": "#BA4C5E",
    "post": "#477AA6",
    "gov": "#5A6672",
}

SKILLS = [
    ("ccf-project-scaffolder", "setup"),
    ("ccf-pipeline-orchestrator", "setup"),
    ("ccf-idea-optimizer", "idea"),
    ("ccf-idea-reviewer", "idea"),
    ("ccf-literature-searcher", "evidence"),
    ("ccf-experiment-designer", "evidence"),
    ("ccf-paper-writer", "writing"),
    ("ccf-paper-reviewer", "review"),
    ("ccf-integrity-auditor", "audit"),
    ("ccf-submission-checker", "submission"),
    ("ccf-rebuttal-writer", "post"),
    ("ccf-common", "gov"),
    ("ccf-skill-forger", "gov"),
]

ROLE = {
    "en": {
        "ccf-project-scaffolder": "workspace + ccfa.yaml",
        "ccf-pipeline-orchestrator": "plan + gates",
        "ccf-idea-optimizer": "shape idea",
        "ccf-idea-reviewer": "score idea",
        "ccf-literature-searcher": "find evidence",
        "ccf-experiment-designer": "experiments + result tables",
        "ccf-paper-writer": "write + compress + present",
        "ccf-paper-reviewer": "science + writing review",
        "ccf-integrity-auditor": "claims + citations",
        "ccf-submission-checker": "venue + package + artifact",
        "ccf-rebuttal-writer": "responses + resubmission",
        "ccf-common": "shared policy",
        "ccf-skill-forger": "skills + docs SVG",
    },
    "zh-CN": {
        "ccf-project-scaffolder": "项目 + ccfa.yaml",
        "ccf-pipeline-orchestrator": "流程 + gate",
        "ccf-idea-optimizer": "优化 idea",
        "ccf-idea-reviewer": "评分取舍",
        "ccf-literature-searcher": "找文献证据",
        "ccf-experiment-designer": "实验 + 结果图表",
        "ccf-paper-writer": "写作 + 压缩 + 展示",
        "ccf-paper-reviewer": "科学 + 写作评审",
        "ccf-integrity-auditor": "claim + 引用",
        "ccf-submission-checker": "会议 + 投稿包 + artifact",
        "ccf-rebuttal-writer": "回复 + 重投",
        "ccf-common": "共享治理",
        "ccf-skill-forger": "skills + 文档 SVG",
    },
    "zh-TW": {
        "ccf-project-scaffolder": "專案 + ccfa.yaml",
        "ccf-pipeline-orchestrator": "流程 + gate",
        "ccf-idea-optimizer": "優化 idea",
        "ccf-idea-reviewer": "評分取捨",
        "ccf-literature-searcher": "找文獻證據",
        "ccf-experiment-designer": "實驗 + 結果圖表",
        "ccf-paper-writer": "寫作 + 壓縮 + 展示",
        "ccf-paper-reviewer": "科學 + 寫作評審",
        "ccf-integrity-auditor": "claim + 引用",
        "ccf-submission-checker": "會議 + 投稿包 + artifact",
        "ccf-rebuttal-writer": "回覆 + 重投",
        "ccf-common": "共享治理",
        "ccf-skill-forger": "skills + 文件 SVG",
    },
}

LANG = {
    "en": {
        "suffix": "",
        "font": "Inter, Segoe UI, Arial, sans-serif",
        "arch": ("CCFA Skills Architecture", "13 runtime skills, one owner per stage, helper abilities as modes."),
        "workflow": ("Paper Project Workflow", "Default path from original idea to NeurIPS-style rebuttal."),
        "catalog": ("Runtime Skill Catalog", "The installable surface after helper-skill consolidation."),
        "routing": ("Routing Boundaries", "Similar prompts now route to one owner skill, not helper fragments."),
        "artifacts": ("Artifact Contract", "Shared state connects idea, evidence, manuscript, review, submission, and rebuttal."),
        "review": ("Review And Audit Boundaries", "Separate judgment, integrity, submission, and writing actions."),
        "install": ("Installation Sets", "Partial installs are supported, but ccf-common is always required."),
        "demo": ("Attention Demo", "Original Transformer paper -> CCFA idea, writing, review, and rebuttal dry run."),
    },
    "zh-CN": {
        "suffix": ".zh-CN",
        "font": "Microsoft YaHei, Segoe UI, Arial, sans-serif",
        "arch": ("CCFA Skills 架构", "13 个 runtime skills，每个阶段一个 owner，helper 能力并入 mode。"),
        "workflow": ("论文项目流程", "从原始 idea 到 NeurIPS 风格 rebuttal 的默认路径。"),
        "catalog": ("Runtime Skill 总览", "合并 helper skills 后的可安装入口。"),
        "routing": ("路由边界", "相似请求只进入一个 owner skill，不再分散到 helper。"),
        "artifacts": ("Artifact 合约", "共享状态串联 idea、证据、正文、审稿、投稿和 rebuttal。"),
        "review": ("评审与审计边界", "区分判断、完整性、投稿检查和写作修改。"),
        "install": ("安装组合", "支持部分安装，但任何组合都必须包含 ccf-common。"),
        "demo": ("Attention Demo", "Transformer 原文 -> CCFA idea、写作、审稿、rebuttal dry run。"),
    },
    "zh-TW": {
        "suffix": ".zh-TW",
        "font": "Microsoft JhengHei, Segoe UI, Arial, sans-serif",
        "arch": ("CCFA Skills 架構", "13 個 runtime skills，每個階段一個 owner，helper 能力併入 mode。"),
        "workflow": ("論文專案流程", "從原始 idea 到 NeurIPS 風格 rebuttal 的預設路徑。"),
        "catalog": ("Runtime Skill 總覽", "合併 helper skills 後的可安裝入口。"),
        "routing": ("路由邊界", "相似請求只進入一個 owner skill，不再分散到 helper。"),
        "artifacts": ("Artifact 合約", "共享狀態串聯 idea、證據、正文、審稿、投稿和 rebuttal。"),
        "review": ("評審與稽核邊界", "區分判斷、完整性、投稿檢查和寫作修改。"),
        "install": ("安裝組合", "支援部分安裝，但任何組合都必須包含 ccf-common。"),
        "demo": ("Attention Demo", "Transformer 原文 -> CCFA idea、寫作、審稿、rebuttal dry run。"),
    },
}


def e(value: str) -> str:
    return escape(value, quote=False)


def text(x: int, y: int, value: str, size: int, weight: int = 500, fill: str = INK, anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{e(value)}</text>'


def rect(x: int, y: int, w: int, h: int, fill: str, stroke: str = "none", rx: int = 18, extra: str = "") -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" {extra}/>'


def line(x1: int, y1: int, x2: int, y2: int, arrow: bool = False, color: str = LINE, width: int = 3) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{marker}/>'


def start(height: int, lang: str, key: str) -> list[str]:
    title, sub = LANG[lang][key]
    font = LANG[lang]["font"]
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">',
        "<defs>",
        '<filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#0B1826" flood-opacity="0.12"/></filter>',
        '<marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M2,2 L10,6 L2,10 Z" fill="#8D9AA8"/></marker>',
        "</defs>",
        f'<style>text{{font-family:{font};dominant-baseline:auto}} .mono{{font-family:Consolas,Menlo,monospace}}</style>',
        rect(0, 0, W, height, BG, "none", 0),
        rect(0, 0, W, 170, NAVY, "none", 0),
        text(70, 72, title, 38, 820, WHITE),
        text(70, 112, sub, 18, 450, "#D6E1EC"),
    ]


def finish(parts: list[str], name: str, lang: str) -> None:
    parts.append("</svg>")
    suffix = LANG[lang]["suffix"]
    (ASSETS / f"ccfa-skills-{name}{suffix}.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")


def skill_card(parts: list[str], x: int, y: int, skill: str, lang: str, w: int = 380) -> None:
    color = COLORS[dict(SKILLS)[skill]]
    parts.append(rect(x, y, w, 64, WHITE, color, 14, 'filter="url(#shadow)"'))
    parts.append(f'<circle cx="{x + 24}" cy="{y + 32}" r="7" fill="{color}"/>')
    parts.append(text(x + 44, y + 27, skill, 15, 780))
    parts.append(text(x + 44, y + 48, ROLE[lang][skill], 13, 500, MUTED))


def band(parts: list[str], x: int, y: int, label: str, color: str, w: int = 300) -> None:
    parts.append(rect(x, y, w, 44, color, "none", 22))
    parts.append(text(x + 24, y + 29, label, 17, 820, WHITE))


def build_architecture(lang: str) -> None:
    parts = start(1040, lang, "arch")
    labels = {
        "en": ["Project", "Idea", "Evidence", "Manuscript", "Assurance", "Submission", "Governance"],
        "zh-CN": ["项目", "选题", "证据", "写作", "保障", "投稿", "治理"],
        "zh-TW": ["專案", "選題", "證據", "寫作", "保障", "投稿", "治理"],
    }[lang]
    groups = [
        (labels[0], 80, 240, ["ccf-project-scaffolder", "ccf-pipeline-orchestrator"], COLORS["setup"]),
        (labels[1], 520, 240, ["ccf-idea-optimizer", "ccf-idea-reviewer"], COLORS["idea"]),
        (labels[2], 960, 240, ["ccf-literature-searcher", "ccf-experiment-designer"], COLORS["evidence"]),
        (labels[3], 1400, 240, ["ccf-paper-writer"], COLORS["writing"]),
        (labels[4], 300, 610, ["ccf-paper-reviewer", "ccf-integrity-auditor"], COLORS["review"]),
        (labels[5], 830, 610, ["ccf-submission-checker", "ccf-rebuttal-writer"], COLORS["submission"]),
        (labels[6], 1360, 610, ["ccf-common", "ccf-skill-forger"], COLORS["gov"]),
    ]
    for label, x, y, skills, color in groups:
        band(parts, x, y, label, color, 340)
        for i, skill in enumerate(skills):
            skill_card(parts, x, y + 66 + i * 84, skill, lang, 390)
    parts.append(rect(650, 455, 500, 125, NAVY, "none", 26, 'filter="url(#shadow)"'))
    parts.append(text(900, 505, "ccfa.yaml", 34, 850, WHITE, "middle"))
    parts.append(text(900, 544, "state / artifacts / gates / handoffs", 16, 500, "#CFE0EF", "middle"))
    finish(parts, "architecture", lang)


def build_workflow(lang: str) -> None:
    parts = start(900, lang, "workflow")
    labels = {
        "en": ["setup", "plan", "idea", "literature", "experiment", "write", "review", "submit", "respond"],
        "zh-CN": ["搭建", "规划", "idea", "文献", "实验", "写作", "审稿", "投稿", "回复"],
        "zh-TW": ["搭建", "規劃", "idea", "文獻", "實驗", "寫作", "審稿", "投稿", "回覆"],
    }[lang]
    flow = [
        ("ccf-project-scaffolder", COLORS["setup"]),
        ("ccf-pipeline-orchestrator", COLORS["setup"]),
        ("ccf-idea-optimizer", COLORS["idea"]),
        ("ccf-literature-searcher", COLORS["evidence"]),
        ("ccf-experiment-designer", COLORS["evidence"]),
        ("ccf-paper-writer", COLORS["writing"]),
        ("ccf-paper-reviewer", COLORS["review"]),
        ("ccf-submission-checker", COLORS["submission"]),
        ("ccf-rebuttal-writer", COLORS["post"]),
    ]
    x0, y = 90, 300
    for i, (skill, color) in enumerate(flow):
        x = x0 + i * 190
        parts.append(f'<circle cx="{x}" cy="{y}" r="46" fill="{color}" filter="url(#shadow)"/>')
        parts.append(text(x, y + 10, str(i + 1), 30, 850, WHITE, "middle"))
        parts.append(text(x - 70, y + 85, labels[min(i, len(labels) - 1)], 20, 800, INK))
        parts.append(text(x - 70, y + 114, skill.replace("ccf-", ""), 13, 600, MUTED))
        if i < len(flow) - 1:
            parts.append(line(x + 55, y, x + 135, y, arrow=True))
    side = [
        ("ccf-idea-reviewer", 360, 610),
        ("ccf-integrity-auditor", 780, 610),
        ("ccf-common", 1200, 610),
        ("ccf-skill-forger", 1200, 710),
    ]
    for skill, x, yy in side:
        skill_card(parts, x, yy, skill, lang, 360)
    finish(parts, "workflow", lang)


def build_catalog(lang: str) -> None:
    parts = start(1080, lang, "catalog")
    cols = [(80, 240), (520, 240), (960, 240), (1400, 240)]
    groups = [
        ("Project", ["ccf-project-scaffolder", "ccf-pipeline-orchestrator", "ccf-common"]),
        ("Idea", ["ccf-idea-optimizer", "ccf-idea-reviewer", "ccf-literature-searcher"]),
        ("Paper", ["ccf-experiment-designer", "ccf-paper-writer", "ccf-paper-reviewer"]),
        ("Deliver", ["ccf-integrity-auditor", "ccf-submission-checker", "ccf-rebuttal-writer", "ccf-skill-forger"]),
    ]
    group_names = {
        "zh-CN": {"Project": "项目", "Idea": "研究", "Paper": "论文", "Deliver": "交付"},
        "zh-TW": {"Project": "專案", "Idea": "研究", "Paper": "論文", "Deliver": "交付"},
        "en": {"Project": "Project", "Idea": "Research", "Paper": "Paper", "Deliver": "Deliver"},
    }[lang]
    for (group, skills), (x, y) in zip(groups, cols):
        band(parts, x, y, group_names[group], COLORS[dict(SKILLS)[skills[0]]], 320)
        for i, skill in enumerate(skills):
            skill_card(parts, x, y + 70 + i * 86, skill, lang, 370)
    finish(parts, "catalog", lang)


def build_routing(lang: str) -> None:
    parts = start(970, lang, "routing")
    pairs = {
        "en": [
            ("Rough idea", "ccf-idea-optimizer", "Idea ranking", "ccf-idea-reviewer"),
            ("New literature", "ccf-literature-searcher", "Existing citations", "ccf-integrity-auditor"),
            ("Experiment plan", "ccf-experiment-designer", "Paper text", "ccf-paper-writer"),
            ("Review judgment", "ccf-paper-reviewer", "Submission package", "ccf-submission-checker"),
            ("Reviewer response", "ccf-rebuttal-writer", "Skill/docs/SVG", "ccf-skill-forger"),
        ],
        "zh-CN": [
            ("优化粗 idea", "ccf-idea-optimizer", "给 idea 排名", "ccf-idea-reviewer"),
            ("找新文献", "ccf-literature-searcher", "核验已引用", "ccf-integrity-auditor"),
            ("实验计划", "ccf-experiment-designer", "论文正文", "ccf-paper-writer"),
            ("审稿判断", "ccf-paper-reviewer", "投稿包检查", "ccf-submission-checker"),
            ("回复审稿人", "ccf-rebuttal-writer", "维护 skill/SVG", "ccf-skill-forger"),
        ],
        "zh-TW": [
            ("優化粗 idea", "ccf-idea-optimizer", "給 idea 排名", "ccf-idea-reviewer"),
            ("找新文獻", "ccf-literature-searcher", "核驗已引用", "ccf-integrity-auditor"),
            ("實驗計畫", "ccf-experiment-designer", "論文正文", "ccf-paper-writer"),
            ("審稿判斷", "ccf-paper-reviewer", "投稿包檢查", "ccf-submission-checker"),
            ("回覆審稿人", "ccf-rebuttal-writer", "維護 skill/SVG", "ccf-skill-forger"),
        ],
    }[lang]
    for i, (l1, s1, l2, s2) in enumerate(pairs):
        y = 235 + i * 130
        parts.append(rect(90, y, 690, 96, WHITE, COLORS[dict(SKILLS)[s1]], 20, 'filter="url(#shadow)"'))
        parts.append(text(120, y + 38, l1, 20, 820))
        parts.append(text(120, y + 68, s1, 16, 760, COLORS[dict(SKILLS)[s1]]))
        parts.append(text(900, y + 58, "vs", 28, 850, MUTED, "middle"))
        parts.append(rect(1020, y, 690, 96, WHITE, COLORS[dict(SKILLS)[s2]], 20, 'filter="url(#shadow)"'))
        parts.append(text(1050, y + 38, l2, 20, 820))
        parts.append(text(1050, y + 68, s2, 16, 760, COLORS[dict(SKILLS)[s2]]))
    finish(parts, "routing", lang)


def build_artifacts(lang: str) -> None:
    parts = start(900, lang, "artifacts")
    nodes = [
        ("ccfa.yaml", "ccf-project-scaffolder / orchestrator", 650, 270, NAVY),
        ("idea.md", "ccf-idea-optimizer", 110, 500, COLORS["idea"]),
        ("evidence.md", "ccf-literature-searcher / experiment", 510, 500, COLORS["evidence"]),
        ("paper.tex", "ccf-paper-writer", 910, 500, COLORS["writing"]),
        ("review.md", "ccf-paper-reviewer / integrity", 1310, 500, COLORS["review"]),
        ("submission/", "ccf-submission-checker", 510, 700, COLORS["submission"]),
        ("rebuttal.tex", "ccf-rebuttal-writer", 910, 700, COLORS["post"]),
    ]
    for title, owner, x, y, color in nodes:
        parts.append(rect(x, y, 330, 105, WHITE if title != "ccfa.yaml" else NAVY, color, 22, 'filter="url(#shadow)"'))
        fill = WHITE if title == "ccfa.yaml" else INK
        subfill = "#D6E1EC" if title == "ccfa.yaml" else MUTED
        parts.append(text(x + 28, y + 42, title, 24, 820, fill))
        parts.append(text(x + 28, y + 73, owner, 14, 550, subfill))
    for x1, y1, x2, y2 in [(815, 375, 275, 500), (815, 375, 675, 500), (815, 375, 1075, 500), (815, 375, 1475, 500), (675, 605, 675, 700), (1075, 605, 1075, 700)]:
        parts.append(line(x1, y1, x2, y2, arrow=True))
    finish(parts, "artifacts", lang)


def build_review(lang: str) -> None:
    parts = start(850, lang, "review")
    cards = {
        "en": [
            ("Judgment", "ccf-paper-reviewer", "novelty · soundness · writing · score"),
            ("Integrity", "ccf-integrity-auditor", "claims · numbers · citations"),
            ("Action", "ccf-paper-writer", "revise · compress · present"),
            ("Package", "ccf-submission-checker", "venue · PDF · artifact"),
            ("Response", "ccf-rebuttal-writer", "rebuttal · ledger · resubmit"),
        ],
        "zh-CN": [
            ("判断", "ccf-paper-reviewer", "创新性 · 正确性 · 写作 · 评分"),
            ("完整性", "ccf-integrity-auditor", "claim · 数字 · 引用"),
            ("修改", "ccf-paper-writer", "重写 · 压缩 · 展示"),
            ("投稿", "ccf-submission-checker", "会议 · PDF · artifact"),
            ("回复", "ccf-rebuttal-writer", "rebuttal · ledger · 重投"),
        ],
        "zh-TW": [
            ("判斷", "ccf-paper-reviewer", "創新性 · 正確性 · 寫作 · 評分"),
            ("完整性", "ccf-integrity-auditor", "claim · 數字 · 引用"),
            ("修改", "ccf-paper-writer", "重寫 · 壓縮 · 展示"),
            ("投稿", "ccf-submission-checker", "會議 · PDF · artifact"),
            ("回覆", "ccf-rebuttal-writer", "rebuttal · ledger · 重投"),
        ],
    }[lang]
    for i, (title, skill, note) in enumerate(cards):
        x = 90 + (i % 3) * 560
        y = 260 + (i // 3) * 240
        color = COLORS[dict(SKILLS)[skill]]
        parts.append(rect(x, y, 480, 160, WHITE, "none", 26, 'filter="url(#shadow)"'))
        band(parts, x, y, title, color, 480)
        parts.append(text(x + 34, y + 92, skill, 22, 820))
        parts.append(text(x + 34, y + 126, note, 16, 550, MUTED))
    finish(parts, "review-boundaries", lang)


def build_install(lang: str) -> None:
    parts = start(850, lang, "install")
    cards = {
        "en": [
            ("Required", ["ccf-common", "all subsets need it"], COLORS["gov"]),
            ("Full workflow", ["all 13 runtime skills", "end-to-end paper project"], COLORS["setup"]),
            ("Writing subset", ["writer · reviewer · submission", "plus ccf-common"], COLORS["writing"]),
            ("Review subset", ["paper-reviewer · integrity", "diagnose, do not rewrite"], COLORS["review"]),
            ("Do not install", ["merged helper names", "avoid trigger collisions"], COLORS["submission"]),
            ("Maintenance", ["ccf-skill-forger", "skills · docs · SVG · release"], COLORS["gov"]),
        ],
        "zh-CN": [
            ("必须安装", ["ccf-common", "所有子集都需要"], COLORS["gov"]),
            ("全流程", ["13 个 runtime skills", "端到端论文项目"], COLORS["setup"]),
            ("写作子集", ["writer · reviewer · submission", "再加 ccf-common"], COLORS["writing"]),
            ("审稿子集", ["paper-reviewer · integrity", "诊断，不直接改写"], COLORS["review"]),
            ("不要安装", ["已合并 helper 名称", "避免触发冲突"], COLORS["submission"]),
            ("维护", ["ccf-skill-forger", "skills · docs · SVG · release"], COLORS["gov"]),
        ],
        "zh-TW": [
            ("必須安裝", ["ccf-common", "所有子集都需要"], COLORS["gov"]),
            ("全流程", ["13 個 runtime skills", "端到端論文專案"], COLORS["setup"]),
            ("寫作子集", ["writer · reviewer · submission", "再加 ccf-common"], COLORS["writing"]),
            ("審稿子集", ["paper-reviewer · integrity", "診斷，不直接改寫"], COLORS["review"]),
            ("不要安裝", ["已合併 helper 名稱", "避免觸發衝突"], COLORS["submission"]),
            ("維護", ["ccf-skill-forger", "skills · docs · SVG · release"], COLORS["gov"]),
        ],
    }[lang]
    for i, (title, lines, color) in enumerate(cards):
        x = 90 + (i % 3) * 560
        y = 250 + (i // 3) * 250
        parts.append(rect(x, y, 480, 165, WHITE, "none", 28, 'filter="url(#shadow)"'))
        band(parts, x, y, title, color, 480)
        parts.append(text(x + 34, y + 92, lines[0], 22, 820))
        parts.append(text(x + 34, y + 126, lines[1], 17, 580, MUTED))
    finish(parts, "installation", lang)


def build_demo(lang: str) -> None:
    parts = start(930, lang, "demo")
    metric = {
        "en": [("28.4", "EN-DE BLEU", "Transformer big"), ("41.0", "EN-FR BLEU", "single model"), ("8x P100", "training hardware", "paper setting"), ("3.5 days", "big EN-DE", "300K steps")],
        "zh-CN": [("28.4", "EN-DE BLEU", "Transformer big"), ("41.0", "EN-FR BLEU", "单模型"), ("8x P100", "训练硬件", "论文设置"), ("3.5 天", "big EN-DE", "300K steps")],
        "zh-TW": [("28.4", "EN-DE BLEU", "Transformer big"), ("41.0", "EN-FR BLEU", "單模型"), ("8x P100", "訓練硬體", "論文設定"), ("3.5 天", "big EN-DE", "300K steps")],
    }[lang]
    for i, (num, title, sub) in enumerate(metric):
        x = 90 + i * 420
        color = [COLORS["idea"], COLORS["evidence"], COLORS["setup"], COLORS["post"]][i]
        parts.append(rect(x, 245, 350, 170, WHITE, "none", 30, 'filter="url(#shadow)"'))
        parts.append(text(x + 34, 315, num, 44, 850, color))
        parts.append(text(x + 34, 354, title, 22, 820))
        parts.append(text(x + 34, 390, sub, 16, 500, MUTED))
    labels = {
        "en": [("read", "original paper"), ("idea", "attention-only seq2seq"), ("write", "NeurIPS story"), ("review", "score + audit"), ("rebuttal", "response plan")],
        "zh-CN": [("读取", "原文"), ("idea", "attention-only seq2seq"), ("写作", "NeurIPS story"), ("审稿", "评分 + 审计"), ("rebuttal", "回复计划")],
        "zh-TW": [("讀取", "原文"), ("idea", "attention-only seq2seq"), ("寫作", "NeurIPS story"), ("審稿", "評分 + 稽核"), ("rebuttal", "回覆計畫")],
    }[lang]
    xs = [120, 450, 780, 1110, 1440]
    for i, (title, sub) in enumerate(labels):
        color = [COLORS["setup"], COLORS["idea"], COLORS["writing"], COLORS["review"], COLORS["post"]][i]
        parts.append(f'<circle cx="{xs[i]}" cy="560" r="42" fill="{color}" filter="url(#shadow)"/>')
        parts.append(text(xs[i], 570, str(i + 1), 28, 850, WHITE, "middle"))
        parts.append(text(xs[i] + 66, 552, title, 22, 820))
        parts.append(text(xs[i] + 66, 586, sub, 16, 500, MUTED))
        if i < 4:
            parts.append(line(xs[i] + 108, 560, xs[i + 1] - 58, 560, arrow=True))
    parts.append(rect(410, 735, 980, 86, NAVY, "none", 22, 'filter="url(#shadow)"'))
    parts.append(text(900, 790, "demo/attention-is-all-you-need/", 28, 820, WHITE, "middle"))
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
        build_install,
        build_demo,
    ]
    for lang in LANG:
        for builder in builders:
            builder(lang)


if __name__ == "__main__":
    main()
