#!/usr/bin/env python3
"""Build README visual showcase figures with deterministic random data."""

from __future__ import annotations

import random
import sys
from math import cos, log10, pi, sin, tau
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ccf-visual-composer" / "resources" / "python"))

from ccfa_plot_recipes import (  # noqa: E402
    Canvas,
    PALETTES,
    Theme,
    correlation_heatmap,
    donut_chart,
    grouped_bar_chart,
    heatmap_matrix,
    lollipop_rank,
    radial_scorecard,
    ridgeline_density,
    save_svg,
    slopegraph,
    small_multiple_lines,
    volcano_plot,
)


OUT = ROOT / "assets" / "visual-showcase"
RNG = random.Random(20260708)


PALETTE_GEM = ["#174A7C", "#D95F02", "#1B9E77", "#7570B3", "#E7298A", "#66A61E", "#E6AB02"]
PALETTE_NOCTURNE = ["#0E2A47", "#28587B", "#9FB798", "#F2C14E", "#F78154", "#B4436C"]
PALETTE_CERAMIC = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51", "#8AB17D"]
PALETTE_ORCHID = ["#3B1F5E", "#6A4C93", "#B565A7", "#E56B6F", "#EAAC8B", "#355070"]
PALETTE_ARCTIC = ["#063B63", "#0B7285", "#38A3A5", "#80ED99", "#F4D35E", "#EE964B"]
PALETTE_WINE = ["#5F0F40", "#9A031E", "#FB8B24", "#E36414", "#0F4C5C", "#6A994E"]
PALETTE_INK = ["#111827", "#374151", "#1D4ED8", "#059669", "#D97706", "#BE123C"]


def _round(value: float, digits: int = 1) -> float:
    return round(value, digits)


def _spark_path(values: list[float], x: float, y: float, width: float, height: float) -> list[tuple[float, float]]:
    lo, hi = min(values), max(values)
    if lo == hi:
        hi = lo + 1
    points = []
    for idx, value in enumerate(values):
        px = x + width * idx / max(1, len(values) - 1)
        py = y + height - (value - lo) / (hi - lo) * height
        points.append((px, py))
    return points


def _lin(value: float, lo: float, hi: float, out_lo: float, out_hi: float) -> float:
    if hi == lo:
        return (out_lo + out_hi) / 2
    return out_lo + (value - lo) / (hi - lo) * (out_hi - out_lo)


def _panel(c: Canvas, x: float, y: float, w: float, h: float, label: str, title: str, subtitle: str) -> None:
    c.rect(x, y, w, h, "#FFFFFF", "#D8E1EA", 22)
    c.rect(x + 18, y + 18, 34, 28, "#102033", "none", 10)
    c.text(x + 35, y + 38, label, 13, 850, "#FFFFFF", "middle")
    c.text(x + 64, y + 37, title, 18, 850, "#102033")
    c.text(x + 64, y + 60, subtitle, 12, 560, "#5D6977")


def _correlation_matrix(labels: list[str]) -> list[list[float]]:
    matrix: list[list[float]] = []
    for i, _ in enumerate(labels):
        row = []
        for j, _ in enumerate(labels):
            if i == j:
                row.append(1.0)
            else:
                distance = abs(i - j)
                base = 0.78 - distance * 0.22
                row.append(round(max(-0.82, min(0.92, base + RNG.uniform(-0.38, 0.32))), 2))
        matrix.append(row)
    return matrix


