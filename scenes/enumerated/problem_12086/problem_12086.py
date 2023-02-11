from manim import LEFT, UP, DOWN, RIGHT
from manim import FadeIn, FadeOut, Write, Wiggle
from manim import AnimationGroup, VGroup, Group
from manim import Line, Circle, BraceBetweenPoints, MathTex
from manim import Axes, Scene
from manim import rate_functions, always_redraw, ValueTracker, ReplacementTransform, Restore
from manim import YELLOW, PURE_RED, ORANGE

from lib.constants import DEFAULT_SEGMENT_STROKE_WIDTH
from lib.qarakusiscene import TaskNumberBox
from lib.segment import Segment, SegmentEndmark
from objects import SimpleSVGMobject
from . import text


class Problem12086(Scene):
    def construct(self):
        # -------------------------------- Base ------------------------------ #
        """Ավտոմեքենան 2 քաղաքների միջև հեռավորությունն անցավ 3 օրում:
        Առաջին օրը նա անցավ ամբողջ ճանապարհի 35%-ը, իսկ երկրորդ օրը 120 կմ-ով ավելի:
        Երրորդ օրը նա անցավ 720 կմ: Գտնել քաղաքների միջև եղած հեռավորությունը:"""

        def get_point_x_on_line(start, end, percent):
            part = percent / 100
            start_x = start[0]
            end_x = end[0]
            return start_x + ((end_x - start_x) * part)

        def obj_movement(obj, move_to_point, run_time=None):
            if not run_time:
                return obj.animate(rate_func=rate_functions.linear).move_to(
                    move_to_point, aligned_edge=RIGHT).shift(0.05 * LEFT + 0.3 * UP)

            return obj.animate(rate_func=rate_functions.linear, run_time=run_time).move_to(
                move_to_point, aligned_edge=RIGHT).shift(0.05 * LEFT + 0.3 * UP)

        ax = Axes().set_opacity(0.3)

        road_y_coord = -1.5
        road_line_start_point = [-5.55, road_y_coord, 0]
        road_line_end_point = [6.63, road_y_coord, 0]

        flag_point_1 = [get_point_x_on_line(road_line_start_point, road_line_end_point, percent=35), road_y_coord, 0]
        flag_point_2_1 = [get_point_x_on_line(road_line_start_point, road_line_end_point, percent=70), road_y_coord, 0]
        flag_point_2_2 = [get_point_x_on_line(road_line_start_point, road_line_end_point, percent=74.4),
                          road_y_coord, 0]

        condition_point = ax.coords_to_point(-4, 4.6 )

        # -------------------------- Task number --------------------------- #
        task_number = TaskNumberBox(text.TASK_NUMBER_STR)
        self.play(FadeIn(task_number))
        self.wait(0.5)

        # --------------------------- Point 1 ------------------------------- #
        segment = Segment(road_line_start_point, road_line_end_point)
        self.play(FadeIn(segment))
        self.wait()

        # -------------------------- Point 2 -------------------------------- #
        car = SimpleSVGMobject('cars/car_2').move_to(road_line_start_point).scale(0.25).shift(0.8 * LEFT + 0.3 * UP)
        self.play(FadeIn(car))
        self.wait()

        # -------------------------- Point 3, 4 ------------------------------ #
        condition_1 = MathTex(text.FIRST_DAY).next_to(condition_point).scale(1.2)

        coord_x_t_1 = ValueTracker(road_line_start_point[0])
        colored_line_1 = always_redraw(
            lambda:Line(road_line_start_point, [coord_x_t_1.get_value(), road_y_coord, 0],
                        color=PURE_RED, stroke_width=5))

        self.play(FadeIn(colored_line_1))
        self.play(AnimationGroup(Write(condition_1, run_time=3),
                    AnimationGroup(
                        obj_movement(car, flag_point_1),
                        coord_x_t_1.animate(rate_func=rate_functions.linear).set_value(flag_point_1[0]),
                    run_time=5)))

        endmark_1 = SegmentEndmark(length=DEFAULT_SEGMENT_STROKE_WIDTH / 20).move_to(flag_point_1).set_z_index(+1)
        self.play(FadeIn(endmark_1))
        self.wait()

        # ------------------------ Point 5 --------------------------------- #
        brace_first_part = BraceBetweenPoints(road_line_start_point, flag_point_1,
                                              direction=DOWN).shift(0.15 * UP).save_state()
        percent_35 = MathTex(text.PERCENT_35).move_to(brace_first_part).shift(0.5 * DOWN).scale(1.2).save_state()

        self.play(Write(brace_first_part), Write(percent_35), run_time=2)
        self.wait()

        # ------------------------ Point 6, 7 ------------------------- #
        condition_2 = MathTex(text.SECOND_DAY).next_to(condition_point).scale(1.2).shift(0.75 * DOWN + 0.25 * LEFT)

        coord_x_t_2 = ValueTracker(flag_point_1[0])
        colored_line_2 = always_redraw(
            lambda: Line(flag_point_1, [coord_x_t_2.get_value(), road_y_coord, 0], color=ORANGE, stroke_width=5))

        self.play(FadeIn(colored_line_2))

        self.play(AnimationGroup(Write(condition_2, run_time=3),
                                 AnimationGroup(
                                     obj_movement(car, flag_point_2_2, run_time=5),
                                     coord_x_t_2.animate(rate_func=rate_functions.linear,
                                                         run_time=5).set_value(flag_point_2_2[0]))))
        self.wait()

        endmark_2 = endmark_1.copy().move_to(flag_point_2_2)
        endmark_3 = endmark_1.copy().move_to(flag_point_2_1)
        colored_line_2_2 = Line(flag_point_1, flag_point_2_1, color=PURE_RED, stroke_width=5)

        self.play(AnimationGroup(FadeIn(endmark_2), FadeIn(endmark_3), FadeIn(colored_line_2_2), lag_ratio=1))
        self.play(Wiggle(colored_line_2_2), Wiggle(colored_line_1))

        brace_second_second_part = BraceBetweenPoints(flag_point_2_1, flag_point_2_2,
                                                      direction=DOWN).shift(0.15 * UP).save_state()
        km_120 = MathTex(text.KM_120).move_to(brace_second_second_part).shift(0.5 * DOWN).scale(1.2).save_state()

        self.play(Write(brace_second_second_part), Write(km_120), run_time=2)
        self.wait()

        # -------------------------- Point 8, 9 ------------------------ #
        condition_3 = MathTex(text.THIRD_DAY).next_to(condition_point).scale(1.2).shift(1.4 * DOWN + 0.44 * LEFT)
        self.play(AnimationGroup(Write(condition_3, run_time=3),
                                 obj_movement(car, road_line_end_point, run_time=5)))
        car.save_state()

        brace_third_part = BraceBetweenPoints(flag_point_2_2, road_line_end_point,
                                              direction=DOWN).shift(0.15 * UP).save_state()
        km_720 = MathTex(text.KM_720).move_to(brace_third_part).shift(0.5 * DOWN).scale(1.2).save_state()
        self.play(Write(brace_third_part), Write(km_720), run_time=2)
        self.wait()

        # ----------------------- Point 10 --------------------- #
        self.play(Wiggle(colored_line_1), Wiggle(colored_line_2_2))
        brace_second_first_part = BraceBetweenPoints(flag_point_1, flag_point_2_1,
                                                     direction=DOWN).shift(0.15 * UP).save_state()
        percent_35_2 = percent_35.copy().move_to(brace_second_first_part).shift(0.5 * DOWN).save_state()

        self.play(Write(brace_second_first_part), Write(percent_35_2), run_time=2)
        self.wait()

        # --------------------- Point 11 ---------------------- #
        self.play(FadeOut(car), FadeOut(condition_1), FadeOut(condition_2), FadeOut(condition_3))
        self.wait()

        # ----------------- Point 12 --------------------------- #
        brace_whole = BraceBetweenPoints(road_line_start_point, road_line_end_point, direction=UP).shift(0.1 * DOWN)
        percent_100 = MathTex(text.PERCENT_100).move_to(brace_whole).shift(0.5 * UP).scale(1.2)

        self.play(Write(brace_whole), Write(percent_100))
        self.wait()

        # --------------------- Point 13 ---------------------- #
        brace_first_and_second_part = BraceBetweenPoints(road_line_start_point, flag_point_2_1,
                                                         direction=DOWN).shift(0.15 * UP)
        plus = MathTex(text.PLUS).move_to(brace_first_and_second_part).shift(0.5 * DOWN).scale(1.2)

        self.play(
            ReplacementTransform(Group(brace_first_part, brace_second_first_part), brace_first_and_second_part),
            percent_35.animate.shift(1.3 * RIGHT),
            percent_35_2.animate.shift(1.3 * LEFT),
            Write(plus))
        self.wait()

        # ----------------------- Point 14 -------------------- #
        percent_70 = MathTex(text.PERCENT_70).move_to(brace_first_and_second_part).shift(0.5 * DOWN).scale(1.2)

        self.play(ReplacementTransform(Group(percent_35, percent_35_2, plus), percent_70))
        self.wait()

        # ----------------------- Point 15 ------------------- #
        brace_third_and_fourth_part = BraceBetweenPoints(flag_point_2_1, road_line_end_point,
                                                         direction=DOWN).shift(0.15 * UP)
        plus_1 = MathTex(text.PLUS).move_to(brace_third_and_fourth_part).shift(0.5 * DOWN).scale(1.2)

        self.play(AnimationGroup(
                    AnimationGroup(
                        km_120.animate.shift(0.5 * RIGHT),
                        km_720.animate.shift(0.8 * RIGHT),
                        ReplacementTransform(Group(brace_second_second_part, brace_third_part),
                                             brace_third_and_fourth_part)),
                    Write(plus_1),
                    lag_ratio=0.7))
        self.wait()

        # ---------------------- Point 16 --------------------- #
        km_840 = MathTex(text.KM_840).move_to(brace_third_and_fourth_part).shift(0.5 * DOWN).scale(1.2)

        self.play(ReplacementTransform(Group(km_120, km_720, plus_1), km_840))
        self.wait()

        # --------------------- Point 17 ----------------------- #
        brace_30_percent_of_road = BraceBetweenPoints(flag_point_2_1, road_line_end_point,
                                                      direction=UP).shift(0.1 * DOWN)
        brace_70_percent_of_road = BraceBetweenPoints(road_line_start_point, flag_point_2_1,
                                                      direction=UP).shift(0.1 * DOWN)
        percent_30_up = MathTex(text.PERCENT_30).move_to(brace_30_percent_of_road).shift(0.5 * UP).scale(1.2)
        percent_70_up = MathTex(text.PERCENT_70).move_to(brace_70_percent_of_road).shift(0.5 * UP).scale(1.2)

        self.play(ReplacementTransform(brace_whole, VGroup(brace_70_percent_of_road, brace_30_percent_of_road)),
                  ReplacementTransform(percent_100, VGroup(percent_30_up, percent_70_up)))
        self.wait()

        # ------------------- Point 18 ------------------------- #
        road = MathTex(text.ROAD).next_to(condition_point).scale(1.2)
        solution_part_1 = MathTex(text.SOLUTION_PART_1).next_to(road).scale(1.2).shift(0.35 * RIGHT)
        self.play(AnimationGroup(Write(road), Write(solution_part_1), lag_ratio=1))
        self.wait()

        # -------------- Point 19 ----------------- #
        road_1 = road.copy().shift(0.7 * DOWN)
        solution_part_2 = MathTex(text.SOLUTION_PART_2).next_to(road_1).scale(1.2).shift(0.35 * RIGHT)
        self.play(AnimationGroup(Write(road_1), Write(solution_part_2), lag_ratio=1))
        self.wait()

        # ------------------ Point 20 -------------------------- #
        self.play(AnimationGroup(FadeOut(Group(road, road_1)),
                                 Group(solution_part_1, solution_part_2).animate.shift(2 * LEFT),
                                 lag_ratio=0.6))
        self.wait()

        # ------------------- Point 21 ---------------------- #
        solution_part_3 = MathTex(text.SOLUTION_PART_3).next_to(condition_point).scale(1.2).shift(1.4 * DOWN)
        result = MathTex(text.KM_2800).next_to(solution_part_3).scale(1.2).shift(0.35 * RIGHT, 0.08 * DOWN)
        self.play(Write(VGroup(solution_part_3, result)))
        self.wait()

        # -------------------- Point 22 --------------------- #
        self.play(FadeOut(Group(brace_30_percent_of_road,
                                brace_70_percent_of_road,
                                percent_30_up,
                                percent_70_up)))
        self.wait()

        self.play(AnimationGroup(
            FadeOut(Group(percent_70,
                          km_840,
                          brace_first_and_second_part,
                          brace_third_and_fourth_part)),
            AnimationGroup(
                Restore(car),
                Restore(brace_first_part),
                Restore(brace_second_first_part),
                Restore(brace_second_second_part),
                Restore(brace_third_part),
                Restore(percent_35),
                Restore(percent_35_2),
                Restore(km_120),
                Restore(km_720)),
            lag_ratio=0.1))
        self.wait()

        # ------------------- Point 23 --------------------- #
        self.play(result.animate.shift(0.45 * RIGHT).scale(1.5))
        circle = Circle(color=YELLOW).surround(result)
        self.play(Write(circle))

        self.wait(3)
