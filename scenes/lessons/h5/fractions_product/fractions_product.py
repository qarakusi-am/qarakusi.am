from qarakusiscene import QarakusiScene
from . import text

from manim import UP, DOWN, UL, DR, LEFT, RIGHT
from manim import FadeOut, Write
from manim import VGroup, Line, MathTex, Arrow, Group
from manim import YELLOW, ORANGE, BLUE_C, WHITE, RED


class FractionsProduct(QarakusiScene):
    """Հ5 – կոտորակների արտադրյալը"""
    def construct(self):
        condition_point = [-1.5, 3, 0]
        MathTex.set_default(font_size=60)

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).next_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_1_0 = condition_1[0].copy()
        arrow_1 = Arrow(condition_1[0].get_critical_point(LEFT), [-3.8, 0.7, 0], color=ORANGE)
        self.play(Write(arrow_1))
        self.play(condition_1_0.animate(run_time=2).set_color(ORANGE).shift(3 * DOWN + 5.5 * LEFT))
        condition_2 = MathTex(*text.CONDITION_2, color=ORANGE).next_to(condition_1_0)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #

        # -------------------------- Point 4 ------------------------------- #
        condition_1_2 = condition_1[2].copy()
        arrow_2 = Arrow(condition_1[2].get_critical_point(RIGHT), [3.8, 0.7, 0], color=BLUE_C).set_z_index(-1)
        self.play(Write(arrow_2))
        self.play(condition_1_2.animate(run_time=2).set_color(BLUE_C).shift(3 * DOWN))
        condition_3 = MathTex(*text.CONDITION_3, color=BLUE_C).next_to(condition_1_2)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        equal = condition_2[1].copy().next_to(condition_1).set_color(WHITE)
        self.play(Write(equal))
        cdot = condition_1[1].copy().next_to(equal).shift(0.8 * RIGHT)
        self.play(condition_2[2].animate(run_time=2).next_to(equal),
                  FadeOut(Group(condition_2[:2], condition_1_0, arrow_1)),
                  condition_3[1].animate(run_time=2.2).next_to(cdot),
                  FadeOut(Group(condition_1_2, condition_3[0], arrow_2)))
        self.play(Write(cdot))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        condition_4 = MathTex(text.CONDITION_4).to_edge().shift(1 * UP)
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        solution_group_1 = VGroup(condition_2[2], cdot, condition_3[1])
        self.play(solution_group_1.animate(run_time=2).next_to(condition_4))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_5 = MathTex(*text.CONDITION_5).next_to(solution_group_1)
        self.play(Write(condition_5[0]))
        self.wait()
        self.play(Write(condition_5[1]))
        self.wait()
        self.play(Write(condition_5[2]))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).to_edge().shift(UP)
        self.play(VGroup(condition_4, solution_group_1, condition_5).animate(run_time=2).shift(3.6 * DOWN))
        self.play(Write(condition_6))

        # -------------------------- Point 10 ------------------------------- #
        option_2 = solution_group_1.copy() + condition_5[0].copy()
        self.play(option_2.animate(run_time=2).next_to(condition_6))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        nums = MathTex(*text.NUMS).scale(0.6).set_color(YELLOW)
        line_1 = Line(option_2[3][1:3].get_critical_point(UL),
                      option_2[3][1:3].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        line_2 = Line(option_2[3][10:].get_critical_point(UL),
                      option_2[3][10:].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        self.play(Write(VGroup(line_1, line_2)))
        self.play(Write(VGroup(nums[2].next_to(option_2[3][1:3]).shift(0.2 * UP + 1.05 * LEFT),
                               nums[0].next_to(option_2[3][10:]).shift(0.2 * UP + 1.05 * LEFT))))
        self.wait()

        line_3 = Line(option_2[3][4:6].get_critical_point(UL),
                      option_2[3][4:6].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        line_4 = Line(option_2[3][7:9].get_critical_point(UL),
                      option_2[3][7:9].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        self.play(Write(VGroup(line_3, line_4)))
        self.play(Write(VGroup(nums[3].next_to(option_2[3][4:6]).shift(0.2 * UP + 1.05 * LEFT),
                               nums[1].next_to(option_2[3][7:9]).shift(0.2 * UP + 1.05 * LEFT))))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        condition_7 = MathTex(*text.CONDITION_7).next_to(option_2)
        self.play(Write(condition_7[0]))
        self.wait()
        self.play(Write(condition_7[1]))
        self.wait()
        self.play(Write(condition_7[2]))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        option_2_all = VGroup(condition_6, option_2, condition_7, line_1, line_2, line_3, line_4, nums)
        self.play(option_2_all.animate(run_time=1.5).shift(1.8 * DOWN))
        self.wait()

        condition_8 = MathTex(text.CONDITION_8).to_edge().shift(UP)
        condition_8_1 = solution_group_1.copy().next_to(condition_8)
        self.play(Write(condition_8))
        self.play(Write(condition_8_1))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        nums_1 = nums.copy()
        line_5 = Line(condition_8_1[0][:2].get_critical_point(UL),
                      condition_8_1[0][:2].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        line_6 = Line(condition_8_1[2][3:].get_critical_point(UL),
                      condition_8_1[2][3:].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        self.play(Write(VGroup(line_5, line_6)))
        self.play(Write(VGroup(nums_1[2].next_to(condition_8_1[0][:2]).shift(0.2 * UP + 1.05 * LEFT),
                               nums_1[0].next_to(condition_8_1[2][3:]).shift(0.2 * UP + 1.05 * LEFT))))
        self.wait()

        line_7 = Line(condition_8_1[0][3:].get_critical_point(UL),
                      condition_8_1[0][3:].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        line_8 = Line(condition_8_1[2][:2].get_critical_point(UL),
                      condition_8_1[2][:2].get_critical_point(DR),
                      stroke_width=5,
                      color=RED)
        self.play(Write(VGroup(line_7, line_8)))
        self.play(Write(VGroup(nums_1[1].next_to(condition_8_1[0][3:]).shift(0.2 * UP + 1.05 * LEFT),
                               nums_1[3].next_to(condition_8_1[2][:2]).shift(0.2 * UP + 1.05 * LEFT))))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        condition_8_2 = condition_7.copy().next_to(condition_8_1)
        self.play(Write(condition_8_2[0]))
        self.wait()
        self.play(Write(condition_8_2[1]))
        self.wait()
        self.play(Write(condition_8_2[2]))
        self.wait(3)
