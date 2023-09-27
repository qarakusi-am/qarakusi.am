from manim import Scene, FadeIn, Tex, Write, VGroup, AnimationGroup, \
    ReplacementTransform, ORANGE, FadeOut, CurvedArrow, SurroundingRectangle, YELLOW, WHITE
from manim import UP, DOWN, RIGHT, LEFT, YELLOW_C
from qarakusiscene import TaskNumberBox
from objects import Bookshelf
from .text import *

FONT_SIZE = 60
FORMULA_FONT_SIZE = 65


class Problem12804(Scene):
    def construct(self):
        # task number
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # Fade in the bookshelf
        bookshelf = Bookshelf().scale(2).shift(DOWN*1.2)

        self.play(FadeIn(bookshelf))
        self.wait()

        # problem settings
        self.problem_settings = problem_settings = VGroup(
            Tex(problem_setting_1_part_1, and_string, problem_setting_1_part_2, font_size=FONT_SIZE).to_edge(UP).shift(
                DOWN * 0.5).align_to(taskNumber, LEFT),
            Tex(problem_setting_2_part_1, and_string, problem_setting_2_part_2, font_size=FONT_SIZE).to_edge(UP).shift(
                DOWN * 1.2).align_to(taskNumber, LEFT),
            Tex(problem_setting_part3, font_size=FONT_SIZE).to_edge(UP).shift(DOWN * 1.9))

        problem_settings.set_color_by_gradient(YELLOW_C, ORANGE)

        self.play(Write(problem_settings[0], run_time=2.5))
        self.wait(1.5)

        self.play(Write(problem_settings[1], run_time=2.5))
        self.wait(1.5)

        self.play(Write(problem_settings[2], run_time=1.4))
        self.wait(2)

        self.book_count_variable = book_count_variable = Tex(book_count_x, font_size=FONT_SIZE).shift(UP * 0.6),

        self.play(ReplacementTransform(bookshelf, book_count_variable[0]))
        self.wait(2)

        self.equality_sign = equality_sign = Tex(" $=$ ", font_size=FORMULA_FONT_SIZE).move_to(problem_settings[-1]),

        self.convert_problem_setting_1()
        self.convert_problem_setting_2()

        # combine problem settings

        converted_setting_part1 = self.converted_setting_part1

        helpers = VGroup(
            Tex("$x\cdot 5- 4\cdot 5 = x\cdot 7 - 8\cdot 7$", font_size=FORMULA_FONT_SIZE).move_to(
                converted_setting_part1).shift(RIGHT * 1.75),
            Tex("$5x - 20 = 7x - 56$", font_size=FORMULA_FONT_SIZE).move_to(converted_setting_part1).shift(
                DOWN + RIGHT * 1.75),
            Tex("$5x - 7x = - 56 + 20$", font_size=FORMULA_FONT_SIZE).move_to(converted_setting_part1).shift(
                DOWN * 2 + RIGHT * 2),
            Tex("$-2x = -36$", font_size=FORMULA_FONT_SIZE).move_to(converted_setting_part1).shift(
                DOWN * 1.8 + RIGHT * 1.75),
            Tex(r"$x=\frac{-36}{-2} = 18$", font_size=FORMULA_FONT_SIZE).move_to(converted_setting_part1).shift(
                DOWN * 2.8 + RIGHT * 2.9)

        )
        helpers[0][0][2].set_color(ORANGE)
        helpers[0][0][6].set_color(ORANGE)
        helpers[0][0][-5].set_color(ORANGE)
        helpers[0][0][-1].set_color(ORANGE)


        self.play(AnimationGroup(ReplacementTransform(problem_settings[2], equality_sign[0]),
                                 VGroup(self.converted_setting_part1, self.converted_setting_part2).animate.shift(UP)))
        self.wait(2)

        self.play(AnimationGroup(
            converted_setting_part1[1][0][-1].animate.set_color(ORANGE),
            self.converted_setting_part2[1][0][-1].animate.set_color(ORANGE),
        ))
        self.wait()

        self.play(Write(helpers[0], run_time=2.2))
        self.wait(2)
        self.play(VGroup(helpers[0],converted_setting_part1,self.converted_setting_part2).animate.set_color(WHITE))
        self.wait(2)
        self.play(Write(helpers[1], run_time=2))
        self.wait()

        curved_arrows = VGroup(
            CurvedArrow(helpers[1][0][3].get_bottom(), helpers[1][0][9].get_bottom(), tip_length=0.15,
                        angle=.6).shift(DOWN * 0.07),
            CurvedArrow(helpers[1][0][6].get_top(), helpers[1][0][1].get_top(), tip_length=0.15,
                        angle=.6).shift(UP * 0.1)
        )

        self.play(Write(curved_arrows[0]))
        self.play(Write(curved_arrows[1]))
        self.wait(2)

        self.play(Write(helpers[2], run_time=2))
        self.wait(3)

        self.play(FadeOut(curved_arrows))
        self.wait(2)

        self.play(VGroup(helpers[0:3],equality_sign[0],converted_setting_part1,self.converted_setting_part2).animate.shift(UP*1.2))
        self.wait()

        for i in range(3, 5):
            self.play(Write(helpers[i], run_time=1.8))
            self.wait()

        solution = Tex(solution_str, font_size=FORMULA_FONT_SIZE).shift(UP * 3.3)

        self.play(Write(solution))
        self.wait(2)

    def convert_problem_setting_1(self):
        problem_settings = self.problem_settings[0]

        self.play(problem_settings.animate.shift(DOWN * 3.3))
        self.wait(2)

        self.converted_setting_part1 = converted_setting_part1 = VGroup(
            Tex("$(x - 4)$", font_size=FORMULA_FONT_SIZE).next_to(problem_settings[1], LEFT),
            Tex("$\cdot 5 $", font_size=FORMULA_FONT_SIZE).next_to(problem_settings[0], RIGHT).shift(LEFT * 0.15+UP*0.1)
        )

        surrounding_rectangles = VGroup(SurroundingRectangle(problem_settings[0], color=YELLOW, buff=0.15),
                                        SurroundingRectangle(problem_settings[2], color=YELLOW, buff=0.15))

        self.play(Write(surrounding_rectangles[0]))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(surrounding_rectangles[0]),
                                 ReplacementTransform(problem_settings[0:2], converted_setting_part1[0][0][1:-1]),
                                 ))
        self.wait(2)

        self.play(Write(surrounding_rectangles[1]))
        self.wait(2)

        self.play(ReplacementTransform(problem_settings[2], converted_setting_part1[1]),
                  FadeOut(surrounding_rectangles[1]),
                  FadeIn(converted_setting_part1[0][0][0], converted_setting_part1[0][0][-1])
                  )
        self.wait(2)

        self.play(AnimationGroup(self.book_count_variable[0].animate.shift(UP * 2.5).scale(1.4),
                  converted_setting_part1.animate.next_to(self.equality_sign[0], LEFT).shift(DOWN),run_time=2))
        self.wait(2)

    def convert_problem_setting_2(self):

        problem_settings = self.problem_settings[1]

        self.play(problem_settings.animate.shift(DOWN * 2.6))
        self.wait(2)

        self.converted_setting_part2 = converted_setting_part2 = VGroup(
            Tex("$(x - 8)$", font_size=FORMULA_FONT_SIZE).next_to(problem_settings[1], LEFT).shift(RIGHT * 0.55+DOWN*0.05),
            Tex("$\cdot 7 $", font_size=FORMULA_FONT_SIZE).next_to(problem_settings[0], RIGHT).shift(RIGHT * 0.45+UP*0.05)
        )

        surrounding_rectangles = VGroup(SurroundingRectangle(problem_settings[0], color=YELLOW, buff=0.15),
                                        SurroundingRectangle(problem_settings[2], color=YELLOW, buff=0.15))

        self.play(Write(surrounding_rectangles[0]))
        self.wait(2)
        self.play(AnimationGroup(
            ReplacementTransform(problem_settings[0:2], converted_setting_part2[0][0][1:-1]),
            FadeOut(surrounding_rectangles[0])))
        self.wait(2)

        self.play(Write(surrounding_rectangles[1]))
        self.wait(2)

        self.play(ReplacementTransform(problem_settings[2], converted_setting_part2[1]),
                  FadeOut(surrounding_rectangles[1]),
                  AnimationGroup(
                      FadeIn(converted_setting_part2[0][0][0], converted_setting_part2[0][0][-1])
                  ))
        self.wait(2)

        self.play(AnimationGroup(
            converted_setting_part2.animate.next_to(self.equality_sign[0], RIGHT).shift(DOWN),
            FadeOut(self.book_count_variable[0])))
        self.wait()
