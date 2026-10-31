"""Question-led, composable statistical panels using supplied observations.

The plotting functions never simulate data, fit a predictive model, or infer a
significance test. ``demo_data`` is a separate, explicitly synthetic entry point.
All functions use a caller-owned Axes and inherit the surrounding paper_style.
Descriptive summaries are identified in their docstrings and return values.
Dependencies: NumPy and Matplotlib only.
"""
from __future__ import annotations

import math

import matplotlib.colors as mcolors
from matplotlib.patches import Polygon, Rectangle
from matplotlib.ticker import FuncFormatter
import numpy as np

import ccfa_analysis_panels as base


def _v(values, name):
    return base._vector(values, name)


def _m(values, name):
    try:
        values = np.asarray(values, dtype=float)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{name} must be a numeric matrix") from exc
    if values.ndim != 2 or not values.size or not np.isfinite(values).all():
        raise ValueError(f"{name} must be a nonempty finite matrix")
    return values


def _prob(values, name):
    values = _v(values, name)
    if ((values < 0) | (values > 1)).any():
        raise ValueError(f"{name} must lie in [0, 1]")
    return values


def _increasing(values, name, *, strict=True):
    values = _v(values, name)
    invalid = (np.diff(values) <= 0).any() if strict else (np.diff(values) < 0).any()
    if invalid:
        raise ValueError(f"{name} must be {'strictly increasing' if strict else 'nondecreasing'}")
    return values


def _label_values(labels, values):
    values = _v(values, "values")
    return base._labels(labels, len(values)), values


def _groups(samples, labels):
    labels = base._labels(labels)
    if len(samples) != len(labels):
        raise ValueError("Supply one observed group per label")
    return [_v(group, "sample group") for group in samples], labels


def _color(color):
    color = "#3C7EA5" if color is None else color
    if not mcolors.is_color_like(color):
        raise ValueError("color must be a Matplotlib color")
    return color


def _xy(x, y):
    x, y = _v(x, "x"), _v(y, "y")
    base._same_length(x, y)
    return x, y


def _density(samples, grid):
    """Gaussian KDE with a stated Silverman bandwidth; constant samples allowed."""
    if len(samples) < 2:
        raise ValueError("Density panels need at least two observations per group")
    spread = float(np.std(samples, ddof=1))
    if spread == 0:
        spread = max(abs(float(samples[0])) * .02, .05)
    bandwidth = 1.06 * spread * len(samples) ** (-.2)
    density = np.exp(-.5 * ((grid[:, None] - samples[None, :]) / bandwidth) ** 2).mean(axis=1)
    return density / (bandwidth * math.sqrt(2 * math.pi)), bandwidth


def ecdf(ax, samples, *, color=None, label=None, xlabel="Value", ylabel="Cumulative fraction"):
    """Right-continuous empirical CDF: ties retain all observation mass."""
    samples = _v(samples, "samples")
    values, counts = np.unique(samples, return_counts=True)
    fraction = np.cumsum(counts) / len(samples)
    line, = ax.step(values, fraction, where="post", color=_color(color), label=label)
    ax.set(xlabel=xlabel, ylabel=ylabel, ylim=(0, 1.02))
    base.clean_axes(ax)
    return {"line": line, "values": values, "fractions": fraction, "sample_count": len(samples)}


def survival_step(ax, time, survival, *, lower=None, upper=None, color=None,
                  label=None, xlabel="Time", ylabel="Survival probability"):
    """Display supplied survival estimates; no censoring estimator is inferred."""
    time = _increasing(time, "time")
    survival = _prob(survival, "survival")
    base._same_length(time, survival)
    if (time < 0).any() or (np.diff(survival) > 0).any():
        raise ValueError("Survival requires nonnegative time and nonincreasing probabilities")
    lo, hi = base._bounds(survival, lower, upper)
    if lo is not None:
        _prob(lo, "lower"); _prob(hi, "upper")
    color = _color(color)
    line, = ax.step(time, survival, where="post", color=color, label=label)
    if lo is not None:
        ax.fill_between(time, lo, hi, step="post", color=color, alpha=.16, linewidth=0)
    ax.set(xlabel=xlabel, ylabel=ylabel, ylim=(0, 1.02))
    base.clean_axes(ax)
    return {"line": line, "survival": survival.copy()}


def raincloud(ax, samples, labels, *, colors=None, seed=0, xlabel="Observed value"):
    """Raw points, median/IQR, and half-KDE; jitter is visual and seed-controlled."""
    groups, labels = _groups(samples, labels)
    if any(len(group) < 2 for group in groups):
        raise ValueError("Raincloud density needs at least two observations per group")
    colors = base._colors(labels, colors)
    span = np.ptp(np.concatenate(groups))
    margin = max(float(span) * .12, .1)
    grid = np.linspace(min(g.min() for g in groups) - margin,
                       max(g.max() for g in groups) + margin, 180)
    rng = np.random.default_rng(seed)
    densities = [_density(group, grid)[0] for group in groups]
    peak = max(float(d.max()) for d in densities)
    points = []
    for i, (group, color, density) in enumerate(zip(groups, colors, densities)):
        ax.fill_between(grid, i, i + density / peak * .38,
                        color=color, alpha=.35, linewidth=.7, edgecolor=color)
        points.append(ax.scatter(group, i - .13 - rng.uniform(0, .12, len(group)),
                                 color=color, s=10, alpha=.55, linewidths=0, zorder=3))
        q1, med, q3 = np.quantile(group, [.25, .5, .75])
        ax.plot([q1, q3], [i, i], color=color, lw=3, solid_capstyle="round")
        ax.scatter([med], [i], s=18, c="white", edgecolors=color, linewidths=.8, zorder=4)
    ax.set_yticks(range(len(labels)), labels)
    ax.set(xlabel=xlabel, ylim=(-.45, len(labels) - .48))
    base.clean_axes(ax, "x")
    return {"points": points, "density_grid": grid, "density_scale": peak,
            "summary": "sample median and 25th–75th percentiles; Gaussian KDE"}


