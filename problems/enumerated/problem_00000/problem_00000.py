from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, GREEN, ORANGE, YELLOW, WHITE, RED, rate_functions
from manim import VMobject, VGroup,  Brace, NumberLine
from manim import MathTex
from manim import Create, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate
from manim import Scene
from manim import always_redraw
from objects import Apple, Locust
import numpy as np

class Problem00000(Scene):
    def construct(self):
        shift_vector = 2*UP
        apples = VGroup(*[Apple() for _ in range(9)])
        apples.scale(2.5)
        apples[-2:].set_opacity(0)
        apples.arrange(RIGHT)
        apples.shift(shift_vector)
        apples[:-2].arrange(RIGHT)
        apples[:-2].shift(shift_vector)
        brace_7 = always_redraw(lambda: Brace(apples[:-2], DOWN).add(MathTex("7").scale(1.5).next_to(apples[:-2], DOWN, buff = 0.8)))
        brace_2 = always_redraw(lambda: Brace(apples[-2:], DOWN).add(MathTex("2").scale(1.5).next_to(apples[-2:], DOWN, buff = 0.8)))
        equation_7_2_9 = MathTex("7", "+", "2", "=", "9")
        equation_7_2_9.shift(1.5*DOWN)
        equation_7_2_9.scale(1.5)
        equation_9_4_5 = MathTex("9", "-", "4", "=", "5")
        equation_9_4_5.scale(1.5)
        equation_9_4_ = MathTex("9", "-", "4", "=", "?")
        equation_9_4_.scale(1.5)
        self.play(FadeIn(apples))
        self.play(Write(brace_7))
        self.wait()
        self.play(apples.animate.arrange(RIGHT).shift(shift_vector).set_opacity(1))
        self.play(Write(brace_2))
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(brace_7[1].copy(), equation_7_2_9[0]),
                Write(equation_7_2_9[1]),
                ReplacementTransform(brace_2[1].copy(), equation_7_2_9[2]),
                Write(equation_7_2_9[3:]),
                lag_ratio=1
            )
        )
        brace_9 = always_redraw(lambda: Brace(apples, DOWN).add(MathTex("9").scale(1.5).next_to(apples, DOWN, buff = 0.8)))
        self.add(brace_9)
        self.remove(brace_9)
        self.play(
            AnimationGroup(
                FadeOut(brace_7, brace_2),
                Write(brace_9),
                lag_ratio = 0.75
            )
        )
        self.wait()
        self.play(
            FadeOut(brace_9),
            equation_7_2_9.animate.next_to(apples, DOWN)
        )
        self.wait()
        nl = NumberLine(
            x_range=[0, 13, 1],
            length=6.25,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )
        nl.scale(2)
        nl.shift(2*DOWN)
        self.play(
            Write(nl),
            VGroup(apples, equation_7_2_9).animate.scale(0.8).shift(0.75*UP)
        )
        self.wait()
        locust = Locust()
        locust.scale(0.5)
        locust.move_to(nl.n2p(7))
        self.play(Create(locust))
        self.wait()
        def jump_to(mob, point, run_time = 0.5):
            point_initial = mob.get_center()
            path_template = lambda t: np.array([0, 3*t * (1 - t), 0]) 
            jump_path_liner = lambda t: (1 - t) * point_initial + t * point
            jump_path = lambda t: path_template(t) + jump_path_liner(t)
            jump_path_points = [jump_path(t/(int(run_time * 60) - 1)) for t in range(int(run_time * 60))]
            path = VMobject()
            path.set_points_as_corners(jump_path_points)
            animation = MoveAlongPath(mob, path, run_time=run_time, rate_func = rate_functions.linear)
            return animation
        self.play(jump_to(locust, nl.n2p(8)))
        self.wait(0.25)
        self.play(jump_to(locust, nl.n2p(9)))
        self.play(Indicate(equation_7_2_9), run_time = 2)
        self.wait()
        self.play(FadeOut(equation_7_2_9))
        self.play(Write(equation_9_4_))
        self.play(Indicate(equation_9_4_[-1]))
        self.wait()
        self.play(
            apples[:-4].animate.arrange(RIGHT).align_to(apples[-4:], UP),
            apples[-4:].animate.shift(4*RIGHT).set_opacity(0)
        )
        self.wait()
        self.play(locust.animate.flip())
        self.play(jump_to(locust, nl.n2p(8)))
        self.wait(0.25)
        self.play(jump_to(locust, nl.n2p(7)))
        self.wait(0.25)
        self.play(jump_to(locust, nl.n2p(6)))
        self.wait(0.25)
        self.play(jump_to(locust, nl.n2p(5)))
        self.wait()
        self.play(ReplacementTransform(equation_9_4_, equation_9_4_5))
        self.wait(2)