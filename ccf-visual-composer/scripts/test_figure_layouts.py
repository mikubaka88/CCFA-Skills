#!/usr/bin/env python3
"""Check scientific linkage, actual axes alignment and editable export."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"ccf-visual-composer/resources/python"))
import ccfa_analysis_panels as p
import ccfa_figure_layouts as layouts


class LinkedLayoutTests(unittest.TestCase):
    def tearDown(self):
        plt.close("all")

    def joint(self):
        return {"x":[0,.5,1,2],"y":[4,2,1,0],"bin_edges_x":[0,1,2],
                "bin_edges_y":[0,1,2,4],"xlabel":"测量 A","ylabel":"测量 B"}

    def matrix(self):
        return {"x":[.1,.4,1.6],"y":[1,2,8],"response":[[1,2,3],[4,5,6],[7,8,9]],
                "row_index":1,"column_index":2,"xlabel":"控制 X","ylabel":"控制 Y",
                "response_label":"观测响应"}

    def tracks(self):
        return {"x":[1,2,5,11],"xlabel":"共享位置 (bp)","tracks":[
            {"label":"信号一","unit":"counts","series":[{"label":"Observed","y":[1,4,2,7]},
                {"label":"Predicted","y":[1.1,3.8,2.2,6.8],"linestyle":"--"}]},
            {"label":"信号二","unit":"a.u.","series":[{"label":"Predicted","y":[.1,.2,.3,.4]},
                {"label":"Observed","y":[.2,.1,.4,.3]}]}]}

    def test_joint_marginals_count_the_actual_same_paired_observations(self):
        data=self.joint();fig=layouts.render_layout("joint_marginals",data)
        info=fig.ccfa_layout;meta=info["computed"]
        np.testing.assert_array_equal(meta["joint_artist"].get_offsets(),np.column_stack((data["x"],data["y"])))
        np.testing.assert_array_equal(meta["counts_x"],[2,2])
        np.testing.assert_array_equal(meta["counts_y"],[1,1,2])
        self.assertEqual(sum(bar.get_height() for bar in meta["x_bars"]),4)
        self.assertEqual(sum(bar.get_width() for bar in meta["y_bars"]),4)

    def test_last_histogram_edge_keeps_observation_and_nonuniform_width(self):
        data=self.joint();data["bin_edges_x"]=[0,.25,1.25,2]
        fig=layouts.render_layout("joint_marginals",data);meta=fig.ccfa_layout["computed"]
        np.testing.assert_allclose([bar.get_width() for bar in meta["x_bars"]],[.25,1,.75])
        self.assertEqual(sum(meta["counts_x"]),len(data["x"]))

    def test_joint_axes_share_limits_and_plot_edges(self):
        fig=layouts.render_layout("joint_marginals",self.joint());fig.canvas.draw()
        axes=fig.ccfa_layout["axes"];main,top,right=axes["main"],axes["x_counts"],axes["y_counts"]
        self.assertEqual(main.get_xlim(),top.get_xlim())
        self.assertEqual(main.get_ylim(),right.get_ylim())
        self.assertAlmostEqual(main.get_position().x0,top.get_position().x0)
        self.assertAlmostEqual(main.get_position().x1,top.get_position().x1)
        self.assertAlmostEqual(main.get_position().y0,right.get_position().y0)
        self.assertAlmostEqual(main.get_position().y1,right.get_position().y1)

    def test_joint_rejects_dropped_observations_or_unpaired_axes(self):
        for mutate in (lambda d:d.update(x=[0,3,1,2]),lambda d:d.update(y=[1,2]),
                       lambda d:d.update(bin_edges_x=[0,1,1,2]),lambda d:d.update(y=[0,np.nan,1,2])):
            data=self.joint();mutate(data)
            with self.assertRaises(ValueError):layouts.render_layout("joint_marginals",data)

    def test_joint_color_values_need_full_declared_range(self):
        data=self.joint();data["color_values"]=[0,1,2,3]
        with self.assertRaisesRegex(ValueError,"color_range"):layouts.render_layout("joint_marginals",data)
        data["color_range"]=[0,2]
        with self.assertRaisesRegex(ValueError,"enclose"):layouts.render_layout("joint_marginals",data)
        data["color_range"]=[0,3];fig=layouts.render_layout("joint_marginals",data)
        self.assertIn("colorbar",fig.ccfa_layout["axes"])
        np.testing.assert_array_equal(fig.ccfa_layout["computed"]["joint_artist"].get_array(),[0,1,2,3])

    def test_joint_hexbin_preserves_observation_count_and_color_meaning(self):
        data=self.joint();data["mode"]="hexbin"
        fig=layouts.render_layout("joint_marginals",data);meta=fig.ccfa_layout["computed"]
        self.assertEqual(sum(meta["joint_artist"].get_array()),len(data["x"]))
        data.update(color_values=[1,2,3,4],color_range=[0,4])
        with self.assertRaisesRegex(ValueError,"scatter"):layouts.render_layout("joint_marginals",data)

    def test_track_coordinates_and_units_remain_literal(self):
        data=self.tracks();fig=layouts.render_layout("aligned_tracks",data);meta=fig.ccfa_layout["computed"]
        np.testing.assert_array_equal(meta["x"],data["x"])
        self.assertEqual(meta["units"],["counts","a.u."])
        for track,lines in zip(data["tracks"],meta["lines"]):
            for series,line in zip(track["series"],lines):
                np.testing.assert_array_equal(line.get_xdata(),data["x"])
                np.testing.assert_array_equal(line.get_ydata(),series["y"])
        self.assertIn("counts",fig.ccfa_layout["axes"]["tracks"][0].get_ylabel())

    def test_track_series_colors_remain_stable_under_reordered_series(self):
        fig=layouts.render_layout("aligned_tracks",self.tracks())
        lines=fig.ccfa_layout["computed"]["lines"]
        self.assertEqual(lines[0][0].get_color(),lines[1][1].get_color())
        self.assertEqual(lines[0][1].get_color(),lines[1][0].get_color())
        self.assertNotEqual(lines[0][0].get_color(),lines[0][1].get_color())

    def test_track_custom_identity_colors_and_dash_remain(self):
        data=self.tracks();data["entity_colors"]={"Observed":"#112233","Predicted":"#AA5500"}
        fig=layouts.render_layout("aligned_tracks",data)
        lines=fig.ccfa_layout["computed"]["lines"]
        self.assertEqual(lines[0][1].get_color(),"#AA5500")
        self.assertEqual(lines[0][1].get_linestyle(),"--")

    def test_track_axes_share_position_without_sharing_units(self):
        fig=layouts.render_layout("aligned_tracks",self.tracks());fig.canvas.draw()
        axes=fig.ccfa_layout["axes"]["tracks"]
        self.assertEqual(axes[0].get_xlim(),axes[1].get_xlim())
        self.assertNotEqual(axes[0].get_ylim(),axes[1].get_ylim())
        self.assertAlmostEqual(axes[0].get_position().x0,axes[1].get_position().x0)
        self.assertAlmostEqual(axes[0].get_position().x1,axes[1].get_position().x1)

    def test_track_missing_units_conflicting_modes_and_nan_are_rejected(self):
        for mutate in (lambda d:d["tracks"][0].pop("unit"),lambda d:d["tracks"][0].update(y=[1,2,3,4]),
                       lambda d:d["tracks"][0]["series"][0].update(y=[1,2]),
                       lambda d:d["tracks"][1]["series"][0].update(y=[.1,.2,np.nan,.4]),
                       lambda d:d.update(x=[1,5,2,11]),lambda d:d["tracks"].append("not a track")):
            data=self.tracks();mutate(data)
            with self.assertRaises(ValueError):layouts.render_layout("aligned_tracks",data)

    def test_track_markers_retain_common_coordinate_and_must_be_inside(self):
        data=self.tracks();data["markers"]=[{"x":5,"label":"变异"}]
        fig=layouts.render_layout("aligned_tracks",data)
        for ax in fig.ccfa_layout["axes"]["tracks"]:
            self.assertTrue(any(np.array_equal(line.get_xdata(),[5,5]) for line in ax.lines))
        data["markers"][0]["x"]=20
        with self.assertRaisesRegex(ValueError,"inside"):layouts.render_layout("aligned_tracks",data)

    def test_matrix_profiles_are_rows_and_columns_of_the_same_supplied_grid(self):
        data=self.matrix();fig=layouts.render_layout("matrix_slices",data);meta=fig.ccfa_layout["computed"]
        np.testing.assert_array_equal(meta["row_values"],[4,5,6])
        np.testing.assert_array_equal(meta["column_values"],[3,6,9])
        np.testing.assert_array_equal(meta["row_line"].get_xdata(),data["x"])
        np.testing.assert_array_equal(meta["column_line"].get_ydata(),data["y"])
        np.testing.assert_array_equal(meta["mesh"].get_array(),data["response"])

    def test_matrix_nonuniform_coordinates_are_not_replaced_by_integer_cells(self):
        data=self.matrix();fig=layouts.render_layout("matrix_slices",data)
        coordinates=fig.ccfa_layout["computed"]["mesh"].get_coordinates()
        np.testing.assert_allclose(coordinates[0,:,0],[-.05,.25,1,2.2])
        np.testing.assert_allclose(coordinates[:,0,1],[.5,1.5,5,11])

    def test_matrix_linked_axis_positions_and_selected_markers(self):
        data=self.matrix();fig=layouts.render_layout("matrix_slices",data);fig.canvas.draw()
        axes=fig.ccfa_layout["axes"];main,row,column=axes["main"],axes["row_slice"],axes["column_slice"]
        self.assertEqual(main.get_xlim(),row.get_xlim())
        self.assertEqual(main.get_ylim(),column.get_ylim())
        self.assertAlmostEqual(main.get_position().x0,row.get_position().x0)
        self.assertAlmostEqual(main.get_position().y1,column.get_position().y1)
        self.assertTrue(any(np.array_equal(line.get_ydata(),[2,2]) for line in main.lines))
        self.assertTrue(any(np.array_equal(line.get_xdata(),[1.6,1.6]) for line in main.lines))

    def test_matrix_rejects_missing_grid_values_and_invalid_selected_indices(self):
        for mutate in (lambda d:d.update(response=[[1,2],[3,4]]),lambda d:d["response"][0].__setitem__(0,float("nan")),
                       lambda d:d.update(row_index=True),lambda d:d.update(column_index=-1),
                       lambda d:d.update(row_index=3),lambda d:d.update(x=[1,1,2])):
            data=self.matrix();mutate(data)
            with self.assertRaises(ValueError):layouts.render_layout("matrix_slices",data)

    def test_matrix_explicit_color_range_cannot_hide_values(self):
        data=self.matrix();data["response_range"]=[1,8]
        with self.assertRaisesRegex(ValueError,"enclose"):layouts.render_layout("matrix_slices",data)
        data["response_range"]=[0,10]
        fig=layouts.render_layout("matrix_slices",data);mesh=fig.ccfa_layout["computed"]["mesh"]
        self.assertEqual(mesh.get_clim(),(0,10))

    def test_each_renderer_preserves_input_and_does_not_invoke_demo(self):
        inputs={"joint_marginals":self.joint(),"aligned_tracks":self.tracks(),"matrix_slices":self.matrix()}
        with patch.object(layouts,"demo_data",side_effect=AssertionError("No invented observations")):
            for kind,data in inputs.items():
                before=copy.deepcopy(data);fig=layouts.render_layout(kind,data)
                self.assertEqual(before,data)
                self.assertFalse(any("Simulated" in text.get_text() for text in fig.texts))

    def test_failed_render_does_not_leak_figures(self):
        before=set(plt.get_fignums())
        data=self.matrix();data["row_index"]=200
        with self.assertRaises(ValueError):layouts.render_layout("matrix_slices",data)
        self.assertEqual(set(plt.get_fignums()),before)

    def test_invalid_dimensions_and_tiny_canvases_are_rejected(self):
        for value in (True,float("nan"),float("inf"),20,1001):
            with self.assertRaises(ValueError):layouts.render_layout("matrix_slices",self.matrix(),width_mm=value)
        with self.assertRaises(ValueError):layouts.render_layout("aligned_tracks",self.tracks(),height_mm=20)

    def test_font_size_defaults_and_override_reach_each_layout_without_global_mutation(self):
        old=matplotlib.rcParams["font.size"]
        for kind,data in (("joint_marginals",self.joint()),("aligned_tracks",self.tracks()),("matrix_slices",self.matrix())):
            for size in (8.5,14):
                with self.subTest(kind=kind,size=size):
                    kwargs={} if size==8.5 else {"font_size":size}
                    fig=layouts.render_layout(kind,data,**kwargs)
                    self.assertEqual(matplotlib.rcParams["font.size"],old)
                    for ax in fig.axes:
                        if ax.get_xlabel():self.assertEqual(ax.xaxis.label.get_fontsize(),size)
                        if ax.get_ylabel():self.assertEqual(ax.yaxis.label.get_fontsize(),size)
                        for tick in ax.get_xticklabels()+ax.get_yticklabels():
                            self.assertEqual(tick.get_fontsize(),size-.5)
                        if ax.get_legend():
                            self.assertTrue(all(t.get_fontsize()==size-.5 for t in ax.get_legend().get_texts()))
                    plt.close(fig)

    def test_layout_demos_use_explicit_synthetic_mark_and_fresh_values_by_default(self):
        a=layouts.demo_data("joint_marginals");b=layouts.demo_data("joint_marginals")
        self.assertFalse(np.array_equal(a["x"],b["x"]))
        fig=layouts.render_layout("joint_marginals",a)
        self.assertTrue(any("Simulated data" in text.get_text() for text in fig.texts))
        self.assertNotIn("seed",a["_meta"])

    def test_cjk_labels_and_all_three_vector_exports_have_no_missing_text(self):
        with tempfile.TemporaryDirectory() as folder:
            for kind,data in (("joint_marginals",self.joint()),("aligned_tracks",self.tracks()),("matrix_slices",self.matrix())):
                with self.subTest(kind=kind),warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    fig=layouts.render_layout(kind,data)
                    qa=p.audit_figure(fig)
                    self.assertEqual(qa["missing_glyphs"],[])
                    self.assertEqual(qa["text_outside_canvas"],[])
                    outputs=p.save_figure(fig,Path(folder)/kind)
                    self.assertTrue(outputs["svg"].exists() and outputs["pdf"].exists() and outputs["png"].exists())
                    self.assertIn("<text",outputs["svg"].read_text(encoding="utf-8"))
                    self.assertFalse([w for w in caught if "Glyph" in str(w.message)])

    def test_simulation_footer_does_not_overlap_axis_labels(self):
        for kind in layouts.LAYOUTS:
            with self.subTest(kind=kind):
                fig=layouts.render_layout(kind,layouts.demo_data(kind,seed=1));fig.canvas.draw()
                renderer=fig.canvas.get_renderer();footer=next(t for t in fig.texts if "Simulated data" in t.get_text())
                footer_box=footer.get_window_extent(renderer)
                for ax in fig.axes:
                    for label in (ax.xaxis.label,ax.yaxis.label):
                        if label.get_visible() and label.get_text():
                            self.assertFalse(footer_box.overlaps(label.get_window_extent(renderer)))


if __name__=="__main__":unittest.main()