def ridgeline(ax, samples, labels, *, colors=None, xlabel="Observed value"):
    """Aligned Gaussian densities on a common grid and common density scale."""
    groups, labels = _groups(samples, labels)
    colors = base._colors(labels, colors)
    span = np.ptp(np.concatenate(groups))
    margin = max(float(span) * .15, .1)
    grid = np.linspace(min(g.min() for g in groups) - margin,
                       max(g.max() for g in groups) + margin, 180)
    calculated = [_density(group, grid) for group in groups]
    scale = max(float(d.max()) for d, _ in calculated)
    for i, ((density, _), color) in enumerate(zip(calculated, colors)):
        ax.fill_between(grid, i, i + density / scale * .8, facecolor=color, alpha=.4)
        ax.plot(grid, i + density / scale * .8, color=color, lw=1)
    ax.set_yticks(range(len(labels)), labels)
    ax.set(xlabel=xlabel, ylim=(-.15, len(labels) - .05))
    base.clean_axes(ax, "x")
    return {"grid": grid, "densities": [d for d, _ in calculated],
            "bandwidths": [bw for _, bw in calculated], "common_density_scale": scale}


def ranked_intervals(ax, labels, values, lower, upper, *, colors=None,
                     order="input", reference=0, xlabel="Effect estimate"):
    """Forest plot of supplied bounds; sorting moves labels and bounds together."""
    labels, values = _label_values(labels, values)
    lo, hi = base._bounds(values, lower, upper)
    if order not in ("input", "ascending", "descending"):
        raise ValueError("order must be input, ascending, or descending")
    indices = np.arange(len(values)) if order == "input" else np.argsort(values, kind="stable")
    if order == "descending": indices = indices[::-1]
    colors = base._colors(labels, colors)
    if reference is not None and not math.isfinite(float(reference)):
        raise ValueError("reference must be finite or None")
    result = base.comparison_intervals(ax, [labels[i] for i in indices], values[indices],
                                       lower=lo[indices], upper=hi[indices],
                                       colors=[colors[i] for i in indices], xlabel=xlabel)
    if reference is not None: ax.axvline(reference, color=base.INK, lw=.7, ls=":", zorder=1)
    result["order"] = indices
    return result


def dumbbell(ax, labels, before, after, *, colors=None,
             endpoints=("Before", "After"), xlabel="Value"):
    """Two measurements for each supplied matched entity; rows never reordered."""
    labels, before = _label_values(labels, before)
    after = _v(after, "after"); base._same_length(before, after)
    if len(endpoints) != 2 or any(not str(v).strip() for v in endpoints):
        raise ValueError("endpoints must contain two nonempty names")
    colors = ["#9DA7AD", "#327DA1"] if colors is None else list(colors)
    if len(colors) != 2 or not all(mcolors.is_color_like(c) for c in colors):
        raise ValueError("Supply two endpoint colors")
    y = np.arange(len(labels))
    for i in y: ax.plot([before[i], after[i]], [i, i], color="#B9C3C8", lw=1.3)
    left = ax.scatter(before, y, color=colors[0], s=26, label=endpoints[0], zorder=3)
    right = ax.scatter(after, y, color=colors[1], s=30, label=endpoints[1], zorder=3)
    ax.set_yticks(y, labels); ax.set(xlabel=xlabel, ylim=(len(labels)-.5, -.5))
    base.clean_axes(ax, "x")
    return {"before": left, "after": right, "difference": after - before}


def bland_altman(ax, first, second, *, color=None, limits_multiplier=1.96,
                 xlabel="Pair mean", ylabel="Second − first"):
    """Descriptive mean difference ± multiplier × sample SD; not a CI or test."""
    first, second = _xy(first, second)
    if len(first) < 2:
        raise ValueError("Agreement summaries require at least two matched pairs")
    multiplier = base._positive(limits_multiplier, "limits_multiplier")
    means = (first + second) / 2; differences = second - first
    bias = float(differences.mean()); sd = float(differences.std(ddof=1))
    scatter = ax.scatter(means, differences, color=_color(color), s=14, alpha=.6, linewidths=0)
    ax.axhline(bias, color=base.INK, lw=1)
    for value in [bias - multiplier*sd, bias + multiplier*sd]:
        ax.axhline(value, color=base.INK, lw=.8, ls="--")
    ax.set(xlabel=xlabel, ylabel=ylabel); base.clean_axes(ax)
    return {"scatter": scatter, "bias": bias, "sample_sd": sd,
            "descriptive_limits": (bias-multiplier*sd, bias+multiplier*sd)}


def residual_diagnostics(ax, fitted, residuals, *, color=None,
                         xlabel="Supplied fitted value", ylabel="Supplied residual"):
    """Show supplied residuals around zero; no model or smoothing fit is added."""
    fitted, residuals = _xy(fitted, residuals)
    artist = ax.scatter(fitted, residuals, color=_color(color), s=14, alpha=.55, linewidths=0)
    ax.axhline(0, color=base.INK, lw=.8, ls=":")
    ax.set(xlabel=xlabel, ylabel=ylabel); base.clean_axes(ax)
    return {"scatter": artist}


def quantile_fan(ax, x, quantiles, probabilities, *, color=None,
                 xlabel="Input", ylabel="Response"):
    """Supplied ordered, symmetric quantile bands and the supplied median."""
    x = _increasing(x, "x"); probabilities = _prob(probabilities, "probabilities")
    q = _m(quantiles, "quantiles")
    if q.shape != (len(probabilities), len(x)) or (np.diff(probabilities) <= 0).any():
        raise ValueError("quantiles must have one row per strictly increasing probability and one column per x")
    if len(probabilities) < 3 or len(probabilities) % 2 != 1:
        raise ValueError("Supply a median and at least one symmetric quantile pair")
    middle = len(probabilities)//2
    if not np.isclose(probabilities[middle], .5) or not np.allclose(probabilities + probabilities[::-1], 1):
        raise ValueError("Quantile probabilities must be symmetric around the supplied median")
    if (np.diff(q, axis=0) < 0).any():
        raise ValueError("Quantile curves must not cross")
    color = _color(color); bands = []
    for i in range(middle):
        bands.append(ax.fill_between(x, q[i], q[-i-1], color=color,
                                     alpha=.1+.12*i, linewidth=0))
    line, = ax.plot(x, q[middle], color=color, lw=1.4)
    ax.set(xlabel=xlabel, ylabel=ylabel); base.clean_axes(ax)
    return {"median": line, "bands": bands, "probabilities": probabilities.copy()}


