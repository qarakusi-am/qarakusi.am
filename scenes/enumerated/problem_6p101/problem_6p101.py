from manim import LEFT, UP, DOWN, RIGHT, CurvedArrow, Create, Rectangle, YELLOW, RED
from manim import FadeOut, Write, FadeIn
from manim import Group, ReplacementTransform, AnimationGroup, VGroup
from manim import MathTex

from qarakusiscene import QarakusiScene
from . import text as t


class Problem6p101(QarakusiScene):
    """Գրե՛ք հնարավոր ամենամեծ տասնորդական կոտորակը, որը.
        ա) փոքր է 5-ից և կետից հետո ունի մեկ թվանշան,
        բ) փոքր է 1-ից և կետից հետո ունի երկու թվանշան,
        գ) փոքր է 10-ից և կետից հետո ունի իրարից տարբեր երեք թվանշան,
        դ) փոքր է 124-ից և կետից հետո ունի երկու թվանշան, որոնց գումարը 15 է:
    """
    def construct(self):
        screen_center = [-0.6, 1.3, 0]
        row_buff = 0.9
        self.add_task_number(text=t.TASK_NUMBER_STR)
        MathTex.set_default(font_size=t.default_font_size)
        # self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_0 = MathTex(t.CONDITION_0).shift(3.4 * UP)
        condition_1 = MathTex(*t.CONDITION_1).shift(1.5 * UP)
        self.play(Write(condition_0), run_time=3)
        self.wait()
        self.play(Write(condition_1), run_time=3)
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_2 = MathTex(t.CONDITION_2).next_to(condition_1, DOWN).shift(1.5 * DOWN)
        hidden_1 = MathTex(t.CONDITION_2).next_to(condition_2, LEFT).shift(0.3 * LEFT)
        hidden_2 = MathTex(t.CONDITION_2).next_to(condition_2, RIGHT).shift(0.3 * RIGHT)
        condition_3 = MathTex(t.CONDITION_3, font_size=50, color=YELLOW).next_to(hidden_1, DOWN).shift(0.95 * LEFT)
        condition_4 = MathTex(t.CONDITION_4, font_size=50, color=RED).next_to(hidden_2, DOWN).shift(1.65 * RIGHT)

        self.play(FadeIn(condition_2), run_time=1)
        self.wait()
        curved_arrow_1 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_1.get_critical_point(UP),
            radius=0.5,
            color=YELLOW,
            tip_length=0.265,
            stroke_width=3,
            ).shift(0.3 * UP)
        self.play(Create(curved_arrow_1))
        self.play(Write(condition_3))

        self.wait()
        curved_arrow_2 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_2.get_critical_point(UP),
            radius=-0.5,
            color=RED,
            tip_length=0.265,
            stroke_width=3,
            ).shift(0.3 * UP)
        self.play(Create(curved_arrow_2))
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_5 = MathTex(t.CONDITION_5, font_size=50).next_to(curved_arrow_1, UP).shift(1.2 * LEFT)
        self.play(Write(condition_5))
        self.wait()


        # -------------------------- Point 4 ------------------------------- #
        num_1 = MathTex(t.NUM_1, font_size=50, color=YELLOW).move_to(hidden_1).shift(0.1 * UP)
        self.play(Write(num_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        self.play(FadeOut(condition_5))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        rectangle_1 = Rectangle(height=0.45, width=0.33, color=RED).move_to(hidden_2).shift(0.1 * UP)
        self.play(ReplacementTransform(condition_1[1].copy(), rectangle_1), run_time=1.5)
        # self.play(Create(rectangle_1))
        self.wait()
        num_2 = MathTex(t.NUM_2, font_size=50, color=RED).move_to(rectangle_1)
        self.play(Write(num_2))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        self.play(
            FadeOut(
                Group(condition_3, condition_4, rectangle_1, curved_arrow_1, curved_arrow_2)
            )
        )
        self.wait()
        self.play(AnimationGroup(num_1.animate.shift(0.4 * RIGHT), num_2.animate.shift(0.4 * LEFT)))

        # -------------------------- Point 8 ------------------------------- #
        num_group_1 = Group(num_1, condition_2, num_2)
        self.play(AnimationGroup(
            condition_1.animate.shift(1.3 * UP + 1.4 * LEFT),
            num_group_1.animate.shift(3.28 * UP + 4.8 * RIGHT),
            run_time=2.6,
        ))

        # -------------------------- Point 9 ------------------------------- #
        condition_11 = MathTex(*t.CONDITION_11).shift(1.5 * UP + 0.3 * LEFT)
        self.play(Write(condition_11), run_time=3)
        self.wait()

            # -------------------------- Point 1 ------------------------------- #
        condition_2 = MathTex(t.CONDITION_2).next_to(condition_1, DOWN).shift(2.6 * DOWN, 1.45 * RIGHT)
        hidden_1 = MathTex(t.CONDITION_2).next_to(condition_2, LEFT).shift(0.3 * LEFT)
        hidden_2 = MathTex(t.CONDITION_2).next_to(condition_2, RIGHT).shift(0.3 * RIGHT)
        condition_3 = MathTex(t.CONDITION_3, font_size=50, color=YELLOW).next_to(hidden_1, DOWN).shift(0.95 * LEFT)
        condition_4 = MathTex(t.CONDITION_4, font_size=50, color=RED).next_to(hidden_2, DOWN).shift(1.65 * RIGHT)

        self.play(FadeIn(condition_2), run_time=1)
        self.wait()
        curved_arrow_1 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_1.get_critical_point(UP),
            radius=0.5,
            color=YELLOW,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_1))
        self.play(Write(condition_3))

        self.wait()
        curved_arrow_2 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_2.get_critical_point(UP),
            radius=-0.5,
            color=RED,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_2))
        self.play(Write(condition_4))
        self.wait()

            # -------------------------- Point 2 ------------------------------- #
        condition_13 = MathTex(t.CONDITION_13, font_size=50).next_to(curved_arrow_1, UP).shift(1.2 * LEFT)
        self.play(Write(condition_13))
        self.wait()

            # -------------------------- Point 3 ------------------------------- #
        num_11 = MathTex(t.NUM_11, font_size=50, color=YELLOW).move_to(hidden_1).shift(0.1 * UP)
        self.play(Write(num_11))
        self.wait()

            # -------------------------- Point 5 ------------------------------- #
        rectangle_11 = Rectangle(height=0.45, width=0.33, color=RED).move_to(hidden_2).shift(0.1 * UP)
        rectangle_12 = Rectangle(height=0.45, width=0.33, color=RED).next_to(rectangle_11, RIGHT, buff=0)
        rectangle_group_1 = VGroup(rectangle_11, rectangle_12)
        self.play(ReplacementTransform(condition_11[1].copy(), rectangle_group_1), run_time=2)
        self.wait()
        num_12 = MathTex(t.NUM_12, font_size=50, color=RED).move_to(rectangle_11)
        num_12_copy = num_12.copy().move_to(rectangle_12)
        self.play(Write(num_12))
        self.play(Write(num_12_copy))
        self.wait()

            # -------------------------- Point 6 ------------------------------- #
        self.play(
            FadeOut(
                Group(condition_3, condition_4, rectangle_11, rectangle_12, curved_arrow_1, curved_arrow_2, condition_13)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                num_11.animate.shift(0.4 * RIGHT),
                num_12.animate.shift(0.4 * LEFT),
                num_12_copy.animate.shift(0.5 * LEFT),
            )
        )

            # -------------------------- Point 7 ------------------------------- #
        num_group_11 = Group(num_11, condition_2, num_12, num_12_copy)
        self.play(AnimationGroup(
            condition_11.animate.shift(0.73 * UP + 0.85 * LEFT),
            num_group_11.animate.shift(2.522 * UP + 5.2 * RIGHT),
            run_time=2.6,
        ))

        ########################## ԳԳԳԳԳԳԳԳԳ ######################################

        condition_21 = MathTex(*t.CONDITION_21).shift(1.63 * UP + 0.1 * LEFT)
        condition_21[2].next_to(condition_21[0], DOWN, buff=0.1, aligned_edge=LEFT)
        self.play(Write(condition_21), run_time=3)
        self.wait()

        # -------------------------- Point 1 ------------------------------- #
        condition_2 = MathTex(t.CONDITION_2).next_to(condition_1, DOWN).shift(3 * DOWN, RIGHT)
        hidden_21 = MathTex(t.CONDITION_2).next_to(condition_2, LEFT).shift(0.3 * LEFT)
        hidden_22 = MathTex(t.CONDITION_2).next_to(condition_2, RIGHT).shift(0.3 * RIGHT)
        condition_3 = MathTex(t.CONDITION_3, font_size=50, color=YELLOW).next_to(hidden_21, DOWN).shift(0.95 * LEFT)
        condition_4 = MathTex(t.CONDITION_4, font_size=50, color=RED).next_to(hidden_22, DOWN).shift(1.65 * RIGHT)

        self.play(FadeIn(condition_2), run_time=1)
        self.wait()
        curved_arrow_1 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_21.get_critical_point(UP),
            radius=0.5,
            color=YELLOW,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_1))
        self.play(Write(condition_3))

        self.wait()
        curved_arrow_2 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_22.get_critical_point(UP),
            radius=-0.5,
            color=RED,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_2))
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_23 = MathTex(t.CONDITION_23, font_size=50).next_to(curved_arrow_1, UP).shift(1.37 * LEFT)
        self.play(Write(condition_23))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        num_21 = MathTex(t.NUM_21, font_size=50, color=YELLOW).move_to(hidden_21).shift(0.1 * UP)
        self.play(Write(num_21))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        rectangle_21 = Rectangle(height=0.45, width=0.33, color=RED).move_to(hidden_22).shift(0.1 * UP)
        rectangle_22 = Rectangle(height=0.45, width=0.33, color=RED).next_to(rectangle_21, RIGHT, buff=0)
        rectangle_23 = Rectangle(height=0.45, width=0.33, color=RED).next_to(rectangle_22, RIGHT, buff=0)
        rectangle_group_3 = VGroup(rectangle_21, rectangle_22, rectangle_23)
        self.play(ReplacementTransform(condition_21[1].copy(), rectangle_group_3), run_time=2)
        self.wait()
        num_22 = MathTex(t.NUM_22, font_size=50, color=RED).move_to(rectangle_21)
        num_23 = MathTex(t.NUM_23, font_size=50, color=RED).move_to(rectangle_22)
        num_24 = MathTex(t.NUM_24, font_size=50, color=RED).move_to(rectangle_23)
        self.play(Write(num_22))
        self.play(Write(num_23))
        self.play(Write(num_24))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        self.play(
            FadeOut(
                Group(condition_3, condition_4, rectangle_21, rectangle_22, rectangle_23, curved_arrow_1, curved_arrow_2, condition_23)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                num_21.animate.shift(0.4 * RIGHT),
                num_22.animate.shift(0.4 * LEFT),
                num_23.animate.shift(0.5 * LEFT),
                num_24.animate.shift(0.6 * LEFT),
            )
        )

        # -------------------------- Point 7 ------------------------------- #
        num_group_11 = Group(num_21, condition_2, num_22, num_23, num_24)
        self.play(AnimationGroup(
            # condition_11.animate.shift(0.3 * UP + 0.27 * LEFT),
            num_group_11.animate.next_to(condition_21[2], RIGHT).shift(0.05 * UP),
            run_time=2.6,
        ))

        ########################## ԴԴԴԴԴԴԴԴԴԴԴԴԴԴ ######################################

        condition_31 = MathTex(*t.CONDITION_31).next_to(condition_21, DOWN, aligned_edge=LEFT).shift(0.2 * UP)
        condition_31[3].next_to(condition_31[0], DOWN, buff=0.1, aligned_edge=LEFT)
        self.play(Write(condition_31), run_time=3)
        self.wait()

        # -------------------------- Point 1 ------------------------------- #
        condition_2 = MathTex(t.CONDITION_2).next_to(condition_1, DOWN).shift(4.2 * DOWN, 1.3 * RIGHT)
        hidden_21 = MathTex(t.CONDITION_2).next_to(condition_2, LEFT).shift(0.3 * LEFT)
        hidden_22 = MathTex(t.CONDITION_2).next_to(condition_2, RIGHT).shift(0.3 * RIGHT)
        condition_3 = MathTex(t.CONDITION_3, font_size=50, color=YELLOW).next_to(hidden_21, DOWN).shift(0.95 * LEFT)
        condition_4 = MathTex(t.CONDITION_4, font_size=50, color=RED).next_to(hidden_22, DOWN).shift(1.65 * RIGHT)

        self.play(FadeIn(condition_2), run_time=1)
        self.wait()
        curved_arrow_1 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_21.get_critical_point(UP),
            radius=0.5,
            color=YELLOW,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_1))
        self.play(Write(condition_3))

        self.wait()
        curved_arrow_2 = CurvedArrow(
            start_point=condition_2.get_critical_point(UP),
            end_point=hidden_22.get_critical_point(UP),
            radius=-0.5,
            color=RED,
            tip_length=0.265,
            stroke_width=3,
        ).shift(0.3 * UP)
        self.play(Create(curved_arrow_2))
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_33 = MathTex(t.CONDITION_33, font_size=50).next_to(curved_arrow_1, UP).shift(1.49 * LEFT)
        self.play(Write(condition_33))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        num_31 = MathTex(t.NUM_31, font_size=50, color=YELLOW).move_to(hidden_21).shift(0.1 * UP)
        self.play(Write(num_31))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        rectangle_31 = Rectangle(height=0.45, width=0.33, color=RED).move_to(hidden_22).shift(0.1 * UP)
        rectangle_32 = Rectangle(height=0.45, width=0.33, color=RED).next_to(rectangle_31, RIGHT, buff=0)
        rectangle_group_4 = VGroup(rectangle_31, rectangle_32)
        self.play(ReplacementTransform(condition_31[1].copy(), rectangle_group_4), run_time=2)
        self.wait()
        num_32 = MathTex(t.NUM_32, font_size=50, color=RED).move_to(rectangle_31)
        num_33 = MathTex(t.NUM_33, font_size=50, color=RED).move_to(rectangle_32)

        self.play(Write(num_32))
        self.play(Write(num_33))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        self.play(
            FadeOut(
                Group(condition_3, condition_4, rectangle_31, rectangle_32, curved_arrow_1,
                      curved_arrow_2, condition_33)
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                num_31.animate.shift(0.17 * RIGHT),
                num_32.animate.shift(0.41 * LEFT),
                num_33.animate.shift(0.51 * LEFT),
            )
        )

        # -------------------------- Point 7 ------------------------------- #
        num_group_31 = Group(num_31, condition_2, num_32, num_33)
        self.play(AnimationGroup(
            num_group_31.animate.next_to(condition_31[3], RIGHT).shift(0.045 * UP),
            run_time=2.6,
        ))

        self.wait(3)
