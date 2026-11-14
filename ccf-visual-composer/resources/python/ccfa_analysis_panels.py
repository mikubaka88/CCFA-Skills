"""Composable Matplotlib panels for scientific figures.

NumPy and Matplotlib are optional dependencies of this module; the existing
standard-library SVG recipes remain independent. These functions plot supplied
values. They do not generate research data, infer significance, or choose an
experimental protocol. Caller-owned axes make layouts and later edits explicit.
"""
from __future__ import annotations

from contextlib import contextmanager
import colorsys
import json
import math
import os
from pathlib import Path
import tempfile
import warnings
from collections.abc import Mapping

import matplotlib as mpl
from matplotlib import colors as mcolors, font_manager
from matplotlib.markers import MarkerStyle
from matplotlib.text import Text
import matplotlib.pyplot as plt
import numpy as np

from ccfa_plot_recipes import PALETTES

INK = "#24313A"
EDGE_WIDTH = 1.15
GRID = "#E6E9EB"
MARKERS = ("o", "s", "^", "D", "v", "P", "X", "h")


def paired_edge(color):
    """An opaque darker shade of the same hue; independent of fill alpha.

    Neutral fills keep neutral borders. Saturated categories keep their own
    color identity instead of receiving the same near-black outline.
    """
    red, green, blue, _ = mcolors.to_rgba(color)
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    shade = min(.38, lightness * .66)
    return (*colorsys.hls_to_rgb(hue, shade, saturation), 1.0)


def _vector(values, name, *, finite=True):
    try:
        result = np.asarray(values, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain numeric values") from exc
    if result.ndim != 1 or not result.size:
        raise ValueError(f"{name} must be a nonempty one-dimensional array")
    if finite and not np.isfinite(result).all():
        raise ValueError(f"{name} must contain finite values")
    return result


def _positive(value, name):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def _labels(values, n=None, name="labels"):
    result = [str(v) for v in values]
    if not result or any(not v.strip() for v in result):
        raise ValueError(f"{name} must contain nonempty labels")
    if len(set(result)) != len(result):
        raise ValueError(f"{name} must be unique; align data by stable IDs first")
    if n is not None and len(result) != n:
        raise ValueError(f"{name} length does not match data")
    return result


def _same_length(*arrays):
    if len({len(a) for a in arrays}) != 1:
        raise ValueError("Data arrays must have the same length")


def _bounds(values, lower, upper):
    if (lower is None) != (upper is None):
        raise ValueError("Supply both lower and upper interval bounds")
    if lower is None:
        return None, None
    low, high = _vector(lower, "lower"), _vector(upper, "upper")
    _same_length(values, low, high)
    if np.any(low > values) or np.any(high < values):
        raise ValueError("Interval bounds must enclose each supplied estimate")
    return low, high


def _colors(labels, colors=None):
    if colors is None:
        colors = [PALETTES["npg"][i % len(PALETTES["npg"])] for i in range(len(labels))]
    elif isinstance(colors, Mapping):
        if any(label not in colors for label in labels):
            raise ValueError("Every entity needs an explicit color mapping")
        colors = [colors[label] for label in labels]
    else:
        colors = list(colors)
    if len(colors) != len(labels) or not all(mcolors.is_color_like(c) for c in colors):
        raise ValueError("colors must contain one valid color per entity")
    return colors


def entity_encoding(ids, palette="npg", colors=None):
    """Build once in canonical ID order, then reuse across all related panels."""
    ids = _labels(ids, name="entity IDs")
    if palette not in PALETTES:
        raise ValueError(f"Unknown palette {palette!r}; available: {', '.join(PALETTES)}")
    if colors is None:
        colors = [PALETTES[palette][i % len(PALETTES[palette])] for i in range(len(ids))]
    colors = _colors(ids, colors)
    return {label: {"color": color, "marker": MARKERS[i % len(MARKERS)]}
            for i, (label, color) in enumerate(zip(ids, colors))}


def _font_families(font):
    available = {item.name for item in font_manager.fontManager.ttflist}
    presets = {
        "serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"],
        "sans": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
        "comic": ["Comic Sans MS", "DejaVu Sans"],
    }
    requested = presets.get(font, [font, "DejaVu Sans"])
    latin = next((family for family in requested if family in available), "DejaVu Sans")
    cjk = [name for name in ("Microsoft YaHei", "SimSun", "PingFang SC", "PingFang TC",
                             "Songti SC", "Songti TC", "Noto Sans CJK SC", "Noto Sans CJK TC",
                             "Noto Serif CJK SC", "Noto Serif CJK TC", "Noto Sans CJK JP", "Noto Serif CJK JP",
                             "Noto Sans CJK KR", "Noto Serif CJK KR", "Source Han Sans SC",
                             "Source Han Sans TC", "Source Han Serif SC", "Source Han Serif TC", "Arial Unicode MS")
           if name in available]
    return list(dict.fromkeys([latin, *cjk[:1], "DejaVu Sans"]))


@contextmanager
def paper_style(font="serif", font_size=8.5):
    """Physical point sizes, available CJK fallback, and no global rc mutation."""
    size = _positive(font_size, "font_size")
    if size <= 0.5:
        raise ValueError("font_size must exceed 0.5 points")
    settings = {
        "font.family": _font_families(font), "font.size": size,
        "axes.labelweight": "bold", "axes.titleweight": "bold",
        "axes.labelsize": size, "axes.titlesize": size + 0.5,
        "xtick.labelsize": size - 0.5, "ytick.labelsize": size - 0.5,
        "legend.fontsize": size - 0.5, "axes.labelcolor": INK,
        "text.color": INK, "xtick.color": INK, "ytick.color": INK,
        "axes.edgecolor": INK, "axes.linewidth": 0.85,
        "xtick.major.width": 0.8, "ytick.major.width": 0.8,
        "xtick.major.size": 3, "ytick.major.size": 3,
        "lines.linewidth": 1.3, "lines.markersize": 3.5,
        "figure.facecolor": "white", "axes.facecolor": "white",
        "savefig.facecolor": "white", "svg.fonttype": "none",
        "pdf.fonttype": 42, "ps.fonttype": 42, "mathtext.fontset": "stix", "mathtext.default": "bf",
        "axes.unicode_minus": True, "legend.frameon": False,
        "axes.labelpad": 3, "axes.titlepad": 5,
        "xtick.major.pad": 2.5, "ytick.major.pad": 2.5,
        "legend.borderaxespad": .3, "legend.labelspacing": .25,
        "legend.handletextpad": .4, "legend.columnspacing": .9,
        "boxplot.boxprops.color": INK, "boxplot.boxprops.linewidth": EDGE_WIDTH,
        "boxplot.whiskerprops.color": INK, "boxplot.whiskerprops.linewidth": EDGE_WIDTH,
        "boxplot.capprops.color": INK, "boxplot.capprops.linewidth": EDGE_WIDTH,
    }
    with mpl.rc_context(settings):
        yield


