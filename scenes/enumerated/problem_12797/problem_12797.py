from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw, Create
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, Brace
from manim import RIGHT, LEFT, UP, DOWN, ORANGE, MovingCameraScene, GREEN
from .text import *
from qarakusiscene import TaskNumberBox

FONT_SIZE=75
class Problem12797(MovingCameraScene):
    def construct(self):
        # write the task number
        taskNumber = TaskNumberBox(taskNumberString)

        self.add(taskNumber)
        self.wait()

        self.play(FadeOut(taskNumber))
        self.wait(.25)

        line_passing_through_points = Tex(line_passing_through_points_string, font_size=55).shift(UP * 3)
        line_passing_through_points[0][:7].set_color(ORANGE)

        line_passing_through_points[0][8:14].set_color(GREEN)

        self.play(Write(line_passing_through_points))
        self.wait()

        # display coordinate system
        coordinate_system = Axes(
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
        ).shift(DOWN * .5)

        self.play(Write(coordinate_system))
        self.wait()

        # display points A and B
        points = VGroup(
            Dot(point=coordinate_system.c2p(0, -2, 0)),
            Dot(point=coordinate_system.c2p(1, 0, 0))
        )

        self.play(AnimationGroup(Write(points[0]),
                                 line_passing_through_points[0][:7].animate.next_to(points[0]).scale(.8).shift(
                                     DOWN * .3 +LEFT * .5)))
        self.wait()

        self.play(AnimationGroup(Write(points[1]),
                                 line_passing_through_points[0][8:14].animate.next_to(points[1]).scale(.8).shift(
                                     UP * .5 +LEFT * 1.3),
                                 FadeOut(line_passing_through_points[0][7],
                                                line_passing_through_points[0][14:])))
        self.wait()

        self.add(line_passing_through_points[0][12].copy().move_to(line_passing_through_points[0][12]),
                 line_passing_through_points[0][10].copy().move_to(line_passing_through_points[0][10]))

        # plot the line
        line = coordinate_system.plot(lambda x: 2 * x - 2, x_range=[-2, 2])

        self.play(Write(line))
        self.wait(2)

        # write linear function formula

        linear_function_formula = Tex("$y = kx + b$", font_size=75).shift(LEFT * 3.2 + UP * 3.5)

        self.play(Write(linear_function_formula))
        self.wait(1.5)

        # find y-intercept
        arrow = Arrow(linear_function_formula[0][5].get_bottom(), coordinate_system.c2p(-.03, -1.92, 0),
                                   tip_length=.2,max_stroke_width_to_length_ratio=0.8).scale(1.1)

        self.play(Write(arrow))
        self.wait(2)

        self.play(FadeOut(arrow))
        self.wait()

        self.play(AnimationGroup(FadeOut(linear_function_formula[0][4:]),
                                 line_passing_through_points[0][4:6].copy().animate.next_to(
                                     linear_function_formula[0][3]).scale(1.8).shift(UP * .1)))
        self.wait(2)

        # draw arrows from point B to the formula
        arrow_to_x = always_redraw(lambda: Arrow(line_passing_through_points[0][12], linear_function_formula[0][0],
                                                 max_stroke_width_to_length_ratio=3,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))
        arrow_to_y = always_redraw(lambda: Arrow(line_passing_through_points[0][10], linear_function_formula[0][3],
                                                 max_stroke_width_to_length_ratio=3.1,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))

        self.play(AnimationGroup(Create(arrow_to_x),
                                 Write(arrow_to_y)))
        self.wait(2)

        self.play(AnimationGroup(
            line_passing_through_points[0][12].animate.move_to(linear_function_formula[0][0]).shift(
                DOWN * 1.95 + LEFT * .1).scale(1.9),
            line_passing_through_points[0][10].animate.move_to(linear_function_formula[0][3]).shift(
                DOWN * 2 + LEFT * .15).scale(1.9)))
        self.wait(2)

        # Write the equations
        equations = VGroup(
            MathTex("0 = k\cdot 1 - 2", font_size=FONT_SIZE).move_to(linear_function_formula).shift(DOWN * .9 + RIGHT * .25),
            MathTex("0 = k - 2", font_size=FONT_SIZE).move_to(linear_function_formula).shift(DOWN * 1.8 + LEFT * .21),
            MathTex("k = 2", font_size=FONT_SIZE).move_to(linear_function_formula).shift(DOWN * 2.7 + LEFT * .9),
            MathTex("y = 2x - 2", font_size=FONT_SIZE).move_to(linear_function_formula).shift(DOWN * 3.6))

        self.play(ReplacementTransform(VGroup(arrow_to_x, arrow_to_y, line_passing_through_points[0][12],
                                              line_passing_through_points[0][10]), equations[0]))
        self.wait(2)

        for i in range(1,4):
            self.play(Write(equations[i]))
            self.wait(2)

        # moving camera
        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(0.5).shift(DOWN + RIGHT))
        self.wait(2)

        # find the slope
        lines_for_brace = VGroup(Line(coordinate_system.c2p(0, -2, 0), coordinate_system.c2p(1, -2, 0)),
                                 Line(coordinate_system.c2p(1, -2, 0), coordinate_system.c2p(1, 0, 0)))

        self.play(Write(lines_for_brace[0]))
        self.wait()

        self.play(Write(lines_for_brace[1]))
        self.wait(2)

        brace = Brace(VGroup(Dot(point=coordinate_system.c2p(1, -.1, 0)), Dot(point=coordinate_system.c2p(1, -1.9, 0))),
                      sharpness=1.5, direction=RIGHT).shift(LEFT * .25)

        self.play(Write(brace))
        self.wait(1)

        brace_length = MathTex("2", font_size=FONT_SIZE).next_to(brace).shift(LEFT * .25)

        self.play(Write(brace_length))
        self.wait(2)

        self.play(self.camera.frame.animate.restore())
        self.wait()
