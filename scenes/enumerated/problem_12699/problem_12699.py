from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeIn, FadeOut, Write
from manim import AnimationGroup, Group, VGroup
from manim import Line, MathTex
from manim import ReplacementTransform, Wiggle, UL, DR, Rectangle, BraceBetweenPoints
from manim import BLUE, RED, YELLOW

from movement_problems import down_brace_with_text, obj_movement, up_brace_with_text
from movement_problems import Coordinate, CustomMovementScene
from constants import DEFAULT_SEGMENT_STROKE_WIDTH
from segment import Segment, SegmentEndmark
from objects import SimpleSVGMobject
from . import text


class Problem12699(CustomMovementScene):
    """Դուբին առաջին օրը կարդաց գրքի 1/3 մասը, իսկ երկրորդ օրը՝ 1/4 մասը։
       Քանի՞ էջից է բաղկացած գիրքը, եթե մնացել է կարդալու 25 էջ։"""
    def construct(self):
        coord_y = -2.2
        start_point = [-6.5, coord_y, 0]
        end_point = [6.5, coord_y, 0]
        screen_center = [0, 0, 0]

        coordinate = Coordinate(start_point, end_point)

        divide_into_12_parts = coordinate.divide_segment_into_equal_parts(12)
        first_point = coordinate.get_point_by_percent_on_segment(percent=33.333333)
        second_point = coordinate.get_point_by_percent_on_segment(percent=58.333333)

        condition_point = [0, 3.40, 0]

        self.add_task_number(text=text.TASK_NUMBER_STR)

        # -------------------------- Point 1 ------------------------------- #
        # Show book
        book = SimpleSVGMobject('colored_book_2').move_to(screen_center).scale(1.5).shift(0.8 * LEFT + 0.3 * UP)
        self.play(FadeIn(book))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        # Transform book to segment
        segment = Segment(start_point, end_point)
        self.play(ReplacementTransform(book, segment))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        condition_1_0 = MathTex(text.CONDITION_1_0).move_to(condition_point).scale(1.2).shift(0.2 * DOWN + 1.25 * LEFT)
        condition_1 = MathTex(text.CONDITION_1, substrings_to_isolate="3").next_to(condition_1_0).scale(1.2)
        condition_1.set_color_by_tex('3', RED)
        part = MathTex(text.PART).next_to(condition_1).scale(1.2).shift(0.15 * RIGHT)

        self.play(AnimationGroup(Write(condition_1_0), Write(condition_1), Write(part), lag_ratio=0.8))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        # Paint red the 1/3 part
        first_part = (start_point, first_point)
        colored_line_1 = Line(*first_part, color=RED, stroke_width=5)
        brace_with_text_1 = down_brace_with_text(text=text.BRACE_TEXT_1, points=first_part, text_shift=(0.8 * DOWN))
        end_mark_1 = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).set_z_index(+1).move_to(first_point)

        self.play(FadeIn(Group(colored_line_1, end_mark_1, *brace_with_text_1)), run_time=2)
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        condition_2_0 = MathTex(text.CONDITION_2_0).move_to(condition_point).scale(1.2).shift(1.6 * DOWN + 1.25 * LEFT)
        condition_2 = MathTex(text.CONDITION_2, substrings_to_isolate="4").next_to(condition_2_0).scale(1.2)
        condition_2.set_color_by_tex('4', BLUE)
        part_copy = part.copy().next_to(condition_2)

        self.play(AnimationGroup(Write(condition_2_0), Write(condition_2), Write(part_copy), lag_ratio=0.8))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        # Paint blue the 1/4 part
        second_part = (first_point, second_point)
        colored_line_2 = Line(*second_part, color=BLUE, stroke_width=5)
        brace_with_text_2 = down_brace_with_text(text=text.BRACE_TEXT_2, points=second_part, text_shift=(0.8 * DOWN))
        end_mark_2 = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).set_z_index(+1).move_to(second_point)

        self.play(FadeIn(Group(colored_line_2, end_mark_2, *brace_with_text_2)), run_time=2)
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).move_to(condition_point).scale(1.2).shift(0.2 * LEFT + 2.7 * DOWN)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        third_part = (second_point, end_point)
        colored_line_3 = Line(*third_part, color=YELLOW, stroke_width=5)
        text_without_brace = down_brace_with_text(text=text.PAGES_25, points=third_part, text_shift=(0.76 * DOWN))

        self.play(FadeIn(Group(colored_line_3, text_without_brace[1])), run_time=2)
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        # FadeOut condition points
        self.play(FadeOut(Group(condition_1_0, condition_2_0, part, part_copy, condition_3)), run_time=1)

        # -------------------------- Point 10 ------------------------------- #
        # Condition transformation to solution
        self.play(AnimationGroup(condition_1.animate.shift(4.6 * LEFT),
                                 condition_2.animate.shift(3.6 * LEFT + 1.4 * UP),
                                 lag_ratio=0.2),
                  run_time=2)
        plus = MathTex(text.PLUS).next_to(condition_1).scale(1.2)
        equal = MathTex(text.EQUAL).next_to(condition_2).scale(1.2).shift(0.1 * RIGHT)

        self.play(AnimationGroup(Write(plus), Write(equal), lag_ratio=1))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        # divide the progress into 12 equal parts and transfer them into corresponding parts
        end_mark_list = []
        end_mark_example = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).set_z_index(+1)
        for point in divide_into_12_parts:
            end_mark_list.append(end_mark_example.copy().move_to(point))

        self.play(FadeIn(Group(*end_mark_list)))
        self.play(Wiggle(Group(*end_mark_list)))
        self.wait()

        brace_1 = BraceBetweenPoints(start_point, end_point, direction=UP).shift(0.1 * DOWN)
        brace_text_1 = MathTex(text.BRACE_TEXT_3).move_to(brace_1).shift(0.4 * UP).scale(1.2)
        self.play(FadeIn(Group(brace_1, brace_text_1)))
        self.wait()

        part_4 = up_brace_with_text(text.PART_4, (start_point, first_point), color=RED)
        part_3 = up_brace_with_text(text.PART_3, (first_point, second_point), color=BLUE)
        part_5 = up_brace_with_text(text.PART_5, (second_point, end_point), color=YELLOW)

        self.play(ReplacementTransform(Group(brace_text_1, brace_1), VGroup(*part_4, *part_3, *part_5)))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        solution_1 = MathTex(text.SOLUTION_PART_1).next_to(equal).scale(1.2).shift(0.65 * RIGHT)
        solution_1[0][0:1].set_color(RED)
        solution_1[0][5:6].set_color(BLUE)
        solution_1[0][10:11].set_color(RED)
        solution_1[0][12:13].set_color(BLUE)

        self.play(Write(solution_1))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        solution_2 = MathTex(text.SOLUTION_PART_2).move_to(solution_1).scale(1.2).shift(1.5 * DOWN + 1.6 * LEFT)
        five_twelfth = MathTex(text.FIVE_TWELFTH, color=YELLOW).next_to(solution_2).scale(1.2).shift(0.1 * RIGHT)

        self.play(AnimationGroup(Write(solution_2), Write(five_twelfth), lag_ratio=1, run_time=2))
        self.wait()

        five_twelfth_copy = five_twelfth.copy()
        parts_group = part_5[1], part_4[1], part_3[1]
        self.play(AnimationGroup(FadeOut(Group(*parts_group)),
                                 five_twelfth_copy.animate.move_to(part_5[1]).shift(0.3 * UP),
                                 lag_ratio=1))

        # -------------------------- Point 14 ------------------------------- #
        # -------------------------- Point 15 ------------------------------- #
        solution_4 = MathTex(text.SOLUTION_PART_4).move_to(solution_2).scale(1.2).shift(1.5 * DOWN + 1.3 * LEFT)
        self.play(Write(solution_4))
        self.wait()
        line = Line(solution_4[0][16:18].get_critical_point(UL), solution_4[0][16:18].get_critical_point(DR), color=RED)
        line_2 = Line(solution_4[0][22:23].get_critical_point(UL), solution_4[0][22:23].get_critical_point(DR), color=RED)
        self.play(Write(line), Write(line_2))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        result_0 = MathTex(text.RESULT_0).next_to(solution_4).scale(1.2).shift(0.2 * RIGHT)
        result = MathTex(text.RESULT).next_to(result_0).scale(1.2).shift(0.1 * RIGHT)

        self.play(AnimationGroup(Write(result_0), Write(result), lag_ratio=1))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        self.play(result.animate.shift(0.3 * RIGHT).scale(1.5))
        rectangle = Rectangle().surround(result)
        self.play(Write(rectangle))

        self.wait(3)