def composite_analysis_dashboard() -> str:
    theme = Theme(width=1600, height=1120, bg="#EEF3F8", accent="#1F6F8B")
    c = Canvas(theme.width, theme.height, theme)
    c.text(56, 62, "Composite analytical figure from synthetic experiment data", 34, 900, "#102033")
    c.text(
        56,
        94,
        "One figure combines composition, categorical comparison, discovery screening, and correlation analysis.",
        15,
        560,
        "#52616F",
    )
    c.text(theme.width - 56, 94, "Fixed random seed: 20260708", 12, 650, "#52616F", "end")

    _panel(c, 52, 132, 700, 410, "A", "Dataset composition", "Donut panel with direct labels and restrained legend.")
    cx, cy, outer, inner = 296, 350, 132, 76
    values = [34, 27, 19, 12, 8]
    labels = ["vision", "language", "tabular", "audio", "graph"]
    total = sum(values)
    angle = -pi / 2
    for i, value in enumerate(values):
        delta = tau * value / total
        end = angle + delta
        large = 1 if delta > pi else 0
        x1, y1 = cx + cos(angle) * outer, cy + sin(angle) * outer
        x2, y2 = cx + cos(end) * outer, cy + sin(end) * outer
        x3, y3 = cx + cos(end) * inner, cy + sin(end) * inner
        x4, y4 = cx + cos(angle) * inner, cy + sin(angle) * inner
        d = (
            f"M{x1:.2f},{y1:.2f} A{outer:.2f},{outer:.2f} 0 {large} 1 {x2:.2f},{y2:.2f} "
            f"L{x3:.2f},{y3:.2f} A{inner:.2f},{inner:.2f} 0 {large} 0 {x4:.2f},{y4:.2f} Z"
        )
        color = PALETTE_CERAMIC[i % len(PALETTE_CERAMIC)]
        c.path(d, color, "#FFFFFF", 2.4, 0.96)
        angle = end
    c.circle(cx, cy, inner * 0.92, "#FFFFFF", "none")
    c.text(cx, cy - 8, f"{total}", 36, 900, "#102033", "middle")
    c.text(cx, cy + 22, "samples", 13, 700, "#64748B", "middle")
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 248 + i * 42
        c.rect(508, y - 13, 22, 22, PALETTE_CERAMIC[i % len(PALETTE_CERAMIC)], "none", 6)
        c.text(542, y + 4, label, 14, 760, "#102033")
        c.text(690, y + 4, f"{value}%", 14, 850, "#102033", "end")

    _panel(c, 800, 132, 748, 410, "B", "Ablation bar comparison", "Grouped bars separate model variants and benchmark families.")
    groups = ["Base", "Aug.", "Cal.", "Full"]
    series = {"Vision": [63, 68, 71, 83], "NLP": [59, 66, 70, 81], "Tabular": [54, 62, 68, 76]}
    left, right, top, bottom = 872, 1506, 230, 474
    for frac in (0, 0.25, 0.5, 0.75, 1):
        y = _lin(frac * 100, 0, 100, bottom, top)
        c.line(left, y, right, y, "#E2E8F0", 1)
        c.text(left - 14, y + 4, f"{int(frac * 100)}", 11, 600, "#64748B", "end")
    group_w = (right - left) / len(groups)
    bar_w = 30
    for i, group in enumerate(groups):
        gx = left + i * group_w + group_w / 2
        c.text(gx, bottom + 28, group, 13, 750, "#102033", "middle")
        for j, (name, vals) in enumerate(series.items()):
            value = vals[i]
            h = bottom - _lin(value, 0, 100, bottom, top)
            x = gx - 50 + j * 34
            color = PALETTE_ARCTIC[j + 1]
            c.rect(x, bottom - h, bar_w, h, color, "none", 8, 0.94)
            if i == len(groups) - 1:
                c.text(x + bar_w / 2, bottom - h - 8, str(value), 11, 850, "#102033", "middle")
    for j, name in enumerate(series):
        x = left + j * 128
        c.rect(x, 500, 20, 12, PALETTE_ARCTIC[j + 1], "none", 4)
        c.text(x + 28, 511, name, 12, 700, "#64748B")

    _panel(c, 52, 592, 700, 458, "C", "Volcano screening", "Effect size and significance reveal candidate features.")
    points = []
    for i in range(145):
        fold = RNG.gauss(0, 1.25)
        p_value = 10 ** (-RNG.uniform(0.1, 4.6)) if abs(fold) > 1.1 else 10 ** (-RNG.uniform(0.05, 2.1))
        points.append((fold, -log10(p_value), f"F{i + 1}"))
    left, right, top, bottom = 122, 706, 700, 994
    c.rect(left, top, right - left, bottom - top, "#FAFBFD", "#E2E8F0", 16)
    c.line(_lin(-1, -3.2, 3.2, left, right), top + 10, _lin(-1, -3.2, 3.2, left, right), bottom - 12, "#CBD5E1", 1.1)
    c.line(_lin(1, -3.2, 3.2, left, right), top + 10, _lin(1, -3.2, 3.2, left, right), bottom - 12, "#CBD5E1", 1.1)
    c.line(left + 12, _lin(1.3, 0, 5, bottom, top), right - 12, _lin(1.3, 0, 5, bottom, top), "#CBD5E1", 1.1)
    for fold, sig, _ in points:
        x = _lin(fold, -3.2, 3.2, left + 14, right - 14)
        y = _lin(sig, 0, 5, bottom - 14, top + 14)
        color = "#BA4C5E" if fold > 1 and sig > 1.3 else "#477AA6" if fold < -1 and sig > 1.3 else "#94A3B8"
        c.circle(x, y, 4.5 if color != "#94A3B8" else 3.2, color, "#FFFFFF", 0.8, 0.82)
    placed_labels: list[tuple[float, float]] = []
    for fold, sig, label in sorted(points, key=lambda item: item[1] + abs(item[0]), reverse=True)[:12]:
        x = _lin(fold, -3.2, 3.2, left + 14, right - 14)
        y = _lin(sig, 0, 5, bottom - 14, top + 14)
        if any(abs(x - px) < 58 and abs(y - py) < 24 for px, py in placed_labels):
            continue
        dx = 10 if x < (left + right) / 2 else -10
        anchor = "start" if dx > 0 else "end"
        c.text(x + dx, y - 7, label, 11, 850, "#102033", anchor)
        placed_labels.append((x, y))
        if len(placed_labels) >= 4:
            break
    c.text((left + right) / 2, bottom + 34, "log2 fold change", 12, 760, "#64748B", "middle")
    c.text(left - 48, top + 12, "-log10 p", 12, 760, "#64748B")

    _panel(c, 800, 592, 748, 458, "D", "Metric correlation matrix", "Diverging colors expose redundant and conflicting metrics.")
    labels_corr = ["acc", "rob", "eff", "cal", "fair", "cost"]
    corr = _correlation_matrix(labels_corr)
    cell = 48
    hx, hy = 966, 714
    for i, label in enumerate(labels_corr):
        c.text(hx - 18, hy + i * cell + 30, label, 12, 760, "#102033", "end")
        c.text(hx + i * cell + cell / 2, hy - 18, label, 12, 760, "#102033", "middle")
    corr_palette = PALETTES["diverging_cork"]
    for i, row in enumerate(corr):
        for j, value in enumerate(row):
            idx = round(_lin(value, -1, 1, 0, len(corr_palette) - 1))
            color = corr_palette[max(0, min(len(corr_palette) - 1, int(idx)))]
            x, y = hx + j * cell, hy + i * cell
            c.rect(x + 2, y + 2, cell - 4, cell - 4, color, "#FFFFFF", 7)
            fill = "#FFFFFF" if abs(value) > 0.62 else "#102033"
            c.text(x + cell / 2, y + cell / 2 + 5, f"{value:.2f}", 10, 800, fill, "middle")
    c.text(1170, 1030, "Synthetic data only; intended to test composite layout grammar.", 12, 650, "#64748B", "middle")
    return c.render()


