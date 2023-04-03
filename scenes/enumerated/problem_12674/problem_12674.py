from . import text

from objects import SimpleSVGMobject, Stopwatch, Train
from qarakusiscene import TaskNumberBox

from manim import LEFT, UP, DOWN, RIGHT, PI
from manim import AnimationGroup, FadeIn, FadeOut, Write, ReplacementTransform
from manim import MathTex, VGroup
from manim import Arrow, Line, Circle
from manim import Axes
from manim import rate_functions, MovingCameraScene, BraceBetweenPoints
from manim import YELLOW


class Problem12674(MovingCameraScene):
    def construct(self):
        # --------------------------------------------- Base -------------------------------------- #
        def cars_movement(left_dist, right_dist, run_time):
            result = AnimationGroup(
                left_car.animate(rate_func=rate_functions.linear).shift(left_dist),
                right_car.animate(rate_func=rate_functions.linear).shift(right_dist),
                run_time=run_time)
            return result

        ax = Axes().set_opacity(0.3)

        road_line_start_point = [-7, -1, 0]
        road_line_end_point = [7, -1, 0]

        left_spead_point = ax.coords_to_point(-4.1, 1.8)
        right_spead_point = ax.coords_to_point(4.8, 1.8)

        left_car_point = [-2.55, -1, 0]
        right_car_point = [3.6, -1, 0]
        flag_point = [0.780, -1, 0]

        # --------------------------------------------- Point 1 -------------------------------------- #
        task_number = TaskNumberBox(text.TASK_NUMBER_STR)
        self.play(FadeIn(task_number))
        self.wait(0.5)

        # --------------------------------------------- Point 2,3 ------------------------------------- #
        line = Line(road_line_start_point, road_line_end_point)
        self.play(FadeIn(line))
        self.wait()

        left_car = SimpleSVGMobject('cars/car_2').move_to(line).scale(0.3).shift(0.35 * UP + 8 * LEFT)
        right_car = SimpleSVGMobject('cars/car_1').flip().move_to(line).scale(0.3).shift(0.35 * UP + 8 * RIGHT)

        left_arrow = Arrow(stroke_width=4, max_tip_length_to_length_ratio=0.2).scale(1.45).move_to(left_spead_point)
        right_arrow = left_arrow.copy().rotate(angle=PI).move_to(right_spead_point)

        left_car_spead = text.left_car_spead.move_to(left_arrow).shift(0.35 * UP + 0.15 * LEFT)
        right_car_spead = text.right_car_spead.move_to(right_arrow).shift(0.35 * UP + 0.15 * RIGHT)

        spead_animation_group = AnimationGroup(Write(left_arrow), Write(left_car_spead), Write(right_arrow), Write(right_car_spead))
        car_animation_group = cars_movement(left_dist=7.83 * RIGHT, right_dist=6.5 * LEFT, run_time=12)

        self.play(AnimationGroup(car_animation_group, spead_animation_group, lag_ratio=0.5))

        # --------------------------------------------- Point 4,5 ------------------------------------- #
        flag = SimpleSVGMobject('flag_meet/flag_meet_2.svg').move_to(left_car).scale(0.6).shift(0.879 * RIGHT + 0.25 * UP)
        meeting_moment = MathTex(text.MEETING_MOMENT).move_to(flag).scale(1.2).shift(0.9 * UP)
        self.add(flag)
        self.wait(0.3)
        self.add(meeting_moment)
        self.wait()

        # --------------------------------------------- Point 6 ------------------------------------- #
        car_animation_group = cars_movement(left_dist=3.3 * LEFT, right_dist=2.8 * RIGHT, run_time=6)
        before_meeting_group = text.before_meeting_group

        self.play(FadeOut(meeting_moment))
        self.wait()
        self.add(before_meeting_group)
        self.play(AnimationGroup(car_animation_group,
                                 text.t.animate(rate_func=rate_functions.linear,run_time=6).set_value(60)))
        self.wait()

        # --------------------------------------------- Point 7 ------------------------------------- #
        self.play(task_number.animate.shift(2.092 * RIGHT + 0.83 *  DOWN).scale(0.7) ,
                  self.camera.frame.animate.set(width=10).shift(0.3 * RIGHT + 0.2 * UP), run_time=3)
        self.wait()

        # --------------------------------------------- Point 8 ------------------------------------- #
        brace_1 = BraceBetweenPoints(left_car_point, flag_point, direction=DOWN).shift(0.17 * UP)
        one_hour_road = MathTex(text.ONE_HOUR_ROAD).move_to(brace_1).shift(0.5 * DOWN).scale(0.75)

        self.play(Write(brace_1), Write(one_hour_road), lag_ratio=1)
        self.wait()

        # --------------------------------------------- Point 9 ------------------------------------- #
        km_80 = MathTex(text.KM_80).move_to(one_hour_road).scale(0.8)
        self.play(ReplacementTransform(one_hour_road, km_80))
        self.wait()

        # --------------------------------------------- Point 10 ------------------------------------- #
        brace_2 = BraceBetweenPoints(flag_point, right_car_point, direction=DOWN).shift(0.17 * UP)
        km_70 = MathTex(text.KM_70).move_to(brace_2).shift(0.5 * DOWN).scale(0.8)

        self.play(Write(brace_2), Write(km_70), lag_ratio=1)
        self.wait()

        # --------------------------------------------- Point 11 ------------------------------------- #
        big_brace = BraceBetweenPoints(left_car_point, right_car_point, direction=DOWN).shift(0.17 * UP)
        plus = MathTex(text.PLUS).move_to(big_brace).shift(0.48 * DOWN).scale(0.8)

        self.play(ReplacementTransform(VGroup(brace_1, brace_2), big_brace))
        self.wait()
        self.play(km_80.animate.shift(0.8 * RIGHT), km_70.animate.shift(1.1 * LEFT), Write(plus))
        self.wait()

        # --------------------------------------------- Point 12 ------------------------------------- #
        self.play(km_80.animate.shift(LEFT), plus.animate.shift(LEFT), km_70.animate.shift(LEFT))

        equal = MathTex(text.EQUAL).next_to(km_70).scale(0.8)
        km_150 = MathTex(text.KM_150).next_to(equal).scale(0.8).shift(0.1 * RIGHT)

        self.play(Write(equal), Write(km_150), lag_ratio=1)
        self.wait()

        # --------------------------------------------- Point 13 ------------------------------------- #
        self.play(km_150.animate.scale(1.5))
        circle = Circle(color=YELLOW).surround(km_150)
        self.play(Write(circle))

        self.wait(3)
