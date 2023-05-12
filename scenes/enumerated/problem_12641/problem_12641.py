from manim import LEFT, UP, DOWN, RIGHT, DL, UL, DR, UR, PI, ORIGIN
from manim import FadeIn, Write, FadeOut
from manim import Group, VGroup, AnimationGroup
from manim import MathTex, Rectangle, Line, Axes, Circle, CurvedArrow, TAU, ArcBetweenPoints, Arrow, Dot
from manim import ReplacementTransform
from manim import ORANGE, BLUE, PURE_RED, YELLOW, GREEN, BLACK

from qarakusiscene import QarakusiScene
from objects import SimpleSVGMobject
from . import text


class Problem12641(QarakusiScene):
    """հետհաշվարկով գտնել մտապահած թիվը"""
    def construct(self):
        # -------------- Base ------------ #
        ax = Axes()
        circle_point = [-7.1, 2, 0]
        solution_point = [-0, 2, 0]
        MathTex.set_default(font_size=80)
        self.add_task_number(text=text.TASK_NUMBER_STR)
        # self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        #conditions
        conditions = MathTex(*text.CONDITIONS).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN).scale(0.9)
        self.play(AnimationGroup(Write(conditions), lag_ratio=1, run_time=8))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        self.play(conditions.animate(run_time=3).shift(2.8 * RIGHT + UP).scale(0.7))
        self.wait()
        check_marks = [SimpleSVGMobject('check').scale(0.25).next_to(conditions[i],
                                                                    LEFT,
                                                                    buff=0.02) for i in range(len(conditions))]

        circle_1 = Circle(radius=0.5, color=PURE_RED, fill_opacity=1).next_to(circle_point)
        operation_1 = MathTex(text.OPERATION_1).next_to(circle_1)
        circle_2 = circle_1.copy().set_color(YELLOW).next_to(operation_1)
        self.play(AnimationGroup(Write(circle_1), Write(operation_1), Write(circle_2), Write(check_marks[0]), lag_ratio=1))
        self.wait()

        circle_3_pos = circle_2.copy().next_to(circle_1, DOWN, buff=0.7)
        circle_3 = circle_2.copy()
        operation_2 = MathTex(text.OPERATION_2).next_to(circle_3_pos).shift(0.3 * RIGHT)
        circle_4 = circle_2.copy().next_to(operation_2).set_color(BLUE)
        # arrow_1 = Arrow(circle_2.get_critical_point(DOWN),
        #                 circle_3_pos.get_critical_point(UR),
        #                 color=YELLOW)

        point_1 = circle_2.get_critical_point(DOWN)
        point_2 = point_1 + 0.5 * LEFT + 0.2 * DOWN
        point_4 = circle_3_pos.get_critical_point(UP)
        point_3 = point_4 + 0.7 * RIGHT + 0.4 * UP
        dot_1 = Dot(point_3, radius=0.01)
        dot_2 = Dot(point_2, radius=0.01)

        arc_1 = ArcBetweenPoints(point_1, point_2, radius=-0.8)
        line_1 = Line(point_2, point_3)
        curved_arrow_1 = CurvedArrow(point_3, point_4, angle=TAU / 12)
        arrow_1 = VGroup(arc_1, line_1, curved_arrow_1, dot_1, dot_2).set_color(YELLOW)

        self.play(AnimationGroup(Write(arrow_1),
                                 circle_3.animate.move_to(circle_3_pos),
                                 Write(operation_2),
                                 Write(circle_4),
                                 Write(check_marks[1]),
                                 lag_ratio=1))
        self.wait()

        circle_5_pos = circle_4.copy().next_to(circle_3_pos, DOWN, buff=0.7)
        circle_5 = circle_4.copy()
        operation_3 = MathTex(text.OPERATION_3).next_to(circle_5_pos)
        circle_6 = circle_2.copy().next_to(operation_3).set_color(GREEN)
        # arrow_2 = Arrow(circle_4.get_critical_point(DOWN),
        #                 circle_5_pos.get_critical_point(UR),
        #                 color=BLUE)
        point_1 = circle_4.get_critical_point(DOWN)
        point_2 = point_1 + 0.5 * LEFT + 0.2 * DOWN
        point_4 = circle_5_pos.get_critical_point(UP)
        point_3 = point_4 + 0.7 * RIGHT + 0.4 * UP
        dot_1 = Dot(point_3, radius=0.01)
        dot_2 = Dot(point_2, radius=0.01)

        arc_1 = ArcBetweenPoints(point_1, point_2, radius=-0.8)
        line_1 = Line(point_2, point_3)
        curved_arrow_1 = CurvedArrow(point_3, point_4, angle=TAU / 12)
        arrow_2 = VGroup(arc_1, line_1, curved_arrow_1, dot_1, dot_2).set_color(BLUE)

        self.play(AnimationGroup(Write(arrow_2),
                                 circle_5.animate.move_to(circle_5_pos),
                                 Write(operation_3),
                                 Write(circle_6),
                                 Write(check_marks[2]),
                                 lag_ratio=1))
        self.wait()

        circle_7_pos = circle_4.copy().next_to(circle_5_pos, DOWN, buff=0.7)
        circle_7 = circle_6.copy()
        operation_4 = MathTex(*text.OPERATION_4).next_to(circle_7_pos).shift(0.45 * RIGHT)
        # arrow_3 = Arrow(circle_6.get_critical_point(DOWN),
        #                 circle_7_pos.get_critical_point(UR),
        #                 color=GREEN)
        point_1 = circle_6.get_critical_point(DOWN)
        point_2 = point_1 + 0.5 * LEFT + 0.2 * DOWN
        point_4 = circle_7_pos.get_critical_point(UP)
        point_3 = point_4 + 0.7 * RIGHT + 0.4 * UP
        dot_1 = Dot(point_3, radius=0.01)
        dot_2 = Dot(point_2, radius=0.01)

        arc_1 = ArcBetweenPoints(point_1, point_2, radius=-0.8)
        line_1 = Line(point_2, point_3)
        curved_arrow_1 = CurvedArrow(point_3, point_4, angle=TAU / 12)
        arrow_3 = VGroup(arc_1, line_1, curved_arrow_1, dot_1, dot_2).set_color(GREEN)

        self.play(AnimationGroup(Write(arrow_3),
                                 circle_7.animate.move_to(circle_7_pos),
                                 Write(operation_4[0]),
                                 Write(check_marks[3]),
                                 Write(operation_4[1]),
                                 Write(check_marks[4]),
                                 lag_ratio=1))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        self.play(FadeOut(*conditions), FadeOut(*check_marks))
        self.wait()

        solution_1 = MathTex(text.SOLUTION_1).next_to(solution_point)
        solution_2 = MathTex(text.SOLUTION_2).next_to(solution_1, DOWN, buff=0.5, aligned_edge=LEFT)
        solution_3 = MathTex(text.SOLUTION_3).next_to(solution_2, DOWN, buff=0.5, aligned_edge=LEFT)
        solution_4 = MathTex(text.SOLUTION_4).next_to(solution_3, DOWN, buff=0.5, aligned_edge=LEFT)

        nums = MathTex(*text.NUMS, color=BLACK)

        nums[0].move_to(circle_7_pos)
        nums[1].move_to(circle_6)
        nums[2].move_to(circle_5_pos)
        nums[3].move_to(circle_4)
        nums[4].move_to(circle_3_pos)
        nums[5].move_to(circle_2)
        nums[6].move_to(circle_1)

        self.play(Write(solution_1))
        self.wait()
        # self.play(ReplacementTransform(circle_7, nums[0]))
        # self.play(ReplacementTransform(circle_6, nums[1]))
        self.play(Write(nums[0]), Write(nums[1]))
        self.wait()

        self.play(Write(solution_2))
        self.wait()
        # self.play(ReplacementTransform(circle_5, nums[2]))
        # self.play(ReplacementTransform(circle_4, nums[3]))
        self.play(Write(nums[2]), Write(nums[3]))
        self.wait()

        self.play(Write(solution_3))
        self.wait()
        # self.play(ReplacementTransform(circle_3, nums[4]))
        # self.play(ReplacementTransform(circle_2, nums[5]))
        self.play(Write(nums[4]), Write(nums[5]))
        self.wait()

        self.play(Write(solution_4))
        self.wait()
        # self.play(ReplacementTransform(circle_1, nums[6]))
        self.play(Write(nums[6]))

        self.wait(3)
