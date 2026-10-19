#!/usr/bin/env python3
"""CCFA publication-visual plotting recipes.

The recipes are original CCFA implementations inspired by public plotting
galleries and scientific visualization principles. They use only Python's
standard library and export editable SVG, so demos can run in a bare
environment. Users may port the same contracts to Matplotlib, Seaborn, Plotly,
Altair, or Bokeh when those libraries are available.
"""

from __future__ import annotations

from collections.abc import Iterable as IterableABC
from dataclasses import dataclass
from html import escape
from math import cos, exp, floor, isfinite, log10, pi, sin, sqrt, tau
from os import replace
from pathlib import Path
from statistics import mean, pstdev
from tempfile import NamedTemporaryFile
from typing import Iterable, Mapping, Sequence
from xml.etree import ElementTree


PALETTES = {
    "okabe_ito": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"],
    "npg": ["#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F", "#8491B4", "#91D1C2", "#DC0000", "#7E6148", "#B09C85"],
    "ccfa": ["#1F6F8B", "#D2673D", "#6657A8", "#2A9D8F", "#B58B2A", "#BA4C5E", "#477AA6", "#5D6977"],
    "ccfa_gem": ["#174A7C", "#D95F02", "#1B9E77", "#7570B3", "#E7298A", "#66A61E", "#E6AB02"],
    "ccfa_nocturne": ["#0E2A47", "#28587B", "#9FB798", "#F2C14E", "#F78154", "#B4436C"],
    "ccfa_ceramic": ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51", "#8AB17D"],
    "ccfa_orchid": ["#3B1F5E", "#6A4C93", "#B565A7", "#E56B6F", "#EAAC8B", "#355070"],
    "ccfa_arctic": ["#063B63", "#0B7285", "#38A3A5", "#80ED99", "#F4D35E", "#EE964B"],
    "ccfa_wine": ["#5F0F40", "#9A031E", "#FB8B24", "#E36414", "#0F4C5C", "#6A994E"],
    "ccfa_ink": ["#111827", "#374151", "#1D4ED8", "#059669", "#D97706", "#BE123C"],
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
    font: str = "Times New Roman, Times, Noto Serif CJK SC, Source Han Serif SC, SimSun, serif"
    mono: str = "Consolas, Menlo, monospace"
    paper_width_in: float | None = None
    min_font_pt: float = 8.0

    def __post_init__(self) -> None:
        for name in ("width", "height", "min_font_pt"):
            if _number(getattr(self, name), name) <= 0:
                raise ValueError(f"{name} must be positive")
        if self.paper_width_in is not None and _number(self.paper_width_in, "paper_width_in") <= 0:
            raise ValueError("paper_width_in must be positive")


@dataclass(frozen=True)
class ColorNorm:
    """A reusable color range; values outside it are errors, never clipped."""

    vmin: float
    vmax: float
    center: float | None = None

    def __post_init__(self) -> None:
        lo, hi = _number(self.vmin, "vmin"), _number(self.vmax, "vmax")
        object.__setattr__(self, "vmin", lo)
        object.__setattr__(self, "vmax", hi)
        if lo > hi:
            raise ValueError("vmin must not exceed vmax")
        if not isfinite(hi - lo):
            raise ValueError("Color range is too wide for floating-point display; use an explicitly rescaled unit")
        if self.center is not None and not lo < _number(self.center, "center") < hi:
            raise ValueError("center must be strictly between vmin and vmax")
        if self.center is not None:
            object.__setattr__(self, "center", float(self.center))

    def position(self, value: float) -> float:
        value = _number(value, "color value")
        if not self.vmin <= value <= self.vmax:
            raise ValueError(f"Color value {value:g} lies outside [{self.vmin:g}, {self.vmax:g}]; expand the shared color range")
        if self.vmin == self.vmax:
            return 0.5
        if self.center is None:
            return (value - self.vmin) / (self.vmax - self.vmin)
        if value <= self.center:
            return 0.5 * (value - self.vmin) / (self.center - self.vmin)
        return 0.5 + 0.5 * (value - self.center) / (self.vmax - self.center)


class Canvas:
    def __init__(self, width: int, height: int, theme: Theme | None = None) -> None:
        self.w = width
        self.h = height
        self.theme = theme or Theme(width=width, height=height)
        physical_width = f"{self.theme.paper_width_in:g}in" if self.theme.paper_width_in is not None else str(width)
        physical_height = f"{self.theme.paper_width_in * height / width:g}in" if self.theme.paper_width_in is not None else str(height)
        self.parts: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{physical_width}" height="{physical_height}" viewBox="0 0 {width} {height}">',
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

    def path(self, d: str, fill: str, stroke: str = "none", width: float = 1.2, opacity: float = 1) -> None:
        self.parts.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width:.2f}" opacity="{opacity:.3f}"/>'
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
        size: float = 14,
        weight: int = 500,
        fill: str | None = None,
        anchor: str = "start",
        klass: str = "",
    ) -> None:
        fill = fill or self.theme.ink
        if self.theme.paper_width_in is not None:
            size = max(size, self.theme.min_font_pt * self.w / (72 * self.theme.paper_width_in))
        cls = f' class="{klass}"' if klass else ""
        self.parts.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size:.6f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{cls}>{escape(str(value))}</text>'
        )

    def label_block(self, title: str, subtitle: str | None = None, note: str | None = None) -> None:
        if title:
            self.text(42, 52, title, 28, 820)
        if subtitle:
            self.text(42, 82, subtitle, 14, 520, self.theme.muted)
        if note:
            self.text(42, self.h - 24, note, 11, 500, self.theme.muted)

    def render(self) -> str:
        return "\n".join(self.parts + ["</svg>\n"])