def new_figure(width_mm=180, height_mm=120, **kwargs):
    """No layout engine is imposed; the caller can use GridSpec or constrained layout."""
    return plt.figure(figsize=(_positive(width_mm, "width_mm") / 25.4,
                               _positive(height_mm, "height_mm") / 25.4), **kwargs)


def _figure_axes(fig):
    axes = list(fig.axes)
    for parent in axes:
        axes.extend(child for child in parent.child_axes if child not in axes)
    return axes


def finish_paper_style(fig):
    """Apply final typography, including legends created after the style context.

    Do not alter values, bounds, coordinate scales, aspect ratios or artist geometry.
    BarContainer patches are observations; arbitrary region/heatmap patches are not.
    """
    from matplotlib.container import BarContainer
    for ax in _figure_axes(fig):
        labels = [ax.title, ax._left_title, ax._right_title, ax.xaxis.label, ax.yaxis.label,
                  ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text(),
                  *ax.get_xticklabels(which="both"), *ax.get_yticklabels(which="both")]
        for text in labels:
            text.set_fontweight("bold")
        for container in ax.containers:
            if isinstance(container, BarContainer):
                for bar in container.patches:
                    face = bar.get_facecolor()
                    # A fully transparent face has no color identity; retain
                    # its original explicit edge as the categorical base.
                    base = face if face[3] > 0 else getattr(bar, "_ccfa_edge_base", bar.get_edgecolor())
                    bar._ccfa_edge_base = base
                    bar.set_alpha(None)
                    bar.set_facecolor(face)  # Keep fill transparency; outline stays opaque.
                    bar.set_edgecolor(paired_edge(base))
                    bar.set_linewidth(max(EDGE_WIDTH, bar.get_linewidth()))
        legend = ax.get_legend()
        if legend is not None:
            for text in [legend.get_title(), *legend.get_texts()]:
                text.set_fontweight("bold")
    for legend in fig.legends:
        for text in [legend.get_title(), *legend.get_texts()]:
            text.set_fontweight("bold")
    return fig


def clean_axes(ax, grid="y"):
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    if grid in ("x", "y", "both"):
        ax.grid(True, axis=grid, color=GRID, linewidth=0.55)
    elif grid is not None:
        raise ValueError("grid must be x, y, both, or None")
    ax.xaxis.label.set_weight("bold"); ax.yaxis.label.set_weight("bold")
    for text in [*ax.get_xticklabels(which="both"), *ax.get_yticklabels(which="both")]:
        text.set_weight("bold")
    return ax


def compact_legend(ax, handles=None, labels=None, **kwargs):
    """Pack a compact header key from bold text metrics; honor explicit placement."""
    from matplotlib.font_manager import FontProperties
    if handles is None:
        handles,found=ax.get_legend_handles_labels()
        if labels is None:labels=found
    if labels is None:labels=[artist.get_label() for artist in handles]
    kwargs.setdefault("frameon",False)
    kwargs.setdefault("fontsize",max(7,float(mpl.rcParams["font.size"])-1))
    # A best-position key can still straddle several curves. Reserve a shallow
    # header by default; constrained layout includes it in the final paper slot.
    if "loc" not in kwargs and "bbox_to_anchor" not in kwargs:
        kwargs.update(loc="lower left",bbox_to_anchor=(0,1.01),borderaxespad=0)
    if handles and "ncol" not in kwargs and "ncols" not in kwargs:
        size=kwargs["fontsize"]
        prop=FontProperties(family=mpl.rcParams["font.family"],size=size,weight="bold")
        renderer=ax.figure.canvas.get_renderer()
        widths=[max(renderer.get_text_width_height_descent(line,prop,line.count("$")>=2 and line.count("$")%2==0)[0]
                    for line in label.split("\n")) for label in labels]
        unit=prop.get_size_in_points()*ax.figure.dpi/72
        available=ax.bbox.width*.94
        for columns in range(min(3,len(handles)),0,-1):
            groups=np.array_split(np.asarray(widths),columns)
            needed=sum(max(group)+2.4*unit for group in groups)+(columns-1)*unit
            if needed<=available or columns==1:
                kwargs["ncol"]=columns;break
        kwargs.setdefault("columnspacing",.8)
        kwargs.setdefault("handletextpad",.35)
    return ax.legend(handles=handles,labels=labels,**kwargs)


def panel_label(ax, letter, title="", *, label_x=-0.14):
    """Letter and title are independent live text objects."""
    label = ax.text(label_x, 1.035, str(letter), transform=ax.transAxes,
                    ha="left", va="bottom", weight="bold", fontsize=10.5,
                    clip_on=False, gid=f"panel-{letter}")
    if title:
        ax.set_title(title, loc="left", pad=5, weight="bold")
    return label