def precision_recall(ax, recall, precision, *, color=None, prevalence=None,
                     label=None, xlabel="Recall", ylabel="Precision"):
    """Plot supplied operating points; prevalence baseline must be supplied."""
    recall = _increasing(_prob(recall, "recall"), "recall", strict=False)
    precision = _prob(precision, "precision"); base._same_length(recall, precision)
    if prevalence is not None:
        prevalence = float(prevalence)
        if not math.isfinite(prevalence) or not 0 <= prevalence <= 1:
            raise ValueError("prevalence must lie in [0, 1]")
    line, = ax.plot(recall, precision, color=_color(color), label=label)
    if prevalence is not None: ax.axhline(prevalence, color="#8A949B", lw=.8, ls=":")
    ax.set(xlabel=xlabel, ylabel=ylabel, xlim=(0, 1), ylim=(0, 1.02))
    base.clean_axes(ax)
    return {"line": line, "prevalence": prevalence}


def roc(ax, false_positive_rate, true_positive_rate, *, color=None,
        label=None, xlabel="False-positive rate", ylabel="True-positive rate"):
    """Supplied nondecreasing ROC points; no AUC or endpoint is fabricated."""
    x = _increasing(_prob(false_positive_rate, "false_positive_rate"), "false_positive_rate", strict=False)
    y = _increasing(_prob(true_positive_rate, "true_positive_rate"), "true_positive_rate", strict=False)
    base._same_length(x, y)
    ax.plot([0, 1], [0, 1], color="#A1A9AE", lw=.8, ls=":")
    line, = ax.plot(x, y, color=_color(color), label=label)
    ax.set(xlabel=xlabel, ylabel=ylabel, xlim=(0, 1), ylim=(0, 1.02))
    base.clean_axes(ax)
    return {"line": line}


def risk_coverage(ax, coverage, risk, *, color=None, label=None,
                  xlabel="Retained fraction", ylabel="Risk on retained observations"):
    """Show supplied selective-prediction risk at increasing positive coverage."""
    coverage = _increasing(_prob(coverage, "coverage"), "coverage")
    risk = _prob(risk, "risk"); base._same_length(coverage, risk)
    if (coverage <= 0).any(): raise ValueError("Risk requires positive coverage")
    line, = ax.plot(coverage, risk, color=_color(color), label=label)
    ax.set(xlabel=xlabel, ylabel=ylabel, xlim=(0, 1), ylim=(0, 1))
    base.clean_axes(ax)
    return {"line": line}


def rank_trajectories(ax, stages, ranks, labels, *, colors=None, xlabel="Condition"):
    """Bump chart of supplied ranks; tied ranks remain tied, not jittered."""
    stages = base._labels(stages); labels = base._labels(labels)
    ranks = _m(ranks, "ranks")
    if ranks.shape != (len(labels), len(stages)):
        raise ValueError("ranks needs one row per entity and one column per stage")
    if (ranks < 1).any() or not np.allclose(ranks, np.round(ranks)):
        raise ValueError("Supply positive integer ranks; do not infer ranks from unrelated scores")
    colors = base._colors(labels, colors)
    lines = []
    for row, name, color in zip(ranks, labels, colors):
        lines.append(ax.plot(range(len(stages)), row, color=color, marker="o", ms=3,
                             label=name)[0])
    ax.set_xticks(range(len(stages)), stages)
    ax.set_yticks(np.arange(1, ranks.max()+1))
    ax.set(xlabel=xlabel, ylabel="Rank (1 is highest)", ylim=(ranks.max()+.35, .65))
    base.clean_axes(ax)
    return {"lines": lines, "ranks": ranks.copy()}


def parallel_coordinates(ax, values, dimensions, ranges, labels, *, colors=None):
    """Normalize by explicit domain ranges, with original ranges in axis labels."""
    dimensions = base._labels(dimensions); labels = base._labels(labels)
    values = _m(values, "values"); ranges = _m(ranges, "ranges")
    if values.shape != (len(labels), len(dimensions)) or ranges.shape != (len(dimensions), 2):
        raise ValueError("values and ranges must match entity and dimension labels")
    if len(dimensions) < 2 or (ranges[:, 1] <= ranges[:, 0]).any():
        raise ValueError("At least two dimensions with positive domain ranges are required")
    if ((values < ranges[:, 0]) | (values > ranges[:, 1])).any():
        raise ValueError("Observed values lie outside the supplied domain ranges")
    normalized = (values-ranges[:, 0])/(ranges[:, 1]-ranges[:, 0])
    colors = base._colors(labels, colors); lines = []
    for i in range(len(dimensions)): ax.axvline(i, color=base.GRID, lw=1, zorder=0)
    for row, name, color in zip(normalized, labels, colors):
        lines.append(ax.plot(range(len(dimensions)), row, color=color, marker="o", ms=3, label=name)[0])
    ax.set_xticks(range(len(dimensions)), [f"{d}\n[{a:g}, {b:g}]" for d, (a,b) in zip(dimensions,ranges)])
    ax.set(ylabel="Position within stated domain", ylim=(-.04, 1.04))
    base.clean_axes(ax)
    return {"lines": lines, "normalized": normalized, "ranges": ranges.copy()}


def ternary(ax, fractions, labels, *, color=None):
    """Three-part compositions with known denominator; no implicit renormalizing."""
    fractions = _m(fractions, "fractions"); labels = base._labels(labels, 3)
    if fractions.shape[1] != 3 or (fractions < 0).any() or not np.allclose(fractions.sum(axis=1), 1):
        raise ValueError("Each composition must contain three nonnegative fractions summing to one")
    vertices = np.array([[0, 0], [1, 0], [.5, math.sqrt(3)/2]])
    xy = fractions @ vertices
    ax.add_patch(Polygon(vertices, closed=True, fill=False, edgecolor=base.INK, lw=.8))
    for i in range(3):
        for q in [.25, .5, .75]:
            others = [j for j in range(3) if j != i]
            a = q*vertices[i]+(1-q)*vertices[others[0]]
            b = q*vertices[i]+(1-q)*vertices[others[1]]
            ax.plot([a[0], b[0]], [a[1], b[1]], color=base.GRID, lw=.55, zorder=0)
    artist = ax.scatter(xy[:,0], xy[:,1], color=_color(color), s=18, alpha=.65, linewidths=0)
    for vertex, label, ha, va in zip(vertices, labels, ["right","left","center"], ["top","top","bottom"]):
        ax.annotate(label, vertex, xytext=(0, -3 if va=="top" else 3), textcoords="offset points", ha=ha, va=va)
    ax.set_aspect("equal"); ax.set(xlim=(-.08,1.08), ylim=(-.08,.97)); ax.axis("off")
    return {"scatter": artist, "coordinates": xy}


