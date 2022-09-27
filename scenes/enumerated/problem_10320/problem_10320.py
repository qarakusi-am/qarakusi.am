from manim import Scene, FadeIn, GrowFromEdge, Tex, MathTex, Write, VGroup, AnimationGroup, Brace, FadeOut, Indicate, Circumscribe, GrowFromCenter, Transform, always_redraw
from manim import WHITE, RIGHT, ORIGIN, LEFT, DOWN, UP, YELLOW, GREEN
from manim import linear
from aramanim import Reset, Segment, CutIn, CutOut, Run
from objects import SimpleSVGMobject, DScissors, Train, Stopwatch
from qarakusiscene import TaskNumberBox
from math import floor
from .text import *

scale = .02

class Problem10320(Scene):
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_string)
        self.play(FadeIn(task_number))

        Arsen_svg = SimpleSVGMobject("boy_1")
        Arsen = VGroup(Arsen_svg, Tex(Arsen_string).next_to(Arsen_svg, DOWN))
        Arsen.scale(.7).to_edge(LEFT, buff=1).shift(UP)
        self.play(FadeIn(Arsen))
        self.wait()

        road = self.get_part(value=605).scale(scale).next_to(Arsen, DOWN, buff=1).align_to(Arsen, LEFT)
        self.play(GrowFromEdge(road, LEFT))
        road_length = MathTex(road_length_string).next_to(road, DOWN, buff=.7)
        self.play(Write(road_length))
        self.wait()
        
        city = SimpleSVGMobject("city").next_to(road.right_edge, UP, buff=1)
        self.play(FadeIn(city))
        self.wait()
        
        train = Train(number_of_rolling_cars=1).scale(.2).next_to(road.left_edge, UP).scale(.8)
        self.play(FadeIn(train))
        self.wait()
        
        self.play(Arsen.animate.scale(.2).move_to(train.get_center()))
        self.play(FadeOut(Arsen))

        first_part_of_road = self.get_part(value=320).scale(scale).align_to(road.line, LEFT+UP)
        stopwatch = Stopwatch()
        stopwatch.scale(.5).to_edge(UP+RIGHT).shift(LEFT)
        timer = always_redraw(lambda: MathTex("{}".format(floor(stopwatch.time.get_value()/240*4))).next_to(stopwatch, DOWN))
        self.add(timer)
        self.play(
            train.animate.next_to(first_part_of_road.right_edge, UP),
            Run(stopwatch, speed=60, run_time=4),
            run_time=4,
            rate_func=linear
        )
        self.play(FadeIn(first_part_of_road))
        first_part_of_road_time = MathTex(first_part_of_road_time_string).next_to(first_part_of_road, UP, buff=.5)
        self.play(Write(first_part_of_road_time))
        self.wait()
        second_part_of_road = self.get_part(value=285).scale(scale).next_to(first_part_of_road, buff=0)
        self.play(Reset(stopwatch))
        self.play(
            train.animate.next_to(second_part_of_road.right_edge, UP),
            Run(stopwatch, speed=60, run_time=3),
            run_time=3,
            rate_func=linear
        )
        self.add(second_part_of_road)
        second_part_of_road_time = MathTex(second_part_of_road_time_string).next_to(second_part_of_road, UP, buff=.5)
        self.play(Write(second_part_of_road_time))
        self.wait()

        self.play(
            VGroup(
                road,
                first_part_of_road,
                first_part_of_road_time,
                second_part_of_road,
                second_part_of_road_time,
                road_length,
                train,
                city
            ).animate.to_edge(DOWN, buff=.8),
            FadeOut(stopwatch, timer)
        )
        self.play(FadeOut(train, city))
        self.wait()
        
        one_part = self.get_part(value=80, color=GREEN).scale(scale).to_edge(LEFT).to_edge(UP, buff=1.7)
        self.play(GrowFromEdge(one_part, LEFT))
        self.wait()
        
        one_part_copy = one_part.copy()
        self.play(FadeIn(one_part_copy))
        self.play(one_part_copy.animate.shift(DOWN*1.5))
        self.wait()
        segment_15 = self.get_part(15, color=YELLOW).scale(scale).next_to(one_part_copy, buff=0)
        segment_15.set_label(MathTex(segment_15_string))
        segment_15_label = segment_15.update_label_pos(buff=.15)
        self.play(
            GrowFromEdge(segment_15, LEFT),
            Write(segment_15_label)
        )
        self.wait()

        x4_one_part = [*[one_part.copy() for i in range(4)]]
        road_animation_part1 = AnimationGroup(*[x4_one_part[i].animate.next_to(first_part_of_road.left_edge, buff=i*80*scale) for i in range(4)], lag_ratio=1.8)
        self.play(road_animation_part1)
        first_part_of_road_brace = Brace(first_part_of_road, UP, buff=.08)
        self.play(FadeIn(first_part_of_road_brace))
        self.wait()
        x3_one_part_and_15 = [*[VGroup(one_part_copy.copy(), segment_15.copy()) for i in range(3)]]
        road_animation_part2 = AnimationGroup(*[x3_one_part_and_15[i].animate.next_to(second_part_of_road.left_edge, buff=i*95*scale) for i in range(3)], lag_ratio=1.8)
        self.play(road_animation_part2)
        second_part_of_road_brace = Brace(second_part_of_road, UP, buff=.08)
        self.play(FadeIn(second_part_of_road_brace))
        self.wait()
        self.play(Indicate(road_length))
        self.wait()

        self.play(*[Circumscribe(x3_one_part_and_15[i][1], fade_out=True) for i in range(3)])
        self.wait()

        self.play(
            FadeOut(
                road,
                first_part_of_road,
                first_part_of_road_time,
                second_part_of_road,
                second_part_of_road_time,
                road_length,
                first_part_of_road_brace,
                second_part_of_road_brace
            )
        )
        scissors = [
            *[DScissors(x3_one_part_and_15[i][1].left_edge.get_center()) for i in range(len(x3_one_part_and_15))],
            *[DScissors(x3_one_part_and_15[i][1].right_edge.get_center()) for i in range(len(x3_one_part_and_15)-1)]
        ]
        self.play(*[CutIn(scissors[i]) for i in range(len(scissors)-2)])
        self.play(*[CutOut(scissors[i]) for i in range(len(scissors)-2)])
        self.play(*[CutIn(scissors[i+3]) for i in range(len(scissors)-3)])
        self.play(*[CutOut(scissors[i+3]) for i in range(len(scissors)-3)])
        self.play(*[x3_one_part_and_15[i][1].animate.shift(UP*.5) for i in range(len(x3_one_part_and_15))])
        self.wait()

        x7_part_value = MathTex(r"605-3\cdot15=560").to_edge(RIGHT, buff=5).to_edge(UP, buff=1.5)
        self.play(Write(x7_part_value))
        self.wait()
        self.play(FadeOut(*[x3_one_part_and_15[i][1] for i in range(len(x3_one_part_and_15))]))
        self.wait()
        x7_one_part = VGroup(
            *[one_part.copy() for i in range(7)]
        ).arrange(RIGHT, buff=0).move_to(road.get_center())
        self.play(
            Transform(
                VGroup(
                    *[x4_one_part[i] for i in range(len(x4_one_part))],
                    *[x3_one_part_and_15[i][0] for i in range(len(x3_one_part_and_15))]
                ),
                x7_one_part
            )
        )
        self.wait()
        x7_one_part = VGroup(
            *[x4_one_part[i] for i in range(len(x4_one_part))],
            *[x3_one_part_and_15[i][0] for i in range(len(x3_one_part_and_15))],
        )
        x7_one_part_brace = Brace(x7_one_part, DOWN)
        x7_one_part_brace_label = x7_one_part_brace.get_tex("560")
        self.play(
            GrowFromCenter(x7_one_part_brace),
            Write(x7_one_part_brace_label)
        )
        self.wait()

        one_part_value = MathTex("560:7=80").next_to(x7_part_value, DOWN, buff=.4).align_to(x7_part_value, LEFT)
        self.play(Write(one_part_value))
        self.wait()
        one_part.set_label(MathTex("80"))
        one_part_label = one_part.update_label_pos()
        one_part_copy.set_label(MathTex("80"))
        one_part_copy_label = one_part_copy.update_label_pos()
        self.play(
            Write(one_part_label),
            Write(one_part_copy_label)
        )
        self.wait()
        one_part_and_15_value = MathTex("80+15=95").next_to(one_part_value, DOWN, buff=.4).align_to(one_part_value, LEFT)
        self.play(Write(one_part_and_15_value))
        self.wait()
        one_part_and_15_brace = Brace(VGroup(one_part_copy, segment_15), UP)
        one_part_and_15_brace_label = one_part_and_15_brace.get_tex("95")
        self.play(
            GrowFromCenter(one_part_and_15_brace),
            Transform(VGroup(one_part_copy_label, segment_15_label), one_part_and_15_brace_label)
        )

        self.wait(2)

    def get_part(self, value, label = None, color = WHITE, **kwargs):
        seg = Segment(
            ORIGIN,
            value * RIGHT,
            label,
            stroke_width = 6,
            color = color,
            **kwargs
        )
        return seg