def comparison_intervals(ax, labels, values, *, lower=None, upper=None, runs=None,
                         colors=None, xlabel="", seed=0):
    """Horizontal estimates and supplied intervals, optionally showing raw runs.

    No uncertainty is inferred. The caller identifies SD/SE/CI in the caption.
    """
    values = _vector(values, "values")
    labels = _labels(labels, len(values)); colors = _colors(labels, colors)
    low, high = _bounds(values, lower, upper)
    if runs is not None:
        if len(runs) != len(values):
            raise ValueError("runs must contain one sample array per label")
        runs = [_vector(run, "runs") for run in runs]
    rng = np.random.default_rng(seed)
    points = []; intervals = []
    for i, (value, color) in enumerate(zip(values, colors)):
        if runs is not None:
            ax.scatter(runs[i], i + rng.uniform(-0.13, 0.13, len(runs[i])),
                       s=10, color=color, alpha=0.4, linewidths=0, zorder=2)
        if low is not None:
            intervals.append(ax.plot([low[i], high[i]], [i, i], color=color,
                                      linewidth=2.0, solid_capstyle="round", zorder=3)[0])
        points.append(ax.scatter([value], [i], s=28, color=color,
                                 edgecolors="white", linewidths=0.6, zorder=4))
    ax.set_yticks(np.arange(len(labels)), labels); ax.set_ylim(len(labels) - 0.6, -0.6)
    ax.set_xlabel(xlabel); clean_axes(ax, "x")
    return {"points": points, "intervals": intervals}


def line_band(ax, x, y, *, lower=None, upper=None, label=None, color=None,
              marker=None, xlabel="", ylabel="", fill_to=None):
    x, y = _vector(x, "x"), _vector(y, "y"); _same_length(x, y)
    if np.any(np.diff(x) <= 0):
        raise ValueError("x must be strictly increasing; align and order the input first")
    low, high = _bounds(y, lower, upper)
    line, = ax.plot(x, y, label=label, color=color, marker=marker, zorder=3)
    if low is not None:
        ax.fill_between(x, low, high, color=line.get_color(), alpha=0.15,
                        linewidth=0, zorder=2)
    if fill_to is not None:
        baseline=float(fill_to)
        if not math.isfinite(baseline):raise ValueError("Fill baseline must be finite")
        ax.fill_between(x,baseline,y,color=line.get_color(),alpha=.12,linewidth=0,zorder=1)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); clean_axes(ax)
    return line


def density_map(ax, x, y, *, gridsize=28, xscale="linear", yscale="linear",
                cmap="viridis", xlabel="", ylabel="", counts=None, corridor=None,
                xlim=None, ylim=None):
    """Hexagonal counts of supplied observations; color uses a logarithmic scale.

    Empty bins are omitted. Axis transforms do not change the input coordinates
    or discard observations. The returned mappable can label a count colorbar.
    """
    x, y = _vector(x, "x"), _vector(y, "y"); _same_length(x, y)
    if not isinstance(gridsize, (int, np.integer)) or isinstance(gridsize, (bool, np.bool_)) or gridsize < 2:
        raise ValueError("gridsize must be an integer of at least two")
    for values, scale, name in ((x, xscale, "x"), (y, yscale, "y")):
        if scale not in ("linear", "log"):
            raise ValueError(f"{name}scale must be linear or log")
        if scale == "log" and np.any(values <= 0):
            raise ValueError(f"Log {name} axis requires strictly positive observations")
    original_x,original_y=x,y
    extra={};original_counts=None
    if counts is not None:
        counts=_vector(counts,"counts");_same_length(x,counts)
        if np.any(counts<0) or not np.equal(counts,np.floor(counts)).all() or not np.isfinite(counts.sum()) or not np.any(counts>0):
            raise ValueError("Aggregate counts must be nonnegative integers with positive total")
        original_counts=counts
        keep=counts>0;x,y,counts=x[keep],y[keep],counts[keep]
        extra={"C":counts,"reduce_C_function":np.sum}
    artist = ax.hexbin(x, y, gridsize=int(gridsize), mincnt=1, cmap=cmap,
                      norm=mcolors.LogNorm(), xscale=xscale, yscale=yscale,
                      linewidths=0, rasterized=False,**extra)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); clean_axes(ax, None)
    for axis,limits,observed,scale in (("x",xlim,x,xscale),("y",ylim,y,yscale)):
        if limits is not None:
            bounds=_vector(limits,axis+" limits")
            if len(bounds)!=2 or bounds[0]>=bounds[1] or (scale=="log" and bounds[0]<=0):
                raise ValueError("Density display limits need an increasing valid domain")
            if np.min(observed)<bounds[0] or np.max(observed)>bounds[1]:
                raise ValueError("Density limits cannot hide supplied observations")
            getattr(ax,"set_"+axis+"lim")(bounds)
    if corridor is not None:
        if not isinstance(corridor,dict):raise ValueError("Corridor requires named thresholds and optional weights")
        import ccfa_analysis_templates as templates
        block={"x":original_x,"y":original_y,"corridor":corridor}
        if original_counts is not None:block["counts"]=original_counts
        artist.ccfa_corridor=templates._density_corridor(ax,block)
    return artist


