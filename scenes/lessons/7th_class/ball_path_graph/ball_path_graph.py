from manim import Write, VGroup, Arrow
from manim import Dot, Line
from manim import MathTex, Tex, ChangeSpeed, AnimationGroup, Axes, Transform, FadeIn
from manim import Scene, RIGHT, LEFT, UP, DOWN, YELLOW, BLUE
from .text import *
from objects import SimpleSVGMobject

FONT_SIZE = 70

class BallPathGraph(Scene):
    def construct(self):
        self.wait(0.25)

        horizontal_line = Line([-3, -2, 0], [3, -2, 0], stroke_width=2)
        self.play(Write(horizontal_line))
        self.wait()

        # FadeIn the ball
        ball = SimpleSVGMobject('tennis_ball', scale=0.75).shift(DOWN * 1.2)
        ball.scale(0.8)
        self.play(FadeIn(ball))
        self.wait()

        arrow_to_up = Arrow([-1, -2, 0], [-1, 0, 0], tip_length=0.15, stroke_width=4)

        speed = VGroup(
            MathTex("v=14.2", font_size=FONT_SIZE).shift(DOWN*1.5 + LEFT*2.5).scale(0.6),
            Tex(meters_second, font_size=FONT_SIZE).shift(DOWN*1.55 + LEFT*1.4).scale(0.6)
        )

        self.play(Write(arrow_to_up))
        self.wait()

        self.play(Write(speed))
        self.wait(2)

        # move the ball upwards
        a = 0.989
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    ball.animate(run_time=1.5).shift(UP * 3.5),
                ),
                speedinfo={0: 1.405, 0.25: 1.3569, 0.5: 1.28165, 0.75: 1.18555,
                           1: 1.0745, 1.25: 0.9549, 1.5: 0.83265},
            ),
        )

        # move the ball downwards
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    ball.animate(run_time=1.5).shift(DOWN * 3.5),
                ),
                speedinfo={1.5: 0.83265, 1.75: 0.9549, 2: 1.0745, 2.25: 1.18555,
                           2.5: 1.28165, 2.75: 1.3569, 3: 1.405},
            )
        )
        # shift the axis to left
        self.play(AnimationGroup(ball.animate.shift(LEFT*4.2 + DOWN*0.3).scale(0.8),
                                 arrow_to_up.animate.shift(LEFT*4 + DOWN*0.4).scale(0.8),
                                 speed[0].animate.shift(LEFT*3.87 + DOWN*0.3).scale(0.8),
                                 speed[1].animate.shift(LEFT*4 + DOWN*0.28).scale(0.8),
                                 horizontal_line.animate.shift(LEFT * 5).scale(0.8)))

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
            },
            tips=False,
        ).shift(RIGHT*2 + UP*0.85)

        self.play(Write(coordinate_axis))
        self.wait(2)

        # display points
        point1 = VGroup(Dot(point=coordinate_axis.c2p(0, 1.5, 0), color=YELLOW),
                        Tex("(0, 1.5)").scale(0.5).next_to(coordinate_axis.c2p(0, 1.5, 0)))
        point2 = VGroup(coordinate_axis.get_horizontal_line(coordinate_axis.c2p(0.4, 6.5, 0), color=BLUE),
                        coordinate_axis.get_vertical_line(coordinate_axis.c2p(0.4, 6.5, 0), color=BLUE),
                        Dot(point=coordinate_axis.c2p(0.4, 6.45, 0), color=YELLOW),
                        Tex("$t$ = (0.4, 6.45)").scale(0.5).next_to(coordinate_axis.c2p(0.4, 6.45, 0)))

        self.play(Write(point1))
        self.wait()

        #display clock
        clock = VGroup(
            SimpleSVGMobject('stopwatch/stopwatch').shift(UP *2.8 + RIGHT * 4.2),
            SimpleSVGMobject('stopwatch/stopwatch_arow').shift(UP *2.8 + RIGHT * 4.2)
        )

        clock_nums = VGroup(
            MathTex(r"\frac{4}{10}", font_size=45).next_to(clock[0]),
            MathTex(r"\frac{145}{100}", font_size=45).next_to(clock[0]),
            MathTex("3", font_size=45).next_to(clock[0])
        )

        time_t = Tex(time, font_size=45).next_to(clock_nums[1])

        self.play(Write(clock))
        self.wait()

        self.play(AnimationGroup(ball.animate.shift(UP),
                                 clock[1].animate.rotate(-.04)),
                  Write(VGroup(point2,
                               clock_nums[0],
                               time_t)))
        self.wait(2)

        #display graphs
        graph_1 = coordinate_axis.plot(lambda t: a*(1.5 + 14.5*t - 5*t**2),
                                       x_range=[0, 1.45],
                                       color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(UP*4),
                                 Write(graph_1),
                                 clock[1].animate.rotate(-.105)),
                  Transform(clock_nums[0], clock_nums[1]))
        self.wait()

        graph_2 = coordinate_axis.plot(lambda t: a*(1.5 + 14.5*t - 5*t**2),
                                       x_range=[1.45, 3],
                                       color=BLUE)

        self.play(AnimationGroup(ball.animate.shift(DOWN*5),
                                 Write(graph_2),
                                 clock[1].animate.rotate(-.155),
                                 time_t.animate.shift(LEFT*.5)),
                  Transform(clock_nums[0], clock_nums[2]))
        self.wait(2)