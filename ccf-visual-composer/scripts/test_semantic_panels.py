#!/usr/bin/env python3
"""Scientific semantics and composability checks for the optional panel library."""
from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
import unittest
from xml.etree import ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ccf-visual-composer/resources/python"))
import ccfa_analysis_panels as base
import ccfa_semantic_panels as panels

BUILD = ROOT / "ccfa-workfiles/skill-maintenance/semantic-figure-library/build"


def _equivalent(first, second):
    if isinstance(first, dict):
        return first.keys() == second.keys() and all(_equivalent(first[k], second[k]) for k in first)
    if isinstance(first, (list, tuple)):
        return len(first) == len(second) and all(_equivalent(a,b) for a,b in zip(first,second))
    if isinstance(first, np.ndarray): return np.array_equal(first,second)
    return first == second


class SemanticPanelTests(unittest.TestCase):
    def setUp(self):
        BUILD.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="semantic-test-", dir=BUILD)
        self.folder = Path(self.temp.name).resolve()
        self.assertEqual(self.folder.parent, BUILD.resolve())
        self.style = base.paper_style(); self.style.__enter__()
        self.fig, self.ax = plt.subplots(figsize=(4,3))

    def tearDown(self):
        plt.close("all"); self.style.__exit__(None,None,None)
        self.temp.cleanup()

    def test_complete_registry_renders_without_mutating_supplied_data(self):
        self.assertEqual(len(panels.REGISTRY),30)
        for kind, entry in panels.REGISTRY.items():
            with self.subTest(kind=kind):
                self.ax.clear()
                data = panels.demo_data(kind, seed=3); original = copy.deepcopy(data)
                self.assertTrue(set(entry["required"]).issubset(data))
                result = entry["function"](self.ax, **data)
                self.assertIsInstance(result,dict)
                self.fig.canvas.draw()
                self.assertTrue(_equivalent(data,original))

    def test_real_mixed_panel_export_keeps_vector_text_and_no_raster(self):
        fig,axes = plt.subplots(2,3,figsize=(8,4.8),layout="constrained")
        for ax,kind in zip(axes.flat,["ecdf","raincloud","quantile_fan","rank_trajectories","matrix_bubbles","mosaic_composition"]):
            panels.REGISTRY[kind]["function"](ax,**panels.demo_data(kind,seed=4))
            ax.set_title(kind.replace("_"," "))
        paths = base.save_figure(fig,self.folder/"mixed-panels",formats=("svg","pdf","png"))
        svg = ET.parse(self.folder/"mixed-panels.svg").getroot()
        ns={"s":"http://www.w3.org/2000/svg"}
        self.assertTrue(svg.findall(".//s:text",ns))
        self.assertFalse(svg.findall(".//s:image",ns))
        for extension in ["svg","pdf","png"]:
            self.assertGreater((self.folder/f"mixed-panels.{extension}").stat().st_size,1000)

    def test_ecdf_counts_ties_without_losing_mass(self):
        result=panels.ecdf(self.ax,[2,1,1,3])
        np.testing.assert_array_equal(result["values"],[1,2,3])
        np.testing.assert_array_equal(result["fractions"],[.5,.75,1])
        self.assertEqual(result["sample_count"],4)

    def test_survival_does_not_reestimate_censoring_or_change_supplied_steps(self):
        result=panels.survival_step(self.ax,[0,2,6],[1,.8,.8],lower=[1,.6,.55],upper=[1,.9,.95])
        np.testing.assert_array_equal(result["line"].get_xdata(),[0,2,6])
        np.testing.assert_array_equal(result["line"].get_ydata(),[1,.8,.8])

    def test_survival_rejects_invalid_probabilities_time_and_increases(self):
        for time,values in [([0,1],[1,1.1]),([0,1],[.6,.7]),([-1,0],[1,.8]),([1,1],[1,.8])]:
            with self.subTest(time=time,values=values),self.assertRaises(ValueError):
                panels.survival_step(self.ax,time,values)

    def test_survival_rejects_interval_outside_probability_domain(self):
        with self.assertRaises(ValueError):
            panels.survival_step(self.ax,[0,1],[.8,.5],lower=[.7,-.1],upper=[1,.6])

    def test_raincloud_retains_all_observations_in_each_group(self):
        samples=[[0,0,1,8],[1,2,2,3]]
        result=panels.raincloud(self.ax,samples,["A","B"],seed=10)
        for sample,artist in zip(samples,result["points"]):
            np.testing.assert_array_equal(artist.get_offsets()[:,0],sample)

    def test_density_panels_reject_singleton_or_empty_observations(self):
        for function in [panels.raincloud,panels.ridgeline]:
            for sample in [[],[1]]:
                with self.subTest(function=function.__name__,sample=sample),self.assertRaises(ValueError):
                    function(self.ax,[sample],["A"])

    def test_density_grid_uses_one_common_scale_across_groups(self):
        result=panels.ridgeline(self.ax,[[-2,0,2],[-.1,0,.1]],["Wide","Narrow"])
        self.assertEqual(len(result["densities"]),2)
        self.assertEqual([len(v) for v in result["densities"]],[len(result["grid"])]*2)
        self.assertEqual(result["common_density_scale"],max(max(v) for v in result["densities"]))

    def test_interval_sort_preserves_labels_bounds_and_entity_colors(self):
        result=panels.ranked_intervals(self.ax,["High","Low"],[4,1],[3,0],[5,2],
                                       order="ascending",colors=["red","blue"])
        self.assertEqual([t.get_text() for t in self.ax.get_yticklabels()],["Low","High"])
        np.testing.assert_array_equal(result["order"],[1,0])
        np.testing.assert_array_equal(result["intervals"][0].get_xdata(),[0,2])
        np.testing.assert_allclose(result["points"][0].get_facecolors()[0,:3],[0,0,1])

    def test_interval_plot_rejects_bounds_that_exclude_estimate(self):
        with self.assertRaises(ValueError):
            panels.ranked_intervals(self.ax,["A"],[2],[3],[4])

    def test_dumbbell_keeps_matching_and_negative_changes(self):
        result=panels.dumbbell(self.ax,["A","B"],[.8,.4],[.7,.6])
        np.testing.assert_allclose(result["difference"],[-.1,.2])
        np.testing.assert_allclose(result["before"].get_offsets()[:,0],[.8,.4])
        self.assertEqual([t.get_text() for t in self.ax.get_yticklabels()],["A","B"])

    def test_bland_altman_returns_descriptive_sd_not_standard_error(self):
        result=panels.bland_altman(self.ax,[0,2],[1,5],limits_multiplier=2)
        self.assertEqual(result["bias"],2)
        self.assertAlmostEqual(result["sample_sd"],np.sqrt(2))
        np.testing.assert_allclose(result["descriptive_limits"],[2-2*np.sqrt(2),2+2*np.sqrt(2)])

    def test_residual_plot_does_not_recompute_or_fit_values(self):
        result=panels.residual_diagnostics(self.ax,[2,1,4],[-1,0,3])
        np.testing.assert_array_equal(result["scatter"].get_offsets(),[[2,-1],[1,0],[4,3]])
        self.assertEqual(len(self.ax.lines),1)

    def test_quantile_fan_rejects_crossed_or_incorrectly_named_quantiles(self):
        with self.assertRaises(ValueError):
            panels.quantile_fan(self.ax,[0,1],[[0,0],[1,1],[.5,2]],[.1,.5,.9])
        with self.assertRaises(ValueError):
            panels.quantile_fan(self.ax,[0,1],[[0,0],[1,1],[2,2]],[.1,.4,.9])
        with self.assertRaises(ValueError):
            panels.quantile_fan(self.ax,[0,1],[[0,0],[1,1],[2,2]],[.1,.5,.8])

    def test_quantile_median_uses_supplied_median_without_recomputation(self):
        result=panels.quantile_fan(self.ax,[0,1],[[0,1],[3,4],[7,9]],[.1,.5,.9])
        np.testing.assert_array_equal(result["median"].get_ydata(),[3,4])

    def test_operating_curves_reject_invalid_rates_or_reordered_threshold_path(self):
        cases=[(panels.precision_recall,dict(recall=[0,.5,1],precision=[1,.7,1.1])),
               (panels.precision_recall,dict(recall=[0,1,.5],precision=[1,.7,.6])),
               (panels.roc,dict(false_positive_rate=[0,.5,1],true_positive_rate=[0,.8,.6])),
               (panels.risk_coverage,dict(coverage=[0,.5,1],risk=[0,.1,.3]))]
        for function,data in cases:
            with self.subTest(function=function.__name__),self.assertRaises(ValueError):function(self.ax,**data)

    def test_precision_recall_does_not_require_precision_to_be_monotone(self):
        result=panels.precision_recall(self.ax,[0,.5,1],[.8,.7,.9],prevalence=.3)
        np.testing.assert_array_equal(result["line"].get_ydata(),[.8,.7,.9])
        np.testing.assert_array_equal(self.ax.lines[1].get_ydata(),[.3,.3])

    def test_rank_trajectories_preserve_ties_and_endpoint_correspondence(self):
        ranks=[[1,2,2],[2,1,2]]
        result=panels.rank_trajectories(self.ax,["A","B","C"],ranks,["First","Second"])
        np.testing.assert_array_equal(result["lines"][1].get_ydata(),[2,1,2])
        self.assertTrue(self.ax.yaxis_inverted())
        with self.assertRaises(ValueError):panels.rank_trajectories(self.ax,["A"],[[1.2]],["First"])

    def test_parallel_axes_use_supplied_domain_not_observed_minmax(self):
        result=panels.parallel_coordinates(self.ax,[[20,3],[40,6]],["A","B"],[[0,100],[0,10]],["X","Y"])
        np.testing.assert_allclose(result["normalized"],[[.2,.3],[.4,.6]])
        with self.assertRaises(ValueError):
            panels.parallel_coordinates(self.ax,[[101,3]],["A","B"],[[0,100],[0,10]],["X"])

    def test_ternary_requires_real_fractions_without_implicit_normalization(self):
        for values in [[[20,30,50]],[[-.1,.6,.5]],[[.2,.3,.4]]]:
            with self.subTest(values=values),self.assertRaises(ValueError):
                panels.ternary(self.ax,values,["A","B","C"])
        result=panels.ternary(self.ax,[[1,0,0],[0,1,0],[0,0,1]],["A","B","C"])
        np.testing.assert_allclose(result["coordinates"],[[0,0],[1,0],[.5,np.sqrt(3)/2]])

    def test_transition_normalization_has_explicit_correct_denominator(self):
        values=[[2,6],[6,2]]
        row=panels.transition_matrix(self.ax,values,["A","B"],normalization="row")
        np.testing.assert_allclose(row["display_values"],[[.25,.75],[.75,.25]])
        result=panels.transition_matrix(self.ax,values,["A","B"],normalization="all")
        self.assertAlmostEqual(result["display_values"].sum(),1)
        with self.assertRaises(ValueError):panels.transition_matrix(self.ax,[[0,0],[1,2]],["A","B"],normalization="row")
        with self.assertRaises(ValueError):panels.transition_matrix(self.ax,values,["A","B"],normalization="unknown")

    def test_zero_raw_transition_counts_are_not_fabricated_or_normalized(self):
        result=panels.transition_matrix(self.ax,[[0,0],[0,0]],["A","B"],normalization="counts")
        np.testing.assert_array_equal(result["display_values"],[[0,0],[0,0]])
        self.fig.canvas.draw()

    def test_mosaic_area_equals_joint_count_fraction(self):
        result=panels.mosaic_composition(self.ax,[[1,3],[6,0]],["Small","Large"],["A","B"])
        np.testing.assert_allclose(result["widths"],[.4,.6])
        areas=[p.get_width()*p.get_height() for p in result["patches"]]
        np.testing.assert_allclose(areas,[.1,.3,.6,0])
        with self.assertRaises(ValueError):panels.mosaic_composition(self.ax,[[0,0]],["Empty"],["A","B"])

    def test_bubble_area_uses_magnitude_and_hue_retains_sign(self):
        result=panels.matrix_bubbles(self.ax,[[-1,.5,0]],["R"],["A","B","C"],magnitude_max=1)
        np.testing.assert_allclose(result["scatter"].get_sizes(),[190,95,0])
        np.testing.assert_allclose(result["scatter"].get_array(),[-1,.5,0])
        with self.assertRaises(ValueError):panels.matrix_bubbles(self.ax,[[2]],["A"],["B"],magnitude_max=1)

    def test_signed_effects_preserve_negative_direction_and_zero(self):
        result=panels.signed_effects(self.ax,["A","B","C"],[-3,0,2])
        np.testing.assert_array_equal(result["scatter"].get_offsets()[:,0],[-3,0,2])

    def test_convergence_envelope_is_pointwise_sample_iqr(self):
        runs=[[1,3],[2,4],[3,7],[4,8]]
        result=panels.convergence_envelope(self.ax,[0,10],runs)
        np.testing.assert_allclose(result["median"].get_ydata(),[2.5,5.5])
        np.testing.assert_allclose(result["lower"],[1.75,3.75])
        np.testing.assert_allclose(result["upper"],[3.25,7.25])

    def test_grouped_dot_keeps_series_category_mapping(self):
        result=panels.grouped_dot(self.ax,["A","B"],[[1,3],[2,4]],["X","Y"])
        np.testing.assert_array_equal(result["points"][0].get_offsets()[:,0],[1,3])
        np.testing.assert_array_equal(result["points"][1].get_offsets()[:,0],[2,4])

    def test_response_grid_does_not_transpose_non_square_observations(self):
        values=[[1,2,3],[4,5,6]]
        result=panels.contour_response(self.ax,[0,1,2],[0,2],values)
        np.testing.assert_array_equal(result["response"],values)
        with self.assertRaises(ValueError):panels.contour_response(self.ax,[0,1,2],[0,2],np.array(values).T)

    def test_robustness_retains_actual_nonmonotone_response(self):
        result=panels.robustness_profile(self.ax,[0,1,2],[[.8,.85,.5]],["A"])
        np.testing.assert_array_equal(result["lines"][0].get_ydata(),[.8,.85,.5])

    def test_frontier_ties_and_dominated_points_are_not_misclassified(self):
        result=panels.cost_quality_frontier(self.ax,[1,2,2,3],[.5,.6,.6,.55],["A","B","C","D"])
        np.testing.assert_array_equal(result["frontier"],[True,True,True,False])
        result=panels.cost_quality_frontier(self.ax,[1,2,2,3],[.5,.6,.6,.55],["A","B","C","D"],quality_direction="min")
        np.testing.assert_array_equal(result["frontier"],[True,False,False,False])
        with self.assertRaises(ValueError):panels.cost_quality_frontier(self.ax,[-1],[.5],["A"])

    def test_quadrant_plot_preserves_positions_and_marks_boundaries(self):
        result=panels.quadrant_scatter(self.ax,[-1,2,0],[3,-2,0],["A","B","C"])
        np.testing.assert_array_equal(result["scatter"].get_offsets(),[[-1,3],[2,-2],[0,0]])
        np.testing.assert_array_equal(result["regions"],[[-1,1],[1,-1],[0,0]])

    def test_quadrants_respect_nonzero_references_without_recentering_values(self):
        result=panels.quadrant_scatter(self.ax,[3,5],[8,10],["A","B"],x_reference=4,y_reference=9)
        np.testing.assert_array_equal(result["scatter"].get_offsets(),[[3,8],[5,10]])
        np.testing.assert_array_equal(result["regions"],[[-1,-1],[1,1]])
        with self.assertRaises(ValueError):panels.quadrant_scatter(self.ax,[1],[2],["A"],x_reference=np.inf)

    def test_mean_delta_uses_before_on_x_and_exact_signed_change_on_y(self):
        result=panels.mean_delta(self.ax,[.8,.2,.6],[.7,.4,.6],["A","B","C"])
        np.testing.assert_allclose(result["scatter"].get_offsets(),[[.8,-.1],[.2,.2],[.6,0]])
        np.testing.assert_allclose(result["delta"],[-.1,.2,0])

    def test_mean_delta_rejects_unmatched_pairs_instead_of_truncating(self):
        with self.assertRaises(ValueError):panels.mean_delta(self.ax,[1,2],[3],["A","B"])

    def test_mirrored_histogram_uses_same_bins_and_includes_final_right_edge(self):
        result=panels.mirrored_histogram(self.ax,[0,.5,1,2],[.2,1.5,1.9],[0,1,2])
        np.testing.assert_array_equal(result["first_counts"],[2,2])
        np.testing.assert_array_equal(result["second_counts"],[1,2])
        np.testing.assert_array_equal([bar.get_height() for bar in result["second_bars"]],[-1,-2])
        self.assertEqual(result["sample_counts"],(4,3))
        self.assertEqual(self.ax.yaxis.get_major_formatter()(-2,0),"2")

    def test_mirrored_histogram_rejects_bad_bins_and_out_of_range_observations(self):
        for bins in [[0],[0,0,1],[1,0],[0,np.nan,2]]:
            with self.subTest(bins=bins),self.assertRaises(ValueError):
                panels.mirrored_histogram(self.ax,[.2],[.4],bins)
        for first,second in [([-1],[.5]),([.5],[2.1])]:
            with self.subTest(first=first,second=second),self.assertRaises(ValueError):
                panels.mirrored_histogram(self.ax,first,second,[0,1,2])

    def test_mirrored_histogram_preserves_nonuniform_bin_widths_and_exposure(self):
        result=panels.mirrored_histogram(self.ax,[0,.2,1,4],[1,3],[0,.5,2,4])
        np.testing.assert_array_equal([bar.get_width() for bar in result["first_bars"]],[.5,1.5,2])
        self.assertEqual(sum(result["first_counts"]),4)
        self.assertEqual(sum(result["second_counts"]),2)

    def test_mirror_stem_keeps_common_x_and_absolute_peak_amplitudes(self):
        result=panels.mirror_stem(self.ax,[2,4,8],[0,6,2],[3,1,10])
        np.testing.assert_array_equal(result["first_points"].get_offsets(),[[2,0],[4,6],[8,2]])
        np.testing.assert_array_equal(result["second_points"].get_offsets(),[[2,-3],[4,-1],[8,-10]])
        np.testing.assert_array_equal(result["first"],[0,6,2])
        np.testing.assert_array_equal(result["second"],[3,1,10])
        self.assertEqual(self.ax.yaxis.get_major_formatter()(-10,0),"10")

    def test_mirror_stem_rejects_negative_amplitude_or_unaligned_peak_positions(self):
        for x,first,second in [([1,2],[-1,2],[1,3]),([1,1],[1,2],[3,4]),([1,2],[1],[2,3])]:
            with self.subTest(x=x,first=first),self.assertRaises(ValueError):
                panels.mirror_stem(self.ax,x,first,second)

    def test_binned_composition_preserves_observation_pairing_and_actual_bin_widths(self):
        values=[0,.2,.8,1,4]
        groups=["A","B","B","A","B"]
        result=panels.binned_group_composition(self.ax,values,groups,[0,.5,2,4],["B","A"])
        np.testing.assert_array_equal(result["counts"],[[1,1,1],[1,1,0]])
        np.testing.assert_array_equal(result["totals"],[2,2,1])
        np.testing.assert_allclose(result["fractions"],[[.5,.5,1],[.5,.5,0]])
        np.testing.assert_array_equal([bar.get_width() for bar in result["bars"][0]],[.5,1.5,2])
        histogram,_=np.histogram(values,[0,.5,2,4])
        np.testing.assert_array_equal(result["totals"],histogram)

    def test_binned_composition_keeps_empty_bins_blank_and_fractions_unknown(self):
        result=panels.binned_group_composition(self.ax,[.1,2.1],["A","B"],[0,1,2,3],["A","B"])
        np.testing.assert_array_equal(result["totals"],[1,0,1])
        self.assertTrue(np.isnan(result["fractions"][:,1]).all())
        self.assertEqual([bar.get_x() for bar in result["bars"][0]],[0,2])
        self.assertEqual(len(result["bars"][0]),2)

    def test_binned_composition_rejects_unknown_groups_unmatched_pairs_and_invalid_bins(self):
        cases=[dict(values=[.5],groups=["C"],bin_edges=[0,1],group_order=["A","B"]),
               dict(values=[.5,.6],groups=["A"],bin_edges=[0,1],group_order=["A"]),
               dict(values=[2],groups=["A"],bin_edges=[0,1],group_order=["A"]),
               dict(values=[.5],groups=["A"],bin_edges=[0,1,1],group_order=["A"]),
               dict(values=[.5],groups=["A"],bin_edges=[0,1],group_order=["A","A"])]
        for data in cases:
            with self.subTest(data=data),self.assertRaises(ValueError):
                panels.binned_group_composition(self.ax,**data)

    def test_ordered_trajectory_retains_folds_and_repeated_coordinates(self):
        x=[3,1,2,2,0];y=[0,1,3,3,4]
        result=panels.ordered_trajectory(self.ax,x,y,steps=[0,5,9,12,20],arrows=8)
        np.testing.assert_array_equal(result["line"].get_xdata(),x)
        np.testing.assert_array_equal(result["line"].get_ydata(),y)
        np.testing.assert_array_equal(result["steps"],[0,5,9,12,20])
        np.testing.assert_array_equal(result["arrow_segments"],[0,1,3])
        np.testing.assert_array_equal(result["first"].get_offsets(),[[3,0]])
        np.testing.assert_array_equal(result["last"].get_offsets(),[[0,4]])

    def test_ordered_trajectory_rejects_misaligned_or_unordered_steps(self):
        for steps in [[0],[0,0],[1,0],[0,np.nan]]:
            with self.subTest(steps=steps),self.assertRaises(ValueError):
                panels.ordered_trajectory(self.ax,[2,1],[0,1],steps=steps)
        with self.assertRaises(ValueError):panels.ordered_trajectory(self.ax,[2],[0])

    def test_ordered_trajectory_composes_with_checkpoint_trend_and_constant_states(self):
        fig,(state_ax,trend_ax)=plt.subplots(1,2,figsize=(6,2.5),layout="constrained")
        state=panels.ordered_trajectory(state_ax,[2,2,2],[1,1,1],steps=[0,1,2])
        panels.convergence_envelope(trend_ax,[0,1,2],[[2,2,2],[3,2,2]])
        self.assertEqual(len(state["arrows"]),0)
        fig.savefig(self.folder/"checkpoint-composition.svg")
        self.assertGreater((self.folder/"checkpoint-composition.svg").stat().st_size,1000)

    def test_all_semantic_panels_reject_nonfinite_observation(self):
        for kind,entry in panels.REGISTRY.items():
            with self.subTest(kind=kind):
                data=panels.demo_data(kind,seed=1)
                # Replace the first required numeric payload, preserving its shape.
                for key in entry["required"]:
                    value=data[key]
                    try:numeric=np.asarray(value,dtype=float)
                    except (ValueError,TypeError):continue
                    if numeric.size:
                        corrupted=numeric.copy();corrupted.flat[0]=np.nan;data[key]=corrupted
                        break
                with self.assertRaises(ValueError):entry["function"](self.ax,**data)

    def test_demo_data_is_seeded_local_and_unknown_kinds_fail(self):
        np.random.seed(21);before=np.random.get_state()
        first=panels.demo_data("raincloud",seed=8);second=panels.demo_data("raincloud",seed=8)
        self.assertTrue(_equivalent(first,second))
        after=np.random.get_state()
        self.assertEqual(before[0],after[0]);np.testing.assert_array_equal(before[1],after[1])
        self.assertEqual(before[2:],after[2:])
        with self.assertRaises(ValueError):panels.demo_data("not_a_plot")


if __name__ == "__main__":
    unittest.main()
