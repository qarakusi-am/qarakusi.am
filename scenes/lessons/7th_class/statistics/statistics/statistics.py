from manim import DOWN, RIGHT, WHITE, LEFT, UP, BLACK, BarChart, GREEN, RED, Rectangle, GREEN_B, YELLOW, ORANGE
from manim import Tex, SurroundingRectangle, VGroup, Line, Text, ReplacementTransform, DrawBorderThenFill
from manim import FadeOut, Write, Create, Table, Brace
from manim import Scene
from . import text
import numpy as np
from .text import *

class Statistics(Scene):
    def construct(self):
        run_time = 5
        data = [f"{ind} {minute}" for ind in range(10, 19)]

        count = [1, 2, 3, 5, 14, 13, 9, 2, 1]

        data_for_table = [[i, str(j)] for i, j in zip(data, count)]

        table = Table(
            data_for_table,
            col_labels=[
                Tex(text.data),
                Tex(text.count)
            ],
            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )
        table.scale(0.6)

        self.play(table.create(), run_time=8)
        self.wait()

        histogram = BarChart(
            values=count,
            bar_names=data,
            bar_colors=np.full(len(data), WHITE),
            x_axis_config={"font_size": 30},
            y_range=[0, 14, 1],
            x_length=13.25,
            y_length=7,
            bar_fill_opacity=1,
        )
        histogram.scale(0.7).shift(DOWN)

        self.play(ReplacementTransform(table, histogram))
        self.wait(2)

        total_days = Tex(text.total_days)
        equality = Tex('$13$', '$ + $', '$9$', '$ + $', '$2$', '$ + $', '$1$').set_color(ORANGE)
        result = Tex('$25$')
        days_bought_a_pie = Tex(text.days_bought_a_pie)
        conclusion = Tex(text.number_of_pie_bought_days, r'$\frac{25}{50} $ ', '$ = 0.5 $' + text.part)
        concolusion_box = SurroundingRectangle(conclusion, color=ORANGE, buff=0.5)

        self.play(Write(total_days.next_to(histogram, UP).shift(UP * 1.5)), run_time=2)
        self.wait()
        histogram.bar_colors = [WHITE, WHITE, WHITE, WHITE, WHITE, ORANGE, ORANGE, ORANGE, ORANGE]
        histogram.change_bar_values(values=count, update_colors=True)
        self.add(histogram)
        self.wait()

        brace = Brace(histogram, color=WHITE, direction=(0., 1., 0.), sharpness=1.)
        brace.stretch(0.35, dim=0).shift(RIGHT * 2.6)
        self.play(Write(brace), run_time=2)
        self.wait()
        bought_a_pie_text = Tex(text.bought_a_pie).scale(0.8).set_color(ORANGE)
        equality_text = VGroup(brace, bought_a_pie_text)

        self.play(Write(bought_a_pie_text.next_to(brace, UP)), run_time=2)
        self.wait(2)

        self.wait()

        self.play(ReplacementTransform(equality_text, equality.next_to(total_days, DOWN).shift(RIGHT * 3 + DOWN)))
        self.wait(2)
        self.play(
            ReplacementTransform(equality, result.set_color(ORANGE).next_to(total_days, DOWN).shift(RIGHT * 3 + DOWN)))
        self.wait(2)
        self.play(result.animate.next_to(total_days, DOWN).align_to(total_days, LEFT), run_time=2)
        self.wait(2)
        self.play(Write(days_bought_a_pie.next_to(result)))
        self.wait()
        self.play(FadeOut(histogram))
        self.wait()

        self.play(Write(VGroup(conclusion, concolusion_box)), run_time=run_time)
        self.wait(2)

