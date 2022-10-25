from manim import Scene, Tex, Write, GrowFromEdge, AnimationGroup, FadeIn, Circumscribe, VGroup, MathTex, Brace, FadeOut, GrowFromCenter
from manim import LEFT, DOWN, UP, YELLOW, ORANGE, WHITE, ORIGIN, RIGHT, GREEN, UL, UR
from aramanim import CutIn, CutOut, Segment
from objects import DScissors, Checkmark
from qarakusiscene import TaskNumberBox
from .text import *

UNIT = .3

class Problem12189(Scene):
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_string)
        self.play(FadeIn(task_number))
        self.wait()

        condition1 = Tex(*condition1_string).to_edge(UL).shift(DOWN*.6)
        condition1[0].set_color(ORANGE)
        self.play(Write(condition1))
        condition2 = Tex(*condition2_string).next_to(condition1, DOWN, aligned_edge=LEFT, buff=.4)
        condition2[0].set_color(ORANGE)
        self.play(Write(condition2))

        armen_label = Tex(armen_string).to_edge(LEFT, buff=0.6).shift(DOWN*.5)
        armen_label.set_color_by_gradient("#FF9673", "#E0B851")
        armen_one_part = self.get_part(9, color=YELLOW).next_to(armen_label, buff=1)
        self.play(Write(armen_label))
        self.play(GrowFromEdge(armen_one_part, LEFT))
        self.wait()

        vazgen_label = Tex(vazgen_string).next_to(armen_label, DOWN, buff=2).align_to(armen_label, RIGHT)
        vazgen_label.set_color_by_gradient("#CFC748", "#7FC381")
        vazgen_one_part = armen_one_part.copy()
        self.play(Write(vazgen_label))
        self.play(vazgen_one_part.animate.next_to(vazgen_label, buff=1))
        self.wait()
        vazgen_segment_13 = self.get_part(13, color=GREEN, label=13).next_to(vazgen_one_part, buff=0)
        vazgen_segment_13_label = vazgen_segment_13.update_label_pos()
        self.play(
            GrowFromEdge(vazgen_segment_13, LEFT),
            Write(vazgen_segment_13_label)
        )
        self.wait()
        checkmark1 = Checkmark().scale(.3).next_to(condition1)
        self.play(FadeIn(checkmark1))
        self.wait()

        segment_5 = self.get_part(5, color=ORANGE, label=5).set_opacity(.5).next_to(vazgen_segment_13, buff=0)
        segment_5_label = segment_5.update_label_pos().set_opacity(.5)
        self.play(
            GrowFromEdge(segment_5, LEFT),
            Write(segment_5_label)
        )
        self.wait()

        x3_one_part = [armen_one_part.copy() for _ in range(3)]
        x3_one_part_animation = AnimationGroup(*[x3_one_part[i].animate.shift(DOWN).shift(RIGHT*i*2.7) for i in range(3)], lag_ratio=.8)
        self.play(x3_one_part_animation)
        self.wait()

        self.play(Circumscribe(segment_5, fade_out=True))
        self.wait()
        checkmark2 = Checkmark().scale(.3).next_to(condition2)
        self.play(FadeIn(checkmark2))
        self.wait()

        scissors1 = DScissors(cut_point=x3_one_part[0].right_edge.get_center())
        scissors2 = DScissors(cut_point=vazgen_one_part.right_edge.get_center())
        self.play(
            CutIn(scissors1),
            CutIn(scissors2),
            FadeOut(checkmark1, checkmark2, condition1, condition2)
        )
        self.wait()
        self.play(
            VGroup(
                x3_one_part[1],
                x3_one_part[2],
                vazgen_segment_13,
                vazgen_segment_13_label,
                segment_5,
                segment_5_label
            ).animate.shift(RIGHT),
            CutOut(scissors1),
            CutOut(scissors2)
        )
        self.wait()

        self.play(Circumscribe(VGroup(x3_one_part[1], x3_one_part[2]), fade_out=True))
        x2_one_part_value_brace = Brace(VGroup(x3_one_part[1], x3_one_part[2]), UP)
        x2_one_part_value_brace_tex = x2_one_part_value_brace.get_tex("18")
        x2_one_part_value = MathTex("13+5=18").to_edge(UL, buff=1.1).shift(DOWN*.3)
        self.play(
            Write(x2_one_part_value),
            run_time=2
        )
        self.wait()
        self.play(
            GrowFromCenter(x2_one_part_value_brace),
            Write(x2_one_part_value_brace_tex)
        )
        self.wait()
        one_part_value = MathTex("18:2=9").next_to(x2_one_part_value, DOWN, buff=.7, aligned_edge=LEFT)
        self.play(Write(one_part_value), run_time=2)
        one_part_label = MathTex("9").align_to(one_part_value, UR)
        one_part_label_copy = one_part_label.copy()
        self.play(VGroup(x2_one_part_value_brace_tex, x2_one_part_value_brace).animate.shift(UP*.7))
        self.play(
            one_part_label.animate.next_to(x3_one_part[1], UP),
            one_part_label_copy.animate.next_to(x3_one_part[2], UP)
        )
        self.wait()

        armen_one_part.set_label(MathTex("9"))
        armen_one_part_label = armen_one_part.update_label_pos()
        vazgen_one_part.set_label(MathTex("9"))
        vazgen_one_part_label = vazgen_one_part.update_label_pos()
        self.play(
            FadeIn(
                armen_one_part_label,
                vazgen_one_part_label
            )
        )
        self.wait()
        self.play(
            VGroup(
                vazgen_segment_13,
                vazgen_segment_13_label
            ).animate.shift(LEFT),
            FadeOut(
                segment_5,
                segment_5_label,
                *[one_part for one_part in x3_one_part],
                one_part_label,
                one_part_label_copy,
                x2_one_part_value_brace_tex, x2_one_part_value_brace
            )
        )
        self.wait()
        vazgen_mushrooms = MathTex("9+13=22").next_to(x2_one_part_value, buff=2)
        self.play(Write(vazgen_mushrooms), run_time=2)
        vazgen_brace = Brace(VGroup(vazgen_one_part, vazgen_segment_13), UP, buff=.4)
        vazgen_brace_label = MathTex("22").align_to(vazgen_mushrooms, UR)
        self.play(
            GrowFromCenter(vazgen_brace),
            vazgen_brace_label.animate.next_to(vazgen_brace, UP)
        )
        self.wait()

        together_value = MathTex("22+9=31").next_to(vazgen_mushrooms, DOWN, buff=.7, aligned_edge=LEFT)
        self.play(Write(together_value), run_time=2)
        together_brace = Brace(VGroup(armen_one_part, vazgen_one_part), RIGHT, buff=4.5)
        together_brace_label = MathTex("31").align_to(together_value, UR)
        self.play(
            GrowFromCenter(together_brace),
            together_brace_label.animate.next_to(together_brace)
        )

        self.wait(2)

    def get_part(self, value, label = None, color = WHITE):
        seg = Segment(
            ORIGIN,
            UNIT * value * RIGHT,
            label,
            stroke_width = 6,
            color = color
        )
        return seg
