from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeIn, FadeOut, Write
from manim import AnimationGroup, Group, VGroup
from manim import Line, MathTex
from manim import rate_functions, always_redraw, ValueTracker, Indicate
from manim import ORANGE

from movement_problems import down_brace_with_text, obj_movement
from movement_problems import Coordinate, CustomMovementScene
from constants import DEFAULT_SEGMENT_STROKE_WIDTH
from segment import Segment, SegmentEndmark
from objects import SimpleSVGMobject
from . import text


class Problem12695(CustomMovementScene):
    """Մեքենան անցավ ամբողջ ճանապարհի 2/5
       մասը, որից հետո մնաց գնալու 126 կմ։
       Գտնել ամբողք ճանապարհի երկարությունը։"""
    def construct(self):
        # -------------- Base ------------ #
        coord_y = -1
        start_point = [-5.55, coord_y, 0]
        end_point = [6.63, coord_y, 0]

        coordinate = Coordinate(start_point, end_point)

        flag_point_1, flag_point_2, flag_point_3, flag_point_4 = coordinate.divide_segment_into_equal_parts(5)
        half_3_part = coordinate.get_point_by_percent_on_segment(percent=50)
        half_4_part = coordinate.get_point_by_percent_on_segment(percent=70)
        half_5_part = coordinate.get_point_by_percent_on_segment(percent=90)

        condition_point = [0, 3.45, 0]

        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        # Road with endpoints
        segment = Segment(start_point, end_point)
        a = MathTex(text.A).move_to(start_point).scale(1.2).shift(0.25 * LEFT + 0.21 * DOWN)
        b = MathTex(text.B).move_to(end_point).scale(1.2).shift(0.25 * RIGHT + 0.21 * DOWN)
        self.play(FadeIn(a), FadeIn(segment), FadeIn(b))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        # FadeIn car
        car = SimpleSVGMobject('cars/car_2').move_to(start_point).scale(0.25).shift(0.8 * LEFT + 0.3 * UP)
        self.play(FadeIn(car))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).move_to(condition_point).scale(1.2)

        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        # divide the road into 5 equal parts
        end_mark_1 = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).set_z_index(+1).move_to(flag_point_1)
        end_mark_2 = end_mark_1.copy().move_to(flag_point_2)
        end_mark_3 = end_mark_1.copy().move_to(flag_point_3)
        end_mark_4 = end_mark_1.copy().move_to(flag_point_4)

        self.play(FadeIn(Group(end_mark_1, end_mark_2, end_mark_3, end_mark_4)))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        # car passed 2/5 of road
        coord_x_flag_point_2 = ValueTracker(start_point[0])
        colored_line_1 = always_redraw(
            lambda: Line(start_point, [coord_x_flag_point_2.get_value(), coord_y, 0],
                         color=ORANGE, stroke_width=5))

        self.play(FadeIn(colored_line_1))
        self.play(AnimationGroup(obj_movement(car, flag_point_2),
                                 coord_x_flag_point_2.animate(rate_func=rate_functions.linear).set_value(flag_point_2[0]),
                                 run_time=6))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        # brace for passed road
        brace_with_text_1 = down_brace_with_text(text=text.TWO_FIFTH_OF_ROAD, points=(start_point, flag_point_2))

        self.play(Write(VGroup(*brace_with_text_1)))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        condition_2 = MathTex(text.CONDITION_2).move_to(condition_point).scale(1.2).shift(0.75 * DOWN)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        # brace for other part of road
        brace_with_text_2 = down_brace_with_text(text=text.KM_126, points=(flag_point_2, end_point))

        self.play(Write(VGroup(*brace_with_text_2)))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        num_1 = MathTex(text.NUM_1).move_to(half_3_part).scale(2).shift(UP)
        num_2 = MathTex(text.NUM_2).move_to(half_4_part).scale(2).shift(UP)
        num_3 = MathTex(text.NUM_3).move_to(half_5_part).scale(2).shift(UP)
        num_group = VGroup(num_1, num_2, num_3)
        self.play(Write(num_group))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        # remove condition points
        self.play(FadeOut(condition_1), FadeOut(condition_2))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        solution_1 = MathTex(text.SOLUTION_PART_1).next_to(condition_point).scale(1.2).shift(2.735 * LEFT)
        self.play(Write(solution_1))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        solution_2 = MathTex(text.SOLUTION_PART_2).next_to(condition_point).scale(1.2).shift(0.75 * DOWN + 2.5 * LEFT)
        scale_group = VGroup(num_group, brace_with_text_2[1])
        self.play(AnimationGroup(Write(solution_2), Indicate(scale_group), lag_ratio=0.4))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        solution_3 = MathTex(text.SOLUTION_PART_3).next_to(condition_point).scale(1.2).shift(1.4 * DOWN + 5.81 * LEFT)
        self.play(Write(solution_3))

        self.wait(3)