def save_svg(svg: str, path: str | Path) -> Path:
    """Publish a valid candidate in place without truncating the previous SVG."""
    root = ElementTree.fromstring(svg)
    if root.tag not in {"svg", "{http://www.w3.org/2000/svg}svg"}:
        raise ValueError("Expected an SVG document")
    target = Path(path)
    # Keep an existing symlinked authoring path intact.
    destination = target.resolve()
    if destination.is_file() and destination.read_text(encoding="utf-8-sig") == svg:
        return target
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=destination.parent, prefix=f".{destination.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(svg)
        replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return target


def _extent(values: Iterable[float]) -> tuple[float, float]:
    vals = _numbers(values, "axis values")
    lo, hi = min(vals), max(vals)
    if lo == hi:
        return lo - 0.5, hi + 0.5
    pad = (hi - lo) * 0.05
    if not isfinite(lo - pad) or not isfinite(hi + pad):
        raise ValueError("Axis range is too wide for floating-point display; use an explicitly rescaled unit")
    return lo - pad, hi + pad


def _scale(value: float, lo: float, hi: float, out_lo: float, out_hi: float) -> float:
    if hi == lo:
        return (out_lo + out_hi) / 2
    return out_lo + (value - lo) / (hi - lo) * (out_hi - out_lo)


def _pretty(value: float, digits: int = 1) -> str:
    if value == 0:
        return "0"
    if abs(value) < 0.01 or abs(value) >= 1e6:
        return f"{value:.15g}"
    if value == int(value):
        return str(int(value))
    # Keep at least two significant digits for small nonzero measurements.
    places = max(digits, 1 - floor(log10(abs(value))))
    return f"{value:.{places}f}"


def _tick_labels(values: Sequence[float], digits: int = 1) -> list[str]:
    """Increase precision as a group so distinct ticks never share a label."""
    labels = [_pretty(value, digits) for value in values]
    distinct_values = sorted(set(values))
    if len(distinct_values) <= 1:
        return labels
    tolerance = min(b - a for a, b in zip(distinct_values, distinct_values[1:])) * 0.001

    def accurate(candidate: Sequence[str]) -> bool:
        numbers = [float(label) for label in candidate]
        return len(set(numbers)) == len(distinct_values) and all(abs(number - value) <= tolerance for number, value in zip(numbers, values))

    if accurate(labels):
        return labels
    for precision in range(2, 18):
        labels = [f"{value:.{precision}g}" for value in values]
        if accurate(labels):
            return labels
    return [repr(value) for value in values]


def _number(value: object, name: str) -> float:
    try:
        result = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number; received {value!r}") from exc
    if not isfinite(result):
        raise ValueError(f"{name} must be finite; received {value!r}")
    return result


def _numbers(values: Iterable[object], name: str) -> list[float]:
    if isinstance(values, (str, bytes)) or not isinstance(values, IterableABC):
        raise ValueError(f"{name} must be a sequence of finite numbers")
    result = [_number(value, f"{name}[{i}]") for i, value in enumerate(values)]
    if not result:
        raise ValueError(f"{name} must contain at least one value")
    return result


def _labels(values: Sequence[object], name: str, *, unique: bool = False) -> list[str]:
    if isinstance(values, (str, bytes)) or not isinstance(values, IterableABC):
        raise ValueError(f"{name} must be a sequence of labels")
    if any(value is None for value in values):
        raise ValueError(f"{name} must not contain missing labels")
    labels = [str(value) for value in values]
    if not labels or any(not label.strip() for label in labels):
        raise ValueError(f"{name} must contain non-empty labels")
    if unique and len(set(labels)) != len(labels):
        raise ValueError(f"{name} must be unique; use distinct entity IDs")
    return labels


def _matrix(matrix: Sequence[Sequence[float]], row_labels: Sequence[str], col_labels: Sequence[str]) -> list[list[float]]:
    _labels(row_labels, "row_labels", unique=True)
    _labels(col_labels, "col_labels", unique=True)
    if len(matrix) != len(row_labels):
        raise ValueError("matrix row count must match row_labels")
    values = []
    for i, row in enumerate(matrix):
        if isinstance(row, (str, bytes)) or not hasattr(row, "__len__"):
            raise ValueError(f"matrix row {i} must be a sequence of numbers")
        if len(row) != len(col_labels):
            raise ValueError(f"matrix row {i} has {len(row)} cells; expected {len(col_labels)} col_labels")
        values.append(_numbers(row, f"matrix[{i}]"))
    return values


