from objects import SimpleSVGMobject
from qarakusiscene import QarakusiScene
from . import text

from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeOut, Write, FadeIn
from manim import AnimationGroup, Group, VGroup,  Restore, MovingCameraScene
from manim import MathTex, BraceText, Brace, ReplacementTransform


class Problem11525(QarakusiScene, MovingCameraScene):
    """Հինգ արկղերում միասին կա 105 կգ մանդարին։ Առաջինում և երկրորդում միասին կա 39 կգ,
    երկրորդ և երրորդում միասին կա 43 կգ, երրորդ և չորրորդում միասին՝ 49 կգ, չորրորդ և հինգերորդում միասին՝ 42 կգ։
    Քանի՞ կգ մանդարին կա յուրաքանչյուր արկղում:"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [0, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)
        bags_list = ['bags/bag_with_mandarins_1', 'bags/bag_with_mandarins_2','bags/bag_with_mandarins_3',
                     'bags/bag_with_mandarins_4', 'bags/bag_with_mandarins_5']
        MathTex.set_default(font_size=60)
        BraceText.set_default(font_size=60)
        self.camera.frame.save_state()

        # -------------------------- Point 1 ------------------------------- #
        mandarins = VGroup(*[SimpleSVGMobject(bags_list[i]) for i in range(5)])
        mandarins.move_to(screen_center).scale(0.8).arrange(buff=1.1).shift(1.7 * DOWN)
        self.play(FadeIn(mandarins))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point).scale(1.1)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        brace_text_1 = BraceText(mandarins[0:2], text.CONDITION_2, brace_direction=UP)
        brace_text_1.save_state()
        self.play(Write(brace_text_1))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        brace_text_2 = BraceText(mandarins[1:3], text.CONDITION_3, brace_direction=DOWN)
        self.play(Write(brace_text_2))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        brace_text_3 = BraceText(mandarins[2:4], text.CONDITION_4, brace_direction=UP)
        brace_text_3.save_state()
        self.play(Write(brace_text_3))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        brace_text_4 = BraceText(mandarins[3:5], text.CONDITION_5, brace_direction=DOWN)
        self.play(Write(brace_text_4))
        self.wait()

        # -------------------------- Point 7 -------------------------------
        brace_1 = Brace(mandarins[0:4], direction=UP)
        plus = MathTex(text.PLUS).move_to(brace_1).shift(0.65 * UP)
        self.play(ReplacementTransform(Group(brace_text_1[0], brace_text_3[0]), brace_1),
                  brace_text_1[1].animate.shift(1.4 * RIGHT),
                  brace_text_3[1].animate.shift(1.30 * LEFT),
                  Write(plus))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).next_to(condition_1, DOWN).shift(3 * LEFT)
        text_group_1 = VGroup(brace_text_1[1].copy(), brace_text_3[1].copy(), plus.copy())
        self.play(AnimationGroup(text_group_1.animate.next_to(condition_6), Write(condition_6), lag_ratio=0.8))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        self.play(FadeOut(brace_1),
                  Restore(brace_text_1),
                  Restore(brace_text_3),
                  FadeOut(plus))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        condition_7 = MathTex(text.CONDITION_7).next_to(text_group_1)
        self.play(Write(condition_7))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        mandarins[4].save_state()
        self.play(mandarins[4].animate.scale(1.3).shift(0.1 * UP))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        condition_8 = MathTex(text.CONDITION_8).next_to(text_group_1, DOWN).shift(0.8 * RIGHT)
        self.play(Write(condition_8))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        condition_8_part = condition_8[0][13:].copy()
        self.play(Restore(mandarins[4]),
                  condition_8_part.animate.move_to(mandarins[4]).shift(1.25 * UP))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        self.play(self.camera.frame.animate.move_to(mandarins[3:]).scale(0.6), run_time=1.5)
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        condition_9 = MathTex(text.CONDITION_9).move_to(mandarins[3]).shift(1.2 * DOWN)
        condition_10 = MathTex(text.CONDITION_10).move_to(condition_9)
        self.play(ReplacementTransform(brace_text_4, condition_9))
        self.wait()
        self.play(ReplacementTransform(condition_9, condition_10))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        self.play(self.camera.frame.animate.move_to(mandarins[2:4]).scale(1.2), run_time=1.5)
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        condition_11 = MathTex(text.CONDITION_11).move_to(mandarins[2]).shift(1.35 * UP)
        condition_12 = MathTex(text.CONDITION_12).move_to(condition_11)
        self.play(ReplacementTransform(brace_text_3, condition_11))
        self.wait()
        self.play(ReplacementTransform(condition_11, condition_12))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        condition_13 = MathTex(text.CONDITION_13).move_to(mandarins[1]).shift(1.2 * DOWN)
        condition_14 = MathTex(text.CONDITION_14).move_to(mandarins[0]).shift(1.35 * UP)
        self.play(Restore(self.camera.frame), condition_10.animate.shift(2.55 * UP))
        self.wait()

        self.play(ReplacementTransform(brace_text_2, condition_13))
        self.wait()

        self.play(ReplacementTransform(brace_text_1, condition_14), condition_13.animate.shift(2.55 * UP))
        self.wait(3)
