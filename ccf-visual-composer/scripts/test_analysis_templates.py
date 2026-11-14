#!/usr/bin/env python3
"""Meaningful real-data, domain, reproducibility and CLI template regressions."""
from __future__ import annotations

import copy
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ccf-visual-composer/resources/python"))
import ccfa_analysis_templates as templates

BUILD = ROOT / "ccfa-workfiles/skill-maintenance/analytical-figures/build"


class AnalysisTemplateTests(unittest.TestCase):
    def test_mixed_template_keeps_supplied_raster_without_rebuilding_its_objects(self):
        data = self.data("mechanism_overview")
        pixels = np.arange(36, dtype=np.uint8).reshape(3, 4, 3)
        image = self.folder / "approved-method.png"
        plt.imsave(image, pixels)
        data["mechanism"] = {"image": str(image)}
        original = image.read_bytes()
        fig = self.render("mechanism_overview", data)
        axes = next(ax for ax in fig.axes if ax.images)
        np.testing.assert_array_equal(axes.images[0].get_array(), plt.imread(image))
        self.assertEqual(len(axes.patches), 0)
        self.assertEqual(image.read_bytes(), original)

    def test_stage_blueprint_cannot_reactivate_mixed_template_diagram_construction(self):
        data = self.data("mechanism_overview")
        data["mechanism"] = {"stages": ["Input", "Encoder", "Output"], "note": "old blueprint"}
        with self.assertRaisesRegex(ValueError, "approved PNG"):
            self.render("mechanism_overview", data)

    def test_pair_default_is_compact_but_explicit_height_is_not_scaled_twice(self):
        data=copy.deepcopy(self.examples["sensitivity_dynamics"]);data["panel_pair"]="sensitivity"
        default=templates.render_template("sensitivity_dynamics",data)
        explicit=templates.render_template("sensitivity_dynamics",data,height_mm=84)
        self.assertAlmostEqual(default.get_figheight()*25.4,142*.56)
        self.assertAlmostEqual(explicit.get_figheight()*25.4,84)
        plt.close(default);plt.close(explicit)

    def test_aggregate_corridor_uses_counts_and_explicit_weight_units(self):
        fig,ax=plt.subplots();ax.set_xlim(0,40);ax.set_ylim(.01,10);ax.set_yscale("log")
        block={"x":[1,30],"y":[.05,1],"counts":[3,7],
               "corridor":{"x_max":20,"y_max":.1,"weights":[2,1],"weight_kind":"per_state"}}
        result=templates._density_corridor(ax,block)
        self.assertAlmostEqual(result["state_share"],30)
        self.assertAlmostEqual(result["mass_share"],100*6/13)
        block["corridor"].update(weights=[6,7],weight_kind="bin_total")
        self.assertAlmostEqual(templates._density_corridor(ax,block)["mass_share"],100*6/13)
        block["corridor"].pop("weight_kind")
        with self.assertRaisesRegex(ValueError,"weight_kind"):
            templates._density_corridor(ax,block)
        plt.close(fig)

    @classmethod
    def setUpClass(cls):
        cls.examples = templates.demo_data(17)

    def setUp(self):
        BUILD.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="template-test-", dir=BUILD)
        self.folder = Path(self.temporary.name).resolve()
        self.assertEqual(self.folder.parent, BUILD.resolve())

    def tearDown(self):
        plt.close("all")
        self.temporary.cleanup()

    def data(self, name):
        data = copy.deepcopy(self.examples[name])
        data.pop("_meta", None)
        return data

    def render(self, name, data=None):
        return templates.render_template(name, self.data(name) if data is None else data)

    def test_all_nine_templates_preserve_every_input_value_and_label(self):
        self.assertEqual(len(templates.CATALOG), 9)
        for name in templates.CATALOG:
            with self.subTest(template=name):
                data = self.data(name)
                before = json.dumps(data, sort_keys=True, allow_nan=False)
                fig = self.render(name, data)
                self.assertEqual(json.dumps(data, sort_keys=True, allow_nan=False), before)
                self.assertAlmostEqual(fig.get_figwidth() * 25.4, 183)
                self.assertFalse(any("Simulated data" in text.get_text() for text in fig.texts))
                plt.close(fig)

    def test_real_renderer_never_calls_demo_generator_or_fills_missing_data(self):
        data = self.data("benchmark_atlas")
        data["performance"]["mean"] = [-2, 0, 2, 4]
        for key in ("runs", "lower", "upper", "uncertainty"):
            data["performance"].pop(key, None)
        with patch.object(templates, "demo_data", side_effect=AssertionError("No synthetic fallback")):
            fig = self.render("benchmark_atlas", data)
            ax = next(a for a in fig.axes if a.get_title(loc="left") == "Repeated runs")
            observed = [float(c.get_offsets()[0, 0]) for c in ax.collections]
            self.assertEqual(observed, [-2, 0, 2, 4])
            data.pop("tradeoff")
            with self.assertRaisesRegex(ValueError, "tradeoff"):
                self.render("benchmark_atlas", data)

    def test_demo_generation_is_seeded_and_keeps_global_rng_unchanged(self):
        before = np.random.get_state()
        first = templates.demo_data(9)
        second = templates.demo_data(9)
        third = templates.demo_data(10)
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)
        self.assertTrue(all(d["_meta"]["synthetic"] for d in first.values()))
        after = np.random.get_state()
        self.assertEqual(before[0], after[0])
        np.testing.assert_array_equal(before[1], after[1])
        self.assertEqual(before[2:], after[2:])

    def test_demo_seed_changes_do_not_make_fixed_color_ranges_hide_observations(self):
        for seed in (2, 3, 13):
            with self.subTest(seed=seed):
                data = templates.demo_data(seed)["mechanism_overview"]
                fig = self.render("mechanism_overview", data)
                self.assertTrue(any("Simulated data" in text.get_text() for text in fig.texts))
                plt.close(fig)

    def test_demo_paired_intervals_are_derived_from_the_same_observations(self):
        block = self.examples["paired_effects"]
        before, after = np.asarray(block["paired"]["values"])
        diff = np.asarray(block["differences"])
        np.testing.assert_allclose(after - before, diff)
        self.assertAlmostEqual(float(diff.mean()), block["subgroups"]["mean"][0])
        self.assertLess(block["subgroups"]["lower"][0], diff.mean())
        self.assertGreater(block["subgroups"]["upper"][0], diff.mean())

    def test_paired_differences_cannot_disagree_with_within_subject_changes(self):
        data = self.data("paired_effects")
        data["differences"][0] += 20
        with self.assertRaises(ValueError): self.render("paired_effects", data)
        data = self.data("paired_effects")
        data["differences"] = data["differences"][:-1]
        with self.assertRaises(ValueError): self.render("paired_effects", data)

    def test_two_group_change_template_rejects_an_ambiguous_third_group(self):
        data = self.data("paired_effects")
        data["methods"].append("Followup")
        data["paired"]["labels"].append("Followup")
        data["paired"]["values"].append(data["paired"]["values"][-1][:])
        with self.assertRaises(ValueError): self.render("paired_effects", data)

    def test_difference_panel_names_the_actual_supplied_contrast(self):
        data = self.data("paired_effects")
        data["methods"] = ["Control", "Treatment"]
        data["paired"]["labels"] = ["Control", "Treatment"]
        for series, method in zip(data["response_curve"]["series"], data["methods"]):
            series["method"] = method
        fig = self.render("paired_effects", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Paired differences")
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], ["Treatment − Control"])

    def test_repeated_run_mean_cannot_conflict_with_plotted_runs(self):
        data = self.data("benchmark_atlas")
        data["performance"]["mean"][0] += 0.5
        # The altered estimate still lies inside the supplied interval, so this
        # specifically catches inconsistent summary and raw observations.
        with self.assertRaises(ValueError): self.render("benchmark_atlas", data)

    def test_empty_required_series_and_observation_lists_are_rejected(self):
        data = self.data("scaling_robustness")
        data["panels"][0]["series"] = []
        with self.assertRaises(ValueError): self.render("scaling_robustness", data)
        for key in ("calibration", "errors"):
            with self.subTest(block=key):
                data = self.data("calibration_errors"); data[key] = []
                with self.assertRaises(ValueError): self.render("calibration_errors", data)

    def test_uncertainty_pair_is_optional_but_half_empty_or_invalid_pairs_fail(self):
        data = self.data("scaling_robustness")
        for block in data["panels"]:
            for series in block["series"]:
                series.pop("lower"); series.pop("upper")
        fig = self.render("scaling_robustness", data)
        self.assertFalse(any(ax.collections for ax in fig.axes))
        for low, high in (([], []), (None, []), ([0], [1])):
            invalid = copy.deepcopy(data)
            invalid["panels"][0]["series"][0].update(lower=low, upper=high)
            with self.subTest(lower=low, upper=high), self.assertRaises(ValueError):
                self.render("scaling_robustness", invalid)

    def test_curves_cannot_hide_outlying_uncertainty_or_use_invalid_log_x(self):
        data = self.data("scaling_robustness")
        block = data["panels"][0]
        lows = [min(s["y"]) for s in block["series"]]
        highs = [max(s["y"]) for s in block["series"]]
        block["ylim"] = [min(lows), max(highs)]
        with self.assertRaisesRegex(ValueError, "hide"):
            self.render("scaling_robustness", data)
        data = self.data("scaling_robustness")
        data["panels"][0]["xscale"] = "log"
        data["panels"][0]["x"][0] = 0
        with self.assertRaises(ValueError): self.render("scaling_robustness", data)

    def test_calibration_confidence_histogram_respects_probability_and_count_domains(self):
        for field, values in (("edges", [-0.1, 0.125, .25, .375, .5, .625, .75, .875, 1]),
                              ("edges", [0, .125, .25, .375, .5, .625, .75, .875, 1.1]),
                              ("counts", [0.5] * 8)):
            data = self.data("calibration_errors"); data["confidence_histogram"][field] = values
            with self.subTest(field=field, values=values), self.assertRaises(ValueError):
                self.render("calibration_errors", data)

    def test_failure_and_confusion_sample_counts_cannot_be_negative_or_fractional(self):
        for value in (-1, 0.5):
            with self.subTest(value=value):
                data = self.data("calibration_errors"); data["failure_counts"]["counts"][0] = value
                with self.assertRaises(ValueError): self.render("calibration_errors", data)
                data = self.data("calibration_errors"); data["confusion"]["values"][0][0] = value
                with self.assertRaises(ValueError): self.render("calibration_errors", data)

    def test_pearson_range_cannot_be_bypassed_by_changing_color_limits(self):
        data = self.data("representation_diagnostics")
        block = data["correlation"]
        block["values"][0][1] = block["values"][1][0] = 1.5
        block.update(vmin=-2, vmax=2)
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_correlation_identity_and_symmetry_are_checked_at_the_template_boundary(self):
        data = self.data("representation_diagnostics")
        data["correlation"]["values"][0][1] = 0.9
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)
        data = self.data("representation_diagnostics")
        data["correlation"]["columns"][0] = "Unknown feature"
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_attention_weights_cannot_be_negative_even_with_a_diverging_palette(self):
        data = self.data("representation_diagnostics")
        block = data["attention"]; block["values"][0][0] = -0.1
        block.update(vmin=-1, vmax=1, cmap="RdBu_r")
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_more_embedding_groups_than_palette_colors_keep_all_group_ids(self):
        data = self.data("representation_diagnostics")
        ids = [f"Group {i}" for i in range(len(templates.PALETTES["tol_muted"]) + 1)]
        data["embedding"] = {"coordinates": [[i, i % 3] for i in range(len(ids))],
                             "groups": ids, "order": ids}
        fig = self.render("representation_diagnostics", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Representation geometry")
        self.assertEqual([collection.get_label() for collection in ax.collections], ids)

    def test_missing_heatmap_observations_remain_missing_and_do_not_change_source(self):
        data = self.data("benchmark_atlas")
        data["benchmark"]["values"][0][0] = float("nan")
        fig = self.render("benchmark_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Cross-task benchmark")
        self.assertEqual(np.ma.count_masked(ax.collections[0].get_array()), 1)
        self.assertTrue(np.isnan(data["benchmark"]["values"][0][0]))
        self.assertIn("×", [text.get_text() for text in ax.texts])

    def test_pareto_template_keeps_supplied_directions_and_excludes_dominated_points(self):
        data = self.data("benchmark_atlas")
        block = data["tradeoff"]
        block.update(x=[0, 0, 1, 1], y=[0, 1, 0, 1], x_direction="max", y_direction="min")
        fig = self.render("benchmark_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Accuracy versus cost")
        line = next(line for line in ax.lines if line.get_label() == "Pareto frontier")
        np.testing.assert_array_equal(line.get_xdata(), [1])
        np.testing.assert_array_equal(line.get_ydata(), [0])
        np.testing.assert_array_equal(ax.collections[0].get_offsets(), np.column_stack([block["x"], block["y"]]))

    def test_biological_template_forwards_explicit_zero_probability_display_floor(self):
        data = self.data("biological_atlas")
        block = data["volcano"]; block["probability"][0] = 0
        positive = np.asarray(block["probability"])[np.asarray(block["probability"]) > 0]
        block["zero_floor"] = float(positive.min() / 10)
        fig = self.render("biological_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Effect-size screening")
        self.assertTrue(any("Zero q displayed" in text.get_text() for text in ax.texts))
        self.assertEqual(block["probability"][0], 0)

    def test_invalid_data_reports_error_without_leaking_figures(self):
        for name, data in (("benchmark_atlas", {}), ("benchmark_atlas", {"methods": ["A"]})):
            before = set(plt.get_fignums())
            with self.subTest(data=data), self.assertRaises(ValueError): self.render(name, data)
            self.assertEqual(set(plt.get_fignums()), before)

    def test_real_cli_exports_are_editable_and_preserve_the_exact_source_file(self):
        data = self.data("paired_effects")
        source = self.folder / "observations.json"
        source.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        original = source.read_bytes()
        out = self.folder / "figures-task"
        with contextlib.redirect_stdout(io.StringIO()):
            code = templates.main(["--data", str(source), "--template", "paired_effects",
                                   "--out", str(out), "--formats", "svg"])
        self.assertEqual(code, 0); self.assertEqual(source.read_bytes(), original)
        manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["synthetic"])
        self.assertIsNone(manifest["seed"])
        self.assertFalse((out / "source/demo-data.json").exists())
        svg = ET.parse(out / manifest["figures"]["paired_effects"]["exports"]["svg"])
        self.assertTrue(svg.findall(".//{http://www.w3.org/2000/svg}text"))

    def test_cli_never_overwrites_input_named_like_the_output_manifest(self):
        out = self.folder / "collision-task"; out.mkdir()
        source = out / "manifest.json"
        source.write_text(json.dumps(self.data("paired_effects")), encoding="utf-8")
        original = source.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()), self.assertRaises((ValueError, SystemExit)):
            templates.main(["--data", str(source), "--template", "paired_effects", "--out", str(out), "--formats", "svg"])
        self.assertEqual(source.read_bytes(), original)

    def test_cli_requires_explicit_real_or_demo_mode(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            templates.main(["--out", str(self.folder)])
        self.assertEqual(list(self.folder.iterdir()), [])

    def test_four_panel_reference_aligns_data_rectangles_with_dedicated_colorbar_column(self):
        fig = self.render("sensitivity_dynamics")
        fig.canvas.draw()
        self.assertEqual(len(fig.axes), 5)
        density, colorbar, quantiles, dynamics, categories = fig.axes
        for top, bottom in ((density, dynamics), (quantiles, categories)):
            self.assertAlmostEqual(top.get_position().x0, bottom.get_position().x0, places=8)
            self.assertAlmostEqual(top.get_position().x1, bottom.get_position().x1, places=8)
        self.assertGreater(colorbar.get_position().x0, density.get_position().x1)
        self.assertLess(colorbar.get_position().x1, quantiles.get_position().x0)

    def test_default_cli_is_png_only_without_editable_exports(self):
        out = self.folder / "ordinary-default"
        with contextlib.redirect_stdout(io.StringIO()):
            code = templates.main(["--demo", "paired_effects", "--out", str(out)])
        self.assertEqual(code, 0)
        self.assertTrue((out / "figures" / "paired_effects.png").is_file())
        self.assertEqual(list(out.rglob("*.svg")), [])
        self.assertEqual(list(out.rglob("*.pdf")), [])

    def test_default_reference_examples_exercise_complete_native_encodings(self):
        import ccfa_figure_library as library
        for example_id, pair in (("reference:sensitivity-pair", "sensitivity"),
                                 ("reference:dynamics-pair", "dynamics")):
            with self.subTest(example=example_id):
                spec = library.example_spec(example_id, demo=True)
                before = json.dumps(spec, sort_keys=True)
                fig = library.compose(spec)
                data, details = spec["data"], fig._ccfa_reference_details
                self.assertEqual(data["panel_pair"], pair)
                if pair == "sensitivity":
                    density = data["density"]
                    self.assertEqual(density["yscale"], "log")
                    self.assertEqual(density["count_range"], [1, 1000])
                    self.assertEqual((density["corridor"]["x_max"], density["corridor"]["y_max"]), (20, .1))
                    mask = (np.asarray(density["x"]) < 20) & (np.asarray(density["y"]) < .1)
                    weights = np.asarray(density["corridor"]["weights"])
                    self.assertAlmostEqual(details["corridor"]["state_share"], 100*mask.mean())
                    self.assertAlmostEqual(details["corridor"]["mass_share"], 100*weights[mask].sum()/weights.sum())
                    self.assertEqual(details["quantiles"]["summary_mode"], "median_p90")
                    self.assertEqual(details["quantiles"]["quantile_line"].get_marker(), "D")
                    np.testing.assert_allclose(details["quantiles"]["quantiles"], [.119, .319, .602, .817])
                    self.assertEqual(len(details["quantiles"]["annotations"]), 4)
                else:
                    near = next(line for line in fig.axes[0].lines if line.get_label() == data["methods"][2])
                    self.assertEqual((near.get_xdata()[0], near.get_linestyle(), near.get_marker()), (4, "--", "s"))
                    self.assertEqual(data["categories"]["bar_style"], "outlined")
                    self.assertEqual(len(details["categories"]["bars"]), 10)
                    self.assertEqual(len(details["categories"]["bands"]), 2)
                    self.assertEqual(len(details["categories"]["annotations"]), 14)
                self.assertEqual(json.dumps(spec, sort_keys=True), before)
                plt.close(fig)

    def test_reference_corridor_and_quantile_elements_follow_supplied_data(self):
        data = self.data("sensitivity_dynamics")
        data["panel_pair"] = "sensitivity"
        density = data["density"]
        density.pop("threshold", None)
        density.update(x=[0, 10, 30, 40], y=[.02, .2, .03, .4], xlim=[0, 60], ylim=[.01, 1],
                       count_range=[1, 1000], colorbar_ticks=[1, 10, 100, 1000],
                       corridor={"x_max": 20, "y_max": .1, "weights": [3, 1, 2, 4], "label": "Corridor"})
        data["sensitivity"].pop("samples")
        data["sensitivity"].update(labels=["Low", "High"], annotate=True,
            summary={"median": [.02, .1], "p90": [.08, .3], "p95": [.119, .319], "p99": [.2, .6]})
        before = json.dumps(data, sort_keys=True)
        fig = self.render("sensitivity_dynamics", data)
        details = fig._ccfa_reference_details
        self.assertEqual(details["corridor"]["state_share"], 25)
        self.assertEqual(details["corridor"]["mass_share"], 30)
        self.assertEqual(details["corridor"]["annotation"].get_text(), "25.0% of states\n30.0% of sensitivity mass")
        density_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "State-space exposure")
        self.assertEqual(density_ax.get_yscale(), "log")
        self.assertEqual(density_ax.collections[0].norm.vmax, 1000)
        self.assertEqual(details["corridor"]["region"].get_width(), 20)
        np.testing.assert_allclose(details["quantiles"]["quantiles"], [.119, .319])
        self.assertEqual(json.dumps(data, sort_keys=True), before)
        density["corridor"].pop("weights")
        without_weights = self.render("sensitivity_dynamics", data)
        self.assertIsNone(without_weights._ccfa_reference_details["corridor"]["mass_share"])
        self.assertNotIn("sensitivity mass", without_weights._ccfa_reference_details["corridor"]["annotation"].get_text())

    def test_reference_bounds_and_mass_require_actual_valid_inputs(self):
        data = self.data("sensitivity_dynamics")
        data["panel_pair"] = "sensitivity"
        data["density"].update(x=[0, 10, 30, 40], y=[.02, .2, .03, .4], xlim=[0, 60], ylim=[.01, 1])
        for weights in ([1], [0, 0, 0, 0], [1, -1, 1, 1]):
            data["density"]["corridor"] = {"x_max": 20, "y_max": .1, "weights": weights}
            with self.subTest(weights=weights), self.assertRaises(ValueError):
                self.render("sensitivity_dynamics", data)
        data["density"].pop("corridor")
        data["density"]["xlim"] = [0, 20]
        with self.assertRaisesRegex(ValueError, "hide"):
            self.render("sensitivity_dynamics", data)

    def test_reference_dynamics_markers_bands_and_outlined_labels_are_optional(self):
        data = self.data("sensitivity_dynamics")
        data["panel_pair"] = "dynamics"
        data["dynamics"]["series"][2].update(marker="s", linestyle="--")
        partial = data["dynamics"]["series"][2]
        partial["x"] = data["dynamics"]["x"][2:]
        data["dynamics"]["title"] = "Regime evolution"
        categories = data["categories"]
        categories.update(bar_style="outlined", bar_labels=True, ylim=[0, 110], yticks=[0, 25, 50, 75, 100], title="Variation across edits")
        for field in ("lower", "upper", "annotate"):
            categories["series"][1].pop(field, None)
        series = categories["series"][0]
        series.update(lower=[v-2 for v in series["values"]], upper=[v+2 for v in series["values"]], annotate=[1, 4])
        fig = self.render("sensitivity_dynamics", data)
        dynamics_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "Regime evolution")
        green = next(line for line in dynamics_ax.lines if line.get_label() == data["methods"][2])
        self.assertEqual((green.get_linestyle(), green.get_marker()), ("--", "s"))
        self.assertEqual(green.get_xdata()[0], 4)
        self.assertEqual(len(green.get_xdata()), len(partial["y"]))
        categories_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "Variation across edits")
        self.assertEqual(len(categories_ax.collections), 1)
        self.assertEqual(len(categories_ax.texts), 1+len(categories["bars"])+2)
        self.assertEqual(categories_ax.patches[0].get_edgecolor()[3], 1)
        self.assertLess(categories_ax.patches[0].get_facecolor()[3], .2)

    def test_sensitivity_summary_and_threshold_share_come_from_the_supplied_observations(self):
        data = self.data("sensitivity_dynamics")
        data["density"].pop("corridor", None)
        data["density"].update(x=[0, 1, 2, 3], y=[.1, .2, .25, .5], threshold=.25)
        data["sensitivity"].update(samples=[[0, 10], [-5, -1, 3]], labels=["Low", "High"], quantile=.95)
        data["sensitivity"].pop("ylim", None)
        before = copy.deepcopy(data)
        fig = self.render("sensitivity_dynamics", data)
        density_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "State-space exposure")
        self.assertEqual(float(density_ax.collections[0].get_array().sum()), 4)
        self.assertTrue(any("75.0% at or below 0.25" == text.get_text() for text in density_ax.texts))
        sensitivity_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "Perturbation by group")
        quantile_line = next(line for line in sensitivity_ax.lines if "percentile" in line.get_label())
        np.testing.assert_allclose(quantile_line.get_ydata(), [9.5, 2.6])
        self.assertEqual(data, before)

    def test_each_sensitivity_pair_has_two_main_axes_and_needs_only_its_own_blocks(self):
        full = self.data("sensitivity_dynamics")
        for pair, blocks in (("sensitivity", ("density", "sensitivity")),
                             ("dynamics", ("dynamics", "categories"))):
            with self.subTest(pair=pair):
                data = {"methods": full["methods"][:], "panel_pair": pair,
                        **{key: copy.deepcopy(full[key]) for key in blocks}}
                for key, title in (("dynamics", "Regime evolution"), ("categories", "Variation across edits")):
                    if key in data:
                        data[key]["title"] = title
                before = copy.deepcopy(data)
                fig = self.render("sensitivity_dynamics", data)
                main_axes = [ax for ax in fig.axes if ax.get_title(loc="left")]
                self.assertEqual(len(main_axes), 2)
                self.assertEqual(len(fig.axes), 3 if pair == "sensitivity" else 2)
                self.assertEqual(data, before)
                plt.close(fig)

    def test_sensitivity_domain_checks_do_not_hide_percentage_intervals_or_invalid_thresholds(self):
        data = self.data("sensitivity_dynamics")
        series = data["dynamics"]["series"][0]
        series["lower"] = [value - 1 for value in series["y"]]
        series["upper"] = [value + 1 for value in series["y"]]
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)
        data = self.data("sensitivity_dynamics"); data["categories"]["bars"][0] = -1
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)
        data = self.data("sensitivity_dynamics"); data["density"]["threshold"] = 0
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