def binned_summary(ax, samples, labels, *, color=None, quantile=.95,
                   line_color="#D85E32", ylabel="", summary=None,
                   summary_mode="iqr", annotate=False, value_format=".3f", quantile_label=None):
    """Observed IQR boxes, or explicit median–P90 boxes with P99 whiskers.

    The default retains median/IQR, 1.5-IQR whiskers and visible outliers.
    median_p90 uses sample-derived quantiles, or a supplied summary with no raw
    samples, and marks P95 as diamonds. These are quantiles, not confidence
    intervals. Numeric annotations are optional and use only supplied values.
    """
    labels = _labels(labels)
    if summary_mode not in ("iqr", "median_p90"):
        raise ValueError("summary_mode must be iqr or median_p90")
    if summary is not None:
        if samples is not None:
            raise ValueError("Supply raw samples or explicit quantile summary, not both")
        if not isinstance(summary, Mapping) or not {"median", "p90", "p95", "p99"} <= set(summary):
            raise ValueError("Quantile summary requires median, p90, p95 and p99")
        summaries = {key: _vector(summary[key], key) for key in ("median", "p90", "p95", "p99")}
        if any(len(values) != len(labels) for values in summaries.values()):
            raise ValueError("Quantile summary lengths must match labels")
        if np.any(np.diff(np.vstack(list(summaries.values())), axis=0) < 0):
            raise ValueError("Quantiles must satisfy median <= P90 <= P95 <= P99")
        summary_mode = "median_p90"
        groups = None
    else:
        if samples is None or len(samples) != len(labels):
            raise ValueError("Supply one observed sample group per label")
        groups = [_vector(group, "sample group") for group in samples]
        summaries = {key: np.array([np.quantile(group, q, method="linear") for group in groups])
                     for key, q in (("median", .5), ("p90", .9), ("p95", .95), ("p99", .99))}
    quantile = float(quantile)
    if not math.isfinite(quantile) or not 0 <= quantile <= 1:
        raise ValueError("quantile must lie in [0, 1]")
    color = "#619ACA" if color is None else color
    if not mcolors.is_color_like(color) or not mcolors.is_color_like(line_color):
        raise ValueError("Box and quantile colors must be valid colors")
    positions = np.arange(len(labels))
    if summary_mode == "median_p90" and not math.isclose(quantile, .95):
        raise ValueError("The median–P90/P99 summary uses P95 diamonds; quantile must be .95")
    quantiles = summaries["p95"] if summary_mode == "median_p90" else np.array([np.quantile(group, quantile, method="linear") for group in groups])
    medians = summaries["median"]
    styling = dict(positions=positions, widths=.42,
                       patch_artist=True, showfliers=True, manage_ticks=False,
                       boxprops={"facecolor": mcolors.to_rgba(color, .35), "edgecolor": paired_edge(color), "linewidth": EDGE_WIDTH},
                       medianprops={"color": paired_edge(color), "linewidth": 1.4},
                       whiskerprops={"color": paired_edge(color), "linewidth": EDGE_WIDTH},
                       capprops={"color": paired_edge(color), "linewidth": EDGE_WIDTH},
                       flierprops={"marker": ".", "markersize": 3, "markerfacecolor": color,
                                   "markeredgecolor": "none", "alpha": .6})
    if summary_mode == "median_p90":
        statistics = [{"med": summaries["median"][i], "q1": summaries["median"][i],
                       "q3": summaries["p90"][i], "whislo": summaries["median"][i],
                       "whishi": summaries["p99"][i], "fliers": []} for i in positions]
        boxes = ax.bxp(statistics, **styling)
    else:
        boxes = ax.boxplot(groups, whis=1.5, **styling)
    percent = quantile * 100
    suffix = "th"
    if percent.is_integer() and not 10 <= int(percent) % 100 <= 20:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(int(percent) % 10, "th")
    line, = ax.plot(positions, quantiles, color=line_color, marker="D" if summary_mode == "median_p90" else "o", markersize=3.5,
                    linewidth=1.3, label=f"{percent:g}{suffix} percentile", zorder=4)
    boxes["boxes"][0].set_label("Median–P90 range" if summary_mode == "median_p90" else "Median / IQR")
    if summary_mode == "median_p90":
        from matplotlib.lines import Line2D
        whisker = Line2D([], [], color=paired_edge(color), marker="_", markersize=7, linewidth=EDGE_WIDTH, label="P99 whisker")
        compact_legend(ax,handles=[boxes["boxes"][0], whisker, line],
                  labels=["Median–P90 range", "P99 whisker", quantile_label or "P95 value"], frameon=False,
                  loc="upper left", handlelength=1.35, handletextpad=.45, labelspacing=.3)
    else:
        compact_legend(ax,handles=[boxes["boxes"][0], line], frameon=False)
    annotations = []
    if annotate:
        indices = list(range(len(labels))) if annotate is True else list(annotate)
        if any(isinstance(i, bool) or not isinstance(i, (int, np.integer)) or not 0 <= i < len(labels) for i in indices):
            raise ValueError("Annotation indices must identify supplied groups")
        for i in indices:
            annotations.append(ax.annotate(format(float(quantiles[i]), value_format), (i, quantiles[i]),
                                          xytext=(0, 8), textcoords="offset points", ha="center", va="bottom",
                                          color=line_color, fontsize=mpl.rcParams["font.size"]-.7, fontweight="bold"))
        ax.margins(y=.18)
    ax.set_xticks(positions, labels); ax.set_xlim(-.6, len(labels) - .4)
    ax.set_ylabel(ylabel); clean_axes(ax)
    return {"boxes": boxes, "quantiles": quantiles, "quantile_line": line, "medians": medians,
            "summary_mode": summary_mode, "summary": summaries, "annotations": annotations}