def transition_matrix(ax, values, labels, *, normalization, colors=None):
    """Counts or explicitly normalized transition mass; rows are source states."""
    values = _m(values, "values"); labels = base._labels(labels)
    if values.shape != (len(labels), len(labels)) or (values < 0).any():
        raise ValueError("Transition counts require a nonnegative square matrix matching labels")
    if normalization not in ("counts", "row", "column", "all"):
        raise ValueError("normalization must be counts, row, column, or all")
    if colors is not None:
        colors = list(colors)
        if len(colors) < 2 or not all(mcolors.is_color_like(c) for c in colors):
            raise ValueError("colors must supply at least two colormap anchors")
        cmap = mcolors.LinearSegmentedColormap.from_list("transitions", colors)
    else: cmap = "Blues"
    shown = values.copy()
    if normalization != "counts":
        axis = {"row": 1, "column": 0, "all": None}[normalization]
        denominator = values.sum(axis=axis, keepdims=True)
        if (denominator == 0).any():
            raise ValueError("A normalized transition matrix cannot have a zero denominator")
        shown = values/denominator
    # An all-zero raw count matrix is valid; its color scale still needs width.
    maximum = max(float(shown.max()), 1.) if normalization == "counts" else 1.
    mesh = base.matrix_heatmap(ax, shown, labels, labels, cmap=cmap,
                               vmin=0, vmax=maximum)
    ax.set(xlabel="Destination state", ylabel="Source state")
    return {"mesh": mesh, "display_values": shown, "normalization": normalization}


def mosaic_composition(ax, counts, group_labels, component_labels, *, colors=None):
    """Area is joint count share; group width is exposure and height conditional share."""
    counts = _m(counts, "counts")
    group_labels = base._labels(group_labels); component_labels = base._labels(component_labels)
    if counts.shape != (len(group_labels), len(component_labels)) or (counts < 0).any():
        raise ValueError("counts must be a nonnegative group-by-component matrix")
    totals = counts.sum(axis=1)
    if (totals <= 0).any(): raise ValueError("Every group needs a positive supplied denominator")
    colors = base._colors(component_labels, colors)
    widths = totals/totals.sum(); fractions = counts/totals[:, None]
    left = 0.; rectangles = []; centers = []
    for i, width in enumerate(widths):
        bottom = 0.; centers.append(left+width/2)
        for j, fraction in enumerate(fractions[i]):
            patch = Rectangle((left,bottom), width, fraction, facecolor=colors[j],
                              edgecolor="white", lw=.8, label=component_labels[j] if i==0 else None)
            ax.add_patch(patch); rectangles.append(patch); bottom += fraction
        left += width
    ax.set_xticks(centers, group_labels)
    ax.set(xlim=(0,1), ylim=(0,1), ylabel="Within-group fraction", xlabel="Group width ∝ supplied count")
    base.clean_axes(ax, None)
    return {"patches": rectangles, "widths": widths, "fractions": fractions, "group_totals": totals}


def matrix_bubbles(ax, values, row_labels, col_labels, *, magnitude_max, colors=None):
    """Signed matrix: hue encodes sign/value, bubble area encodes absolute value."""
    values = _m(values, "values"); rows = base._labels(row_labels); cols = base._labels(col_labels)
    maximum = base._positive(magnitude_max, "magnitude_max")
    if values.shape != (len(rows),len(cols)) or (np.abs(values)>maximum).any():
        raise ValueError("Matrix shape must match labels and magnitudes cannot exceed magnitude_max")
    colors = ["#4575B4", "#F4F4F4", "#D6604D"] if colors is None else list(colors)
    if len(colors) < 3 or not all(mcolors.is_color_like(c) for c in colors):
        raise ValueError("colors must contain negative, neutral and positive anchors")
    cmap = mcolors.LinearSegmentedColormap.from_list("signed_matrix",colors)
    yy,xx = np.indices(values.shape)
    artist = ax.scatter(xx.ravel(),yy.ravel(),s=np.abs(values).ravel()/maximum*190,
                        c=values.ravel(),cmap=cmap,vmin=-maximum,vmax=maximum,
                        edgecolors=base.INK,linewidths=.35)
    ax.set_xticks(range(len(cols)),cols); ax.set_yticks(range(len(rows)),rows)
    ax.set(xlim=(-.5,len(cols)-.5),ylim=(len(rows)-.5,-.5))
    base.clean_axes(ax,"both"); ax.tick_params(length=0)
    return {"scatter":artist,"magnitude_max":maximum}


def signed_effects(ax, labels, effects, *, colors=None, xlabel="Change from reference"):
    """Diverging lollipops with an honest zero baseline and supplied effect sign."""
    labels,effects = _label_values(labels,effects)
    colors = ["#4B88B4", "#D87953"] if colors is None else list(colors)
    if len(colors)!=2 or not all(mcolors.is_color_like(c) for c in colors):
        raise ValueError("Supply a negative and positive color")
    chosen=[colors[0] if value<0 else colors[1] for value in effects]
    ax.hlines(np.arange(len(labels)),0,effects,colors=chosen,lw=2.1)
    artist=ax.scatter(effects,np.arange(len(labels)),c=chosen,s=28,zorder=3)
    ax.axvline(0,color=base.INK,lw=.8)
    ax.set_yticks(range(len(labels)),labels);ax.set(xlabel=xlabel,ylim=(len(labels)-.5,-.5))
    base.clean_axes(ax,"x")
    return {"scatter":artist,"effects":effects.copy()}


def convergence_envelope(ax, steps, runs, *, color=None, xlabel="Training step", ylabel="Objective"):
    """Plot all supplied runs and their pointwise median/IQR; not a confidence band."""
    steps=_increasing(steps,"steps");runs=_m(runs,"runs")
    if runs.shape[1]!=len(steps):raise ValueError("runs needs one column per step")
    color=_color(color);lo,median,hi=np.quantile(runs,[.25,.5,.75],axis=0)
    for row in runs:ax.plot(steps,row,color=color,alpha=.18,lw=.7)
    band=ax.fill_between(steps,lo,hi,color=color,alpha=.16,linewidth=0)
    line,=ax.plot(steps,median,color=color,lw=1.6)
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax)
    return {"median":line,"band":band,"lower":lo,"upper":hi,"summary":"Pointwise sample median and IQR across runs"}


