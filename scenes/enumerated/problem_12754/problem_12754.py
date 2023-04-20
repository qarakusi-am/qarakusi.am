from manim import SurroundingRectangle, Axes, Dot, CurvedArrow, FadeOut
from manim import Write, AnimationGroup
from manim import TransformFromCopy
from manim import YELLOW, BLUE, WHITE, ORANGE, GREEN
from manim import RIGHT, LEFT, UP, DOWN
from manim import MathTex, VGroup, Scene

FONT_SIZE = 55
RUN_TIME_SPEED = 2


class Problem12754(Scene):
    def construct(self):

        coordinate_axes = Axes(
            x_range=[-4, 6, 1],
            y_range=[-3.3, 10, 1],
            x_length=9,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 40,
            },
            tips=True,
        ).shift(DOWN * 0.6)
        # graphs and respective formulas
        graph1 = coordinate_axes.plot(lambda t: 2 * t + 4,
                                      x_range = [-3, 5],
                                      color = ORANGE)
        formula1 = MathTex("y=2x+4", font_size = FONT_SIZE, color = ORANGE).move_to(graph1).shift(RIGHT * 0.5 + UP * 2.1)

        graph2 = coordinate_axes.plot(lambda t: 4.5 * t - 7,
                                      x_range=[-2, 5],
                                      color = GREEN)
        formula2 = MathTex("y=4.5x-7", font_size = FONT_SIZE, color = GREEN).move_to(graph2).shift(RIGHT * 2.3 + UP)

        # intersection points
        graphs_intersection_point = Dot(point = coordinate_axes.c2p(4.4, 12.8, 0), color = WHITE)
        graphs_intersection_point_label = MathTex("(4.4,12.8)").scale(0.7).next_to(coordinate_axes.c2p(4.4, 12.8, 0))

        point_x1 = Dot(point = coordinate_axes.c2p(1, 0, 0), color = WHITE)

        line_intersection_point1 = VGroup(
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(1, 15, 0), color = BLUE),
            Dot(point = coordinate_axes.c2p(1, 6, 0), color = YELLOW),
            MathTex("(x,", "2x + 4", ")").scale(0.7).next_to(coordinate_axes.c2p(0.9, 6, 0)))
        line_intersection_point2 = VGroup(
            coordinate_axes.get_vertical_line(coordinate_axes.c2p(1, -5, 0), color = BLUE),
            Dot(point = coordinate_axes.c2p(1, -2.5, 0), color = YELLOW),
            MathTex("(x,", "4.5x - 7", ")").scale(0.7).next_to(coordinate_axes.c2p(1, -2.5, 0)))

        # create coordinate axis
        self.play(Write(coordinate_axes))
        self.wait(2)

        # display graphs
        self.play(Write(graph1))
        self.play(Write(formula1))
        self.wait()

        self.play(Write(graph2))
        self.play(Write(formula2))
        self.wait()

        # display intersection points
        self.play(Write(point_x1))
        self.wait()

        self.play(Write(graphs_intersection_point))
        self.wait()

        self.play(Write(line_intersection_point1[0:2], run_time = RUN_TIME_SPEED))
        self.play(Write(line_intersection_point1[-1]))
        self.wait()

        self.play(Write(VGroup(line_intersection_point2[0:2]), run_time = RUN_TIME_SPEED))
        self.play(Write(line_intersection_point2[-1]))
        self.wait()

        self.play(FadeOut(formula1, formula2))
        self.wait()

        self.play(AnimationGroup(
            VGroup(line_intersection_point1[0], line_intersection_point2[0],point_x1).animate(run_time = 2.5).shift(RIGHT * 3.074),
            line_intersection_point1[1].animate(run_time = 2.5).move_to(graphs_intersection_point),
            line_intersection_point2[1].animate(run_time = 2.5).move_to(graphs_intersection_point),
            line_intersection_point1[2].animate(run_time = 2.5).move_to(graphs_intersection_point).shift(LEFT),
            line_intersection_point2[2].animate(run_time = 2.5).move_to(graphs_intersection_point).shift(
                RIGHT * 1.2 + UP * 0.02),
            ))
        self.wait(2)

        surrounding_rectangles = VGroup(SurroundingRectangle(line_intersection_point1[2][1], color = YELLOW, buff=0.1),
                                        SurroundingRectangle(line_intersection_point2[2][1], color = YELLOW, buff=0.1))

        self.play(Write(surrounding_rectangles, run_time = RUN_TIME_SPEED))
        self.wait(2)

        # find intersection point
        equations = VGroup(MathTex("2x+4=4.5x-7", font_size = FONT_SIZE).shift(UP * 3 + LEFT * 4),
                           MathTex("2x-4.5x=-7-4", font_size = FONT_SIZE).shift(UP * 2.2 + LEFT * 4.52),
                           MathTex("-2.5x=-11", font_size = FONT_SIZE).shift(UP * 1.4 + LEFT * 4.46),
                           MathTex(r"x=\frac{-11}{-2.5}=4.4", font_size = FONT_SIZE).shift(UP * 0.4 + LEFT * 5.03),
                           MathTex("2x+4=2\cdot 4.4+4=12.8", font_size = FONT_SIZE).shift(DOWN * 0.6 + LEFT * 2.95)
                           )
        curved_arrows = VGroup(
            CurvedArrow(equations[0][0][3].get_bottom(), equations[0][0][9].get_bottom(), tip_length=0.15,
                        angle=.6).shift(DOWN * 0.1),
            CurvedArrow(equations[0][0][5].get_top(), equations[0][0][2].get_top(), tip_length=0.15,
                        angle=.6).shift(UP * 0.1)
        )
        self.wait()
        self.play(AnimationGroup(
            TransformFromCopy(line_intersection_point1[2][1], equations[0][0][0:4]),
            TransformFromCopy(line_intersection_point2[2][1], equations[0][0][5:]), run_time = RUN_TIME_SPEED))
        self.play(Write(equations[0][0][4]))
        self.wait()
        self.play(FadeOut(surrounding_rectangles))
        self.wait()

        self.play(VGroup(coordinate_axes, graph1, graph2, graphs_intersection_point, point_x1,
                         line_intersection_point1, line_intersection_point2).animate.shift(RIGHT * 1.85))
        self.wait(2)

        self.play(Write(curved_arrows[0]))
        self.wait(0.5)
        self.play(Write(curved_arrows[1]))
        self.wait()

        self.play(Write(equations[1], run_time = RUN_TIME_SPEED))
        self.wait()

        self.play(Write(equations[2], run_time = RUN_TIME_SPEED))
        self.wait()

        self.play(Write(equations[3], run_time = RUN_TIME_SPEED))
        self.wait()

        self.play(Write(equations[4], run_time = 2.5))
        self.wait()

        self.play(AnimationGroup(
            TransformFromCopy(VGroup(equations[3][0][-3:], equations[4][0][-4:]), graphs_intersection_point_label),
            VGroup(line_intersection_point1[-1], line_intersection_point2[-1]).animate.set_opacity(0)))
        self.wait(2)
