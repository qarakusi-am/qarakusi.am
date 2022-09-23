from this import s
from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, LIGHT_PINK, LIGHT_PINK, YELLOW, WHITE, RED, DEGREES, rate_functions
from manim import VMobject, Line, DashedLine, Arrow, VGroup,  Brace, Circle, Triangle, SurroundingRectangle, NumberLine, ArcBetweenPoints
from manim import MathTex, Tex
from manim import ShowPassingFlash, Wiggle, Create, Circumscribe, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate, UpdateFromAlphaFunc
from manim import Scene
from manim import always_redraw
from aramanim import Segment
from objects import Apple, Locust, Boy, Girl, Thinking
from .text import coordinate_text, number_line_text, step_number_text, left_ruler_text, rigth_ruler_text
import numpy as np

def jump_to(mob, point, run_time = 0.5, hight = 3):
            point_initial = mob.get_center()
            path_template = lambda t: np.array([0, hight*t * (1 - t), 0]) 
            jump_path_liner = lambda t: (1 - t) * point_initial + t * point
            jump_path = lambda t: path_template(t) + jump_path_liner(t)
            jump_path_points = [jump_path(t/(int(run_time * 60) - 1)) for t in range(int(run_time * 60))]
            path = VMobject()
            path.set_points_as_corners(jump_path_points)
            animation = MoveAlongPath(mob, path, run_time=run_time, rate_func = rate_functions.linear)
            return animation

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
        self.play(
            AnimationGroup(
                FadeIn(apples),
                Write(brace_5),
                lag_ratio=1
            )
        )
        self.wait()
        #5+2=7
        self.play(
            AnimationGroup(
                apples.animate.arrange(RIGHT).shift(shift_vector).set_opacity(1),
                Write(brace_2),
                lag_ratio=1
            )
        )
        self.wait()
        self.play(
            ReplacementTransform(brace_5[1].copy(), equation_5_2_7[0]),
            ReplacementTransform(brace_2[1].copy(), equation_5_2_7[2]),
            Write(equation_5_2_7[1])
        )
        self.wait()
        self.play(
            AnimationGroup(
                Write(equation_5_2_7[3:]),
                lag_ratio=1
            )
        )
        brace_7 = always_redraw(lambda: Brace(apples, DOWN).add(MathTex("7").scale(1.5).next_to(apples, DOWN, buff = 0.9)))
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
            FadeOut(equation_5_2_7, shift = UP),
            FadeOut(srd_rec_5, srd_rec_2)
        )
        self.wait()
        brace_3 = always_redraw(
            lambda: Brace(apples[4:], UP).add(
                MathTex("3").scale(1.5).next_to(apples[4:], UP, buff = 0.9)
            )
        )
        #7-3=4
        self.play(
            AnimationGroup(
                FadeIn(brace_3, suspend_mobject_updating = False),
                AnimationGroup(
                    apples[:-3].animate.shift(LEFT),
                    apples[-3:].animate.shift(RIGHT),
                ),
                Write(equation_7_3_4[:-2]),
                lag_ratio=1,
            )
        )
        self.wait()
        brace_4 = always_redraw(
            lambda: Brace(apples[:4], UP).add(
                MathTex("4").scale(1.5).next_to(apples[:4], UP, buff = 0.9)
            )
        )
        self.play(
            AnimationGroup(
                Write(equation_7_3_4[-2:]),
                FadeIn(brace_4),
                lag_ratio=0.75
            )
        )
        self.wait()
        self.play(
            FadeOut(
                apples,
                equation_7_3_4,
                brace_4,
                brace_3,
                brace_7
            )
        )
        #some apples scene (start)
        boy = Boy(2)
        boy.scale(2)
        boy.move_to([-4, -1, 0])
        girl = Girl(3)
        girl.scale(2)
        girl.move_to([4, -1, 0])
        self.wait()
        self.play(
            AnimationGroup(
                Write(boy),
                Write(girl),
                lag_ratio=0.8
            )
        )
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
        self.wait()      
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
        self.wait()
        self.play(FadeOut(boy, girl))
        self.wait()
        #some apples scene (end)
        def set_numberline(right = True, sign = 1, sur = True):
            a = 1 if right else -1
            nl = NumberLine(
                x_range=[0, a*7, 1],
                length=6.5,
                include_tip=False,
                include_numbers=False,
                include_ticks=False
            )
            nl.add(*[
                nl.get_tick(a*x, size=0.15).align_to(nl, UP) for x in range(8)
            ])
            for i in range(8):
                nl.add(MathTex("{:,}".format(sign*i)).next_to(nl.n2p(a*i), DOWN, buff = 0.5))
            if sur:
                sr = SurroundingRectangle(nl, color=WHITE, stroke_width = 2, buff=0.05)
                sr.stretch_to_fit_width((nl.n2p(7) - nl.n2p(0))[0] + 0.75)
                sr.align_to(nl, UP + a*LEFT)
                sr.shift(0.15*a*LEFT)
                nl.add(sr)
            return nl
        nl_right = set_numberline()
        nl_right.shift(-nl_right.n2p(0)+DOWN)
        nl_left = set_numberline(False)
        nl_left.shift(-nl_left.n2p(0)+DOWN)
        line = Line(8*LEFT, 8*RIGHT).align_to(DOWN, UP)
        self.play(Create(line))
        self.wait()
        locust = Locust()
        locust.scale(0.5)
        locust.set_z_index(1)
        locust.move_to(DOWN)
        self.play(FadeIn(locust))
        self.wait()
        self.play(jump_to(locust, DOWN + RIGHT))
        self.play(jump_to(locust, DOWN + 2*RIGHT))
        self.play(jump_to(locust, DOWN + 3*RIGHT))
        self.wait()
        self.play(locust.animate.flip())
        self.wait()
        self.play(jump_to(locust, DOWN + 2*RIGHT))
        self.play(jump_to(locust, DOWN + RIGHT))
        self.play(jump_to(locust, DOWN))
        self.play(locust.animate.flip())
        self.wait()
        trip =  MathTex("0").add(Triangle().scale(0.3).set_opacity(1).rotate(60*DEGREES).stretch(0.2, 0).move_to(ORIGIN).shift(0.5*DOWN))
        self.play(
            FadeIn(trip),
            locust.animate.scale(0.7)
        )
        self.wait()
        self.play(Write(nl_right))
        self.wait()
        self.play(FadeIn(nl_left))
        self.wait()
        self.play(FadeOut(trip))
        self.wait()
        for i in range(1, 6):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.25)
        self.wait()
        #5+2
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
        self.play(
            AnimationGroup(
                apples.animate.arrange(RIGHT).shift(shift_vector).set_opacity(1),
                FadeIn(srd_rec_5, srd_rec_2),
                lag_ratio=0.75
            )
        )
        self.wait()
        self.play(
            FadeOut(
                apples,
                equation_5_2_7,
                srd_rec_5,
                srd_rec_2
            )
        )
        self.wait()
        self.play(locust.animate.flip())
        self.wait()
        #7-3
        for i in range(6, 3, -1):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.35)
        self.play(Indicate(equation_7_3_4))
        self.play(FadeOut(equation_7_3_4))
        self.play(
            apples[:-3].animate.shift(LEFT),
            apples[-3:].animate.shift(RIGHT),
        )
        self.play(FadeIn(brace_7, brace_3, brace_4))
        self.wait()
        self.play(FadeOut(brace_7, brace_3, brace_4, apples))
        self.wait()
        #4-6
        for i in range(3, -3, -1):
            self.play(jump_to(locust, nl_right.n2p(i)))
            self.wait(0.35)
        self.wait()
        self.play(Indicate(nl_left))
        self.wait()
        circle_1 = Circle(0.3).next_to(nl_left.n2p(-2), DOWN, buff=0.38)
        circle_2 = Circle(0.3).next_to(nl_right.n2p(2), DOWN, buff=0.38)
        self.play(Indicate(circle_1), Indicate(circle_2))
        self.wait()
        self.play(FadeOut(circle_1, circle_2))
        nl_right_left = set_numberline(False, -1)
        nl_right_left.shift(-nl_right_left.n2p(0)+DOWN)
        self.wait()
        self.play(ReplacementTransform(nl_left, nl_right_left, lag_ratio=0.05), run_time = 5)
        self.wait()
        locust_ = locust.copy().move_to(nl_left.n2p(4))
        arc = ArcBetweenPoints(nl_left.n2p(4), nl_left.n2p(-2))
        arc_tex = Tex(step_number_text).next_to(arc, UP)
        self.play(FadeIn(locust_, arc_tex), Create(arc))
        self.wait()
        self.play(FadeOut(locust_, arc, arc_tex))
        self.wait()
        self.play(
                *[Indicate(n) for n in nl_right_left[-9:-1]],
                *[Indicate(n) for n in nl_right[-9:-1]]
        )
        coordinate_tex = Tex(coordinate_text)
        coordinate_tex.next_to(VGroup(nl_right_left, nl_right), DOWN)
        number_line_tex = Tex(number_line_text)
        number_line_tex.next_to(line, UP)
        trip__2 =  MathTex("-2").add(Triangle().scale(0.3).set_opacity(1).rotate(60*DEGREES).stretch(0.2, 0).move_to(ORIGIN).shift(0.5*DOWN))
        trip__2.next_to(nl_right.n2p(-2), UP)
        self.wait()
        self.play(
            *[Indicate(n) for n in nl_right_left[-9:-1]],
            *[Indicate(n) for n in nl_right[-9:-1]],
            FadeOut(coordinate_tex),
            Indicate(trip__2),
            run_time = 3
        )
        self.play(FadeOut(trip__2))
        self.wait()
        nl_5_2_7 = NumberLine(
            x_range=[-1, 8.5, 1],
            length=5,
            include_tip=False,
            include_numbers=True,
            include_ticks=True
        )
        nl_7_3_4 = nl_5_2_7.copy()
        VGroup(nl_5_2_7, nl_7_3_4).arrange(RIGHT, buff = 2.5).shift(1.5*UP)
        locust_5_2_7 = Locust().scale(0.2)
        locust_7_3_4 = Locust().scale(0.2).flip()
        def jumping_updater(p_1, p_2, vel = 1):
            def updater(mob, dt, start = p_1, end = p_2, v = vel):
                displacement = end - start
                [x, y, z] = displacement
                v_x = v*np.sign(x)*RIGHT
                v_y_0 = v*np.abs(y/x) + (1/2) * np.abs(x/v)
                t = (mob.get_center()[0] - start[0])/v
                v_y = (v_y_0 - np.sign(x)*t)*UP
                mob.shift((v_x + v_y)*dt)
                if np.abs(mob.get_center()[0] - end[0]) < 0.02 and np.abs(mob.get_center()[1] - end[1]) < 0.02:
                    mob.move_to(start)
            return updater
        locust_5_2_7.move_to(nl_5_2_7.n2p(5))
        locust_7_3_4.move_to(nl_7_3_4.n2p(7))
        locust_5_2_7.add_updater(jumping_updater(nl_5_2_7.n2p(5), nl_5_2_7.n2p(7)))
        locust_7_3_4.add_updater(jumping_updater(nl_7_3_4.n2p(7), nl_7_3_4.n2p(4), 3/2))
        self.play(
            FadeIn(equation_5_2_7.next_to(nl_5_2_7, UP, buff=1)),
            FadeIn(equation_7_3_4.next_to(nl_7_3_4, UP, buff=1)),
            FadeIn(locust_5_2_7, locust_7_3_4),
            Write(nl_5_2_7), Write(nl_7_3_4)
        )
        self.wait(2)
        self.play(Circumscribe(VGroup(nl_5_2_7, equation_5_2_7), color=BLUE), run_time = 1.5)
        self.wait()
        self.play(Circumscribe(VGroup(nl_7_3_4, equation_7_3_4), color=BLUE), run_time = 1.5)
        self.wait(3)
        equation_4_6__2 = MathTex("4", "-", "6", "=", "-2")
        equation_4_6__2.scale(1.5)
        equation_4_6__2.next_to(VGroup(nl_right_left, nl_right), DOWN)
        self.wait()
        self.play(Write(equation_4_6__2))
        self.wait(3)
        self.play(ShowPassingFlash(line.copy().set_stroke(YELLOW, 8)), run_time = 2)
        self.wait(2)
        nl_l = set_numberline(True, 1, False)
        nl_l.shift(-nl_l.n2p(0)+DOWN)
        nl_r = set_numberline(False, -1, False)
        nl_r.shift(-nl_r.n2p(0)+DOWN)
        self.play(
            Indicate(number_line_tex),
            ShowPassingFlash(line.copy().set_stroke(YELLOW, 8)),
            run_time = 2
        )
        self.add(nl_l, nl_r)
        self.play(FadeOut(number_line_tex, nl_right, nl_right_left))
        self.wait(2)
        self.add(coordinate_tex.next_to(VGroup(nl_right_left, nl_right), UP))
        self.play(
            *[Indicate(n) for n in nl_l[-8:]],
            *[Indicate(n) for n in nl_r[-8:]],
            run_time = 2
        )
        self.play(FadeOut(coordinate_tex))
        self.wait()
        self.play(FadeIn(locust_, arc_tex), Create(arc))
        self.wait()
        self.play(FadeOut(locust_, arc, arc_tex))
        self.wait()
        plas = MathTex("+").scale(2)
        self.play(locust.animate.flip(), Indicate(plas))
        self.wait()
        self.play(jump_to(locust, nl_left.n2p(-1)))
        self.play(jump_to(locust, nl_left.n2p(0)))
        self.play(jump_to(locust, nl_left.n2p(1)), FadeOut(plas))
        self.wait(2)
        min = MathTex("-").scale(2)
        self.play(locust.animate.flip(), Indicate(min))
        self.wait()
        self.play(jump_to(locust, nl_left.n2p(0)))
        self.play(jump_to(locust, nl_left.n2p(-1)))
        self.play(jump_to(locust, nl_left.n2p(-2)), FadeOut(min))
        self.wait(3)
        th = Thinking()
        self.play(FadeIn(th))
        self.wait(2)
        self.play(FadeOut(equation_4_6__2))
        self.play(FadeOut(th))
        self.play(FadeOut(
            locust_5_2_7, locust_7_3_4,
            nl_5_2_7, nl_7_3_4,
            equation_5_2_7, equation_7_3_4
        ))
        self.wait()
        #3-7
        equation_3_7__4 = MathTex("3", "-", "7", "=", "-", "4")
        equation_3_7__4.scale(1.5)
        equation_3_7__4.next_to(VGroup(nl_right_left, nl_right), DOWN)
        self.wait()
        self.play(locust.animate.move_to(nl_left.n2p(3)))
        self.wait()
        self.play(Write(equation_3_7__4[:3]))
        self.wait()
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
        s_0__4.set_color(LIGHT_PINK)
        self.play(s_3_0.animate.shift(2.5*UP))
        self.wait()
        self.play(s_3__4.animate.shift(1.5*UP))
        s_0__4.shift(2.5*UP)
        dash = DashedLine(ORIGIN, 3.5*UP).next_to(nl_l.n2p(0), UP, buff= 0)
        arr = Arrow(start=0.5*RIGHT, end=LEFT).next_to(dash, LEFT, buff=0, aligned_edge=UP)
        left_ruler_ = Tex(left_ruler_text).next_to(arr, LEFT)
        self.wait()
        
        big_3__7 = VGroup(
            equation_3_7__4.copy(),
            s_3_0.copy(),
            s_3__4.copy(),
            s_0__4.copy().add(s_0__4.update_label_pos().copy()),
            locust.copy(),
            nl_l.copy(),
            nl_r.copy()
        )
        self.wait()
        self.play(Create(s_0__4))
        self.wait()
        self.play(Indicate(s_3__4.label, 1.5))
        self.wait()
        self.play(Indicate(s_3_0.label, 1.5))
        self.wait()
        self.play(Write(s_0__4.update_label_pos()))
        s_0__4.add(s_0__4.update_label_pos())
        self.wait()
        self.play(Wiggle(s_0__4))
        self.wait()
        self.play(Write(equation_3_7__4[-3]))
        self.play(Indicate(equation_3_7__4[-1]))
        self.wait()
        self.play(Create(dash))
        self.play(FadeIn(arr))
        self.play(Write(left_ruler_))
        self.wait()
        self.play(Write(equation_3_7__4[-2]), Indicate(nl_r))
        self.play(FadeOut(dash, arr, left_ruler_))
        self.wait()
        self.play(
            FadeOut(s_0__4, s_3_0, s_3__4, equation_3_7__4, suspend_mobject_updating = True),
            big_3__7.animate.scale(0.3).to_corner(UL)
        )
        self.wait()
        #1-5=-4
        equation_1__5__4 = MathTex("1", "-", "5", "=", "-", "4")
        equation_1__5__4.scale(1.5)
        equation_1__5__4.next_to(VGroup(nl_right_left, nl_right), DOWN)
        locust.move_to(nl_r.n2p(1))
        self.play(Write(equation_1__5__4[:3]))
        self.play(jump_to(locust, nl_r.n2p(-4)))
        s_1_0 = Segment(nl_left.n2p(1), nl_left.n2p(0), label = "1")
        s_1_0.set_color(RED)
        s_1_0.add(s_1_0.update_label_pos())
        s_1__4 = Segment(nl_left.n2p(1), nl_left.n2p(-4), label = "5")
        s_1__4.set_color(BLUE)
        s_1__4.add(s_1__4.update_label_pos())
        s_0__4 = Segment(nl_left.n2p(0), nl_left.n2p(-4), label = "5-1")
        s_0__4.set_color(LIGHT_PINK)
        self.play(s_1_0.animate.shift(2.5*UP))
        self.play(s_1__4.animate.shift(1.5*UP))
        s_0__4.shift(2.5*UP)
        self.play(Create(s_0__4))
        self.play(Write(s_0__4.update_label_pos()))
        self.play(Write(equation_1__5__4[3:]))
        s_0__4.add(s_0__4.update_label_pos())
        self.wait()
        self.play(FadeOut(s_0__4, s_1_0, s_1__4, equation_1__5__4, big_3__7))
        self.wait()
        #-2+6
        self.play(locust.animate.move_to(nl_l.n2p(-2)).flip())
        self.wait()
        equation__2_6_4 = MathTex("-2", "+", "6", "=", "4")
        equation__2_6_4.scale(1.5)
        equation__2_6_4.next_to(VGroup(nl_right_left, nl_right), DOWN)
        self.play(Write(equation__2_6_4[:3]))
        s__2_0 = Segment(nl_left.n2p(-2), nl_left.n2p(0), label = "2")
        s__2_0.set_color(RED)
        s__2_0.add(s__2_0.update_label_pos())
        s__2_4 = Segment(nl_left.n2p(-2), nl_left.n2p(4), label = "6")
        s__2_4.set_color(BLUE)
        s__2_4.add(s__2_4.update_label_pos())
        s_0_4 = Segment(nl_left.n2p(0), nl_left.n2p(4), label = "6-2")
        s_0_4.set_color(LIGHT_PINK)
        s_0_4.shift(2.5*UP)
        self.wait()
        for i in range(-1, 5, 1):
            self.play(jump_to(locust, nl_left.n2p(i)))
            if i == 0:
                self.wait()
                self.play(
                    FadeOut(MathTex("6-2=4").scale(2)),
                    run_time = 2
                )
                self.wait()
            self.wait(0.25)
        self.play(s__2_0.animate.shift(2.5*UP), s__2_4.animate.shift(1.5*UP))
        self.wait()
        arr_ = Arrow(start=0.5*LEFT, end=RIGHT).next_to(dash, RIGHT, buff=0, aligned_edge=UP)
        rigth_ruler_ = Tex(rigth_ruler_text).next_to(arr_, RIGHT)
        self.play(Create(s_0_4), Write(s_0_4.update_label_pos()))
        s_0_4.add(s_0_4.update_label_pos())
        self.wait()
        self.play(Create(dash))
        self.play(FadeIn(arr_))
        self.play(Write(rigth_ruler_))
        self.wait()
        self.play(Write(equation__2_6_4[3:]))
        self.wait()
        self.play(FadeOut(equation__2_6_4, s_0_4, s__2_4, s__2_0, dash, arr_, rigth_ruler_))
        self.wait()
        #-3-2
        equation__3__2__5 = MathTex("-3", "-", "2", "=", "-", "5")
        equation__3__2__5.scale(1.5)
        equation__3__2__5.next_to(VGroup(nl_right_left, nl_right), DOWN)
        self.play((locust.animate.move_to(nl_left.n2p(-3)).flip()))
        self.wait()
        self.play(Write(equation__3__2__5[:3]))
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
        s_0__5.set_color(LIGHT_PINK)
        self.play(s__3_0.animate.shift(2*UP))
        self.wait(0.5)
        self.play(s__3__5.animate.shift(2*UP))
        s_0__5.shift(2*UP)
        self.wait(0.5)
        self.play(s_0__5.animate.shift(DOWN))
        self.wait(0.5)
        self.play(Write(s_0__5.update_label_pos()))
        s_0__5.add(s_0__5.update_label_pos())
        self.wait()
        self.play(Create(dash))
        self.play(FadeIn(arr))
        self.play(Write(left_ruler_))
        self.wait()
        self.play(AnimationGroup(
            Write(equation__3__2__5[-3]),
            Write(equation__3__2__5[-1]),   
            Write(equation__3__2__5[-2]),
            lag_ratio=1
        ))
        self.wait()
        self.play(FadeOut(dash, arr, left_ruler_))
        self.play(FadeOut(s__3_0, s__3__5, s_0__5, equation__3__2__5))
        self.wait()
        self.play(FadeOut(locust, nl_l, nl_r, line))
        self.wait()
        ########
        nl_6__9__3 = NumberLine(
            x_range=[-4, 6.5, 1],
            length=5,
            include_tip=False,
            include_numbers=True,
            include_ticks=True
        )
        nl__4__5__9 = NumberLine(
            x_range=[-10, -1, 1],
            length=5,
            include_tip=False,
            include_numbers=True,
            include_ticks=True
        )
        VGroup(nl_6__9__3, nl__4__5__9).arrange(RIGHT, buff=2.75).shift(2*DOWN)
        locust__4__5__9 = Locust().scale(0.2).flip()
        locust_6__9__3 = Locust().scale(0.2).flip()
        locust_6__9__3.move_to(nl_6__9__3.n2p(6))
        locust__4__5__9.move_to(nl__4__5__9.n2p(-4))
        locust_6__9__3.add_updater(jumping_updater(nl_6__9__3.n2p(6), nl_6__9__3.n2p(-3)))
        locust__4__5__9.add_updater(jumping_updater(nl__4__5__9.n2p(-4), nl__4__5__9.n2p(-9)))
        equation__4__5__9 = MathTex("-4", "-", "5", "=", "-9").next_to(nl__4__5__9, UP, buff=2.5)
        equation_6__9__3 = MathTex("6", "-", "9", "=", "-3").next_to(nl_6__9__3, UP, buff=2.5)
        self.play(Write(nl_6__9__3))
        self.wait()
        self.play(FadeIn(locust_6__9__3), Write(equation_6__9__3))
        self.wait()
        self.play(Write(nl__4__5__9))
        self.wait()
        self.play(FadeIn(locust__4__5__9), Write(equation__4__5__9))
        self.wait(6)
