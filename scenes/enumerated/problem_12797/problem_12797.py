from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, Brace, CurvedArrow
from manim import RIGHT, LEFT, UP, DOWN, ORANGE, Scene, GREEN
from .text import *
from qarakusiscene import TaskNumberBox

class Problem12797(Scene):
    def construct(self):
        #writing task number
        taskNumber = TaskNumberBox(taskNumberString)

        self.add(taskNumber)
        self.wait()

        self.play(FadeOut(taskNumber))
        self.wait(.25)

        #Writing the problem
        text = Tex(a_line_through_the_points, font_size=55).shift(UP*3)
        text[0][:7].set_color(ORANGE)

        text[0][8:14].set_color(GREEN)

        self.play(Write(text))
        self.wait()

        #displaying coordinate axes
        coordinate_axes = Axes(
            x_range=[-3, 3.4, 1],
            y_range=[-6, 6.4, 1],
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
                                 text[0][:7].animate.next_to(points[0]).scale(.7).shift(DOWN*.3 + LEFT*.5)))
        self.wait()

        self.play(AnimationGroup(Write(points[1]),
                                 text[0][8:14].animate.next_to(points[1]).scale(.7).shift(UP*.5 + LEFT*1.3),
                                 FadeOut(VGroup(text[0][7],
                                                text[0][14:]))))
        self.wait()

        self.add(text[0][12].copy().next_to(text[0][9]).shift(UP*.03 + RIGHT*.17),
                 text[0][10].copy().next_to(text[0][8]).shift(LEFT*.017))

        #draw the graph
        graph = coordinate_axes.plot(lambda x: 2*x - 2,
                                     x_range=[-2, 2])

        self.play(Write(graph))
        self.wait()

        linear_function = Tex("$y = kx + b$", font_size=75).shift(LEFT*3.2 + UP*3.5)

        self.play(Write(linear_function))
        self.wait()

        curved_arrow = CurvedArrow(linear_function[0][5].get_bottom(), text[0][5].get_top(), tip_length=.1, angle=-.9)

        self.play(Write(curved_arrow))
        self.wait(2)

        self.play(FadeOut(curved_arrow))
        self.wait()

        self.play(AnimationGroup(FadeOut(linear_function[0][4:]),
                                 text[0][4:6].copy().animate.next_to(linear_function[0][3]).scale(1.8).shift(UP*.05)))
        self.wait(2)

        #drawing arrows from coordinate points to y = kx + b

        arrow_to_x = always_redraw(lambda: Arrow(text[0][12], linear_function[0][0],
                                                 max_stroke_width_to_length_ratio=.8,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))
        arrow_to_y = always_redraw(lambda: Arrow(text[0][10], linear_function[0][3],
                                                 max_stroke_width_to_length_ratio=.8,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))

        self.play(Write(VGroup(arrow_to_x,
                               arrow_to_y)))
        self.wait(2)

        self.play(AnimationGroup(text[0][12].animate.move_to(linear_function[0][0]).shift(DOWN*1.95 + LEFT*.1).scale(1.8),
                                 text[0][10].animate.move_to(linear_function[0][3]).shift(DOWN*2 + LEFT*.15).scale(1.8)))
        self.wait(2)

        #Writing equations
        equations = VGroup(MathTex("0 = k\cdot 1 - 2", font_size=75).move_to(linear_function).shift(DOWN*.9 + RIGHT*.25),
                           MathTex("0 = k - 2", font_size=75).move_to(linear_function).shift(DOWN*1.8 + LEFT*.21),
                           MathTex("k = 2", font_size=75).move_to(linear_function).shift(DOWN*2.7 + LEFT*.9),
                           MathTex("y = 2x - 2", font_size=75).move_to(linear_function).shift(DOWN*3.6))

        self.play(ReplacementTransform(VGroup(arrow_to_x, arrow_to_y, text[0][12], text[0][10]), equations[0]))
        self.wait(2)

        self.play(Write(equations[1]))
        self.wait(2)

        self.play(Write(equations[2]))
        self.wait(2)

        self.play(Write(equations[3]))
        self.wait(2)

        #drawing lines for brace
        lines_for_brace = VGroup(Line(coordinate_axes.c2p(0, -2, 0), coordinate_axes.c2p(1, -2, 0)),
                                 Line(coordinate_axes.c2p(1, -2, 0), coordinate_axes.c2p(1, 0, 0)))

        self.play(Write(lines_for_brace[0]))
        self.wait()

        self.play(Write(lines_for_brace[1]))
        self.wait(2)

        #drawing the brace
        brace = Brace(VGroup(Dot(point=coordinate_axes.c2p(1, -.1, 0)), Dot(point=coordinate_axes.c2p(1, -1.9, 0))),
                      sharpness=1.5, direction=RIGHT).shift(LEFT*.25)

        self.play(Write(brace))
        self.wait(2)

        helper = MathTex("k=2", font_size=45).next_to(brace).shift(LEFT*.25)

        self.play(Write(helper))
        self.wait(2)