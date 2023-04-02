from qarakusiscene import QarakusiScene
from . import text

from manim import UP, DOWN, UL, DR
from manim import FadeOut, Write
from manim import VGroup, Line, MathTex
from manim import YELLOW


class FractionsProduct(QarakusiScene):
    """Հ5 – կոտորակների արտադրյալը"""
    def construct(self):
        condition_point = [-2, 3, 0]
        MathTex.set_default(font_size=60)
        self.add_task_number(text=text.TASK_NUMBER_STR)
        # self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).next_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_1_0 = condition_1[0].copy()
        self.play(condition_1_0.animate.next_to(condition_1[0], DOWN))
        condition_2 = MathTex(*text.CONDITION_2).next_to(condition_1_0)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        self.play(condition_2[1:].animate.next_to(condition_1), FadeOut(condition_2[0]), FadeOut(condition_1_0))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_1_2 = condition_1[2].copy()
        self.play(condition_1_2.animate.next_to(condition_1[0], DOWN))
        condition_3 = MathTex(*text.CONDITION_3).next_to(condition_1_2)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        cdot = condition_1[1].copy().next_to(condition_2[2])
        self.play(condition_3[1].animate.next_to(cdot), FadeOut(condition_1_2), FadeOut(condition_3[0]))
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
        self.play(option_2.animate(run_time=1.5).next_to(condition_6))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        line_1 = Line(option_2[3][1:3].get_critical_point(UL),
                      option_2[3][1:3].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        line_2 = Line(option_2[3][10:].get_critical_point(UL),
                      option_2[3][10:].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        self.play(Write(VGroup(line_1, line_2)))
        self.wait()

        line_3 = Line(option_2[3][4:6].get_critical_point(UL),
                      option_2[3][4:6].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        line_4 = Line(option_2[3][7:9].get_critical_point(UL),
                      option_2[3][7:9].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        self.play(Write(VGroup(line_3, line_4)))
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
        option_2_all = VGroup(condition_6, option_2, condition_7, line_1, line_2, line_3, line_4)
        self.play(option_2_all.animate(run_time=1.5).shift(1.8 * DOWN))
        self.wait()

        condition_8 = MathTex(text.CONDITION_8).to_edge().shift(UP)
        condition_8_1 = solution_group_1.copy().next_to(condition_8)
        self.play(Write(condition_8))
        self.play(Write(condition_8_1))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        line_5 = Line(condition_8_1[0][:2].get_critical_point(UL),
                      condition_8_1[0][:2].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        line_6 = Line(condition_8_1[2][3:].get_critical_point(UL),
                      condition_8_1[2][3:].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        self.play(Write(VGroup(line_5, line_6)))
        self.wait()

        line_7 = Line(condition_8_1[0][3:].get_critical_point(UL),
                      condition_8_1[0][3:].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        line_8 = Line(condition_8_1[2][:2].get_critical_point(UL),
                      condition_8_1[2][:2].get_critical_point(DR),
                      stroke_width=5,
                      color=YELLOW)
        self.play(Write(VGroup(line_7, line_8)))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        condition_8_2 = condition_7.copy().next_to(condition_8_1)
        self.play(Write(condition_8_2[0]))
        self.wait()
        self.play(Write(condition_8_2[1]))
        self.wait()
        self.play(Write(condition_8_2[2]))
        self.wait(3)
