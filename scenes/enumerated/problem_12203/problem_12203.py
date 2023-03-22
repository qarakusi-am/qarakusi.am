from qarakusiscene import QarakusiScene
from . import text

from manim import LEFT, UP, DOWN, RIGHT, TAU
from manim import FadeOut, Write, FadeIn, Create
from manim import Group, ReplacementTransform, BraceBetweenPoints, CurvedArrow, ImageMobject, SurroundingRectangle, VGroup
from manim import Arrow, MathTex
from manim import DR, UR



class Problem12203(QarakusiScene):
    """Դրոնն աշխատեց 3 օր, օրական 6 ժամ, իսկ այնուհետև 2 օր, օրական 7 ժամ և ընդհանուր մշակեց 168 հա դաշտը։
    Պարզել, թե քանի՞ ար դաշտ է մշակում դրոնը մեկ ժամում։"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]

        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        drone = ImageMobject('objects/PNG_files/drone').move_to(screen_center).scale(1.5).set_z_index(-1)
        self.play(FadeIn(drone))
        self.wait(2)
        self.play(FadeOut(drone))
        self.wait(1)

        # -------------------------- Point 2 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point)
        self.play(Write(condition_1))
        self.wait(1)

        # -------------------------- Point 3 ------------------------------- #
        condition_2 = MathTex(text.CONDITION_2).next_to(condition_1, DOWN)
        self.play(Write(condition_2))
        self.wait(1)

        # -------------------------- Point 4 ------------------------------- #
        brace = BraceBetweenPoints(condition_1.get_critical_point(UR), condition_2.get_critical_point(DR), RIGHT)
        condition_3 = MathTex(text.CONDITION_3).next_to(brace).shift(0.01 * RIGHT)
        self.play(Write(brace), Write(condition_3))
        self.wait(1)

        # -------------------------- Point 5 ------------------------------- #
        condition_4 = MathTex(*text.CONDITION_45)
        condition_4.arrange(buff=1.5).move_to(screen_center).shift(0.5 * DOWN)
        condition_4[2].shift(0.1 * UP)

        addition_to_condition_1 = MathTex(*text.ADDITION_TO_CONDITION_1)
        addition_to_condition_1.arrange(buff=text.addition_to_condition_buff
                                        ).move_to(condition_4).shift(text.addition_to_condition_shift * RIGHT + 0.1 * UP)

        arc_1 = CurvedArrow(start_point=condition_1.get_critical_point(LEFT),
                            end_point=condition_4.get_critical_point(LEFT),
                            angle=TAU / 3)
        self.play(FadeIn(Group(condition_4, addition_to_condition_1)), Create(arc_1))
        self.wait(1)

        # -------------------------- Point 6 ------------------------------- #
        condition_5 = condition_4.copy()
        condition_5.arrange(buff=1.5).move_to(screen_center).shift(0.5 * UP)
        condition_5[2].shift(0.1 * UP)

        addition_to_condition_2 = MathTex(*text.ADDITION_TO_CONDITION_2)
        addition_to_condition_2.arrange(buff=text.addition_to_condition_buff
                                        ).move_to(condition_5).shift(text.addition_to_condition_shift * RIGHT + 0.1 * UP)

        arc_2 = CurvedArrow(start_point=condition_2.get_critical_point(LEFT),
                            end_point=condition_5.get_critical_point(LEFT),
                            angle=TAU / 3)

        self.play(FadeIn(Group(condition_5, addition_to_condition_2)), Create(arc_2))
        self.wait(1)

        # -------------------------- Point 7 -------------------------------
        self.play(FadeOut(Group(arc_1, arc_2)))
        self.wait(1)

        # -------------------------- Point 8 ------------------------------- #
        addition_to_condition_3 = MathTex(*text.ADDITION_TO_CONDITION_3)
        addition_to_condition_3.arrange(buff=text.addition_to_condition_buff
                                        ).move_to(condition_5).shift(text.addition_to_condition_shift * RIGHT + 0.1 * UP)
        self.play(condition_4.animate.move_to(condition_5),
                  ReplacementTransform(
                      Group(addition_to_condition_1[0], addition_to_condition_2[0]),
                      addition_to_condition_3[0]),
                  ReplacementTransform(
                      Group(addition_to_condition_1[1], addition_to_condition_2[1]),
                      addition_to_condition_3[1]))

        self.remove(condition_4)
        self.wait(1)

        # -------------------------- Point 9 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).move_to(condition_5).shift(1.3 * DOWN)
        self.play(Write(condition_6))
        self.wait(1)

        # -------------------------- Point 10 ------------------------------- #
        condition_7 = MathTex(*text.CONDITION_7).move_to(condition_6).shift(1.3 * DOWN + 2.3 * LEFT)
        self.play(Write(condition_7))
        self.wait(1)

        # -------------------------- Point 11 ------------------------------- #
        condition_8 = MathTex(text.CONDITION_8).next_to(condition_7).shift(RIGHT + 0.05 * UP)
        arrow_1 = Arrow(max_tip_length_to_length_ratio=1.5).scale(0.6).next_to(condition_7)
        self.play(Write(arrow_1), Write(condition_8))
        self.wait(1)

        # -------------------------- Point 12 ------------------------------- #
        rectangle = SurroundingRectangle(VGroup(condition_7[1], condition_8))
        self.wait(1)
        self.play(Write(rectangle))
        self.wait(3)
