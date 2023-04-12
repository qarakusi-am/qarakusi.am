from manim import Write, VGroup, AnimationGroup, ReplacementTransform
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, TransformFromCopy, Brace
from manim import MovingCameraScene, RIGHT, LEFT, UP, DOWN, ORANGE, WHITE, BLUE_C
from .text import *

FONT_SIZE = 60
DOT_SIZE= 40

class Problem12755(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        self.points_to_display=points_to_display = MathTex("A(1,8)",","," B(2,4)",",", "C(3.5,-8)",",","D(-4,7)",",","E(0,4)", font_size=40).shift(UP * 3)
        self.answers=VGroup()

        self.play(Write(points_to_display))
        self.wait()

        self.coordinate_axes=coordinate_axes = Axes(
            x_range=[-4, 4.3, 1],
            y_range=[-8.3, 10.3, 1],
            x_length=11,
            y_length=10,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        ).shift(DOWN * 0.9)

        #move point for display to left
        self.play(AnimationGroup(
            *[points_to_display[i].animate.to_corner(LEFT,UP).shift(DOWN*0.3*i+ RIGHT*0.2+DOWN*1.5) for i in range(0,len(points_to_display[0])+3,2)],
            *[points_to_display[i].animate.set_opacity(0) for i in range(1, len(points_to_display[0])+2, 2)]
            )
        )
        self.wait()

        # create coordinate axis
        self.play(Write(coordinate_axes))
        self.wait(2)

        # write the function
        function_size = 55
        self.function=function = MathTex("y=-1.5x+7", font_size=function_size).shift(RIGHT * 3.2 + UP * 3.4)

        self.play(Write(function))
        self.wait()

        # find y for x=0
        first_point_helpers = VGroup(MathTex("x=0", font_size=function_size).move_to(function, LEFT).shift(DOWN * 0.6),
                                     MathTex("y=", font_size=function_size).move_to(function, LEFT).shift(
                                         DOWN * 0.69 + RIGHT * 1.8),
                                     MathTex("7", font_size=function_size))
        first_point_helpers[2].next_to(first_point_helpers[1], RIGHT).shift(UP * 0.09)

        self.play(Write(first_point_helpers[0]))
        self.wait()

        self.play(Write(first_point_helpers[1]))
        self.wait()

        self.play(TransformFromCopy(function[0][-1], first_point_helpers[2]))
        self.wait()

        self.points=points = VGroup(
            VGroup(Dot(point=coordinate_axes.c2p(0, 7, 0)),
                   Tex("(0, 7)", font_size=DOT_SIZE).next_to(coordinate_axes.c2p(0, 7, 0)), ),
            VGroup(Dot(point=coordinate_axes.c2p(1, 5.5, 0)),
                   Tex("(1, 5.5)", font_size=DOT_SIZE).next_to(coordinate_axes.c2p(1, 5.5, 0)),
                   coordinate_axes.get_horizontal_line(coordinate_axes.c2p(1, 5.5, 0)),
                   coordinate_axes.get_vertical_line(coordinate_axes.c2p(1, 5.5, 0))),
        )
        self.play(TransformFromCopy(first_point_helpers, points[0][0]))
        self.play(Write(points[0][-1]))
        self.wait(2)

        self.play(FadeOut(first_point_helpers))
        self.wait()

        # find y for x=1
        second_point_helpers = VGroup(MathTex("x=1", font_size=function_size).move_to(function, LEFT).shift(DOWN * 0.6),
                                      MathTex("y=-1.5 \cdot 1 + 7", font_size=function_size).move_to(function,
                                                                                                           LEFT).shift(
                                          DOWN * 0.64 + RIGHT * 1.8),
                                      MathTex("5.5", font_size=function_size))

        self.play(Write(second_point_helpers[0]))
        self.wait()

        self.play(Write(second_point_helpers[1]))
        self.wait()

        second_point_helpers[2].move_to(second_point_helpers[1][0][2],LEFT)
        self.play(ReplacementTransform(VGroup(second_point_helpers[1][0][2:]),second_point_helpers[2]))
        self.wait()

        self.play(ReplacementTransform(second_point_helpers,points[1][0],run_time=2))
        self.play(Write(points[1][1:],run_time=3))
        self.wait(2)

        #divide graph into 2 parts
        dividing_line=coordinate_axes.plot(lambda x: -1.5*x+7, x_range=[-15, 15])

        self.play(Write(dividing_line,run_time=2))
        self.wait(2)

        area_above_dividing_line = coordinate_axes.get_area(
            graph=coordinate_axes.plot(lambda x:-x+30, x_range=[-15, 15],),
            bounded_graph=dividing_line,
            x_range=(-15,15),
            color=(ORANGE),
            opacity=0.5,
        )
        area_under_dividing_line = coordinate_axes.get_area(
            graph=coordinate_axes.plot(lambda x: -x - 30, x_range=[-15, 15]),
            bounded_graph=dividing_line,
            x_range=(-15, 15),
            color=(BLUE_C),
            opacity=0.5,
        )
        area_position_texts=VGroup(
            Tex(above_line,font_size=FONT_SIZE).move_to(function,LEFT).shift(DOWN),
            Tex(below_line, font_size=FONT_SIZE).move_to(function, LEFT).shift(DOWN*2+LEFT*6)
        )
        area_above_dividing_line.z_index=area_above_dividing_line.z_index-1
        area_under_dividing_line.z_index=area_under_dividing_line.z_index-1

        self.play(AnimationGroup(Write(area_above_dividing_line)))
        self.play(FadeOut(points[0]))
        self.wait(2)

        self.play(Write(area_under_dividing_line))
        self.wait()

        self.play(Write(area_position_texts[0]))
        self.wait()

        self.play(Write(area_position_texts[1]))
        self.wait()

        self.play(FadeOut(area_position_texts))
        self.wait()

        self.solve_for_point_a()
        self.solve_for_point_b()
        self.solve_for_point_c()
        self.solve_for_point_d()
        self.solve_for_point_e()



    def solve_for_point_a(self):

        coordinate_axes=self.coordinate_axes

        #display point on the graph
        point = VGroup(
            Dot(point=coordinate_axes.c2p(1, 8, 0), color=WHITE),
            MathTex("A(1,8)", font_size=DOT_SIZE, color=WHITE).next_to(coordinate_axes.c2p(1, 8, 0)),
            coordinate_axes.get_horizontal_line(coordinate_axes.c2p(1, 8, 0), color=WHITE),
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(1, 8, 0), color=WHITE)),

        self.play(TransformFromCopy(self.points_to_display[0], point[0][0]))
        self.play(Write(point[0][1:]))
        self.wait(2)

        lines = VGroup(Line(coordinate_axes.c2p(1, 0, 0), coordinate_axes.c2p(1, 5.5, 0), stroke_width=3),
                       Line(coordinate_axes.c2p(1, 0, 0), coordinate_axes.c2p(1, 8, 0), stroke_width=3))
        braces = VGroup(Brace(lines[0], direction=(-1., 0., 0.), sharpness=1),
                        Brace(lines[1], direction=(1., 0., 0.), sharpness=1), )
        line_lengths = VGroup(MathTex("5.5", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT).shift(RIGHT*0.15),
                              MathTex("8", font_size=DOT_SIZE, color=WHITE).next_to(braces[1], RIGHT))

        self.play(Write(lines[0]))
        self.wait()

        self.play(Write(braces[0]))
        self.wait()

        self.play(Write(line_lengths[0]))


        self.play(self.camera.frame.animate.scale(0.8).shift(UP+RIGHT))
        self.wait()

        self.play(Write(lines[1]))
        self.wait()
        self.play(Write(braces[1]))
        self.wait()
        self.play(Write(line_lengths[1]))
        self.wait()

        #write the conclusion
        conclusion = Tex("$8 > 5.5,$", hence_str, " \\\\ $A$ ", is_str, above_str, str_suffix, font_size=50).shift(RIGHT*4.3 + UP*2.3)
        self.play(Write(conclusion, run_time=2))
        self.wait(2)

        self.play(self.camera.frame.animate.restore())
        self.wait()

        self.play(FadeOut(conclusion[0:4], conclusion[-1], braces, lines, line_lengths))
        self.wait()

        #add conclusion to answers, to shift it left in solve_for_point_d
        self.answers.add(conclusion[4])

        self.play(conclusion[4].animate.next_to(self.points_to_display[0]))
        self.wait()

        self.play(FadeOut(point[0][0:],self.points[1]))
        self.wait(2)

    def solve_for_point_b(self):

        coordinate_axes = self.coordinate_axes

        # display point on the graph
        point = VGroup(
            Dot(point=coordinate_axes.c2p(2, 4, 0), color=WHITE),
            MathTex("B(2,4)", font_size=DOT_SIZE, color=WHITE).next_to(coordinate_axes.c2p(2, 4,  0)),
            coordinate_axes.get_horizontal_line(coordinate_axes.c2p(2, 4,  0), color=WHITE),
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(2, 4,  0), color=WHITE)),

        self.play(TransformFromCopy(self.points_to_display[2], point[0][0]))
        self.play(Write(point[0][1:]))
        self.wait(2)

        lines = VGroup(Line(coordinate_axes.c2p(2, 0, 0), coordinate_axes.c2p(2, 4, 0), stroke_width=3),
                       Line(coordinate_axes.c2p(2, 0, 0), coordinate_axes.c2p(2, 4,  0), stroke_width=3))
        braces = VGroup(Brace(lines[0], direction=(-1., 0., 0.), sharpness=1),
                        Brace(lines[1], direction=(1., 0., 0.), sharpness=1))
        line_lengths = VGroup(MathTex("4", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT),
                              MathTex("4", font_size=DOT_SIZE, color=WHITE).next_to(braces[1], RIGHT))

        equation_for_line_length=MathTex(" -1.5\cdot2+7 ", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT).shift(RIGHT*0.25)

        self.play(Write(lines[0]))
        self.wait()

        self.play(Write(braces[0]))
        self.wait()

        self.play(Write(equation_for_line_length))
        self.wait()

        self.play(ReplacementTransform(equation_for_line_length,line_lengths[0]))
        self.wait()

        self.play(Write(lines[1]))
        self.wait()

        self.play(Write(braces[1]))
        self.wait()

        self.play(Write(line_lengths[1]))
        self.wait()

        #write the conclusion
        conclusion = Tex("$4 = 4,$ ", hence_str, "\\\\$B$", is_str_for_on_case, on_str,str_suffix, font_size=50).shift(RIGHT*3 + UP*2.3)

        self.play(Write(conclusion, run_time=2))
        self.wait(2)

        self.play(FadeOut(conclusion[0:4], conclusion[-1], braces, lines, line_lengths))
        self.wait()

        #add conclusion to answers, to shift it left in solve_for_point_d
        self.answers.add(conclusion[4])

        self.play(conclusion[4].animate.next_to(self.points_to_display[2]))
        self.wait()

        self.play(FadeOut(point[0][0:]))
        self.wait(2)

    def solve_for_point_c(self):
        #scale camera
        self.play(AnimationGroup(self.camera.frame.animate.scale(1.3).shift(DOWN*2),self.function.animate.shift(DOWN*0.7)))
        self.wait()

        coordinate_axes = self.coordinate_axes

        # display point on the graph
        point = VGroup(
            Dot(point=coordinate_axes.c2p(3.5, -8, 0), color=WHITE),
            MathTex("C(3.5,-8)", font_size=DOT_SIZE, color=WHITE).next_to(coordinate_axes.c2p(3.5, -8,  0)),
            coordinate_axes.get_horizontal_line(coordinate_axes.c2p(3.5, -8,   0), color=WHITE),
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(3.5, -8,   0), color=WHITE)),

        self.play(TransformFromCopy(self.points_to_display[4], point[0][0]))
        self.wait()

        self.play(Write(point[0][1:]))
        self.wait(2)

        lines = VGroup(Line(coordinate_axes.c2p(3.5, 0, 0), coordinate_axes.c2p(3.5, 1.75, 0), stroke_width=3),
                       Line(coordinate_axes.c2p(3.5, 0, 0), coordinate_axes.c2p(3.5, -8,  0), stroke_width=3))
        braces = VGroup(Brace(lines[0], direction=(-1., 0., 0.), sharpness=1),
                        Brace(lines[1], direction=(1., 0., 0.), sharpness=1))
        line_lengths = VGroup(MathTex(
                                      "1.75", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT),
                              MathTex("8", font_size=DOT_SIZE, color=WHITE).next_to(braces[1], RIGHT))
        equations_for_line_length=MathTex(" -1.5\cdot3.5+7", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT)

        self.play(Write(lines[0]))
        self.wait()

        self.play(Write(braces[0]))
        self.wait()

        self.play(Write(equations_for_line_length))
        self.wait()

        self.play(ReplacementTransform(equations_for_line_length,line_lengths[0]))
        self.wait()

        self.play(Write(lines[1]))
        self.wait()

        self.play(Write(braces[1]))
        self.wait()

        self.play(Write(line_lengths[1]))
        self.wait()

        #write the conclusion
        conclusion = Tex("$1.75 > -8,$ ", hence_str, "\\\\$C$", is_str, below_str, str_suffix, font_size=50).shift(RIGHT*3.7+ UP*1.8)
        self.play(Write(conclusion, run_time=2))
        self.wait(2)

        self.play(FadeOut(conclusion[0:4], conclusion[-1], braces, lines, line_lengths))
        self.wait()
        #add conclusion to answers, to shift it left in solve_for_point_d
        self.answers.add(conclusion[4])

        self.play(conclusion[4].animate.next_to(self.points_to_display[4]))
        self.wait()

        self.play(FadeOut(point[0][0:]))
        self.wait(2)

    def solve_for_point_d(self):

        #scale cameraVGroup
        self.play(AnimationGroup(VGroup(self.points_to_display,self.answers).animate.shift(LEFT*2.5),
                  self.camera.frame.animate.scale(0.9).shift(UP*3+LEFT*1.5)))
        self.wait(2)

        coordinate_axes = self.coordinate_axes

        # display point on the graph
        point = VGroup(
            Dot(point=coordinate_axes.c2p(-4,7, 0), color=WHITE),
            MathTex("D(-4,7)", font_size=DOT_SIZE, color=WHITE).next_to(coordinate_axes.c2p(-4,7, 0)).shift(UP*0.3),
            coordinate_axes.get_horizontal_line(coordinate_axes.c2p(-4,7, 0), color=WHITE),
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(-4,7, 0), color=WHITE)),

        self.play(TransformFromCopy(self.points_to_display[6], point[0][0]))
        self.play(Write(point[0][1:]))
        self.wait(2)

        lines = VGroup(Line(coordinate_axes.c2p(-4, 0, 0), coordinate_axes.c2p(-4,13, 0), stroke_width=3),
                       Line(coordinate_axes.c2p(-4, 0, 0), coordinate_axes.c2p(-4,7, 0), stroke_width=3))
        braces = VGroup(Brace(lines[0], direction=(-1., 0., 0.), sharpness=1),
                        Brace(lines[1], direction=(1., 0., 0.), sharpness=1))
        line_lengths = VGroup(MathTex("13", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT).shift(RIGHT*0.1),
                              MathTex("7", font_size=DOT_SIZE, color=WHITE).next_to(braces[1], RIGHT))

        self.play(Write(lines[0]))
        self.wait()

        self.play(Write(braces[0]))
        self.wait()

        self.play(Write(line_lengths[0]))
        self.wait()

        self.play(Write(lines[1]))
        self.wait()

        self.play(Write(braces[1]))
        self.wait()

        self.play(Write(line_lengths[1]))
        self.wait()

        #write the conclusion
        conclusion = Tex(below_str, font_size=50).next_to(self.points_to_display[6])

        self.play(Write(conclusion, run_time=2))
        self.wait()

        self.play(FadeOut( braces, lines, line_lengths,point[0][0:]))
        self.wait(2)

    def solve_for_point_e(self):
        coordinate_axes = self.coordinate_axes
        # display point on the graph
        point = VGroup(
            Dot(point=coordinate_axes.c2p(0,4, 0), color=WHITE),
            MathTex("E(0,4)", font_size=DOT_SIZE, color=WHITE).next_to(coordinate_axes.c2p(0,4, 0)),
            coordinate_axes.get_horizontal_line(coordinate_axes.c2p(0,4, 0), color=WHITE),
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(0,4, 0), color=WHITE)),

        self.play(TransformFromCopy(self.points_to_display[8], point[0][0]))
        self.play(Write(point[0][1:]))
        self.wait(2)

        lines = VGroup(Line(coordinate_axes.c2p(0, 0, 0), coordinate_axes.c2p(0,7, 0), stroke_width=3),
                       Line(coordinate_axes.c2p(0, 0, 0), coordinate_axes.c2p(0,4, 0), stroke_width=3))

        braces = VGroup(Brace(lines[0], direction=(-1., 0., 0.), sharpness=1).shift(LEFT*0.3),
                        Brace(lines[1], direction=(1., 0., 0.), sharpness=1) )

        line_lengths = VGroup(MathTex("7", font_size=DOT_SIZE, color=WHITE).next_to(braces[0], LEFT),
                              MathTex("4", font_size=DOT_SIZE, color=WHITE).next_to(braces[1], RIGHT))

        self.play(Write(braces[0]))
        self.wait()

        self.play(Write(line_lengths[0]))
        self.wait()

        self.play(Write(braces[1]))
        self.wait()

        self.play(Write(line_lengths[1]))
        self.wait()
        # write the conclusion
        conclusion = Tex(below_str, font_size=50).next_to(self.points_to_display[8])

        self.play(Write(conclusion, run_time=2))
        self.wait()

        self.play(FadeOut(braces, lines, line_lengths,point[0][0:]))
        self.wait(2)

