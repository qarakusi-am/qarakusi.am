from manim import Write, VGroup, Arrow, FadeOut, DashedLine, Wiggle
from manim import Dot, Line
from manim import MathTex, Tex, ChangeSpeed, AnimationGroup, Axes, Transform, FadeIn, DoubleArrow
from manim import Scene, RIGHT, LEFT, UP, DOWN, YELLOW, BLUE, TransformFromCopy
from .text import *
from objects import SimpleSVGMobject, Stopwatch
from aramanim import Run

FONT_SIZE = 70


class BallPathGraph(Scene):
    def construct(self):
        self.wait(0.25)
        stopwatch = Stopwatch()
        # stopwatch.shift(UP * 2.8 + RIGHT * 4.2)
        print(stopwatch)
        self.play(
            Run(stopwatch, speed=60, run_time=3),
            run_time=3,
        )
        horizontal_line = Line([-3, -2, 0], [3, -2, 0], stroke_width=2).shift(LEFT * 5 + DOWN * .5).scale(.8)

        # FadeIn the ball
        ball = SimpleSVGMobject('tennis_ball', scale=0.75).shift(DOWN * 1.2)
        ball.scale(0.8)
        self.play(FadeIn(ball))
        self.wait(2)

        arrow_to_up = Arrow([-1, -2, 0], [-1, 0, 0], tip_length=0.15, stroke_width=4)

        speed = VGroup(
            MathTex("v=14.2", font_size=FONT_SIZE).shift(DOWN * 1.5 + LEFT * 2.5).scale(0.6),
            Tex(meters_second, font_size=FONT_SIZE).shift(DOWN * 1.55 + LEFT * 1.4).scale(0.6)
        )

        self.play(Write(arrow_to_up))
        self.wait()

        self.play(Write(speed))
        self.wait(2)

        # move the ball upwards
        a = 0.989
        self.play(
            ChangeSpeed(
                AnimationGroup(ball.animate(run_time=1.5).shift(UP * 3.5)),
                speedinfo={0: 1.405, 0.25: 1.3569, 0.5: 1.28165, 0.75: 1.18555,
                           1: 1.0745, 1.25: 0.9549, 1.5: 0.83265},
            )
        )

        # move the ball downwards
        self.play(
            ChangeSpeed(
                AnimationGroup(ball.animate(run_time=1.5).shift(DOWN * 3.5)),
                speedinfo={1.5: 0.83265, 1.75: 0.9549, 2: 1.0745, 2.25: 1.18555,
                           2.5: 1.28165, 2.75: 1.3569, 3: 1.405},
            )
        )

        slanted_lines = VGroup()

        i = 3
        while i <= 7.5:
            slanted_lines.add(Line(UP + RIGHT, DOWN + LEFT).scale(.2).shift(DOWN * 2.71 + LEFT * i))
            i = i + .5

        # shift the axis to the left
        self.play(AnimationGroup(ball.animate.shift(LEFT * 4.2 + DOWN * .05).scale(0.15),
                                 arrow_to_up.animate.shift(LEFT * 3.7 + UP * .3).scale(0.8),
                                 speed[0].animate.shift(LEFT * 3.57 + UP * .3).scale(0.8),
                                 speed[1].animate.shift(LEFT * 3.7 + UP * .3).scale(0.8),
                                 Write(VGroup(horizontal_line, slanted_lines))))
        self.wait(2)

        double_arrow = DoubleArrow(UP, DOWN, tip_length=0.15, stroke_width=4,
                                   color=BLUE).next_to(ball).shift(DOWN * .65).scale(.8)
        ball_distance = Tex(ball_line_distance, font_size=35, color=BLUE).next_to(double_arrow)

        self.play(Write(VGroup(double_arrow, ball_distance)))
        self.wait(2)

        # create coordinate axis
        coordinate_axis = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 12, 1],
            x_length=6.4,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        ).shift(RIGHT * 2 + UP * 0.85)

        self.play(Write(coordinate_axis, run_time=2))
        self.wait(2)

        # display points
        points = VGroup(
            VGroup(Dot(point=coordinate_axis.c2p(0, 1.5, 0), color=YELLOW),
                   Tex("(0, 1.5)").scale(0.5).next_to(coordinate_axis.c2p(0, 1.5, 0))),
            VGroup(coordinate_axis.get_horizontal_line(coordinate_axis.c2p(0.4, 6.5, 0), color=BLUE),
                   coordinate_axis.get_vertical_line(coordinate_axis.c2p(0.4, 6.5, 0), color=BLUE),
                   Dot(point=coordinate_axis.c2p(0.4, 6.45, 0), color=YELLOW),
                   Tex("$t$ = (0.4, 6.45)").scale(0.5).next_to(coordinate_axis.c2p(0.4, 6.45, 0))),
            VGroup(Dot(point=coordinate_axis.c2p(0.4, 0, 0), color=YELLOW),
                   Tex("(0.4, 0)").scale(.5).next_to(coordinate_axis.c2p(0.4, 0, 0)).shift(DOWN * .4 + LEFT * .5)),
            VGroup(Dot(point=coordinate_axis.c2p(0.8, 9.791, 0), color=YELLOW),
                   Tex("(0.8, 9.791)").scale(.5).next_to(coordinate_axis.c2p(0.8, 9.791, 0))),
            VGroup(Dot(point=coordinate_axis.c2p(1, 10.879, 0), color=YELLOW),
                   Tex("(1, 10.879)").scale(.5).next_to(coordinate_axis.c2p(1, 10.879, 0))),
            VGroup(Dot(point=coordinate_axis.c2p(1.45, 11.88, 0), color=YELLOW),
                   Tex("(1.45, 11.88)").scale(.5).next_to(coordinate_axis.c2p(1.45, 11.88, 0))),
            VGroup(Dot(point=coordinate_axis.c2p(2.5, 6.428, 0), color=YELLOW),
                   Tex("(2.5, 6.428)").scale(.5).next_to(coordinate_axis.c2p(2.5, 6.428, 0))))

        vertical_line = DashedLine(points[2][0], points[1][2])

        self.play(Write(points[0]))
        self.wait(2)

        # display the clock
        clock = VGroup(
            SimpleSVGMobject('stopwatch/stopwatch').shift(UP * 2.8 + RIGHT * 4.2),
        )
        clock.add(SimpleSVGMobject('stopwatch/stopwatch_arow').scale(0.5).move_to(clock[0]))

        clock_nums = VGroup(
            Tex("0.4", sec, font_size=45).next_to(clock[0]),
            Tex("0.8", sec, font_size=45).next_to(clock[0]),
            Tex("$1$", sec, font_size=45).next_to(clock[0]),
            Tex("1.45", sec, font_size=45).next_to(clock[0]),
            Tex("2.5", sec, font_size=45).next_to(clock[0]),
            Tex("$3$", sec, font_size=45).next_to(clock[0])
        )

        self.play(AnimationGroup(FadeIn(clock, run_time=2), FadeOut(VGroup(ball_distance, double_arrow))))
        self.wait(2)

        self.play(AnimationGroup(ball.animate.shift(UP * 2.3),
                                 clock[1].animate.rotate(-.04),
                                 Write(VGroup(clock_nums[0])),
                                 run_time=2))
        self.wait(2)

        def graphs(t):
            graph = a * (1.5 + 14.5 * t - 5 * t ** 2)
            return graph

        # display the graphs
        graph1 = coordinate_axis.plot(lambda t: graphs(t), x_range=[0, .4], color=BLUE)

        self.play(AnimationGroup(Write(points[2][0]),
                                 TransformFromCopy(ball, points[1][2]),
                                 TransformFromCopy(clock_nums[0], points[2][1]),
                                 Write(VGroup(vertical_line, points[1][-1:2])), run_time=2))
        self.wait()

        self.play(Write(graph1))
        self.wait(2)

        graph2 = coordinate_axis.plot(lambda t: graphs(t), x_range=[.4, .8], color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(UP * 1.55),
                                 clock[1].animate.rotate(-.04),
                                 Transform(clock_nums[0], clock_nums[1])))
        self.wait(2)

        self.play(AnimationGroup(TransformFromCopy(ball, points[3][0]), Write(VGroup(points[3][1])), run_time=2))
        self.wait()

        self.play(Write(graph2))
        self.wait(2)

        graph3 = coordinate_axis.plot(lambda t: graphs(t), x_range=[.8, 1], color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(UP * .5),
                                 clock[1].animate.rotate(-.02),
                                 Transform(clock_nums[0], clock_nums[2])))
        self.wait(2)

        self.play(AnimationGroup(TransformFromCopy(ball, points[4][0]), Write(VGroup(points[4][1]))), run_time=2)
        self.wait()

        self.play(Write(graph3))
        self.wait(2)

        graph4 = coordinate_axis.plot(lambda t: graphs(t), x_range=[1, 1.45], color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(UP * .5),
                                 clock[1].animate.rotate(-.045),
                                 Transform(clock_nums[0], clock_nums[3])))
        self.wait(2)

        self.play(AnimationGroup(TransformFromCopy(ball, points[5][0]), Write(VGroup(points[5][1])), run_time=2))
        self.wait()

        self.play(Write(graph4))
        self.wait(2)

        graph5 = coordinate_axis.plot(lambda t: graphs(t), x_range=[1.45, 2.5], color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(DOWN * 2.5),
                                 clock[1].animate.rotate(-.15),
                                 Transform(clock_nums[0], clock_nums[4])))
        self.wait(2)

        self.play(AnimationGroup(TransformFromCopy(ball, points[6][0]), Write(VGroup(points[6][1])), run_time=2))
        self.wait()

        self.play(Write(graph5))
        self.wait(2)

        graph6 = coordinate_axis.plot(lambda t: graphs(t), x_range=[2.5, 3], color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(DOWN * 3),
                                 clock[1].animate.rotate(-.05),
                                 Transform(clock_nums[0], clock_nums[5]),
                                 Write(graph6, run_time=2)))
        self.wait(2)
