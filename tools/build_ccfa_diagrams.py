from __future__ import annotations

import math
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


LANG = {
    "en": {
        "suffix": "",
        "title": "CCFA Skills family",
        "subtitle": "A coordinated skill family for CCF-style research papers",
        "groups": {
            "governance": "Governance",
            "ideation": "Ideation",
            "evidence": "Evidence",
            "writing": "Writing",
            "delivery": "Delivery",
            "maintenance": "Maintenance",
        },
    },
    "zh-CN": {
        "suffix": ".zh-CN",
        "title": "CCFA Skills 家族",
        "subtitle": "面向 CCF 论文研究的协作式 skill 家族",
        "groups": {
            "governance": "共同规则",
            "ideation": "选题",
            "evidence": "研究证据",
            "writing": "论文表达",
            "delivery": "图表与投稿",
            "maintenance": "家族完善",
        },
    },
    "zh-TW": {
        "suffix": ".zh-TW",
        "title": "CCFA Skills 家族",
        "subtitle": "面向 CCF 論文研究的協作式 skill 家族",
        "groups": {
            "governance": "共同規則",
            "ideation": "選題",
            "evidence": "研究證據",
            "writing": "論文表達",
            "delivery": "圖表與投稿",
            "maintenance": "家族完善",
        },
    },
}


PALETTE = {
    "ink": "#233044",
    "muted": "#667085",
    "line": "#D9E1F2",
    "bg": "#F8FAFF",
    "white": "#FFFFFF",
    "blue": "#DDEBFF",
    "blue2": "#7AA7FF",
    "purple": "#E9DFFF",
    "purple2": "#9D7BFF",
    "red": "#FFE1E1",
    "red2": "#FF8A8A",
    "green": "#DFF7EA",
    "green2": "#58C58A",
    "orange": "#FFE9C7",
    "orange2": "#FFB552",
}


ROLES = {
    "ccf-common": ("Shared rules", "共同规则", "共同規則"),
    "ccf-pipeline-orchestrator": ("Plan", "规划", "規劃"),
    "ccf-project-scaffolder": ("Project setup", "项目起步", "專案起步"),
    "ccf-idea-reviewer": ("Score ideas", "选题评分", "選題評分"),
    "ccf-idea-optimizer": ("Shape ideas", "优化选题", "優化選題"),
    "ccf-literature-searcher": ("Search literature", "文献检索", "文獻檢索"),
    "ccf-literature-monitor": ("Track new work", "前沿追踪", "前沿追蹤"),
    "ccf-experiment-designer": ("Design evidence", "实验设计", "實驗設計"),
    "ccf-integrity-auditor": ("Check integrity", "完整性核验", "完整性核驗"),
    "ccf-paper-reviewer": ("Independent review", "独立评审", "獨立評審"),
    "ccf-paper-writer": ("Write and revise", "写作改写", "寫作改寫"),
    "ccf-humanization": ("Natural academic prose", "自然学术表达", "自然學術表達"),
    "ccf-rebuttal-writer": ("Rebuttal", "回复审稿", "回覆審稿"),
    "ccf-visual-composer": ("Figures", "绘图", "繪圖"),
    "ccf-submission-checker": ("Submission", "投稿检查", "投稿檢查"),
    "ccf-paper-to-exemplar": ("Writing exemplars", "范文学习", "範文學習"),
    "ccf-skill-forger": ("Maintain skills", "家族维护", "家族維護"),
}


GROUPS = {
    "governance": ["ccf-common", "ccf-pipeline-orchestrator", "ccf-project-scaffolder"],
    "ideation": ["ccf-idea-reviewer", "ccf-idea-optimizer"],
    "evidence": ["ccf-literature-searcher", "ccf-literature-monitor", "ccf-experiment-designer", "ccf-integrity-auditor"],
    "writing": ["ccf-paper-reviewer", "ccf-paper-writer", "ccf-humanization", "ccf-rebuttal-writer"],
    "delivery": ["ccf-visual-composer", "ccf-submission-checker", "ccf-paper-to-exemplar"],
    "maintenance": ["ccf-skill-forger"],
}


# Daily cumulative GitHub stars from the public Stargazers API, UTC.
# Snapshot: 2026-08-13. The first point is the repository creation baseline.
STAR_HISTORY_TOTALS = [
    0, 107, 130, 142, 151, 176, 192, 210, 217, 223, 227, 291, 350, 389,
    404, 411, 425, 445, 459, 481, 510, 535, 558, 576, 595, 617, 628,
    640, 658, 676, 689, 701, 721, 739, 769, 790, 812, 827, 841, 858,
    879, 890, 904, 919, 926, 932, 940, 949, 957, 968, 981, 987, 994,
    1002, 1018, 1038, 1171, 1313, 1350, 1397, 1426, 1453, 1468, 1504,
    1542, 1557, 1586, 1610, 1635, 1661, 1662,
]


def tr(role: str, lang: str) -> str:
    value = ROLES[role]
    if lang == "en":
        return value[0]
    if lang == "zh-CN":
        return value[1]
    return value[2]


def attrs(**kwargs: object) -> str:
    return " ".join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k, v in kwargs.items() if v is not None)


