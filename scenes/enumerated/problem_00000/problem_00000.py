from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, GREEN, ORANGE, YELLOW, WHITE, RED, rate_functions
from manim import VMobject, VGroup,  Brace, SurroundingRectangle, NumberLine, ArcBetweenPoints
from manim import MathTex
from manim import Create, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate, UpdateFromAlphaFunc
from manim import Scene
from manim import always_redraw
from objects import Apple, Locust, Boy, Girl
import numpy as np

class Problem00000(Scene):
    def construct(self):
        shift_vector = 2*UP
        apples = VGroup(*[Apple() for _ in range(7)])
        apples.scale(2.5)
        apples[-2:].set_opacity(0)
        apples.arrange(RIGHT)
        apples.shift(shift_vector)
        apples[:-2].arrange(RIGHT)
        apples[:-2].shift(shift_vector)
        brace_5 = always_redraw(lambda: Brace(apples[:-2], DOWN).add(MathTex("5").scale(1.5).next_to(apples[:-2], DOWN, buff = 0.9)))
        brace_2 = always_redraw(lambda: Brace(apples[-2:], DOWN).add(MathTex("2").scale(1.5).next_to(apples[-2:], DOWN, buff = 0.9)))
        equation_5_2_7 = MathTex("5", "+", "2", "=", "7")
        equation_5_2_7.shift(1.5*DOWN)
        equation_5_2_7.scale(1.5)
        equation_7_3_4 = MathTex("7", "-", "3", "=", "4")
        equation_7_3_4.shift(1.5*DOWN)
        equation_7_3_4.scale(1.5)
        equation_9_4_ = MathTex("9", "-", "4", "=", "?")
        equation_9_4_.scale(1.5)
        self.play(FadeIn(apples))
        self.play(Write(brace_5))
        self.wait()
        self.play(apples.animate.arrange(RIGHT).shift(shift_vector).set_opacity(1))
        self.play(Write(brace_2))
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(brace_5[1].copy(), equation_5_2_7[0]),
                Write(equation_5_2_7[1]),
                ReplacementTransform(brace_2[1].copy(), equation_5_2_7[2]),
                Write(equation_5_2_7[3:]),
                lag_ratio=1
            )
        )
        brace_7 = always_redraw(lambda: Brace(apples, DOWN).add(MathTex("7").scale(1.5).next_to(apples, DOWN, buff = 0.9)))
        self.add(brace_7)
        self.remove(brace_7)
        srd_rec_5 = SurroundingRectangle(apples[:-2], stroke_width = 2, buff=0.05)
        srd_rec_2 = SurroundingRectangle(apples[-2:], stroke_width = 2, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(srd_rec_5, srd_rec_2),
                FadeOut(brace_5, brace_2),
                Write(brace_7),
                lag_ratio = 0.75
            )
        )
        self.wait()
        self.play(
            FadeOut(brace_7),
            FadeOut(equation_5_2_7, shift = UP)
        )
        self.play(FadeOut(srd_rec_5, srd_rec_2))
        self.wait()
        self.play(FadeIn(equation_7_3_4, shift = DOWN))
        self.play(
            apples[:-3].animate.arrange(RIGHT).align_to(apples[-4:], UP),
            apples[-3:].animate.shift(4*RIGHT).set_opacity(0)
        )
        self.wait()
        self.play(
            FadeOut(apples, equation_7_3_4)
        )
        boy = Boy(2)
        boy.scale(2)
        boy.move_to([-4, -1, 0])
        girl = Girl(3)
        girl.scale(2)
        girl.move_to([4, -1, 0])
        self.play(Create(boy))
        self.play(Create(girl))
        def apple_exchange(vmob, to_girl = True):
            arc = (ArcBetweenPoints(boy.get_center() + 0.5*UP, girl.get_center() + 0.5*UP, radius = 8) if to_girl
            else ArcBetweenPoints(girl.get_center() + 0.5*UP, boy.get_center() + 0.5*UP, radius = 5))
            def alfa_func(mob, alpha, a = arc, m = vmob.copy()):
                mob.become(m)
                mob.move_to(a.point_from_proportion(alpha))
                mob.scale(2*alpha*(1-alpha) + 1)
                mob.set_opacity(1-((2*alpha-1)**4))
            return alfa_func
        apple_1 = Apple().set_opacity(0)
        apple_2 = Apple(color = RED).set_opacity(0)
        apple_3 = Apple().set_opacity(0)
        apple_1.scale(1.5)
        apple_2.scale(1.5)
        apple_3.scale(1.5)        
        self.add(apple_1, apple_2, apple_3)        
        self.play(
            AnimationGroup(
                UpdateFromAlphaFunc(apple_1, apple_exchange(apple_1)),
                UpdateFromAlphaFunc(apple_2, apple_exchange(apple_2, False)),
                UpdateFromAlphaFunc(apple_3, apple_exchange(apple_3)),
                lag_ratio=0.65
            ),
            run_time = 4
        )
        self.remove(apple_1, apple_2, apple_3) 
        self.play(FadeOut(boy, girl))
        self.wait()
        def set_numberline(right = True):
            a = 1 if right else -1
            nl = NumberLine(
                x_range=[0, a*7, 1],
                length=6,
                include_tip=False,
                include_numbers=False,
                include_ticks=False
            )
            nl.add(*[
                nl.get_tick(a*x, size=0.15).align_to(nl, UP) for x in range(8)
            ])
            for i in range(8):
                if i == 0:
                    nl.add(MathTex("{:,}".format(i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5).align_to(nl.n2p(a*i), a*LEFT).shift())
                elif i == 7:
                    nl.add(MathTex("{:,}".format(i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5).align_to(nl.n2p(a*i), a*RIGHT))
                else:
                    nl.add(MathTex("{:,}".format(i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5))
            sr = SurroundingRectangle(nl, color=WHITE, stroke_width = 2, buff=0.05)
            sr.align_to(nl, UP + a*LEFT)
            nl.add(sr)
            return nl
        nl_right = set_numberline()
        nl_right.align_to(DOWN, LEFT+UP)
        nl_left = set_numberline(False)
        nl_left.align_to(DOWN, RIGHT+UP)
        self.play(Write(nl_right))
        self.play(Write(nl_left))
        self.wait()

        #nl = NumberLine(
        #    x_range=[0, 13, 1],
        #    length=6.25,
        #    color=BLUE,
        #    include_numbers=True,
        #    label_direction=DOWN,
        #)
        #nl.scale(2)
        #nl.shift(2*DOWN)
        #self.play(
        #    Write(nl),
        #    VGroup(apples, equation_5_2_7).animate.scale(0.8).shift(0.75*UP)
        #)
        #self.wait()
        #locust = Locust()
        #locust.scale(0.5)
        #locust.move_to(nl.n2p(7))
        #self.play(Create(locust))
        #self.wait()
        #def jump_to(mob, point, run_time = 0.5):
        #    point_initial = mob.get_center()
        #    path_template = lambda t: np.array([0, 3*t * (1 - t), 0]) 
        #    jump_path_liner = lambda t: (1 - t) * point_initial + t * point
        #    jump_path = lambda t: path_template(t) + jump_path_liner(t)
        #    jump_path_points = [jump_path(t/(int(run_time * 60) - 1)) for t in range(int(run_time * 60))]
        #    path = VMobject()
        #    path.set_points_as_corners(jump_path_points)
        #    animation = MoveAlongPath(mob, path, run_time=run_time, rate_func = rate_functions.linear)
        #    return animation
        #self.play(jump_to(locust, nl.n2p(8)))
        #self.wait(0.25)
        #self.play(jump_to(locust, nl.n2p(9)))
        #self.play(Indicate(equation_5_2_7), run_time = 2)
        #self.wait()
        #self.play(FadeOut(equation_5_2_7))
        #self.play(Write(equation_9_4_))
        #self.play(Indicate(equation_9_4_[-1]))
        #self.wait()
        #self.play(locust.animate.flip())
        #self.play(jump_to(locust, nl.n2p(8)))
        #self.wait(0.25)
        #self.play(jump_to(locust, nl.n2p(7)))
        #self.wait(0.25)
        #self.play(jump_to(locust, nl.n2p(6)))
        #self.wait(0.25)
        #self.play(jump_to(locust, nl.n2p(5)))
        #self.wait()
        #self.play(ReplacementTransform(equation_9_4_, equation_7_3_4))
        #self.wait(2)