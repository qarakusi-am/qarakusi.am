from manim import Scene, FadeIn, Tex, MathTex, Write, VGroup, AnimationGroup, Transform, Indicate, Table, \
    ReplacementTransform, Group, Wiggle, ORANGE, FadeOut, CurvedArrow
from manim import UL, UP, UR, DOWN, RIGHT, LEFT, ORIGIN
from qarakusiscene import TaskNumberBox
from objects import BagOfMandarins, SimpleSVGMobject
from numpy import pi, array
from .text import *

FONT_SIZE = 47


class Problem12804(Scene):
    def construct(self):
        # task number
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # Fade in the bookshelf
        bookshelf = SimpleSVGMobject("banana").shift(DOWN)

        self.play(FadeIn(bookshelf))
        self.wait()

        # problem settings
        problem_settings = VGroup(
            Tex(problem_setting_1_part_1, problem_setting_1_part_2, font_size=FONT_SIZE).to_edge(UP).shift(
                DOWN * 0.5).align_to(taskNumber, LEFT),
            Tex(problem_setting_2_part_1, problem_setting_2_part_2, font_size=FONT_SIZE).to_edge(UP).shift(
                DOWN * 1.2).align_to(taskNumber, LEFT),
            Tex(problem_setting_part3, font_size=FONT_SIZE).to_edge(UP).shift(DOWN * 1.9).align_to(taskNumber, LEFT))

        problem_settings.set_color_by_gradient("#CFC748", "#7FC381")

        for item in problem_settings:
            self.play(Write(item, run_time=2.2))
            self.wait(1.5)

        book_count_variable = Tex(book_count_x, font_size=FONT_SIZE).shift(UP * 0.6),

        self.play(ReplacementTransform(bookshelf, book_count_variable[0]))
        self.wait()

        # write problem settings part 1 in terms of x
        self.play(problem_settings[0].animate.shift(DOWN * 3.3))
        self.wait()

        helpers_for_part1 = VGroup(
            Tex("$(x - 4)$", font_size=FONT_SIZE).next_to(problem_settings[0][1], LEFT),
            Tex("$\cdot 5 $", font_size=FONT_SIZE).next_to(problem_settings[0][0], RIGHT).shift(LEFT * 0.2)
        )
        helpers_for_part1[0][0][0].set_opacity(0)
        helpers_for_part1[0][0][-1].set_opacity(0)

        self.play(ReplacementTransform(problem_settings[0][0], helpers_for_part1[0]))
        self.wait()

        self.play(ReplacementTransform(problem_settings[0][1], helpers_for_part1[1]),
                  AnimationGroup(
                      helpers_for_part1[0][0][0].animate.set_opacity(1),
                      helpers_for_part1[0][0][-1].animate.set_opacity(1)
                  ))
        self.wait()

        self.play(helpers_for_part1.animate.move_to(book_count_variable[0]).shift( LEFT * 4.5))
        self.wait(2)

        # write problem settings part 2 in terms of x
        self.play(problem_settings[1].animate.shift(DOWN * 2.6))
        self.wait()

        helpers_for_part2 = VGroup(
            Tex("$(x - 8)$", font_size=FONT_SIZE).next_to(problem_settings[1][1], LEFT).shift(RIGHT * 0.1),
            Tex("$\cdot 7 $", font_size=FONT_SIZE).next_to(problem_settings[1][0], RIGHT).shift(LEFT * 0.2)
        )
        helpers_for_part2[0][0][0].set_opacity(0)
        helpers_for_part2[0][0][-1].set_opacity(0)

        self.play(ReplacementTransform(problem_settings[1][0], helpers_for_part2[0]))
        self.wait()

        self.play(ReplacementTransform(problem_settings[1][1], helpers_for_part2[1]),
                  AnimationGroup(
                      helpers_for_part2[0][0][0].animate.set_opacity(1),
                      helpers_for_part2[0][0][-1].animate.set_opacity(1)
                  ))
        self.wait()

        self.play(AnimationGroup(helpers_for_part2.animate.next_to(helpers_for_part1, RIGHT).shift(RIGHT * 0.55),
                                 FadeOut(book_count_variable[0])))
        self.wait()

        # combine problem settings

        helpers_for_part3 = VGroup(
            Tex("$=$", font_size=FONT_SIZE).next_to(helpers_for_part1, RIGHT),
            Tex("$x\cdot 5- 4\cdot 5 = x\cdot 7 - 8\cdot 7$", font_size=FONT_SIZE).move_to(helpers_for_part1).shift(
                DOWN * 0.7 + RIGHT*1.35),
            Tex("$5x - 20 = 7x - 56$", font_size=FONT_SIZE).move_to(helpers_for_part1).shift(DOWN * 1.4 +RIGHT*1.35),
            Tex("$5x - 7x = - 56 + 20$", font_size=FONT_SIZE).move_to(helpers_for_part1).shift(DOWN * 2.1 + RIGHT*1.5),
            Tex("$-2x = -36$", font_size=FONT_SIZE).move_to(helpers_for_part1).shift(DOWN * 2.8 + RIGHT*1.33),
            Tex(r"$x=\frac{-36}{-2} = 18$", font_size=FONT_SIZE).move_to(helpers_for_part1).shift(
                DOWN * 3.5 + RIGHT*2.18)

        )

        self.play(ReplacementTransform(problem_settings[2], helpers_for_part3[0]))
        self.wait()

        self.play(AnimationGroup(
            helpers_for_part1[1][0][-1].animate.set_color(ORANGE),
            helpers_for_part2[1][0][-1].animate.set_color(ORANGE),
        ))
        self.wait()

        for i in range(1,3):
            self.play(Write(helpers_for_part3[i],run_time=1.5))
            self.wait()
        self.wait()

        curved_arrows=VGroup(
            CurvedArrow(helpers_for_part3[2][0][3].get_bottom(),helpers_for_part3[2][0][8].get_bottom(),tip_length=0.15,
                                    angle=.6).shift(DOWN*0.1),
            CurvedArrow(helpers_for_part3[2][0][6].get_top(), helpers_for_part3[2][0][2].get_top(),tip_length=0.15,
                                    angle=.6).shift(UP*0.1)
        )

        self.play(Write(curved_arrows[0]))
        self.play(Write(curved_arrows[1]))
        self.wait(2)

        for i in range(3,6):
            self.play(Write(helpers_for_part3[i],run_time=1.5))
            self.wait()

        solution=Tex(solution_str,font_size=FONT_SIZE).shift(UP*2)

        self.play(Write(solution))
        self.wait(2)
