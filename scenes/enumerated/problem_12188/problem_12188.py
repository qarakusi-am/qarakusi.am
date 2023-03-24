from qarakusiscene import QarakusiScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text

from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeOut, Write
from manim import AnimationGroup, VGroup, ReplacementTransform
from manim import Rectangle, Arrow, MathTex, BraceText
from manim import PURE_GREEN, ORANGE


class Problem12188(QarakusiScene, FormulaModificationsScene):
    """Քանի՞ հատ եռանիշ թիվ կա, որ թվանշանների արտադրյալը հավասար է ա) 5-ի, բ) 6-ի:"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point).scale(1.75)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        cdot = VGroup(*[MathTex(text.CDOT) for _ in range(2)]).scale(1.75)
        rectangles = VGroup(*[Rectangle(height=1, width=0.6) for _ in range(3)])
        rectangles.arrange(buff=1.5).next_to(condition_1, DOWN)
        cdot.arrange(buff=2).move_to(rectangles)

        self.play(Write(rectangles), Write(cdot))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_2 = MathTex(text.CONDITION_2).next_to(rectangles).scale(2.3).shift(0.6 * RIGHT)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        brace_text = VGroup(*[BraceText(rectangles[i], text.NUMS_1[i]) for i in range(3)]).shift(0.1 * UP)
        self.play(Write(brace_text))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        nums_2 = VGroup(*[MathTex(text.NUMS_2[i]).move_to(brace_text[i]) for i in range(3)]).scale(1.75)
        nums_2.arrange(buff=0.95).shift(0.5 * UP)
        self.play(ReplacementTransform(brace_text, nums_2))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).next_to(rectangles).scale(2.3).shift(0.6 * RIGHT)
        self.play(FadeOut(nums_2))
        self.play(ReplacementTransform(condition_2, condition_3))
        self.wait()

        # -------------------------- Point 7 -------------------------------
        condition_4 = MathTex(text.CONDITION_4).move_to(screen_center).scale(1.75)
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_5 = MathTex(text.CONDITION_5).next_to(condition_4[0][0]).scale(1.75).shift(2.9 * LEFT + 0.05 * DOWN)

        condition_6 = MathTex(text.CONDITION_6).next_to(condition_4[0][2]).scale(1.75).shift(2.65 * RIGHT + 0.3 * DOWN)
        condition_7 = MathTex(text.CONDITION_7).next_to(condition_4).scale(1.75).shift(2.45 * RIGHT + 0.06 * DOWN)

        self.play(AnimationGroup(
            AnimationGroup(condition_4[0][0:2].animate.shift(3 * LEFT),
                          ReplacementTransform(condition_4[0][1], condition_5),

                          condition_4[0][2].animate.shift(2.75 * RIGHT),
                          condition_4[0][4].animate.shift(2.45 * RIGHT),
                          ReplacementTransform(condition_4[0][3], condition_6)),
                          Write(condition_7), lag_ratio=0.35))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        arrow_1 = Arrow([-1, 1.7, 0], [-3.7, 0.4, 0])
        arrow_2 = Arrow([1, 1.7, 0], [3.7, 0.4, 0])
        self.play(Write(arrow_1), Write(arrow_2),
                  condition_7.animate.set_color(PURE_GREEN),
                  condition_5.animate.set_color(ORANGE),
                  condition_6.animate.set_color(PURE_GREEN),
                  condition_4[0][0].animate.set_color(ORANGE),
                  condition_4[0][2].animate.set_color(PURE_GREEN),
                  condition_4[0][4].animate.set_color(PURE_GREEN))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        nums_3 = MathTex(text.NUMS_3).scale(1.75).next_to(condition_5, DOWN).set_color(ORANGE)
        self.play(Write(nums_3))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        nums_4 = VGroup(*[MathTex(text.NUMS_4[i]) for i in range(2)]).scale(1.75).set_color(PURE_GREEN)
        nums_4.arrange(DOWN).next_to(condition_6, DOWN).shift(0.5 * RIGHT)
        self.play(Write(nums_4))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        condition_8 = text.condition_8

        self.play(Write(condition_8))
        self.wait(3)