def category_comparison(ax, labels, bars, series, *, bar_label="Occupancy",
                        bar_color="#619ACA", ylabel="Share (%)", bar_style="filled",
                        bar_labels=False, value_format=".1f", legend=True, legend_options=None,
                        label_wrap=None, tick_font_size=None):
    """Same-unit bars and line series on one axis, without normalization.

    The caller supplies a common unit through ylabel and converts quantities
    before calling. Values are never clipped to an assumed percentage range.
    """
    labels = _labels(labels); bars = _vector(bars, "bars")
    if len(labels) != len(bars):
        raise ValueError("Bars and category labels must have the same length")
    if not mcolors.is_color_like(bar_color):
        raise ValueError("bar_color must be a valid color")
    if bar_style not in ("filled", "outlined"):
        raise ValueError("bar_style must be filled or outlined")
    if not series:
        raise ValueError("Supply at least one line series")
    names = [str(bar_label)]; checked = []
    for i, block in enumerate(series):
        if not isinstance(block, Mapping) or "label" not in block or "values" not in block:
            raise ValueError("Each series needs a label and observed values")
        values = _vector(block["values"], "series values"); _same_length(bars, values)
        name = str(block["label"]); names.append(name)
        color = block.get("color", PALETTES["npg"][i % len(PALETTES["npg"])])
        marker = block.get("marker", MARKERS[i % len(MARKERS)])
        if not mcolors.is_color_like(color):
            raise ValueError("Each series needs a valid color")
        MarkerStyle(marker)  # Validate before creating any bars or lines.
        low, high = _bounds(values, block.get("lower"), block.get("upper"))
        alpha = float(block.get("band_alpha", .12))
        if not math.isfinite(alpha) or not 0 <= alpha <= 1:
            raise ValueError("band_alpha must be between zero and one")
        checked.append((name, values, color, marker, low, high, alpha, block))
    _labels(names, name="legend labels")
    positions = np.arange(len(labels))
    bar_artists = ax.bar(positions, bars, width=.6, label=str(bar_label),
                         color=mcolors.to_rgba(bar_color, .10 if bar_style == "outlined" else .55),
                         alpha=None,
                         edgecolor=paired_edge(bar_color), linewidth=EDGE_WIDTH, zorder=2)
    lines, bands, annotations = [], [], []
    if bar_labels:
        for position, value in zip(positions, bars):
            annotations.append(ax.annotate(format(float(value), value_format), (position, value),
                              xytext=(0, 2.5), textcoords="offset points", ha="center", va="bottom",
                              color=bar_color, fontsize=mpl.rcParams["font.size"]-1.1, fontweight="bold"))
    for name, values, color, marker, low, high, alpha, block in checked:
        if low is not None:
            bands.append(ax.fill_between(positions, low, high, color=color, alpha=alpha, linewidth=0, zorder=1))
        line = ax.plot(positions, values, label=name, color=color, marker=marker,
                       linestyle=block.get("linestyle", "-"), linewidth=1.3, markersize=3.5, zorder=3)[0]
        lines.append(line)
        chosen = block.get("annotate", [])
        indices = list(range(len(labels))) if chosen is True else list(chosen or [])
        if any(isinstance(i, bool) or not isinstance(i, (int, np.integer)) or not 0 <= i < len(labels) for i in indices):
            raise ValueError("Series annotation indices must identify supplied categories")
        for i in indices:
            annotations.append(ax.annotate(format(float(values[i]), block.get("value_format", value_format)),
                              (i, values[i]), xytext=(0, float(block.get("annotation_offset", 5))),
                              textcoords="offset points", ha="center", va="bottom", color=color,
                              fontsize=mpl.rcParams["font.size"]-.7, fontweight="bold"))
    display_labels = labels
    if label_wrap is not None:
        if isinstance(label_wrap, bool) or not isinstance(label_wrap, int) or label_wrap < 2:
            raise ValueError("label_wrap must be an integer of at least two characters")
        import textwrap
        display_labels = ["\n".join(textwrap.fill(line, width=label_wrap, break_on_hyphens=False)
                                   for line in label.split("\n")) for label in labels]
    ax.set_xticks(positions, display_labels); ax.set_xlim(-.6, len(labels) - .4)
    if tick_font_size is not None:
        ax.tick_params(axis="x", labelsize=_positive(tick_font_size, "tick_font_size"))
    ax.set_ylabel(ylabel); clean_axes(ax)
    if legend:
        compact_legend(ax,handles=[bar_artists, *lines], **(legend_options or {}))
    return {"bars": bar_artists, "lines": lines, "bands": bands, "annotations": annotations}


def _matrix(values, row_labels, col_labels):
    arr = np.asarray(values, dtype=float)
    rows, cols = _labels(row_labels, name="row labels"), _labels(col_labels, name="column labels")
    if arr.shape != (len(rows), len(cols)):
        raise ValueError("Matrix shape must match row and column labels")
    if np.isinf(arr).any():
        raise ValueError("Matrix values cannot be infinite; use NaN only for explicitly missing observations")
    return arr, rows, cols


def _normalization(values, vmin, vmax, center=None):
    valid = values[np.isfinite(values)]
    if not valid.size and (vmin is None or vmax is None):
        raise ValueError("All-missing matrices require an explicit color range")
    if center is not None and vmin is None and vmax is None:
        center = float(center)
        span = max(float(np.max(np.abs(valid - center))), 0.5)
        vmin, vmax = center - span, center + span
    low = float(np.min(valid)) if vmin is None else float(vmin)
    high = float(np.max(valid)) if vmax is None else float(vmax)
    if low == high and vmin is None and vmax is None:
        pad = max(abs(low) * 0.01, 0.5); low -= pad; high += pad
    if not np.isfinite([low, high]).all() or low >= high:
        raise ValueError("Color range must be finite and increasing")
    if valid.size and (np.min(valid) < low or np.max(valid) > high):
        raise ValueError("Color range must cover all supplied observations; no silent clipping")
    if center is not None:
        center = float(center)
        if not math.isfinite(center) or not low < center < high:
            raise ValueError("Color center must lie strictly inside the range")
        return mcolors.TwoSlopeNorm(vcenter=center, vmin=low, vmax=high)
    return mcolors.Normalize(vmin=low, vmax=high)


def matrix_heatmap(ax, values, row_labels, col_labels, *, cmap="viridis", vmin=None,
                   vmax=None, center=None, annotate=False, fmt=".1f", missing_color="#EEEEEE"):
    arr, rows, cols = _matrix(values, row_labels, col_labels)
    norm = _normalization(arr, vmin, vmax, center)
    cmap_object = (mpl.colormaps[cmap] if isinstance(cmap, str) else cmap).with_extremes(bad=missing_color)
    # QuadMesh preserves individual editable cells in SVG/PDF (not an embedded image).
    mesh = ax.pcolormesh(np.ma.masked_invalid(arr), cmap=cmap_object, norm=norm,
                        edgecolors="white", linewidth=0.5, rasterized=False)
    ax.set_xlim(0, len(cols)); ax.set_ylim(len(rows), 0)
    ax.set_xticks(np.arange(len(cols)) + 0.5, cols)
    ax.set_yticks(np.arange(len(rows)) + 0.5, rows)
    ax.tick_params(length=0, pad=4)
    for spine in ax.spines.values(): spine.set_visible(False)
    for i, j in np.ndindex(arr.shape):
        if np.isnan(arr[i, j]):
            ax.text(j + 0.5, i + 0.5, "×", ha="center", va="center", color="#808080")
        elif annotate:
            rgba = cmap_object(norm(arr[i, j])); light = 0.2126 * rgba[0] + 0.7152 * rgba[1] + 0.0722 * rgba[2]
            ax.text(j + 0.5, i + 0.5, format(arr[i, j], fmt), ha="center", va="center",
                    color="white" if light < 0.48 else INK, fontsize=7.5)
    return mesh