def bubble_quadrant() -> str:
    theme = Theme(width=920, height=620, bg="#F8FAFC", accent=PALETTE_ARCTIC[1])
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(
        "Opportunity map from synthetic paper signals",
        "Bubble size encodes evidence readiness; axes are random novelty and tractability scores.",
        "Synthetic data generated with fixed seed 20260708.",
    )
    left, right, top, bottom = 110, 850, 132, 536
    c.rect(left, top, right - left, bottom - top, "#FFFFFF", "#E2E8F0", 18)
    c.line((left + right) / 2, top + 18, (left + right) / 2, bottom - 18, "#CBD5E1", 1.4, 0.9)
    c.line(left + 18, (top + bottom) / 2, right - 18, (top + bottom) / 2, "#CBD5E1", 1.4, 0.9)
    c.text(left + 20, top + 32, "high risk / high novelty", 12, 700, "#64748B")
    c.text(right - 20, bottom - 18, "high tractability", 12, 700, "#64748B", "end")
    c.text(left - 18, bottom, "low", 11, 600, "#64748B", "end")
    c.text(left - 18, top + 8, "high", 11, 600, "#64748B", "end")
    for idx in range(17):
        novelty = RNG.uniform(0.12, 0.95)
        tractability = RNG.uniform(0.12, 0.95)
        readiness = RNG.uniform(0.25, 1.0)
        x = left + 30 + tractability * (right - left - 60)
        y = bottom - 30 - novelty * (bottom - top - 60)
        r = 8 + readiness * 21
        color = PALETTE_ARCTIC[idx % len(PALETTE_ARCTIC)]
        c.circle(x, y, r, color, "#FFFFFF", 2, 0.72)
        if idx in (2, 7, 13):
            c.text(x + r + 6, y + 4, f"S{idx + 1}", 11, 760, "#0F172A")
    c.text(left, bottom + 32, "tractability", 12, 760, "#475569")
    c.text(left - 64, top + 10, "novelty", 12, 760, "#475569")
    return c.render()


