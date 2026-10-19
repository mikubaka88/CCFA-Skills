#!/usr/bin/env python3
"""Data, comparison, and physical-size regressions for editable SVG recipes.

Run from any working directory. Tests use the standard library and keep SVGs
in memory; no figures or configuration are written by the suite.
"""

from __future__ import annotations

import copy
from pathlib import Path
import runpy
import unittest
from xml.etree import ElementTree as ET


PLOTS = runpy.run_path(str(Path(__file__).resolve().parents[1] / "resources/python/ccfa_plot_recipes.py"))
NS = {"s": "http://www.w3.org/2000/svg"}


def elements(svg: str, tag: str) -> list[ET.Element]:
    return ET.fromstring(svg).findall(f".//s:{tag}", NS)


def text(svg: str) -> str:
    return " ".join(element.text or "" for element in elements(svg, "text"))


class PlotRegressionTests(unittest.TestCase):
    def call(self, name: str, *args, **kwargs) -> str:
        svg = PLOTS[name](*args, **kwargs)
        ET.fromstring(svg)
        return svg

    def panels(self):
        return [
            {"title": "Cohort A", "entity": "method", "x": [0, 1, 2], "y": [1, 2, 1], "y_unit": "ms"},
            {"title": "Cohort B", "entity": "method", "x": [0, 1, 2], "y": [100, 200, 100], "y_unit": "ms"},
        ]

    def test_correlation_rejects_out_of_range_instead_of_clipping(self):
        for value in (-1.01, 1.7, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, r"finite|\[-1, 1\]"):
                self.call("correlation_heatmap", [[value]], ["A"], "")

    def test_matrix_shape_and_labels_are_validated(self):
        for matrix, row_labels, col_labels in (
            ([], [], []), ([[1]], ["A", "B"], ["X"]),
            ([[1], [2, 3]], ["A", "B"], ["X"]),
            ([[1, 2]], ["A"], ["X", "X"]), ([[1]], [""], ["X"]),
        ):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                self.call("heatmap_matrix", matrix, row_labels, col_labels, "")

    def test_heatmap_keeps_zero_and_negative_values(self):
        svg = self.call("heatmap_matrix", [[-2, 0, 2]], ["A"], ["X", "Y", "Z"], "", center=0)
        self.assertIn("-2", text(svg))
        self.assertIn("0", text(svg))
        self.assertIn("2", text(svg))

    def test_small_heatmap_values_are_not_printed_as_zero(self):
        svg = self.call("heatmap_matrix", [[0.01, 0.02, 0.04]], ["A"], ["X", "Y", "Z"], "", show_colorbar=False)
        numbers = [float(item.text) for item in elements(svg, "text") if item.text[0].isdigit()]
        self.assertEqual(numbers, [0.01, 0.02, 0.04])

    def test_shared_color_range_maps_equal_values_to_equal_colors(self):
        norm = PLOTS["ColorNorm"](0, 100)
        svgs = [self.call("heatmap_matrix", [values], ["A"], ["X", "Y"], "", norm=norm)
                for values in ([10, 20], [10, 100])]
        # Background precedes the first data cell.
        self.assertEqual(elements(svgs[0], "rect")[1].get("fill"), elements(svgs[1], "rect")[1].get("fill"))
        for svg in svgs:
            bar = next(g for g in elements(svg, "g") if "data-color-min" in g.attrib)
            self.assertEqual((bar.get("data-color-min"), bar.get("data-color-max")), ("0", "100"))

    def test_centered_normalization_preserves_midpoint(self):
        norm = PLOTS["ColorNorm"](-2, 8, 0)
        self.assertEqual([norm.position(v) for v in (-2, 0, 8)], [0, 0.5, 1])

    def test_constant_heatmap_does_not_divide_by_zero(self):
        svg = self.call("heatmap_matrix", [[3, 3]], ["A"], ["X", "Y"], "")
        self.assertEqual(elements(svg, "rect")[1].get("fill"), elements(svg, "rect")[2].get("fill"))

    def test_norm_rejects_conflicts_and_out_of_range_values(self):
        for kwargs in ({"vmin": 2, "vmax": 1}, {"vmin": 0, "vmax": 1},
                       {"vmin": 0, "vmax": 2, "center": 2},
                       {"norm": PLOTS["ColorNorm"](0, 3), "vmin": 0}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.call("heatmap_matrix", [[2]], ["A"], ["X"], "", **kwargs)

    def test_colorbar_uses_true_endpoints(self):
        svg = self.call("heatmap_matrix", [[0.000001, 1]], ["A"], ["X", "Y"], "", vmin=0.000001, vmax=1)
        self.assertIn("1e-06", text(svg))
        bar = next(g for g in elements(svg, "g") if "data-color-min" in g.attrib)
        rects = bar.findall("s:rect", NS)
        labels = bar.findall("s:text", NS)
        self.assertAlmostEqual(float(labels[1].get("x")), float(rects[-1].get("x")) + float(rects[-1].get("width")), places=1)

    def test_heatmap_can_hide_values_and_colorbar(self):
        svg = self.call("heatmap_matrix", [[42]], ["A"], ["X"], "", show_values=False, show_colorbar=False)
        self.assertNotIn("42", text(svg))
        self.assertEqual(elements(svg, "g"), [])

    def test_volcano_rejects_invalid_statistics_and_thresholds(self):
        for probability in (-0.01, 1.1, float("inf"), float("nan")):
            with self.subTest(probability=probability), self.assertRaises(ValueError):
                self.call("volcano_plot", [{"fc": 2, "p": probability}], "fc", "p", None, "")
        for kwargs in ({"p_threshold": 0}, {"p_threshold": 1.1}, {"fold_threshold": -1}, {"statistic": "fdr-ish"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.call("volcano_plot", [{"fc": 2, "p": 0.01}], "fc", "p", None, "", **kwargs)

    def test_volcano_zero_needs_explicit_display_floor(self):
        rows = [{"fc": 2, "p": 0}, {"fc": -2, "p": 1e-20}]
        original = copy.deepcopy(rows)
        with self.assertRaisesRegex(ValueError, "zero_floor"):
            self.call("volcano_plot", rows, "fc", "p", None, "")
        svg = self.call("volcano_plot", rows, "fc", "p", None, "", zero_floor=1e-30)
        self.assertIn("zero p value(s) shown at 1e-30", text(svg))
        self.assertIn("positive values unchanged", text(svg))
        self.assertEqual(rows, original)
        groups = [g for g in elements(svg, "g") if "data-statistic" in g.attrib]
        self.assertEqual(float(groups[0].get("data-statistic")), 0)
        self.assertEqual(float(groups[1].get("data-statistic")), 1e-20)

    def test_zero_floor_cannot_displace_positive_values(self):
        for floor in (-1, 0, 1e-5, float("nan")):
            with self.subTest(floor=floor), self.assertRaises(ValueError):
                self.call("volcano_plot", [{"fc": 2, "p": 0}, {"fc": 1, "p": 1e-10}], "fc", "p", None, "", zero_floor=floor)

    def test_extremely_small_positive_p_is_not_clipped(self):
        svg = self.call("volcano_plot", [{"fc": 2, "p": 1e-200}, {"fc": 2, "p": 1e-20}], "fc", "p", None, "")
        dots = elements(svg, "circle")
        self.assertLess(float(dots[0].get("cy")), float(dots[1].get("cy")))

    def test_volcano_statistic_labels_match_supplied_type(self):
        for statistic, label in (("p", "p"), ("adjusted_p", "adjusted p"), ("q", "q")):
            svg = self.call("volcano_plot", [{"fc": 0, "p": 1}], "fc", "p", None, "", statistic=statistic, p_threshold=1)
            self.assertIn(f"-log10 {label}", text(svg))
            self.assertIn(f"{label} <= 1", text(svg))

    def test_shared_axes_preserve_magnitude_difference(self):
        svg = self.call("small_multiple_lines", self.panels(), "")
        groups = [g for g in elements(svg, "g") if "data-panel" in g.attrib]
        self.assertEqual(groups[0].get("data-y-min"), groups[1].get("data-y-min"))
        self.assertEqual(groups[0].get("data-y-max"), groups[1].get("data-y-max"))
        y_ranges = []
        for g in groups:
            ys = [float(c.get("cy")) for c in g.findall("s:circle", NS)]
            y_ranges.append(max(ys) - min(ys))
        self.assertAlmostEqual(y_ranges[1] / y_ranges[0], 100, delta=1)

    def test_ticks_distinguish_small_values_and_close_large_values(self):
        for values in ([0.01, 0.02], [1000000000001, 1000000000002], [1.001, 1.002]):
            with self.subTest(values=values):
                svg = self.call("small_multiple_lines", [{"title": "A", "x": [0, 1], "y": values}], "")
                group = next(g for g in elements(svg, "g") if "data-panel" in g.attrib)
                y_ticks = [item for item in group.findall("s:text", NS) if item.get("text-anchor") == "end"][:3]
                numbers = [float(item.text) for item in y_ticks]
                self.assertEqual(len(set(numbers)), 3)
                self.assertTrue(all(value > 0 for value in numbers))
                lo, hi = float(group.get("data-y-min")), float(group.get("data-y-max"))
                for actual, expected in zip(numbers, [lo, (lo + hi) / 2, hi]):
                    self.assertAlmostEqual(actual, expected, delta=(hi - lo) / 2000)

    def test_shared_axes_use_identical_plot_areas_with_mixed_titles(self):
        panels = [
            {"title": "Named", "entity": "Method", "x": [0, 1], "y": [0, 100]},
            {"title": "", "entity": "Method", "x": [0, 1], "y": [0, 100]},
        ]
        svg = self.call("small_multiple_lines", panels, "")
        groups = [g for g in elements(svg, "g") if "data-panel" in g.attrib]
        positions = [[float(item.get("cy")) for item in g.findall("s:circle", NS)] for g in groups]
        self.assertEqual(positions[0], positions[1])
        # A unit label reserves the same headroom for both panels as a title.
        panels[0]["title"] = ""
        panels[0]["y_unit"] = "ms"
        svg = self.call("small_multiple_lines", panels, "")
        groups = [g for g in elements(svg, "g") if "data-panel" in g.attrib]
        positions = [[float(item.get("cy")) for item in g.findall("s:circle", NS)] for g in groups]
        self.assertEqual(positions[0], positions[1])

    def test_free_axes_are_explicit_and_labeled(self):
        svg = self.call("small_multiple_lines", self.panels(), "", share_x=False, share_y=False)
        self.assertIn("x: free; y: free", text(svg))
        groups = [g for g in elements(svg, "g") if "data-panel" in g.attrib]
        self.assertNotEqual(groups[0].get("data-y-max"), groups[1].get("data-y-max"))

    def test_different_units_require_explicit_free_axis(self):
        panels = self.panels()
        panels[1]["y_unit"] = "accuracy"
        with self.assertRaisesRegex(ValueError, "different y units"):
            self.call("small_multiple_lines", panels, "")
        self.call("small_multiple_lines", panels, "", share_y=False)

    def test_panel_xy_lengths_cannot_silently_truncate(self):
        panels = self.panels()
        panels[0]["y"] = [1]
        with self.assertRaisesRegex(ValueError, "paired observations"):
            self.call("small_multiple_lines", panels, "")

    def test_entity_colors_persist_across_reordering_and_calls(self):
        panels = self.panels()
        panels[1]["entity"] = "baseline"
        colors = {"method": "#123456", "baseline": "#abcdef"}
        for panel_list in (panels, list(reversed(panels)), panels[:1]):
            svg = self.call("small_multiple_lines", panel_list, "", entity_colors=colors)
            for group in elements(svg, "g"):
                if "data-entity" in group.attrib:
                    self.assertEqual(group.find("s:polyline", NS).get("stroke"), colors[group.get("data-entity")])
        with self.assertRaisesRegex(ValueError, "missing entities"):
            self.call("small_multiple_lines", panels, "", entity_colors={"method": "#123456"})

    def test_same_entity_uses_same_default_color(self):
        svg = self.call("small_multiple_lines", self.panels(), "")
        self.assertEqual(elements(svg, "polyline")[0].get("stroke"), elements(svg, "polyline")[1].get("stroke"))

    def test_entity_legend_is_deduplicated_and_can_be_shared_externally(self):
        svg = self.call("small_multiple_lines", self.panels(), "")
        self.assertEqual([t.text for t in elements(svg, "text")].count("method"), 1)
        svg = self.call("small_multiple_lines", self.panels(), "", show_legend=False)
        self.assertNotIn("method", text(svg))

    def test_panel_title_can_be_omitted_with_an_entity_id(self):
        svg = self.call("small_multiple_lines", [{"title": "", "entity": "Method", "x": [0, 1], "y": [1, 2]}], "")
        self.assertIn("Method", text(svg))
        self.assertTrue(all(item.text for item in elements(svg, "text")))
        with self.assertRaisesRegex(ValueError, "entity or title"):
            self.call("small_multiple_lines", [{"title": "", "x": [0, 1], "y": [1, 2]}], "")

    def test_nonnumeric_shapes_and_overflow_ranges_are_rejected(self):
        for values in (123, "123", [float("nan")]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                self.call("small_multiple_lines", [{"title": "A", "x": [0], "y": values}], "")
        with self.assertRaisesRegex(ValueError, "range"):
            PLOTS["ColorNorm"](-1e308, 1e308)

    def test_physical_width_and_minimum_font_points(self):
        theme = PLOTS["Theme"](width=900, height=560, paper_width_in=7, min_font_pt=9)
        svg = self.call("heatmap_matrix", [[1, 2]], ["A"], ["X", "Y"], "Paper figure", theme=theme)
        root = ET.fromstring(svg)
        self.assertEqual(root.get("width"), "7in")
        self.assertAlmostEqual(float(root.get("height")[:-2]), 7 * 560 / 900, places=4)
        for item in elements(svg, "text"):
            points = float(item.get("font-size")) * 7 * 72 / 900
            self.assertGreaterEqual(points + 1e-6, 9)

    def test_legacy_theme_dimensions_are_unchanged(self):
        svg = self.call("heatmap_matrix", [[1]], ["A"], ["X"], "Legacy", theme=PLOTS["Theme"](width=900, height=560))
        self.assertEqual(ET.fromstring(svg).get("width"), "900")
        self.assertIn("12.000000", [item.get("font-size") for item in elements(svg, "text")])

    def test_invalid_theme_and_palette_are_actionable(self):
        for kwargs in ({"paper_width_in": 0}, {"min_font_pt": -1}, {"width": float("nan")}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                PLOTS["Theme"](**kwargs)
        with self.assertRaisesRegex(ValueError, "palette"):
            self.call("heatmap_matrix", [[1]], ["A"], ["X"], "", palette=[])

    def test_negative_bar_values_have_positive_geometry(self):
        svg = self.call("grouped_bar_chart", [{"group": "A", "x": -2, "y": 3}], "group", ["x", "y"], "")
        bars = [r for r in elements(svg, "rect") if r.get("opacity") == "0.920"]
        self.assertEqual(len(bars), 2)
        self.assertTrue(all(float(bar.get("height")) > 0 for bar in bars))
        self.assertAlmostEqual(float(bars[1].get("y")) + float(bars[1].get("height")), float(bars[0].get("y")), places=1)

    def test_zero_bars_and_negative_lollipops_remain_valid(self):
        self.call("grouped_bar_chart", [{"group": "A", "x": 0}], "group", ["x"], "")
        self.assertIn("-2", text(self.call("lollipop_rank", [{"label": "A", "x": -2}], "x", "label", "")))

    def test_donut_rejects_negative_and_zero_total(self):
        for values in ([-1, 2], [0, 0]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                self.call("donut_chart", [{"label": str(i), "x": v} for i, v in enumerate(values)], "x", "label", "")

    def test_single_donut_category_is_full_circle(self):
        svg = self.call("donut_chart", [{"label": "A", "x": 0.5}, {"label": "B", "x": 0}], "x", "label", "")
        ring = next(c for c in elements(svg, "circle") if c.get("fill") == "none")
        self.assertGreater(float(ring.get("stroke-width")), 0)
        self.assertIn("0.50", text(svg))

    def test_radial_rejects_out_of_range_instead_of_clipping(self):
        for value, maximum in ((1.7, 1), (-1, 1), (1, 0)):
            with self.subTest(value=value, maximum=maximum), self.assertRaises(ValueError):
                self.call("radial_scorecard", [{"label": name, "x": value} for name in "ABC"], "x", "label", "", max_value=maximum)

    def test_all_legacy_recipe_calls_and_unicode(self):
        rows = [{"name": "中文 & A", "value": 1, "after": 2}, {"name": "繁體 < B", "value": 2, "after": 3}]
        calls = [
            ("lollipop_rank", (rows, "value", "name", "图")),
            ("slopegraph", (rows, "value", "after", "name", "图", "前", "后")),
            ("heatmap_matrix", ([[1, 2]], ["中文"], ["甲", "乙"], "图")),
            ("donut_chart", (rows, "value", "name", "图")),
            ("grouped_bar_chart", (rows, "name", ["value", "after"], "图")),
            ("volcano_plot", ([{"fc": 2, "p": .01, "name": "基因"}], "fc", "p", "name", "图")),
            ("correlation_heatmap", ([[1, -.2], [-.2, 1]], ["甲", "乙"], "图")),
            ("ridgeline_density", ({"中文": [1, 2, 3]}, "图")),
            ("small_multiple_lines", ([{"x": [0, 1], "y": [1, 2], "title": "中文"}], "图")),
            ("radial_scorecard", ([{"name": n, "value": .5} for n in "甲乙丙"], "value", "name", "图")),
        ]
        self.assertEqual(len(calls), len(PLOTS["recipe_catalog"]()))
        for name, args in calls:
            with self.subTest(recipe=name):
                self.assertIn("图", text(self.call(name, *args)))

    def test_missing_and_nonfinite_inputs_fail_before_render(self):
        for name, args in (
            ("lollipop_rank", ([], "x", "label", "")),
            ("slopegraph", ([{"label": "A", "x": 1}], "x", "y", "label", "", "L", "R")),
            ("ridgeline_density", ({"A": []}, "")),
            ("small_multiple_lines", ([{"title": "A", "x": [0], "y": [float("nan")]}], "")),
            ("grouped_bar_chart", ([{"label": "A", "x": float("inf")}], "label", ["x"], "")),
        ):
            with self.subTest(recipe=name), self.assertRaises(ValueError):
                self.call(name, *args)


if __name__ == "__main__":
    unittest.main(verbosity=2)