def text(x: int, y: int, content: str, size: int = 16, weight: int = 500, fill: str | None = None, anchor: str = "start") -> str:
    return f'<text {attrs(x=x, y=y, font_size=size, font_weight=weight, fill=fill or PALETTE["ink"], text_anchor=anchor)}>{escape(content)}</text>'


def rect(x: int, y: int, w: int, h: int, fill: str, stroke: str | None = None, r: int = 18, extra: str = "") -> str:
    return f'<rect {attrs(x=x, y=y, width=w, height=h, rx=r, fill=fill, stroke=stroke or PALETTE["line"], stroke_width=1.4)} {extra}/>'


def line(x1: int, y1: int, x2: int, y2: int, color: str = "#AAB7D4", width: float = 2.0, arrow: bool = True) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line {attrs(x1=x1, y1=y1, x2=x2, y2=y2, stroke=color, stroke_width=width, stroke_linecap="round")}{marker}/>'


def path(d: str, color: str = "#AAB7D4", width: float = 2.0, arrow: bool = False, dash: str | None = None) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{marker}{dash_attr}/>'


def circle(cx: int, cy: int, r: int, fill: str, stroke: str | None = None, width: float = 1.4, extra: str = "") -> str:
    return f'<circle {attrs(cx=cx, cy=cy, r=r, fill=fill, stroke=stroke or PALETTE["line"], stroke_width=width)} {extra}/>'


