from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, GREEN, ORANGE, YELLOW, WHITE, RED, DEGREES, rate_functions
from manim import VMobject, Line, VGroup,  Brace, Circle, Triangle, RoundedRectangle, SurroundingRectangle, NumberLine, ArcBetweenPoints
from manim import MathTex, Tex
from manim import Create, Uncreate, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate, UpdateFromAlphaFunc
from manim import Scene
from manim import always_redraw
from aramanim import Segment
from objects import Apple, Locust, Boy, Girl
from .text import coordinate_text, number_line_text
import numpy as np

class Problem00000(Scene):
    def construct(self):
        shift_vector = 2*UP
        apples = VGroup(*[Apple() for _ in range(7)])
        apples.scale(2.5)
        def set_apples(i = 2):
            apples[-i:].set_opacity(0)
            apples.arrange(RIGHT)
            apples.shift(shift_vector)
            apples[:-i].arrange(RIGHT)
            apples[:-i].shift(shift_vector)
        set_apples()
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
        self.play(Write(boy))
        self.play(Write(girl))
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
        def set_numberline(right = True, sign = 1):
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
                    nl.add(MathTex("{:,}".format(sign*i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5).align_to(nl.n2p(a*i), a*LEFT).shift(0.1*a*RIGHT))
                elif i == 7:
                    nl.add(MathTex("{:,}".format(sign*i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5).align_to(nl.n2p(a*i), a*RIGHT))
                else:
                    nl.add(MathTex("{:,}".format(sign*i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5))
            sr = SurroundingRectangle(nl, color=WHITE, stroke_width = 2, buff=0.05)
            sr.align_to(nl, UP + a*LEFT)
            nl.add(sr)
            return nl
        nl_right = set_numberline()
        nl_right.align_to(DOWN, LEFT+UP)
        nl_left = set_numberline(False)
        nl_left.align_to(DOWN, RIGHT+UP)
        line = Line(8*LEFT, 8*RIGHT).align_to(DOWN, UP)
        self.play(Create(line))
        self.wait()
        locust = Locust()
        locust.scale(0.5)
        locust.set_z_index(1)
        locust.move_to(DOWN)
        self.play(Write(locust))
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
        self.play(jump_to(locust, DOWN + RIGHT))
        self.wait(0.5)
        self.play(locust.animate.flip())
        self.wait(0.25)
        self.play(jump_to(locust, DOWN))
        self.wait(0.5)
        self.play(locust.animate.flip())
        trip =  MathTex("0").add(Triangle().scale(0.3).set_opacity(1).rotate(60*DEGREES).stretch(0.2, 0).move_to(ORIGIN).shift(0.5*DOWN))
        self.play(FadeIn(trip))
        self.play(Write(nl_right))
        self.play(ReplacementTransform(nl_right.copy(), nl_left.next_to(nl_right, DOWN)), run_time = 2)
        self.wait()
        self.play(nl_left.animate.align_to(DOWN, RIGHT+UP), FadeOut(trip))
        self.wait()
        for i in range(1, 6):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.25)
        self.wait()
        equation_5_2_7.move_to(UP)
        equation_7_3_4.move_to(UP)
        self.play(Write(equation_5_2_7[0]))
        self.play(jump_to(locust, nl_right.n2p(6)))
        self.wait()
        self.play(jump_to(locust, nl_right.n2p(7)), Write(equation_5_2_7[1]))
        self.play(Write(equation_5_2_7[2:]))
        self.wait()
        self.play(Indicate(equation_5_2_7))
        self.wait()
        apples.become(VGroup(*[Apple() for _ in range(7)]).scale(2.5))
        set_apples()
        self.play(apples.animate.arrange(RIGHT).shift(shift_vector).set_opacity(1))
        self.wait()
        self.play(FadeOut(apples, equation_5_2_7))
        self.wait(0.25)
        self.play(locust.animate.flip())
        self.wait(0.5)
        for i in range(6, 3, -1):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.35)
        self.play(Indicate(equation_7_3_4))
        self.play(FadeOut(equation_7_3_4))
        self.wait()
        for i in range(3, -3, -1):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.35)
        self.wait()
        self.play(Indicate(nl_left))
        self.wait()
        circle_1 = Circle(0.3).next_to(nl_left.n2p(-2), DOWN, buff=0.38)
        circle_2 = Circle(0.3).next_to(nl_right.n2p(2), DOWN, buff=0.38)
        self.play(Indicate(circle_1), Indicate(circle_2))
        self.play(FadeOut(circle_1, circle_2))
        nl_right_left = set_numberline(False, -1)
        nl_right_left.align_to(DOWN, RIGHT+UP)
        self.play(ReplacementTransform(nl_left, nl_right_left))
        self.wait()
        coordinate_tex = Tex(coordinate_text)
        coordinate_tex.next_to(VGroup(nl_right_left, nl_right), DOWN)
        number_line_tex = Tex(number_line_text)
        number_line_tex.next_to(line, UP)
        coord_rec = RoundedRectangle()
        coord_rec.stretch_to_fit_width(13)
        coord_rec.stretch_to_fit_height(0.8)
        coord_rec.set_stroke(YELLOW)
        coord_rec.next_to(nl_left.n2p(0), DOWN, buff=0.38)
        self.add(coordinate_tex)
        self.play(FadeOut(coord_rec), run_time = 2)
        trip__2 =  MathTex("-2").add(Triangle().scale(0.3).set_opacity(1).rotate(60*DEGREES).stretch(0.2, 0).move_to(ORIGIN).shift(0.5*DOWN))
        trip__2.next_to(nl_right.n2p(-2), UP)
        self.play(FadeOut(coordinate_tex), Indicate(trip__2))
        self.play(FadeOut(trip__2))
        self.wait()
        self.play(FadeOut(equation_5_2_7), run_time = 2)
        self.play(FadeOut(equation_7_3_4), run_time = 2)
        equation_4_6__2 = MathTex("4", "-", "6", "=", "-2")
        equation_4_6__2.scale(1.5)
        equation_4_6__2.move_to(equation_5_2_7)
        self.play(Write(equation_4_6__2))
        self.wait()
        self.play(line.animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW).shift(0.02*UP), run_time = 2)
        self.wait()
        self.add(number_line_tex)
        self.play(line.animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW).shift(0.02*UP), run_time = 2)
        self.play(FadeOut(number_line_tex))
        self.wait()
        self.wait()
        self.play(line.animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW).shift(0.02*UP), run_time = 1)
        self.add(coordinate_tex)
        self.play(Uncreate(coord_rec), run_time = 2)
        self.play(FadeOut(coordinate_tex, equation_4_6__2))
        self.wait()
        plas = MathTex("+").scale(2)
        self.play(locust.animate.flip(), Indicate(plas))
        self.wait(0.25)
        self.play(jump_to(locust, nl_left.n2p(-1)), FadeOut(plas))
        self.wait(0.25)
        min = MathTex("-").scale(2)
        self.play(locust.animate.flip(), Indicate(min))
        self.wait(0.25)
        self.play(jump_to(locust, nl_left.n2p(-2)), FadeOut(min))
        self.wait(0.25)
        self.wait()
        self.play(jump_to(locust, nl_left.n2p(3)))
        self.wait(0.5)
        for i in range(2, -5, -1):
            self.play(jump_to(locust, nl_left.n2p(i)))
            self.wait(0.2)
        self.wait()
        s_3_0 = Segment(nl_left.n2p(3), nl_left.n2p(0), label = "3")
        s_3_0.set_color(RED)
        s_3_0.add(s_3_0.update_label_pos())
        s_3__4 = Segment(nl_left.n2p(3), nl_left.n2p(-4), label = "7")
        s_3__4.set_color(BLUE)
        s_3__4.add(s_3__4.update_label_pos())
        s_0__4 = Segment(nl_left.n2p(0), nl_left.n2p(-4), label = "7-3")
        s_0__4.set_color(GREEN)
        self.play(s_3_0.animate.shift(2*UP))
        self.wait()
        self.play(s_3__4.animate.shift(UP))
        s_0__4.shift(2*UP)
        self.play(Create(s_0__4))
        self.play(Indicate(s_3__4.label))
        self.play(Indicate(s_3_0.label))
        self.play(Write(s_0__4.update_label_pos()))
        s_0__4.add(s_0__4.update_label_pos())
        self.play(FadeOut(s_0__4, s_3_0, s_3__4))
        equation_3_7__4 = MathTex("3", "-", "7", "=", "-", "4")
        equation_3_7__4.scale(1.5)
        equation_3_7__4.move_to(equation_5_2_7)
        self.play(Write(equation_3_7__4[:4]))
        self.play(Write(equation_3_7__4[-1]))
        self.play(Write(equation_3_7__4[-2]))
        self.wait()
        self.play(locust.animate.flip(), FadeOut(equation_3_7__4))

        self.wait(0.25)
        self.play(jump_to(locust, nl_left.n2p(-2)))
        self.wait()
        for i in range(-1, 5, 1):
            w = 0.2 if i != 0 else 1
            self.play(jump_to(locust, nl_left.n2p(i)))
            self.wait(0.5*w)
            if i == 0:
                self.play(FadeOut(MathTex("6-2=4").scale(2)))
            self.wait(0.5*w)
        equation__2_6_4 = MathTex("-2", "+", "6", "=", "4")
        equation__2_6_4.scale(1.5)
        equation__2_6_4.move_to(equation_5_2_7)
        self.play(Write(equation__2_6_4))
        self.wait()
        self.play(FadeOut(equation__2_6_4), locust.animate.flip())
        self.play(jump_to(locust, nl_left.n2p(-3)))
        self.wait()
        for i in range(-4, -6, -1):
            self.play(jump_to(locust, nl_left.n2p(i)))
            self.wait(0.2)
        self.wait()
        s__3_0 = Segment(nl_left.n2p(-3), nl_left.n2p(0), label = "3")
        s__3_0.set_color(RED)
        s__3_0.add(s__3_0.update_label_pos())
        s__3__5 = Segment(nl_left.n2p(-3), nl_left.n2p(-5), label = "2")
        s__3__5.set_color(BLUE)
        s__3__5.add(s__3__5.update_label_pos())
        s_0__5 = Segment(nl_left.n2p(0), nl_left.n2p(-5), label = "3+2")
        s_0__5.set_color(GREEN)
        self.play(s__3_0.animate.shift(2*UP))
        self.wait(0.5)
        self.play(s__3__5.animate.shift(2*UP))
        s_0__5.shift(2*UP)
        self.wait(0.5)
        self.play(s_0__5.animate.shift(DOWN))
        self.wait(0.5)
        self.play(Write(s_0__5.update_label_pos()))
        s_0__5.add(s_0__5.update_label_pos())
        self.play(FadeOut(s__3_0, s__3__5, s_0__5))
        self.wait()
        equation__3__2__5 = MathTex("-3", "-", "-2", "=", "-", "5")
        equation__3__2__5.scale(1.5)
        equation__3__2__5.move_to(equation_5_2_7)
        self.play(Write(equation__3__2__5[:-2]))
        self.play(Write(equation__3__2__5[-1]))
        self.play(Write(equation__3__2__5[-2]))
        self.wait()