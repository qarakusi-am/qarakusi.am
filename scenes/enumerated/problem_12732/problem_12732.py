from manim import Write, FadeOut, AnimationGroup, Tex, VGroup
from manim import Rotate, TransformFromCopy, Create, Transform
from manim import WHITE, MathTex, PI, RED, BLUE, GREEN, linear
from manim import Scene, LEFT, UP, DOWN, RIGHT, Circle, Line, ORIGIN, ReplacementTransform
from qarakusiscene import TaskNumberBox
from .text import *
from numpy import *

FONT_SIZE = 64
RUN_TIME_SPEED = 2


class Problem12732(Scene):

    def construct(self):

        task_number = TaskNumberBox(taskNumberString)
        self.add(task_number)
        self.wait(0.25)

        formed_angle_text = Tex(angle_between_clock_hands, font_size=FONT_SIZE).shift(UP * 2.7)
        self.play(Write(formed_angle_text, run_time=RUN_TIME_SPEED))
        self.wait()

        hours_to_display = Tex('15:00, 18:00, 13:00, 17:00', font_size=FONT_SIZE).shift(UP * 2)
        self.play(Write(hours_to_display, run_time=RUN_TIME_SPEED))
        self.wait()

        clock, hands, marks = create_clock_and_time_marks()

        self.play(Write(clock))
        self.wait()
        self.play(FadeOut(formed_angle_text))
        self.wait()

        # move time labels to the left

        self.play(hours_to_display[0][0:5].animate.shift(LEFT * 3.1),
                  hours_to_display[0][6:11].animate.shift(LEFT * 4.9 + DOWN),
                  hours_to_display[0][12:17].animate.shift(LEFT * 6.7 + DOWN * 2),
                  hours_to_display[0][18:].animate.shift(LEFT * 8.5 + DOWN * 3),
                  VGroup(hours_to_display[0][11], hours_to_display[0][5], hours_to_display[0][17]).animate.set_opacity(
                      0))
        self.wait()

        self.play(clock.animate.shift(UP).scale(1.5))
        self.wait()

        clock.add(hands)

        self.play(Write(hands))
        self.wait(2)

        self.play(Rotate(hands[0], angle=-PI / 8 * 0.6, about_point=hands[0].get_start(), rate_func=linear, run_time=2),
                  Rotate(hands[1], angle=-PI * 0.993, about_point=hands[1].get_start(), rate_func=linear, run_time=2))
        self.wait(2)

        self.play(
            AnimationGroup(
                Rotate(hands[0], angle=-PI / 2 * 1.01, about_point=hands[0].get_start(), rate_func=linear, run_time=7),
                Rotate(hands[1], angle=-6 * PI, about_point=hands[1].get_start(), rate_func=linear, run_time=7)))
        self.wait()

        angles = VGroup(Tex('90$^{\circ}$').move_to(hands[0]).shift(UP * 0.3),
                        Tex('180$^{\circ}$').move_to(hands[0]),
                        Tex('150$^{\circ}$').move_to(hands[0]).shift(UP * 0.2 + RIGHT * 0.2))

        angle_labels = VGroup(Tex(right_angle).next_to(angles[0], UP).shift(RIGHT * 4),
                              Tex(obtuse_angle).next_to(angles[0], UP).shift(RIGHT * 4))

        self.play(Write(angles[0]))
        self.wait()

        self.play(Write(angle_labels[0]))
        self.wait()

        self.play(FadeOut(angle_labels[0]))
        self.wait()

        self.play(angles[0].animate.set_color(GREEN).scale(1.3).move_to(hours_to_display[0][4]).shift(RIGHT * 0.85))
        self.wait()

        self.play(
            AnimationGroup(
                Rotate(hands[0], angle=-PI / 2 * 1.01, about_point=hands[0].get_start(), rate_func=linear, run_time=7),
                Rotate(hands[1], angle=-6 * PI, about_point=hands[1].get_start(), rate_func=linear, run_time=7)))
        self.wait()

        self.play(Write(VGroup(angles[1], angle_labels[1])))
        self.wait()
        self.play(FadeOut(angle_labels[1]))
        self.play(angles[1].animate.set_color(GREEN).scale(1.3).move_to(hours_to_display[0][10]).shift(RIGHT))
        self.wait()

        self.play(FadeOut(hands))
        self.wait(2)

        # display 13:00
        hands_copy = hands.copy()
        hands_copy[0].rotate(angle=PI * 5 / 6 * 1.01, about_point=hands_copy[0].get_start())
        self.play(TransformFromCopy(VGroup(hours_to_display[0][12:17]), hands_copy))
        self.wait(2)

        radius_lines = VGroup()

        for i in range(0, 7):
            radius_lines.add(Line(hands[0].get_start(), marks[i][0].get_start(), buff=0, stroke_width=2, color=WHITE))
        radius_lines[0].set_style(stroke_width=5)
        radius_lines[1].set_style(stroke_width=5)

        self.play(Create(radius_lines[2:], run_time=2))
        self.wait()

        self.play(Create(VGroup(radius_lines[0:2])))
        hands_copy.set_opacity(0)
        self.wait()

        hands.set_opacity(0)

        angle_numbers = VGroup()

        for i in range(6):
            alpha = math.pi / 2 - math.pi * 2 * 6 * i / 60
            label = MathTex(str(i + 1), color=GREEN).move_to(
                [1 * math.cos(alpha), 1 * math.sin(alpha), 0]).shift(DOWN + RIGHT * 0.3)
            angle_numbers.add(label)

        angle_numbers.shift(UP)

        self.play(Write(angle_numbers))
        self.wait()

        angle_equality = MathTex('180:6 = 30 ^{\circ}').next_to(clock, RIGHT)
        self.play(Write(angle_equality))
        self.wait()
        angle_values = VGroup()
        for item in angle_numbers:
            angle_values.add(MathTex('30 ^{\circ}').scale(0.7).move_to(item).shift(RIGHT * 0.1))
        angle_values[-1].shift(LEFT * 0.1)
        angle_values[0].shift(LEFT * 0.08)

        self.play(*[ReplacementTransform(angle_numbers[i], angle_values[i]) for i in range(len(angle_values))])
        self.wait()

        self.play(FadeOut(angle_equality))
        self.wait()

        self.play(TransformFromCopy(angle_values[0],
                                    angle_values[0].copy().set_color(GREEN).scale(1 / 0.7 * 1.3).move_to(
                                        hours_to_display[0][16]).shift(RIGHT * 0.85)))
        self.wait()
        self.play(FadeOut(radius_lines[-1], angle_values[-1]))
        self.wait()
        self.play(AnimationGroup(
            radius_lines[1].animate.set_style(stroke_width=2),
            radius_lines[0].animate.set_style(stroke_width=5),
            radius_lines[-2].animate.set_style(stroke_width=5)

        ))
        self.wait()

        new_hour_line = hands[0].copy().set_opacity(1)
        new_minute_line = hands[1].copy().set_opacity(1)
        new_hour_line.rotate(PI / 6, about_point=new_hour_line.get_start())

        self.play(AnimationGroup(ReplacementTransform(radius_lines[0], new_minute_line),
                                 Transform(radius_lines[-2], new_hour_line)))
        self.wait()

        self.play(ReplacementTransform(VGroup(radius_lines[1:5], angle_values[:5]), angles[2]))
        self.wait()

        self.play(angles[-1].animate.set_color(GREEN).scale(1.3).move_to(hours_to_display[0][-1]).shift(RIGHT))
        self.wait()


