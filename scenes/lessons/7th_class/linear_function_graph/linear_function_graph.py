from manim import Write, VGroup, AnimationGroup, ValueTracker, Transform
from manim import Dot, Arrow, FadeOut, Line, DashedLine, CurvedArrow
from manim import MathTex, Tex, MathTable, Axes, TransformFromCopy, always_redraw, SurroundingRectangle
from manim import Scene, RIGHT, LEFT, UP, DOWN, YELLOW, RED, GREEN, ORANGE, BLACK, WHITE
from .text import *

FONT_SIZE = 60

class LinearFunctionGraph(Scene):
    def construct(self):

        lin_function = Tex(linear_function_str, font_size=FONT_SIZE).shift(UP*3)

        functions = VGroup(MathTex("y = kx + b", font_size=55).move_to(lin_function).shift(DOWN*1),
                           MathTex("k = 2", font_size=45).move_to(lin_function).shift(DOWN*1.5 + LEFT*5.5),
                           MathTex("b = 3", font_size=45).move_to(lin_function).shift(DOWN*2 + LEFT*5.5),
                           MathTex("y = 2x + ", font_size=45).move_to(lin_function).shift(DOWN + LEFT*5.2),
                           MathTex("y = 2x", font_size=45).shift(UP*3.2 + RIGHT*5),
                           MathTex("y = 3x", font_size=45).shift(UP*3.6 + RIGHT*4.5),
                           MathTex("-", font_size=45).move_to(lin_function).shift(LEFT*4.5)
                           )

        self.play(Write(lin_function))
        self.wait(0.5)

        self.play(Write(functions[0]))
        self.wait()

        coordinate_system = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 7, 1],
            x_length=9,
            y_length=7.5,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True
        ).shift(RIGHT*1.5)

        x_label = coordinate_system.get_x_axis_label("x")
        y_label = coordinate_system.get_y_axis_label("y", edge=RIGHT, direction=RIGHT, buff=0.4).shift(UP*3.4)

        axis_labels = VGroup(x_label, y_label)

        self.play(lin_function.animate.shift(LEFT*4),
                  functions[0].animate.shift(LEFT*4.8))
        self.wait()

        self.play(Write(coordinate_system),
                  Write(axis_labels))
        self.wait()

        rand_lines = VGroup(
            Line(LEFT, RIGHT, color=GREEN).shift(RIGHT*1),
            Line(LEFT*2, RIGHT*1.5, color=YELLOW).shift(UP*2.5 + RIGHT*1),
            Line(LEFT*0.5, RIGHT*2.5, color=RED).shift(DOWN*1.5 + LEFT*1)
        )

        self.play(Write(rand_lines))
        self.wait(2)

        self.play(FadeOut(rand_lines))
        self.wait()

        self.play(Write(functions[1:3]))
        self.wait()

        k = ValueTracker(3)
        time_k = always_redraw(lambda: MathTex(str(round(k.get_value(), 2)),
                                               font_size=45).next_to(functions[0]).shift(LEFT*.2 + UP*.02))

        self.play(Transform(functions[0], VGroup(functions[3], time_k)))
        self.wait()

        graph_1 = coordinate_system.plot(lambda x: 2*x, x_range=[-3, 3])

        self.play(Write(graph_1))
        self.play(Write(functions[4]))
        self.wait()

        table = VGroup(MathTable(
                        [["x", "1"],
                         ["2x", "2"],
                         ["2x+3", "5"]],
                        include_outer_lines=True
                        ).shift(LEFT*5.3 + UP*1.5).scale(0.5),
                       MathTable(
                           [["2"],
                            ["4"],
                            ["7"]],
                           include_outer_lines=True
                       ).shift(LEFT*3.89 + UP*1.5).scale(0.5),
                       MathTable(
                           [["0"],
                            ["0"],
                            ["3"]],
                           include_outer_lines=True
                       ).shift(LEFT*3.15 + UP*1.5).scale(0.5),
                       MathTable(
                           [["-2"],
                            ["-4"],
                            ["-1"]],
                           include_outer_lines=True
                       ).shift(LEFT*2.33 + UP*1.5).scale(0.5))

        table[0][0][5].color = BLACK

        self.play(FadeOut(VGroup(lin_function)))
        self.wait()

        self.play(FadeOut(functions[1:3]))
        self.wait()

        self.play(functions[0].animate.shift(UP),
                  time_k.animate.shift(UP))

        self.play(Write(table[0]))
        self.wait(2)

        points = VGroup(VGroup(
                            Dot(point=coordinate_system.c2p(1, 2, 0), color=ORANGE),
                            Tex("(1, 2)", font_size=35, color=ORANGE).next_to(coordinate_system.c2p(1, 2, 0)),
                            coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 2, 0), color=ORANGE),
                            coordinate_system.get_vertical_line(coordinate_system.c2p(1, 2, 0), color=ORANGE)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(1, 5,  0), color=GREEN),
                           Tex("(1, 5)", font_size=35, color=GREEN).next_to(coordinate_system.c2p(1, 5, 0)),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 5, 0), color=GREEN),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(1, 5, 0), color=GREEN)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(2, 4, 0), color=ORANGE),
                           Tex("(2, 4)", font_size=35, color=ORANGE).next_to(coordinate_system.c2p(2, 4, 0)),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(2, 4, 0), color=ORANGE),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(2, 4, 0), color=ORANGE)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(2, 7, 0), color=GREEN),
                           Tex("(2, 7)", font_size=35, color=GREEN).next_to(coordinate_system.c2p(2, 7, 0)),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(2, 7, 0), color=GREEN),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(2, 7, 0), color=GREEN)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(0, 0, 0), color=ORANGE),
                           Tex("(0, 0)", font_size=35, color=ORANGE).next_to(coordinate_system.c2p(0, 0, 0)).shift(DOWN*.4 + LEFT*.1),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 0, 0), color=ORANGE),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(0, 0, 0), color=ORANGE)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(0, 3, 0), color=GREEN),
                           Tex("(0, 3)", font_size=35, color=GREEN).next_to(coordinate_system.c2p(0, 3, 0)).shift(LEFT*1.5 + UP*.1),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 3, 0), color=GREEN),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(0, 3, 0), color=GREEN)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(-2, -4, 0), color=ORANGE),
                           Tex("(-2, -4)", font_size=35, color=ORANGE).next_to(coordinate_system.c2p(-2, -4, 0)).shift(LEFT*1.5),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(-2, -4, 0), color=ORANGE),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(-2, -4, 0), color=ORANGE)
                       ),
                       VGroup(
                           Dot(point=coordinate_system.c2p(-2, -1, 0), color=GREEN),
                           Tex("(-2, -1)", font_size=35, color=GREEN).next_to(coordinate_system.c2p(-2, -1, 0)).shift(LEFT*1.5),
                           coordinate_system.get_horizontal_line(coordinate_system.c2p(-2, -1, 0), color=GREEN),
                           coordinate_system.get_vertical_line(coordinate_system.c2p(-2, -1, 0), color=GREEN)
                       )
                       )

        #display first point
        self.play(TransformFromCopy(VGroup(table[0][0][1], table[0][0][3]), points[0][0]))
        self.wait(0.5)

        self.play(Write(points[0][1:]))
        self.wait()

        table[0][0][5].color = WHITE
        self.play(Write(table[0][0][5]))
        self.wait()

        #display second point
        self.play(TransformFromCopy(VGroup(table[0][0][1], table[0][0][5]), points[1][0]))
        self.wait(0.5)

        self.play(Write(points[1][1:]))
        self.wait()

        arrows = VGroup(
            VGroup(DashedLine(points[0][0], points[1][0], dashed_ratio=0.5),
                   Arrow(points[0][0], points[1][0], max_stroke_width_to_length_ratio=0).shift(UP*.25)),
            VGroup(DashedLine(points[2][0], points[3][0], dashed_ratio=0.5),
                   Arrow(points[2][0], points[3][0], max_stroke_width_to_length_ratio=0).shift((UP*0.25))),
            VGroup(DashedLine(points[6][0], points[7][0], dashed_ratio=0.5),
                   Arrow(points[6][0], points[7][0], max_stroke_width_to_length_ratio=0).shift(UP*0.25))
        )

        t = ValueTracker(3)
        time = always_redraw(lambda: MathTex(str(round(t.get_value(), 2)),
                                             font_size=35).next_to(arrows[0]).shift(LEFT*.9))

        self.play(Write(VGroup(arrows[0],
                               time)),
                  FadeOut(VGroup(points[0][2:],
                                 points[1][2:])))
        self.wait()

        self.play(Write(table[1]))
        self.wait()

        #display third point
        self.play(TransformFromCopy(VGroup(table[1][0][0], table[1][0][1]), points[2][0]))
        self.wait(0.5)

        self.play(Write(points[2][1:]))
        self.wait()

        #display fourth point
        self.play(TransformFromCopy(VGroup(table[1][0][0], table[1][0][2]), points[3][0]),
                  Write(points[3][1:]))
        self.wait()

        self.play(Write(arrows[1]),
                  FadeOut(VGroup(points[2][2:],
                                 points[3][2:])))
        self.wait()

        self.play(Write(table[2]))
        self.wait()

        #display fifth and sixth points
        self.play(TransformFromCopy(VGroup(table[2][0][0], table[2][0][1]), points[4][0]),
                  TransformFromCopy(VGroup(table[2][0][0], table[2][0][2]), points[5][0])
                  )
        self.wait(0.5)
        self.play(Write(VGroup(points[4][1:], points[5][1:])))
        self.wait()

        self.play(Write(table[3]))
        self.wait()

        #display seventh point
        self.play(TransformFromCopy(VGroup(table[3][0][0], table[3][0][1]), points[6][0]),
                  TransformFromCopy(VGroup(table[3][0][0], table[3][0][2]), points[7][0])
                  )
        self.wait(0.5)

        self.play(Write(VGroup(points[6][1:], points[7][1:])))
        self.wait()

        self.play(Write(arrows[2]),
                  FadeOut(VGroup(points[6][2:],
                                 points[7][2:])))

        #display points for 2x + 3
        dotes = VGroup()
        x = -3
        while x <= 3:
            dotes.add(Dot(point=coordinate_system.c2p(x, 2*x, 0), color=GREEN))
            x = x + 0.5

        self.play(Write(dotes, run_time=.5))
        self.wait()

        self.play(FadeOut(table))
        self.wait()

        for i in dotes:
            i.shift(UP*1.9)

        self.play(Write(dotes))
        self.wait()

        time_k.set_color(ORANGE)

        self.play(time_k.animate.scale(1.1))
        self.wait()

        graph_2 = coordinate_system.plot(lambda x: 2 * x + 2.5, [-4, 2.5])
        self.play(Write(graph_2))
        self.wait()

        self.play(t.animate.set_value(2.50),
                  k.animate.set_value(2.50),
                  arrows.animate.shift(DOWN*.17).scale(.8))
        self.wait()

        self.play(FadeOut(VGroup(points[1][:2],
                                 points[3][:2],
                                 points[5][:2],
                                 points[7][:2])))

        for i in dotes:
            i.shift(DOWN*.34)

        self.play(Write(dotes, run_time=.5))
        self.wait()

        self.play(t.animate.set_value(0),
                  k.animate.set_value(0))
        self.wait(.5)

        self.play(FadeOut(time))
        self.wait()

        for i in dotes:
            i.shift(DOWN*1.56)

        self.play(Write(dotes, run_time=.5))
        self.wait()

        self.play(FadeOut(arrows))
        self.wait()

        time = always_redraw(lambda: MathTex(str(round(t.get_value(), 2)),
                                             font_size=35).move_to(points[2]).shift(DOWN*.71 + LEFT*.75))

        graph_3 = coordinate_system.plot(lambda x: 2 * x - 2, [-4, 2.5])
        self.play(Write(VGroup(graph_3,
                               time)),
                  t.animate.set_value(2),
                  k.animate.set_value(2),
                  Transform(functions[0][0][-1], functions[-1]))

        for i in dotes:
            i.shift(DOWN*1.23)

        self.play(Write(dotes, run_time=.5))
        self.wait()

        arrows[0].shift(DOWN*1.4).scale(.7)
        arrows[1].shift(DOWN*1.4).scale(.7)

        self.play(Write(arrows[:2]),
                  FadeOut(arrows[-1]))
        self.wait()

        self.play(FadeOut(VGroup(graph_2,
                                 graph_3,
                                 arrows[0][:2],
                                 arrows[1:],
                                 points[0][:2],
                                 points[2][:2],
                                 points[4][:2],
                                 points[6][:2],
                                 dotes,
                                 time,
                                 time_k,
                                 functions[0],
                                 functions[-1]
                                 )),
                  Write(points[5]))
        self.wait()

        self.play(coordinate_system.animate.shift(RIGHT),
                  x_label.animate.shift(RIGHT),
                  y_label.animate.shift(RIGHT),
                  functions[4].animate.shift(RIGHT + UP*.2),
                  graph_1.animate.shift(RIGHT),
                  points[5].animate.shift(RIGHT))
        self.wait()

        conclusions = VGroup(
             Tex("$1) y = 2x + 3$ ", passes_through_point, font_size=35).to_edge(LEFT + UP).shift(LEFT*.4),
             Tex("$2) y = 2x + 3$ ", is_parallel_to_line, font_size=35).to_edge(LEFT + UP).shift(LEFT*.4 + DOWN*.8),
             Tex("$y = 3x-5  ?$", font_size=FONT_SIZE).to_edge(LEFT).shift(UP*1.5),
             Tex("$y = 2x + 3 $",  is_parallel_to_line_and_passes_through_point,
                 font_size=35).to_edge(LEFT + UP).shift(LEFT*.4)
        )

        self.play(Write(conclusions[0]))
        self.wait()

        curved_arrow = CurvedArrow(conclusions[0][1][11].get_bottom(), points[-3][1].get_left(), tip_length=.15,
                                   angle=.6)

        self.play(Write(curved_arrow))
        self.wait()

        self.play(FadeOut(curved_arrow))
        self.wait()

        self.play(Write(conclusions[1]))
        self.wait()

        graph_1_copy = coordinate_system.plot(lambda x: 2*x, [-3, 3])

        self.play(graph_1_copy.animate.shift(UP*1.85))
        self.wait()

        self.play(FadeOut(VGroup(graph_1,
                                 graph_1_copy,
                                 points[5],
                                 functions[4])))
        self.wait()

        self.play(Transform(conclusions[:2], conclusions[-1]))
        self.wait()

        self.play(Write(conclusions[2]))
        self.wait()

        helper_numbers = VGroup(
             Tex(" $-$" + " $5$ ", font_size=35).to_edge(LEFT + UP).move_to(conclusions[3][0][4:]),
             Tex("$3x$", font_size=35).to_edge(LEFT + UP).move_to(conclusions[3][0][2:4]),
        )

        self.play(AnimationGroup(
            Transform(conclusions[:2][0][4:], helper_numbers[0]),
            Transform(conclusions[:2][0][2:4], helper_numbers[1])
        ))
        self.wait()

        final_points = VGroup(
            VGroup(Dot(point=coordinate_system.c2p(0, 0, 0)),
                   Tex("(0, 0)", font_size=35).next_to(coordinate_system.c2p(0, 0, 0)).shift(DOWN*.3 + LEFT*.1),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 0, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(0, 0, 0))
                   ),
            VGroup(Dot(point=coordinate_system.c2p(1, 3, 0)),
                   Tex("(1, 3)", font_size=35).next_to(coordinate_system.c2p(1, 3, 0)),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 3, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(1, 3, 0))
                   ),
            VGroup(Dot(point=coordinate_system.c2p(0, -5, 0)),
                   Tex("(0, -5)", font_size=35).next_to(coordinate_system.c2p(0, -5, 1)),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(0, -5, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(0, -5, 0))
                   )
        )

        graph_4 = coordinate_system.plot(lambda x: 3*x, [-3, 3])
        graph_5 = coordinate_system.plot(lambda x: 3*x - 5, [-3, 3])

        self.play(Write(VGroup(final_points[:-1],
                               graph_4,
                               functions[5])))
        self.wait()

        self.play(Write(final_points[2]),
                  conclusions[:2].animate.scale(1.1).shift(RIGHT*.5))
        self.wait()

        surrounding_answer_box = SurroundingRectangle(conclusions[:2], color=YELLOW)

        self.play(Write(surrounding_answer_box))
        self.wait()

        self.play(
            Transform(graph_4, graph_5),
            FadeOut(functions[5])
        )
        self.wait()

        self.play(conclusions[2][0][2:6].animate.scale(1.1))
        self.wait()
