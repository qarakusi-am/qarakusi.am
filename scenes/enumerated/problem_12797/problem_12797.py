from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, Brace, CurvedArrow
from manim import RIGHT, LEFT, UP, DOWN, ORANGE, MovingCameraScene, GREEN
from .text import *
from qarakusiscene import TaskNumberBox

class Problem12797(MovingCameraScene):
    def construct(self):

        #write the task number
        taskNumber = TaskNumberBox(taskNumberString)

        self.add(taskNumber)
        self.wait()

        self.play(FadeOut(taskNumber))
        self.wait(.25)

        if LanguageConfig.is_armenian():
            line_passing_through_points = Tex(line_passing_through_points_string, font_size=55).shift(UP*3 + RIGHT*2.1)
            and_ = Tex(and_string, font_size=55).next_to(line_passing_through_points).shift(LEFT*11.9 + UP*.02)
            point_a = MathTex("A(0, -2)", font_size=55, color=ORANGE).shift(UP*3 + LEFT*6)
            point_b = MathTex("B(1, 0)", font_size=55, color=GREEN).next_to(and_).shift(DOWN*.02)

            self.play(Write(VGroup(point_a,
                                   and_,
                                   point_b,
                                   line_passing_through_points)))
        else:
            line_passing_through_points = Tex(line_passing_through_points_string, font_size=45).to_edge(UP).shift(UP*.1)
            point_a = MathTex("A(0, -2)", font_size=45, color=ORANGE).shift(UP*2.8 + LEFT*2)
            and_ = Tex(and_string, font_size=45).next_to(point_a[0][-1])
            point_b = MathTex("B(1, 0)", font_size=45, color=GREEN).next_to(and_[0][-1])

            self.play(Write(VGroup(line_passing_through_points,
                                   point_a,
                                   and_,
                                   point_b)))

        self.wait()

        #display coordinate axes
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
        ).shift(DOWN*.5)

        self.play(Write(coordinate_system))
        self.wait()

        #display points A and B
        points = VGroup(
            Dot(point=coordinate_system.c2p(0, -2, 0)),
            Dot(point=coordinate_system.c2p(1, 0, 0))
        )

        self.play(AnimationGroup(Write(points[0]),
                                 point_a.animate.next_to(points[0]).scale(.8).shift(DOWN*.3 + LEFT*.5)))
        self.wait()

        self.play(AnimationGroup(Write(points[1]),
                                 point_b.animate.next_to(points[1]).scale(.8).shift(UP*.5 + LEFT*1.3),
                                 FadeOut(VGroup(line_passing_through_points,
                                                and_))))
        self.wait()

        self.add(point_b[0][2].copy().move_to(point_b[0][2]),
                 point_b[0][4].copy().move_to(point_b[0][4]))

        #plot the line
        line = coordinate_system.plot(lambda x: 2*x - 2, x_range=[-2, 2])

        self.play(Write(line))
        self.wait()

        #write linear function formula

        linear_function_formula = Tex("$y = kx + b$", font_size=75).shift(LEFT*3.2 + UP*3.5)

        self.play(Write(linear_function_formula))
        self.wait()

        #find y-intercept
        curved_arrow = CurvedArrow(linear_function_formula[0][5].get_bottom(), coordinate_system.c2p(0, -1.9, 0),
                                   tip_length=.1, angle=-.9)

        self.play(Write(curved_arrow))
        self.wait(2)

        self.play(FadeOut(curved_arrow))
        self.wait()

        self.play(AnimationGroup(FadeOut(linear_function_formula[0][4:]),
                                 point_a[0][4:6].copy().animate.next_to(linear_function_formula[0][3]).scale(1.8).shift(UP*.1)))
        self.wait(2)

        #draw arrows from point B to the formula
        arrow_to_x = always_redraw(lambda: Arrow(point_b[0][4], linear_function_formula[0][0],
                                                 max_stroke_width_to_length_ratio=3,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))
        arrow_to_y = always_redraw(lambda: Arrow(point_b[0][2], linear_function_formula[0][3],
                                                 max_stroke_width_to_length_ratio=3.1,
                                                 max_tip_length_to_length_ratio=.1, buff=.05))

        self.play(AnimationGroup(Write(arrow_to_x),
                                 Write(arrow_to_y)))
        self.wait(2)

        self.play(AnimationGroup(point_b[0][4].animate.move_to(linear_function_formula[0][0]).shift(DOWN*1.95 + LEFT*.1).scale(1.9),
                                 point_b[0][2].animate.move_to(linear_function_formula[0][3]).shift(DOWN*2 + LEFT*.15).scale(1.9)))
        self.wait(2)

        #Write the equations
        equations = VGroup(MathTex("0 = k\cdot 1 - 2", font_size=75).move_to(linear_function_formula).shift(DOWN*.9 +
                                                                                                            RIGHT*.25),
                           MathTex("0 = k - 2", font_size=75).move_to(linear_function_formula).shift(DOWN*1.8 +
                                                                                                     LEFT*.21),
                           MathTex("k = 2", font_size=75).move_to(linear_function_formula).shift(DOWN*2.7 + LEFT*.9),
                           MathTex("y = 2x - 2", font_size=75).move_to(linear_function_formula).shift(DOWN*3.6))

        self.play(ReplacementTransform(VGroup(arrow_to_x, arrow_to_y, point_b[0][4],
                                              point_b[0][2]), equations[0]))
        self.wait(2)

        self.play(Write(equations[1]))
        self.wait(2)

        self.play(Write(equations[2]))
        self.wait(2)

        self.play(Write(equations[3]))
        self.wait(2)

        #moving camera
        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(0.5).shift(DOWN + RIGHT))
        self.wait(2)

        #find the slope
        lines_for_brace = VGroup(Line(coordinate_system.c2p(0, -2, 0), coordinate_system.c2p(1, -2, 0)),
                                 Line(coordinate_system.c2p(1, -2, 0), coordinate_system.c2p(1, 0, 0)))

        self.play(Write(lines_for_brace[0]))
        self.wait()

        self.play(Write(lines_for_brace[1]))
        self.wait(2)

        brace = Brace(VGroup(Dot(point=coordinate_system.c2p(1, -.1, 0)), Dot(point=coordinate_system.c2p(1, -1.9, 0))),
                      sharpness=1.5, direction=RIGHT).shift(LEFT*.25)

        self.play(Write(brace))
        self.wait(2)