def dot_matrix(ax, values, sizes, row_labels, col_labels, *, cmap="viridis", vmin=None,
               vmax=None, size_max=100, size_scale=80):
    arr, rows, cols = _matrix(values, row_labels, col_labels)
    size_values = np.asarray(sizes, dtype=float)
    if size_values.shape != arr.shape:
        raise ValueError("Size and color matrices must have the same shape")
    size_max = _positive(size_max, "size_max"); size_scale = _positive(size_scale, "size_scale")
    valid = np.isfinite(arr)
    if not np.isfinite(size_values[valid]).all() or np.any(size_values[valid] < 0) or np.any(size_values[valid] > size_max):
        raise ValueError("Marker sizes must lie between zero and size_max at observed cells")
    norm = _normalization(arr, vmin, vmax)
    yy, xx = np.indices(arr.shape)
    artist = ax.scatter(xx[valid], yy[valid], s=size_values[valid] / size_max * size_scale,
                        c=arr[valid], cmap=cmap, norm=norm, edgecolors="none")
    if (~valid).any():
        ax.scatter(xx[~valid], yy[~valid], marker="x", color="#999999", s=12, linewidths=0.6)
    ax.set_xticks(range(len(cols)), cols); ax.set_yticks(range(len(rows)), rows)
    ax.set_xlim(-0.6, len(cols) - 0.4); ax.set_ylim(len(rows) - 0.4, -0.6)
    clean_axes(ax, "both"); ax.tick_params(length=0)
    return artist


def size_legend(ax, values=(25, 50, 100), *, size_max=100, size_scale=80, title="Fraction (%)", **kwargs):
    values = _vector(values, "legend size values"); size_max = _positive(size_max, "size_max")
    size_scale = _positive(size_scale, "size_scale")
    if np.any(values < 0) or np.any(values > size_max):
        raise ValueError("Size legend must use the same zero-to-size_max scale as the plot")
    handles = [ax.scatter([], [], s=v / size_max * size_scale, color="#66737C", label=f"{v:g}") for v in values]
    return ax.legend(handles=handles, title=title, frameon=False, **kwargs)


def pareto_mask(x, y, *, x_direction="min", y_direction="max"):
    x, y = _vector(x, "x"), _vector(y, "y"); _same_length(x, y)
    if x_direction not in ("min", "max") or y_direction not in ("min", "max"):
        raise ValueError("Pareto directions must be min or max")
    costs = np.column_stack([x if x_direction == "min" else -x,
                             y if y_direction == "min" else -y])
    return np.array([not np.any(np.all(costs <= p, axis=1) & np.any(costs < p, axis=1)) for p in costs])


def pareto_scatter(ax, x, y, labels, *, colors=None, x_direction="min", y_direction="max",
                   connect=True, sizes=None, xlabel="", ylabel="", annotate=True):
    x, y = _vector(x, "x"), _vector(y, "y"); _same_length(x, y)
    labels = _labels(labels, len(x)); colors = _colors(labels, colors)
    frontier = pareto_mask(x, y, x_direction=x_direction, y_direction=y_direction)
    if sizes is None: sizes = np.full(len(x), 36.0)
    else:
        sizes = _vector(sizes, "sizes"); _same_length(x, sizes)
        if np.any(sizes < 0): raise ValueError("Marker areas cannot be negative")
    if connect:
        coords = np.unique(np.column_stack([x[frontier], y[frontier]]), axis=0)
        order = np.argsort(coords[:, 0], kind="stable")
        ax.plot(coords[order, 0], coords[order, 1], color="#8C969D", linewidth=1,
                linestyle="--", zorder=1, label="Pareto frontier")
    scatter = ax.scatter(x, y, c=colors, s=sizes, edgecolors="white", linewidths=0.7, zorder=3)
    if annotate:
        for xx, yy, label in zip(x, y, labels):
            ax.annotate(label, (xx, yy), xytext=(4, 4), textcoords="offset points", fontsize=7.5)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); clean_axes(ax, "both")
    return {"scatter": scatter, "frontier": frontier}


def paired_distribution(ax, values, labels, *, colors=None, paired=False, seed=0,
                        ylabel="", violin=True):
    labels = _labels(labels); colors = _colors(labels, colors)
    if len(values) != len(labels): raise ValueError("Supply one sample array per label")
    groups = [_vector(group, "sample values") for group in values]
    if paired and len({len(group) for group in groups}) != 1:
        raise ValueError("Paired samples require equal lengths in matched entity order")
    rng = np.random.default_rng(seed); x_positions = []
    for i, group in enumerate(groups): x_positions.append(i + rng.uniform(-0.22, -0.06, len(group)))
    if paired:
        for j in range(len(groups[0])):
            ax.plot([xp[j] for xp in x_positions], [group[j] for group in groups],
                    color="#BCC3C7", linewidth=0.5, alpha=0.55, zorder=1)
    for i, (group, color) in enumerate(zip(groups, colors)):
        if violin and len(group) >= 3 and np.ptp(group) > 0:
            parts = ax.violinplot([group], positions=[i + 0.04], widths=0.7,
                                  showextrema=False, showmeans=False, showmedians=False)
            for body in parts["bodies"]:
                body.set_facecolor(color); body.set_edgecolor("none"); body.set_alpha(0.24)
                vertices = body.get_paths()[0].vertices
                vertices[:, 0] = np.maximum(vertices[:, 0], i + 0.04)
        ax.scatter(x_positions[i], group, s=10, color=color, alpha=0.65, linewidths=0, zorder=3)
        q1, median, q3 = np.percentile(group, [25, 50, 75])
        ax.plot([i + 0.035] * 2, [q1, q3], color=INK, linewidth=2, zorder=4)
        ax.scatter([i + 0.035], [median], color="white", edgecolor=INK, s=16, linewidth=0.8, zorder=5)
    ax.set_xticks(range(len(labels)), labels); ax.set_xlim(-0.5, len(labels) - 0.5)
    ax.set_ylabel(ylabel); clean_axes(ax)
    return {"groups": groups, "median": np.array([np.median(v) for v in groups])}


