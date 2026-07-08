#!/usr/bin/env python3
"""CCFA publication-visual plotting recipes.

The recipes are original CCFA implementations inspired by public plotting
galleries and scientific visualization principles. They use only Python's
standard library and export editable SVG, so demos can run in a bare
environment. Users may port the same contracts to Matplotlib, Seaborn, Plotly,
Altair, or Bokeh when those libraries are available.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from math import exp, pi, sqrt
from pathlib import Path
from statistics import mean, pstdev
from typing import Iterable, Sequence


PALETTES = {
    "okabe_ito": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"],
    "npg": ["#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F", "#8491B4", "#91D1C2", "#DC0000", "#7E6148", "#B09C85"],
    "ccfa": ["#1F6F8B", "#D2673D", "#6657A8", "#2A9D8F", "#B58B2A", "#BA4C5E", "#477AA6", "#5D6977"],
    "sequential_blue": ["#F7FBFF", "#DEEBF7", "#C6DBEF", "#9ECAE1", "#6BAED6", "#3182BD", "#08519C"],
    "sequential_mint": ["#F7FCF5", "#E5F5E0", "#C7E9C0", "#A1D99B", "#74C476", "#31A354", "#006D2C"],
    "diverging_cork": ["#6C2E67", "#B2669E", "#E6C5DE", "#F7F7F7", "#BFD9CA", "#5DAA86", "#0B6B53"],
    "neutral": ["#17212B", "#4E5A66", "#8B96A3", "#C9D1D9", "#EEF2F6"],
}


@dataclass(frozen=True)
class Theme:
    width: int = 900
    height: int = 520
    bg: str = "#FBFCFE"
    ink: str = "#17212B"
    muted: str = "#5D6977"
    grid: str = "#DCE4EC"
    panel: str = "#FFFFFF"
    accent: str = "#1F6F8B"
    font: str = "Inter, Segoe UI, Arial, sans-serif"
    mono: str = "Consolas, Menlo, monospace"


class Canvas:
    def __init__(self, width: int, height: int, theme: Theme | None = None) -> None:
        self.w = width
        self.h = height
        self.theme = theme or Theme(width=width, height=height)
        self.parts: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<style>text{{font-family:{self.theme.font};dominant-baseline:auto}} .mono{{font-family:{self.theme.mono}}}</style>',
            f'<rect x="0" y="0" width="{width}" height="{height}" rx="0" fill="{self.theme.bg}"/>',
        ]

    def rect(self, x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", rx: float = 0, opacity: float = 1) -> None:
        self.parts.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx:.2f}" fill="{fill}" stroke="{stroke}" opacity="{opacity:.3f}"/>'
        )

    def line(self, x1: float, y1: float, x2: float, y2: float, stroke: str, width: float = 1.5, opacity: float = 1) -> None:
        self.parts.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{width:.2f}" stroke-linecap="round" opacity="{opacity:.3f}"/>'
        )

    def circle(self, x: float, y: float, r: float, fill: str, stroke: str = "none", width: float = 1.5, opacity: float = 1) -> None:
        self.parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{width:.2f}" opacity="{opacity:.3f}"/>'
        )

    def polyline(self, points: Sequence[tuple[float, float]], stroke: str, width: float = 2.5, fill: str = "none", opacity: float = 1) -> None:
        data = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        self.parts.append(
            f'<polyline points="{data}" fill="{fill}" stroke="{stroke}" stroke-width="{width:.2f}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity:.3f}"/>'
        )

    def polygon(self, points: Sequence[tuple[float, float]], fill: str, stroke: str = "none", width: float = 1.2, opacity: float = 1) -> None:
        data = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        self.parts.append(
            f'<polygon points="{data}" fill="{fill}" stroke="{stroke}" stroke-width="{width:.2f}" opacity="{opacity:.3f}"/>'
        )

    def text(
        self,
        x: float,
        y: float,
        value: str,
        size: int = 14,
        weight: int = 500,
        fill: str | None = None,
        anchor: str = "start",
        klass: str = "",
    ) -> None:
        fill = fill or self.theme.ink
        cls = f' class="{klass}"' if klass else ""
        self.parts.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{cls}>{escape(str(value))}</text>'
        )

    def label_block(self, title: str, subtitle: str | None = None, note: str | None = None) -> None:
        self.text(42, 52, title, 28, 820)
        if subtitle:
            self.text(42, 82, subtitle, 14, 520, self.theme.muted)
        if note:
            self.text(42, self.h - 24, note, 11, 500, self.theme.muted)

    def render(self) -> str:
        return "\n".join(self.parts + ["</svg>\n"])


def save_svg(svg: str, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(svg, encoding="utf-8")
    return target


def _extent(values: Iterable[float]) -> tuple[float, float]:
    vals = list(values)
    lo, hi = min(vals), max(vals)
    if lo == hi:
        return lo - 0.5, hi + 0.5
    pad = (hi - lo) * 0.05
    return lo - pad, hi + pad


def _scale(value: float, lo: float, hi: float, out_lo: float, out_hi: float) -> float:
    if hi == lo:
        return (out_lo + out_hi) / 2
    return out_lo + (value - lo) / (hi - lo) * (out_hi - out_lo)


def _pretty(value: float, digits: int = 1) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.{digits}f}"


def lollipop_rank(
    rows: Sequence[dict[str, object]],
    value_key: str,
    label_key: str,
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    unit: str = "",
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme()
    palette = list(palette or PALETTES["ccfa"])
    data = sorted(rows, key=lambda r: float(r[value_key]))
    values = [float(row[value_key]) for row in data]
    lo = min(0, min(values))
    hi = max(values) * 1.12
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, right, top, bottom = 230, theme.width - 70, 122, theme.height - 70
    c.line(left, bottom, right, bottom, theme.grid, 1)
    for frac in (0, 0.25, 0.5, 0.75, 1):
        x = left + (right - left) * frac
        c.line(x, top - 14, x, bottom, theme.grid, 0.8, 0.8)
        c.text(x, bottom + 24, _pretty(lo + (hi - lo) * frac), 11, 500, theme.muted, "middle")
    gap = (bottom - top) / max(1, len(data) - 1)
    for i, row in enumerate(data):
        y = bottom - i * gap
        value = float(row[value_key])
        color = palette[i % len(palette)]
        x = _scale(value, lo, hi, left, right)
        c.text(left - 18, y + 5, str(row[label_key]), 13, 650, theme.ink, "end")
        c.line(left, y, x, y, color, 5, 0.78)
        c.circle(x, y, 8.5, color, "#FFFFFF", 2)
        c.text(x + 14, y + 5, f"{_pretty(value)}{unit}", 12, 760, theme.ink)
    return c.render()


def slopegraph(
    rows: Sequence[dict[str, object]],
    left_key: str,
    right_key: str,
    label_key: str,
    title: str,
    left_label: str,
    right_label: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=820, height=560)
    palette = list(palette or PALETTES["npg"])
    left_vals = [float(r[left_key]) for r in rows]
    right_vals = [float(r[right_key]) for r in rows]
    lo, hi = _extent(left_vals + right_vals)
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    top, bottom = 126, theme.height - 68
    x1, x2 = 245, theme.width - 245
    c.text(x1, 108, left_label, 15, 820, theme.ink, "middle")
    c.text(x2, 108, right_label, 15, 820, theme.ink, "middle")
    c.line(x1, top, x1, bottom, theme.grid, 1.2)
    c.line(x2, top, x2, bottom, theme.grid, 1.2)
    for i, row in enumerate(rows):
        color = palette[i % len(palette)]
        y1 = _scale(float(row[left_key]), lo, hi, bottom, top)
        y2 = _scale(float(row[right_key]), lo, hi, bottom, top)
        c.line(x1, y1, x2, y2, color, 2.6, 0.82)
        c.circle(x1, y1, 6, color, "#FFFFFF", 1.5)
        c.circle(x2, y2, 6, color, "#FFFFFF", 1.5)
        c.text(x1 - 18, y1 + 5, f"{row[label_key]}  {_pretty(float(row[left_key]))}", 12, 650, theme.ink, "end")
        c.text(x2 + 18, y2 + 5, f"{_pretty(float(row[right_key]))}", 12, 650, theme.ink)
    return c.render()


def heatmap_matrix(
    matrix: Sequence[Sequence[float]],
    row_labels: Sequence[str],
    col_labels: Sequence[str],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=860, height=560)
    palette = list(palette or PALETTES["sequential_blue"])
    flat = [float(v) for row in matrix for v in row]
    lo, hi = min(flat), max(flat)
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, top = 190, 132
    cell_w = (theme.width - left - 60) / len(col_labels)
    cell_h = min(56, (theme.height - top - 82) / len(row_labels))
    for j, label in enumerate(col_labels):
        c.text(left + j * cell_w + cell_w / 2, top - 18, label, 12, 720, theme.muted, "middle")
    for i, row in enumerate(matrix):
        y = top + i * cell_h
        c.text(left - 18, y + cell_h / 2 + 5, row_labels[i], 12, 650, theme.ink, "end")
        for j, value in enumerate(row):
            idx = round(_scale(float(value), lo, hi, 0, len(palette) - 1))
            color = palette[max(0, min(len(palette) - 1, int(idx)))]
            x = left + j * cell_w
            c.rect(x + 3, y + 3, cell_w - 6, cell_h - 6, color, "#FFFFFF", 10)
            fill = "#FFFFFF" if idx > len(palette) * 0.6 else theme.ink
            c.text(x + cell_w / 2, y + cell_h / 2 + 5, _pretty(float(value)), 12, 760, fill, "middle")
    return c.render()


def _density(values: Sequence[float], xs: Sequence[float]) -> list[float]:
    vals = [float(v) for v in values]
    sd = pstdev(vals) or 1.0
    bandwidth = max(sd * 0.55, (max(vals) - min(vals)) / 18 or 1.0)
    norm = 1 / (sqrt(2 * pi) * bandwidth * max(1, len(vals)))
    result = []
    for x in xs:
        result.append(sum(exp(-0.5 * ((x - v) / bandwidth) ** 2) for v in vals) * norm)
    return result


def ridgeline_density(
    series: dict[str, Sequence[float]],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=920, height=580)
    palette = list(palette or PALETTES["ccfa"])
    all_values = [float(v) for vals in series.values() for v in vals]
    lo, hi = _extent(all_values)
    xs = [lo + (hi - lo) * i / 80 for i in range(81)]
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, right = 118, theme.width - 62
    top, bottom = 136, theme.height - 76
    row_gap = (bottom - top) / max(1, len(series) - 1)
    for idx, (label, vals) in enumerate(series.items()):
        base = bottom - idx * row_gap
        dens = _density(vals, xs)
        peak = max(dens) or 1.0
        points = [(left + (x - lo) / (hi - lo) * (right - left), base - d / peak * row_gap * 0.72) for x, d in zip(xs, dens)]
        poly = [(points[0][0], base)] + points + [(points[-1][0], base)]
        color = palette[idx % len(palette)]
        c.polygon(poly, color, "none", opacity=0.36)
        c.polyline(points, color, 2.5, opacity=0.92)
        c.line(left, base, right, base, theme.grid, 0.8, 0.72)
        c.text(left - 18, base + 4, label, 12, 720, theme.ink, "end")
        c.circle(_scale(mean([float(v) for v in vals]), lo, hi, left, right), base, 4.8, color, "#FFFFFF", 1.4)
    for frac in (0, 0.25, 0.5, 0.75, 1):
        x = left + (right - left) * frac
        c.text(x, bottom + 30, _pretty(lo + (hi - lo) * frac), 11, 500, theme.muted, "middle")
    return c.render()


def small_multiple_lines(
    panels: Sequence[dict[str, object]],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=960, height=620)
    palette = list(palette or PALETTES["ccfa"])
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    cols = 2 if len(panels) <= 4 else 3
    rows = (len(panels) + cols - 1) // cols
    gap = 26
    left, top = 70, 128
    plot_w = (theme.width - left * 2 - gap * (cols - 1)) / cols
    plot_h = (theme.height - top - 58 - gap * (rows - 1)) / rows
    for idx, panel in enumerate(panels):
        px = left + (idx % cols) * (plot_w + gap)
        py = top + (idx // cols) * (plot_h + gap)
        xs = [float(v) for v in panel["x"]]  # type: ignore[index]
        ys = [float(v) for v in panel["y"]]  # type: ignore[index]
        xlo, xhi = _extent(xs)
        ylo, yhi = _extent(ys)
        color = palette[idx % len(palette)]
        c.rect(px, py, plot_w, plot_h, "#FFFFFF", "#E6ECF2", 14)
        c.text(px + 14, py + 24, str(panel["title"]), 13, 760, theme.ink)
        for frac in (0.33, 0.66):
            c.line(px + 12, py + plot_h * frac, px + plot_w - 12, py + plot_h * frac, theme.grid, 0.7, 0.8)
        points = [(_scale(x, xlo, xhi, px + 18, px + plot_w - 18), _scale(y, ylo, yhi, py + plot_h - 22, py + 42)) for x, y in zip(xs, ys)]
        c.polyline(points, color, 2.8)
        for x, y in points:
            c.circle(x, y, 3.5, color, "#FFFFFF", 1)
        c.text(px + 14, py + plot_h - 10, f"{_pretty(ylo)} - {_pretty(yhi)}", 10, 500, theme.muted)
    return c.render()


def radial_scorecard(
    scores: Sequence[dict[str, object]],
    value_key: str,
    label_key: str,
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    max_value: float = 1.0,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=720, height=720)
    palette = list(palette or PALETTES["ccfa"])
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    cx, cy = theme.width / 2, theme.height / 2 + 32
    radius = min(theme.width, theme.height) * 0.31
    from math import cos, sin, tau

    n = len(scores)
    rings = [0.25, 0.5, 0.75, 1.0]
    for r in rings:
        c.circle(cx, cy, radius * r, "none", theme.grid, 1)
    points = []
    for i, score in enumerate(scores):
        angle = -pi / 2 + tau * i / n
        value = max(0.0, min(max_value, float(score[value_key]))) / max_value
        x = cx + cos(angle) * radius * value
        y = cy + sin(angle) * radius * value
        points.append((x, y))
        lx = cx + cos(angle) * (radius + 46)
        ly = cy + sin(angle) * (radius + 46)
        c.line(cx, cy, cx + cos(angle) * radius, cy + sin(angle) * radius, theme.grid, 0.8)
        c.text(lx, ly + 4, str(score[label_key]), 11, 650, theme.ink, "middle")
    c.polygon(points, palette[0], palette[0], 2, 0.22)
    c.polyline(points + [points[0]], palette[0], 2.8)
    for i, (x, y) in enumerate(points):
        c.circle(x, y, 5.5, palette[i % len(palette)], "#FFFFFF", 1.5)
    return c.render()


def recipe_catalog() -> dict[str, str]:
    return {
        "lollipop_rank": "Ranked comparisons with direct value labels; good for headline results.",
        "slopegraph": "Before/after or base/big comparison; good for paired scientific changes.",
        "heatmap_matrix": "Dense model/config/result matrix; good for compact tables-as-visuals.",
        "ridgeline_density": "Distribution comparison; good for seeds, runs, samples, or uncertainty.",
        "small_multiple_lines": "Repeated temporal or scale trends with shared grammar.",
        "radial_scorecard": "Compact multi-criterion profile; use carefully and always label scale.",
    }
