from . import text

from objects import SimpleSVGMobject, Stopwatch, Train
from aramanim import Run
from qarakusiscene import TaskNumberBox

from manim import Scene
from manim import GRAY, RED
from manim import LEFT, UP, DOWN, RIGHT, OUT, PI, MED_LARGE_BUFF
from manim import AnimationGroup, FadeIn, FadeOut, Write, Create, ReplacementTransform, Indicate, Wiggle
from manim import MathTex, VGroup, Group
from manim import Arrow, DashedLine, Brace, SurroundingRectangle
from manim import rate_functions
# from manim import 


class Problem11375(Scene):

    def construct(self):
        # ------------------------------------- Task Number -------------------------------------
        task_number = TaskNumberBox(text.TASK_NUMBER_STR)
        self.play(FadeIn(task_number))
        self.wait(0.5)

        # ------------------------------------- City imaging ------------------------------------
        city = SimpleSVGMobject('cities/city_3', color=GRAY).to_corner((LEFT + UP), buff=1)
        self.play(FadeIn(city))
        self.wait(1)

        # ---------------------------------------- Man ------------------------------------------
        man = SimpleSVGMobject('people/men/man_18', color=GRAY).next_to(city, DOWN).scale(0.5).shift(UP * 0.5)
        self.play(FadeIn(man))
        self.wait(1)

        # ----------- Train speed with arrow / Train imaging, moving --------------
        train_speed = MathTex(text.TRAIN_SPEED).next_to(man).scale(1.2).shift(LEFT * 5)
        arrow = Arrow(stroke_width=4, max_tip_length_to_length_ratio=0.15)
        arrow.next_to(train_speed, DOWN * 0.01).shift(RIGHT * 0.1).scale(1.5)
        speed_group = AnimationGroup(Write(arrow), Write(train_speed, lag_ratio=0.8, run_time=1.5))

        train = Train(number_of_rolling_cars=2).scale(0.17).next_to(man).shift(11.2 * LEFT + DOWN)

        self.play(AnimationGroup(train.animate(rate_func=rate_functions.linear, run_time=12).shift(RIGHT * 18.5),
                                 speed_group, lag_ratio=0.11))

        # ------------------------------ Remove city, scale man ---------------------------------
        self.play(
            AnimationGroup(
                FadeOut(city),
                man.animate.shift(1 * UP + 1.5 * RIGHT).scale(2),
                train_speed.animate.shift(0.5 * UP, 1 * RIGHT),
                arrow.animate.shift(0.5 * UP, 1 * RIGHT)
            )
        )

        # ------------------------------ Big train from left ---------------------------------
        train.shift(LEFT * 20).scale(1.5)
        self.play(train.animate(rate_func=rate_functions.linear, run_time=5).shift(RIGHT * (8.82 + 0.5)))

        # ------------------------------------ Copy train----------------------------------------
        train_copy = train.copy()
        self.play(train_copy.animate.shift(1 * DOWN).set_opacity(0.5), run_time=1)

        # ֊֊֊֊------------------ Stopwatch animation and train passes man -------------------------
        stopwatch = Stopwatch()
        stopwatch.next_to(1.5 * RIGHT + 1.5 * UP, buff=0.5).scale(0.4)
        stopwatch_animation = Run(stopwatch, speed=7, run_time=2)
        self.play(stopwatch_animation, train.animate(rate_func=rate_functions.linear).shift(RIGHT * 5.38), run_time=3)

        # ---------------------------------- DashedLine---------------------------------------
        dashed_line1 = DashedLine(dash_length=0.15).set_length(0.75)
        dashed_line2 = DashedLine(dash_length=0.15).set_length(0.75)
        dashed_line1.rotate(angle=-0.5 * PI, axis=OUT).next_to(train).shift(LEFT * 0.22)
        dashed_line2.rotate(angle=-0.5 * PI, axis=OUT).next_to(train_copy).shift(LEFT * 0.22)
        self.play(Create(dashed_line1), Create(dashed_line2))

        # ------------------------------ Train length with brace ---------------------------------
        brace = Brace(VGroup(dashed_line1, dashed_line2), direction=DOWN)
        train_length = MathTex(text.TRAIN_LENGTH)
        train_length.next_to(brace, DOWN).scale(1.2)

        self.play(Write(brace), Write(train_length), lag_ratio=0.8, run_time=2)

        #  ----------Transform---------------------
        group = Group(arrow, train_speed)
        one_hour = MathTex(text.ONE_HOUR).scale(1.2)
        small_arrow = Arrow(max_stroke_width_to_length_ratio=6, max_tip_length_to_length_ratio=0.2).scale(0.65)
        km = MathTex(text.KM)
        train_speed_2 = VGroup(one_hour, small_arrow, km)
        train_speed_2.arrange_submobjects(buff=0.3)
        train_speed_2.move_to(group).scale(1.2)

        self.play(Indicate(group))
        self.play(ReplacementTransform(group, train_speed_2))

        # -------------------------------- Train speed calculation ------------------------------
        train_calculation = MathTex(text.TRAIN_CALCULATION).next_to(train_speed, DOWN).scale(1.2).shift(2 * LEFT)
        train_calculation[0][3:5].set_color(RED)
        train_calculation[0][7:9].set_color(RED)
        seconds = MathTex(text.SECONDS).next_to(train_calculation).scale(1.2)
        self.play(Write(train_calculation), Write(seconds), lag_ratio=0.0, run_time=3)

        # -------------------------------- Hour transform ------------------------------

        self.play(AnimationGroup(seconds.animate.move_to(one_hour).shift(0.74 * DOWN, 0.52 * LEFT),
                                 FadeOut(train_calculation),
                                 lag_ratio=0.05))

        small_arrow_2 = small_arrow.copy().move_to(seconds).shift(1.79 * RIGHT)

        self.play(Write(small_arrow_2))
        self.play(Indicate(km))

        meter = MathTex(text.METER).move_to(small_arrow_2).scale(1.2).shift(1.95 * RIGHT)
        self.play(Write(meter))
        self.wait(1)

        self.play(AnimationGroup(FadeOut(train_speed_2),
                                 Group(seconds, small_arrow_2, meter).animate.shift(2.50 * UP, 0.7 * LEFT),
                                 lag_ratio=0.5))

        one_second = MathTex(text.ONE_SECOND).move_to(seconds).shift(DOWN, 0.45 * RIGHT).scale(1.2)
        small_arrow_3 = small_arrow_2.copy().move_to(one_second).shift(1.34 * RIGHT)
        question_mark = MathTex(text.QUESTION_MARK).move_to(small_arrow_3).scale(1.2).shift(1.6 * RIGHT)
        self.play(AnimationGroup(Write(one_second), Write(small_arrow_3), Write(question_mark), lag_ratio=1))

        self.wait(1)
        # ------------------------------ Surrounding rectangle ------------------------------------
        box_content = VGroup(seconds, meter, one_second, question_mark, small_arrow_2, small_arrow_3)
        box = SurroundingRectangle(box_content, buff=MED_LARGE_BUFF).scale(0.9)
        self.play(Write(box), run_time=1.5)

        # -----------------------------------------delete man-------------------------------------
        self.play(FadeOut(man), run_time=2)
        self.wait(1)

        # -------------------------------------
        meter_second = MathTex(text.METER_SECOND).next_to(box, DOWN).scale(1.2).shift(0.5 * RIGHT)
        self.play(AnimationGroup(Write(meter_second, run_time=5),
                  AnimationGroup(Wiggle(one_second, scale_value=1.5),
                                 Wiggle(meter, scale_value=1.5),
                                 Wiggle(seconds, scale_value=1.5),
                                 lag_ratio=0.5), lag_ratio=0))
        self.wait(1)

        # ---------------------------------- Result ------------------------------------------------
        self.play(AnimationGroup(Wiggle(brace, scale_value=1.2),
                                 Wiggle(train, scale_value=1.2),
                                 Wiggle(train_copy, scale_value=1.2),
                                 Wiggle(train_length, scale_value=1.2),
                                 lag_ratio=0))
        result = MathTex(text.RESULT).scale(1.2).next_to(train, 2 * DOWN)
        self.play(Write(result))
        self.play(Indicate(result))

        self.play(stopwatch.animate.scale(1.5).shift(0.4 * LEFT))
        small_arrow_4 = Arrow(max_stroke_width_to_length_ratio=6,
                              max_tip_length_to_length_ratio=0.2
                              ).scale(0.5).rotate(angle=PI).move_to(stopwatch).shift(3 * RIGHT, 0.1 * DOWN)

        self.play(small_arrow_4.animate.shift(1.48 * LEFT))
        result_meter = MathTex(text.RESULT_SECOND).move_to(small_arrow_4).scale(1.5).shift(0.9 * RIGHT)
        self.play(Write(result_meter))
        self.play(Indicate(result_meter))
        self.wait(1)
