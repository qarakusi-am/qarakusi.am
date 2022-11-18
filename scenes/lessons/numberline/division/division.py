from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, GREEN, LIGHT_PINK, YELLOW, WHITE, RED, DEGREES, rate_functions
from manim import VMobject, Line, DashedLine, Arrow, VGroup,  Brace, Circle, SurroundingRectangle, RoundedRectangle, NumberLine, ArcBetweenPoints
from manim import MathTex, Tex
from manim import ShowPassingFlash, Wiggle, Create, Circumscribe, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate, UpdateFromAlphaFunc, MoveToTarget
from manim import Scene
from manim import always_redraw
from aramanim import Segment, CutOut, CutIn
from objects import SimpleSVGMobject, DScissors, AppleSLices
from .text import method_1, method_2, quotient, remainder, group
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

class Division(Scene):
    def construct(self):
        apple = SimpleSVGMobject('green_apple')
        apple.set_color(GREEN)
        quotient_tex = Tex(quotient).scale(0.9)
        remainder_tex = Tex(remainder).scale(0.9)
        boy_1 = SimpleSVGMobject('boy_1').scale(0.5)
        boy_2 = SimpleSVGMobject('boy_2').scale(0.5)
        girl_1 = SimpleSVGMobject('girl_1').scale(0.5)
        girl_2 = SimpleSVGMobject('girl_3').scale(0.5)
    
    #8 : 2 = 4
        div_8_2 = MathTex('8:2', '=', '4')
        div_8_2.scale(3)
        self.play(Write(div_8_2))
        self.wait()
        self.play(div_8_2.animate.to_corner(UP, buff=0.5).scale(0.5))
        self.wait()
    
    # 2 methods
        rect_1 = RoundedRectangle(corner_radius=0.33, height=9/2.45, width=16/2.45)
        rect_2 = RoundedRectangle(corner_radius=0.33, height=9/2.45, width=16/2.45)
        VGroup(rect_1, rect_2).arrange(RIGHT, buff=1).to_corner(DOWN, buff=1.5)
        tex_method_1 = Tex(method_1)
        tex_method_1.set_color(BLUE)
        tex_method_2 = Tex(method_2)
        tex_method_2.set_color(RED)
        tex_method_1.next_to(rect_1, UP, aligned_edge=LEFT)
        tex_method_2.next_to(rect_2, UP, aligned_edge=LEFT)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Write(tex_method_1),
                    Write(tex_method_2)),
                AnimationGroup(
                    Create(rect_1),
                    Create(rect_2)),
                lag_ratio=0.75),
            run_time=2)
    
    #8 : 2 = 4 in method 1
        apples_m1 = VGroup(*[apple.copy().scale(1.3) for _ in range(8)])
        apples_m1.arrange(RIGHT, buff=0.15)
        apples_m1.move_to(rect_1)
        apples_m1.generate_target()
        VGroup(apples_m1.target[:4], apples_m1.target[-4:]).arrange(DOWN, buff=1.25).move_to(rect_1)
        apples_m1.target[:4].set_color(RED)
        apples_m1.target[-4:].set_color(BLUE)
        self.play(
            AnimationGroup(*[FadeIn(apple) for apple in apples_m1], lag_ratio=0.05))
        self.wait()
        self.play(MoveToTarget(apples_m1))
        self.play(
            FadeIn(girl_1.next_to(apples_m1[:4], LEFT)),
            FadeIn(boy_1.next_to(apples_m1[-4:], LEFT)))
        self.wait()
        count_4_m1 = VGroup(
            MathTex('1').scale(0.7).set_opacity(0).next_to(apples_m1[4], DOWN),
            MathTex('2').scale(0.7).set_opacity(0).next_to(apples_m1[5], DOWN),
            MathTex('3').scale(0.7).set_opacity(0).next_to(apples_m1[6], DOWN),
            MathTex('4').scale(0.7).set_opacity(0).next_to(apples_m1[7], DOWN))    
        self.play(
            AnimationGroup(
                *[AnimationGroup(
                    Indicate(apples_m1[i]),
                    Indicate(apples_m1[i+4]),
                    Write(count_4_m1[i].set_opacity(1))) for i in range(4)],
                lag_ratio=0.25),
                run_time = 1)
        self.wait(2)
    
    #8 : 2 = 4 in method 2
        apples_m2 = VGroup(*[apple.copy().scale(1.3) for _ in range(8)])
        apples_m2.arrange(RIGHT, buff=0.15)
        apples_m2.move_to(rect_2)
        apples_m2.generate_target()
        VGroup(
            apples_m2.target[:2],
            apples_m2.target[2:4],
            apples_m2.target[4:6],
            apples_m2.target[6:]).arrange_in_grid(2, 2, buff=(1.5, 0.75))
        apples_m2.target[:2].set_color(RED)        
        apples_m2.target[2:4].set_color(BLUE)
        apples_m2.target[4:6].set_color(YELLOW)
        apples_m2.target[6:].set_color(GREEN)
        self.play(
            AnimationGroup(*[FadeIn(apple) for apple in apples_m2], lag_ratio=0.05))
        self.wait()
        self.play(Circumscribe(apples_m2[:2]))
        self.wait(0.5)
        self.play(MoveToTarget(apples_m2))
        self.wait()
        surrect_4_m2 = VGroup(
            SurroundingRectangle(apples_m2[:2]).add(MathTex('1').scale(0.7).next_to(apples_m2[:2], RIGHT)),
            SurroundingRectangle(apples_m2[2:4]).add(MathTex('2').scale(0.7).next_to(apples_m2[2:4], RIGHT)),
            SurroundingRectangle(apples_m2[4:6]).add(MathTex('3').scale(0.7).next_to(apples_m2[4:6], RIGHT)),
            SurroundingRectangle(apples_m2[6:]).add(MathTex('4').scale(0.7).next_to(apples_m2[6:], RIGHT))
        )
        self.play(AnimationGroup(*[Write(s) for s in surrect_4_m2], lag_ratio=0.25))
        self.wait()
    
    #8 : 2 = 4 cleanup
        self.play(
            AnimationGroup(
                FadeOut(div_8_2),
                FadeOut(surrect_4_m2, count_4_m1),
                FadeOut(apples_m1, apples_m2, boy_1, girl_1),
                lag_ratio=0.25))
        self.wait()
    
    #13 : 4
        div_13_4 = MathTex('13:4')
        div_13_4.scale(3)
        div_13_4.to_corner(UP, buff=0.5)
        self.play(Write(div_13_4))
        self.wait()
        self.play(div_13_4.animate.to_corner(UP, buff=0.5).scale(0.5))
        self.wait()
    
    #13 : 4  in method 1
        apples_13_m1 = VGroup(*[apple.copy().scale(0.8) for _ in range(13)])
        apples_13_m1.arrange(RIGHT, buff=0.15)
        apples_13_m1.move_to(rect_1)
        apples_13_m1.generate_target()
        VGroup(
            VGroup(
                apples_13_m1.target[:3].set_color(RED).scale(1.25),
                apples_13_m1.target[3:6].set_color(BLUE).scale(1.25),
                apples_13_m1.target[6:9].set_color(YELLOW).scale(1.25),
                apples_13_m1.target[9:12].set_color(LIGHT_PINK).scale(1.25)).arrange(DOWN),
                apples_13_m1.target[12].scale(1.25)).arrange(RIGHT, buff=2, aligned_edge=UP).move_to(rect_1).shift(0.1*UP)
        self.play(
            AnimationGroup(*[FadeIn(apple) for apple in apples_13_m1], lag_ratio=0.05))
        self.wait()
        self.play(MoveToTarget(apples_13_m1))
        self.play(
            FadeIn(boy_1.scale(0.725).next_to(apples_13_m1[:3], LEFT)),
            FadeIn(girl_1.scale(0.725).next_to(apples_13_m1[3:6], LEFT)),
            FadeIn(boy_2.scale(0.725).next_to(apples_13_m1[6:9], LEFT)),
            FadeIn(girl_2.scale(0.725).next_to(apples_13_m1[9:12], LEFT)))
        self.wait()
        count_3_m1 = VGroup(
            MathTex('1').scale(0.7).set_opacity(0).next_to(apples_13_m1[9], DOWN),
            MathTex('2').scale(0.7).set_opacity(0).next_to(apples_13_m1[10], DOWN),
            MathTex('3').scale(0.7).set_opacity(0).next_to(apples_13_m1[11], DOWN),
            MathTex('1').scale(0.7).set_opacity(0).next_to(apples_13_m1[12], DOWN))
        self.play(
            AnimationGroup(
                *[AnimationGroup(
                    Indicate(apples_13_m1[i]),
                    Indicate(apples_13_m1[i+3]),
                    Indicate(apples_13_m1[i+6]),
                    Indicate(apples_13_m1[i+9]),
                    Write(count_3_m1[i].set_opacity(1))) for i in range(3)],
                lag_ratio=0.25),
                run_time = 1)
        self.wait()
        self.play(Indicate(apples_13_m1[12]), Write(count_3_m1[3].set_opacity(1)))
        self.wait()
        surrec_13_quotient = SurroundingRectangle(count_3_m1[2], color=BLUE, buff=0.2, corner_radius=0.25)
        surrec_13_quotient.set_fill(BLACK, 0.75)
        count_3_m1[2].set_z_index(1)
        quotient_tex.add_background_rectangle()
        quotient_tex.next_to(count_3_m1[2], RIGHT, buff=1.4)
        arrow_13_quotient = Arrow(surrec_13_quotient.get_corner(RIGHT), quotient_tex.get_corner(LEFT))
        self.play(AnimationGroup(
            Create(surrec_13_quotient),
            Create(arrow_13_quotient),
            Write(quotient_tex),
            lag_ratio=0.05), run_time = 2)
        self.wait()
        surrec_13_remainder = SurroundingRectangle(VGroup(count_3_m1[3], apples_13_m1[12]), color=YELLOW, corner_radius=0.25)
        remainder_tex.add_background_rectangle()
        remainder_tex.next_to(count_3_m1[3], DOWN, buff=1.25)
        remainder_tex.align_to(quotient_tex, LEFT)
        arrow_13_remainder = Arrow(surrec_13_remainder.get_corner(DOWN), remainder_tex.get_corner(UP))
        self.play(AnimationGroup(
            Create(surrec_13_remainder),
            Create(arrow_13_remainder),
            Write(remainder_tex),
            lag_ratio=0.05), run_time = 2)
        self.wait()
        self.play(Indicate(count_3_m1[2]))
        self.wait()
        self.play(Indicate(count_3_m1[3]))
        self.wait()
        self.play(AnimationGroup(
            FadeOut(surrec_13_remainder, surrec_13_quotient),
            FadeOut(arrow_13_remainder, arrow_13_quotient),
            FadeOut(remainder_tex, quotient_tex),
            lag_ratio=0.05))
        self.wait(2)
    
    #13 : 4  in method 2
        apples_13_m2 = VGroup(*[apple.copy().scale(0.8) for _ in range(13)])
        apples_13_m2.arrange(RIGHT, buff=0.15)
        apples_13_m2.move_to(rect_2)
        apples_13_m2.generate_target()
        VGroup(
            VGroup(
                apples_13_m2.target[:4].scale(1.25).set_color(RED) ,
                apples_13_m2.target[4:8].scale(1.25).set_color(BLUE),
                apples_13_m2.target[8:12].scale(1.25).set_color(YELLOW)).arrange(DOWN, buff=0.75),
            apples_13_m2.target[12].scale(1.25)).arrange(RIGHT, buff=2, aligned_edge=UP).move_to(rect_2)
        self.play(
            AnimationGroup(*[FadeIn(apple) for apple in apples_13_m2], lag_ratio=0.05))
        self.wait()
        self.play(Circumscribe(apples_13_m2[:4]))
        self.wait(0.5)
        self.play(MoveToTarget(apples_13_m2))
        self.wait()
        surrect_13_m2 = VGroup(
            SurroundingRectangle(apples_13_m2[:4]).add(MathTex('1').scale(0.7).next_to(apples_13_m2[:4], RIGHT)),
            SurroundingRectangle(apples_13_m2[4:8]).add(MathTex('2').scale(0.7).next_to(apples_13_m2[4:8], RIGHT)),
            SurroundingRectangle(apples_13_m2[8:12]).add(MathTex('3').scale(0.7).next_to(apples_13_m2[8:12], RIGHT)))
        self.play(AnimationGroup(*[Write(s) for s in surrect_13_m2], lag_ratio=0.25))
        remainder_13_m2 = MathTex('1').scale(0.7).next_to(apples_13_m2[12], DOWN)
        self.play(Write(remainder_13_m2))
        self.wait(2)
    
    #comparing methods 1 and 2
        apples_13_m1_12 = AppleSLices()
        apples_13_m1_12.match_width(apples_13_m1[12])
        apples_13_m1_12.align_to(apples_13_m1[12], DOWN + LEFT)
        self.play(Indicate(apples_13_m1[12]))
        cut_lines = DashedLine(ORIGIN, DOWN).add(DashedLine(0.5*(DOWN+LEFT), 0.5*(DOWN+RIGHT)))
        self.wait()
        self.play(Create(cut_lines.move_to(apples_13_m1[12])))
        apples_13_m1[12].set_opacity(0)
        self.play(
            apples_13_m1_12.apple_ul.animate.shift(0.25*UP + LEFT),
            apples_13_m1_12.apple_dl.animate.shift(0.25*DOWN + LEFT),
            apples_13_m1_12.apple_ur.animate.shift(0.25*UP + RIGHT),
            apples_13_m1_12.apple_dr.animate.shift(0.25*DOWN + RIGHT),
            cut_lines.animate.set_opacity(0),
            count_3_m1[-1].animate.set_opacity(0))
        self.play(
            apples_13_m1_12.apple_ul.animate.set_color(RED).next_to(apples_13_m1.target[:3]),
            apples_13_m1_12.apple_dl.animate.set_color(BLUE).next_to(apples_13_m1.target[3:6]),
            apples_13_m1_12.apple_ur.animate.set_color(YELLOW).next_to(apples_13_m1.target[6:9]),
            apples_13_m1_12.apple_dr.animate.set_color(LIGHT_PINK).next_to(apples_13_m1.target[9:12]))
        self.wait()
        frac = MathTex(r'13:4 = 3\frac{1}{4}')
        frac.scale(0.7)
        frac.next_to(apples_13_m1_12)
        frac.shift(0.1*RIGHT)
        self.play(Write(frac))
        self.wait()
        self.play(Wiggle(apples_13_m2[12]))
        self.wait()
    
    #choosing method 2
        tex_method_2.add_background_rectangle()
        m_1 = VGroup(rect_1, tex_method_1, apples_13_m1, count_3_m1, cut_lines, girl_1, girl_2, boy_1, boy_2, frac, apples_13_m1_12)
        m_2 = VGroup(rect_2, tex_method_2, apples_13_m2, surrect_13_m2, remainder_13_m2)
        self.play(
            ShowPassingFlash(rect_2.copy().set_stroke(RED, 9), time_width=0.2),
            Wiggle(tex_method_2),
            run_time = 2)
        self.wait()
        self.play(
            m_1.animate.scale(1/10000, about_point = rect_1.get_edge_center(LEFT)).set_color(BLACK).set_opacity(0),
            m_2.animate.scale(2.4, about_point = rect_2.get_edge_center(RIGHT)).set_opacity(0),
            FadeOut(div_13_4))
        self.wait()
    
    #numberline
        nl_13 = NumberLine(
            x_range=[0, 15, 1],
            length=13.5,
            include_tip=True)
        nl_13.shift(2*DOWN)
        numbers = VGroup(*[MathTex(f'{i}') for i in range(15)])
        for i in range(15):
            numbers[i].next_to(nl_13.n2p(i), DOWN, buff=0.4)

        self.play(Write(div_13_4))
        self.wait()
        self.play(Write(nl_13))
        self.wait()
        self.play(AnimationGroup(*[Write(n) for n in numbers], lag_ratio=0.1), run_time = 2)
        apples_13_nl = VGroup(*[apple.copy().scale(1.3).next_to(nl_13.n2p(i+1), UP) for i in range(13)])
        self.play(
            AnimationGroup(*[FadeIn(apple) for apple in apples_13_nl], lag_ratio=0.05))
        self.wait()
        self.play(
            AnimationGroup(*[Indicate(apple) for apple in apples_13_nl], lag_ratio=0.05))
        self.wait()
        surrec_13_nl = VGroup(
            SurroundingRectangle(apples_13_nl[0:4]).add(Tex(group, '$1$').set_color(RED).next_to(apples_13_nl[0:4], UP, buff=0.25)),
            SurroundingRectangle(apples_13_nl[4:8]).add(Tex(group, '$2$').set_color(BLUE).next_to(apples_13_nl[4:8], UP, buff=0.25)),
            SurroundingRectangle(apples_13_nl[8:12]).add(Tex(group, '$3$').set_color(YELLOW).next_to(apples_13_nl[8:12], UP, buff=0.25))) 
        self.play(
            AnimationGroup(
                *[AnimationGroup(
                    apples_13_nl[i].animate.set_color(RED),
                    Indicate(numbers[i+1])) for i in range(4)],
                Write(surrec_13_nl[0]),
                lag_ratio=0.25))
        self.wait()
        self.play(
            AnimationGroup(
                *[AnimationGroup(
                    apples_13_nl[i].animate.set_color(BLUE),
                    Indicate(numbers[i+1])) for i in range(4, 8)],
                Write(surrec_13_nl[1]),
                lag_ratio=0.25))
        self.wait()
        self.play(
            AnimationGroup(
                *[AnimationGroup(
                    apples_13_nl[i].animate.set_color(YELLOW),
                    Indicate(numbers[i+1])) for i in range(8, 12)],
                Write(surrec_13_nl[2]),
                lag_ratio=0.25))
        self.wait()
        remainder_nl_13 = MathTex('1').next_to(apples_13_nl[12], UP)
        self.play(Wiggle(apples_13_nl[12]), Indicate(numbers[13]), Write(remainder_nl_13))
        surrnl_13_quotient = SurroundingRectangle(surrec_13_nl[2][1][1], BLUE, buff=0.2, corner_radius=0.25)
        surrnl_13_quotient.set_fill(BLACK, 0.75)
        surrec_13_nl[2][1].set_z_index(1)
        quotient_tex.move_to(1.5*UP)
        nl_13_quotient_arrow = Arrow(surrnl_13_quotient.get_edge_center(UP), quotient_tex.get_edge_center(DOWN))
        self.play(AnimationGroup(
            Create(surrnl_13_quotient),
            Create(nl_13_quotient_arrow),
            Write(quotient_tex),
            lag_ratio=0.05), run_time = 2)
        surrnl_13_remainder = SurroundingRectangle(VGroup(apples_13_nl[12], remainder_nl_13), BLUE, corner_radius=0.25)
        remainder_tex.next_to(quotient_tex, RIGHT, buff=2.5)
        nl_13_remainder_arrow = Arrow(surrnl_13_remainder.get_edge_center(UP), remainder_tex.get_edge_center(DOWN))
        self.wait()
        self.play(AnimationGroup(
            Create(surrnl_13_remainder),
            Create(nl_13_remainder_arrow),
            Write(remainder_tex),
            lag_ratio=0.05), run_time = 2)
        self.wait(2)
        self.play(AnimationGroup(
            FadeOut(surrnl_13_remainder, surrnl_13_quotient),
            FadeOut(nl_13_remainder_arrow, nl_13_quotient_arrow),
            FadeOut(remainder_tex, quotient_tex),
            lag_ratio=0.25), run_time = 2)
        self.wait()
        self.play(
            numbers[1:5].animate.set_color(RED),
            numbers[5:9].animate.set_color(BLUE),
            numbers[9:13].animate.set_color(YELLOW),
            numbers[13].animate.set_color(GREEN),
            FadeOut(apples_13_nl, shift=DOWN),
            FadeOut(surrec_13_nl, remainder_nl_13))
        self.wait()
        parts = VGroup(
            Segment(nl_13.n2p(0), nl_13.n2p(13), stroke_width = 6),
            Segment(nl_13.n2p(0), nl_13.n2p(4), stroke_width = 6),
            Segment(nl_13.n2p(4), nl_13.n2p(8), stroke_width = 6),
            Segment(nl_13.n2p(8), nl_13.n2p(12), stroke_width = 6),
            Segment(nl_13.n2p(12), nl_13.n2p(13), stroke_width = 6))
        self.play(FadeIn(parts[0]))
        self.wait()
        self.play(parts[0].animate(rate_func = rate_functions.there_and_back).shift(0.25*UP))
        self.play(FadeIn(parts[1:]))
        self.remove(parts[0])
        self.play(AnimationGroup(
            parts[1].animate.set_color(RED),
            parts[2].animate.set_color(BLUE),
            parts[3].animate.set_color(YELLOW),
            parts[4].animate.set_color(GREEN)))
        self.wait()
        self.play(FadeIn(quotient_tex.move_to(ORIGIN)))
        self.play(
            AnimationGroup(*[m.animate(rate_func = rate_functions.there_and_back).shift(0.25*UP) for m in parts[1:4]], lag_ratio=0.1),
            run_time = 2.5)
        self.play(FadeOut(quotient_tex))
        self.wait()
        self.play(FadeIn(remainder_tex.move_to(ORIGIN)))
        self.play(parts[4].animate(rate_func = rate_functions.there_and_back).shift(0.25*UP), run_time = 1.5)
        self.wait()
        self.play(FadeOut(remainder_tex))
        self.play(FadeOut(div_13_4, nl_13, parts, numbers))
        self.wait()
    
    #27 : 5 
        self.play
        div_27_5 = MathTex('27:5')
        div_27_5.scale(3)
        div_13_4.to_corner(UP, buff=0.5)
        self.play(Write(div_27_5))
        self.wait()
        self.play(div_27_5.animate.to_corner(UP, buff=0.5).scale(0.5))
        self.wait()
        nl_27 = NumberLine(
            x_range=[0, 29, 1],
            length=13.5,
            include_tip=True)
        nl_13.shift(2*DOWN)
        numbers_27 = VGroup(*[MathTex(f'{i}').scale(0.7) for i in range(29)])
        for i in range(29):
            numbers_27[i].next_to(nl_27.n2p(i), DOWN, buff=0.4)
        parts_27 = VGroup(
            Segment(nl_27.n2p(0), nl_27.n2p(27), stroke_width = 6),
            Segment(nl_27.n2p(0), nl_27.n2p(5), stroke_width = 6),
            Segment(nl_27.n2p(5), nl_27.n2p(10), stroke_width = 6),
            Segment(nl_27.n2p(10), nl_27.n2p(15), stroke_width = 6),
            Segment(nl_27.n2p(15), nl_27.n2p(20), stroke_width = 6),
            Segment(nl_27.n2p(20), nl_27.n2p(25), stroke_width = 6),
            Segment(nl_27.n2p(25), nl_27.n2p(27), stroke_width = 6))
        self.play(Write(nl_27))
        self.play(AnimationGroup(*[Write(n) for n in numbers_27], lag_ratio=0.1), run_time = 2)
        self.wait()
        self.play(Create(parts_27[0]))
        scissors = VGroup(
            DScissors(nl_27.n2p(5)),
            DScissors(nl_27.n2p(10)),
            DScissors(nl_27.n2p(15)),
            DScissors(nl_27.n2p(20)),
            DScissors(nl_27.n2p(25)))
        self.play(AnimationGroup(
            *[CutIn(s) for s in scissors], lag_ratio=0.1
        ))
        self.add(scissors, parts_27[1:])
        self.remove(parts_27[0])
        self.play(AnimationGroup(
            *[CutOut(s) for s in scissors], lag_ratio=0.1
        ))
        self.remove(scissors)
        self.wait()
        self.play(
            parts_27[1].animate.set_color(RED),
            parts_27[2].animate.set_color(BLUE),
            parts_27[3].animate.set_color(YELLOW),
            parts_27[4].animate.set_color(LIGHT_PINK),
            parts_27[5].animate.set_color(GREEN))
        quotient_c = VGroup(*[MathTex(f'{i}').scale(0.7) for i in range(1, 6)])
        remainder_c = MathTex('2').scale(0.7)
        self.play(
            FadeIn(quotient_tex.move_to(2*DOWN)),
            AnimationGroup(*[p.animate(rate_func = rate_functions.there_and_back).shift(0.25*UP) for p in parts_27[1:-1]], lag_ratio=0.15))
        self.wait()
        self.play(
            FadeIn(remainder_tex.next_to(quotient_tex, DOWN, aligned_edge=LEFT)),
            parts_27[-1].animate(rate_func = rate_functions.there_and_back).shift(0.25*UP))
        self.wait()
        quotient_c.next_to(quotient_tex)
        remainder_c.next_to(remainder_tex)
        self.play(ReplacementTransform(parts_27[1].copy(), quotient_c[0]))
        self.play(
                ReplacementTransform(parts_27[2].copy(), quotient_c[1]),
                quotient_c[0].animate.set_opacity(0)),
        self.play(
                ReplacementTransform(parts_27[3].copy(), quotient_c[2]),
                quotient_c[1].animate.set_opacity(0)),
        self.play(
                ReplacementTransform(parts_27[4].copy(), quotient_c[3]),
                quotient_c[2].animate.set_opacity(0))
        self.play(
                ReplacementTransform(parts_27[5].copy(), quotient_c[4]),
                quotient_c[3].animate.set_opacity(0))
        self.wait()
        self.play(ReplacementTransform(parts_27[6].copy(), remainder_c))
        self.wait(2)
