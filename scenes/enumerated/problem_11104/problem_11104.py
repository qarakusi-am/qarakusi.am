from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeOut, Write
from manim import AnimationGroup, Group, VGroup, ReplacementTransform, Wiggle, Transform, Animation
from manim import Line, Rectangle, Arrow, MathTex
from manim import UL, DR, UR, DL, PI
from manim import RED, GREEN, ORANGE, BLUE_C, YELLOW, PURE_BLUE, WHITE

from movement_problems import CustomMovementScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text


class Problem11104(CustomMovementScene):
    """Վեց տարբեր քարտերի վրա գրված են 61, 24, 7, 599, թվերը: Այդ քարտերը դասավորելով իրար կողքի
     կստացվի 8-անիշ թիվ: Այդ եղանակով ստացեք՝
    ա) հնարավոր ամենամեծ 8-անիշ թիվը,
    բ) հնարավոր ամենափոքր 8-անիշ թիվը:"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)
        self.add_plane()

        # def smart_rectangles(qty, position="horizontal")
        #     Rectangle(height=1.5, width=2)

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point).scale(1.75).shift(RIGHT)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        rectangle_1 = Rectangle(height=1.5, width=2)
        rectangle_2 = rectangle_1.copy().next_to(rectangle_1)
        rectangle_3 = Rectangle(height=1.5, width=1).next_to(rectangle_2)
        rectangle_4 = Rectangle(height=1.5, width=3).next_to(rectangle_3)
        rectangles = VGroup(rectangle_1, rectangle_2, rectangle_3, rectangle_4
                           ).move_to(screen_center).scale(0.6)

        nums_1 = MathTex(*text.NUMS_1).scale(1.8)
        nums_1[0].set_color(BLUE_C).move_to(rectangle_1)
        nums_1[1].set_color(RED).move_to(rectangle_2)
        nums_1[2].set_color(PURE_BLUE).move_to(rectangle_3)
        nums_1[3].set_color(YELLOW).move_to(rectangle_4)
        self.play(Write(rectangles), Write(nums_1))
        self.wait()


        # -------------------------- Point 3 ------------------------------- #
        self.play(FadeOut(rectangles),
                  nums_1[0].animate.shift(0.65 * RIGHT),
                  nums_1[1].animate.shift(0.24 * RIGHT),
                  nums_1[2].animate.shift(0.15 * LEFT),
                  nums_1[3].animate.shift(0.64 * LEFT))
        self.wait()
        # line_1 = Line(condition_2[2].get_critical_point(UL), condition_2[2].get_critical_point(DR), color=RED, stroke_width=7)
        # line_2 = Line(condition_2[2].get_critical_point(UR), condition_2[2].get_critical_point(DL), color=RED, stroke_width=7)
        # cross = VGroup(line_1, line_2)
        # self.play(Wiggle(condition_2[2], scale_value=1.7))
        # self.wait()
        # self.play(Write(cross))
        # self.wait()

        # -------------------------- Point 4 ------------------------------- #
        consequence_1 = MathTex(text.CONSEQUENCE_1).next_to(nums_1).scale(1.85).shift(1.7 * RIGHT + 0.08 * DOWN)
        arrow_1 = Arrow(max_stroke_width_to_length_ratio=10).next_to(nums_1).scale(0.6).shift(0.3 * LEFT)
        self.play(Write(arrow_1), Write(consequence_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        nums_2 = MathTex(*text.NUMS_2).scale(1.8).move_to(nums_1)
        nums_2[0:2].set_color(RED)
        nums_2[2:4].set_color(BLUE_C)
        nums_2[4:7].set_color(YELLOW)
        nums_2[7:].set_color(PURE_BLUE)


        self.play(ReplacementTransform(nums_1, nums_2))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        nums_3 = MathTex(*text.NUMS_3).scale(1.8).move_to(nums_2)
        nums_3[0].set_color(PURE_BLUE)
        nums_3[1:3].set_color(BLUE_C)
        nums_3[3:5].set_color(RED)
        nums_3[5:].set_color(YELLOW)
        self.play(ReplacementTransform(nums_2, nums_3))
        self.wait()

        # -------------------------- Point 7 -------------------------------
        rectangle_1 = Rectangle(height=1.2, width=0.8)
        rectangle_2 = rectangle_1.copy().next_to(rectangle_1, DOWN)
        rectangle_3 = rectangle_1.copy().next_to(rectangle_2, DOWN)
        rectangle_4 = rectangle_1.copy().next_to(rectangle_3, DOWN)
        rectangle_5 = rectangle_1.copy().next_to(rectangle_4, DOWN)
        rectangle_6 = rectangle_1.copy().next_to(rectangle_5, DOWN)
        rectangle_7 = rectangle_1.copy().next_to(rectangle_6, DOWN)
        rectangle_8 = rectangle_1.copy().next_to(rectangle_7, DOWN)
        rectangles_1 = VGroup(rectangle_1, rectangle_2, rectangle_3, rectangle_4, rectangle_5, rectangle_6,
                            rectangle_7, rectangle_8).move_to([-6, -0.4, 0]).scale(0.6)
        nums_3_copy = nums_3.copy() # TODO: make work without copy
        for i in range(8):
            nums_3_copy[i].move_to(rectangles_1[i])
        self.play(ReplacementTransform(nums_3, nums_3_copy), FadeOut(arrow_1))
        self.wait()
        self.play(Write(rectangles_1))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        rectangle_1 = Rectangle(height=1.5, width=1)
        rectangle_2 = rectangle_1.copy().next_to(rectangle_1)
        rectangle_3 = rectangle_1.copy().next_to(rectangle_2)
        rectangle_4 = rectangle_1.copy().next_to(rectangle_3)
        rectangle_5 = rectangle_1.copy().next_to(rectangle_4)
        rectangle_6 = rectangle_1.copy().next_to(rectangle_5)
        rectangle_7 = rectangle_1.copy().next_to(rectangle_6)
        rectangle_8 = rectangle_1.copy().next_to(rectangle_7)
        rectangles_2 = VGroup(rectangle_1,
                              rectangle_2,
                              rectangle_3,
                              rectangle_4,
                              rectangle_5,
                              rectangle_6,
                              rectangle_7,
                              rectangle_8).move_to(screen_center).scale(0.6)
        self.play(ReplacementTransform(consequence_1, rectangles_2))

        # self.fix_formula(condition_2_copy_1)
        # self.fix_formula(condition_2_copy_2)
        # self.fix_formula(condition_2_copy_3)
        # self.fix_formula(condition_2_copy_4)
        # self.play(ModifyFormula(condition_2_copy_1, remove_items=[0]))
        # self.wait()
        # self.play(ModifyFormula(condition_2_copy_2, remove_items=[1]))
        # self.wait()
        # self.play(ModifyFormula(condition_2_copy_3, remove_items=[2]))
        # self.wait()
        # self.play(ModifyFormula(condition_2_copy_4, remove_items=[3]))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        question_mark = MathTex(text.QUESTION_MARK).scale(1.8).move_to(rectangles_2[0])
        condition_2 = MathTex(text.CONDITION_2).scale(1.4).move_to(rectangles_2[0]).shift(1.75 * DOWN)
        arrow_2 = Arrow(max_stroke_width_to_length_ratio=13).next_to(rectangles_2[0], DOWN).scale(0.5)
        arrow_2.shift(0.1 * DOWN).rotate(0.5 * PI)
        self.play(Write(arrow_2))
        self.play(Write(condition_2), Write(question_mark))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #

        self.wait()

        # -------------------------- Point 11 ------------------------------- #

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