def _palette(palette: Sequence[str] | None, default: Sequence[str], minimum: int = 1) -> list[str]:
    colors = list(default if palette is None else palette)
    if len(colors) < minimum or any(not isinstance(color, str) or not color.strip() for color in colors):
        raise ValueError(f"palette must contain at least {minimum} non-empty colors")
    return colors


def _column(rows: Sequence[dict[str, object]], key: str) -> list[float]:
    if not rows:
        raise ValueError("rows must contain at least one observation")
    values = []
    for i, row in enumerate(rows):
        if key not in row:
            raise ValueError(f"rows[{i}] is missing {key!r}")
        values.append(_number(row[key], f"rows[{i}][{key!r}]"))
    return values


def _row_labels(rows: Sequence[dict[str, object]], key: str) -> list[str]:
    if any(key not in row for row in rows):
        raise ValueError(f"Every row must provide label key {key!r}")
    return _labels([row[key] for row in rows], key)


def _plot_top(title: str, subtitle: str | None) -> float:
    return 128 if subtitle else 100 if title else 28


def _contrast(color: str) -> str:
    """Readable annotation color for hex palettes; conservative for named colors."""
    if color.startswith("#") and len(color) in (4, 7):
        text = "".join(ch * 2 for ch in color[1:]) if len(color) == 4 else color[1:]
        try:
            channels = [int(text[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        except ValueError:
            return "#17212B"
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
        luminance = sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))
        return "#FFFFFF" if luminance < 0.179 else "#17212B"
    return "#17212B"


def _colorbar(c: Canvas, norm: ColorNorm, palette: Sequence[str], x: float, y: float, width: float, label: str = "") -> None:
    sw = width / len(palette)
    c.parts.append(f'<g data-color-min="{norm.vmin:g}" data-color-max="{norm.vmax:g}">')
    for i, color in enumerate(palette):
        c.rect(x + i * sw, y, sw, 12, color)
    tick_values = [norm.vmin, norm.vmax] + ([norm.center] if norm.center is not None else [])
    tick_labels = _tick_labels(tick_values, 2)
    c.text(x, y + 29, tick_labels[0], 11, 500, c.theme.muted)
    c.text(x + width, y + 29, tick_labels[1], 11, 500, c.theme.muted, "end")
    if norm.center is not None:
        c.text(x + width / 2, y + 29, tick_labels[2], 11, 500, c.theme.muted, "middle")
    if label:
        c.text(x + width / 2, y - 9, label, 11, 500, c.theme.muted, "middle")
    c.parts.append("</g>")


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
    palette = _palette(palette, PALETTES["ccfa"])
    _column(rows, value_key)
    _row_labels(rows, label_key)
    data = sorted(rows, key=lambda r: float(r[value_key]))
    values = [float(row[value_key]) for row in data]
    lo = min(0, min(values))
    hi = max(0, max(values))
    span = hi - lo or 1.0
    lo, hi = lo - span * 0.06 if lo < 0 else 0, hi + span * 0.12
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, right, top, bottom = 230, theme.width - 70, 122, theme.height - 70
    c.line(left, bottom, right, bottom, theme.grid, 1)
    fractions = (0, 0.25, 0.5, 0.75, 1)
    tick_labels = _tick_labels([lo + (hi - lo) * frac for frac in fractions])
    for frac, tick_label in zip(fractions, tick_labels):
        x = left + (right - left) * frac
        c.line(x, top - 14, x, bottom, theme.grid, 0.8, 0.8)
        c.text(x, bottom + 24, tick_label, 11, 500, theme.muted, "middle")
    gap = (bottom - top) / max(1, len(data) - 1)
    for i, row in enumerate(data):
        y = bottom - i * gap
        value = float(row[value_key])
        color = palette[i % len(palette)]
        x = _scale(value, lo, hi, left, right)
        c.text(left - 18, y + 5, str(row[label_key]), 13, 650, theme.ink, "end")
        c.line(_scale(0, lo, hi, left, right), y, x, y, color, 5, 0.78)
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
    palette = _palette(palette, PALETTES["npg"])
    left_vals = _column(rows, left_key)
    right_vals = _column(rows, right_key)
    _row_labels(rows, label_key)
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
    *,
    vmin: float | None = None,
    vmax: float | None = None,
    center: float | None = None,
    norm: ColorNorm | None = None,
    show_values: bool = True,
    show_colorbar: bool = True,
    colorbar_label: str = "",
) -> str:
    """Render a matrix; reuse ColorNorm across panels for comparable colors."""
    theme = theme or Theme(width=860, height=560)
    matrix = _matrix(matrix, row_labels, col_labels)
    flat = [v for row in matrix for v in row]
    if norm is not None and any(value is not None for value in (vmin, vmax, center)):
        raise ValueError("Pass norm or vmin/vmax/center, not both")
    if norm is None:
        if center is not None and vmin is None and vmax is None:
            center = _number(center, "center")
            radius = max(abs(v - center) for v in flat) or 1.0
            vmin, vmax = center - radius, center + radius
        norm = ColorNorm(min(flat) if vmin is None else vmin, max(flat) if vmax is None else vmax, center)
    if not isinstance(norm, ColorNorm):
        raise ValueError("norm must be a ColorNorm shared by the compared matrices")
    positions = [[norm.position(value) for value in row] for row in matrix]
    palette = _palette(palette, PALETTES["diverging_cork" if norm.center is not None else "sequential_blue"], minimum=2)
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, top = 190, _plot_top(title, subtitle) + 18
    cell_w = (theme.width - left - 60) / len(col_labels)
    cell_h = min(56, (theme.height - top - (112 if show_colorbar else 50)) / len(row_labels))
    minimum_cell = max(18, theme.min_font_pt * theme.width / (72 * theme.paper_width_in) + 10) if theme.paper_width_in else 18
    if cell_w < minimum_cell or cell_h < minimum_cell:
        raise ValueError("Heatmap cells are too small; increase Theme width/height or split the matrix")
    for j, label in enumerate(col_labels):
        c.text(left + j * cell_w + cell_w / 2, top - 18, label, 12, 720, theme.muted, "middle")
    for i, row in enumerate(matrix):
        y = top + i * cell_h
        c.text(left - 18, y + cell_h / 2 + 5, row_labels[i], 12, 650, theme.ink, "end")
        for j, value in enumerate(row):
            idx = round(positions[i][j] * (len(palette) - 1))
            color = palette[idx]
            x = left + j * cell_w
            c.rect(x + 3, y + 3, cell_w - 6, cell_h - 6, color, "#FFFFFF", 10)
            if show_values:
                c.text(x + cell_w / 2, y + cell_h / 2 + 5, _pretty(value), 12, 760, _contrast(color), "middle")
    if show_colorbar:
        _colorbar(c, norm, palette, left, top + len(matrix) * cell_h + 36, min(280, cell_w * len(col_labels)), colorbar_label)
    return c.render()