def grouped_dot(ax, labels, values, series_labels, *, colors=None, xlabel="Value"):
    """Aligned categorical dot strips, using position rather than filled bar area."""
    labels=base._labels(labels);series_labels=base._labels(series_labels);values=_m(values,"values")
    if values.shape!=(len(series_labels),len(labels)):
        raise ValueError("values needs one row per series and one column per category")
    colors=base._colors(series_labels,colors);points=[]
    offsets=np.linspace(-.22,.22,len(series_labels)) if len(series_labels)>1 else [0]
    for row,name,color,offset in zip(values,series_labels,colors,offsets):
        points.append(ax.scatter(row,np.arange(len(labels))+offset,s=24,color=color,label=name))
    ax.set_yticks(range(len(labels)),labels);ax.set(xlabel=xlabel,ylim=(len(labels)-.5,-.5))
    base.clean_axes(ax,"x")
    return {"points":points,"values":values.copy()}


def contour_response(ax, x, y, response, *, colors=None, xlabel="Control A", ylabel="Control B", levels=8):
    """A supplied response grid, without fitting, extrapolation, or optimum claims."""
    x=_increasing(x,"x");y=_increasing(y,"y");response=_m(response,"response")
    if len(x)<2 or len(y)<2 or response.shape!=(len(y),len(x)):
        raise ValueError("A response grid needs at least 2×2 points aligned as y rows × x columns")
    if not isinstance(levels,(int,np.integer)) or isinstance(levels,bool) or levels<2:
        raise ValueError("levels must be an integer of at least two")
    if colors is None:cmap="viridis"
    else:
        colors=list(colors)
        if len(colors)<2 or not all(mcolors.is_color_like(c) for c in colors):raise ValueError("Supply at least two colormap colors")
        cmap=mcolors.LinearSegmentedColormap.from_list("response",colors)
    surface=ax.contourf(x,y,response,levels=int(levels),cmap=cmap)
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax,None)
    return {"contours":surface,"response":response.copy()}


def robustness_profile(ax, severity, scores, labels, *, colors=None,
                       xlabel="Perturbation severity", ylabel="Score"):
    """Aligned model curves across supplied perturbations; no smoothing or clipping."""
    severity=_increasing(severity,"severity");scores=_m(scores,"scores");labels=base._labels(labels)
    if scores.shape!=(len(labels),len(severity)):
        raise ValueError("scores needs one row per method and one column per severity")
    colors=base._colors(labels,colors);lines=[]
    for row,name,color in zip(scores,labels,colors):
        lines.append(ax.plot(severity,row,color=color,marker="o",ms=3,label=name)[0])
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax)
    return {"lines":lines,"scores":scores.copy()}


def cost_quality_frontier(ax, cost, quality, labels, *, colors=None,
                          cost_direction="min", quality_direction="max",
                          xlabel="Measured cost", ylabel="Measured quality"):
    """Use the existing exact dominance rule; equal points remain non-dominated."""
    cost,quality=_xy(cost,quality)
    if (cost<0).any():raise ValueError("Measured costs must be nonnegative")
    return base.pareto_scatter(ax,cost,quality,labels,colors=colors,
                               x_direction=cost_direction,y_direction=quality_direction,
                               xlabel=xlabel,ylabel=ylabel,annotate=False)


def quadrant_scatter(ax, x, y, labels, *, x_reference=0, y_reference=0,
                     colors=None, xlabel="Change in objective A", ylabel="Change in objective B",
                     annotate=False):
    """Two signed changes around supplied references; no quadrant is declared best.

    Useful for reward conflicts, competing objectives, and simultaneous effects.
    Exactly-on-reference observations remain boundary observations rather than
    being assigned to a favorable quadrant. Comparability of units is not assumed.
    """
    x,y=_xy(x,y);labels=base._labels(labels,len(x));colors=base._colors(labels,colors)
    x_reference,y_reference=float(x_reference),float(y_reference)
    if not np.isfinite([x_reference,y_reference]).all():
        raise ValueError("Quadrant references must be finite")
    ax.axvline(x_reference,color=base.INK,lw=.8,ls=":",zorder=1)
    ax.axhline(y_reference,color=base.INK,lw=.8,ls=":",zorder=1)
    scatter=ax.scatter(x,y,c=colors,s=26,edgecolors="white",linewidths=.6,zorder=3)
    if annotate:
        for xx,yy,label in zip(x,y,labels):
            ax.annotate(label,(xx,yy),xytext=(4,4),textcoords="offset points",fontsize=7.5)
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax,"both")
    return {"scatter":scatter,"regions":np.column_stack([np.sign(x-x_reference),np.sign(y-y_reference)]),
            "references":(x_reference,y_reference)}


def mean_delta(ax, before, after, labels, *, colors=None,
               xlabel="Before", ylabel="After − before (same unit)", annotate=False):
    """Baseline-versus-change scatter of matched values in the same unit.

    Despite the conventional name, no mean is estimated: the supplied entity
    values can already be means or individual observations. Descriptive baseline
    dependence does not establish a causal benefit or adjust regression to mean.
    """
    before,after=_xy(before,after);labels=base._labels(labels,len(before));colors=base._colors(labels,colors)
    delta=after-before
    ax.axhline(0,color=base.INK,lw=.8,ls=":",zorder=1)
    scatter=ax.scatter(before,delta,c=colors,s=26,edgecolors="white",linewidths=.6,zorder=3)
    if annotate:
        for xx,yy,label in zip(before,delta,labels):
            ax.annotate(label,(xx,yy),xytext=(4,4),textcoords="offset points",fontsize=7.5)
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax,"both")
    return {"scatter":scatter,"delta":delta,"before":before.copy()}


def _mirror_colors(colors):
    colors=["#3C7EA5","#D77957"] if colors is None else list(colors)
    if len(colors)!=2 or not all(mcolors.is_color_like(c) for c in colors):
        raise ValueError("Mirror panels need exactly two valid group colors")
    return colors


def _mirror_labels(labels):
    return base._labels(labels,2)


def _mirror_axis(ax,labels,xlabel,ylabel):
    ax.axhline(0,color=base.INK,lw=.75,zorder=2)
    # The negative vertical position is a visual mirror, not a negative count.
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value,_:f"{abs(value):g}"))
    ax.set(xlabel=xlabel,ylabel=ylabel or f"Absolute amount: {labels[0]} ↑ / {labels[1]} ↓")
    base.clean_axes(ax)


