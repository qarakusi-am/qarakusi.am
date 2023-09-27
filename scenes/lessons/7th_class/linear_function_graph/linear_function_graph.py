from manim import Write, VGroup, AnimationGroup, ValueTracker, Transform, FadeIn
from manim import Dot, Arrow, FadeOut, DashedLine, CurvedArrow, rate_functions
from manim import MathTex, Tex, MathTable, Axes, TransformFromCopy, always_redraw, SurroundingRectangle
from manim import Scene, RIGHT, LEFT, UP, DOWN, YELLOW, RED, GREEN, ORANGE, BLACK
from .text import *


class LinearFunctionGraph(Scene):
    def construct(self):
        # font sizes
        font_sizes = {'lin_func': 60, 'functions': 55, 'graphs': 45, 'points': 35}

        lin_function = Tex(linear_function_str, font_size=font_sizes['lin_func']).shift(UP * 3.3)

        functions = VGroup(
            MathTex("y = kx + b", font_size=font_sizes['functions']).move_to(lin_function).shift(DOWN * .6),
            MathTex("k = 2", font_size=font_sizes['functions']).move_to(lin_function).shift(DOWN * 1.2 + LEFT * 6.1),
            MathTex("b = 3", font_size=font_sizes['functions']).move_to(lin_function).shift(DOWN * 1.8 + LEFT * 6.1),
            MathTex("y = 2x + 3", font_size=font_sizes['functions']).move_to(lin_function).shift(
                DOWN * .6 + LEFT * 5.6),
            MathTex("y = 2x", font_size=font_sizes['graphs']).shift(UP * 2.35 + RIGHT * 6),
            MathTex("y = 3x", font_size=font_sizes['graphs']).shift(UP * 3.6 + RIGHT * 4.5),
            MathTex("-", font_size=66).move_to(lin_function).shift(LEFT * 4.3 + DOWN * .57)
        )

        self.play(Write(lin_function))
        self.wait(0.5)

        self.play(Write(functions[0]))
        self.wait()

        # displaying coordinate system
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
        ).shift(RIGHT * 1.5)

        x_label = coordinate_system.get_x_axis_label("x")
        y_label = coordinate_system.get_y_axis_label("y", edge=RIGHT, direction=RIGHT, buff=0.4).shift(UP * 3.4)

        axis_labels = VGroup(x_label, y_label)

        self.play(AnimationGroup(
            lin_function.animate.shift(LEFT * 4.25 + UP * .1),
            functions[0].animate.shift(LEFT * 5.4)))
        self.wait()

        self.play(Write(coordinate_system),
                  Write(axis_labels))
        self.wait()

        # displaying random lines
        random_graphs = VGroup(
            coordinate_system.plot(lambda x: 2 * x, x_range=[-3, 3],color=RED),
            coordinate_system.plot(lambda x: 3 - 0.5 * x, x_range=[-3, 3],color=GREEN),
            coordinate_system.plot(lambda x: x + 1, x_range=[-3, 3], color=ORANGE)
        )

        self.play(Write(random_graphs))
        self.wait(2)

        self.play(FadeOut(random_graphs))
        self.wait()

        self.play(Write(functions[1:3]))
        self.wait()

        self.play(AnimationGroup(Transform(functions[0], functions[3], run_time=1.5),
                                 FadeOut(functions[1:3])))
        self.wait()

        graph1 = coordinate_system.plot(lambda x: 2 * x, x_range=[-3, 3])

        self.play(Write(VGroup(graph1,
                               functions[4])))
        self.wait()

        # displaying the table
        table = VGroup(MathTable(
            [["x", "1"],
             ["2x", "2"],
             ["2x+3", "5"]],
            include_outer_lines=True
        ).shift(LEFT * 5.3 + UP).scale(0.8),
                       MathTable(
                           [["2"],
                            ["4"],
                            ["7"]],
                           include_outer_lines=True
                       ).shift(LEFT * 3.05 + UP).scale(0.8),
                       MathTable(
                           [["0"],
                            ["0"],
                            ["3"]],
                           include_outer_lines=True
                       ).shift(LEFT * 1.85 + UP).scale(0.8),
                       MathTable(
                           [["-2"],
                            ["-4"],
                            ["-1"]],
                           include_outer_lines=True
                       ).shift(LEFT * .5 + UP).scale(0.8))

        table[0][0][5].color = BLACK
        table[0][0][2:4].color = ORANGE

        for i in range(1, 4, 1):
            table[i][0][1].color = ORANGE
            table[i][0][2].color = GREEN

        table[0][0][4].color = GREEN

        self.play(FadeOut(lin_function))
        self.wait()

        self.play(Write(table[0]))
        self.wait(2)

        points = VGroup(VGroup(
            Dot(point=coordinate_system.c2p(1, 2, 0), color=ORANGE),
            Tex("(1, 2)", font_size=font_sizes['points'], color=ORANGE).next_to(coordinate_system.c2p(1, 2, 0)),
            coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 2, 0), color=ORANGE),
            coordinate_system.get_vertical_line(coordinate_system.c2p(1, 2, 0), color=ORANGE)
        ),
            VGroup(
                Dot(point=coordinate_system.c2p(1, 5, 0), color=GREEN),
                Tex("(1, 5)", font_size=font_sizes['points'], color=GREEN).next_to(coordinate_system.c2p(1, 5, 0)),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 5, 0), color=GREEN),
                coordinate_system.get_vertical_line(coordinate_system.c2p(1, 5, 0), color=GREEN)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(2, 4, 0), color=ORANGE),
                Tex("(2, 4)", font_size=font_sizes['points'], color=ORANGE).next_to(coordinate_system.c2p(2, 4, 0)),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(2, 4, 0), color=ORANGE),
                coordinate_system.get_vertical_line(coordinate_system.c2p(2, 4, 0), color=ORANGE)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(2, 7, 0), color=GREEN),
                Tex("(2, 7)", font_size=font_sizes['points'], color=GREEN).next_to(coordinate_system.c2p(2, 7, 0)),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(2, 7, 0), color=GREEN),
                coordinate_system.get_vertical_line(coordinate_system.c2p(2, 7, 0), color=GREEN)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(0, 0, 0), color=ORANGE),
                Tex("(0, 0)", font_size=font_sizes['points'], color=ORANGE).next_to(coordinate_system.c2p(0, 0, 0)).shift(
                    DOWN * .4 + LEFT * .1),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 0, 0), color=ORANGE),
                coordinate_system.get_vertical_line(coordinate_system.c2p(0, 0, 0), color=ORANGE)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(0, 3, 0), color=GREEN),
                Tex("(0, 3)", font_size=font_sizes['points'], color=GREEN).next_to(coordinate_system.c2p(0, 3, 0)).shift(
                    LEFT * 1.45),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 3, 0), color=GREEN),
                coordinate_system.get_vertical_line(coordinate_system.c2p(0, 3, 0), color=GREEN)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(-2, -4, 0), color=ORANGE),
                Tex("(-2, -4)", font_size=font_sizes['points'], color=ORANGE).next_to(
                    coordinate_system.c2p(-2, -4, 0)).shift(LEFT * 1.5),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(-2, -4, 0), color=ORANGE),
                coordinate_system.get_vertical_line(coordinate_system.c2p(-2, -4, 0), color=ORANGE)
            ),
            VGroup(
                Dot(point=coordinate_system.c2p(-2, -1, 0), color=GREEN),
                Tex("(-2, -1)", font_size=font_sizes['points'], color=GREEN).next_to(
                    coordinate_system.c2p(-2, -1, 0)).shift(LEFT * 1.5),
                coordinate_system.get_horizontal_line(coordinate_system.c2p(-2, -1, 0), color=GREEN),
                coordinate_system.get_vertical_line(coordinate_system.c2p(-2, -1, 0), color=GREEN)
            )
        )

        # display the first point
        self.play(TransformFromCopy(VGroup(table[0][0][1], table[0][0][3]), points[0][0]))
        self.wait(0.5)

        self.play(Write(points[0][1:]))
        self.wait()

        table[0][0][5].color = GREEN
        self.play(Write(table[0][0][5]))
        self.wait()

        # display the second point
        self.play(TransformFromCopy(VGroup(table[0][0][1], table[0][0][5]), points[1][0]))
        self.wait(0.5)

        self.play(Write(points[1][1:]))
        self.wait()

        arrows = VGroup(
            VGroup(DashedLine(points[0][0], points[1][0], dashed_ratio=0.5),
                   Arrow(points[0][0], points[1][0], max_stroke_width_to_length_ratio=0).shift(UP * .25)),
            VGroup(DashedLine(points[2][0], points[3][0], dashed_ratio=0.5),
                   Arrow(points[2][0], points[3][0], max_stroke_width_to_length_ratio=0).shift((UP * 0.25))),
            VGroup(DashedLine(points[6][0], points[7][0], dashed_ratio=0.5),
                   Arrow(points[6][0], points[7][0], max_stroke_width_to_length_ratio=0).shift(UP * 0.25))
        )

        arrow_value = ValueTracker(3)
        arrow_counter = always_redraw(lambda: MathTex(str(round(arrow_value.get_value(), 2)),
                                                          font_size=font_sizes['points']).next_to(arrows[0]).shift(
            LEFT))

        self.play(Write(VGroup(arrows[0],
                               arrow_counter)),
                  FadeOut(points[0][2:]
                          ,
                          points[1][2:]))
        self.wait()

        self.play(Write(table[1]))
        self.wait()

        # display third point
        self.play(TransformFromCopy(VGroup(table[1][0][0], table[1][0][1]), points[2][0]))
        self.wait(0.5)

        self.play(Write(points[2][1:]))
        self.wait()

        # display fourth point
        self.play(AnimationGroup(TransformFromCopy(VGroup(table[1][0][0], table[1][0][2]), points[3][0]),
                                 Write(points[3][1:])))
        self.wait()

        self.play(AnimationGroup(Write(arrows[1]),FadeOut(points[2][2:], points[3][2:])))
        self.wait()

        self.play(Write(table[2]))
        self.wait()

        # display fifth and sixth points
        self.play(AnimationGroup(TransformFromCopy(VGroup(table[2][0][0], table[2][0][1]), points[4][0]),
                                 TransformFromCopy(VGroup(table[2][0][0], table[2][0][2]), points[5][0])))

        self.wait(0.5)
        self.play(Write(VGroup(points[4][1:], points[5][1:])))
        self.wait()

        self.play(Write(table[3]))
        self.wait()

        # display seventh point
        self.play(AnimationGroup(TransformFromCopy(VGroup(table[3][0][0], table[3][0][1]), points[6][0]),
                                 TransformFromCopy(VGroup(table[3][0][0], table[3][0][2]), points[7][0])))
        self.wait()

        self.play(Write(VGroup(points[6][1:], points[7][1:])))
        self.wait()

        self.play(AnimationGroup(Write(arrows[2]),FadeOut(points[6][2:] , points[7][2:])))

        # display points for the line 2x + 3
        points_for_lines = VGroup()
        x = -3
        while x <= 3:
            points_for_lines.add(Dot(point=coordinate_system.c2p(x, 2 * x, 0), color=ORANGE))
            x = x + 0.5

        points_for_lines_copy = points_for_lines.copy()

        self.play(Write(points_for_lines, run_time=2))
        self.wait()

        self.play(FadeOut(table))
        self.wait()

        self.play(points_for_lines_copy.animate.shift(UP * 1.9).set_color(GREEN))
        self.wait()

        graph2 = coordinate_system.plot(lambda x: 2 * x + 3, [-4, 2.5])
        self.play(Write(graph2))
        self.wait()

        self.play(functions[0].animate.shift(RIGHT * .5).scale(1.2))
        self.wait()

        value_for_3 = ValueTracker(3)
        counter_for_equation = always_redraw(lambda: MathTex(str(round(value_for_3.get_value(), 2)),
                                                             font_size=66).next_to(functions[0][0][-2]).shift(UP * .05 +
                                                                                                              LEFT * .025))
        #convert 3 to 3.0 to use value tracker
        self.play(AnimationGroup(FadeIn(counter_for_equation,run_time=10 ** -20),
                                 FadeOut(functions[0][0][-1],run_time=10 ** -20)))

        self.play(AnimationGroup(
            value_for_3.animate.set_value(2.50),
            arrow_value.animate.set_value(2.50),
            arrows.animate.shift(DOWN * .17),
            graph2.animate.shift(DOWN * .34),
            points_for_lines_copy.animate.shift(DOWN * .34),
            FadeOut(VGroup(points[1][:2],
                           points[3][:2],
                           points[5][:2],
                           points[7][:2])),
            rate_func=rate_functions.rush_from,
            run_time=4
        ))
        self.wait(3)

        self.play(AnimationGroup(value_for_3.animate.set_value(0),
                                 arrow_value.animate.set_value(0),
                                 points_for_lines_copy.animate.shift(DOWN * 1.56),
                                 FadeOut(arrows),
                                 rate_func=rate_functions.rush_from,
                                 run_time=4))
        self.wait(3)

        self.play(FadeOut(arrow_counter))
        self.wait()

        arrow_value = ValueTracker(0)
        arrow_counter = always_redraw(lambda: MathTex(str(round(arrow_value.get_value(), 2)),
                                                          font_size=font_sizes['points']).move_to(points[2]).shift(
            DOWN * .71 +LEFT * .8))

        graph3 = coordinate_system.plot(lambda x: 2 * x - 2, [-4, 2.5])

        arrows_down = VGroup(VGroup(DashedLine(points[0][0], coordinate_system.c2p(1, .15, 0), dashed_ratio=.5),
                                    Arrow(points[0][0], coordinate_system.c2p(1, 0, 0),
                                          max_stroke_width_to_length_ratio=0).shift(DOWN * .2)),
                             VGroup(DashedLine(points[2][0], coordinate_system.c2p(2, 2.15, 0), dashed_ratio=.5),
                                    Arrow(points[2][0], coordinate_system.c2p(2, 2, 0),
                                          max_stroke_width_to_length_ratio=0).shift(DOWN * .2)))

        self.play(Write(VGroup(graph3,
                               arrow_counter)))

        self.play(AnimationGroup(value_for_3.animate.set_value(2),
                                 arrow_value.animate.set_value(2),
                                 points_for_lines_copy.animate.shift(DOWN * 1.23),
                                 Write(arrows_down),
                                 rate_func=rate_functions.rush_from,
                                 run_time=5),
                  Transform(functions[0][0][-2], functions[-1]))
        self.wait(3)

        self.play(FadeOut(graph2,
                          graph3,
                          arrows_down,
                          points[0][:2],
                          points[2][:2],
                          points[4][:2],
                          points[6][:2],
                          points_for_lines,
                          points_for_lines_copy,
                          arrow_counter,
                          counter_for_equation,
                          functions[0][0][:-1],
                          functions[-1]
                          ))
        self.wait(2)

        self.play(Write(points[5]))
        self.wait()

        self.play(AnimationGroup(
            coordinate_system.animate.shift(RIGHT),
            x_label.animate.shift(RIGHT * .7),
            y_label.animate.shift(RIGHT),
            functions[4].animate.shift(RIGHT * .4 + DOWN),
            graph1.animate.shift(RIGHT),
            points[5].animate.shift(RIGHT)))
        self.wait()

        conclusions = VGroup(
            Tex("$1) y = 2x + 3$ ", passes_through_point, font_size=font_sizes['functions']).to_edge(LEFT + UP).shift(
                LEFT * .4),
            Tex("$2) y = 2x + 3$ ", is_parallel_to_line, font_size=font_sizes['functions']).to_edge(LEFT + UP).shift(
                LEFT * .4 + DOWN * 1.5),
            Tex("$y = 3x-5  ?$", font_size=font_sizes['functions']).to_edge(LEFT).shift(UP * .3 + LEFT * .4),
            Tex("$y = 2x + 3 $", is_parallel_to_line_and_passes_through_point,
                font_size=font_sizes['functions']).to_edge(LEFT + UP).shift(LEFT * .4)
        )

        self.play(Write(conclusions[0]))
        self.wait(2)

        # displaying the curved arrow
        curved_arrow = CurvedArrow(conclusions[0][1][11].get_bottom(), points[-3][1].get_left(), tip_length=.1,
                                   angle=.9).shift(DOWN * .1)

        self.play(Write(curved_arrow))
        self.wait()

        self.play(FadeOut(curved_arrow))
        self.wait(2)

        self.play(Write(conclusions[1]))
        self.wait(2)

        graph1_copy = coordinate_system.plot(lambda x: 2 * x, [-3, 3])

        self.play(graph1_copy.animate.shift(UP * 1.85))
        self.wait()

        self.play(FadeOut(graph1,
                          graph1_copy,
                          points[5],
                          functions[4]))
        self.wait()

        self.play(Transform(conclusions[:2], conclusions[-1], run_time=2))
        self.wait(3)

        self.play(Write(conclusions[2]))
        self.wait(2)

        # creating helper numbers for transforming
        helper_numbers = VGroup(
            Tex(
                " $-$" + " $5$ ", font_size=font_sizes['functions']).to_edge(LEFT + UP).move_to(conclusions[3][0][4:]),
            Tex("$3x$", font_size=font_sizes['functions']).to_edge(LEFT + UP).move_to(conclusions[3][0][2:4]),
        )

        self.play(AnimationGroup(
            Transform(conclusions[:2][0][4:]
                      , helper_numbers[0]),
            Transform(conclusions[:2][0][2:4], helper_numbers[1]),
            run_time=2
        ))
        self.wait(3)

        # creating final points for displaying
        final_points = VGroup(
            VGroup(Dot(point=coordinate_system.c2p(0, 0, 0)),
                   Tex("(0, 0)", font_size=font_sizes['points']).next_to(coordinate_system.c2p(0, 0, 0)).shift(DOWN * .3 +
                                                                                                             LEFT * .1),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(0, 0, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(0, 0, 0))
                   ),
            VGroup(Dot(point=coordinate_system.c2p(1, 3, 0)),
                   Tex("(1, 3)", font_size=font_sizes['points']).next_to(coordinate_system.c2p(1, 3, 0)),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(1, 3, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(1, 3, 0))
                   ),
            VGroup(Dot(point=coordinate_system.c2p(0, -5, 0)),
                   Tex("(0, -5)", font_size=font_sizes['points']).next_to(coordinate_system.c2p(0, -5, 1)),
                   coordinate_system.get_horizontal_line(coordinate_system.c2p(0, -5, 0)),
                   coordinate_system.get_vertical_line(coordinate_system.c2p(0, -5, 0))
                   )
        )

        graph4 = coordinate_system.plot(lambda x: 3 * x, [-3, 3])

        self.play(Write(final_points[:-1]))
        self.wait(2)

        self.play(Write(VGroup(graph4,
                               functions[5]),
                        run_time=2))
        self.wait(2)

        self.play(AnimationGroup(Write(final_points[2]),
                                 conclusions[:2].animate.scale(1.2).shift(RIGHT * .8),
                                 run_time=2))
        self.wait(2)

        # creating surrounding answer box
        surrounding_answer_box = SurroundingRectangle(conclusions[:2], color=YELLOW)

        self.play(Write(surrounding_answer_box))
        self.wait(2)

        self.play(
            AnimationGroup(graph4.animate.shift(DOWN * 3.15),
                           FadeOut(functions[5]))
        )
        self.wait(2)

        self.play(AnimationGroup(
            conclusions[2][0][2:6].animate.scale(1.2),
            conclusions[2][0][6].animate.shift(RIGHT * .3)))
        self.wait(2)
