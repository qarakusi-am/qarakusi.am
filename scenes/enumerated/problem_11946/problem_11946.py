from . import text

from objects import SimpleSVGMobject
from qarakusiscene import TaskNumberBox
from lib.segment import Segment

from manim import Scene
from manim import LEFT, UP, DOWN, RIGHT
from manim import AnimationGroup, FadeIn, FadeOut, Write, ReplacementTransform, Create
from manim import MathTex, VGroup
from manim import Line, Dot, DashedLine
from manim import Axes
from manim import rate_functions, always_redraw, ValueTracker, BraceBetweenPoints, Brace
from manim import YELLOW, BLUE_D
from manim import PI, OUT


class Problem11946(Scene):

    def construct(self):
        # --------------------------------------------- Base -------------------------------------- #
        def get_point_x(start, end, percent):
            part = 100 / percent
            start_x = start[0]
            end_x = end[0]
            one_third_x = start_x + ((abs(start_x) + end_x) / part)
            return one_third_x

        def car_movement(car_obj, move_tp_point):
            return car_obj.animate(rate_func=rate_functions.linear).move_to(move_tp_point, aligned_edge=RIGHT).shift(0.05 * LEFT + 0.3 * UP)

        ax = Axes().set_opacity(0.3)

        road_y_coord = -2.5
        road_line_start_point = [-5.55, road_y_coord, 0]
        road_line_end_point = [6.63, road_y_coord, 0]

        flag_point = [get_point_x(road_line_start_point, road_line_end_point, percent=33.33), road_y_coord, 0]

        road_first_part_center = [get_point_x(road_line_start_point, flag_point, percent=50), road_y_coord, 0]
        road_second_part_center = [get_point_x(flag_point, road_line_end_point, percent=50), road_y_coord, 0]

        road_second_part_70_percent = [get_point_x(flag_point, road_line_end_point, percent=70), road_y_coord, 0]

        condition_point = ax.coords_to_point(-7, 3.5)

        # --------------------------------------------- Task number -------------------------------------- #
        task_number = TaskNumberBox(text.TASK_NUMBER_STR)
        self.play(FadeIn(task_number))
        self.wait(0.5)

        # --------------------------------------------- Point 1 ------------------------------------- #
        segment = Segment(road_line_start_point, road_line_end_point)
        a = MathTex(text.A).move_to(road_line_start_point).scale(1.2).shift(0.25 * LEFT + 0.21 * DOWN)
        b = MathTex(text.B).move_to(road_line_end_point).scale(1.2).shift(0.25 * RIGHT + 0.21 * DOWN)
        self.play(FadeIn(a), FadeIn(segment), FadeIn(b))
        self.wait()

        # --------------------------------------------- Point 2 ------------------------------------- #
        car = SimpleSVGMobject('cars/car_2').move_to(road_line_start_point).scale(0.25).shift(0.8 * LEFT + 0.3 * UP)
        self.play(FadeIn(car))
        self.wait()

        # --------------------------------------------- Point 3 ------------------------------------- #
        condition_1 = MathTex(text.CONDITION_1).next_to(condition_point).scale(1.2)
        condition_2_1 = MathTex(text.CONDITION_2_1).next_to(condition_point).scale(1.2).shift(0.75 * DOWN + 0.25 * LEFT)
        condition_2_2 = MathTex(text.CONDITION_2_2).next_to(condition_point).scale(1.2).shift(1.4 * DOWN + 0.1 * LEFT)

        self.play(AnimationGroup(Write(condition_1), Write(condition_2_1), Write(condition_2_2), lag_ratio=1, run_time=7))
        self.wait()

        # --------------------------------------------- Point 4 ------------------------------------- #
        brace_1 = BraceBetweenPoints(road_line_start_point, road_line_end_point, direction=DOWN).shift(0.15 * UP)
        hour_21 = MathTex(text.HOUR_21).move_to(brace_1).shift(0.8 * DOWN).scale(1.2)

        self.play(Write(brace_1), Write(hour_21))
        self.wait()

        # --------------------------------------------- Point 5 ------------------------------------- #
        dot = Dot(flag_point, radius=0.08, color=YELLOW)
        flag_point_text = MathTex(text.FLAG_POINT_TEXT).move_to(dot).shift(0.9 * UP).scale(1.2)

        self.play(AnimationGroup(FadeIn(dot), Write(flag_point_text), lag_ratio=1))
        self.wait()

        # --------------------------------------------- Point 6 ------------------------------------- #
        road_first_part_text = MathTex(text.ROAD_FIRST_PART_TEXT).move_to(road_first_part_center).shift(0.8 * DOWN).scale(1.2)
        hour_7 = MathTex(text.HOUR_7).move_to(road_first_part_text).scale(1.2)

        # --------------------------------------------- Point 6,7 ------------------------------------- #
        self.play(AnimationGroup(car_movement(car, flag_point), Write(road_first_part_text), run_time=4))
        self.wait()
        self.play(ReplacementTransform(road_first_part_text, hour_7))
        self.wait()

        # --------------------------------------------- Review point 2 ------------------------------------- #
        self.play(FadeOut(hour_21), FadeOut(brace_1))

        # --------------------------------------------- Point 8 ------------------------------------- #
        road_second_part_text = MathTex(text.ROAD_SECOND_PART_TEXT).move_to(road_second_part_center).shift(0.8 * DOWN).scale(1.2)
        hour_14 = MathTex(text.HOUR_14).move_to(road_second_part_text).scale(1.2)

        self.play(Write(road_second_part_text), run_time=2)
        self.wait(1.5)
        self.play(ReplacementTransform(road_second_part_text, hour_14))
        self.wait()

        # --------------------------------------------- Point 9 ------------------------------------- #
        brace_2 = BraceBetweenPoints(road_line_start_point, flag_point, direction=DOWN).shift(0.15 * UP)
        brace_3 = BraceBetweenPoints(flag_point, road_line_end_point, direction=DOWN).shift(0.15 * UP)

        self.play(AnimationGroup(
            AnimationGroup(Write(brace_2), Write(brace_3)),
                  lag_ratio=0.7))
        self.wait()

        # --------------------------------------------- Point 10 ------------------------------------- #
        self.play(FadeOut(condition_1), FadeOut(condition_2_1), FadeOut(condition_2_2))
        self.wait()

        # --------------------------------------------- Point 11 ------------------------------------- #
        road_second_part_text_percent = MathTex(text.ROAD_SECOND_PART_TEXT_PERCENT).move_to(road_second_part_center).shift(1.1 * UP).scale(1.2)
        self.play(Write(road_second_part_text_percent))
        self.wait()

        # --------------------------------------------- Point 12 ------------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).next_to(task_number).scale(1.1).shift(0.6 * RIGHT + 0.05 * DOWN)
        self.play(Write(condition_3), run_time=3)
        self.wait()

        # --------------------------------------------- Point 13 ------------------------------------- #
        coord_x_t = ValueTracker(flag_point[0])
        colored_line = always_redraw(lambda: Line(flag_point, [coord_x_t.get_value(), road_y_coord, 0], color=YELLOW))

        self.play(FadeIn(colored_line))
        self.play(
            AnimationGroup(car_movement(car, road_second_part_70_percent),
                           coord_x_t.animate(rate_func=rate_functions.linear).set_value(road_second_part_70_percent[0]),
                           run_time=6))
        self.wait()

        # --------------------------------------------- Point 14 ------------------------------------- #
        brace_4 = always_redraw(lambda: Brace(VGroup(dot, car)).shift(0.23 * UP + 0.065 * RIGHT))
        self.play(ReplacementTransform(brace_3, brace_4), hour_14.animate.shift(1.2 * LEFT))
        self.wait()

        # --------------------------------------------- Point 15 ------------------------------------- #
        self.play(FadeOut(flag_point_text))
        self.wait()

        # --------------------------------------------- New comments 2 ------------------------------------- #
        dashed_line1 = DashedLine(dash_length=0.15, color=BLUE_D).set_length(3)
        dashed_line2 = DashedLine(dash_length=0.15, color=BLUE_D).set_length(3)
        dashed_line1.rotate(angle=-0.5 * PI, axis=OUT).move_to(flag_point).shift(1.7 * UP)
        dashed_line2.rotate(angle=-0.5 * PI, axis=OUT).move_to(road_line_end_point).shift(1.7 * UP)
        self.play(Create(dashed_line1), Create(dashed_line2), run_time=3)
        self.wait()

        # --------------------------------------------- New comments 3,4,5 ------------------------------------- #
        one_third_to_b_line = Line(flag_point, road_line_end_point)
        one_third_to_b_line.z_index = -1

        one_third_to_70_percent_line = Line(flag_point, road_second_part_70_percent, color=YELLOW)
        one_third_to_70_percent_line.z_index = -1

        dashed_line3 = DashedLine(dash_length=0.3, color=BLUE_D).set_length(1.44)
        dashed_line3.rotate(angle=-0.5 * PI, axis=OUT).move_to(road_second_part_70_percent).shift(2.475 * UP)

        self.play(AnimationGroup(
                        AnimationGroup(one_third_to_b_line.animate(rate_func=rate_functions.linear).shift(3.175 * UP),
                                       Create(dashed_line3),
                                       run_time=3,
                                       lag_ratio=1),
                        one_third_to_70_percent_line.animate(rate_func=rate_functions.linear, run_time=2.25).shift(1.78 * UP),
                                       lag_ratio=0.25))
        self.wait()

        # --------------------------------------------- New comments 6 ------------------------------------- #
        percent_100 = MathTex(text.PERCENT_100).move_to(one_third_to_b_line).shift(0.3 * UP).scale(1.2)
        percent_70 = MathTex(text.PERCENT_70).move_to(one_third_to_70_percent_line).shift(0.3 * UP).scale(1.2)

        self.play(Write(percent_100), Write(percent_70))

        # --------------------------------------------- Point 16 ------------------------------------- #
        solution_1_part = MathTex(text.SOLUTION_1_PART).next_to(condition_point).shift(0.4 * LEFT).scale(1.2)
        solution_2_part = MathTex(text.SOLUTION_2_PART).move_to(solution_1_part).shift(0.7 * DOWN).scale(1.2)

        self.play(AnimationGroup(Write(solution_1_part), Write(solution_2_part), lag_ratio=1, run_time=4))
        self.wait()

        # --------------------------------------------- Point 17 ------------------------------------- #
        solution_3_part = MathTex(text.SOLUTION_3_PART).move_to(solution_2_part).shift(0.7 * DOWN).scale(1.2)

        self.play(Write(solution_3_part), run_time=2)
        self.wait()

        # --------------------------------------------- Point 18 ------------------------------------- #
        t = ValueTracker(14)
        coord_x = ValueTracker()
        hour_14_to_20 = always_redraw(lambda: MathTex(int(t.get_value()), text.HOUR).
                                      move_to(hour_14).shift(coord_x.get_value() * RIGHT).scale(1.2))

        self.play(FadeIn(hour_14_to_20), FadeOut(hour_14), lag_ratio=1)
        self.play(AnimationGroup(
            t.animate(rate_func=rate_functions.linear).set_value(20),
            coord_x.animate(rate_func=rate_functions.linear).set_value(1.22),
            car_movement(car, road_line_end_point),
            run_time=4))
        self.wait()

        # --------------------------------------------- Point 19 ------------------------------------- #
        hour_14_to_20_copy = hour_14_to_20.copy()
        self.add(hour_14_to_20_copy)
        self.remove(hour_14_to_20)
        self.play(hour_7.animate.shift(1.0 * RIGHT),
                  hour_14_to_20_copy.animate.shift(2.65 * LEFT),
                  run_time=2)

        plus = MathTex(text.PLUS).next_to(hour_7).scale(1.2)
        solution_result = MathTex(text.SOLUTION_RESULT).next_to(hour_14_to_20_copy).shift(0.25 * RIGHT).scale(1.2)
        self.play(AnimationGroup(Write(plus), Write(solution_result), lag_ratio=1))

        self.wait(3)