def create_clock_and_time_marks(hour, minute):
    # create clock
    radius = 2
    circle = Circle(radius, color=WHITE)
    clock = VGroup(circle)

    marks = VGroup()
    for i in range(12):
        alpha = math.pi / 2 - math.pi * 2 * i / 12
        if i == 0:
            label_str = '12'
        else:
            label_str = str(i)

        label = MathTex(label_str).move_to([1.2 * radius * math.cos(alpha), 1.2 * radius * math.sin(alpha), 0])
        start_dot = [0.96 * radius * math.cos(alpha), 0.96 * radius * math.sin(alpha), 0]
        end_dot = [0.8 * radius * math.cos(alpha), 0.8 * radius * math.sin(alpha), 0]
        line = Line(start_dot, end_dot, buff=0, color=WHITE, stroke_width=1.5)
        marks.add(VGroup(line, label))

    clock.add(marks)
    clock.shift(DOWN)

    # set clock hands at hour:minute

    hour_dot = ((hour % 12) + minute / 60) * 5 * math.pi * 2 / 60
    minute_dot = minute * math.pi * 2 / 60

    hour_dot = [0.5 * radius * math.cos(math.pi / 2 - hour_dot), 0.5 * radius * math.sin(math.pi / 2 - hour_dot), 0]
    minute_dot = [0.65 * radius * math.cos(math.pi / 2 - minute_dot),
                  0.65 * radius * math.sin(math.pi / 2 - minute_dot), 0]

    hour_line = Line(ORIGIN, hour_dot, buff=0, stroke_width=5, color=RED)
    minute_line = Line(ORIGIN, minute_dot, buff=0, stroke_width=5, color=BLUE)

    hands = VGroup(hour_line, minute_line).scale(1.5).shift(DOWN * 0.08)

    return clock, hands, marks,