def embedding_scatter(ax, coordinates, groups, *, order=None, colors=None, size=10,
                      alpha=0.65, rasterized=False):
    coords = np.asarray(coordinates, dtype=float); groups = np.asarray(groups, dtype=str)
    if coords.ndim != 2 or coords.shape[1] != 2 or not len(coords) or not np.isfinite(coords).all():
        raise ValueError("Coordinates must be a finite nonempty N by 2 array")
    if groups.ndim != 1 or len(groups) != len(coords) or any(not g.strip() for g in groups):
        raise ValueError("Each coordinate needs a group ID")
    labels = _labels(order if order is not None else list(dict.fromkeys(groups)))
    if set(labels) != set(groups): raise ValueError("Group order must contain each observed ID exactly once")
    colors = _colors(labels, colors); artists = []
    if not math.isfinite(float(alpha)) or not 0 <= alpha <= 1: raise ValueError("alpha must lie in [0, 1]")
    size = _positive(size, "size")
    for i, (label, color) in enumerate(zip(labels, colors)):
        part = coords[groups == label]
        artists.append(ax.scatter(part[:, 0], part[:, 1], c=color, label=label,
                                  s=size, marker=MARKERS[i % len(MARKERS)], alpha=alpha,
                                  linewidths=0, rasterized=rasterized))
    ax.set_xlabel("Dimension 1"); ax.set_ylabel("Dimension 2"); clean_axes(ax, None)
    return artists


def forest_intervals(ax, labels, estimates, lower, upper, *, colors=None, reference=0, xlabel="Effect"):
    if reference is not None:
        if not math.isfinite(float(reference)): raise ValueError("reference must be finite")
        ax.axvline(reference, color="#ABB3B8", linestyle="--", linewidth=0.8, zorder=0)
    return comparison_intervals(ax, labels, estimates, lower=lower, upper=upper,
                                colors=colors, xlabel=xlabel)


def volcano(ax, effects, probabilities, *, labels=None, statistic="q", effect_threshold=1,
            probability_threshold=0.05, annotate_indices=(), zero_floor=None,
            colors=None, xlabel="Log2 fold change"):
    effects, probs = _vector(effects, "effects"), _vector(probabilities, "probabilities")
    _same_length(effects, probs)
    annotate_indices = tuple(annotate_indices)
    if np.any((probs < 0) | (probs > 1)): raise ValueError("Probabilities must lie in [0, 1]")
    if statistic not in ("p", "q", "adjusted p"): raise ValueError("statistic must be p, q, or adjusted p")
    effect_threshold = _positive(effect_threshold, "effect_threshold")
    probability_threshold = _positive(probability_threshold, "probability_threshold")
    if probability_threshold > 1: raise ValueError("Probability threshold cannot exceed one")
    display = probs.copy()
    if np.any(probs == 0):
        if zero_floor is None: raise ValueError("Zero probabilities require an explicit display-only zero_floor")
        floor = _positive(zero_floor, "zero_floor")
        positive = probs[probs > 0]
        if floor > 1 or floor > probability_threshold or (positive.size and floor > positive.min()):
            raise ValueError("zero_floor cannot exceed the threshold or any positive supplied probability")
        display[probs == 0] = floor
        ax.text(0.98, 0.02, f"Zero {statistic} displayed at {floor:g}", ha="right", va="bottom",
                transform=ax.transAxes, fontsize=6.5)
    elif zero_floor is not None:
        _positive(zero_floor, "zero_floor")
    palette = ["#3C5488", "#C3C8CC", "#E64B35"] if colors is None else list(colors)
    if len(palette) != 3 or not all(mcolors.is_color_like(c) for c in palette):
        raise ValueError("Volcano colors must be [negative, neutral, positive]")
    sig = probs <= probability_threshold
    codes = np.where(sig & (effects <= -effect_threshold), 0,
                     np.where(sig & (effects >= effect_threshold), 2, 1))
    yy = -np.log10(display)
    artist = ax.scatter(effects, yy, c=np.array(palette)[codes], s=10,
                         alpha=0.72, linewidths=0, rasterized=False)
    ax.axhline(-math.log10(probability_threshold), color="#A9B1B6", linestyle="--", linewidth=0.7)
    for threshold in [-effect_threshold, effect_threshold]:
        ax.axvline(threshold, color="#A9B1B6", linestyle="--", linewidth=0.7)
    if labels is not None:
        labels = _labels(labels, len(effects))
    if annotate_indices and labels is None: raise ValueError("Annotation indices require labels")
    for index in annotate_indices:
        if not isinstance(index, (int, np.integer)) or not 0 <= index < len(effects):
            raise ValueError("Annotation index is out of bounds")
        ax.annotate(labels[index], (effects[index], yy[index]), xytext=(3, 4),
                    textcoords="offset points", fontsize=7)
    ax.set_xlabel(xlabel); ax.set_ylabel(f"−log10({statistic})"); clean_axes(ax, None)
    return artist


