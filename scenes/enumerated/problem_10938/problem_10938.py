from . import text

from objects import SimpleSVGMobject, Stopwatch, Train
from aramanim import Run
from qarakusiscene import TaskNumberBox

from manim import Scene
from manim import LEFT, UP, DOWN, RIGHT, OUT, PI
from manim import AnimationGroup, FadeIn, FadeOut, Write, Create, ReplacementTransform, Indicate, Wiggle
from manim import MathTex, VGroup, Group
from manim import Arrow, DashedLine, Brace, Line
from manim import rate_functions
from manim import YELLOW


class Problem10938(Scene):

    def construct(self):
        # ------------------------------------- Task Number -------------------------------------
        task_number = TaskNumberBox(text.TASK_NUMBER_STR)
        self.play(FadeIn(task_number))
        self.wait(0.5)

        # ---------------------------------------------------------------------------------------------------
        # ---------------------------- First road - Bridge, train, stopwatch --------------------------------
        bridge = SimpleSVGMobject('kamurj/kamurj_3').to_corner(DOWN).scale(0.3).shift(2.80 * UP)
        self.play(FadeIn(bridge))
        self.wait(1)

        train = Train(number_of_rolling_cars=2).scale(0.128).move_to(bridge).shift(8.5 * LEFT + 0.48 * UP)

        stopwatch = Stopwatch()
        stopwatch.move_to(task_number, RIGHT).scale(0.6).shift(7 * RIGHT +  1.2 * DOWN)
        stopwatch_animation = Run(stopwatch, speed=1.8947, run_time=9.5)

        bridge_length_text = MathTex(text.BRIDGE_LENGTH_TEXT).move_to(task_number).scale(1.2).shift(0.8 * DOWN, 0.7 * RIGHT)
        train_length_text = MathTex(text.TRAIN_LENGTH_TEXT).move_to(bridge_length_text).scale(1.2).shift(0.7 * DOWN, 0.2 * LEFT)
        self.play(Write(bridge_length_text), Write(train_length_text))
        self.play(AnimationGroup(
            train.animate(rate_func=rate_functions.linear, run_time=12).shift(RIGHT * 12.5),
                AnimationGroup(
                    Wiggle(stopwatch, scale_value=1.5),
                    stopwatch_animation,
                    lag_ratio=0),
            lag_ratio=0.25))
        self.wait(1)

        # ------------------------------------- Small arrow, time ------------------------------------
        small_arrow_1 = Arrow(max_stroke_width_to_length_ratio=6,
                              max_tip_length_to_length_ratio=0.2
                              ).scale(0.5).rotate(angle=PI).move_to(stopwatch).shift(2.5 * RIGHT, 0.5 * DOWN)
        seconds_18 = MathTex(text.SECONDS_18).move_to(small_arrow_1).scale(1.2).shift(0.01 * LEFT)

        self.play(small_arrow_1.animate.shift(LEFT))
        self.play(Write(seconds_18))
        self.wait(1)

        # -------------------------------------------------------------------------------------------------
        # ------------------------------------- Second road with column -----------------------------------
        column = SimpleSVGMobject('syun/syun-01').to_corner(DOWN).scale(0.6).shift(2.74 * LEFT + 0.8 * UP)
        self.play(FadeIn(column))

        train_2 = train.copy().next_to(column, LEFT + UP).shift(3.5 * LEFT, 1.3  * DOWN)
        self.play(train_2.animate(rate_func=rate_functions.linear, run_time=3).shift(RIGHT * 3.89))
        self.wait(1)
        train_2_copy = train_2.copy()
        self.play(train_2_copy.animate.shift(0.40 * DOWN).set_opacity(0.5), run_time = 2)
        self.play(train_2.animate(rate_func=rate_functions.linear, run_time=3).shift(2.69 * RIGHT))
        self.wait(1)
        # ---------------------------------- DashedLine---------------------------------------
        dashed_line1 = DashedLine(dash_length=0.15).set_length(0.38)
        dashed_line2 = DashedLine(dash_length=0.15).set_length(0.38)
        dashed_line1.rotate(angle=-0.5 * PI, axis=OUT).next_to(train_2).shift(LEFT * 0.22)
        dashed_line2.rotate(angle=-0.5 * PI, axis=OUT).next_to(train_2_copy).shift(LEFT * 0.22)
        self.play(Create(dashed_line1), Create(dashed_line2))
        self.wait(1)

        # ------------------------------ Train length with brace ---------------------------------
        brace = Brace(VGroup(dashed_line1, dashed_line2), direction=DOWN).shift(0.12 * UP)
        train_length = MathTex(text.TRAIN_LENGTH)
        train_length.next_to(brace, DOWN).scale(1.2).shift(0.1 * UP)

        self.play(Write(brace), Write(train_length), lag_ratio=0.8, run_time=2)
        self.wait(2)

        # ------------------------------ Surrounding rectangle ------------------------------------
        property_1_rect = VGroup()
        vertices = [[3.3, -2.8, 0], [-4, -2.8, 0], [-4, -5.5, 0], [3.7, -5.5, 0], [3.7, -3.2, 0]]
        for i in range(4):
            property_1_rect += Line(vertices[i], vertices[i+1], color=YELLOW)
        question_mark = MathTex(r"?").scale(1.2).move_to(property_1_rect).shift(3.85 * RIGHT, 1.3 * UP)
        rectangle = VGroup(property_1_rect, question_mark)
        rectangle.move_to(column).shift(0.61 * DOWN)
        self.play(Write(rectangle), run_time=1.5)
        self.wait(2)

        # -----------------------------------------------------------------------------------------
        # -------------------------------- First road ---------------------------------------
        train.shift(12.5 * LEFT + 0.7 * UP)
        self.play(AnimationGroup(FadeOut(stopwatch),
                                 FadeOut(small_arrow_1),
                                 FadeOut(train_length_text),
                                 FadeOut(bridge_length_text),
                                 seconds_18.animate.shift(1.5 * UP, 3.5 * LEFT),
                                 bridge.animate.shift(0.7 * UP)),
                                 run_time=5)
        self.wait(1)
        self.play(train.animate(rate_func=rate_functions.linear, run_time=4).shift(4.4 * RIGHT))
        self.wait(1)
        train_copy = train.copy()
        self.play(train_copy.animate.shift(DOWN).set_opacity(0.5), run_time=2)
        self.wait(1)
        self.play(train.animate(rate_func=rate_functions.linear, run_time=8).shift(8.1 * RIGHT),
                  lag_ratio=0,
                  run_time=8)
        self.wait(1)

        # ---------------------------------- DashedLine---------------------------------------
        dashed_line3 = DashedLine(dash_length=0.15).set_length(1.4)
        dashed_line4 = DashedLine(dash_length=0.49).set_length(0.35)
        dashed_line3.rotate(angle=-0.5 * PI, axis=OUT).next_to(train, LEFT).shift(RIGHT * 0.23 + 0.47 * DOWN)
        dashed_line4.rotate(angle=-0.5 * PI, axis=OUT).next_to(train_copy).shift(LEFT * 0.22 + 0.01 * DOWN)
        self.play(Create(dashed_line3), Create(dashed_line4))
        self.wait(1)

        # ------------------------------ Train length with brace ---------------------------------
        brace_1 = Brace(VGroup(dashed_line3, dashed_line4), direction=DOWN).shift(0.1 * UP)
        bridge_length = MathTex(text.BRIDGE_LENGTH)
        bridge_length.next_to(brace_1, DOWN).scale(1.2).shift(0.1 * UP)

        self.play(Write(brace_1), Write(bridge_length), lag_ratio=0.8, run_time=2)
        self.wait(1)

        dashed_line5 = DashedLine(dash_length=0.15).set_length(1.4)
        dashed_line5.rotate(angle=-0.5 * PI, axis=OUT).next_to(train).shift(LEFT * 0.22 + 0.47 * DOWN)
        self.play(Write(dashed_line5))
        self.wait(1)

        brace_2 = Brace(VGroup(dashed_line3, dashed_line5), direction=DOWN).shift(0.08 * UP)

        train_length_2_copy = train_length.copy().next_to(brace_2, DOWN).shift(0.13 * UP)

        self.play(Write(brace_2), Write(train_length_2_copy), lag_ratio=0.8, run_time=2)
        self.wait(1)

        brace_3 = Brace(VGroup(dashed_line4, dashed_line5), direction=DOWN).shift(0.08 * UP)
        self.play(ReplacementTransform(VGroup(brace_1, brace_2), brace_3), run_time=1)
        self.wait(1)
        self.play(bridge_length.animate.shift(0.55 * RIGHT), train_length_2_copy.animate.shift(1.84 * LEFT))
        self.wait(1)

        plus = MathTex(text.PLUS)
        plus.next_to(bridge_length).scale(1.2)
        self.play(Write(plus))
        self.wait(1)

        meters_group = Group(bridge_length, train_length_2_copy, plus)
        meters_72 = MathTex(text.METERS_72).scale(1.2).move_to(meters_group).shift(0.05 * DOWN)

        self.play(ReplacementTransform(meters_group, meters_72),run_time=1)
        self.wait(1)

        small_arrow_2 = small_arrow_1.copy().rotate(angle=PI)
        self.play(meters_72.animate.move_to(seconds_18, RIGHT).shift(2.1 * RIGHT, 0.05 * UP),
                  Write(small_arrow_2.next_to(seconds_18)),
                  run_time=2)
        self.wait(1)

        one_second = MathTex(text.ONE_SECOND).scale(1.2).move_to(seconds_18).shift(0.7 * DOWN, 0.15 * RIGHT)
        small_arrow_3 = small_arrow_2.copy().move_to(small_arrow_2).shift(0.7 *  DOWN)
        self.play(Write(one_second), Write(small_arrow_3), lag_ratio=1)
        self.wait(1)

        divide = MathTex(text.DIVIDE).scale(1.2).next_to(meters_72).shift(0.7 * DOWN)
        seconds_18_copy = seconds_18.copy().next_to(divide).shift(0.05 * DOWN)
        meters_72_copy = meters_72.copy()
        self.play(AnimationGroup(meters_72_copy.animate.shift(0.7 * DOWN), Write(divide), Write(seconds_18_copy), lag_ratio=1))
        self.wait(1)

        transform_group = Group(meters_72_copy, divide, seconds_18_copy)
        meter_second_4 = MathTex(text.METER_SECOND_4).scale(1.2).move_to(transform_group).shift(0.01 * UP + 0.35 * LEFT)

        self.play(ReplacementTransform(transform_group,meter_second_4), run_time=1)
        self.wait(1)

        meter_second_4_copy = meter_second_4.copy()

        self.play(train_length.animate.shift(0.9 * LEFT))
        divide_2 = MathTex(text.DIVIDE).scale(1.2).next_to(train_length)

        self.play(Write(divide_2), meter_second_4_copy.animate.next_to(divide_2).shift(0.06 * DOWN), run_time=2)
        self.wait(1)

        self.play(FadeOut(seconds_18),
                  FadeOut(small_arrow_2),
                  FadeOut(small_arrow_3),
                  FadeOut(meters_72),
                  FadeOut(bridge),
                  FadeOut(brace_3),
                  FadeOut(train),
                  FadeOut(train_copy),
                  FadeOut(dashed_line3),
                  FadeOut(dashed_line4),
                  FadeOut(dashed_line5),
                  FadeOut(one_second),
                  FadeOut(meter_second_4)
        )
        self.wait(1)

        obj_group = VGroup(column, dashed_line1, dashed_line2, brace, train_2, train_2_copy, train_length, divide_2, meter_second_4_copy)

        self.play(FadeOut(rectangle), FadeOut(question_mark))
        self.wait(0.5)
        self.play(obj_group.animate.shift(2.0 * RIGHT + 2.3 * UP), run_time=1.5)
        self.wait(1)

        equal = MathTex(text.EQUAL).scale(1.2).next_to(meter_second_4_copy)
        result = MathTex(text.RESULT).scale(1.2).next_to(equal)
        self.play(Write(equal), Write(result))
        self.wait(1)
        self.play(Indicate(result))

        self.wait(3)
