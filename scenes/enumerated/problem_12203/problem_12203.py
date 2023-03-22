from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeOut, Write
from manim import AnimationGroup, Group, VGroup, ReplacementTransform, Wiggle
from manim import Line, Rectangle, Arrow, MathTex
from manim import UL, DR, UR, DL
from manim import RED, GREEN, ORANGE

from movement_problems import CustomMovementScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text


class Problem12203(CustomMovementScene):
    """Դրոնն աշխատեց 3 օր, օրական 6 ժամ, իսկ այնուհետև 2 օր, օրական 7 ժամ և ընդհանուր մշակեց 24 հա դաշտը։
    Պարզել, թե քանի՞ ար դաշտ է մշակում դրոնը մեկ ժամում։"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        # condition_1_0 = MathTex(text.CONDITION_1_0).move_to(condition_point).scale(1.8)
        # condition_1_1 = MathTex(text.CONDITION_1_1).move_to(condition_1_0).scale(1.8).shift(DOWN)
        # self.play(AnimationGroup(Write(condition_1_0), Write(condition_1_1), lag_ratio=1))

        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        # condition_2 = MathTex(*text.CONDITION_2).move_to(screen_center).scale(2.5).shift(0.8 * DOWN)
        # self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        # line_1 = Line(condition_2[2].get_critical_point(UL), condition_2[2].get_critical_point(DR), color=RED, stroke_width=7)
        # line_2 = Line(condition_2[2].get_critical_point(UR), condition_2[2].get_critical_point(DL), color=RED, stroke_width=7)
        # cross = VGroup(line_1, line_2)
        # self.play(Wiggle(condition_2[2], scale_value=1.7))
        # self.wait()
        # self.play(Write(cross))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        question_mark = MathTex(text.QUESTION_MARK).move_to(condition_2).scale(3).shift(1.2 * UP)
        self.play(Write(question_mark))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        self.play(FadeOut(Group(question_mark, cross)))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        condition_2_copy_1 = condition_2.copy().move_to(condition_2).shift(4 * LEFT + 1.8 * UP)
        condition_2_copy_2 = condition_2.copy().move_to(condition_2_copy_1).shift(1.2 * DOWN)
        condition_2_copy_3 = condition_2.copy().move_to(condition_2_copy_2).shift(1.2 * DOWN)
        condition_2_copy_4 = condition_2.copy().move_to(condition_2_copy_3).shift(1.2 * DOWN)
        condition_2_group = VGroup(condition_2_copy_1, condition_2_copy_2, condition_2_copy_3, condition_2_copy_4).scale(0.8)
        self.play(ReplacementTransform(condition_2, condition_2_group))
        self.wait()

        # -------------------------- Point 7 -------------------------------
        self.play(condition_2_copy_1[0].animate.set_color(RED),
                  condition_2_copy_2[1].animate.set_color(RED),
                  condition_2_copy_3[2].animate.set_color(RED),
                  condition_2_copy_4[3].animate.set_color(RED))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        self.fix_formula(condition_2_copy_1)
        self.fix_formula(condition_2_copy_2)
        self.fix_formula(condition_2_copy_3)
        self.fix_formula(condition_2_copy_4)
        self.play(ModifyFormula(condition_2_copy_1, remove_items=[0]))
        self.wait()
        self.play(ModifyFormula(condition_2_copy_2, remove_items=[1]))
        self.wait()
        self.play(ModifyFormula(condition_2_copy_3, remove_items=[2]))
        self.wait()
        self.play(ModifyFormula(condition_2_copy_4, remove_items=[3]))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        rectangle = Rectangle(height=3.8, width=0.7).move_to(condition_2_copy_1).shift(1.5 * DOWN + 0.82 * LEFT)
        self.play(Write(rectangle), condition_2_copy_1[0].animate.set_color(GREEN))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        self.play(FadeOut(rectangle))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        self.play(FadeOut(Group(condition_2_copy_2, condition_2_copy_3, condition_2_copy_4)))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        four = MathTex(text.FOUR).move_to(condition_2_copy_1).scale(1.8).shift(1.7 * LEFT).set_z_index(-1)
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        line_1 = Line(four.get_critical_point(UL), four.get_critical_point(DR), color=RED, stroke_width=7)
        line_2 = Line(four.get_critical_point(UR), four.get_critical_point(DL), color=RED, stroke_width=7)
        cross_1 = VGroup(line_1, line_2)
        self.play(Write(four), Write(cross_1))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        condition_4 = MathTex(text.CONDITION_4).move_to(screen_center).scale(1.8).shift(0.3 * RIGHT + 0.3 * DOWN)
        self.play(AnimationGroup(FadeOut(Group(cross_1, condition_2_copy_1, four)), Write(condition_4), lag_ratio=0.7))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        condition_4_copy_1 = MathTex(text.CONDITION_4_1).move_to([-5.5, 1, 0])
        condition_4_copy_2 = MathTex(text.CONDITION_4_2).move_to(condition_4_copy_1).shift(DOWN)
        condition_4_copy_3 = MathTex(text.CONDITION_4_3).move_to(condition_4_copy_2).shift(DOWN)
        condition_4_copy_4 = MathTex(text.CONDITION_4_4).move_to(condition_4_copy_3).shift(DOWN)
        condition_4_copy_5 = MathTex(text.CONDITION_4_5).copy().move_to(condition_4_copy_4).shift(DOWN)

        self.play(AnimationGroup(Write(condition_4_copy_1),
                                 Write(condition_4_copy_2),
                                 Write(condition_4_copy_3),
                                 Write(condition_4_copy_4),
                                 Write(condition_4_copy_5),
                                 lag_ratio=1))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        self.play(FadeOut(Group(condition_4_copy_1,
                                condition_4_copy_2,
                                condition_4_copy_3,
                                condition_4_copy_4,
                                condition_4_copy_5)))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        nums = MathTex(*text.NUMS, color=ORANGE).scale(0.9) #.next_to(condition_4, DOWN)
        for i in range(12):
            nums[i].next_to(condition_4[0][i], DOWN)
        self.play(Write(nums))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        condition_5 = MathTex(text.CONDITION_5).move_to(nums).scale(1.8).shift(DOWN)
        self.play(Write(condition_5))
        self.wait()
        self.play(FadeOut(nums))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        rectangle_1 = Rectangle(height=1.5, width=1)
        rectangle_2 = rectangle_1.copy().next_to(rectangle_1)
        rectangle_3 = rectangle_1.copy().next_to(rectangle_2)
        rectangle_4 = rectangle_1.copy().next_to(rectangle_3)
        rectangle_5 = rectangle_1.copy().next_to(rectangle_4)
        rectangle_6 = rectangle_1.copy().next_to(rectangle_5)
        rectangle_7 = rectangle_1.copy().next_to(rectangle_6)
        rectangle_8 = rectangle_1.copy().next_to(rectangle_7)
        rectangle_9 = rectangle_1.copy().next_to(rectangle_8)
        rectangle_10 = rectangle_1.copy().next_to(rectangle_9)
        rectangle_11 = rectangle_1.copy().next_to(rectangle_10)
        rectangles = VGroup(rectangle_1,
                            rectangle_2,
                            rectangle_3,
                            rectangle_4,
                            rectangle_5,
                            rectangle_6,
                            rectangle_7,
                            rectangle_8,
                            rectangle_9,
                            rectangle_10,
                            rectangle_11).move_to(condition_4).scale(0.6).shift(DOWN + 0.2 * RIGHT)
        self.play(ReplacementTransform(condition_5, rectangles))
        self.wait()

        # -------------------------- Point 20 ------------------------------- #
        self.play(FadeOut(Group(condition_1_0, condition_1_1)),
                  condition_4.animate.shift(2 * UP), rectangles.animate.shift(UP))
        self.wait()

        # -------------------------- Point 21 ------------------------------- #
        arrow_1 = Arrow(condition_4[0][0], rectangles[0].get_top())
        arrow_2 = Arrow(condition_4[0][1], rectangles[0].get_top())
        self.play(Write(arrow_1), Write(arrow_2))
        self.wait()

        # -------------------------- Point 22 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).move_to(condition_4).scale(1.8).shift(0.8 * UP)
        self.play(Write(condition_6))
        self.wait()
        self.play(condition_4[0][0].copy().animate.move_to(rectangles[0]), condition_4[0][0].animate.set_color(GREEN))
        self.wait()

        # -------------------------- Point 23 ------------------------------- #
        self.play(FadeOut(Group(condition_6, arrow_1, arrow_2)))
        self.wait()

        # -------------------------- Point 24 ------------------------------- #
        arrow_3 = Arrow(condition_4[0][1], rectangles[1].get_top())
        arrow_4 = Arrow(condition_4[0][2], rectangles[1].get_top())
        self.play(Write(arrow_3), Write(arrow_4))
        self.wait()

        # -------------------------- Point 25 ------------------------------- #
        condition_7 = MathTex(text.CONDITION_7).move_to(condition_4).scale(1.8).shift(0.8 * UP)
        self.play(Write(condition_7))
        self.wait()
        self.play(condition_4[0][2].copy().animate.move_to(rectangles[1]),
                  condition_4[0][2].animate.set_color(GREEN),
                  FadeOut(Group(condition_7, arrow_3, arrow_4)))
        self.wait()

        # -------------------------- Point 26 ------------------------------- #
        line_1 = Line(condition_4[0][1].get_critical_point(UL), condition_4[0][1].get_critical_point(DR), color=RED, stroke_width=7)
        line_2 = Line(condition_4[0][1].get_critical_point(UR), condition_4[0][1].get_critical_point(DL), color=RED, stroke_width=7)
        cross_2 = VGroup(line_1, line_2)
        self.play(Write(cross_2))
        self.wait()

        # -------------------------- Point 27 ------------------------------- #
        arrow_5 = Arrow(condition_4[0][3], rectangles[2].get_top())
        arrow_6 = Arrow(condition_4[0][4], rectangles[3].get_top())
        arrow_7 = Arrow(condition_4[0][5], rectangles[4].get_top())
        arrow_8 = Arrow(condition_4[0][6], rectangles[5].get_top())
        arrow_9 = Arrow(condition_4[0][7], rectangles[6].get_top())
        arrow_10 = Arrow(condition_4[0][8], rectangles[7].get_top())
        arrow_11 = Arrow(condition_4[0][9], rectangles[8].get_top())
        arrow_12 = Arrow(condition_4[0][10], rectangles[9].get_top())
        arrow_13 = Arrow(condition_4[0][11], rectangles[10].get_top())
        self.play(Write(arrow_5), Write(arrow_6), Write(arrow_7), Write(arrow_8), Write(arrow_9), Write(arrow_10),
                  Write(arrow_11), Write(arrow_12), Write(arrow_13))
        self.wait()

        # -------------------------- Point 28 ------------------------------- #
        self.play(condition_4[0][3].copy().animate.move_to(rectangles[2]),
                  condition_4[0][4].copy().animate.move_to(rectangles[3]),
                  condition_4[0][5].copy().animate.move_to(rectangles[4]),
                  condition_4[0][6].copy().animate.move_to(rectangles[5]),
                  condition_4[0][7].copy().animate.move_to(rectangles[6]),
                  condition_4[0][8].copy().animate.move_to(rectangles[7]),
                  condition_4[0][9].copy().animate.move_to(rectangles[8]),
                  condition_4[0][10].copy().animate.move_to(rectangles[9]),
                  condition_4[0][11].copy().animate.move_to(rectangles[10]),
                  condition_4[0][3:].animate.set_color(GREEN))

        # -------------------------- Point 29 ------------------------------- #
        self.play(FadeOut(Group(rectangles, arrow_5, arrow_6, arrow_7, arrow_8,
                                arrow_9, arrow_10, arrow_11, arrow_12, arrow_13)))
        self.wait(3)