def mirrored_histogram(ax, first, second, bin_edges, *, colors=None,
                       labels=("First","Second"), xlabel="Observed value", ylabel=None):
    """Raw counts on common explicit bins, mirrored around zero.

    Counts are not probabilities or densities. Every supplied observation must
    fall in the given bin range, including the final right edge. Group sample
    sizes are returned so unequal exposure is visible to the integrating owner.
    """
    first,second=_v(first,"first"),_v(second,"second")
    edges=_increasing(bin_edges,"bin_edges")
    if len(edges)<2:raise ValueError("At least two bin edges are required")
    if any((group<edges[0]).any() or (group>edges[-1]).any() for group in (first,second)):
        raise ValueError("Every observation must fall inside the supplied histogram bin range")
    colors=_mirror_colors(colors);labels=_mirror_labels(labels)
    first_counts,_=np.histogram(first,bins=edges);second_counts,_=np.histogram(second,bins=edges)
    top=ax.bar(edges[:-1],first_counts,width=np.diff(edges),align="edge",color=colors[0],
               edgecolor="white",linewidth=.5,label=labels[0])
    bottom=ax.bar(edges[:-1],-second_counts,width=np.diff(edges),align="edge",color=colors[1],
                  edgecolor="white",linewidth=.5,label=labels[1])
    _mirror_axis(ax,labels,xlabel,ylabel or f"Count: {labels[0]} ↑ / {labels[1]} ↓")
    ax.set_xlim(edges[0],edges[-1])
    return {"first_bars":top,"second_bars":bottom,"bin_edges":edges.copy(),
            "first_counts":first_counts,"second_counts":second_counts,
            "sample_counts":(len(first),len(second)),"normalization":"raw counts"}


def mirror_stem(ax, x, first, second, *, colors=None, labels=("First","Second"),
                xlabel="Shared position", ylabel=None):
    """Paired nonnegative spectra on common x; below-zero placement means mirroring.

    Peak amplitudes retain their supplied absolute values and common units. No
    maximum normalization, peak matching, or interpolation is performed.
    """
    x=_increasing(x,"x");first,second=_v(first,"first"),_v(second,"second")
    base._same_length(x,first,second)
    if (first<0).any() or (second<0).any():
        raise ValueError("Mirrored stem amplitudes must be nonnegative absolute amounts")
    colors=_mirror_colors(colors);labels=_mirror_labels(labels)
    top=ax.vlines(x,0,first,colors=colors[0],linewidth=1.3,label=labels[0])
    bottom=ax.vlines(x,0,-second,colors=colors[1],linewidth=1.3,label=labels[1])
    top_points=ax.scatter(x,first,c=colors[0],s=9,zorder=3)
    bottom_points=ax.scatter(x,-second,c=colors[1],s=9,zorder=3)
    _mirror_axis(ax,labels,xlabel,ylabel)
    return {"first_stems":top,"second_stems":bottom,"first_points":top_points,
            "second_points":bottom_points,"first":first.copy(),"second":second.copy()}


def binned_group_composition(ax, values, groups, bin_edges, group_order, *,
                             colors=None, xlabel="Value"):
    """Within-bin group shares from the same paired value/group observations.

    Horizontal positions and widths use the literal bin edges, allowing a shared
    x axis with a count histogram. The denominator of each occupied bin is its
    total observation count, returned as ``totals``. Empty bins stay blank and
    have NaN fractions; no pseudocounts, smoothing or hidden renormalizing occur.
    Numeric observations on the final right edge belong to the last bin, as in
    NumPy histogram. Group order also fixes stacking and color identity.
    """
    values=_v(values,"values");edges=_increasing(bin_edges,"bin_edges")
    order=base._labels(group_order)
    if len(edges)<2:raise ValueError("At least two bin edges are required")
    group_array=np.asarray(groups,dtype=object)
    if group_array.ndim!=1 or len(group_array)!=len(values):
        raise ValueError("Supply exactly one group ID per observed value")
    group_array=np.array([str(group) for group in group_array],dtype=object)
    if any(group not in order for group in group_array):
        raise ValueError("Every observed group must appear in group_order")
    if (values<edges[0]).any() or (values>edges[-1]).any():
        raise ValueError("Every observation must fall inside the supplied bin range")
    colors=base._colors(order,colors)
    counts=np.stack([np.histogram(values[group_array==group],bins=edges)[0] for group in order])
    totals=counts.sum(axis=0)
    fractions=np.divide(counts,totals[None,:],out=np.full(counts.shape,np.nan,dtype=float),
                         where=totals[None,:]>0)
    occupied=totals>0;bottom=np.zeros(int(occupied.sum()));containers=[]
    for name,color,row in zip(order,colors,fractions):
        container=ax.bar(edges[:-1][occupied],row[occupied],width=np.diff(edges)[occupied],
                          bottom=bottom,align="edge",color=color,edgecolor="white",
                          linewidth=.45,label=name)
        containers.append(container);bottom=bottom+row[occupied]
    ax.set(xlabel=xlabel,ylabel="Within-bin fraction",xlim=(edges[0],edges[-1]),ylim=(0,1))
    base.clean_axes(ax,None)
    return {"counts":counts,"totals":totals,"fractions":fractions,
            "bin_edges":edges.copy(),"group_order":order,"bars":containers,
            "denominator":"Total observation count in each numeric bin"}


def ordered_trajectory(ax, x, y, *, steps=None, color=None,
                        xlabel="State X", ylabel="State Y", arrows=2):
    """Connect state-plane checkpoints in supplied order, including folds in x.

    ``steps`` validates temporal order but never replaces or sorts coordinates.
    First/last checkpoints have distinct markers. Direction arrows, when enabled,
    use spaced nonzero segments without division by their length; repeated state
    coordinates remain in the line and cannot produce undefined arrow geometry.
    No interpolation, smoothing, regression, or inferred checkpoint is added.
    """
    x,y=_xy(x,y)
    if len(x)<2:raise ValueError("A trajectory needs at least two checkpoints")
    if steps is None:steps=np.arange(len(x))
    else:
        steps=_increasing(steps,"steps")
        base._same_length(x,steps)
    if not isinstance(arrows,(int,np.integer)) or isinstance(arrows,(bool,np.bool_)) or arrows<0:
        raise ValueError("arrows must be a nonnegative integer")
    color=_color(color)
    line,=ax.plot(x,y,color=color,lw=1.4,zorder=2)
    first=ax.scatter([x[0]],[y[0]],s=32,facecolors="white",edgecolors=color,
                      linewidths=1.1,marker="o",zorder=5,label="First checkpoint")
    last=ax.scatter([x[-1]],[y[-1]],s=28,color=color,marker="s",zorder=6,label="Final checkpoint")
    valid=np.flatnonzero((np.diff(x)!=0)|(np.diff(y)!=0))
    selected=valid[np.linspace(0,len(valid)-1,min(int(arrows),len(valid)),dtype=int)] if len(valid) and arrows else np.array([],dtype=int)
    annotations=[]
    for i in selected:
        annotations.append(ax.annotate("",xy=(x[i+1],y[i+1]),xytext=(x[i],y[i]),
                                        arrowprops={"arrowstyle":"-|>","color":color,"lw":1.0,"mutation_scale":8},
                                        zorder=3))
    ax.set(xlabel=xlabel,ylabel=ylabel);base.clean_axes(ax,"both")
    return {"line":line,"first":first,"last":last,"steps":np.array(steps,copy=True),
            "arrow_segments":selected,"arrows":annotations}


