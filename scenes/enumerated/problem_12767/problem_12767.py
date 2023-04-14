from manim import LEFT, UP, DOWN, RIGHT, DL, UL, DR, UR, PI
from manim import FadeIn, FadeOut, Write, Create
from manim import AnimationGroup, Group, VGroup
from manim import MathTex, DashedLine, Rectangle, Line, BraceBetweenPoints
from manim import rate_functions, ReplacementTransform
from manim import PURE_RED, YELLOW

from movement_problems import Coordinate
from constants import DEFAULT_SEGMENT_STROKE_WIDTH
from qarakusiscene import QarakusiScene
from segment import SegmentEndmark
from objects import SimpleSVGMobject
from . import text


class Problem12767(QarakusiScene):
    """տրված է ուղղանկյան պարագիծն ու լայնությունը:"""
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
        self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        # show rectangle
        rectangle_template = Rectangle(height=2.5, width=5)
        perimeter = MathTex(*text.PERIMETER).move_to(rectangle_template)

        top_line = Line(rectangle_template.get_corner(UL), rectangle_template.get_corner(UR))
        bottom_line = Line(rectangle_template.get_corner(DR), rectangle_template.get_corner(DL))

        right_line = Line(rectangle_template.get_corner(UR), rectangle_template.get_corner(DR))
        left_line = Line(rectangle_template.get_corner(DL), rectangle_template.get_corner(UL))
        rectangle_group = VGroup(top_line, bottom_line, left_line, right_line)

        self.play(FadeIn(top_line), FadeIn(right_line), FadeIn(bottom_line), FadeIn(left_line))
        self.play(Write(perimeter))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        length_sides = VGroup(*[MathTex(text.LENGTH_SIDE).next_to(*pos) for pos in ((left_line, LEFT), (right_line, RIGHT))])
        self.play(Group(right_line, left_line).animate.set_color(YELLOW), FadeIn(*length_sides))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        rectangle_group_copy = rectangle_group.copy()
        self.play(FadeIn(rectangle_group_copy))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        self.play(Group(perimeter, rectangle_group).animate.shift(4.1 * RIGHT),
                  Group(length_sides, rectangle_group_copy).animate.shift(3 * LEFT))
        left_line_shift = (0.70 * DOWN)
        right_line_shift = (2.2 * DOWN + 5 * LEFT)
        left_line_invisible = rectangle_group_copy[2].copy().shift(left_line_shift + 0.4 * UP).rotate(0.5 * PI)
        right_line_invisible = rectangle_group_copy[3].copy().shift(right_line_shift + 0.4 * UP).rotate(0.5 * PI)

        self.play(rectangle_group_copy[0].animate.shift(1 * UP + 1.25 * LEFT),
                  rectangle_group_copy[1].animate.shift(2 * UP + 1.25 * LEFT),
                  rectangle_group_copy[2].animate.shift(left_line_shift).rotate(0.5 * PI),
                  rectangle_group_copy[3].animate.shift(right_line_shift).rotate(0.5 * PI),
                  length_sides[0].animate.move_to(left_line_invisible),
                  length_sides[1].animate.move_to(right_line_invisible))
        self.wait()

        end_mark_pattern = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).set_z_index(+1)
        left_end_marks = VGroup(*[end_mark_pattern.copy().move_to(point.get_critical_point(LEFT)) for point in rectangle_group_copy])
        right_end_marks = VGroup(*[end_mark_pattern.copy().move_to(point.get_critical_point(RIGHT)) for point in rectangle_group_copy])

        brace = BraceBetweenPoints(right_end_marks[0].get_critical_point(UR),
                                   [rectangle_group_copy[0].get_critical_point(RIGHT)[0],
                                    right_end_marks[3].get_critical_point(DR)[1], 0],
                                   direction=RIGHT)

        self.play(
            Write(VGroup(*left_end_marks, *right_end_marks)),
            perimeter.animate.shift(5.1 * LEFT),
            ReplacementTransform(perimeter[0], brace))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        self.play(brace.animate.scale(0.40).set_stroke_width(2.7).shift(1.5 * UP),
                  perimeter[1].animate.shift(1.5 * UP),
                  rectangle_group.animate.shift(2 * DOWN))

        num_1 = MathTex(text.NUM_1).next_to(perimeter[1])
        self.play(Write(num_1))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        num_2 = MathTex(text.NUM_2).next_to(num_1)
        self.play(Write(num_2))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        num_3 = VGroup(*[MathTex(text.NUM_3).next_to(pos, UP) for pos in rectangle_group_copy[:2]])
        self.play(ReplacementTransform(num_2, num_3))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        self.play(num_3[0].copy().animate.next_to(rectangle_group[0], UP))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        result = MathTex(*text.RESULT).arrange(DOWN).move_to(rectangle_group)
        self.play(Write(result))
        self.wait(3)