def donut_chart(
    rows: Sequence[dict[str, object]],
    value_key: str,
    label_key: str,
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
) -> str:
    theme = theme or Theme(width=760, height=560)
    palette = _palette(palette, PALETTES["npg"])
    values = _column(rows, value_key)
    _row_labels(rows, label_key)
    if min(values) < 0:
        raise ValueError("Donut values must be nonnegative; use a signed comparison chart for negative values")
    total = sum(values)
    if total <= 0 or not isfinite(total):
        raise ValueError("Donut values must have a positive finite total")
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    cx, cy = theme.width * 0.38, theme.height * 0.56
    outer, inner = min(theme.width, theme.height) * 0.28, min(theme.width, theme.height) * 0.16
    angle = -pi / 2
    for i, (row, value) in enumerate(zip(rows, values)):
        if value == 0:
            continue
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
        color = palette[i % len(palette)]
        if value == total:
            c.circle(cx, cy, (outer + inner) / 2, "none", color, outer - inner, 0.95)
        else:
            c.path(d, color, "#FFFFFF", 2.2, 0.95)
        mid = angle + delta / 2
        lx, ly = cx + cos(mid) * (outer + 28), cy + sin(mid) * (outer + 28)
        pct = value / total * 100
        if pct >= 7:
            c.text(lx, ly + 4, f"{pct:.0f}%", 12, 780, theme.ink, "middle")
        angle = end
    c.circle(cx, cy, inner * 0.92, theme.bg, "none")
    c.text(cx, cy - 5, _pretty(total, 2), 28, 850, theme.ink, "middle")
    c.text(cx, cy + 20, "total", 11, 650, theme.muted, "middle")
    legend_x, legend_y = theme.width * 0.66, theme.height * 0.30
    for i, row in enumerate(rows):
        y = legend_y + i * 34
        color = palette[i % len(palette)]
        pct = values[i] / total * 100
        c.rect(legend_x, y - 10, 18, 18, color, "none", 5)
        c.text(legend_x + 28, y + 4, str(row[label_key]), 13, 720, theme.ink)
        c.text(theme.width - 46, y + 4, f"{pct:.1f}%", 12, 680, theme.muted, "end")
    return c.render()