REGISTRY = {
    "ecdf": {"function": ecdf, "intent": "distribution", "required": ["samples"], "description": "Compare thresholds, tails, and cumulative observation mass without histogram bin choices."},
    "survival_step": {"function": survival_step, "intent": "time_to_event", "required": ["time", "survival"], "description": "Display externally estimated event-free probability and optional supplied intervals."},
    "raincloud": {"function": raincloud, "intent": "distribution", "required": ["samples", "labels"], "description": "Expose raw observations, median/IQR, and density together."},
    "ridgeline": {"function": ridgeline, "intent": "distribution_shift", "required": ["samples", "labels"], "description": "Read changing modes and tails across ordered conditions on a common scale."},
    "ranked_intervals": {"function": ranked_intervals, "intent": "subgroup_effect", "required": ["labels", "values", "lower", "upper"], "description": "Compare signed subgroup effects with supplied uncertainty and an explicit reference."},
    "dumbbell": {"function": dumbbell, "intent": "paired_change", "required": ["labels", "before", "after"], "description": "Connect two matched measurements per entity without losing identity."},
    "bland_altman": {"function": bland_altman, "intent": "agreement", "required": ["first", "second"], "description": "Distinguish agreement bias and spread from high correlation."},
    "residual_diagnostics": {"function": residual_diagnostics, "intent": "error_structure", "required": ["fitted", "residuals"], "description": "Reveal residual structure around a meaningful zero reference."},
    "quantile_fan": {"function": quantile_fan, "intent": "conditional_uncertainty", "required": ["x", "quantiles", "probabilities"], "description": "Show asymmetric conditional spread with a supplied median and nested quantiles."},
    "precision_recall": {"function": precision_recall, "intent": "operating_tradeoff", "required": ["recall", "precision"], "description": "Compare retrieval operating points, optionally against known prevalence."},
    "roc": {"function": roc, "intent": "operating_tradeoff", "required": ["false_positive_rate", "true_positive_rate"], "description": "Display sensitivity versus false alarms at supplied thresholds."},
    "risk_coverage": {"function": risk_coverage, "intent": "selective_prediction", "required": ["coverage", "risk"], "description": "Expose the cost in retained observations of reducing prediction risk."},
    "rank_trajectories": {"function": rank_trajectories, "intent": "ranking_stability", "required": ["stages", "ranks", "labels"], "description": "Trace which entities exchange rank across conditions while preserving ties."},
    "parallel_coordinates": {"function": parallel_coordinates, "intent": "multimetric_tradeoff", "required": ["values", "dimensions", "ranges", "labels"], "description": "Compare multi-objective profiles using explicit, documented original value ranges."},
    "ternary": {"function": ternary, "intent": "three_part_composition", "required": ["fractions", "labels"], "description": "Locate observations inside a three-part simplex without renormalizing them."},
    "transition_matrix": {"function": transition_matrix, "intent": "state_transition", "required": ["values", "labels", "normalization"], "description": "Separate raw transition exposure from conditional transition probability."},
    "mosaic_composition": {"function": mosaic_composition, "intent": "composition_exposure", "required": ["counts", "group_labels", "component_labels"], "description": "Use width for population size and height for conditional category composition."},
    "matrix_bubbles": {"function": matrix_bubbles, "intent": "signed_interaction", "required": ["values", "row_labels", "col_labels", "magnitude_max"], "description": "Use bubble area for magnitude and diverging hue for signed pairwise effects."},
    "signed_effects": {"function": signed_effects, "intent": "directional_change", "required": ["labels", "effects"], "description": "Compare positive and negative changes around an explicit zero reference."},
    "convergence_envelope": {"function": convergence_envelope, "intent": "training_stability", "required": ["steps", "runs"], "description": "Show individual training runs with pointwise median and IQR, not a fabricated confidence band."},
    "grouped_dot": {"function": grouped_dot, "intent": "categorical_comparison", "required": ["labels", "values", "series_labels"], "description": "Compare aligned category scores through position with less filled area than grouped bars."},
    "contour_response": {"function": contour_response, "intent": "two_factor_response", "required": ["x", "y", "response"], "description": "Reveal nonlinear joint effects across an actual two-control observation grid."},
    "robustness_profile": {"function": robustness_profile, "intent": "robustness", "required": ["severity", "scores", "labels"], "description": "Separate nominal quality from performance degradation as perturbations increase."},
    "cost_quality_frontier": {"function": cost_quality_frontier, "intent": "resource_tradeoff", "required": ["cost", "quality", "labels"], "description": "Identify measured non-dominated cost/quality alternatives using explicit optimization directions."},
    "quadrant_scatter": {"function": quadrant_scatter, "intent": "objective_conflict", "required": ["x", "y", "labels"], "description": "Locate simultaneous signed changes relative to two supplied reference values without assuming which quadrant is desirable."},
    "mean_delta": {"function": mean_delta, "intent": "baseline_dependent_change", "required": ["before", "after", "labels"], "description": "Ask which matched entities changed most and how that change relates to their supplied baseline."},
    "mirrored_histogram": {"function": mirrored_histogram, "intent": "paired_distribution", "required": ["first", "second", "bin_edges"], "description": "Compare raw observation counts on identical bins above and below a clearly labeled mirror baseline."},
    "mirror_stem": {"function": mirror_stem, "intent": "paired_spectrum", "required": ["x", "first", "second"], "description": "Compare absolute peak amplitudes at shared positions with a vertical mirror and no peak normalization."},
    "binned_group_composition": {"function": binned_group_composition, "intent": "conditional_composition", "required": ["values", "groups", "bin_edges", "group_order"], "description": "Align group fractions to the same numeric bins as a count histogram, with explicit per-bin observation denominators and blank empty bins."},
    "ordered_trajectory": {"function": ordered_trajectory, "intent": "state_plane_dynamics", "required": ["x", "y"], "description": "Trace supplied checkpoints through a state plane in temporal order, retaining loops, repeated states, explicit endpoints and optional direction arrows."},
}


