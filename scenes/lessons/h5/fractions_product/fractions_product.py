from movement_problems import down_brace_with_text, obj_movement, up_brace_with_text, Coordinate
from qarakusiscene import QarakusiScene
from constants import DEFAULT_SEGMENT_STROKE_WIDTH
from segment import Segment, SegmentEndmark
from objects import SimpleSVGMobject
from . import text

from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeIn, FadeOut, Write
from manim import AnimationGroup, Group, VGroup
from manim import Line, MathTex
from manim import ReplacementTransform, Wiggle, UL, DR, Rectangle, BraceBetweenPoints
from manim import BLUE, RED, YELLOW


class FractionsProduct(QarakusiScene):
    """Հ5 – կոտորակների արտադրյալը"""
    def construct(self):
        coord_y = -2.2
        start_point = [-6.5, coord_y, 0]
        end_point = [6.5, coord_y, 0]
        screen_center = [0, 0, 0]

        # coordinate = Coordinate(start_point, end_point)
        #
        # divide_into_12_parts = coordinate.divide_segment_into_equal_parts(12)
        # first_point = coordinate.get_point_by_percent_on_segment(percent=33.333333)
        # second_point = coordinate.get_point_by_percent_on_segment(percent=58.333333)

        condition_point = [-2, 3, 0]


        MathTex.set_default(font_size=70)
        self.add_task_number(text=text.TASK_NUMBER_STR)
        self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).move_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        condition_1_0 = condition_1[0].copy()
        self.play(condition_1_0.animate.next_to(condition_1[0], DOWN))
        condition_2 = MathTex(*text.CONDITION_2).next_to(condition_1_0)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        self.play(condition_2[1:].animate.next_to(condition_1), FadeOut(condition_2[0]), FadeOut(condition_1_0))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_1_2 = condition_1[2].copy()
        self.play(condition_1_2.animate.next_to(condition_1[0], DOWN))
        condition_3 = MathTex(*text.CONDITION_3).next_to(condition_1_2)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        cdot = condition_1[1].copy().next_to(condition_2[2])
        self.play(condition_3[1].animate.next_to(cdot), FadeOut(condition_1_2), FadeOut(condition_3[0]))
        self.play(Write(cdot))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        condition_4 = MathTex(text.CONDITION_4).to_edge().shift(0.5 * DOWN)
        self.play(Write(condition_4))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        solution_group_1 = VGroup(condition_2[2], cdot, condition_3[1])
        self.play(solution_group_1.animate(run_time=2).next_to(condition_4, DOWN).shift(0.7 * LEFT))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_5 = MathTex(*text.CONDITION_5).next_to(solution_group_1)
        self.play(Write(condition_5[0]))
        self.wait()
        self.play(Write(condition_5[1]))
        self.wait()
        self.play(Write(condition_5[2]))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        # FadeOut condition points
        # self.play(FadeOut(Group(condition_1_0, condition_2_0, part, part_copy, condition_3)), run_time=1)

        # -------------------------- Point 10 ------------------------------- #
        # Condition transformation to solution
        # self.play(AnimationGroup(condition_1.animate.shift(4.6 * LEFT),
        #                          condition_2.animate.shift(3.6 * LEFT + 1.4 * UP),
        #                          lag_ratio=0.2),
        #           run_time=2)
        # plus = MathTex(text.PLUS).next_to(condition_1).scale(1.2)
        # equal = MathTex(text.EQUAL).next_to(condition_2).scale(1.2).shift(0.1 * RIGHT)
        #
        # self.play(AnimationGroup(Write(plus), Write(equal), lag_ratio=1))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #

        # self.play(ReplacementTransform(Group(brace_text_1, brace_1), VGroup(*part_4, *part_3, *part_5)))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #

        # self.play(Write(solution_1))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #

        # self.play(AnimationGroup(Write(solution_2), Write(five_twelfth), lag_ratio=1, run_time=2))
        self.wait()


        # -------------------------- Point 14 ------------------------------- #
        # -------------------------- Point 15 ------------------------------- #

        # self.play(Write(line), Write(line_2))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #

        # self.play(AnimationGroup(Write(result_0), Write(result), lag_ratio=1))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #

        # self.play(Write(rectangle))

        self.wait(3)
