from manim import *
from math import floor
from functools import reduce

from aramanim import Segment, Run, Reset, CutIn, CutOut
from qarakusiscene import TaskNumberBox
from objects import SimpleSVGMobject, Stopwatch, DScissors, Car
from .text import km, souren_string, arshak_string, task_number_string, condition1_string, condition2_string, \
    condition3_string, condition4_string, road_len, road_length_string, meeting_time_string, \
    souren_time_string, arshak_time_string, souren_time_amount, arshak_time_amount, segment_10_string, \
    hour_string, question_mark_string, cut_road_length_string, arshak_one_part_len_string, \
    souren_recap_s_string, arshak_recap_s_string, souren_recap_v_string, arshak_recap_v_string, \
    souren_one_part_len_string

scale = .02



def flatten_list(lst):
    return sum(lst, [])


class Problem10349(Scene):
    def construct(self):
        self.wait()
        colors = [BLUE, RED]
        task_number = TaskNumberBox(task_number_string)
        self.play(FadeIn(task_number))

        souren, arshak = [self.get_boy(boy_name, f'boy_{idx + 1}', pos, c)
                          for (idx, boy_name), pos, c in zip(enumerate([souren_string, arshak_string]), [LEFT, RIGHT], colors)]
        boys = [souren, arshak]

        # # պայմաններ ###############################################################################
        condition1 = Tex(*condition1_string).scale(.7).to_edge(UP, buff=0.8).shift(LEFT * 0.6)
        condition2 = Tex(*condition2_string).scale(.7).next_to(condition1, DOWN, buff=0.3).align_to(condition1, LEFT)
        condition3 = Tex(*condition3_string).scale(.7).next_to(condition2, DOWN, buff=0.3).align_to(condition2, LEFT)
        condition4 = Tex(*condition4_string).scale(.7).next_to(condition3, DOWN, buff=0.3).align_to(condition3, LEFT)
        conditions = [condition1, condition2, condition3, condition4]
        for c in conditions:
            c[0].set_color(ORANGE)
        check_marks = [
            SimpleSVGMobject('check').scale(0.1).align_to(condition, UL).shift(LEFT * 0.3)
            for condition in conditions
        ]
        # ##########################################################################################

        self.play(FadeIn(souren), FadeIn(arshak))
        self.wait()

        # Ճանապարհի մասին տվյալների համառոտագրություն
        road = self.get_part(value=road_len).scale(scale).next_to(souren, DOWN * 1.7 + RIGHT, buff=1)
        road_length = Tex(road_length_string).next_to(road, DOWN, buff=0.3)
        self.play(Write(conditions[0]))
        self.wait()
        self.play(GrowFromEdge(road, LEFT), Write(road_length))
        self.wait()
        self.play(Write(check_marks[0]))

        # Սուրենի և Արշակի ճանապարհների մասերը
        souren_road = self.get_part(value=250, color=BLUE).scale(scale).next_to(road.left_edge, buff=0)
        arshak_road = self.get_part(value=180, color=RED).scale(scale).next_to(road.right_edge, LEFT, buff=0)
        roads = [souren_road, arshak_road]
        self.play(GrowFromEdge(souren_road, LEFT))
        self.play(GrowFromEdge(arshak_road, RIGHT))

        # Քաղաքի անիմացիա
        city = SimpleSVGMobject("city_1").next_to(souren_road.get_edge_center(RIGHT), UP * 1.3, buff=1).scale(0.7)
        meeting_t = MathTex(meeting_time_string, color=BLUE_B).next_to(city, 0.5 * DOWN, buff=.3)
        self.play(FadeIn(city))
        self.play(Write(meeting_t))
        self.wait()

        # Սուրենի և Արշակի ժամերի համառոտագրություն
        time_strings = [souren_time_string, arshak_time_string]

        souren_t, arshak_t = [
            MathTex(time_str, color=c).next_to(boy, DOWN, buff=.3)
            for time_str, boy, c in zip(time_strings, boys, colors)
        ]

        self.play(Write(souren_t), Write(conditions[1]))
        self.wait()
        self.play(Write(arshak_t), Write(conditions[2]))
        self.wait()

        # Սուրենի և Արշակի հանդիպման անիմացիա
        souren_car = Car('car_1').scale(0.3).align_to(souren_road, UL).shift(UP * 0.5).shift(LEFT * 1.4)
        arshak_car = Car('car_2').scale(0.3).align_to(arshak_road, UR).shift(UP * 0.6).shift(RIGHT * 1.8).flip()
        cars = [souren_car, arshak_car]
        self.play(*[FadeIn(car) for car in cars])

        souren_car_move, arshak_car_move = [
            car.animate(rate_func=linear, run_time=run_time).align_to(road, align_pos).shift(UP * 0.5 + shift_pos * 0.1)
            for car, run_time, road, align_pos, shift_pos in zip(
                cars, [souren_time_amount, arshak_time_amount], roads, [UR, UL], [LEFT, RIGHT]
            )
        ]
        self.play(AnimationGroup(souren_car_move, arshak_car_move, lag_ratio=0.4))
        self.wait()
        self.play(Write(check_marks[1]), Write(check_marks[2]))
        self.wait()

        self.play(
            AnimationGroup(
                VGroup(road, road_length, *roads, *cars).animate.to_edge(DOWN, buff=0.5),
                FadeOut(city),
                FadeOut(meeting_t),
                lag_ratio=0.2
            )
        )

        self.remove(city, meeting_t)

        self.wait()
        self.play(FadeOut(souren_car), FadeOut(arshak_car))
        self.wait()

        self.play(Write(conditions[3]))
        self.wait()
        self.play(Circumscribe(VGroup(check_marks[3], conditions[3])))
        self.wait()

        # Մեկ մասի և հավելյալ մասի պատկերում
        one_part = self.get_part(value=50, color=GREEN).scale(scale).next_to(souren, UP, buff=0.3)
        self.play(GrowFromEdge(one_part, LEFT))
        one_part_copy = one_part.copy()
        self.play(FadeIn(one_part_copy))
        self.play(one_part_copy.animate.next_to(arshak, UP).align_to(one_part, UP))
        self.wait()
        segment_10 = self.get_part(int(segment_10_string), color=YELLOW).scale(scale).next_to(one_part_copy, buff=0)
        segment_10.set_label(MathTex(segment_10_string))
        segment_10_label = segment_10.update_label_pos(buff=.17)
        self.play(
            GrowFromEdge(segment_10, LEFT),
            Write(segment_10_label),
        )
        self.wait()
        self.play(Write(check_marks[3]))
        self.wait()

        # Սուրենի ժամերի ընդգծում
        self.play(Indicate(souren_t))
        self.wait()

        # Սուրենի ժամացույցի անիմացիա
        stopwatch = Stopwatch()
        stopwatch.scale(.4).next_to(condition4, DOWN, buff=0.5)
        timer = always_redraw(
            lambda: MathTex(str(floor(stopwatch.time.get_value() // 60)), hour_string).next_to(
                stopwatch, DOWN) if floor(stopwatch.time.get_value() // 60) != 0 else MathTex(""))
        self.add(timer)
        self.play(FadeIn(stopwatch))
        timer_animation = Run(stopwatch, speed=60, run_time=souren_time_amount)

        # Սուրենի ճանապարհի մասերի պատկերում
        x5_one_part = [one_part.copy() for i in range(souren_time_amount)]
        road_animation_part1 = AnimationGroup(
            *[x5_one_part[i].animate.next_to(souren_road.left_edge, buff=i * 50 * scale) for i in
              range(souren_time_amount)],
            run_time=souren_time_amount, lag_ratio=1)

        self.play(road_animation_part1, timer_animation, rate_func=linear, run_time=souren_time_amount)
        self.wait()

        # Սուրենի ժամի ցուցադրում ճանապարհի վրա
        souren_road_brace = Brace(souren_road, UP, buff=.08)
        souren_road_time = timer.copy().next_to(souren_road, UP, buff=.5).set_color(BLUE)
        self.play(FadeIn(souren_road_brace))
        self.play(ReplacementTransform(timer, souren_road_time), FadeOut(stopwatch))
        self.wait()
        self.remove(stopwatch)
        self.remove(timer)

        # Արշակի ժամերի ընդգծում
        self.play(Indicate(arshak_t))
        self.wait()

        # Արշակի ժամացույցի անիմացիա
        stopwatch = Stopwatch()
        stopwatch.scale(.4).next_to(condition4, DOWN, buff=0.5)
        timer = always_redraw(
            lambda: MathTex(str(floor(stopwatch.time.get_value() // 60)), hour_string).next_to(
                stopwatch, DOWN) if floor(stopwatch.time.get_value() // 60) != 0 else MathTex(""))
        self.add(timer)
        timer_animation = Run(stopwatch, speed=60, run_time=arshak_time_amount)
        self.play(FadeIn(stopwatch))
        self.wait()

        # Արշակի ճանապարհի մասերի պատկերում
        x3_one_part_and_10 = [VGroup(one_part_copy.copy(), segment_10.copy()) for _ in range(arshak_time_amount)]
        for obj in x3_one_part_and_10:
            self.bring_to_front(obj)
        road_animation_part2 = AnimationGroup(
            *[x3_one_part_and_10[i].animate.next_to(arshak_road.right_edge, buff=-((i + 1) * 60 * scale)) for i in
              range(arshak_time_amount)], run_time=arshak_time_amount, lag_ratio=1)
        self.play(road_animation_part2, timer_animation, rate_func=linear, run_time=arshak_time_amount)
        arshak_road_brace = Brace(arshak_road, UP, buff=.08)
        arshak_road_time = timer.copy().next_to(arshak_road, UP, buff=.5).set_color(RED)
        self.play(FadeIn(arshak_road_brace))
        self.play(ReplacementTransform(timer, arshak_road_time), FadeOut(stopwatch))

        road_group = VGroup(souren_road, souren_road_time,
                            arshak_road, arshak_road_time)
        road_group.save_state()

        self.wait()

        # Մեկ մասի հարցական նշանները
        question_mark_1 = MathTex(question_mark_string).next_to(one_part, UP, buff=.2)
        question_mark_2 = MathTex(question_mark_string).next_to(one_part_copy, UP, buff=.2)
        self.play(FadeIn(question_mark_1), FadeIn(question_mark_2))
        self.wait()
        self.play(FadeOut(question_mark_1), FadeOut(question_mark_2))
        self.wait()

        # Հեռցնենք պայմանները
        checks_and_conditions = [[FadeOut(check_marks[i]), FadeOut(conditions[i])] for i in range(len(conditions))]
        self.play(AnimationGroup(
            *flatten_list(checks_and_conditions),
            lag_ratio=0.3,
            run_time=1
        ))

        # Դեղինով շրջապտույտ նդգծենք 10֊երի շուրջ
        self.play(*[Circumscribe(x3_one_part_and_10[i][1], fade_out=True) for i in range(3)])
        road_new = VGroup(*[x3_one_part_and_10[i] for i in reversed(range(3))], *[x5_one_part[i] for i in range(5)])
        self.wait()
        self.play(
            FadeOut(
                road, souren_road, arshak_road,
                souren_road_time, arshak_road_time,
                road_length, souren_t, arshak_t,
                souren_road_brace, arshak_road_brace
            ),
            road_new.animate.align_to(souren_t, DOWN)
        )
        self.remove(road, souren_road, arshak_road)
        self.wait()

        # Հաշվենք 1-ից մինչև 8 մասերը
        count_x8_one_part_labels = [
            *[Tex(str(i + 1)).next_to(x5_one_part[i], UP) for i in range(5)],
            *[Tex(str(8 - i)).next_to(x3_one_part_and_10[i][0], UP) for i in range(3)]
        ]
        count_x8_one_part_animation = AnimationGroup(
            *[Write(count_x8_one_part_labels[i]) for i in range(5)],
            *[Write(count_x8_one_part_labels[i + 5]) for i in reversed(range(3))],
            lag_ratio=.5, run_time=2
        )
        self.play(count_x8_one_part_animation)
        self.play(
            *[FadeOut(count_x8_one_part_labels[i]) for i in range(8)]
        )

        # Մկրատով կտրենք 10-երը
        scissors = [
            *[DScissors(x3_one_part_and_10[i][1].left_edge.get_center())
              for i in range(len(x3_one_part_and_10))],
            *[DScissors(x3_one_part_and_10[len(x3_one_part_and_10) - 1 - i][1].right_edge.get_center())
              for i in range(len(x3_one_part_and_10) - 1)]
        ]
        self.play(*[CutIn(scissors[i]) for i in range(len(scissors) - 2)])
        self.play(*[CutOut(scissors[i]) for i in range(len(scissors) - 2)])
        self.play(*[CutIn(scissors[i + 3]) for i in range(len(scissors) - 3)])
        self.play(*[CutOut(scissors[i + 3]) for i in range(len(scissors) - 3)])

        for i in range(len(x3_one_part_and_10)):
            x3_one_part_and_10[i][1].set_label(Tex(segment_10_string))

        segment_10_labels = [segment_10_label.copy() for _ in range(len(x3_one_part_and_10))]

        self.play(AnimationGroup(
            *[x3_one_part_and_10[i][1].animate.shift(UP * .5) for i in range(len(x3_one_part_and_10))],
            *[segment_10_labels[i].animate.next_to(x3_one_part_and_10[i][1], UP, buff=0.7)
              for i in range(len(x3_one_part_and_10))],
            lag_ratio=0.2), run_time=1)
        self.wait()

        # Ձևավոր փակագծեր ամբողջ ճանապարհին
        entire_road = VGroup(
            *[x5_one_part[i] for i in range(len(x5_one_part))],
            *[x3_one_part_and_10[i] for i in range(len(x3_one_part_and_10))],
        )

        entire_road_brace = Brace(entire_road, DOWN)
        entire_road_brace_label = Tex(road_length_string).next_to(entire_road_brace, DOWN, buff=0.5)
        self.play(
            GrowFromCenter(entire_road_brace),
            Write(entire_road_brace_label)
        )
        self.wait()

        # Ամբողջ ճանապարհից 10-երը հանելու հավասարումը
        minus_parts = road_len - 3 * int(segment_10_string)
        x8_part_value = MathTex(f"{road_len}-3\cdot{segment_10_string}={minus_parts}").to_edge(
            RIGHT, buff=3.5).to_edge(UP, buff=1)
        self.play(Write(x8_part_value))
        self.wait()
        self.play(
            FadeOut(
                *[x3_one_part_and_10[i][1] for i in range(len(x3_one_part_and_10))],
                *segment_10_labels[::-1]
            )
        )

        # Ամբողջ ճանապարհից 10-երը հանելու ձևավոր փակագծերը
        x8_one_part = VGroup(*[one_part.copy() for _ in range(8)]).arrange(RIGHT, buff=0).align_to(x5_one_part[0], LEFT+UP)
        x8_one_part_brace = Brace(x8_one_part, DOWN)
        x8_one_part_brace_label = MathTex(cut_road_length_string).next_to(x8_one_part_brace, DOWN, buff=0.5)
        self.play(
            ReplacementTransform(
                VGroup(
                    *[x5_one_part[i] for i in range(len(x5_one_part))],
                    *[x3_one_part_and_10[i][0] for i in reversed(range(len(x3_one_part_and_10)))]
                ),
                x8_one_part
            ),
            ReplacementTransform(entire_road_brace, x8_one_part_brace),
            ReplacementTransform(entire_road_brace_label, x8_one_part_brace_label)
        )
        self.wait()

        # Մեկ մասը գտնելու հավասարումը
        one_part_value = MathTex("400:8=").next_to(x8_part_value, DOWN, buff=.4).align_to(x8_part_value, LEFT)
        fifty = MathTex("50").next_to(one_part_value, RIGHT, buff=0.15)
        one_part_label = fifty.copy()
        one_part_copy_label = fifty.copy()
        self.play(Write(one_part_value))
        self.play(Write(fifty))
        self.wait()
        self.play(
            one_part_label.animate.move_to(one_part, UP).align_to(segment_10_label, UP).set_color(GREEN),
            one_part_copy_label.animate.move_to(one_part_copy, UP).align_to(segment_10_label, UP).set_color(GREEN),
        )
        self.wait()

        # Մեկ մաս+10֊ը գտնելու հավասարումը
        one_part_and_10_value = MathTex("50+10=").next_to(
            one_part_value, DOWN, buff=.4).align_to(one_part_value, LEFT)
        sixty = MathTex("60").next_to(one_part_and_10_value, RIGHT, buff=0.15)
        one_part_and_10_label = sixty.copy()
        self.play(Write(one_part_and_10_value))
        self.play(Write(sixty))
        self.wait()

        one_part_and_10_brace = Brace(VGroup(one_part_copy, segment_10), UP)
        self.play(
            ReplacementTransform(VGroup(one_part_copy_label, segment_10_label), one_part_and_10_brace),
            one_part_and_10_label.animate.next_to(one_part_and_10_brace, UP, buff=0.1),
            one_part_and_10_label.animate.become(Tex(arshak_one_part_len_string).next_to(one_part_and_10_brace, UP, .05).set_color(RED)),
            one_part_label.animate.become(Tex(souren_one_part_len_string).next_to(one_part, UP, .05).set_color(BLUE))
        )

        self.play(FadeOut(x8_one_part), FadeOut(x8_one_part_brace), FadeOut(x8_one_part_brace_label),
                  FadeOut(x8_one_part_brace), FadeOut(x8_one_part))

        # Վերականգնենք սկզբնական ճանապարհի գրաֆիկը ու տեսնենք վերջնական ինչ ստացվեց
        road_group.restore().align_to(souren_t, DOWN).scale(0.9)
        self.play(FadeIn(road_group))
        self.wait()

        souren_road_length = MathTex(r"5\cdot50=250" + km, color=BLUE).next_to(souren_road, DOWN, buff=.5).scale(0.9)
        self.play(Write(souren_road_length))
        self.wait()
        arshak_road_length = MathTex(r"3\cdot60=180" + km, color=RED).next_to(arshak_road, DOWN, buff=.5).scale(0.9)
        self.play(Write(arshak_road_length))

        recap_souren_s = MathTex(souren_recap_s_string, color=BLUE).scale(0.7).align_to(souren_t, DL)
        recap_arshak_s = MathTex(arshak_recap_s_string, color=RED).scale(0.7).align_to(arshak_t, DL)
        recap_souren_v = MathTex(souren_recap_v_string, color=BLUE).scale(0.7).next_to(
            recap_souren_s, DL, buff=0.3).align_to(recap_souren_s, LEFT)
        recap_arshak_v = MathTex(arshak_recap_v_string, color=RED).scale(0.7).next_to(
            recap_arshak_s, DL, buff=0.3).align_to(recap_arshak_s, LEFT)
        self.play(
            AnimationGroup(
                Write(recap_souren_s), Write(recap_arshak_s), Write(recap_souren_v), Write(recap_arshak_v), lag_ratio=1
            )
        )

        self.wait(2)

    def get_boy(self, name, svg_name, edge, color=WHITE):
        boy_svg = SimpleSVGMobject(svg_name)
        boy = VGroup(boy_svg, Tex(name).next_to(boy_svg, DOWN).set_color(color))
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
