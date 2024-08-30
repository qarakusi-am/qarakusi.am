from manim import UP, DOWN, LEFT, RIGHT, ORIGIN, DR, UR, RED, BLUE
from manim import SurroundingRectangle, BraceBetweenPoints
from manim import FadeOut, Write, Create
from manim import ReplacementTransform, AnimationGroup, VGroup
from manim import MathTex

from segment import Segment, SegmentEndmark
from qarakusiscene import QarakusiScene
from . import text as t


class Problem13460(QarakusiScene):
    """Մաթեմյանները գնեցին 5 տուփ ոսպ և $6$ տուփ բրինձ՝ $14.95$ կգ ընդհանուր քաշով:
    Քանի՞ կիլոգրամ են գնել յուրաքանչյուրից, եթե հայտնի է, որ ոսպի տուփը $3$ անգամ թեթև է բրնձի տուփից:
    """
    def construct(self):
        screen_center = [0, 0, 0]
        segment_buff = 0.19
        self.add_task_number(text=t.TASK_NUMBER_STR)
        MathTex.set_default(font_size=t.default_font_size)
        # self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*t.CONDITION_1).move_to(screen_center, ORIGIN)
        self.wait()
        self.play(Write(condition_1), run_time=3)
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_2 = MathTex(t.CONDITION_2, font_size=55).next_to(condition_1, DOWN).shift(0.4 * DOWN)

        self.play(Write(condition_2), run_time=3)
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_3 = MathTex(t.CONDITION_3, color=RED).next_to(condition_2, DOWN, aligned_edge=LEFT).shift(0.4 * DOWN)
        self.play(Write(condition_3))
        self.wait()


        # -------------------------- Point 4 ------------------------------- #
        x, y, _ = condition_3.get_critical_point(DR)
        x += 0.4
        y += 0.2
        start_point = [x, y, 0]
        end_point = [x + 1, y, 0]
        segment_1 = Segment(start_point, end_point).set_color(RED)
        self.play(Create(segment_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        condition_4 = MathTex(t.CONDITION_4, color=BLUE).next_to(condition_3, DOWN).shift(0.2 * DOWN)
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        _, y1, _ = condition_4.get_critical_point(DR)
        y1 += 0.2
        start_point = [x, y1, 0]
        end_point = [x + 3, y1, 0]
        segment_2 = Segment(start_point, end_point).set_color(BLUE)
        self.play(AnimationGroup(Create(segment_2), runtime=3))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        grouped_segment_blue_1 = segment_1.copy().next_to(segment_2.get_critical_point(LEFT), RIGHT, buff=0).set_color(BLUE)
        grouped_segment_blue_2 = grouped_segment_blue_1.copy().next_to(grouped_segment_blue_1, RIGHT, buff=0)
        grouped_segment_blue_3 = grouped_segment_blue_1.copy().next_to(grouped_segment_blue_2, RIGHT, buff=0)
        segments_group_blue_1 = VGroup(grouped_segment_blue_1, grouped_segment_blue_2, grouped_segment_blue_3)
        self.play(ReplacementTransform(segment_1.copy(), segments_group_blue_1), run_time=1.5)
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        rectangle_1 = SurroundingRectangle(condition_1[0], corner_radius=0.2, buff=0.17)
        self.play(AnimationGroup(FadeOut(condition_2), Create(rectangle_1), lag_ratio=0), run_time=2)
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        start_point = [-5.0, 3.3, 0]
        end_point = [-4.0, 3.3, 0]
        grouped_segment_1 = Segment(start_point, end_point).set_color(RED)
        grouped_segment_2 = grouped_segment_1.copy().next_to(grouped_segment_1, DOWN, buff=segment_buff)
        grouped_segment_3 = grouped_segment_1.copy().next_to(grouped_segment_2, DOWN, buff=segment_buff)
        grouped_segment_4 = grouped_segment_1.copy().next_to(grouped_segment_3, DOWN, buff=segment_buff)
        grouped_segment_5 = grouped_segment_1.copy().next_to(grouped_segment_4, DOWN, buff=segment_buff)

        segments_group_red_1 = VGroup(
            grouped_segment_1,
            grouped_segment_2,
            grouped_segment_3,
            grouped_segment_4,
            grouped_segment_5,
        )
        self.play(
            AnimationGroup(
                FadeOut(rectangle_1),
                ReplacementTransform(condition_1[0], segments_group_red_1),
                lag_ratio=0.3
            ),
            run_time=2)
        self.wait(1)

        # -------------------------- Point 10 ------------------------------- #
        start_point = [-5.0, 3.3, 0]
        end_point = [-2.0, 3.3, 0]
        grouped_segment_1 = Segment(start_point, end_point).set_color(BLUE)
        grouped_segment_2 = grouped_segment_1.copy().next_to(grouped_segment_1, DOWN, buff=segment_buff)
        grouped_segment_3 = grouped_segment_1.copy().next_to(grouped_segment_2, DOWN, buff=segment_buff)
        grouped_segment_4 = grouped_segment_1.copy().next_to(grouped_segment_3, DOWN, buff=segment_buff)
        grouped_segment_5 = grouped_segment_1.copy().next_to(grouped_segment_4, DOWN, buff=segment_buff)
        grouped_segment_6 = grouped_segment_1.copy().next_to(grouped_segment_5, DOWN, buff=segment_buff)

        segments_group_blue_2 = VGroup(
            grouped_segment_1,
            grouped_segment_2,
            grouped_segment_3,
            grouped_segment_4,
            grouped_segment_5,
            grouped_segment_6,
        ).next_to(segments_group_red_1, DOWN, buff=0.25, aligned_edge=LEFT)

        self.play(
            AnimationGroup(
                FadeOut(condition_1[1]),
                ReplacementTransform(condition_1[2], segments_group_blue_2, run_time=2),
                run_time=3,
                lag_ratio=0.8,
            )
        )
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        segments_grouped_group = VGroup(*segments_group_red_1, *segments_group_blue_2)
        self.play(condition_1[3:].animate.next_to(segments_grouped_group, RIGHT), run_time=3)
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        brace_1 = BraceBetweenPoints(
            segments_grouped_group.get_critical_point(UR),
            segments_grouped_group.get_critical_point(DR),
            direction=RIGHT
        ).shift(0.17 * RIGHT)
        self.play(ReplacementTransform(condition_1[3], brace_1))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        segments_group_blue_3 = VGroup(
            *[grouped_segment_blue_1.copy().move_to(item) for item in segments_group_blue_2]
        )
        self.play(Write(segments_group_blue_3), run_time=1.5)
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        nums_1 = VGroup(
            *[MathTex(
                str(num), font_size=t.num_font_size).move_to(segments_group_red_1[num - 1]).shift(0.2 * UP) for num in range(1,6)
              ]
        )
        self.play(AnimationGroup(*[Write(num) for num in nums_1], lag_ratio=1))

        # -------------------------- Point 15 ------------------------------- #
        num_6 = MathTex('6', font_size=t.num_font_size).move_to(nums_1[4]).shift(0.55 * DOWN)
        num_7 = MathTex('7', font_size=t.num_font_size).move_to(num_6).shift(RIGHT)
        num_8 = MathTex('8', font_size=t.num_font_size).move_to(num_7).shift(RIGHT)

        num_9 = MathTex('9', font_size=t.num_font_size).move_to(num_6).shift(t.num_shift_down * DOWN)

        self.play(Write(num_6))
        self.play(Write(num_7))
        self.play(Write(num_8))
        self.play(Write(num_9))

        num_10 = MathTex('10', font_size=t.num_font_size).move_to(num_9).shift(RIGHT)
        num_11 = MathTex('11', font_size=t.num_font_size).move_to(num_10).shift(RIGHT)

        num_12 = MathTex('12', font_size=t.num_font_size).move_to(num_9).shift(t.num_shift_down * DOWN)
        num_13 = MathTex('13', font_size=t.num_font_size).move_to(num_12).shift(RIGHT)
        num_14 = MathTex('14', font_size=t.num_font_size).move_to(num_13).shift(RIGHT)

        num_15 = MathTex('15', font_size=t.num_font_size).move_to(num_12).shift(t.num_shift_down * DOWN)
        num_16 = MathTex('16', font_size=t.num_font_size).move_to(num_15).shift(RIGHT)
        num_17 = MathTex('17', font_size=t.num_font_size).move_to(num_16).shift(RIGHT)

        num_18 = MathTex('18', font_size=t.num_font_size).move_to(num_15).shift(t.num_shift_down * DOWN)
        num_19 = MathTex('19', font_size=t.num_font_size).move_to(num_18).shift(RIGHT)
        num_20 = MathTex('20', font_size=t.num_font_size).move_to(num_19).shift(RIGHT)

        num_21 = MathTex('21', font_size=t.num_font_size).move_to(num_18).shift(t.num_shift_down * DOWN)
        num_22 = MathTex('22', font_size=t.num_font_size).move_to(num_21).shift(RIGHT)
        num_23 = MathTex('23', font_size=t.num_font_size).move_to(num_22).shift(RIGHT)

        self.play(
            Write(num_10),
            Write(num_11),
            Write(num_12),
            Write(num_13),
            Write(num_14),
            Write(num_15),
            Write(num_16),
            Write(num_17),
            Write(num_18),
            Write(num_19),
            Write(num_20),
            Write(num_21),
            Write(num_22),
            Write(num_23),
        )
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        solution_1 = MathTex(t.SOLUTION_1).next_to(condition_1[4], DR).shift(0.5 * LEFT + 0.3 * DOWN)
        self.play(Write(solution_1))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        solution_2 = MathTex(t.SOLUTION_2).next_to(solution_1, DOWN, aligned_edge=LEFT).shift(0.05 * LEFT)
        self.play(Write(solution_2))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        solution_3 = MathTex(t.SOLUTION_3, color=RED).next_to(segment_1)
        self.play(Write(solution_3))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        solution_4 = MathTex(t.SOLUTION_4, color=BLUE).next_to(segment_2)
        self.play(Write(solution_4))
        self.wait(3)