def evidence_table() -> str:
    theme = Theme(width=960, height=580, bg="#FBFAF8", accent=PALETTE_WINE[0])
    rows = []
    for label in ["Main result", "Ablation", "Robustness", "Efficiency", "Failure cases", "Reproducibility"]:
        rows.append(
            {
                "label": label,
                "support": RNG.uniform(0.52, 0.96),
                "clarity": RNG.uniform(0.45, 0.93),
                "risk": RNG.uniform(0.08, 0.58),
                "trend": [RNG.uniform(0.35, 0.92) for _ in range(8)],
            }
        )
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(
        "Evidence dashboard as a paper-ready table",
        "A compact table combines bars, risk chips, and sparklines from synthetic review data.",
        "Synthetic data generated with fixed seed 20260708.",
    )
    x0, y0 = 56, 124
    widths = [210, 190, 190, 140, 250]
    row_h = 54
    headers = ["Evidence block", "Support", "Clarity", "Risk", "Stability sparkline"]
    c.rect(x0, y0, sum(widths), row_h, "#2B183F", "none", 16)
    cursor = x0
    for idx, header in enumerate(headers):
        c.text(cursor + 16, y0 + 34, header, 13, 820, "#FFFFFF")
        cursor += widths[idx]
    for i, row in enumerate(rows):
        y = y0 + row_h * (i + 1)
        fill = "#FFFFFF" if i % 2 == 0 else "#F7F0F3"
        c.rect(x0, y, sum(widths), row_h, fill, "#E7DDE4", 0)
        c.text(x0 + 16, y + 33, row["label"], 13, 760, "#1F2937")
        sx = x0 + widths[0] + 16
        for j, key in enumerate(["support", "clarity"]):
            base = sx + j * widths[j + 1]
            value = float(row[key])
            color = PALETTE_WINE[(i + j) % len(PALETTE_WINE)]
            c.rect(base, y + 18, 124, 12, "#E5E7EB", "none", 6)
            c.rect(base, y + 18, 124 * value, 12, color, "none", 6)
            c.text(base + 136, y + 31, f"{value * 100:.0f}%", 12, 760, "#374151")
        risk = float(row["risk"])
        risk_color = "#6A994E" if risk < 0.25 else "#FB8B24" if risk < 0.45 else "#9A031E"
        rx = x0 + sum(widths[:3]) + 22
        c.rect(rx, y + 14, 74, 26, risk_color, "none", 13, 0.9)
        c.text(rx + 37, y + 32, f"{risk * 100:.0f}%", 12, 820, "#FFFFFF", "middle")
        spark_x = x0 + sum(widths[:4]) + 18
        points = _spark_path([float(v) for v in row["trend"]], spark_x, y + 14, 190, 25)
        c.polyline(points, PALETTE_WINE[(i + 2) % len(PALETTE_WINE)], 2.3)
        for px, py in points[-2:]:
            c.circle(px, py, 3.6, PALETTE_WINE[(i + 2) % len(PALETTE_WINE)], "#FFFFFF", 1)
    return c.render()


