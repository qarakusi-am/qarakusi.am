from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw, FadeIn
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, Brace, CurvedArrow
from manim import RIGHT, LEFT, UP, DOWN, ORANGE, Scene, GREEN
from .text import *
from qarakusiscene import TaskNumberBox

class Problem12797(Scene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)

        self.add(taskNumber)
        self.wait()

        self.play(FadeOut(taskNumber))
        self.wait(.25)

        FONT_SIZES = {'text': 55, 'lin_func': 65, 'graph': 35}

        #Writing the problem
        text = Tex(a_line_through_the_points, font_size=FONT_SIZES['text']).shift(UP*3)
        text[0][:7].set_color(ORANGE)
        text[0][8:14].set_color(GREEN)

        self.play(Write(text))
        self.wait()

        #displaying coordinate axes
        coordinate_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-6, 6, 1],
            x_length=10,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 35,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        ).shift(DOWN*.5)

        self.play(Write(coordinate_axes))
        self.wait()

        #displaying the main points
        points = VGroup(
            Dot(point=coordinate_axes.c2p(0, -2, 0)),
            Dot(point=coordinate_axes.c2p(1, 0, 0))
        )

        self.play(AnimationGroup(Write(points[0]),
                                 text[0][:7].animate.next_to(points[0]).scale(.7).shift(LEFT*.5 + DOWN*.5)))
        self.wait()

        self.play(AnimationGroup(Write(points[1]),
                                 text[0][8:14].animate.next_to(points[1]).scale(.7).shift(UP*.3 + LEFT*1.2),
                                 FadeOut(VGroup(text[0][7],
                                                text[0][14:]))))
        self.wait()

        #draw the graph
        graph = coordinate_axes.plot(lambda x: 2*x - 2,
                                     x_range=[-2, 2])

        self.play(Write(graph))
        self.wait()

        linear_function = Tex("$y = kx + b$", font_size=FONT_SIZES['lin_func']).shift(LEFT*3 + UP*3)

        self.play(Write(linear_function))
        self.wait()

        curved_arrow = CurvedArrow(linear_function[0][5].get_bottom(), text[0][5].get_top(), tip_length=.1, angle=-.9)

        self.play(Write(curved_arrow))
        self.wait(2)

        self.play(FadeOut(curved_arrow))
        self.wait()

        self.play(AnimationGroup(FadeOut(linear_function[0][4:]),
                                 text[0][4:6].copy().animate.next_to(linear_function[0][3]).scale(1.6).shift(UP*.05)))
        self.wait(2)

        #drawing arrows from coordinate points to y = kx + b
        text_copy_x = text[0][12].copy()
        text_copy_y = text[0][10].copy()

        arrow_to_x = always_redraw(lambda: Arrow(text[0][12], linear_function[0][3],
                                                 max_stroke_width_to_length_ratio=.5, max_tip_length_to_length_ratio=.1))
        arrow_to_y = always_redraw(lambda: Arrow(text[0][10], linear_function[0][0],
                                                 max_stroke_width_to_length_ratio=.5, max_tip_length_to_length_ratio=.1))

        self.play(Write(VGroup(arrow_to_x,
                               arrow_to_y)))
        self.wait(2)

        self.play(AnimationGroup(text[0][12].animate.move_to(linear_function[0][3]).shift(DOWN*2 + LEFT*.1).scale(1.6),
                                 text[0][10].animate.move_to(linear_function[0][0]).shift(DOWN*1.95 + LEFT*.1).scale(1.6),
                                 FadeIn(VGroup(text_copy_x,
                                               text_copy_y))))
        self.wait(2)

        #Writing equations
        equations = VGroup(MathTex("0 = k\cdot 1 - 2", font_size=FONT_SIZES['lin_func']).move_to(linear_function).shift(DOWN*.7 + RIGHT*.25),
                           MathTex("0 = k - 2", font_size=FONT_SIZES['lin_func']).move_to(linear_function).shift(DOWN*1.4 + LEFT*.15),
                           MathTex("k = 2", font_size=FONT_SIZES['lin_func']).move_to(linear_function).shift(DOWN*2.1 + LEFT*.8),
                           MathTex("y = 2k - 2", font_size=FONT_SIZES['lin_func']).move_to(linear_function).shift(DOWN*2.8 + LEFT*.05))

        self.play(ReplacementTransform(VGroup(arrow_to_x, arrow_to_y, text[0][12], text[0][10]), equations[0]))
        self.wait(2)

        self.play(Write(equations[1]))
        self.wait(2)

        self.play(Write(equations[2]))
        self.wait(2)

        self.play(Write(equations[3]))
        self.wait(2)

        #drawing lines for brace
        line_to_1_2 = Line(coordinate_axes.c2p(0, -2, 0), coordinate_axes.c2p(1, -2, 0))
        line_to_1_0 = Line(coordinate_axes.c2p(1, -2, 0), coordinate_axes.c2p(1, 0, 0))

        self.play(Write(line_to_1_2))
        self.wait()

        self.play(Write(line_to_1_0))
        self.wait(2)

        #drawing the brace
        brace = Brace(VGroup(Dot(point=coordinate_axes.c2p(1, 0, 0)), Dot(point=coordinate_axes.c2p(1, -2, 0))),
                      sharpness=1, direction=RIGHT)

        self.play(Write(brace))
        self.wait(2)

        two_and_k = VGroup(MathTex("2", font_size=FONT_SIZES['graph']).next_to(brace),
                           MathTex("k", font_size=FONT_SIZES['graph']).next_to(brace).shift(RIGHT))

        self.play(Write(two_and_k[0]))
        self.wait(2)

        self.play(Write(two_and_k[1]))
        self.wait(2)

        #drawing curved arrow from k to 2
        arrow_to_2 = CurvedArrow(two_and_k[1].get_bottom(), two_and_k[0].get_bottom(), tip_length=.1, angle=-.9)

        self.play(Write(arrow_to_2))
        self.wait()
