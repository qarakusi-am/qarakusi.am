from manim import Scene, VGroup, Dot, Line, Tex, Graph, Create, FadeIn, AnimationGroup, ReplacementTransform, Square, Write, FadeOut, ValueTracker, MathTex, Integer, Circumscribe, rate_functions
from objects import Car, SimpleSVGMobject
from manim import ORANGE, GREEN, DOWN, RIGHT, UP, ORIGIN, LEFT, BLUE, RED, PURPLE
from random import uniform
import numpy as np
import networkx as nx

nxgraph = nx.erdos_renyi_graph(6, 1)

class TwoNVideo(Scene):
    def construct(self):
        self.wait()

        dots = Graph.from_networkx(
            nxgraph,
            layout={
                0: [-4, 0, 0],
                1: [0, 3, 0],
                2: [-1.5, .5, 0],
                3: [3.5, 0, 0],
                4: [-.4, -3.3, 0],
                5: [2.5, -2.3, 0],
            },
            layout_scale=3.4,
            vertex_config={
                "fill_color": ORANGE,
                "radius": .2
            }
        ).scale(.85).shift(RIGHT*.2)

        square = Square(7.7, color=PURPLE)
        self.play(Create(square))

        house_svg = SimpleSVGMobject('house').scale(.4)
        houses = VGroup(
            *[
                house_svg.copy().move_to(dots.vertices[i].get_center())
                for i in range(len(dots.vertices))
            ]
        )
        self.play(FadeIn(houses))
        self.wait()

        village = VGroup(square, houses)
        self.play(village.animate.scale(.7).to_edge(UP))
        self.wait()

        question = Tex("Հնարավո՞ր է արդյոք բաժանել 2 հավասար խմբերի։", font_size=60)
        question.to_edge(DOWN)
        self.play(Write(question))
        self.wait()

        self.play(FadeOut(question))
        self.play(
            village.animate.scale(1.3).move_to(ORIGIN)
        )

        self.play(
            AnimationGroup(
                *[ReplacementTransform(houses[i], dots.vertices[i]) for i in range(len(dots.vertices))],
                lag_ratio=.3
            )
        )
        temp = [dots.vertices[i].copy() for i in range(len(dots.vertices))]
        self.add(*temp)
        self.play(Create(dots, run_time=4))
        self.remove(*temp)

        number1 = Integer(0, color=GREEN, font_size=120).next_to(square, LEFT, buff=1.5)
        number2 = Integer(6, color=ORANGE, font_size=120).next_to(square, RIGHT, buff=1.5)

        self.play(
            Write(number1),
            Write(number2)
        )
        self.wait()

        paralel_line = Line(
            dots.vertices[1].get_center(),
            dots.vertices[4].get_center()
        ).set_length(15).set_color(RED)
        paralel_line.save_state()
        paralel_line.shift(LEFT*4)

        self.play(Create(paralel_line))
        self.wait()

        self.play(
            paralel_line.animate.next_to(dots.vertices[0]),
            number1.animate.set_value(1),
            number2.animate.set_value(5),
            dots.vertices[0].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            paralel_line.animate.next_to(dots.vertices[2], buff=0).shift(LEFT*.35),
            number1.animate.set_value(2),
            number2.animate.set_value(4),
            dots.vertices[2].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            paralel_line.animate.restore(),
            number1.animate.set_value(4),
            number2.animate.set_value(2),
            dots.vertices[4].animate.set_color(GREEN),
            dots.vertices[1].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            Circumscribe(number1, fade_out=True),
            Circumscribe(number2, fade_out=True),
            run_time=2
        )
        self.wait()

        self.play(
            FadeOut(number1, number2, paralel_line),
            *[dots.vertices[i].animate.set_color(ORANGE) for i in range(len(dots.vertices))]
        )
        self.wait()

        line = Line(
            [-5, 10, 0],
            [-3.8, -10, 0]
        ).set_color(BLUE)
        self.play(Create(line))
        self.wait()

        number1 = Integer(0, color=GREEN, font_size=120).next_to(square, LEFT, buff=1.5)
        number2 = Integer(6, color=ORANGE, font_size=120).next_to(square, RIGHT, buff=1.5)

        self.play(
            Write(number1),
            Write(number2)
        )
        self.wait()

        self.play(
            line.animate.next_to(dots.vertices[0]),
            number1.animate.set_value(1),
            number2.animate.set_value(5),
            dots.vertices[0].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            line.animate.next_to(dots.vertices[2], buff=0).shift(LEFT*.35),
            number1.animate.set_value(2),
            number2.animate.set_value(4),
            dots.vertices[2].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            line.animate.next_to(dots.vertices[2]),
            number1.animate.set_value(3),
            number2.animate.set_value(3),
            dots.vertices[4].animate.set_color(GREEN),
            rate_func=rate_functions.linear
        )
        self.wait()

        self.play(
            Circumscribe(number1, fade_out=True),
            Circumscribe(number2, fade_out=True)
        )

        self.wait(5)