def calibration(ax, confidence, accuracy, counts, *, edges=None, color=None, label=None):
    confidence, accuracy = _vector(confidence, "confidence"), _vector(accuracy, "accuracy")
    counts = _vector(counts, "counts"); _same_length(confidence, accuracy, counts)
    if np.any((confidence < 0) | (confidence > 1) | (accuracy < 0) | (accuracy > 1)):
        raise ValueError("Calibration confidence and accuracy must lie in [0, 1]")
    if np.any(counts < 0) or np.any(counts != np.floor(counts)) or counts.sum() <= 0:
        raise ValueError("Calibration counts must be nonnegative integers with a positive total")
    if edges is not None:
        edges = _vector(edges, "edges")
        if len(edges) != len(counts) + 1 or np.any(np.diff(edges) <= 0) or edges[0] < 0 or edges[-1] > 1:
            raise ValueError("Bin edges must be increasing within [0, 1] with len(counts)+1 entries")
        if np.any((counts > 0) & ((confidence < edges[:-1]) | (confidence > edges[1:]))):
            raise ValueError("Observed mean confidence must lie inside its bin")
    used = counts > 0
    if np.any(np.diff(confidence[used]) <= 0):
        raise ValueError("Observed calibration bins must have increasing mean confidence")
    ece = float(np.sum(counts[used] * np.abs(accuracy[used] - confidence[used])) / counts[used].sum())
    ax.plot([0, 1], [0, 1], color="#AAB3B9", linestyle="--", linewidth=0.8, zorder=1)
    line, = ax.plot(confidence[used], accuracy[used], marker="o", color=color, label=label, zorder=3)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Mean confidence", ylabel="Observed accuracy")
    clean_axes(ax, "both")
    return {"line": line, "ece": ece, "used_bins": used}


def audit_figure(fig):
    """Report missing glyphs and visible text outside the canvas, not all overlaps."""
    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        fig.canvas.draw()
        if fig.get_layout_engine() is not None:
            # Constrained axes can change tick domains during the first draw.
            # Measure the settled layout that the actual export will use.
            fig.canvas.draw()
    glyphs = sorted({str(w.message) for w in captured if "Glyph" in str(w.message) and "missing" in str(w.message)})
    renderer = fig.canvas.get_renderer(); bounds = fig.bbox
    outside_ticks = set()
    for ax in _figure_axes(fig):
        if not ax.axison:
            # Axis-off layout cells keep tick Text objects that are not painted.
            outside_ticks.update([ax.xaxis.label, ax.yaxis.label,
                                  ax.xaxis.get_offset_text(), ax.yaxis.get_offset_text()])
            for axis in (ax.xaxis, ax.yaxis):
                for tick in [*axis.get_major_ticks(), *axis.get_minor_ticks()]:
                    outside_ticks.update((tick.label1, tick.label2))
            continue
        for axis in (ax.xaxis, ax.yaxis):
            low, high = sorted(axis.get_view_interval())
            for tick in [*axis.get_major_ticks(), *axis.get_minor_ticks()]:
                if not low - 1e-10 <= tick.get_loc() <= high + 1e-10:
                    outside_ticks.update((tick.label1, tick.label2))
    outside = []
    for text in fig.findobj(match=Text):
        if text in outside_ticks: continue
        if not text.get_visible() or not text.get_text().strip(): continue
        # Matplotlib retains invisible off-range tick labels as artists.
        if text.axes is not None and text.get_clip_on(): continue
        box = text.get_window_extent(renderer)
        if not np.isfinite(box.extents).all(): continue
        if box.width == 0 or box.height == 0: continue
        if box.x0 < bounds.x0 - 2 or box.y0 < bounds.y0 - 2 or box.x1 > bounds.x1 + 2 or box.y1 > bounds.y1 + 2:
            outside.append(text.get_text())
    return {"missing_glyphs": glyphs, "text_outside_canvas": outside,
            "width_mm": float(fig.get_figwidth() * 25.4), "height_mm": float(fig.get_figheight() * 25.4)}


def save_figure(fig, base_path, formats=("png",), dpi=300,
                metadata=None, protected_paths=()):
    """Export at the figure's physical size; never change numeric artists.

    PNG is the ordinary deliverable. SVG/PDF are explicit format opt-ins.
    This exporter handles numerical figures; new conceptual diagrams stay raster.
    Supply protected_paths for every upstream input file.
    """
    base = Path(base_path)
    if base.suffix.lower() in (".svg", ".pdf", ".png"): base = base.with_suffix("")
    formats = tuple(formats)
    if not formats or len(set(formats)) != len(formats) or any(f not in ("svg", "pdf", "png") for f in formats):
        raise ValueError("formats must be a nonempty unique subset of svg, pdf, png")
    dpi = _positive(dpi, "dpi")
    targets = {fmt: base.parent / (base.name + "." + fmt) for fmt in formats}
    metadata_text = None
    if metadata is not None:
        metadata_text = json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        targets["metadata"] = base.parent / (base.name + ".metadata.json")
    protected = {Path(path).resolve() for path in protected_paths}
    if any(path.resolve() in protected for path in targets.values()):
        raise ValueError("An export would overwrite protected source data")
    finish_paper_style(fig)
    qa = audit_figure(fig)
    if qa["missing_glyphs"]:
        raise ValueError("Missing glyphs: select an installed CJK/font fallback before export: " + "; ".join(qa["missing_glyphs"]))
    base.parent.mkdir(parents=True, exist_ok=True)
    temporary = []
    try:
        with mpl.rc_context({"svg.fonttype": "none", "pdf.fonttype": 42,
                             "ps.fonttype": 42, "svg.hashsalt": "ccfa-analysis-panels"}):
            for fmt, target in targets.items():
                fd, name = tempfile.mkstemp(prefix=".ccfa-figure-", suffix=target.suffix, dir=base.parent)
                os.close(fd); path = Path(name); temporary.append((path, target))
                if fmt == "metadata": path.write_text(metadata_text, encoding="utf-8", newline="\n")
                else:
                    stamp = {"Date": None} if fmt == "svg" else ({"CreationDate": None, "ModDate": None} if fmt == "pdf" else {"Software": "CCFA-Skills"})
                    fig.savefig(path, format=fmt, dpi=dpi, bbox_inches=None, metadata=stamp)
        for path, target in temporary: os.replace(path, target)
    finally:
        for path, _ in temporary:
            if path.exists(): path.unlink()
    return targets