def defs() -> str:
    return """
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#8EA0C5"/>
  </marker>
  <filter id="softShadow" x="-15%" y="-20%" width="130%" height="145%">
    <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#2F3A5F" flood-opacity="0.10"/>
  </filter>
  <linearGradient id="hero" x1="0" x2="1" y1="0" y2="1">
    <stop offset="0%" stop-color="#F8FAFF"/>
    <stop offset="100%" stop-color="#EEF3FF"/>
  </linearGradient>
</defs>
"""


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
{defs()}
<rect width="{width}" height="{height}" fill="url(#hero)"/>
<style>
text {{ font-family: Inter, "Noto Sans SC", "Microsoft YaHei", Arial, sans-serif; }}
.small {{ fill: {PALETTE["muted"]}; font-size: 13px; }}
.mono {{ font-family: "JetBrains Mono", Consolas, monospace; }}
</style>
{body}
</svg>
"""


def write_svg(name: str, lang: str, content: str) -> None:
    ASSETS.mkdir(exist_ok=True)
    path = ASSETS / f"{name}{LANG[lang]['suffix']}.svg"
    path.write_text(content, encoding="utf-8")


def build_hero(lang: str) -> None:
    copy = {
        "en": {
            "eyebrow": "A skill family for research papers",
            "title_lines": ["From research idea", "to submission"],
            "subtitle_lines": [
                "17 focused skills for literature, experiments, writing,",
                "review, figures, and submission.",
            ],
            "chips": ["Focused collaboration", "Evidence-grounded writing", "Editable scientific figures"],
            "nodes": ["Idea", "Evidence", "Manuscript", "Visuals", "Submission"],
            "hub_label": "Family",
            "footer": "Each task meets the skill that understands it best.",
            "footer_detail": "Shared context · Academic expression · Scientific figures",
        },
        "zh-CN": {
            "eyebrow": "为科研论文而生的 skill 家族",
            "title_lines": ["从研究想法到论文投稿"],
            "subtitle_lines": ["17 个彼此协作的 skills，覆盖文献、实验、写作、审稿、绘图与投稿检查。"],
            "chips": ["清晰分工", "证据支撑写作", "可编辑科研图"],
            "nodes": ["选题", "证据", "论文", "绘图", "投稿"],
            "hub_label": "家族",
            "footer": "让每项任务交给最理解它的 skill。",
            "footer_detail": "任务理解 · 学术表达 · 科研绘图",
        },
        "zh-TW": {
            "eyebrow": "為研究論文而生的 skill 家族",
            "title_lines": ["從研究想法到論文投稿"],
            "subtitle_lines": ["17 個彼此協作的 skills，涵蓋文獻、實驗、寫作、審稿、繪圖與投稿檢查。"],
            "chips": ["清晰分工", "證據支撐寫作", "可編輯科研圖"],
            "nodes": ["選題", "證據", "論文", "繪圖", "投稿"],
            "hub_label": "家族",
            "footer": "讓每項任務交給最理解它的 skill。",
            "footer_detail": "任務理解 · 學術表達 · 科研繪圖",
        },
    }[lang]
    body = [
        '<path d="M0 0 H1400 V620 H0 Z" fill="#F8FAFF"/>',
        '<path d="M730 0 C900 80 860 230 1040 280 C1190 320 1260 210 1400 250 V0 Z" fill="#EEF3FF"/>',
        '<path d="M810 620 C900 500 1040 540 1120 420 C1210 290 1290 370 1400 320 V620 Z" fill="#F2ECFF" opacity="0.75"/>',
        text(72, 92, copy["eyebrow"], 17, 800, PALETTE["purple2"]),
    ]
    if lang == "en":
        body.extend([
            text(72, 151, copy["title_lines"][0], 43, 900),
            text(72, 200, copy["title_lines"][1], 43, 900),
            text(72, 239, copy["subtitle_lines"][0], 17, 500, PALETTE["muted"]),
            text(72, 265, copy["subtitle_lines"][1], 17, 500, PALETTE["muted"]),
        ])
        chip_y = 294
        chip_widths = [174, 205, 205]
    else:
        body.extend([
            text(72, 168, copy["title_lines"][0], 46, 900),
            text(72, 213, copy["subtitle_lines"][0], 19, 500, PALETTE["muted"]),
        ])
        chip_y = 258
        chip_widths = [148, 168, 156]
    chip_x = 72
    chip_colors = [PALETTE["blue"], PALETTE["green"], PALETTE["orange"]]
    for label, color, w in zip(copy["chips"], chip_colors, chip_widths):
        body.append(rect(chip_x, chip_y, w, 42, color, r=21, stroke=color))
        body.append(text(chip_x + w // 2, chip_y + 27, label, 13, 750, anchor="middle"))
        chip_x += w + 14

    # A routed research constellation: the geometry carries the product message.
    hub_x, hub_y = 1035, 305
    body.extend([
        circle(hub_x, hub_y, 88, PALETTE["white"], PALETTE["purple2"], 3.0, 'filter="url(#softShadow)"'),
        circle(hub_x, hub_y, 58, "#F2ECFF", PALETTE["purple2"], 1.5),
        text(hub_x, hub_y - 3, "CCFA", 25, 900, anchor="middle"),
        text(hub_x, hub_y + 25, copy["hub_label"], 15, 750, PALETTE["muted"], "middle"),
    ])
    nodes = [(855, 135), (1160, 120), (1270, 310), (1165, 505), (850, 485)]
    fills = [PALETTE["purple"], PALETTE["green"], PALETTE["red"], PALETTE["orange"], PALETTE["blue"]]
    accents = [PALETTE["purple2"], PALETTE["green2"], PALETTE["red2"], PALETTE["orange2"], PALETTE["blue2"]]
    for (nx, ny), label, fill, accent in zip(nodes, copy["nodes"], fills, accents):
        dx = nx - hub_x
        dy = ny - hub_y
        body.append(path(f"M {hub_x + dx * 0.63:.0f} {hub_y + dy * 0.63:.0f} Q {(hub_x + nx) / 2 + dy * 0.10:.0f} {(hub_y + ny) / 2 - dx * 0.10:.0f} {nx} {ny}", accent, 3.2, False))
        body.append(circle(nx, ny, 57, fill, accent, 2.0, 'filter="url(#softShadow)"'))
        body.append(circle(nx, ny - 11, 12, accent, accent, 1.0))
        body.append(text(nx, ny + 27, label, 15, 800, anchor="middle"))
    body.extend([
        path("M 855 135 Q 1000 45 1160 120", PALETTE["line"], 1.8, False, "5 8"),
        path("M 1160 120 Q 1340 170 1270 310", PALETTE["line"], 1.8, False, "5 8"),
        path("M 1270 310 Q 1320 450 1165 505", PALETTE["line"], 1.8, False, "5 8"),
        path("M 1165 505 Q 980 590 850 485", PALETTE["line"], 1.8, False, "5 8"),
        rect(72, 410, 590, 92, PALETTE["white"], r=24, extra='filter="url(#softShadow)"'),
        circle(112, 456, 17, PALETTE["green"], PALETTE["green2"], 1.6),
        text(112, 462, "✓", 18, 900, PALETTE["green2"], "middle"),
        text(145, 451, copy["footer"], 15, 700),
        text(145, 476, copy["footer_detail"], 13, 600, PALETTE["muted"]),
    ])
    write_svg("ccfa-skills-hero", lang, svg(1400, 620, "\n".join(body)))


def build_architecture(lang: str) -> None:
    l = LANG[lang]
    subtitle = {
        "en": "Clear responsibilities and coherent transitions from idea to submission",
        "zh-CN": "从研究方向到投稿检查，分工清晰，衔接连贯",
        "zh-TW": "從研究方向到投稿檢查，分工清晰，銜接連貫",
    }[lang]
    labels = {
        "en": [
            ("Research direction", "idea review · idea optimization"),
            ("Evidence construction", "literature · experiments · integrity"),
            ("Publication narrative", "review · writing · humanization · rebuttal"),
            ("Scientific delivery", "figures · exemplars · submission"),
        ],
        "zh-CN": [
            ("研究方向", "选题评审 · 选题优化"),
            ("证据构建", "文献 · 实验 · 完整性核验"),
            ("论文叙事", "评审 · 写作 · 学术表达 · 审稿回复"),
            ("科研交付", "绘图 · 范文 · 投稿检查"),
        ],
        "zh-TW": [
            ("研究方向", "選題評審 · 選題優化"),
            ("證據構建", "文獻 · 實驗 · 完整性核驗"),
            ("論文敘事", "評審 · 寫作 · 學術表達 · 審稿回覆"),
            ("研究交付", "繪圖 · 範文 · 投稿檢查"),
        ],
    }[lang]
    route_title = {"en": "Understand the task", "zh-CN": "理解任务", "zh-TW": "理解任務"}[lang]
    owner_rule = {"en": "one task · one owner", "zh-CN": "每项任务 · 明确负责", "zh-TW": "每項任務 · 明確負責"}[lang]
    sidecar = {"en": "Supporting checks", "zh-CN": "辅助检查", "zh-TW": "輔助檢查"}[lang]
    artifact = {"en": "Traceable result", "zh-CN": "可追溯成果", "zh-TW": "可追溯成果"}[lang]
    owner_label = {"en": ("Owner", "skill"), "zh-CN": ("主责", "模块"), "zh-TW": ("主責", "模組")}[lang]
    footer = {
        "en": "Project planning · Project setup · Skill family maintenance",
        "zh-CN": "项目规划 · 项目起步 · 家族维护",
        "zh-TW": "專案規劃 · 專案起步 · 家族維護",
    }[lang]
    body = [
        text(60, 62, l["title"], 32, 800),
        text(60, 92, subtitle, 16, 500, PALETTE["muted"]),
        rect(56, 130, 1288, 535, PALETTE["white"], r=30, extra='filter="url(#softShadow)"'),
        rect(90, 275, 185, 170, PALETTE["blue"], r=35),
        circle(182, 330, 31, PALETTE["white"], PALETTE["blue2"], 2.0),
        text(182, 337, "↗", 26, 900, PALETTE["blue2"], "middle"),
        text(182, 388, route_title, 19, 850, anchor="middle"),
        text(182, 418, "ccf-common", 14, 700, PALETTE["muted"], "middle"),
        path("M 275 360 C 330 360 340 205 400 205", PALETTE["blue2"], 3.0, True),
        path("M 275 360 C 330 360 340 325 400 325", PALETTE["green2"], 3.0, True),
        path("M 275 360 C 330 360 340 445 400 445", PALETTE["red2"], 3.0, True),
        path("M 275 360 C 330 360 340 565 400 565", PALETTE["orange2"], 3.0, True),
    ]
    ys = [205, 325, 445, 565]
    fills = [PALETTE["purple"], PALETTE["green"], PALETTE["red"], PALETTE["orange"]]
    accents = [PALETTE["purple2"], PALETTE["green2"], PALETTE["red2"], PALETTE["orange2"]]
    symbols = ["◇", "▦", "¶", "✦"]
    for (title_, detail), y, fill, accent, symbol in zip(labels, ys, fills, accents, symbols):
        body.append(rect(400, y - 47, 470, 94, fill, stroke=accent, r=28))
        body.append(circle(442, y, 23, PALETTE["white"], accent, 1.6))
        body.append(text(442, y + 7, symbol, 19, 850, accent, "middle"))
        body.append(text(480, y - 5, title_, 18, 850))
        body.append(text(480, y + 23, detail, 13, 650, PALETTE["muted"]))
        body.append(path(f"M 870 {y} C 920 {y} 920 360 960 360", accent, 2.8, True))

    body.extend([
        rect(970, 250, 165, 220, "#F4F0FF", stroke=PALETTE["purple2"], r=34),
        text(1052, 292, owner_rule, 15, 850, anchor="middle"),
        circle(1052, 355, 46, PALETTE["white"], PALETTE["purple2"], 2.2),
        text(1052, 349, owner_label[0], 16, 900, PALETTE["purple2"], "middle"),
        text(1052, 371, owner_label[1], 13, 750, PALETTE["muted"], "middle"),
        rect(991, 420, 122, 32, PALETTE["white"], stroke=PALETTE["line"], r=16),
        text(1052, 441, sidecar, 12, 750, anchor="middle"),
        path("M 1135 360 C 1170 360 1170 360 1200 360", PALETTE["purple2"], 3.0, True),
        rect(1204, 295, 105, 130, PALETTE["blue"], stroke=PALETTE["blue2"], r=26),
        text(1256, 340, "✓", 28, 900, PALETTE["green2"], "middle"),
        text(1256, 379, artifact, 13, 850, anchor="middle"),
        text(1256, 402, "ccfa.yaml", 11, 650, PALETTE["muted"], "middle"),
        text(635, 633, footer, 13, 650, PALETTE["muted"], "middle"),
    ])
    write_svg("ccfa-skills-architecture", lang, svg(1400, 720, "\n".join(body)))


def build_workflow(lang: str) -> None:
    title = {"en": "A research workflow that stays coherent", "zh-CN": "彼此衔接的科研工作流", "zh-TW": "彼此銜接的研究工作流程"}[lang]
    steps = {
        "en": [("Plan", ""), ("Review", "ideas"), ("Search", "literature"), ("Design", "experiments"), ("Write", ""), ("Refine", "prose"), ("Audit", ""), ("Create", "figures"), ("Check", "submission")],
        "zh-CN": [("规划", ""), ("评审", "选题"), ("检索", "文献"), ("设计", "实验"), ("撰写", "论文"), ("改善", "表达"), ("核验", "证据"), ("绘制", "图表"), ("检查", "投稿")],
        "zh-TW": [("規劃", ""), ("評審", "選題"), ("檢索", "文獻"), ("設計", "實驗"), ("撰寫", "論文"), ("改善", "表達"), ("核驗", "證據"), ("繪製", "圖表"), ("檢查", "投稿")],
    }[lang]
    owners = {
        "en": ["Project planning", "Idea review", "Literature search", "Experiment design", "Paper writing", "Humanization", "Integrity audit", "Visual composer", "Submission check"],
        "zh-CN": ["项目规划", "选题评审", "文献检索", "实验设计", "论文写作", "学术表达", "完整性核验", "科研绘图", "投稿检查"],
        "zh-TW": ["專案規劃", "選題評審", "文獻檢索", "實驗設計", "論文寫作", "學術表達", "完整性核驗", "科研繪圖", "投稿檢查"],
    }[lang]
    colors = [PALETTE["blue"], PALETTE["purple"], PALETTE["green"], PALETTE["green"], PALETTE["red"], PALETTE["red"], PALETTE["orange"], PALETTE["orange"], "#EEF2FF"]
    body = [text(60, 62, title, 30, 800), text(60, 92, LANG[lang]["subtitle"], 15, 500, PALETTE["muted"])]
    x = 55
    card_w = 146
    gap = 24
    for i, ((step_1, step_2), owner, color) in enumerate(zip(steps, owners, colors), 1):
        body.append(rect(x, 155, card_w, 150, color, r=22, extra='filter="url(#softShadow)"'))
        body.append(text(x + card_w / 2, 188, f"{i}", 20, 900, PALETTE["ink"], "middle"))
        body.append(text(x + card_w / 2, 224 if step_2 else 237, step_1, 15, 850, PALETTE["ink"], "middle"))
        if step_2:
            body.append(text(x + card_w / 2, 245, step_2, 15, 850, PALETTE["ink"], "middle"))
        body.append(text(x + card_w / 2, 280, owner, 11, 650, PALETTE["muted"], "middle"))
        if i < len(steps):
            body.append(line(x + card_w + 4, 230, x + card_w + gap - 5, 230))
        x += card_w + gap
    note = {
        "en": "Humanization refines publication prose while Paper Writer keeps the argument coherent.",
        "zh-CN": "学术表达模块改善文字，论文写作模块保持论证连贯。",
        "zh-TW": "學術表達模組改善文字，論文寫作模組保持論證連貫。",
    }[lang]
    body.append(rect(340, 365, 920, 82, PALETTE["white"], r=22, extra='filter="url(#softShadow)"'))
    body.append(text(800, 408, note, 17, 700, PALETTE["ink"], "middle"))
    write_svg("ccfa-skills-workflow", lang, svg(1600, 530, "\n".join(body)))


def build_catalog(lang: str) -> None:
    title = {"en": "Skill catalog by responsibility", "zh-CN": "按职责划分的技能目录", "zh-TW": "按職責劃分的技能目錄"}[lang]
    subtitle = {
        "en": "17 skills with distinct responsibilities and purposeful collaboration",
        "zh-CN": "17 个 skills 各有专长，并在需要时彼此协作",
        "zh-TW": "17 個 skills 各有專長，並在需要時彼此協作",
    }[lang]
    body = [text(60, 58, title, 30, 800), text(60, 88, subtitle, 15, 500, PALETTE["muted"])]
    layout = [("governance", 60, 125, PALETTE["blue"]), ("ideation", 430, 125, PALETTE["purple"]), ("evidence", 800, 125, PALETTE["green"]), ("writing", 60, 380, PALETTE["red"]), ("delivery", 430, 380, PALETTE["orange"]), ("maintenance", 800, 380, "#EEF2FF")]
    for group, x, y, color in layout:
        body.append(rect(x, y, 320, 205, color, r=24, extra='filter="url(#softShadow)"'))
        body.append(text(x + 20, y + 36, LANG[lang]["groups"][group], 20, 850))
        yy = y + 70
        for skill in GROUPS[group]:
            body.append(text(x + 22, yy, f"{skill}", 13, 700, PALETTE["ink"]))
            body.append(text(x + 220, yy, tr(skill, lang), 12, 600, PALETTE["muted"]))
            yy += 29
    write_svg("ccfa-skills-catalog", lang, svg(1200, 660, "\n".join(body)))


def build_routing(lang: str) -> None:
    title = {"en": "Clear boundaries between skills", "zh-CN": "清晰的 skill 职责边界", "zh-TW": "清晰的 skill 職責邊界"}[lang]
    rows = {
        "en": [
            ("Idea scoring", "ccf-idea-reviewer", "scores and ranks; does not rewrite"),
            ("Idea shaping", "ccf-idea-optimizer", "turns fuzzy ideas into method plans"),
            ("Literature retrieval", "ccf-literature-searcher", "searches prior art and benchmarks"),
            ("Experiment semantics", "ccf-experiment-designer", "chooses evidence structure, not rendering"),
            ("Manuscript editing", "ccf-paper-writer", "changes prose; humanization preflight applies"),
            ("Rendered visuals", "ccf-visual-composer", "uses GPT Image 2 first unless pure SVG is requested"),
        ],
        "zh-CN": [
            ("选题评分", "ccf-idea-reviewer", "负责评分排序，不改写论文"),
            ("发展选题", "ccf-idea-optimizer", "把模糊想法发展成研究方案"),
            ("文献检索", "ccf-literature-searcher", "检索相关工作与 benchmark"),
            ("实验设计", "ccf-experiment-designer", "设计证据结构，不负责图形美化"),
            ("论文改写", "ccf-paper-writer", "修改正文，并按需改善学术表达"),
            ("科研绘图", "ccf-visual-composer", "默认先用 GPT Image 2，除非指定纯 SVG"),
        ],
        "zh-TW": [
            ("選題評分", "ccf-idea-reviewer", "負責評分排序，不改寫論文"),
            ("發展選題", "ccf-idea-optimizer", "把模糊想法發展成研究方案"),
            ("文獻檢索", "ccf-literature-searcher", "檢索相關工作與 benchmark"),
            ("實驗設計", "ccf-experiment-designer", "設計證據結構，不負責圖形美化"),
            ("論文改寫", "ccf-paper-writer", "修改正文，並按需改善學術表達"),
            ("科研繪圖", "ccf-visual-composer", "預設先用 GPT Image 2，除非指定純 SVG"),
        ],
    }[lang]
    body = [text(60, 58, title, 30, 800)]
    y = 115
    for task, owner, rule in rows:
        body.append(rect(70, y, 1060, 62, PALETTE["white"], r=18, extra='filter="url(#softShadow)"'))
        body.append(text(100, y + 38, task, 16, 800))
        body.append(text(420, y + 38, owner, 15, 800, PALETTE["purple2"]))
        body.append(text(720, y + 38, rule, 14, 600, PALETTE["muted"]))
        y += 78
    write_svg("ccfa-skills-routing", lang, svg(1200, 630, "\n".join(body)))


def build_artifacts(lang: str) -> None:
    title = {"en": "From research content to editable figures", "zh-CN": "从研究内容到可编辑图形", "zh-TW": "從研究內容到可編輯圖形"}[lang]
    labels = {
        "en": ["Research content", "Visual composition", "Figure checks", "Editable delivery"],
        "zh-CN": ["研究内容", "视觉构图", "成图检查", "可编辑交付"],
        "zh-TW": ["研究內容", "視覺構圖", "成圖檢查", "可編輯交付"],
    }[lang]
    details = {
        "en": ["paper, prompt, data", "layout, icons, hierarchy", "meaning, text, alignment", "SVG, PDF, PPTX"],
        "zh-CN": ["论文、指令、数据", "版式、图标、层次", "含义、文字、对齐", "SVG、PDF、PPTX"],
        "zh-TW": ["論文、指令、資料", "版式、圖示、層次", "含義、文字、對齊", "SVG、PDF、PPTX"],
    }[lang]
    body = [text(60, 58, title, 30, 800)]
    x_positions = [80, 345, 610, 875]
    colors = [PALETTE["blue"], PALETTE["purple"], PALETTE["green"], PALETTE["orange"]]
    for i, (x, label, detail, color) in enumerate(zip(x_positions, labels, details, colors)):
        body.append(rect(x, 170, 210, 130, color, r=24, extra='filter="url(#softShadow)"'))
        body.append(text(x + 105, 215, label, 20, 850, anchor="middle"))
        body.append(text(x + 105, 252, detail, 13, 600, PALETTE["muted"], "middle"))
        if i < 3:
            body.append(line(x + 215, 235, x + 260, 235))
    note = {
        "en": "The final figure remains clear, traceable, and genuinely editable.",
        "zh-CN": "最终图形保持清晰、可追溯，并且能够真正编辑。",
        "zh-TW": "最終圖形保持清晰、可追溯，並且能夠真正編輯。",
    }[lang]
    body.append(rect(250, 390, 700, 70, PALETTE["white"], r=24, extra='filter="url(#softShadow)"'))
    body.append(text(600, 433, note, 17, 700, PALETTE["ink"], "middle"))
    write_svg("ccfa-skills-artifacts", lang, svg(1200, 560, "\n".join(body)))


def build_review(lang: str) -> None:
    title = {"en": "Review and revision scoring", "zh-CN": "评审与修订评分", "zh-TW": "評審與修訂評分"}[lang]
    labels = {
        "en": ["Current readiness", "Version improvement", "Issue history", "Reviewer confidence"],
        "zh-CN": ["当前稿件", "版本进步", "问题记录", "评审置信度"],
        "zh-TW": ["當前稿件", "版本進步", "問題記錄", "評審信心"],
    }[lang]
    details = {
        "en": ["meets venue standard", "better than previous draft", "resolved, partial, new", "stable evidence threshold"],
        "zh-CN": ["距离录用标准多远", "是否优于上一版", "已解决、部分解决、新问题", "判断依据是否充分"],
        "zh-TW": ["距離錄用標準多遠", "是否優於上一版", "已解決、部分解決、新問題", "判斷依據是否充分"],
    }[lang]
    body = [text(60, 58, title, 30, 800)]
    for i, (label, detail) in enumerate(zip(labels, details)):
        x = 90 + i * 270
        body.append(rect(x, 150, 220, 150, [PALETTE["blue"], PALETTE["purple"], PALETTE["green"], PALETTE["orange"]][i], r=24, extra='filter="url(#softShadow)"'))
        body.append(text(x + 110, 205, label, 17, 850, anchor="middle"))
        body.append(text(x + 110, 245, detail, 13, 600, PALETTE["muted"], "middle"))
    write_svg("ccfa-skills-review-boundaries", lang, svg(1200, 430, "\n".join(body)))


def build_installation(lang: str) -> None:
    title = {"en": "Installation shape", "zh-CN": "安装形态", "zh-TW": "安裝形態"}[lang]
    labels = {
        "en": ["Repository", "Installed skills", "Local project"],
        "zh-CN": ["仓库", "已安装 skills", "本地项目"],
        "zh-TW": ["倉庫", "已安裝 skills", "本地專案"],
    }[lang]
    paths = ["CCFA-Skills/", "~/.codex/skills/", "paper workspace"]
    body = [text(60, 58, title, 30, 800)]
    x_positions = [120, 490, 860]
    for x, label, path, color in zip(x_positions, labels, paths, [PALETTE["blue"], PALETTE["purple"], PALETTE["green"]]):
        body.append(rect(x, 150, 240, 145, color, r=24, extra='filter="url(#softShadow)"'))
        body.append(text(x + 120, 205, label, 20, 850, anchor="middle"))
        body.append(text(x + 120, 245, path, 14, 650, PALETTE["muted"], "middle"))
    body.append(line(365, 222, 485, 222))
    body.append(line(735, 222, 855, 222))
    write_svg("ccfa-skills-installation", lang, svg(1200, 430, "\n".join(body)))


def build_star_history(lang: str) -> None:
    copy = {
        "en": {
            "title": "Our open-source journey, one star at a time",
            "subtitle": "Cumulative GitHub stars since the repository opened",
            "milestone": "The first 1,000",
            "peak": "+142 in one day",
            "final": "1,662 stars!",
            "bubble": "Thank you for helping the family grow!",
            "cta": "If CCFA Skills helps your research, leave a star for the next chapter.",
            "source": "Source: GitHub Stargazers API · UTC · updated 2026-08-13",
            "axis": "Cumulative stars",
        },
        "zh-CN": {
            "title": "开源旅程，由每一颗星共同写成",
            "subtitle": "仓库公开以来的 GitHub 累计星标",
            "milestone": "跨过 1,000 颗星",
            "peak": "单日新增 142",
            "final": "1,662 颗星！",
            "bubble": "谢谢你陪这个家族一起成长！",
            "cta": "如果 CCFA Skills 帮到了你的研究，欢迎为下一章点亮一颗 Star。",
            "source": "数据来源：GitHub Stargazers API · UTC · 更新于 2026-08-13",
            "axis": "累计星标",
        },
        "zh-TW": {
            "title": "開源旅程，由每一顆星共同寫成",
            "subtitle": "儲存庫公開以來的 GitHub 累計星標",
            "milestone": "跨過 1,000 顆星",
            "peak": "單日新增 142",
            "final": "1,662 顆星！",
            "bubble": "謝謝你陪這個家族一起成長！",
            "cta": "如果 CCFA Skills 幫助了你的研究，歡迎為下一章點亮一顆 Star。",
            "source": "資料來源：GitHub Stargazers API · UTC · 更新於 2026-08-13",
            "axis": "累計星標",
        },
    }[lang]

    plot_left, plot_right = 120, 1280
    plot_top, plot_bottom = 145, 470
    max_value = 1700
    count = len(STAR_HISTORY_TOTALS)

    def point(index: int, value: int) -> tuple[float, float]:
        x = plot_left + index * (plot_right - plot_left) / (count - 1)
        y = plot_bottom - value * (plot_bottom - plot_top) / max_value
        return x, y

    points = [point(i, value) for i, value in enumerate(STAR_HISTORY_TOTALS)]
    curve = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in points)
    area = curve + f" L {plot_right} {plot_bottom} L {plot_left} {plot_bottom} Z"

    def star_points(cx: float, cy: float, outer: float, inner: float) -> str:
        coords = []
        for i in range(10):
            angle = -math.pi / 2 + i * math.pi / 5
            radius = outer if i % 2 == 0 else inner
            coords.append(f"{cx + radius * math.cos(angle):.1f},{cy + radius * math.sin(angle):.1f}")
        return " ".join(coords)

    body = [
        f'<desc>{escape(copy["source"])}</desc>',
        text(70, 62, copy["title"], 32, 900),
        text(70, 92, copy["subtitle"], 16, 550, PALETTE["muted"]),
        text(72, 126, copy["axis"], 13, 750, PALETTE["purple2"]),
    ]

    for tick in [0, 500, 1000, 1500]:
        _, y = point(0, tick)
        body.append(line(plot_left, int(y), plot_right, int(y), PALETTE["line"], 1.2, False))
        body.append(text(plot_left - 18, int(y) + 5, f"{tick:,}", 12, 650, PALETTE["muted"], "end"))

    body.extend([
        f'<path d="{area}" fill="#E9DFFF" opacity="0.48" stroke="none"/>',
        path(curve, "#233044", 6.5, False),
        path(curve, PALETTE["purple2"], 3.8, False),
    ])

    for index, label in [(0, "Jun 4"), (27, "Jul 1"), (58, "Aug 1"), (70, "Aug 13")]:
        x, _ = point(index, STAR_HISTORY_TOTALS[index])
        body.append(line(int(x), plot_bottom, int(x), plot_bottom + 8, PALETTE["muted"], 1.3, False))
        body.append(text(int(x), plot_bottom + 29, label, 12, 650, PALETTE["muted"], "middle"))

    milestone_index = next(i for i, value in enumerate(STAR_HISTORY_TOTALS) if value >= 1000)
    mx, my = points[milestone_index]
    px, py = points[57]
    fx, fy = points[-1]
    body.extend([
        circle(int(mx), int(my), 7, PALETTE["white"], PALETTE["purple2"], 3.0),
        line(int(mx), int(my) - 10, int(mx) - 55, int(my) - 58, PALETTE["purple2"], 1.8, False),
        rect(int(mx) - 190, int(my) - 105, 165, 42, PALETTE["white"], PALETTE["purple2"], 16, 'filter="url(#softShadow)"'),
        text(int(mx) - 107, int(my) - 78, copy["milestone"], 13, 800, anchor="middle"),
        circle(int(px), int(py), 7, PALETTE["white"], PALETTE["orange2"], 3.0),
        rect(int(px) - 92, int(py) - 82, 184, 40, PALETTE["orange"], PALETTE["orange2"], 16),
        text(int(px), int(py) - 56, copy["peak"], 13, 800, anchor="middle"),
    ])

    # A small hand-drawn star mascot marks the current endpoint.
    mascot_x, mascot_y = fx - 8, fy - 8
    body.extend([
        f'<polygon points="{star_points(mascot_x, mascot_y, 31, 14)}" fill="#F7D154" stroke="#233044" stroke-width="3.2" stroke-linejoin="round"/>',
        circle(int(mascot_x - 8), int(mascot_y - 2), 2, PALETTE["ink"], PALETTE["ink"], 1.0),
        circle(int(mascot_x + 8), int(mascot_y - 2), 2, PALETTE["ink"], PALETTE["ink"], 1.0),
        path(f"M {mascot_x - 8:.1f} {mascot_y + 8:.1f} Q {mascot_x:.1f} {mascot_y + 15:.1f} {mascot_x + 9:.1f} {mascot_y + 7:.1f}", PALETTE["ink"], 2.0, False),
        path(f"M {mascot_x - 26:.1f} {mascot_y + 5:.1f} Q {mascot_x - 44:.1f} {mascot_y + 14:.1f} {mascot_x - 50:.1f} {mascot_y + 2:.1f}", PALETTE["ink"], 2.0, False),
        path(f"M {mascot_x + 25:.1f} {mascot_y + 5:.1f} Q {mascot_x + 43:.1f} {mascot_y + 13:.1f} {mascot_x + 48:.1f} {mascot_y - 1:.1f}", PALETTE["ink"], 2.0, False),
        rect(960, 60, 330, 62, PALETTE["white"], PALETTE["ink"], 22, 'filter="url(#softShadow)"'),
        text(1125, 88, copy["final"], 18, 900, anchor="middle"),
        text(1125, 110, copy["bubble"], 12, 650, PALETTE["muted"], "middle"),
        path(f"M 1230 122 Q 1250 135 {mascot_x - 15:.1f} {mascot_y - 24:.1f}", PALETTE["ink"], 2.0, False),
        rect(220, 525, 960, 52, "#FFF7DA", "#F0C84D", 24),
        text(700, 557, copy["cta"], 15, 800, PALETTE["ink"], "middle"),
        text(70, 613, copy["source"], 12, 550, PALETTE["muted"]),
    ])
    write_svg("ccfa-skills-star-history", lang, svg(1400, 640, "\n".join(body)))


def build_demo(lang: str) -> None:
    title = {"en": "Demo: attention study routing", "zh-CN": "Demo：注意力研究路由", "zh-TW": "Demo：注意力研究路由"}[lang]
    stages = {
        "en": ["Idea", "Reviewer", "Searcher", "Experiment", "Writer", "Submission"],
        "zh-CN": ["想法", "评审", "检索", "实验", "写作", "投稿"],
        "zh-TW": ["想法", "評審", "檢索", "實驗", "寫作", "投稿"],
    }[lang]
    body = [text(60, 58, title, 30, 800)]
    x = 95
    for i, stage in enumerate(stages):
        body.append(rect(x, 155, 140, 105, [PALETTE["blue"], PALETTE["purple"], PALETTE["green"], PALETTE["green"], PALETTE["red"], PALETTE["orange"]][i], r=22, extra='filter="url(#softShadow)"'))
        body.append(text(x + 70, 210, stage, 18, 850, anchor="middle"))
        if i < len(stages) - 1:
            body.append(line(x + 145, 208, x + 205, 208))
        x += 180
    note = {
        "en": "The demo is illustrative and preserved as-is in README.",
        "zh-CN": "README 保留原 demo，仅重生成架构说明图。",
        "zh-TW": "README 保留原 demo，僅重生成架構說明圖。",
    }[lang]
    body.append(text(600, 345, note, 17, 700, PALETTE["muted"], "middle"))
    write_svg("ccfa-skills-demo-attention", lang, svg(1200, 440, "\n".join(body)))


BUILDERS = [
    build_hero,
    build_architecture,
    build_workflow,
    build_catalog,
    build_routing,
    build_artifacts,
    build_review,
    build_installation,
    build_star_history,
    build_demo,
]


def main() -> None:
    for lang in LANG:
        for builder in BUILDERS:
            builder(lang)
    print(f"Generated {len(LANG) * len(BUILDERS)} SVG files in {ASSETS}")


if __name__ == "__main__":
    main()
