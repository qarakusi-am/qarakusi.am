from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeIn, FadeOut, Write
from manim import AnimationGroup, Group, VGroup, ReplacementTransform
from manim import Line, BraceBetweenPoints, Rectangle, Arrow, MathTex
from manim import UL, DR, PI, UR
from manim import RED, YELLOW

from qarakusiscene import QarakusiScene
from objects import SimpleSVGMobject
from . import text


class Problem12187(QarakusiScene):
    """Գտնել ամենափոքր բնական թիվը, որի թվանշանների գումարը հավասար է 23:"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        condition_1_0 = MathTex(text.CONDITION_1_0).move_to(screen_center).scale(1.9).shift(0.5 * UP)
        condition_1_1 = MathTex(text.CONDITION_1_1).move_to(condition_1_0).scale(1.9).shift(DOWN)
        self.play(AnimationGroup(Write(condition_1_0), Write(condition_1_1), lag_ratio=1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        # replace some text
        condition_1_1_final = MathTex(text.CONDITION_1_1_FINAL).scale(1.9).move_to(condition_point).shift(0.8 * RIGHT + 0.06 * DOWN)
        self.play(AnimationGroup(FadeOut(condition_1_0),
                                 ReplacementTransform(condition_1_1, condition_1_1_final, run_time=2),
                                 lag_ratio=0.7))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_2 = MathTex(text.CONDITION_2).move_to(screen_center).scale(1.8)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).move_to(screen_center).scale(1.8)
        self.play(AnimationGroup(FadeOut(condition_2), Write(condition_3), lag_ratio=1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        condition_4 = MathTex(text.CONDITION_4).move_to(condition_3).scale(1.8).shift(DOWN)
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        line = Line(condition_3[0].get_critical_point(UL), condition_3[0].get_critical_point(DR), color=RED)
        self.play(Write(line))
        self.wait()
        self.play(FadeOut(condition_3), FadeOut(condition_4), FadeOut(line))

        # -------------------------- Point 7 ------------------------------- #
        condition_5 = MathTex(text.CONDITION_5).move_to(screen_center).scale(1.8)
        self.play(Write(condition_5))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).move_to(condition_5).scale(1.8).shift(DOWN)
        self.play(Write(condition_6))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        line_1 = Line(condition_5[0].get_critical_point(UL), condition_5[0].get_critical_point(DR), color=RED)
        self.play(Write(line_1))
        self.wait()
        self.play(FadeOut(condition_5), FadeOut(condition_6), FadeOut(line_1))

        # -------------------------- Point 10 ------------------------------- #
        condition_7 = MathTex(text.CONDITION_7).move_to(screen_center).scale(1.8)
        self.play(Write(condition_7))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        condition_8 = MathTex(text.CONDITION_8).move_to(condition_5).scale(1.8).shift(DOWN)
        self.play(Write(condition_8))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        check_mark = SimpleSVGMobject('check').next_to(condition_7).scale(0.4).shift(0.5 * LEFT + 0.15 * UP)
        self.play(FadeIn(check_mark))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        rectangle_1 = Rectangle(height=0.8, width=0.6)
        rectangle_2 = rectangle_1.copy().next_to(rectangle_1).shift(0.5 * RIGHT)
        rectangle_3 = rectangle_1.copy().next_to(rectangle_2).shift(0.5 * RIGHT)
        rectangle_group = VGroup(rectangle_1, rectangle_2, rectangle_3).move_to(screen_center).shift(0.68 * LEFT)

        self.play(FadeOut(condition_8))
        self.play(ReplacementTransform(Group(condition_7, check_mark), rectangle_group))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        plus = MathTex(text.PLUS).next_to(rectangle_1).scale(1.8)
        plus_copy = plus.copy().next_to(rectangle_2).shift(0.1 * LEFT)
        equal_23 = MathTex(text.EQUAL_23).next_to(rectangle_3).scale(1.8).shift(0.4 * RIGHT)
        self.play(AnimationGroup(Write(plus), Write(plus_copy), Write(equal_23), lag_ratio=1))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        small_arrow = Arrow(max_stroke_width_to_length_ratio=10).rotate(0.5 * PI).scale(0.6)
        small_arrow.move_to(rectangle_group).shift(1.35 * LEFT + DOWN)
        condition_9 = MathTex(text.CONDITION_9).move_to(rectangle_group).scale(1.8).shift(1.8 * DOWN + 0.7 * RIGHT)
        self.play(AnimationGroup(Write(small_arrow), Write(condition_9), lag_ratio=1))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        up_brace_1 = BraceBetweenPoints(rectangle_2.get_critical_point(UL),
                                        rectangle_3.get_critical_point(UR), direction=UP).shift(0.1 * DOWN)
        condition_10 = MathTex(text.CONDITION_10).move_to(up_brace_1).scale(1.8).shift(0.6 * UP)
        self.play(AnimationGroup(Write(up_brace_1), Write(condition_10), lag_ratio=0.5))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        nine = MathTex(text.NINE).move_to(rectangle_2).scale(1.8).set_color(YELLOW)
        nine_copy = nine.copy().move_to(rectangle_3)
        self.play(AnimationGroup(FadeOut(Group(small_arrow, up_brace_1, condition_10, condition_9)),
                                 Write(VGroup(nine, nine_copy)), lag_ratio=0.5))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        solution_part_1 = MathTex(text.SOLUTION_PART_1).move_to(rectangle_group).scale(1.8).shift(UP)
        self.play(Write(solution_part_1))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        five = solution_part_1[0][7]
        self.play(five.animate.move_to(rectangle_1).set_color(YELLOW), FadeOut(solution_part_1[0][:7]))
        self.wait()

        # -------------------------- Point 20 ------------------------------- #
        self.play(FadeOut(Group(rectangle_group, plus, plus_copy, equal_23)))
        self.play(nine.animate.shift(0.6 * RIGHT),
                  five.animate.shift(1.5 * RIGHT),
                  nine_copy.animate.shift(0.3 * LEFT))
        self.wait()

        # -------------------------- Point 21 ------------------------------- #
        num_group = Group(five, nine, nine_copy)
        self.play(num_group.animate.scale(1.5))
        self.wait()

        self.wait(3)
