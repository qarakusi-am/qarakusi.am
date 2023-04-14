from manim import LEFT, UP, DOWN, RIGHT, DL, UL, DR, UR
from manim import FadeIn, FadeOut, Write
from manim import AnimationGroup, Group, VGroup
from manim import MathTex, DashedLine
from manim import rate_functions, ReplacementTransform
from manim import PURE_RED, YELLOW

from movement_problems import Coordinate
from qarakusiscene import QarakusiScene
from segment import Segment
from objects import SimpleSVGMobject
from . import text


class Problem10620(QarakusiScene):
    """A և B քաղաքների միջև հեռավորությունը բեռնատարն անցնում է 5 ժամում:
    Եթե նա շարժվեր 16կմ/ժ ավելի մեծ արագությամբ, ապա այդ ճանապարհը կանցներ
    4 ժամում: Գտնել բեռնատարի արագությունը:"""
    def construct(self):
        # -------------- Base ------------ #
        coord_y = -3.3
        start_point = [-5.55, coord_y, 0]
        end_point = [6.63, coord_y, 0]

        new_road_start_point = [-5.55, -2, 0]

        condition_point = [0, 3.45, 0]
        condition_point_left = [-7, 0.8, 0]

        MathTex.set_default(font_size=60)
        self.add_task_number(text=text.TASK_NUMBER_STR)

        coordinate = Coordinate(start_point, end_point)
        flag_point_1, flag_point_2, flag_point_3, flag_point_4 = coordinate.divide_segment_into_equal_parts(5)
        one_fifth = coordinate.get_point_by_percent_on_segment(percent=5)


        # -------------------------- Point 1 ------------------------------- #
        # Road with endpoints and truck
        main_segment = Segment(start_point, end_point)
        a = MathTex(text.A).move_to(start_point).shift(0.25 * LEFT + 0.21 * DOWN)
        b = MathTex(text.B).move_to(end_point).shift(0.25 * RIGHT + 0.21 * DOWN)
        truck = SimpleSVGMobject('cars/car_5').move_to(start_point).scale(0.365).shift(0.78 * LEFT + 0.4 * UP)
        self.play(FadeIn(a), FadeIn(main_segment), FadeIn(b), FadeIn(truck))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_2 = MathTex(text.CONDITION_2).next_to(condition_1, DOWN)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).next_to(condition_point_left).shift(text.condition_3_shift * RIGHT)
        segment_1 = Segment(start_point, flag_point_1).next_to(condition_3).set_color(YELLOW)
        self.play(Write(condition_3))
        self.play(FadeIn(segment_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        positions = (start_point, flag_point_1, flag_point_2, flag_point_3, flag_point_4)
        self.play(AnimationGroup(
            *[segment_1.copy().animate(rate_func=rate_functions.linear).next_to(pos, buff=0) for pos in positions],
            lag_ratio=0.2,
            run_time=3),
            FadeOut(truck))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        segment_2 = segment_1.copy()
        segment_2.next_to(segment_1, DOWN, aligned_edge=LEFT).shift(0.4 * DOWN).set_color(YELLOW)
        segment_3 = Segment(start_point, one_fifth).next_to(segment_2, buff=0).set_color(PURE_RED)
        num_1 = MathTex(text.NUM_1).move_to(segment_3).shift(0.4 * UP)

        self.play(FadeIn(segment_2))
        self.play(FadeIn(segment_3))
        self.play(Write(num_1))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        segment_group = VGroup(segment_2, segment_3, num_1)
        segments_position = VGroup(*[segment_group[:2].copy() for _ in range(4)]).arrange(buff=0).next_to(new_road_start_point, buff=0)

        segments = VGroup(*[segment_group.copy() for _ in range(4)])
        self.play(AnimationGroup(*[segments[i].animate.move_to(segments_position[i]) for i in range(4)], lag_ratio=1, run_time=5))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        # dashed lines
        dashed_line_1 = DashedLine(segments[0][0].get_critical_point(DL), main_segment.get_critical_point(UL)).set_z_index(-1)
        dashed_line_2 = DashedLine(segments[3][1].get_critical_point(DR), main_segment.get_critical_point(UR)).set_z_index(-1)
        self.play(Write(dashed_line_1), Write(dashed_line_2), run_time=1.5)
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        self.play(*[item[1:].animate.shift(0.7 * UP) for item in segments])
        self.play(segments[1][0].animate.next_to(segments[0][0], buff=0),
                  segments[-2][1:].animate.next_to(segments[-1][1:], LEFT, buff=0))
        self.play(segments[2][0].animate.next_to(segments[1][0], buff=0),
                  segments[-3][1:].animate.next_to(segments[-2][1:], LEFT, buff=0))
        self.play(segments[3][0].animate.next_to(segments[2][0], buff=0),
                  segments[-4][1:].animate.next_to(segments[-3][1:], LEFT, buff=0))
        self.play(*[item[1:].animate.shift(0.7 * DOWN) for item in segments])
        self.wait()

        dashed_line_3 = DashedLine(segments[0][1].get_critical_point(DL), flag_point_4).set_z_index(-1)
        self.play(Write(dashed_line_3))

        # -------------------------- Point 10 ------------------------------- #
        nums_group = Group(segments[0][2], segments[1][2], segments[2][2], segments[3][2])
        num_2 = MathTex(text.NUM_2).move_to(nums_group)
        self.play(ReplacementTransform(nums_group, num_2))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        num_2_copy = num_2.copy()
        self.play(num_2_copy.animate.shift(1 * DOWN))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        num_2_copy_copy = num_2_copy.copy()
        km_h = MathTex(text.KM_H).move_to(segment_1).shift(0.4 * UP + 0.4 *  RIGHT)
        self.play(AnimationGroup(
            num_2_copy_copy.animate(run_time=1.5).move_to(segment_1).shift(0.4 * UP + text.result_shit * LEFT),
            Write(km_h),
            lag_ratio=0.6))
        self.wait(3)