def grouped_bar_chart(
    rows: Sequence[dict[str, object]],
    group_key: str,
    series_keys: Sequence[str],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
    unit: str = "",
) -> str:
    theme = theme or Theme(width=940, height=560)
    palette = _palette(palette, PALETTES["ccfa"])
    series_keys = _labels(series_keys, "series_keys", unique=True)
    values = [value for key in series_keys for value in _column(rows, key)]
    _row_labels(rows, group_key)
    lo, hi = min(0.0, min(values)), max(0.0, max(values))
    span = hi - lo or 1.0
    lo, hi = lo - span * 0.12 if lo < 0 else 0, hi + span * 0.16
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, right, top, bottom = 82, theme.width - 42, 132, theme.height - 92
    zero_y = _scale(0, lo, hi, bottom, top)
    fractions = (0, 0.25, 0.5, 0.75, 1.0)
    tick_labels = _tick_labels([lo + (hi - lo) * frac for frac in fractions])
    for frac, tick_label in zip(fractions, tick_labels):
        y = _scale(lo + (hi - lo) * frac, lo, hi, bottom, top)
        c.line(left, y, right, y, theme.grid, 0.9, 0.82)
        c.text(left - 12, y + 4, tick_label, 11, 500, theme.muted, "end")
    if lo < 0:
        c.line(left, zero_y, right, zero_y, theme.muted, 1.2)
        c.text(left - 12, zero_y + 4, "0", 11, 500, theme.muted, "end")
    group_w = (right - left) / max(1, len(rows))
    bar_w = min(26, group_w * 0.68 / max(1, len(series_keys)))
    for i, row in enumerate(rows):
        gx = left + i * group_w + group_w / 2
        c.text(gx, bottom + 28, str(row[group_key]), 12, 720, theme.ink, "middle")
        for j, key in enumerate(series_keys):
            value = float(row[key])
            value_y = _scale(value, lo, hi, bottom, top)
            h = abs(zero_y - value_y)
            x = gx - bar_w * len(series_keys) / 2 + j * bar_w
            color = palette[j % len(palette)]
            c.rect(x + 2, min(zero_y, value_y), max(1, bar_w - 4), h, color, "none", 6, 0.92)
            if value > hi * 0.72:
                c.text(x + bar_w / 2, value_y - 8, f"{_pretty(value)}{unit}", 10, 720, theme.ink, "middle")
    legend_x = left
    legend_y = top - 34
    for j, key in enumerate(series_keys):
        x = legend_x + j * 126
        c.rect(x, legend_y, 18, 12, palette[j % len(palette)], "none", 4)
        c.text(x + 26, legend_y + 11, key, 12, 650, theme.muted)
    return c.render()


