from manim import *
from math import floor

from aramanim import Segment, Run, Reset, CutIn, CutOut
from qarakusiscene import TaskNumberBox
from objects import SimpleSVGMobject, Stopwatch, DScissors
from .text import *

scale = .02


class Problem10349(Scene):
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_string)
        self.play(FadeIn(task_number))

        souren = self.get_boy(souren_string, 'boy_1', LEFT)
        arshak = self.get_boy(arshak_string, 'boy_2', RIGHT)

        self.play(FadeIn(souren), FadeIn(arshak))
        self.wait()

        self.condition1 = Tex(*condition1_string).scale(.9).to_edge(LEFT).shift(UP)
        self.condition1[0].set_color(ORANGE)
        self.condition2 = Tex(*condition2_string).scale(.9)
        self.condition2.next_to(self.condition1, DOWN, buff=1).align_to(self.condition1, LEFT)
        self.condition2[0].set_color(ORANGE)

        # Ճանապարհի մասին տվյալների համառոտագրություն
        road = self.get_part(value=road_len).scale(scale).next_to(souren, DOWN + RIGHT, buff=1)
        self.play(GrowFromEdge(road, LEFT))
        road_length = MathTex(road_length_string).next_to(road, DOWN, buff=.7)
        self.play(Write(road_length))
        self.wait()

        # Սուրենի և Արշակի ճանապարհների մասերը
        souren_road = self.get_part(value=250, color=BLUE).scale(scale).next_to(road.left_edge, buff=0)
        self.play(GrowFromEdge(souren_road, LEFT))
        arshak_road = self.get_part(value=180, color=RED).scale(scale).next_to(road.right_edge, LEFT, buff=0)
        self.play(GrowFromEdge(arshak_road, RIGHT))

        # Քաղաքի անիմացիա
        city = SimpleSVGMobject("city_2", color=YELLOW_B).next_to(souren_road.get_edge_center(RIGHT), UP, buff=1)
        self.play(FadeIn(city))
        meeting_t = MathTex(meeting_time_string, color=BLUE_B).next_to(city, 0.5 * DOWN, buff=.3)
        self.play(Write(meeting_t))
        self.wait()

        # Սուրենի և Արշակի ժամերի համառոտագրություն
        souren_t = MathTex(souren_time_string, color=BLUE_B).next_to(souren, DOWN, buff=.3)
        arshak_t = MathTex(arshak_time_string, color=BLUE_B).next_to(arshak, DOWN, buff=.3)
        self.play(Write(souren_t))
        self.wait()
        self.play(Write(arshak_t))
        self.wait()

        # Սուրենի և Արշակի հանդիպման անիմացիա
        # souren_copy, arshak_copy = souren.copy(), arshak.copy()
        souren_car = SimpleSVGMobject('car_1').scale(0.2).align_to(souren_road, UL).shift(UP*0.5)
        arshak_car = SimpleSVGMobject('car_2').scale(0.2).align_to(arshak_road, UR).shift(UP*0.5)
        self.play(FadeIn(souren_car), FadeIn(arshak_car))
        souren_car_move = souren_car.animate(rate_func=linear, run_time=5).align_to(souren_road, UR).shift(UP*0.5 + LEFT*0.1)
        arshak_car_move = arshak_car.animate(rate_func=linear, run_time=3).align_to(arshak_road, UL).shift(UP*0.5 + RIGHT*0.1)
        self.play(AnimationGroup(souren_car_move, arshak_car_move, lag_ratio=0.4))
        self.wait()

        # souren_move = souren_copy.animate.scale(.2).move_to(souren_road.get_edge_center(RIGHT) + 0.25*(UP+LEFT))
        # arshak_move = arshak_copy.animate.scale(.2).move_to(souren_road.get_edge_center(RIGHT) + 0.25*(UP+RIGHT))
        # self.play(souren_move, arshak_move)
        self.play(FadeOut(souren_car), FadeOut(arshak_car))
        self.play(FadeOut(city))
        self.wait()
        #
        # self.play(Indicate(meeting_t))
        # self.wait()
        #
        # # Մեկ մասի և հավելյալ մասի պատկերում
        # one_part = self.get_part(value=50, color=GREEN).scale(scale).next_to(souren.get_edge_center(UR), buff=0)
        # self.play(GrowFromEdge(one_part, LEFT))
        # one_part_copy = one_part.copy()
        # self.play(FadeIn(one_part_copy))
        # self.play(one_part_copy.animate.next_to(arshak.get_edge_center(UL), buff=-1.1))
        # self.wait()
        # segment_10 = self.get_part(int(segment_10_string), color=YELLOW).scale(scale).next_to(one_part_copy, buff=0)
        # segment_10.set_label(MathTex(segment_10_string))
        # segment_10_label = segment_10.update_label_pos(buff=.17)
        # self.play(
        #     GrowFromEdge(segment_10, LEFT),
        #     Write(segment_10_label)
        # )
        # self.wait()
        #
        # # Սուրենի ժամերի ընդգծում
        # self.play(Indicate(souren_t))
        # self.wait()
        # self.play(Indicate(meeting_t))
        # self.wait()
        #
        # # Սուրենի ժամացույցի անիմացիա
        # stopwatch = Stopwatch()
        # stopwatch.scale(.5).to_edge(UP)
        # timer = always_redraw(
        #     lambda: MathTex(str(floor(stopwatch.time.get_value() // 60)) + hour_string).next_to(stopwatch, DOWN))
        # self.add(timer)
        # self.play(
        #     Run(stopwatch, speed=60, run_time=5),
        #     run_time=5,
        #     rate_func=linear
        # )
        #
        # # Սուրենի ժամի ցուցադրում ճանապարհի վրա
        # souren_road_brace = Brace(souren_road, UP, buff=.08)
        # souren_road_time = MathTex(souren_road_time_string).next_to(souren_road, UP, buff=.5)
        # self.play(FadeIn(souren_road_brace))
        # self.play(ReplacementTransform(timer, souren_road_time))
        # self.wait()
        #
        # # Սուրենի ճանապարհի մասերի պատկերում
        # x5_one_part = [one_part.copy() for i in range(5)]
        # road_animation_part1 = AnimationGroup(
        #     *[x5_one_part[i].animate.next_to(souren_road.left_edge, buff=i * 50 * scale) for i in range(5)],
        #     lag_ratio=1.8)
        # self.play(road_animation_part1)
        # self.wait()
        #
        # # Արշակի ժամերի ընդգծում
        # self.play(Indicate(arshak_t))
        # self.wait()
        # self.play(Indicate(meeting_t))
        # self.wait()
        #
        # # Արշակի ժամացույցի անիմացիա
        # self.play(Reset(stopwatch))
        # timer = always_redraw(
        #     lambda: MathTex(str(floor(stopwatch.time.get_value() // 60)) + hour_string).next_to(stopwatch, DOWN))
        # self.add(timer)
        # self.play(
        #     Run(stopwatch, speed=60, run_time=3),
        #     run_time=3,
        #     rate_func=linear
        # )
        # self.wait()
        #
        # # Արշակի ճանապարհի մասերի պատկերում
        # x3_one_part_and_10 = [VGroup(one_part_copy.copy(), segment_10.copy()) for i in range(3)]
        # road_animation_part2 = AnimationGroup(
        #     *[x3_one_part_and_10[i].animate.next_to(arshak_road.left_edge, buff=i * 60 * scale) for i in
        #       range(3)], lag_ratio=1.8)
        # self.play(road_animation_part2)
        # arshak_road_brace = Brace(arshak_road, UP, buff=.08)
        # arshak_road_time = MathTex(arshak_road_time_string).next_to(arshak_road, UP, buff=.5)
        # self.play(FadeIn(arshak_road_brace))
        # self.play(ReplacementTransform(timer, arshak_road_time), FadeOut(stopwatch))
        #
        # self.wait()
        #
        # self.play(Indicate(road_length))
        # self.wait()
        #
        # # Մեկ մասի հարցական նշանները
        # question_mark_1 = MathTex(question_mark_string).next_to(one_part, UP, buff=.2)
        # question_mark_2 = MathTex(question_mark_string).next_to(one_part_copy, UP, buff=.2)
        # self.play(FadeIn(question_mark_1), FadeIn(question_mark_2))
        # self.wait()
        # self.play(FadeOut(question_mark_1), FadeOut(question_mark_2))
        # self.wait()
        #
        # # Ընդգծենք 10֊երը
        # self.play(*[Circumscribe(x3_one_part_and_10[i][1], fade_out=True) for i in range(3)])
        # self.wait()
        # self.play(
        #     FadeOut(
        #         souren_road_time,
        #         arshak_road_time,
        #         road_length,
        #         meeting_t,
        #         souren_t,
        #         arshak_t,
        #         souren_road_brace,
        #         arshak_road_brace
        #     )
        # )
        # self.remove(
        #     road,
        #     souren_road,
        #     arshak_road
        # )
        # self.wait()
        #
        # # Հաշվենք 1-ից մինչև 8 մասերը
        # count_x8_one_part_labels = [
        #     *[Tex(str(i + 1)).next_to(x5_one_part[i], UP) for i in range(5)],
        #     *[Tex(str(i + 6)).next_to(x3_one_part_and_10[i][0], UP) for i in range(3)]
        # ]
        # count_x8_one_part_animation = AnimationGroup(
        #     *[Write(count_x8_one_part_labels[i]) for i in range(8)],
        #     lag_ratio=.5
        # )
        # self.play(count_x8_one_part_animation)
        # self.wait()
        #
        # self.play(
        #     *[FadeOut(count_x8_one_part_labels[i]) for i in range(8)]
        # )
        # self.wait()
        #
        # # Մկրատով կտրենք 10-երը
        # scissors = [
        #     *[DScissors(x3_one_part_and_10[i][1].left_edge.get_center()) for i in range(len(x3_one_part_and_10))],
        #     *[DScissors(x3_one_part_and_10[i][1].right_edge.get_center()) for i in range(len(x3_one_part_and_10)-1)]
        # ]
        # self.play(*[CutIn(scissors[i]) for i in range(len(scissors)-2)])
        # self.play(*[CutOut(scissors[i]) for i in range(len(scissors)-2)])
        # self.play(*[CutIn(scissors[i+3]) for i in range(len(scissors)-3)])
        # self.play(*[CutOut(scissors[i+3]) for i in range(len(scissors)-3)])
        # self.play(*[x3_one_part_and_10[i][1].animate.shift(UP*.5) for i in range(len(x3_one_part_and_10))])
        # for i in range(len(x3_one_part_and_10)):
        #     x3_one_part_and_10[i][1].set_label(MathTex(segment_10_string))
        # self.play(AnimationGroup(*[
        #     TransformFromCopy(segment_10_label, x3_one_part_and_10[i][1].update_label_pos())
        #     for i in range(len(x3_one_part_and_10))
        # ], lag_ratio=0))
        # self.wait()
        #
        # # Ձևավոր փակագծեր ամբողջ ճանապարհին
        # entire_road = VGroup(
        #     *[x5_one_part[i] for i in range(len(x5_one_part))],
        #     *[x3_one_part_and_10[i] for i in range(len(x3_one_part_and_10))],
        # )
        # entire_road_brace = Brace(entire_road, DOWN)
        # entire_road_brace_label = entire_road_brace.get_tex(road_length_string)
        # self.play(
        #     GrowFromCenter(entire_road_brace),
        #     Write(entire_road_brace_label)
        # )
        # self.wait()
        #
        # # Ամբողջ ճանապարհից 10-երը հանելու հավասարումը
        # minus_parts = road_len-3*int(segment_10_string)
        # x8_part_value = MathTex(f"{road_len}-3\cdot{segment_10_string}={minus_parts}").to_edge(
        #     RIGHT, buff=3.5).to_edge(UP, buff=1)
        # self.play(Write(x8_part_value))
        # self.wait()
        # self.play(
        #     FadeOut(
        #         *[x3_one_part_and_10[i][1] for i in range(len(x3_one_part_and_10))],
        #         *[x3_one_part_and_10[i][1].label for i in range(len(x3_one_part_and_10))],
        #         entire_road_brace,
        #         entire_road_brace_label
        #     )
        # )
        #
        # # Ամբողջ ճանապարհից 10-երը հանելու ձևավոր փակագծերը
        # x8_one_part = VGroup(
        #     *[x5_one_part[i] for i in range(len(x5_one_part))],
        #     *[x3_one_part_and_10[i][0] for i in range(len(x3_one_part_and_10))],
        # )
        # x8_one_part_brace = Brace(x8_one_part, DOWN)
        # x8_one_part_brace_label = x8_one_part_brace.get_tex(str(minus_parts))
        # self.play(
        #     GrowFromCenter(x8_one_part_brace),
        #     Write(x8_one_part_brace_label)
        # )
        # self.wait()
        #
        # # Մեկ մասը գտնելու հավասարումը
        # one_part_value = MathTex("400:8=50").next_to(x8_part_value, DOWN, buff=.4).align_to(x8_part_value, LEFT)
        # self.play(Write(one_part_value))
        # self.wait()
        # one_part.set_label(MathTex("50", color=GREEN))
        # one_part_label = one_part.update_label_pos()
        # one_part_copy.set_label(MathTex("50", color=GREEN))
        # one_part_copy_label = one_part_copy.update_label_pos()
        # self.play(
        #     Write(one_part_label),
        #     Write(one_part_copy_label)
        # )
        # self.wait()
        #
        # # Մեկ մաս+10֊ը գտնելու հավասարումը
        # one_part_and_15_value = MathTex("50+10=60").next_to(one_part_value, DOWN, buff=.4).align_to(one_part_value,
        #                                                                                             LEFT)
        # self.play(Write(one_part_and_15_value))
        # self.wait()
        #
        # one_part_and_10_brace = Brace(VGroup(one_part_copy, segment_10), UP)
        # one_part_and_10_brace_label = one_part_and_10_brace.get_tex("60" + km)
        # self.play(
        #     GrowFromCenter(one_part_and_10_brace),
        #     Transform(VGroup(one_part_copy_label, segment_10_label), one_part_and_10_brace_label),
        #     one_part.label.animate.become(MathTex(rf"50\text{{{km}}}").next_to(one_part, UP, .05))
        # )
        #
        # self.play(FadeOut(x8_one_part), FadeOut(x8_one_part_brace), FadeOut(x8_one_part_brace_label))
        #
        # # Վերականգնենք սկզբնական ճանապարհի գրաֆիկը ու տեսնենք վերջնական ինչ ստացվեց
        # self.play(GrowFromEdge(road, LEFT), Write(road_length), GrowFromEdge(souren_road, LEFT), GrowFromEdge(arshak_road, RIGHT))
        # x5_one_part = [one_part.copy() for i in range(5)]
        # road_animation_part1 = AnimationGroup(
        #     *[x5_one_part[i].animate.next_to(souren_road.left_edge, buff=i * 50 * scale) for i in range(5)],
        #     lag_ratio=.3)
        # x3_one_part_and_10 = [VGroup(one_part_copy.copy(), segment_10.copy()) for i in range(3)]
        # road_animation_part2 = AnimationGroup(
        #     *[x3_one_part_and_10[i].animate.next_to(arshak_road.left_edge, buff=i * 60 * scale) for i in
        #       range(3)], lag_ratio=.3)
        # self.play(road_animation_part1, road_animation_part2)
        # self.play(FadeIn(souren_road_brace), Write(souren_road_time), FadeIn(arshak_road_brace), Write(arshak_road_time))
        # self.wait()
        #
        # souren_road_brace_2 = Brace(souren_road, DOWN, buff=.08)
        # souren_road_length = MathTex(r"5\cdot50=250"+km).next_to(souren_road, DOWN, buff=.5)
        # self.play(road_length.animate.move_to(3*DOWN), FadeIn(souren_road_brace_2), Write(souren_road_length))
        # self.wait()
        # arshak_road_brace_2 = Brace(arshak_road, DOWN, buff=.08)
        # arshak_road_length = MathTex(r"3\cdot60=180"+km).next_to(arshak_road, DOWN, buff=.5)
        # self.play(FadeIn(arshak_road_brace_2), Write(arshak_road_length))
        #
        # self.wait(2)

    def get_boy(self, name, svg_name, edge):
        boy_svg = SimpleSVGMobject(svg_name)
        boy = VGroup(boy_svg, Tex(name).next_to(boy_svg, DOWN))
        boy.scale(.7).to_edge(edge, buff=1).shift(UP)
        return boy

    def get_part(self, value, label=None, color=WHITE, **kwargs):
        seg = Segment(
            ORIGIN,
            value * RIGHT,
            label,
            stroke_width=6,
            color=color,
            **kwargs
        )
        return seg
