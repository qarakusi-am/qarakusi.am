from manim import LEFT, UP, DOWN, RIGHT, ORIGIN
from manim import FadeOut, Write
from manim import Group, VGroup, ReplacementTransform, AnimationGroup
from manim import Line, Rectangle, Arrow, MathTex, rate_functions
from manim import RED, ORANGE, YELLOW

from qarakusiscene import QarakusiScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text


class Problem12803(QarakusiScene, FormulaModificationsScene):
    """3^60 թիվը ներկայացնել հետևյալ հիմքի աստիճանների տեսքով․
        ա) 36
        բ) 315
        գ) 9
        դ) 27
    """
    def construct(self):
        screen_center = [-0.6, 1.3, 0]
        row_buff = 0.9
        self.add_task_number(text=text.TASK_NUMBER_STR)
        MathTex.set_default(font_size=text.default_font_size)
        # self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1)
        condition_1[:10].move_to(screen_center)
        condition_1[10].next_to(condition_1[:10], DOWN, aligned_edge=LEFT)
        self.play(Write(condition_1), run_time=3)
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        equal_1 = MathTex(text.EQUAL).next_to(condition_1[0]).shift(0.13 * DOWN)
        brackets_1 = MathTex(*text.BRACKETS_1).next_to(equal_1).shift(0.11 * UP)
        self.play(AnimationGroup(
            AnimationGroup(condition_1[4:9].animate(rate_func=rate_functions.linear).shift(2 * UP + RIGHT),
                           FadeOut(Group(condition_1[1], condition_1[-2:], condition_1[3]))),
                  Write(equal_1),
                  condition_1[2].animate(rate_func=rate_functions.linear).move_to(brackets_1).shift(0.2 * LEFT),
                  Write(brackets_1),
                  lag_ratio=0.3,
                  run_time=2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        solution_1_2 = MathTex(*text.SOLUTION_1_2).next_to(brackets_1)
        self.play(Write(solution_1_2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        self.play(condition_1[0][-2:].animate.set_color(ORANGE), solution_1_2[2][-2:].animate.set_color(ORANGE))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        hint_1 = MathTex(text.HINT_1).next_to(solution_1_2, DOWN, aligned_edge=RIGHT, buff=row_buff).shift(0.19 * LEFT)
        self.play(Write(hint_1))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        solution_1_3 = MathTex(*text.SOLUTION_1_3).next_to(hint_1, DOWN, aligned_edge=LEFT, buff=row_buff).shift(0.25 * RIGHT)
        self.play(Write(solution_1_3[0]))
        self.wait()
        self.play(Write(solution_1_3[1:]))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        self.fix_formula(brackets_1)
        self.play(FadeOut(Group(hint_1, solution_1_2, solution_1_3)),
                  ModifyFormula(brackets_1,
                                replace_items=[[1]],
                                replace_items_strs=[["{10}"]],
                                replace_items_colors=[[ORANGE]]))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_1_0_copy = condition_1[0].copy()
        self.play(condition_1_0_copy.animate.next_to(condition_1[0], DOWN, aligned_edge=LEFT, buff=row_buff))
        equal_2 = equal_1.copy().next_to(condition_1_0_copy).shift(0.13 * DOWN)
        self.play(Write(equal_2))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        brackets_2 = MathTex(*text.BRACKETS_2).next_to(equal_2).shift(0.11 * UP)
        brackets_2[-1].set_color(ORANGE)
        self.play(AnimationGroup(
            FadeOut(condition_1[5]),
            condition_1[4].animate(rate_func=rate_functions.linear).move_to(brackets_2).shift(0.2 * LEFT),
            lag_ratio=0.5,
            run_time=2))
        self.play(Write(brackets_2))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        hint_2 = MathTex(text.HINT_2).next_to(condition_1[4], DOWN, aligned_edge=RIGHT, buff=row_buff).shift(0.03 * LEFT)
        self.play(Write(hint_2))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        solution_2_3 = MathTex(text.SOLUTION_2_3).next_to(hint_2, DOWN).shift(0.6 * RIGHT)
        self.play(Write(solution_2_3))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        self.play(FadeOut(Group(hint_2, solution_2_3)))
        self.fix_formula(brackets_2)
        self.play(ModifyFormula(brackets_2, replace_items=[[1]], replace_items_strs=[["{4}"]]))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        condition_1_0_copy_1 = condition_1[0].copy()
        self.play(condition_1_0_copy_1.animate(run_time=2).next_to(condition_1[0], aligned_edge=DOWN).shift(6 * RIGHT))
        equal_3 = equal_1.copy().next_to(condition_1_0_copy_1).shift(0.13 * DOWN)
        self.play(Write(equal_3))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        self.play(AnimationGroup(
            FadeOut(condition_1[7]),
            condition_1[6].animate(
                rate_func=rate_functions.linear
            ).next_to(condition_1_0_copy_1, aligned_edge=DOWN, buff=1),
            lag_ratio=0.5,
            run_time=2))
        self.wait()
        solution_3_2 = MathTex(*text.SOLUTION_3_2).move_to(condition_1[6]).shift(0.2 * RIGHT)
        solution_3_2[-1].set_color(ORANGE)
        self.play(ReplacementTransform(condition_1[6], solution_3_2))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        solution_3_3 = MathTex(*text.SOLUTION_3_3).next_to(solution_3_2, DOWN, buff=row_buff).shift(0.28 * RIGHT)
        self.play(Write(solution_3_3))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        solution_3_4 = MathTex(*text.SOLUTION_3_4).next_to(solution_3_2)
        solution_3_4[-1].set_color(ORANGE)
        self.play(ReplacementTransform(solution_3_3[1], solution_3_4),
                  FadeOut(solution_3_3[0]))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        solution_3_5 = MathTex(text.SOLUTION_3_5).next_to(condition_1_0_copy_1, DOWN, aligned_edge=LEFT, buff=row_buff).shift(0.2 * RIGHT)
        self.play(Write(solution_3_5))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        solution_3_6 = MathTex(text.SOLUTION_3_6).next_to(solution_3_5, DOWN, aligned_edge=LEFT, buff=row_buff).shift(0.27 * RIGHT)
        self.play(Write(solution_3_6))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        self.play(FadeOut(Group(solution_3_5, solution_3_6[0])))
        self.fix_formula(solution_3_2)
        self.play(ModifyFormula(solution_3_2, replace_items=[[1]], replace_items_strs=[["{30}"]]),
                  FadeOut(solution_3_4))
        self.wait()

        # -------------------------- Point 20 ------------------------------- #
        solution_4_1 = MathTex(*text.SOLUTION_4_1).next_to(condition_1_0_copy_1, DOWN, aligned_edge=LEFT, buff=row_buff)
        solution_4_1[0][1:3].set_color(ORANGE)
        solution_4_1[1][-1].set_color(ORANGE)
        self.play(Write(solution_4_1), FadeOut(condition_1[-3]))
        self.wait()

        # -------------------------- Point 21 ------------------------------- #
        solution_4_2 = MathTex(*text.SOLUTION_4_2).move_to(solution_4_1[1]).shift(0.3 * RIGHT)
        solution_4_2[-1].set_color(ORANGE)
        self.play(ReplacementTransform(solution_4_1[1], solution_4_2))
        self.wait()

        # -------------------------- Point 22 ------------------------------- #
        solution_4_3 = MathTex(text.SOLUTION_4_3).next_to(solution_4_1, DOWN, aligned_edge=LEFT, buff=row_buff)
        self.play(Write(solution_4_3))
        self.wait()

        # -------------------------- Point 23 ------------------------------- #
        self.fix_formula(solution_4_2)
        self.play(ModifyFormula(solution_4_2, replace_items=[[1]], replace_items_strs=[["{20}"]]),
                  FadeOut(solution_4_3))
        self.wait()

        # -------------------------- Point 24 ------------------------------- #
        self.fix_formula(solution_4_2)
        self.play(ModifyFormula(solution_4_2, replace_items=[[0]],
                                replace_items_strs=[["27^"]],
                                new_formula_alignment=UP))
        self.wait(3)