def volcano_plot(
    rows: Sequence[dict[str, object]],
    fold_key: str,
    p_key: str,
    label_key: str | None,
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    fold_threshold: float = 1.0,
    p_threshold: float = 0.05,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
    *,
    statistic: str = "p",
    zero_floor: float | None = None,
) -> str:
    """Plot log2 effects against supplied p/adjusted-p/q values, without correction.

    A reported zero needs an explicit display floor smaller than every positive
    value and the threshold. Only zeros use it; the source values are retained.
    """
    theme = theme or Theme(width=900, height=590)
    palette = _palette(palette, ["#477AA6", "#B58B2A", "#BA4C5E", "#8B96A3"], minimum=4)
    statistic_labels = {"p": "p", "adjusted_p": "adjusted p", "q": "q"}
    if statistic not in statistic_labels:
        raise ValueError("statistic must be 'p', 'adjusted_p', or 'q'; supply the corresponding data column")
    fold_threshold = _number(fold_threshold, "fold_threshold")
    p_threshold = _number(p_threshold, "p_threshold")
    if fold_threshold < 0 or not 0 < p_threshold <= 1:
        raise ValueError("fold_threshold must be nonnegative and p_threshold must be in (0, 1]")
    folds, probabilities = _column(rows, fold_key), _column(rows, p_key)
    if label_key is not None:
        _row_labels(rows, label_key)
    if any(p < 0 or p > 1 for p in probabilities):
        raise ValueError(f"{statistic_labels[statistic]} values in {p_key!r} must be in [0, 1]; source values are never clipped")
    zero_count = probabilities.count(0)
    if zero_floor is not None:
        zero_floor = _number(zero_floor, "zero_floor")
        bound = min([p for p in probabilities if p > 0] + [p_threshold])
        if not 0 < zero_floor < bound:
            raise ValueError("zero_floor must be positive and smaller than every positive statistic and p_threshold")
    if zero_count and zero_floor is None:
        raise ValueError("Zero statistics need an explicit zero_floor for log display; choose it from the reporting precision")
    points = []
    for fold, p_value, row in zip(folds, probabilities, rows):
        display_value = zero_floor if p_value == 0 else p_value
        points.append((fold, -log10(display_value), p_value, row))  # type: ignore[arg-type]
    xlo, xhi = _extent([p[0] for p in points] + [-fold_threshold, fold_threshold])
    ylo, yhi = 0.0, max(max([p[1] for p in points] + [-log10(p_threshold)]) * 1.08, 1.0)
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    left, right, top, bottom = 88, theme.width - 44, _plot_top(title, subtitle) + 22, theme.height - (104 if zero_count else 78)
    c.rect(left, top, right - left, bottom - top, "#FFFFFF", "#E2E8F0", 14)
    y_ticks = (0, yhi / 2, yhi)
    for value, tick_label in zip(y_ticks, _tick_labels(y_ticks)):
        y = _scale(value, ylo, yhi, bottom - 16, top + 18)
        c.text(left - 10, y + 4, tick_label, 11, 500, theme.muted, "end")
    x_ticks = (xlo, 0, xhi)
    for value, tick_label in zip(x_ticks, _tick_labels(x_ticks)):
        x = _scale(value, xlo, xhi, left + 18, right - 18)
        c.text(x, bottom + 20, tick_label, 11, 500, theme.muted, "middle")
    for fold in (-fold_threshold, fold_threshold):
        x = _scale(fold, xlo, xhi, left + 18, right - 18)
        c.line(x, top + 14, x, bottom - 14, "#CBD5E1", 1.2, 0.95)
    y_thr = _scale(-log10(p_threshold), ylo, yhi, bottom - 16, top + 18)
    c.line(left + 14, y_thr, right - 14, y_thr, "#CBD5E1", 1.2, 0.95)
    for fold, score, original, row in points:
        x = _scale(fold, xlo, xhi, left + 18, right - 18)
        y = _scale(score, ylo, yhi, bottom - 16, top + 18)
        if fold >= fold_threshold and original <= p_threshold:
            color, r = palette[2], 5.6
        elif fold <= -fold_threshold and original <= p_threshold:
            color, r = palette[0], 5.6
        elif original <= p_threshold:
            color, r = palette[1], 4.8
        else:
            color, r = palette[3], 3.8
        c.parts.append(f'<g data-statistic="{original:.17g}" data-log2-fold="{fold:.17g}">')
        c.circle(x, y, r, color, "#FFFFFF", 0.9, 0.84)
        if original == 0:
            c.line(x - r, y - r - 3, x + r, y - r - 3, color, 1.5)
        c.parts.append("</g>")
    top_hits = sorted(points, key=lambda item: item[1] + abs(item[0]) * 0.35, reverse=True)[:12]
    placed: list[tuple[float, float]] = []
    for fold, score, original, row in top_hits:
        x = _scale(fold, xlo, xhi, left + 18, right - 18)
        y = _scale(score, ylo, yhi, bottom - 16, top + 18)
        if any(abs(x - px) < 62 and abs(y - py) < 22 for px, py in placed):
            continue
        if label_key is None:
            break
        label = str(row[label_key])
        dx = 10 if x < (left + right) / 2 else -10
        anchor = "start" if dx > 0 else "end"
        c.text(x + dx, y - 8, label, 11, 760, theme.ink, anchor)
        placed.append((x, y))
        if len(placed) >= 5:
            break
    c.text((left + right) / 2, bottom + 42, "log2 fold change", 12, 760, theme.muted, "middle")
    stat_label = statistic_labels[statistic]
    c.text(left, top - 16, f"-log10 {stat_label}", 12, 760, theme.muted)
    c.text(right, top - 16, f"{stat_label} <= {p_threshold:g}; |log2 FC| >= {fold_threshold:g}", 11, 500, theme.muted, "end")
    if zero_count:
        c.text(left, bottom + 64, f"{zero_count} zero {stat_label} value(s) shown at {zero_floor:g} (capped marker); positive values unchanged", 11, 500, theme.muted)
    return c.render()


def correlation_heatmap(
    matrix: Sequence[Sequence[float]],
    labels: Sequence[str],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
    *,
    show_values: bool = True,
) -> str:
    theme = theme or Theme(width=760, height=700)
    palette = _palette(palette, PALETTES["diverging_cork"], minimum=2)
    matrix = _matrix(matrix, labels, labels)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if not -1 <= value <= 1:
                raise ValueError(f"Correlation matrix[{i}][{j}]={value:g} must be in [-1, 1]; check the supplied coefficients")
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    n = len(labels)
    left, top = 148, _plot_top(title, subtitle) + 22
    cell = min((theme.width - left - 70) / n, (theme.height - top - 116) / n)
    minimum_cell = max(18, theme.min_font_pt * theme.width / (72 * theme.paper_width_in) + 10) if theme.paper_width_in else 18
    if cell < minimum_cell:
        raise ValueError("Correlation cells are too small; increase Theme width/height or split the matrix")
    for i, label in enumerate(labels):
        c.text(left - 18, top + i * cell + cell / 2 + 5, label, 12, 700, theme.ink, "end")
        c.text(left + i * cell + cell / 2, top - 18, label, 12, 700, theme.ink, "middle")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            v = value
            idx = round(_scale(v, -1, 1, 0, len(palette) - 1))
            color = palette[max(0, min(len(palette) - 1, int(idx)))]
            x, y = left + j * cell, top + i * cell
            c.rect(x + 2, y + 2, cell - 4, cell - 4, color, "#FFFFFF", 8, 0.95)
            if show_values:
                c.text(x + cell / 2, y + cell / 2 + 4, f"{v:.2f}", 10, 760, _contrast(color), "middle")
    _colorbar(c, ColorNorm(-1, 1, 0), palette, left, top + n * cell + 36, min(260, n * cell), "correlation")
    return c.render()


