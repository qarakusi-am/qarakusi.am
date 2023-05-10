from manim import LEFT, UP, DOWN, RIGHT, BLUE, ORIGIN
from manim import FadeOut, Write, FadeIn
from manim import AnimationGroup, Group, VGroup, ReplacementTransform
from manim import Line, Rectangle, Arrow, MathTex, Circle, Dot, Arc, PI, Restore, Difference
from manim import RED, PURE_GREEN, ORANGE, WHITE
from manim import MovingCameraScene

from qarakusiscene import QarakusiScene
from . import text


class Problem12795(QarakusiScene, MovingCameraScene):
    """Գտե´ք 100-ից փոքր այն թվերի քանակը, որոնք բաժանվում են 2-ի կամ 3-ի, բայց չեն բաժանվում 6-ի։"""
    def construct(self):
        screen_center = [0, 1.5, 0]
        condition_point = [0, 3.2, 0]
        condition_1_down_shift = 1.5
        self.add_task_number(text=text.TASK_NUMBER_STR)
        # self.add_plane()
        MathTex.set_default(font_size=65)

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*list(range(1, 16))).arrange(buff=0.55).move_to(screen_center)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        even_index = list(range(1, 15, 2))
        self.play(*[condition_1[i].animate.set_color(ORANGE) for i in even_index])
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_1_1_copy = condition_1[1].copy()
        self.play(condition_1_1_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_1 = MathTex(text.TRANSFORM_1, color=ORANGE).move_to(condition_1_1_copy)
        self.play(ReplacementTransform(condition_1_1_copy, transform_1))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_1_3_copy = condition_1[3].copy()
        self.play(condition_1_3_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_2 = MathTex(text.TRANSFORM_2, color=ORANGE).move_to(condition_1_3_copy)
        self.play(ReplacementTransform(condition_1_3_copy, transform_2))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        condition_1_5_copy = condition_1[5].copy()
        self.play(condition_1_5_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_3 = MathTex(text.TRANSFORM_3, color=ORANGE).move_to(condition_1_5_copy)
        self.play(ReplacementTransform(condition_1_5_copy, transform_3))
        self.wait()

        condition_1_7_copy = condition_1[7].copy()
        condition_1_9_copy = condition_1[9].copy()
        condition_1_11_copy = condition_1[11].copy()

        self.play(condition_1_7_copy.animate.shift(condition_1_down_shift * DOWN),
                  condition_1_9_copy.animate.shift(condition_1_down_shift * DOWN+ 0.1 * LEFT),
                  condition_1_11_copy.animate.shift(condition_1_down_shift * DOWN + 0.7 * LEFT))

        transform_4 = MathTex(text.TRANSFORM_4, color=ORANGE).move_to(condition_1_7_copy)
        transform_5 = MathTex(text.TRANSFORM_5, color=ORANGE).move_to(condition_1_9_copy)
        transform_6 = MathTex(text.TRANSFORM_6, color=ORANGE).move_to(condition_1_11_copy).shift(0.05 * UP)

        self.play(ReplacementTransform(condition_1_7_copy, transform_4),
                  ReplacementTransform(condition_1_9_copy, transform_5),
                  ReplacementTransform(condition_1_11_copy, transform_6))
        self.wait()

        multipoint_1 = MathTex(text.MULTIPOINT, color=ORANGE).next_to(transform_6, aligned_edge=DOWN, buff=0.5)
        self.play(Write(multipoint_1))
        self.wait()

        for_49 = MathTex(text.FOR_49, color=ORANGE).next_to(multipoint_1, aligned_edge=DOWN, buff=0.5)
        self.play(Write(for_49))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        circle_1 = Circle(1.5, color=ORANGE).shift(2.2 * DOWN + 2 * RIGHT)
        num_49 = MathTex(text.NUM_49).move_to(circle_1)
        self.play(ReplacementTransform(Group(transform_1, transform_2, transform_3, transform_4,
                                             transform_5, transform_6, multipoint_1, for_49), circle_1))
        self.play(Write(num_49))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        self.play(condition_1.animate.set_color(WHITE))
        self.play(condition_1[2::3].animate.set_color(PURE_GREEN))
        self.wait()

        condition_1_2_copy = condition_1[2].copy()
        self.play(condition_1_2_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_7 = MathTex(text.TRANSFORM_7, color=PURE_GREEN).move_to(condition_1_2_copy)
        self.play(ReplacementTransform(condition_1_2_copy, transform_7))
        self.wait()

        condition_1_5_copy = condition_1[5].copy()
        self.play(condition_1_5_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_8 = MathTex(text.TRANSFORM_8, color=PURE_GREEN).move_to(condition_1_5_copy)
        self.play(ReplacementTransform(condition_1_5_copy, transform_8))
        self.wait()

        condition_1_8_copy = condition_1[8].copy()
        self.play(condition_1_8_copy.animate.shift(condition_1_down_shift * DOWN))
        transform_9 = MathTex(text.TRANSFORM_9, color=PURE_GREEN).move_to(condition_1_8_copy)
        self.play(ReplacementTransform(condition_1_8_copy, transform_9))
        self.wait()

        condition_1_11_copy = condition_1[11].copy()
        self.play(condition_1_11_copy.animate.shift(condition_1_down_shift * DOWN + 0.8 * LEFT))
        transform_10 = MathTex(text.TRANSFORM_10, color=PURE_GREEN).move_to(condition_1_11_copy).shift(0.06 * UP)
        self.play(ReplacementTransform(condition_1_11_copy, transform_10))
        self.wait()

        multipoint_2 = MathTex(text.MULTIPOINT,
                               color=PURE_GREEN).next_to(condition_1_11_copy,
                                                         aligned_edge=DOWN, buff=0.5).shift(0.01 * UP)
        self.play(Write(multipoint_2))
        self.wait()

        for_33 = MathTex(text.FOR_33, color=PURE_GREEN).next_to(multipoint_2, aligned_edge=DOWN, buff=0.5)
        self.play(Write(for_33))
        self.wait()

        circle_2 = Circle(1.5, color=PURE_GREEN).shift(2.2 * DOWN + 2 * LEFT)
        num_33 = MathTex(text.NUM_33).move_to(circle_2)
        self.play(ReplacementTransform(Group(transform_10, transform_9, transform_8, transform_7, multipoint_2, for_33), circle_2))
        self.play(Write(num_33))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        dot_1 = Dot([1, -1, 0])
        arrow_1 = Arrow(condition_1[5].get_critical_point(DOWN),
                        dot_1,
                        color=ORANGE)

        arrow_2 = Arrow(condition_1[5].get_critical_point(DOWN),
                        circle_2.get_critical_point(UP),
                        color=PURE_GREEN)
        self.play(Write(arrow_1), Write(arrow_2))
        self.wait()

        arrow_3 = Arrow(condition_1[11].get_critical_point(DOWN),
                        circle_1.get_critical_point(UP),
                        color=ORANGE)

        dot_2 = Dot([-1, -1, 0])
        arrow_4 = Arrow(condition_1[11].get_critical_point(DOWN),
                        dot_2,
                        color=PURE_GREEN)
        self.play(Write(arrow_3), Write(arrow_4))

        # -------------------------- Point 9 ------------------------------- #
        condition_2 = MathTex(*text.CONDITION_2).move_to(condition_point)
        self.play(Write(condition_2))
        self.wait()

        arc_1 = Arc(start_angle=PI / 100 * 173.5, angle=PI / 1.89, radius=1.5).shift(2.2 * DOWN)
        arc_2 = Arc(start_angle=-PI / 100 * 73.5, angle=-PI / 1.89, radius=1.5).shift(2.2 * DOWN)
        line_1 = Line(arc_1.get_start_and_end()[0], arc_1.get_start_and_end()[1])
        line_2 = Line(arc_2.get_start_and_end()[0], arc_2.get_start_and_end()[1])
        self.play(FadeIn(Group(arc_1, arc_2)))
        self.wait()
        self.play(arc_1.animate.set_color(PURE_GREEN), arc_2.animate.set_color(ORANGE))
        self.wait()

        num_33_copy = num_33.copy().move_to(num_49)
        num_33.save_state()
        num_49.save_state()
        self.camera.frame.save_state()

        self.play(FadeOut(Group(arrow_1, arrow_2, arrow_3, arrow_4)))
        condition_2_1_copy_1 = condition_2[1].copy()
        condition_2_1_copy_2 = condition_2[1].copy()
        self.play(condition_2_1_copy_1.animate.move_to(line_1),
                  condition_2_1_copy_2.animate.move_to(line_2),
                  self.camera.frame.animate.move_to(Group(circle_1, circle_2)).scale(0.7),
                  num_33.animate.scale(0.7).set_opacity(0.7),
                  num_49.animate.scale(0.7).set_opacity(0.7),
                  run_time=3)
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        self.play(Restore(num_49))
        self.play(ReplacementTransform(num_49, num_33_copy))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        self.play(Restore(num_33))
        num_17 = MathTex(text.NUM_17).move_to(num_33)
        self.play(ReplacementTransform(num_33, num_17))
        self.wait()

        # -------------------------- Point 10 ------------------------------- # + 1.5 * UP
        self.play(Group(circle_1, num_33_copy, arc_1, condition_2_1_copy_1).animate.shift(LEFT + 1.5 * UP),
                  Group(circle_2, num_17, arc_2, condition_2_1_copy_2).animate.shift(RIGHT + 1.5 * UP),
                  Restore(self.camera.frame),
                  run_time=3)
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        diff_1 = Difference(circle_1, circle_2, color=ORANGE, fill_opacity=0.2)
        diff_2 = Difference(circle_2, circle_1, color=PURE_GREEN, fill_opacity=0.2)
        result = MathTex(*text.RESULT).next_to(Group(circle_1, circle_2), DOWN).shift(0.6 * DOWN)
        result[0].set_color(PURE_GREEN)
        result[2].set_color(ORANGE)
        self.play(Write(result))
        self.play(FadeIn(diff_1), FadeIn(diff_2))
        arrow_5 = Arrow(result[0],
                        circle_2,
                        color=PURE_GREEN,
                        max_tip_length_to_length_ratio=0.45,
                        max_stroke_width_to_length_ratio=9).scale(1.4)
        arrow_6 = Arrow(result[2], circle_1,  color=ORANGE)
        self.play(FadeIn(arrow_5), FadeIn(arrow_6))
        self.wait(3)