def build() -> list[Path]:
    outputs: list[Path] = []
    OUT.mkdir(parents=True, exist_ok=True)
    note = "Synthetic random data generated with fixed seed 20260708."

    outputs.append(
        save_svg(
            lollipop_rank(
                rows=[{"axis": f"Claim {i}", "score": _round(RNG.uniform(62, 96), 1)} for i in range(1, 8)],
                value_key="score",
                label_key="axis",
                title="Claim strength ranking",
                subtitle="Direct labels keep a dense comparison readable without legend hunting.",
                note=note,
                unit="",
                palette=PALETTE_GEM,
                theme=Theme(width=900, height=520, bg="#FAFBFF", accent=PALETTE_GEM[0]),
            ),
            OUT / "showcase-01-claim-strength-lollipop.svg",
        )
    )

    outputs.append(
        save_svg(
            slopegraph(
                rows=[
                    {"metric": name, "before": _round(before + RNG.uniform(-1.2, 1.2), 1), "after": _round(after + RNG.uniform(-1.8, 1.8), 1)}
                    for name, before, after in [
                        ("Motivation", 47, 74),
                        ("Method", 55, 80),
                        ("Evidence", 63, 87),
                        ("Visuals", 71, 91),
                        ("Rebuttal", 78, 95),
                    ]
                ],
                left_key="before",
                right_key="after",
                label_key="metric",
                title="Revision lift after CCFA coordination",
                left_label="Draft",
                right_label="Revised",
                subtitle="A paired-change view for before/after writing or experiment quality.",
                note=note,
                palette=PALETTE_NOCTURNE,
                theme=Theme(width=900, height=560, bg="#F7FAFC", accent=PALETTE_NOCTURNE[1]),
            ),
            OUT / "showcase-02-revision-lift-slopegraph.svg",
        )
    )

    outputs.append(
        save_svg(
            heatmap_matrix(
                matrix=[[round(RNG.uniform(0.42, 0.97) * 100, 1) for _ in range(6)] for _ in range(5)],
                row_labels=["Vision", "NLP", "ML", "Systems", "HCI"],
                col_labels=["novel", "sound", "abl.", "rob.", "eff.", "clear"],
                title="Evidence coverage matrix",
                subtitle="A table-like heatmap for quickly spotting weak evidence columns.",
                note=note,
                palette=PALETTE_CERAMIC,
                theme=Theme(width=920, height=540, bg="#FCFBF8", accent=PALETTE_CERAMIC[1]),
            ),
            OUT / "showcase-03-evidence-coverage-heatmap.svg",
        )
    )

    series = {
        "seed A": [RNG.gauss(72, 4.8) for _ in range(80)],
        "seed B": [RNG.gauss(77, 5.6) for _ in range(80)],
        "seed C": [RNG.gauss(82, 4.2) for _ in range(80)],
        "seed D": [RNG.gauss(86, 3.8) for _ in range(80)],
    }
    outputs.append(
        save_svg(
            ridgeline_density(
                series=series,
                title="Run stability ridgeline",
                subtitle="Distribution shapes make random-seed behavior visible without a crowded table.",
                note=note,
                palette=PALETTE_ORCHID,
                theme=Theme(width=920, height=580, bg="#FCF8FB", accent=PALETTE_ORCHID[1]),
            ),
            OUT / "showcase-04-run-stability-ridgeline.svg",
        )
    )

    panels = []
    for title, base, drift in [
        ("loss", 1.2, -0.08),
        ("accuracy", 58, 3.4),
        ("latency", 84, -2.6),
        ("memory", 62, -1.4),
        ("stability", 70, 2.1),
        ("coverage", 48, 4.2),
    ]:
        values = []
        current = base
        for _ in range(8):
            current += drift + RNG.uniform(-2.1, 2.1)
            values.append(_round(current, 2))
        panels.append({"title": title, "x": list(range(len(values))), "y": values})
    outputs.append(
        save_svg(
            small_multiple_lines(
                panels=panels,
                title="Six-panel analysis surface",
                subtitle="Small multiples keep heterogeneous metrics comparable while avoiding one overstuffed chart.",
                note=note,
                palette=PALETTE_ARCTIC,
                theme=Theme(width=980, height=650, bg="#F8FCFD", accent=PALETTE_ARCTIC[2]),
            ),
            OUT / "showcase-05-analysis-small-multiples.svg",
        )
    )

    outputs.append(
        save_svg(
            radial_scorecard(
                scores=[
                    {"axis": axis, "value": RNG.uniform(0.58, 0.96)}
                    for axis in ["story", "novelty", "method", "evidence", "visual", "format", "risk"]
                ],
                value_key="value",
                label_key="axis",
                title="Submission readiness profile",
                subtitle="A secondary summary view for multi-criterion readiness checks.",
                note=note,
                max_value=1.0,
                palette=PALETTE_INK,
                theme=Theme(width=760, height=740, bg="#F9FAFB", accent=PALETTE_INK[2]),
            ),
            OUT / "showcase-06-readiness-radial-scorecard.svg",
        )
    )

    outputs.append(save_svg(bubble_quadrant(), OUT / "showcase-07-opportunity-bubble-map.svg"))
    outputs.append(save_svg(evidence_table(), OUT / "showcase-08-evidence-dashboard-table.svg"))

    outputs.append(
        save_svg(
            donut_chart(
                rows=[
                    {"source": "benchmark", "value": 42},
                    {"source": "ablation", "value": 24},
                    {"source": "robustness", "value": 16},
                    {"source": "efficiency", "value": 11},
                    {"source": "case study", "value": 7},
                ],
                value_key="value",
                label_key="source",
                title="Evidence-source composition",
                subtitle="Donut charts are useful when composition is the question, not precise ranking.",
                note=note,
                palette=PALETTE_CERAMIC,
                theme=Theme(width=820, height=560, bg="#FCFBF8", accent=PALETTE_CERAMIC[1]),
            ),
            OUT / "showcase-09-evidence-composition-donut.svg",
        )
    )

    outputs.append(
        save_svg(
            grouped_bar_chart(
                rows=[
                    {"setting": "clean", "base": 72, "ours": 86, "oracle": 91},
                    {"setting": "shift", "base": 61, "ours": 79, "oracle": 84},
                    {"setting": "low-data", "base": 54, "ours": 73, "oracle": 80},
                    {"setting": "noisy", "base": 48, "ours": 68, "oracle": 77},
                ],
                group_key="setting",
                series_keys=["base", "ours", "oracle"],
                title="Grouped benchmark comparison",
                subtitle="Grouped bars make categorical comparison stronger than a pie chart.",
                note=note,
                palette=PALETTE_NOCTURNE,
                theme=Theme(width=940, height=560, bg="#F7FAFC", accent=PALETTE_NOCTURNE[1]),
            ),
            OUT / "showcase-10-grouped-benchmark-bars.svg",
        )
    )

    volcano_rows = []
    for i in range(180):
        fold = RNG.gauss(0, 1.35)
        p_value = 10 ** (-RNG.uniform(0.08, 4.8)) if abs(fold) > 1.05 else 10 ** (-RNG.uniform(0.02, 2.0))
        volcano_rows.append({"feature": f"m{i + 1}", "fold": fold, "p": p_value})
    outputs.append(
        save_svg(
            volcano_plot(
                rows=volcano_rows,
                fold_key="fold",
                p_key="p",
                label_key="feature",
                title="Volcano plot for candidate module discovery",
                subtitle="Effect size and significance thresholds are visible without a separate legend.",
                note=note,
                palette=["#1F6F8B", "#B58B2A", "#BA4C5E", "#94A3B8"],
                theme=Theme(width=920, height=600, bg="#F9FBFD", accent="#1F6F8B"),
            ),
            OUT / "showcase-11-volcano-candidate-screen.svg",
        )
    )

    corr_labels = ["acc", "rob", "cal", "fair", "cost", "lat", "mem"]
    outputs.append(
        save_svg(
            correlation_heatmap(
                matrix=_correlation_matrix(corr_labels),
                labels=corr_labels,
                title="Correlation analysis matrix",
                subtitle="Diverging colors help separate reinforcing and conflicting metric families.",
                note=note,
                palette=PALETTES["diverging_cork"],
                theme=Theme(width=820, height=760, bg="#FAFAFB", accent="#6C2E67"),
            ),
            OUT / "showcase-12-correlation-analysis-heatmap.svg",
        )
    )

    outputs.append(
        save_svg(
            composite_analysis_dashboard(),
            OUT / "showcase-13-composite-analysis-dashboard.svg",
        )
    )
    return outputs


if __name__ == "__main__":
    for path in build():
        print(path.relative_to(ROOT).as_posix())
