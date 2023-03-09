from manim import UP, DOWN, LEFT, RIGHT, Scene, PI
from manim import  GREEN, ORANGE
from manim import  VGroup, MathTex, Tex,  SurroundingRectangle, Arrow
from manim import Write, AnimationGroup, FadeOut, Transform, ReplacementTransform
from manim import  smooth
from .text import *

FONT_SIZE = 64
RUN_TIME_SPEED = 3

class DivisibilityRules(Scene):
    def construct(self):

        self.divisibility_of_10()
        self.divisibility_of_5()
        self.divisibility_of_2()

    def loading_animation(self, repeat_number,position,font_size):
        ellipsis = Tex('$.$', '$.$', '$.$',font_size=font_size).next_to(position,RIGHT)
        ellipsis.set_opacity(0)
        self.play(Write(ellipsis))
        for i in range(repeat_number):
            ellipsis.set_opacity(0)
            self.play(ellipsis[0].animate.set_opacity(0.9))
            self.play(ellipsis[1].animate.set_opacity(0.9))
            self.play(ellipsis[2].animate.set_opacity(0.9))
            self.play(ellipsis.animate.set_opacity(0))
            self.wait(0.05)

    def divisibility_of_10(self):
        multiples_of_10_str = Tex('$10$', multiples_are, font_size=FONT_SIZE).shift(UP * 2)
        self.play(Write(multiples_of_10_str, run_time=RUN_TIME_SPEED))
        self.wait()

        multiples_of_10_list_str = '1 {\cdot} 10,2 {\cdot} 10,3 {\cdot} 10,4 {\cdot} 10,5 {\cdot} 10,'

        multiples_of_10 = MathTex(multiples_of_10_list_str, font_size=FONT_SIZE).next_to(multiples_of_10_str,
                                                                                         DOWN).shift(DOWN + LEFT * 2)

        for i in range(2, len(multiples_of_10[0]), 5):
            multiples_of_10[0][i].set_color(ORANGE)
            multiples_of_10[0][i + 1].set_color(ORANGE)
        self.play(Write(multiples_of_10, run_time=RUN_TIME_SPEED))
        self.wait()
        left_shift_factor = 0.5
        self.play(
            AnimationGroup(
                FadeOut(multiples_of_10[0][1], multiples_of_10[0][2]),
                VGroup(multiples_of_10[0][3:28]).animate.shift(LEFT * left_shift_factor)
            ))
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(multiples_of_10[0][6], multiples_of_10[0][7]),
                VGroup(multiples_of_10[0][8:28]).animate.shift(LEFT * left_shift_factor)
            ))
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(
                    multiples_of_10[0][11], multiples_of_10[0][12],
                    multiples_of_10[0][16], multiples_of_10[0][17],
                    multiples_of_10[0][21], multiples_of_10[0][22], run_time=0.1),

                VGroup(multiples_of_10[0][13:16]).animate.shift(LEFT * left_shift_factor),
                VGroup(multiples_of_10[0][18:21]).animate.shift(LEFT * left_shift_factor * 2),
                VGroup(multiples_of_10[0][23:len(multiples_of_10[0])]).animate.shift(LEFT * left_shift_factor * 3)
            ))
        self.wait()
        multiples_of_10_remaining_str = ''
        for i in range(6, 50):
            multiples_of_10_remaining_str += (str(i) + '0,')
        multiples_of_10_remaining = MathTex(multiples_of_10_remaining_str, font_size=FONT_SIZE)
        for i in range(1, 11, 3):
            multiples_of_10_remaining[0][i].set_color(ORANGE)

        for i in range(14, len(multiples_of_10_remaining[0]), 4):
            multiples_of_10_remaining[0][i].set_color(ORANGE)

        self.play(Write(multiples_of_10_remaining.next_to(multiples_of_10[0][24], RIGHT).shift(UP * 0.2),
                        run_time=RUN_TIME_SPEED))
        self.wait()
        multiples = VGroup(multiples_of_10_remaining,
                           multiples_of_10[0][0],
                           multiples_of_10[0][3],
                           multiples_of_10[0][4],
                           multiples_of_10[0][5],
                           multiples_of_10[0][8],
                           multiples_of_10[0][9],
                           multiples_of_10[0][10],
                           multiples_of_10[0][13],
                           multiples_of_10[0][14],
                           multiples_of_10[0][15],
                           multiples_of_10[0][18],
                           multiples_of_10[0][19],
                           multiples_of_10[0][20],
                           multiples_of_10[0][23],
                           multiples_of_10[0][24])
        self.play(multiples.animate(run_time=3).shift(LEFT * 45), rate_func=smooth)
        self.wait()
        self.play(multiples.animate(run_time=2).shift(RIGHT * 45), rate_func=smooth)
        self.wait()
        is_a_divider_text = Tex('$10$', is_a_divider, font_size=FONT_SIZE).shift(UP * 2)

        self.play(FadeOut(multiples_of_10_str))
        self.play(Write(is_a_divider_text, run_time=RUN_TIME_SPEED))
        self.wait()

        self.numbers_divisible_by_10=numbers_divisible_by_10 = Tex(numbers_ending_with_0, font_size=FONT_SIZE).next_to(is_a_divider_text, DOWN).shift(DOWN)
        self.play(FadeOut(multiples))
        self.play(Write(numbers_divisible_by_10, run_time=RUN_TIME_SPEED))
        self.loading_animation(3, numbers_divisible_by_10[0][len(numbers_divisible_by_10[0]) - 1], FONT_SIZE)
        self.wait(0.5)

        no_other_number = Tex(and_no_other_number_str, font_size=FONT_SIZE).next_to(
            numbers_divisible_by_10[0][len(numbers_divisible_by_10[0]) - 1], RIGHT)
        self.play(Write(no_other_number))
        self.wait()

        surrounding_box_numbers_divisible_by_10 = SurroundingRectangle(VGroup(numbers_divisible_by_10, no_other_number),
                                                                       color=GREEN)
        self.play(Write(surrounding_box_numbers_divisible_by_10))
        self.wait()

        self.play(FadeOut(is_a_divider_text))

        self.divisible_by_10_objects =divisible_by_10_objects= VGroup(numbers_divisible_by_10, surrounding_box_numbers_divisible_by_10,
                                         no_other_number)
        self.play(divisible_by_10_objects.animate.shift(UP * 3))
        self.play(VGroup(numbers_divisible_by_10, no_other_number).animate.set_opacity(0.6))
        self.wait()
    def divisibility_of_5(self):
        multiples_of_5_str = Tex('$5$', multiples_are, font_size=FONT_SIZE).next_to(self.divisible_by_10_objects,
                                                                                    DOWN).shift(DOWN * 0.7)
        self.play(Write(multiples_of_5_str, run_time=RUN_TIME_SPEED))
        self.wait()
        multiples_of_5 = ''
        for i in range(1, 12):
            multiples_of_5 += (str(i) + '{\cdot} 5,')

        multiples_of_5_list = MathTex(multiples_of_5, font_size=FONT_SIZE).next_to(multiples_of_5_str, DOWN).shift(
            DOWN + LEFT * 0.5)

        for i in range(2, 36, 4):
            multiples_of_5_list[0][i].set_color(ORANGE)
        multiples_of_5_list[0][39].set_color(ORANGE)
        multiples_of_5_list[0][44].set_color(ORANGE)
        self.play(
            Write(multiples_of_5_list, run_time=RUN_TIME_SPEED))
        self.wait()
        numbers_after_transform = VGroup(
            MathTex('5', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][3], LEFT).shift(UP * 0.3),
            MathTex('10', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][7], LEFT).shift(UP * 0.3),
            MathTex('15', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][11], LEFT).shift(UP * 0.3),
            MathTex('20', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][15], LEFT).shift(UP * 0.3),
            MathTex('25', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][19], LEFT).shift(UP * 0.3),
            MathTex('30', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][23], LEFT).shift(UP * 0.3),
            MathTex('35', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][27], LEFT).shift(UP * 0.3),
            MathTex('40', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][31], LEFT).shift(UP * 0.3),
            MathTex('45', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][35], LEFT).shift(UP * 0.3),
            MathTex('50', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][40], LEFT).shift(UP * 0.3),
            MathTex('55', font_size=FONT_SIZE).next_to(multiples_of_5_list[0][45], LEFT).shift(UP * 0.3),

        )
        self.play(ReplacementTransform(VGroup(multiples_of_5_list[0][0:3]), numbers_after_transform[0]))
        self.wait()

        self.play(ReplacementTransform(VGroup(multiples_of_5_list[0][4:7]), numbers_after_transform[1]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(
            Transform(VGroup(multiples_of_5_list[0][(4 * i - 4):(4 * i - 1)]), numbers_after_transform[i])) for i in
            range(2, 10)],
                                 ReplacementTransform(VGroup(multiples_of_5_list[0][36:40]),
                                                      numbers_after_transform[9]),
                                 ReplacementTransform(VGroup(multiples_of_5_list[0][41:45]),
                                                      numbers_after_transform[10])))
        self.wait()

        multiples_of_5_remaining_str = ''
        for i in range(1, 100):
            multiples_of_5_remaining_str += (str(i * 5) + ',')
        multiples_of_5_remaining = MathTex(multiples_of_5_remaining_str, font_size=FONT_SIZE)
        for i in range(0, 55, 3):
            multiples_of_5_remaining[0][i].set_color(ORANGE)

        for i in range(54, len(multiples_of_5_remaining[0]), 4):
            multiples_of_5_remaining[0][i].set_color(ORANGE)

        multiples_of_5_remaining.next_to(multiples_of_5_list[0], DOWN).align_to(multiples_of_5_list, LEFT)

        self.play(Write(multiples_of_5_remaining, run_time=4))

        arrow_group = VGroup()

        for i in range(1, 100):
            up = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                       max_tip_length_to_length_ratio=0.1, )
            down = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                         max_tip_length_to_length_ratio=0.1).shift(DOWN * 0.4)
            up.rotate(PI / 4)
            down.rotate(-PI / 4)
            group = VGroup(up, down)
            group.scale(0.5)
            final = VGroup()
            final.add(Tex('$0$', font_size=40, color=ORANGE).next_to(group[0], RIGHT).shift(UP * 0.1 + LEFT * 0.2))
            final.add(Tex('$5$', font_size=40, color=ORANGE).next_to(group[1], RIGHT).shift(DOWN * 0.1 + LEFT * 0.2))
            arrow_group += final.add(group)

        self.wait()
        self.play(Transform(multiples_of_5_remaining[0][3],
                            arrow_group[0].next_to(multiples_of_5_remaining[0][4], LEFT).shift(RIGHT * 0.2 + UP * 0.2)))
        self.wait()
        self.play(Transform(multiples_of_5_remaining[0][6],
                            arrow_group[1].next_to(multiples_of_5_remaining[0][7], LEFT).shift(RIGHT * 0.2 + UP * 0.2)))
        self.wait()
        self.play(AnimationGroup(*[Transform(multiples_of_5_remaining[0][3 * i],
                                             arrow_group[i].next_to(multiples_of_5_remaining[0][3 * i + 1], LEFT).shift(
                                                 RIGHT * 0.25 + UP * 0.2))
                                   for i in range(3, 19)]))
        self.play(AnimationGroup(*[Transform(multiples_of_5_remaining[0][54 + 4 * i],
                                             arrow_group[i].next_to(multiples_of_5_remaining[0][4 * i + 55],
                                                                    LEFT).shift(
                                                 RIGHT * 0.25 + UP * 0.2))
                                   for i in range(0, 40)]))

        self.play(multiples_of_5_remaining.animate(run_time=3).shift(LEFT * 40), rate_func=smooth)
        self.wait()
        self.play(multiples_of_5_remaining.animate(run_time=2).shift(RIGHT * 40), rate_func=smooth)
        self.wait()

        numbers_divisible_by_5_rule = Tex(number_divisible_by_5_end_with_0_and_5, font_size=FONT_SIZE).align_to(self.numbers_divisible_by_10,LEFT)
        surrounding_box_numbers_divisible_by_5 = SurroundingRectangle(numbers_divisible_by_5_rule, color=GREEN)
        self.play(AnimationGroup(VGroup(multiples_of_5_str, multiples_of_5_list, multiples_of_5_remaining,
                                        numbers_after_transform).animate.set_opacity(0),
                                 Write(surrounding_box_numbers_divisible_by_5)))
        self.wait()
        self.play(Write(numbers_divisible_by_5_rule))
        self.wait()
        self.divisible_by_5_objects=divisible_by_5_objects = VGroup(numbers_divisible_by_5_rule, surrounding_box_numbers_divisible_by_5)
        self.play(VGroup(divisible_by_5_objects,self.divisible_by_10_objects).animate.shift(UP * 2.3))
        self.play(numbers_divisible_by_5_rule.animate.set_opacity(0.6))
        self.wait()

    def divisibility_of_2(self):
        multiples_of_2_str = Tex('$2$', multiples_are, font_size=FONT_SIZE).next_to(self.divisible_by_5_objects,
                                                                                    DOWN).shift(DOWN )
        self.play(Write(multiples_of_2_str, run_time=RUN_TIME_SPEED))
        self.wait()
        multiples_of_2 = ''
        for i in range(1, 12):
            multiples_of_2 += (str(i) + '{\cdot} 2,')

        multiples_of_2_list = MathTex(multiples_of_2, font_size=FONT_SIZE).next_to(multiples_of_2_str, DOWN).shift(
            DOWN + LEFT * 0.5)

        for i in range(2, 36, 4):
            multiples_of_2_list[0][i].set_color(ORANGE)
        multiples_of_2_list[0][39].set_color(ORANGE)
        multiples_of_2_list[0][44].set_color(ORANGE)
        self.play(
            Write(multiples_of_2_list, run_time=RUN_TIME_SPEED))
        self.wait()
        numbers_after_transform = VGroup(
            MathTex('2', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][3], LEFT).shift(UP * 0.3),
            MathTex('4', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][7], LEFT).shift(UP * 0.3),
            MathTex('6', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][11], LEFT).shift(UP * 0.3),
            MathTex('8', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][15], LEFT).shift(UP * 0.3),
            MathTex('10', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][19], LEFT).shift(UP * 0.3),
            MathTex('12', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][23], LEFT).shift(UP * 0.3),
            MathTex('14', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][27], LEFT).shift(UP * 0.3),
            MathTex('16', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][31], LEFT).shift(UP * 0.3),
            MathTex('18', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][35], LEFT).shift(UP * 0.3),
            MathTex('20', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][40], LEFT).shift(UP * 0.3),
            MathTex('22', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][45], LEFT).shift(UP * 0.3),

        )
        self.play(ReplacementTransform(VGroup(multiples_of_2_list[0][0:3]), numbers_after_transform[0]))
        self.wait()

        self.play(ReplacementTransform(VGroup(multiples_of_2_list[0][4:7]), numbers_after_transform[1]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(
            Transform(VGroup(multiples_of_2_list[0][(4 * i - 4):(4 * i - 1)]), numbers_after_transform[i])) for i in
            range(2, 10)],
                                 ReplacementTransform(VGroup(multiples_of_2_list[0][36:40]),
                                                      numbers_after_transform[9]),
                                 ReplacementTransform(VGroup(multiples_of_2_list[0][41:45]),
                                                      numbers_after_transform[10])))
        self.wait()

        multiples_of_2_remaining_str = ''
        for i in range(1, 151):
            multiples_of_2_remaining_str += (str(i * 2) + ',')
        multiples_of_2_remaining = MathTex(multiples_of_2_remaining_str, font_size=FONT_SIZE)
        for i in range(0, 7, 2):
            multiples_of_2_remaining[0][i].set_color(ORANGE)

        for i in range(9, 144, 3):
            multiples_of_2_remaining[0][i].set_color(ORANGE)

        for i in range(145, len(multiples_of_2_remaining[0]), 4):
            multiples_of_2_remaining[0][i].set_color(ORANGE)

        multiples_of_2_remaining.next_to(multiples_of_2_list[0], DOWN).align_to(multiples_of_2_list, LEFT)

        self.play(Write(multiples_of_2_remaining, run_time=4))

        self.play(multiples_of_2_remaining.animate(run_time=5).shift(LEFT * 80), rate_func=smooth)
        self.wait()
        self.play(multiples_of_2_remaining.animate(run_time=6).shift(RIGHT * 80), rate_func=smooth)
        self.wait()

        numbers_divisible_by_2_rule = Tex(number_divisible_by_2, font_size=FONT_SIZE)
        surrounding_box_numbers_divisible_by_5 = SurroundingRectangle(numbers_divisible_by_2_rule, color=GREEN)
        self.play(AnimationGroup(VGroup(multiples_of_2_str, multiples_of_2_list, multiples_of_2_remaining,
                                        numbers_after_transform).animate.set_opacity(0),
                                 Write(surrounding_box_numbers_divisible_by_5)))
        self.wait()
        self.play(Write(numbers_divisible_by_2_rule, run_time=RUN_TIME_SPEED + 2))
        self.wait()





