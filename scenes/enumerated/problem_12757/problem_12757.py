from manim import LEFT, UP, DOWN, RIGHT, ORIGIN
from manim import FadeOut, Write
from manim import AnimationGroup, Group, VGroup, ReplacementTransform, Wiggle, Dot, Restore
from manim import Line, Rectangle, Arrow, MathTex, SurroundingRectangle
from manim import UL, DR, UR, DL
from manim import RED, GREEN, ORANGE, YELLOW

from qarakusiscene import QarakusiScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text


class Problem12757(QarakusiScene, FormulaModificationsScene):
    """Ապացուցել, որ թվերը բաղադրյալ են"""
    def construct(self):
        screen_center = [0, 0.9, 0]
        condition_point = [-5.25, 3.4, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)
        MathTex.set_default(font_size=57)
        self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).next_to(condition_point)
        self.play(Write(condition_1), run_time=3)
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_2 = MathTex(*text.CONDITION_2).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(screen_center)
        rectangle_1 = Rectangle(height=4.15, width=14, color=YELLOW).move_to(condition_2)
        self.play(Write(condition_2), run_time=2.5)
        self.play(Write(rectangle_1), run_time=1.5)
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_1_0_copy = condition_1[0].copy()
        self.play(rectangle_1.animate.shift(2.3 * DOWN), condition_2.animate.shift(0.8 * UP))
        self.play(condition_1_0_copy.animate.move_to(rectangle_1).shift(1.2 * UP))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_1_0_copy_0 = condition_1_0_copy[:5].copy().next_to(condition_1_0_copy, DOWN)
        self.play(Write(condition_1_0_copy_0))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        solution_1_2 = MathTex(text.SOLUTION_1_2).move_to(condition_1_0_copy_0[:2]).shift(0.25 * LEFT)
        self.play(ReplacementTransform(condition_1_0_copy_0[:2], solution_1_2))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        solution_1_3 = MathTex(text.SOLUTION_1_3).move_to(condition_1_0_copy_0[2:]).shift(1.3 * RIGHT)
        self.play(ReplacementTransform(condition_1_0_copy_0[3:], solution_1_3))
        self.wait()

        # -------------------------- Point 7 -------------------------------
        self.play(VGroup(solution_1_2, solution_1_3, condition_1_0_copy_0).animate.shift(1.7 * LEFT))
        solution_1_4 = MathTex(text.SOLUTION_1_4).next_to(solution_1_3)
        self.play(Write(solution_1_4))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        solution_1_5 = MathTex(text.SOLUTION_1_5).next_to(solution_1_4, DOWN).shift(2.25 * LEFT)
        self.play(Write(solution_1_5))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        solution_1_6 = MathTex(text.SOLUTION_1_6).next_to(solution_1_5, DOWN).shift(0.2 * UP)
        self.play(Write(solution_1_6))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        up_y = condition_1_0_copy.get_critical_point(UP)[1]
        down_y = solution_1_6.get_critical_point(DOWN)[1]
        line_1 = Line([-5, up_y, 0], [5, down_y, 0], color=RED, stroke_width=7).scale(0.9).set_z_index(+1)
        line_2 = Line([-5, down_y, 0], [5, up_y, 0], color=RED, stroke_width=7).scale(0.9).set_z_index(+1)
        self.play(Write(VGroup(line_1, line_2)))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        self.play(FadeOut(Group(condition_1_0_copy_0,
                                solution_1_2,
                                solution_1_3,
                                solution_1_4,
                                solution_1_5,
                                solution_1_6,
                                line_1,
                                line_2)))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        self.play(condition_1_0_copy.animate.shift(3 * LEFT))
        solution_2_2 = MathTex(text.SOLUTION_2_2).next_to(condition_1_0_copy)
        self.play(Write(solution_2_2))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        solution_2_3 = MathTex(text.SOLUTION_2_3).next_to(solution_2_2, DOWN).shift(1.3 * DOWN + 0.3 * RIGHT)
        arrow_1 = Arrow(solution_2_3[0][0:4].get_critical_point(UP),
                        solution_2_2[0][1:3].get_critical_point(DOWN),
                        color=YELLOW,
                        max_tip_length_to_length_ratio=0.5,
                        max_stroke_width_to_length_ratio=10).scale(1.2)
        arrow_2 = Arrow(solution_2_3[0][-2:].get_critical_point(UP),
                        solution_2_2[0][-1].get_critical_point(DOWN),
                        color=YELLOW,
                        max_tip_length_to_length_ratio=0.5,
                        max_stroke_width_to_length_ratio=10).scale(1.3)
        arrow_3 = Arrow(solution_2_3[0][6:11].get_critical_point(UP),
                        solution_2_2[0][4:11].get_critical_point(DOWN),
                        color=YELLOW,
                        max_tip_length_to_length_ratio=0.7,
                        max_stroke_width_to_length_ratio=12).scale(1.5)

        self.play(Write(solution_2_3))
        self.play(Write(arrow_1), Write(arrow_2), Write(arrow_3))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        solution_2_4 = MathTex(text.SOLUTION_2_4).move_to(solution_2_3)
        self.play(ReplacementTransform(solution_2_3, solution_2_4), FadeOut(Group(arrow_1, arrow_2, arrow_3)))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        self.play(solution_2_2[0][8:11].animate.set_color(ORANGE))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        self.play(Group(condition_1_0_copy, solution_2_2, solution_2_4).animate.shift(2.1 * LEFT))
        solution_2_5 = MathTex(text.SOLUTION_2_5).next_to(solution_2_2)
        solution_2_5[0][8:11].set_color(ORANGE)
        self.play(Write(solution_2_5))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        solution_2_6 = MathTex(text.SOLUTION_2_6).next_to(condition_1_0_copy, DOWN, aligned_edge=LEFT)
        self.play(Write(solution_2_6))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        equal = MathTex(text.EQUAL).next_to(condition_1_0_copy)
        self.play(FadeOut(Group(solution_2_2, solution_2_4, solution_2_5)),
                  Write(equal),
                  solution_2_6.animate.next_to(condition_1_0_copy).shift(0.7 * RIGHT))
        self.play(Group(condition_1_0_copy, equal, solution_2_6).animate.shift(0.41 * UP))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        condition_3 = MathTex(*text.CONDITION_3).next_to(condition_1_0_copy, DOWN, aligned_edge=LEFT, buff=0.2)
        condition_3[4:].next_to(condition_3[:4], DOWN, buff=0.2, aligned_edge=RIGHT)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 20 ------------------------------- #
        condition_1_2_copy = condition_1[2].copy()
        self.play(condition_1_2_copy.animate.next_to(condition_3, DOWN, aligned_edge=LEFT, buff=0.2))
        self.wait()

        # -------------------------- Point 21 ------------------------------- #
        solution_3_2 = MathTex(text.SOLUTION_3_2).next_to(condition_1_2_copy)
        self.play(Write(solution_3_2))
        self.wait()

        # -------------------------- Point 22 ------------------------------- #
        solution_3_3 = MathTex(text.SOLUTION_3_3).next_to(solution_3_2)
        self.play(Write(solution_3_3))
        self.wait()

        # -------------------------- Point 23 ------------------------------- #
        solution_3_4 = MathTex(text.SOLUTION_3_4).move_to(solution_3_3[0][-3:]).shift(0.3 * RIGHT)
        self.play(ReplacementTransform(solution_3_3[0][-3:], solution_3_4))
        self.wait()

        # -------------------------- Point 24 ------------------------------- #
        solution_3_5 = MathTex(text.SOLUTION_3_5).next_to(condition_1_2_copy, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(solution_3_5))
        self.wait()

        # -------------------------- Point 25 ------------------------------- #
        self.play(FadeOut(Group(solution_3_2, solution_3_3, solution_3_4)),
                  solution_3_5.animate.next_to(condition_1_2_copy))
        self.wait()

        # -------------------------- Point 26 ------------------------------- #
        result = MathTex(*text.RESULT).next_to(condition_1_2_copy, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(result))
        self.wait(3)
