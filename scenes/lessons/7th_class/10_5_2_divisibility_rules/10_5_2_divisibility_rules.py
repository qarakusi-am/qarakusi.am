from manim import UP, DOWN, LEFT, RIGHT, Scene, PI
from manim import GREEN, ORANGE, WHITE, BLACK
from manim import VGroup, MathTex, Tex, SurroundingRectangle, Arrow, Animation
from manim import Write, AnimationGroup, FadeOut, Transform, ReplacementTransform
from manim import smooth
from .text import *

FONT_SIZE = 64
RUN_TIME_SPEED = 3


class DivisibilityRules(Scene):
    def construct(self):

        self.divisibility_of_10()
        self.divisibility_of_5()
        self.divisibility_of_2()

    def loading_animation(self, repeat_number, position, font_size):
        ellipsis = Tex('$.$', '$.$', '$.$', font_size=font_size).next_to(position, RIGHT)
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

        multiples_of_10_list_str = '1 {\cdot} 10,2 {\cdot} 10,3 {\cdot} 10,4 {\cdot} 10,5 {\cdot} 10'

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
        multiples_of_10_remaining_str = ' ,'
        for i in range(6, 50):
            multiples_of_10_remaining_str += (str(i) + '0,')
        multiples_of_10_remaining = MathTex(multiples_of_10_remaining_str, font_size=FONT_SIZE)
        for i in range(2, 12, 3):
            multiples_of_10_remaining[0][i].set_color(ORANGE)

        for i in range(15, len(multiples_of_10_remaining[0]), 4):
            multiples_of_10_remaining[0][i].set_color(ORANGE)

        self.play(Write(multiples_of_10_remaining.next_to(multiples_of_10[0][23], RIGHT).shift(DOWN * 0.05),
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
                           multiples_of_10[0][23])
        self.play(multiples.animate(run_time=3).shift(LEFT * 45), rate_func=smooth)
        self.wait()
        self.play(multiples.animate(run_time=2).shift(RIGHT * 45), rate_func=smooth)
        self.wait()
        is_a_divisor_text = Tex('$10$', is_a_divisor, font_size=FONT_SIZE).shift(UP * 2)

        self.play(FadeOut(multiples_of_10_str))
        self.play(Write(is_a_divisor_text, run_time=RUN_TIME_SPEED))
        self.wait()

        self.numbers_divisible_by_10 = numbers_divisible_by_10 = Tex(numbers_ending_with_0,
                                                                     font_size=FONT_SIZE).next_to(is_a_divisor_text,
                                                                                                  DOWN).shift(DOWN)
        self.play(FadeOut(multiples, is_a_divisor_text))
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

        self.divisible_by_10_objects = divisible_by_10_objects = VGroup(numbers_divisible_by_10,
                                                                        surrounding_box_numbers_divisible_by_10,
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

        multiples_of_5_list = MathTex(multiples_of_5, font_size=FONT_SIZE+5).next_to(multiples_of_5_str, DOWN).shift(
            DOWN + LEFT * 0.5)

        for i in range(2, 36, 4):
            multiples_of_5_list[0][i].set_color(ORANGE)
        multiples_of_5_list[0][39].set_color(ORANGE)
        multiples_of_5_list[0][44].set_color(ORANGE)
        self.play(
            Write(multiples_of_5_list, run_time=RUN_TIME_SPEED))
        self.wait()

        numbers_after_transform = VGroup(
            MathTex('5', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][3], LEFT).shift(UP * 0.3),
            MathTex('10', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][7], LEFT).shift(UP * 0.3),
            MathTex('15', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][11], LEFT).shift(UP * 0.3),
            MathTex('20', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][15], LEFT).shift(UP * 0.3),
            MathTex('25', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][19], LEFT).shift(UP * 0.3),
            MathTex('30', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][23], LEFT).shift(UP * 0.3),
            MathTex('35', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][27], LEFT).shift(UP * 0.3),
            MathTex('40', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][31], LEFT).shift(UP * 0.3),
            MathTex('45', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][35], LEFT).shift(UP * 0.3),
            MathTex('50', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][40], LEFT).shift(UP * 0.3),
            MathTex('55', font_size=FONT_SIZE + 5).next_to(multiples_of_5_list[0][45], LEFT).shift(UP * 0.3),

        )
        self.play(ReplacementTransform(VGroup(multiples_of_5_list[0][0:3]), numbers_after_transform[0]))
        self.wait()

        self.play(ReplacementTransform(VGroup(multiples_of_5_list[0][4:7]), numbers_after_transform[1]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(
            Transform(VGroup(multiples_of_5_list[0][(4 * i):(4 * i + 3)]), numbers_after_transform[i])) for i in
            range(2, 10)],
                                 ReplacementTransform(VGroup(multiples_of_5_list[0][36:40]),
                                                      numbers_after_transform[9]),
                                 ReplacementTransform(VGroup(multiples_of_5_list[0][41:45]),
                                                      numbers_after_transform[10])))
        self.wait()

        arrow_group = VGroup()

        for i in range(1, 16):
            up = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                       max_tip_length_to_length_ratio=0.1, )
            down = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                         max_tip_length_to_length_ratio=0.1).shift(DOWN * 0.4)
            up.rotate(PI / 4)
            down.rotate(-PI / 4)
            group = VGroup(up, down)
            group.scale(0.5)
            final = VGroup()
            final.add(Tex('$0$', font_size=50, color=ORANGE).next_to(group[0], RIGHT).shift(UP * 0.1 + LEFT * 0.2))
            final.add(Tex('$5$', font_size=50, color=ORANGE).next_to(group[1], RIGHT).shift(DOWN * 0.1 + LEFT * 0.2))
            arrow_group += final.add(group)

        self.wait()
        self.play(AnimationGroup(*[AnimationGroup(numbers_after_transform[i][0][1].animate.set_color(ORANGE),
                                                  numbers_after_transform[0][0][0].animate.set_color(ORANGE))
                                   for i in range(1, len(numbers_after_transform))]))

        self.wait()
        self.play(AnimationGroup(
            multiples_of_5_list[0][8].animate.set_opacity(0),
            multiples_of_5_list[0][7].animate.set_opacity(0),
        ))
        self.wait()
        multiples_of_5_list[0][10].set_opacity(0),

        self.play(AnimationGroup(numbers_after_transform[1][0][1].animate.scale(1 / 1.48).shift(UP * 0.2),
                                 numbers_after_transform[2][0][1].animate.next_to(numbers_after_transform[1][0][1],
                                                                                  DOWN).scale(1 / 1.48).shift(
                                     UP * 0.4)))
        self.wait()

        up = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                   max_tip_length_to_length_ratio=0.1, )
        down = Arrow(start=LEFT, end=[0, 0, 0], max_stroke_width_to_length_ratio=2,
                     max_tip_length_to_length_ratio=0.1).shift(DOWN * 0.4)
        up.rotate(PI / 4)
        down.rotate(-PI / 4)
        group = VGroup(up, down)
        group.scale(0.5).next_to(multiples_of_5_list[0][3], RIGHT).shift(UP * 0.3 + RIGHT * 0.2)
        self.play(Write(group))
        self.wait()
        VGroup(multiples_of_5_list[0][14:19]).set_opacity(0)
        VGroup(multiples_of_5_list[0][21:27]).set_opacity(0)
        VGroup(multiples_of_5_list[0][29:35]).set_opacity(0)
        VGroup(multiples_of_5_list[0][36:41]).set_opacity(0)

        self.play(AnimationGroup(Transform(
            VGroup(numbers_after_transform[3][0][1], numbers_after_transform[4], multiples_of_5_list[0][14:19]),
            arrow_group[0].next_to(numbers_after_transform[3][0][0], RIGHT).shift(LEFT * 0.2)),
                                 Transform(
                                     VGroup(numbers_after_transform[5][0][1], numbers_after_transform[6],
                                            multiples_of_5_list[0][21:27]),
                                     arrow_group[1].next_to(numbers_after_transform[5][0][0], RIGHT).shift(LEFT * 0.2))
                                 ),
        Transform(
            VGroup(numbers_after_transform[7][0][1], numbers_after_transform[8], multiples_of_5_list[0][29:35]),
            arrow_group[2].next_to(numbers_after_transform[7][0][0], RIGHT).shift(LEFT * 0.2)),
        Transform(
            VGroup(numbers_after_transform[9][0][1], numbers_after_transform[10], multiples_of_5_list[0][36:41]),
            arrow_group[3].next_to(numbers_after_transform[9][0][0], RIGHT).shift(LEFT * 0.2)))

        self.wait()
        numbers_divisible_by_5_rule = Tex(number_divisible_by_5_end_with_0_and_5, font_size=FONT_SIZE).align_to(
            self.numbers_divisible_by_10, LEFT)
        surrounding_box_numbers_divisible_by_5 = SurroundingRectangle(numbers_divisible_by_5_rule, color=GREEN)
        VGroup( multiples_of_5_list, numbers_after_transform,group).set_opacity(0)

        self.play(multiples_of_5_str.animate.set_opacity(0))
        self.play(Write(surrounding_box_numbers_divisible_by_5))
        self.wait()
        self.play(Write(numbers_divisible_by_5_rule))
        self.wait()
        self.divisible_by_5_objects = divisible_by_5_objects = VGroup(numbers_divisible_by_5_rule,
                                                                      surrounding_box_numbers_divisible_by_5)
        self.play(VGroup(divisible_by_5_objects, self.divisible_by_10_objects).animate.shift(UP * 2.3))
        self.play(numbers_divisible_by_5_rule.animate.set_opacity(0.6))
        self.wait()

    def divisibility_of_2(self):
        multiples_of_2_str = Tex('$2$', multiples_are, font_size=FONT_SIZE).next_to(self.divisible_by_5_objects,
                                                                                    DOWN).shift(DOWN)
        self.play(Write(multiples_of_2_str, run_time=RUN_TIME_SPEED))
        self.wait()
        multiples_of_2 = ''
        for i in range(1, 12):
            multiples_of_2 += (str(i) + '{\cdot} 2,')

        for i in range(12, 85):
            multiples_of_2 += (str(i * 2) + ',')
        multiples_of_2_list = MathTex(multiples_of_2, font_size=FONT_SIZE).align_to(multiples_of_2_str, LEFT).shift(
            DOWN*2.4 + LEFT *2.5)

        for i in range(2, 36, 4):
            multiples_of_2_list[0][i].set_color(ORANGE)
        multiples_of_2_list[0][39].set_color(ORANGE)
        multiples_of_2_list[0][44].set_color(ORANGE)


        for i in range(47, 159, 3):
            multiples_of_2_list[0][i].set_color(ORANGE)

        for i in range(162, len(multiples_of_2_list[0]), 4):
            multiples_of_2_list[0][i].set_color(ORANGE)
        self.play(
            Write(multiples_of_2_list, run_time=RUN_TIME_SPEED))
        self.wait()
        numbers_after_transform = VGroup(
            MathTex('2', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][3], LEFT).shift(UP * 0.25),
            MathTex('4', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][7], LEFT).shift(UP * 0.25),
            MathTex('6', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][11], LEFT).shift(UP * 0.25),
            MathTex('8', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][15], LEFT).shift(UP * 0.25),
            MathTex('10', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][19], LEFT).shift(UP * 0.25),
            MathTex('12', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][23], LEFT).shift(UP * 0.25),
            MathTex('14', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][27], LEFT).shift(UP * 0.25),
            MathTex('16', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][31], LEFT).shift(UP * 0.25),
            MathTex('18', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][35], LEFT).shift(UP * 0.25),
            MathTex('20', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][40], LEFT).shift(UP * 0.25),
            MathTex('22', font_size=FONT_SIZE).next_to(multiples_of_2_list[0][45], LEFT).shift(UP * 0.25),

        )
        for i in range(0,4):
            numbers_after_transform[i][0][0].set_color(ORANGE)
        for i in range(4,len(numbers_after_transform)):
            numbers_after_transform[i][0][1].set_color(ORANGE)

        self.play(Transform(VGroup(multiples_of_2_list[0][0:3]), numbers_after_transform[0]))
        self.wait()

        self.play(Transform(VGroup(multiples_of_2_list[0][4:7]), numbers_after_transform[1]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(
            Transform(VGroup(multiples_of_2_list[0][(4 * i ):(4 * i +3)]), numbers_after_transform[i])) for i in
            range(2, 10)],
                                 Transform(VGroup(multiples_of_2_list[0][36:40]),
                                                      numbers_after_transform[9]),
                                 Transform(VGroup(multiples_of_2_list[0][41:45]),
                                                      numbers_after_transform[10])))
        self.wait()


        self.play(multiples_of_2_list.animate(run_time=5).shift(LEFT * 60), rate_func=smooth)
        self.wait()
        self.play(AnimationGroup(*[multiples_of_2_list[0][i].animate.scale(1.4)
                                   for i in range(162, len(multiples_of_2_list[0]), 4)]))
        self.wait()
        self.play(AnimationGroup(*[multiples_of_2_list[0][i].animate.scale(1 / 1.4)
                                   for i in range(162, len(multiples_of_2_list[0]), 4)]))
        self.wait()
        for i in range(0,4):
            numbers_after_transform[i][0][0].set_color(WHITE)
        for i in range(4,len(numbers_after_transform)):
            numbers_after_transform[i][0][1].set_color(WHITE)
        self.play(
            VGroup(multiples_of_2_list[0][0:202],multiples_of_2_list[0][203:206],multiples_of_2_list[0][207:210],multiples_of_2_list[0][211:214],
                   multiples_of_2_list[0][215:218],multiples_of_2_list[0][219:len(multiples_of_2_list[0])-1],).animate.set_opacity(0))
        self.wait()

        numbers_divisible_by_2_rule = Tex(number_divisible_by_2, font_size=FONT_SIZE)
        surrounding_box_numbers_divisible_by_2 = SurroundingRectangle(numbers_divisible_by_2_rule, color=GREEN,buff=0.6).align_to(self.divisible_by_5_objects,LEFT).shift(DOWN*0.3)
        self.play(AnimationGroup(multiples_of_2_str.animate.set_opacity(0),
                                 Write(surrounding_box_numbers_divisible_by_2)))
        self.wait()


        self.wait()
        numbers_divisible_by_2_rule[0][19].set_opacity(0)
        numbers_divisible_by_2_rule[0][29].set_opacity(0)
        numbers_divisible_by_2_rule[0][24].set_opacity(0)
        numbers_divisible_by_2_rule[0][14].set_opacity(0)
        numbers_divisible_by_2_rule[0][36].set_opacity(0)
        numbers_divisible_by_2_rule[0][15:72].set_opacity(0)

        self.play(Write(numbers_divisible_by_2_rule[0:14]))
        self.play(AnimationGroup(
            multiples_of_2_list[0][202].animate(run_time=0.5).move_to(numbers_divisible_by_2_rule[0][14]),
            VGroup(numbers_divisible_by_2_rule[0][15:19]).animate(run_time=2.5).set_opacity(1)))

        self.play(AnimationGroup(multiples_of_2_list[0][206].animate(run_time=0.5).move_to(numbers_divisible_by_2_rule[0][19]),
                                 VGroup(numbers_divisible_by_2_rule[0][20:24]).animate(run_time=2.5).set_opacity(1)))
        self.wait(0)

        self.play(AnimationGroup(
            multiples_of_2_list[0][210].animate(run_time=0.5).move_to(numbers_divisible_by_2_rule[0][24]),
            VGroup(numbers_divisible_by_2_rule[0][25:29]).animate(run_time=2.5).set_opacity(1)))
        self.wait(0)
        self.play(AnimationGroup(
            multiples_of_2_list[0][214].animate(run_time=0.5).move_to(numbers_divisible_by_2_rule[0][29]),
            VGroup(numbers_divisible_by_2_rule[0][30:33]).animate(run_time=2.5).set_opacity(1)))
        self.wait(0)
        self.play(AnimationGroup(
            multiples_of_2_list[0][218].animate(run_time=0.5).move_to(numbers_divisible_by_2_rule[0][36]),
            VGroup(numbers_divisible_by_2_rule[0][37:40],numbers_divisible_by_2_rule[0][33:36]).animate(run_time=2.5).set_opacity(1)))
        self.wait(0)

        self.play(VGroup(numbers_divisible_by_2_rule[0][40:72]).animate.set_opacity(1))
        self.wait()
