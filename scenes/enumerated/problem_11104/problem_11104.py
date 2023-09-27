from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeOut, Write
from manim import AnimationGroup, Group, VGroup, ReplacementTransform
from manim import Rectangle, Arrow, MathTex, SurroundingRectangle
from manim import PI
from manim import RED, PURE_GREEN, BLUE_C, YELLOW, WHITE

from hanrahashiv import FormulaModificationsScene
from qarakusiscene import QarakusiScene
from hanrahashiv import FormulaModificationsScene
from . import text


class Problem11104(QarakusiScene, FormulaModificationsScene):
    """Վեց տարբեր քարտերի վրա գրված են 61, 24, 7, 599, թվերը: Այդ քարտերը դասավորելով իրար կողքի
     կստացվի 8-անիշ թիվ: Այդ եղանակով ստացեք՝
    ա) հնարավոր ամենամեծ 8-անիշ թիվը,
    բ) հնարավոր ամենափոքր 8-անիշ թիվը:"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point).scale(1.75).shift(RIGHT)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        nums_1 = MathTex(*text.NUMS_1).scale(1.8)
        rectangles = VGroup(*[SurroundingRectangle(nums_1[i], color=WHITE) for i in range(4)])
        rectangles.arrange(buff=0.3).move_to(screen_center)

        nums_1[0].set_color(BLUE_C).move_to(rectangles[0])
        nums_1[1].set_color(RED).move_to(rectangles[1])
        nums_1[2].set_color(PURE_GREEN).move_to(rectangles[2])
        nums_1[3].set_color(YELLOW).move_to(rectangles[3])
        self.play(Write(rectangles), Write(nums_1))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        self.play(AnimationGroup(FadeOut(rectangles), nums_1.animate.arrange(buff=0.06), lag_ratio=0.8))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        consequence_1 = MathTex(text.CONSEQUENCE_1).next_to(nums_1).scale(1.85).shift(1.7 * RIGHT + 0.08 * DOWN)
        arrow_1 = Arrow(max_stroke_width_to_length_ratio=10).next_to(nums_1).scale(0.6).shift(0.3 * LEFT)
        self.play(Write(arrow_1), Write(consequence_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        self.fix_formula(nums_1)
        self.rearrange_formula(nums_1, new_sequence=[1, 0, 3, 2], move_down=[0, 2])
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        self.fix_formula(nums_1)
        self.rearrange_formula(nums_1, new_sequence=[3, 1, 0, 2], move_down=[0], move_up=[3])
        self.wait()

        # -------------------------- Point 7 -------------------------------
        rectangles_1 = VGroup(*[SurroundingRectangle(nums_1[i], color=WHITE) for i in range(4)])
        rectangles_1.arrange(DOWN, buff=0.1).move_to([-5.5, 0.5, 0])
        self.play(*[nums_1[i].animate.move_to(rectangles_1[i]) for i in range(4)], FadeOut(arrow_1))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        rectangles_2 = VGroup(*[Rectangle(height=1.5, width=1) for _ in range(8)])
        rectangles_2.arrange(buff=0.3).move_to(screen_center).scale(0.6).set_z_index(-1)
        self.play(ReplacementTransform(consequence_1, rectangles_2))
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
        self.play(*[nums_1[i].animate.next_to([-6.4, nums_1[i].get_y(), 0]) for i in range(4)])
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        rectangle_1 = Rectangle(height=3.6, width=0.47).move_to(Group(nums_1[0], nums_1[3][0])).shift(0.03 * LEFT)
        self.play(Write(rectangle_1))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        self.play(FadeOut(Group(condition_2, arrow_2)))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #

        # -------------------------- Point 14 ------------------------------- #
        self.play(FadeOut(rectangle_1))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        self.play(AnimationGroup(nums_1[0].animate.move_to(rectangles_2[0]), FadeOut(question_mark), lag_ratio=0.1))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #

        # -------------------------- Point 17 ------------------------------- #
        question_mark.move_to(rectangles_2[1])
        condition_2.move_to(rectangles_2[1]).shift(1.75 * DOWN)
        arrow_2.next_to(rectangles_2[1], DOWN)
        self.play(Write(arrow_2))
        self.play(Write(condition_2), Write(question_mark))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        rectangle_2 = Rectangle(height=2.6, width=0.47).move_to(Group(nums_1[1][0], nums_1[3][0])).shift(0.03 * LEFT)
        self.play(Write(rectangle_2))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        self.play(FadeOut(Group(condition_2, arrow_2)))
        self.wait()

        # -------------------------- Point 20 ------------------------------- #

        # -------------------------- Point 21 ------------------------------- #
        self.play(FadeOut(rectangle_2))
        self.wait()

        # -------------------------- Point 22 ------------------------------- #
        self.play(nums_1[1][0].animate.move_to(rectangles_2[1]),
                  nums_1[1][1].animate.move_to(rectangles_2[2]),
                  FadeOut(question_mark))
        self.wait()

        # -------------------------- Point 23 ------------------------------- #
        question_mark.move_to(rectangles_2[3])
        self.play(Write(question_mark))
        self.wait()

        # -------------------------- Point 24 ------------------------------- #

        # -------------------------- Point 25 ------------------------------- #
        self.play(nums_1[3][0].animate.move_to(rectangles_2[3]),
                  nums_1[3][1].animate.move_to(rectangles_2[4]),
                  nums_1[3][2].animate.move_to(rectangles_2[5]),
                  FadeOut(question_mark))
        self.wait()

        # -------------------------- Point 26 ------------------------------- #
        self.play(nums_1[2][0].animate(run_time=1.5).move_to(rectangles_2[6]),
                  nums_1[2][1].animate(run_time=1.5).move_to(rectangles_2[7]))
        self.wait()

        # -------------------------- Point 27 ------------------------------- #
        self.play(FadeOut(rectangles_2))
        self.wait()

        # -------------------------- Point 28 ------------------------------- #
        self.play(VGroup(*nums_1[0], *nums_1[1], *nums_1[3], *nums_1[2]).animate.arrange(buff=0.1).scale(1.2))
        self.wait()

        # -------------------------- Point 29 ------------------------------- #
        self.play(nums_1.animate.shift(1.7 * UP)) #  set_color(YELLOW).
        self.wait()

        # -------------------------- Point 30 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).move_to(screen_center).scale(1.75)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 31 ------------------------------- #
        nums_2 = MathTex(*text.NUMS_2).next_to(condition_3, DOWN, buff=1).scale(2.2)
        nums_2[0].set_color(RED)
        nums_2[1].set_color(YELLOW)
        nums_2[2].set_color(BLUE_C)
        nums_2[3].set_color(PURE_GREEN)
        self.play(Write(nums_2))
        self.wait(3)