def demo_data(kind, seed=0):
    """Return explicitly synthetic examples; never called by any plotting function.

    No result is transcribed from a paper. The caller must label demo exports as
    simulated. A local generator leaves global NumPy random state untouched.
    """
    if kind not in REGISTRY: raise ValueError(f"Unknown semantic panel {kind!r}")
    rng=np.random.default_rng(seed)
    labels=["Base", "Method A", "Method B"]
    x=np.linspace(0,1,12)
    if kind=="ecdf":return {"samples":rng.lognormal(0,.55,100),"xlabel":"Response time (simulated)"}
    if kind=="survival_step":return {"time":np.arange(9),"survival":np.exp(-np.arange(9)/6),"xlabel":"Time (simulated)"}
    if kind in ("raincloud","ridgeline"):
        return {"samples":[rng.normal(loc,scale,50) for loc,scale in [(0,1),(.6,.6),(1.1,.8)]],"labels":labels}
    if kind=="ranked_intervals":
        return {"labels":["Group A","Group B","Group C","Group D"],"values":[-.08,.18,.35,.1],"lower":[-.2,.04,.2,-.08],"upper":[.04,.32,.51,.28]}
    if kind=="dumbbell":return {"labels":["Task A","Task B","Task C","Task D"],"before":[.6,.7,.64,.74],"after":[.69,.74,.79,.71]}
    if kind=="bland_altman":
        first=rng.normal(3,1,70);return {"first":first,"second":first+rng.normal(.12,.3,70)}
    if kind=="residual_diagnostics":
        fitted=np.linspace(0,4,90);return {"fitted":fitted,"residuals":rng.normal(0,.1+.14*fitted)}
    if kind=="quantile_fan":
        median=1.2*x+.2*np.sin(6*x);spread=.15+.3*x
        return {"x":x,"quantiles":np.array([median-2*spread,median-spread,median,median+1.3*spread,median+2.6*spread]),"probabilities":[.05,.25,.5,.75,.95]}
    if kind=="precision_recall":return {"recall":x,"precision":.96-.48*x**2,"prevalence":.2}
    if kind=="roc":return {"false_positive_rate":x,"true_positive_rate":np.sqrt(x)}
    if kind=="risk_coverage":return {"coverage":np.linspace(.05,1,12),"risk":.025+.23*x**1.7}
    if kind=="rank_trajectories":return {"stages":["Clean","Mild","Moderate","Severe"],"ranks":[[1,2,3,3],[2,1,1,2],[3,3,2,1]],"labels":labels}
    if kind=="parallel_coordinates":return {"values":[[.75,80,8],[.82,55,13],[.85,95,11]],"dimensions":["Accuracy","Latency","Memory"],"ranges":[[.5,1],[0,100],[0,20]],"labels":labels}
    if kind=="ternary":return {"fractions":rng.dirichlet([2.5,4,2],60),"labels":["Correct","Uncertain","Error"]}
    if kind=="transition_matrix":return {"values":[[65,15,4],[12,45,9],[5,17,38]],"labels":["State A","State B","State C"],"normalization":"row"}
    if kind=="mosaic_composition":return {"counts":[[35,12,3],[45,18,12],[16,20,14]],"group_labels":["Group A","Group B","Group C"],"component_labels":["Correct","Uncertain","Error"]}
    if kind=="matrix_bubbles":return {"values":rng.uniform(-1,1,(4,5)),"row_labels":["Layer 1","Layer 2","Layer 3","Layer 4"],"col_labels":["A","B","C","D","E"],"magnitude_max":1}
    if kind=="signed_effects":return {"labels":["Component A","Component B","Component C","Component D"],"effects":[.12,-.08,.24,-.04]}
    if kind=="convergence_envelope":
        steps=np.linspace(0,1000,35);runs=np.array([np.exp(-steps/(220+30*i))+.04+rng.normal(0,.018,len(steps)) for i in range(6)])
        return {"steps":steps,"runs":runs}
    if kind=="grouped_dot":return {"labels":["Task A","Task B","Task C","Task D"],"values":[[.66,.73,.7,.76],[.72,.76,.79,.8],[.75,.81,.78,.84]],"series_labels":labels}
    if kind=="contour_response":
        xx=np.linspace(0,1,15);yy=np.linspace(0,1,12);a,b=np.meshgrid(xx,yy)
        return {"x":xx,"y":yy,"response":.7+.15*np.exp(-((a-.4)**2+(b-.65)**2)/.12)-.08*a*b}
    if kind=="robustness_profile":return {"severity":x,"scores":[.89-.31*x,.87-.17*x,.9-.24*x**1.5],"labels":labels}
    if kind=="cost_quality_frontier":return {"cost":[1,2,3,4,5,3.5],"quality":[.62,.71,.78,.76,.83,.72],"labels":["A","B","C","D","E","F"]}
    if kind=="quadrant_scatter":return {"x":[-.2,.1,.3,-.1,.15,.0],"y":[.18,.22,-.12,-.08,.05,.0],"labels":["A","B","C","D","E","F"]}
    if kind=="mean_delta":return {"before":[.45,.62,.71,.8,.86,.92],"after":[.61,.73,.77,.85,.87,.9],"labels":["A","B","C","D","E","F"]}
    if kind=="mirrored_histogram":
        return {"first":rng.beta(2,5,90),"second":rng.beta(4,3,110),"bin_edges":np.linspace(0,1,13),"xlabel":"Observed fraction"}
    if kind=="mirror_stem":return {"x":np.arange(1,13),"first":[0,2,7,3,0,1,4,9,2,0,3,1],"second":[1,1,5,2,0,3,8,4,2,1,0,2],"xlabel":"Shared spectral position"}
    if kind=="binned_group_composition":
        values=np.concatenate([rng.beta(2,5,50),rng.beta(5,2,40),rng.beta(3,3,30)])
        return {"values":values,"groups":["Group A"]*50+["Group B"]*40+["Group C"]*30,
                "bin_edges":np.linspace(0,1,9),"group_order":["Group A","Group B","Group C"],"xlabel":"Observed fraction"}
    if kind=="ordered_trajectory":
        return {"x":[.9,.65,.45,.5,.35,.22,.28,.15],"y":[.3,.4,.48,.6,.67,.69,.79,.86],
                "steps":[0,10,20,30,40,50,60,70],"xlabel":"Loss (simulated)","ylabel":"Accuracy (simulated)"}
    raise AssertionError("Registry entry lacks explicit synthetic demo data")
