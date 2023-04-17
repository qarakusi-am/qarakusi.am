from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Rotate, linear, BLUE, Arrow
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, TransformFromCopy, TAU, PI
from manim import Scene, RIGHT, LEFT, UP, DOWN, ORANGE, WHITE, BLUE_C
from .text import *

FONT_SIZE = 60
DOT_SIZE = 40


class Problem12777(Scene):
    def construct(self):
        self.coordinate_axes = coordinate_axes = Axes(
            x_range=[-7.3, 7.3, 1],
            x_length=13,
            y_range=[-3, 9.3, 1],
            y_length=8,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        )

        point = VGroup(MathTex("A(2, 7)", font_size=DOT_SIZE).next_to(coordinate_axes.c2p(2, 7, 0)),
                       Dot(point=coordinate_axes.c2p(2, 7, 0)),
                       coordinate_axes.get_horizontal_line(coordinate_axes.c2p(2, 7, 0)),
                       coordinate_axes.get_vertical_line(coordinate_axes.c2p(2, 7, 0)))

        # create coordinate axis
        self.play(Write(coordinate_axes))
        self.wait(2)

        self.play(Write(point[1:]))
        self.play(Write(point[0]))
        self.wait()

        # initial line with equation y=3x+1
        line = VGroup(Line(coordinate_axes.c2p(-3, -8, 0), coordinate_axes.c2p(10, 31, 0)),
                      MathTex("y=kx+b", font_size=DOT_SIZE).next_to(coordinate_axes.c2p(0, 8.3, 0)))
        self.play(Write(line[0]))
        self.wait()

        self.play(Rotate(
            line[0],
            angle=PI,
            about_point=point[1].get_center(),
            rate_func=linear,
            run_time=3
        ))
        self.wait(2)
        # plot y=2x-1 line
        helper_line = VGroup(coordinate_axes.plot(lambda x: 2 * x - 1, x_range=[-5, 10]),
                             MathTex("y=2x-1", font_size=DOT_SIZE).next_to(coordinate_axes.c2p(4, 7, 0)))

        self.play(Write(helper_line[0]))
        self.play(Write(helper_line[1]))

        self.wait(3)

        # rotate initial line to be parallel with y=2x-1
        self.play(Rotate(
            line[0],
            angle=-PI * 0.057,
            about_point=point[1].get_center(),
            rate_func=linear,
            run_time=2
        ))
        self.wait()
        self.play(line[0].animate.set_color(ORANGE))
        self.wait(2)

        self.play(Write(line[1]))
        self.wait()

        # move the line up and down and bring to initial position
        self.play(line[0].animate(run_time=2).shift(UP * 3))
        self.play(line[0].animate(run_time=3).shift(DOWN * 7))
        self.play(line[0].animate(run_time=2).shift(UP * 4))
        self.wait()

        # write parallel line properties

        slope_property = Tex(parallel_lines_have_the_same_slope, font_size=40).shift((UP * 2 + LEFT * 4))
        self.play(Write(slope_property))
        self.wait()

        # find the slope
        self.play(AnimationGroup(line[1][0][2].animate.scale(1.3).set_color(BLUE),
                                 helper_line[1][0][2].animate.scale(1.3).set_color(BLUE)))
        new_slope = MathTex("2", font_size=DOT_SIZE).scale(1.3).set_color(BLUE).move_to(line[1][0][2])

        self.wait()

        self.play(TransformFromCopy(helper_line[1][0][2], new_slope), line[1][0][2].animate.set_opacity(0))
        self.wait()

        self.play(AnimationGroup(helper_line[1][0][2].animate.scale(1 / 1.3).set_color(WHITE),
                                 new_slope.animate.scale(1 / 1.3).set_color(WHITE)))
        self.wait()

        self.play(FadeOut(helper_line))

        equation = MathTex("y=2x+b", font_size=DOT_SIZE).move_to(slope_property).shift(DOWN)

        self.play(Write(equation))
        self.wait(2)

        helper_numbers = VGroup(MathTex("2", font_size=DOT_SIZE).move_to(equation[0][3]).shift(DOWN * 0.72),
                                MathTex("7", font_size=DOT_SIZE).move_to(equation[0][0]).shift(DOWN * 0.7),
                                MathTex("*2", font_size=DOT_SIZE).move_to(equation[0][3]).shift(
                                    UP * 0.055 + RIGHT * 0.07),
                                MathTex("7", font_size=DOT_SIZE).move_to(equation[0][0]).shift(UP * 0.09 * 0.6),
                                )

        arrows = VGroup(Arrow(helper_numbers[1].get_top(), equation[0][0].get_top()).scale(2).shift(DOWN * 0.1 + RIGHT),
                        Arrow(helper_numbers[1].get_top(), equation[0][0].get_top()).scale(2).shift(DOWN * 0.12))
        self.play(AnimationGroup(TransformFromCopy(point[0][0][2], helper_numbers[0]),
                                 TransformFromCopy(point[0][0][4], helper_numbers[1])))
        self.play(Write(arrows))
        self.wait()

        self.play(AnimationGroup(TransformFromCopy(helper_numbers[0], helper_numbers[-2]),
                                 TransformFromCopy(helper_numbers[1], helper_numbers[-1]),
                                 equation[0][3].animate.set_opacity(0),
                                 equation[0][0].animate.set_opacity(0)))
        self.wait(2)

        self.play(FadeOut(helper_numbers[0:2], arrows))
        self.wait()

        helper_equations = VGroup(
            MathTex("7=b+4", font_size=DOT_SIZE).move_to(equation[0][3]).shift(DOWN * 0.7 + LEFT * 0.25),
            MathTex("b=3", font_size=DOT_SIZE).move_to(equation[0][0]).shift(DOWN * 1.4 + RIGHT * 0.43), )

        self.play(Write(helper_equations[0], run_time=2))
        self.wait()

        self.play((Write(helper_equations[1], run_time=2)))
        self.wait(2)

        self.play(
            TransformFromCopy(helper_equations[-1][0][-1], helper_equations[-1][0][-1].copy().move_to(line[1][0][-1]),
                              run_time=2), line[1][0][-1].animate.set_opacity(0))
        self.wait()