def _density(values: Sequence[float], xs: Sequence[float]) -> list[float]:
    vals = _numbers(values, "density samples")
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
    palette = _palette(palette, PALETTES["ccfa"])
    _labels(list(series), "series labels", unique=True)
    series = {label: _numbers(vals, f"series[{label!r}]") for label, vals in series.items()}
    all_values = [v for vals in series.values() for v in vals]
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
    fractions = (0, 0.25, 0.5, 0.75, 1)
    tick_labels = _tick_labels([lo + (hi - lo) * frac for frac in fractions])
    for frac, tick_label in zip(fractions, tick_labels):
        x = left + (right - left) * frac
        c.text(x, bottom + 30, tick_label, 11, 500, theme.muted, "middle")
    return c.render()


def small_multiple_lines(
    panels: Sequence[dict[str, object]],
    title: str,
    subtitle: str | None = None,
    note: str | None = None,
    palette: Sequence[str] | None = None,
    theme: Theme | None = None,
    *,
    share_x: bool = True,
    share_y: bool = True,
    entity_colors: Mapping[str, str] | None = None,
    show_legend: bool = True,
) -> str:
    """Compare panels on shared scales; explicitly free axes for different units.

    Panels accept x, y, title, and optional entity, x_unit, y_unit. Reuse the
    entity_colors mapping in separate calls to keep entity colors consistent.
    """
    theme = theme or Theme(width=960, height=620)
    palette = _palette(palette, PALETTES["ccfa"])
    if not panels:
        raise ValueError("panels must contain at least one panel")
    if not isinstance(share_x, bool) or not isinstance(share_y, bool):
        raise ValueError("share_x and share_y must be booleans")
    values = []
    for i, panel in enumerate(panels):
        if any(key not in panel for key in ("x", "y", "title")):
            raise ValueError(f"panels[{i}] needs x, y, and title")
        xs = _numbers(panel["x"], f"panels[{i}].x")  # type: ignore[arg-type]
        ys = _numbers(panel["y"], f"panels[{i}].y")  # type: ignore[arg-type]
        if len(xs) != len(ys):
            raise ValueError(f"panels[{i}] has {len(xs)} x values and {len(ys)} y values; provide paired observations")
        _labels([panel.get("entity", panel["title"])], f"panels[{i}] entity or title")
        values.append((xs, ys))
    for axis, shared in (("x", share_x), ("y", share_y)):
        units = {str(panel[f"{axis}_unit"]) for panel in panels if panel.get(f"{axis}_unit") is not None}
        if shared and len(units) > 1:
            raise ValueError(f"Panels have different {axis} units; convert them explicitly or use share_{axis}=False")
    shared_x = _extent(x for xs, _ in values for x in xs)
    shared_y = _extent(y for _, ys in values for y in ys)
    colors = dict(entity_colors or {})
    entities = list(dict.fromkeys(str(panel.get("entity", panel["title"])) for panel in panels))
    if entity_colors is not None:
        missing = [entity for entity in entities if entity not in colors]
        if missing:
            raise ValueError(f"entity_colors is missing entities: {', '.join(missing)}")
        _palette([colors[entity] for entity in entities], [])
    else:
        colors = {entity: palette[i % len(palette)] for i, entity in enumerate(entities)}
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    cols = min(len(panels), 2 if len(panels) <= 4 else 3)
    rows = (len(panels) + cols - 1) // cols
    gap = 24
    font_size = max(12, theme.min_font_pt * theme.width / (72 * theme.paper_width_in)) if theme.paper_width_in else 12
    left, top = 30, max(_plot_top(title, subtitle), font_size + 16)
    scale_label = f"x: {'shared' if share_x else 'free'}; y: {'shared' if share_y else 'free'}"
    c.text(theme.width - left, top - 12, scale_label, 11, 500, theme.muted, "end")
    if show_legend and any("entity" in panel for panel in panels):
        legend_x, legend_y = left, top - 12
        right = theme.width - left - max(230, font_size * 16)
        for entity in entities:
            item_width = len(entity) * font_size * 0.65 + 40
            if item_width > right - left:
                raise ValueError("Entity legend is too wide; use shorter display IDs or show_legend=False with a shared external legend")
            if legend_x + item_width > right:
                legend_x = left
                legend_y += font_size + 12
            c.line(legend_x, legend_y - 4, legend_x + 18, legend_y - 4, colors[entity], 2.8)
            c.text(legend_x + 25, legend_y, entity, 12, 500, theme.muted)
            legend_x += item_width
        top = legend_y + 12
    plot_w = (theme.width - left * 2 - gap * (cols - 1)) / cols
    plot_h = (theme.height - top - 50 - gap * (rows - 1)) / rows
    if plot_w < 180 or plot_h < 135:
        raise ValueError("Panels are too small; increase Theme width/height or split the figure")
    # Reserve the same header space across the composition, including unnamed
    # panels, so a shared numerical scale also has a shared physical scale.
    head_gap = 48 if any(panel["title"] or panel.get("y_unit") for panel in panels) else 22
    y_ranges = [shared_y if share_y else _extent(ys) for _, ys in values]
    y_labels = [_tick_labels([lo, lo + (hi - lo) / 2, hi]) for lo, hi in y_ranges]
    tick_font = max(10, theme.min_font_pt * theme.width / (72 * theme.paper_width_in)) if theme.paper_width_in else 10
    left_inset = max(58, max(len(label) for labels in y_labels for label in labels) * tick_font * 0.62 + 14)
    if plot_w - left_inset - 18 < 80:
        raise ValueError("Tick labels leave too little plotting width; increase Theme width or use explicitly rescaled units")
    for idx, panel in enumerate(panels):
        px = left + (idx % cols) * (plot_w + gap)
        py = top + (idx // cols) * (plot_h + gap)
        xs, ys = values[idx]
        xlo, xhi = shared_x if share_x else _extent(xs)
        ylo, yhi = y_ranges[idx]
        entity = str(panel.get("entity", panel["title"]))
        color = colors[entity]
        c.parts.append(f'<g data-panel="{idx}" data-entity="{escape(entity, quote=True)}" data-x-min="{xlo:.17g}" data-x-max="{xhi:.17g}" data-y-min="{ylo:.17g}" data-y-max="{yhi:.17g}">')
        c.rect(px, py, plot_w, plot_h, "#FFFFFF", "#E6ECF2", 14)
        if panel["title"]:
            c.text(px + 14, py + 24, str(panel["title"]), 13, 760, theme.ink)
        x1, x2, y1, y2 = px + left_inset, px + plot_w - 18, py + head_gap, py + plot_h - 42
        fractions = (0, 0.5, 1)
        tick_labels = y_labels[idx]
        for frac, tick_label in zip(fractions, tick_labels):
            y = _scale(frac, 0, 1, y2, y1)
            c.line(x1, y, x2, y, theme.grid, 0.7, 0.8)
            c.text(x1 - 7, y + 4, tick_label, 10, 500, theme.muted, "end")
        x_labels = _tick_labels([xlo, xhi])
        c.text(x1, y2 + 20, x_labels[0], 10, 500, theme.muted)
        c.text(x2, y2 + 20, x_labels[1], 10, 500, theme.muted, "end")
        if panel.get("y_unit"):
            c.text(px + plot_w - 14, py + 24, str(panel["y_unit"]), 11, 500, theme.muted, "end")
        if panel.get("x_unit"):
            c.text((x1 + x2) / 2, y2 + 20, str(panel["x_unit"]), 10, 500, theme.muted, "middle")
        points = [(_scale(x, xlo, xhi, x1, x2), _scale(y, ylo, yhi, y2, y1)) for x, y in zip(xs, ys)]
        c.polyline(points, color, 2.8)
        for x, y in points:
            c.circle(x, y, 3.5, color, "#FFFFFF", 1)
        c.parts.append("</g>")
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
    palette = _palette(palette, PALETTES["ccfa"])
    max_value = _number(max_value, "max_value")
    if max_value <= 0:
        raise ValueError("max_value must be positive")
    values = _column(scores, value_key)
    _row_labels(scores, label_key)
    if len(scores) < 3:
        raise ValueError("A radial scorecard needs at least three criteria; use a bar chart for fewer")
    if any(value < 0 or value > max_value for value in values):
        raise ValueError(f"Radial values must be in [0, {max_value:g}]; change max_value or use another chart, never clip scores")
    c = Canvas(theme.width, theme.height, theme)
    c.label_block(title, subtitle, note)
    cx, cy = theme.width / 2, theme.height / 2 + 32
    radius = min(theme.width, theme.height) * 0.31
    n = len(scores)
    rings = [0.25, 0.5, 0.75, 1.0]
    for r in rings:
        c.circle(cx, cy, radius * r, "none", theme.grid, 1)
        c.text(cx + 5, cy - radius * r + 4, _pretty(max_value * r, 2), 10, 500, theme.muted)
    points = []
    for i, score in enumerate(scores):
        angle = -pi / 2 + tau * i / n
        value = values[i] / max_value
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
        "donut_chart": "Composition and proportion summary with explicit labels; use sparingly for exact comparisons.",
        "grouped_bar_chart": "Grouped categorical comparisons; good for baselines, ablations, and cohorts.",
        "volcano_plot": "Effect-size versus significance screening; good for biomarker, feature, and ablation scans.",
        "correlation_heatmap": "Relationship matrix; good for metrics, modules, datasets, or feature correlations.",
        "ridgeline_density": "Distribution comparison; good for seeds, runs, samples, or uncertainty.",
        "small_multiple_lines": "Repeated trends on shared axes, with explicit free scales and stable entity colors.",
        "radial_scorecard": "Compact multi-criterion profile; use carefully and always label scale.",
    }
