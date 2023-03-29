from manim import Write, FadeOut, VGroup, AnimationGroup, ReplacementTransform, Create
from manim import Rectangle, Line
from manim import ORANGE, MathTex
from manim import Scene, RIGHT, LEFT, UP, DOWN, WHITE, GREEN

FONT_SIZE = 65
RUN_TIME_SPEED = 2

class FractionSum(Scene):
    def construct(self):

        rectangles = VGroup(Rectangle(width=8.0, height=4.0, fill_opacity=1),
                       Rectangle(width=6.07, height=4.0, fill_color=ORANGE, fill_opacity=1,color=ORANGE).shift(LEFT),
                       Rectangle(width=1.37, height=4.0, fill_color=GREEN, fill_opacity=1,color=GREEN).shift(RIGHT*3.35)
                       )

        dividing_line_width=10
        dividing_line_sample= Line((0,0.2,0),(0,-0.2,0),fill_opacity=1,stroke_width=dividing_line_width)

        dividing_lines = VGroup(
           dividing_line_sample.copy().set_color(ORANGE).shift(UP * 2 + LEFT * 2),
            dividing_line_sample.copy().set_color(ORANGE).shift(UP * 2),
            dividing_line_sample.copy().set_color(ORANGE).shift(UP * 2 + RIGHT * 2),
            dividing_line_sample.copy().set_color(GREEN).shift(DOWN * 2 + LEFT * 2.7),
            dividing_line_sample.copy().set_color(GREEN).shift(DOWN * 2 + LEFT * 1.4),
            dividing_line_sample.copy().set_color(GREEN).shift(DOWN * 2 + LEFT * 0.1),
            dividing_line_sample.copy().set_color(GREEN).shift(DOWN * 2 + RIGHT * 1.4),
            dividing_line_sample.copy().set_color(GREEN).shift(DOWN * 2 + RIGHT * 2.7)
        )
        line_for_first_rectangle = Line(dividing_lines[2], (2,-2.02,0), stroke_width=dividing_line_width,color=ORANGE)
        line_for_second_rectangle = Line(dividing_lines[-1], (2.7,2.01,0),stroke_width=dividing_line_width, color=GREEN)

        helper_numbers = VGroup(MathTex(r"\frac{3}{4}", font_size=FONT_SIZE).move_to(rectangles[1]),
                           MathTex(r"\frac{1}{6}", font_size=FONT_SIZE).move_to(rectangles[2]))

        helper_equations=VGroup(MathTex(r"= \frac{3\cdot3}{3\cdot4} + \frac{2\cdot1}{2\cdot6}", font_size=FONT_SIZE),
                           MathTex(r"= \frac{9}{12} + \frac{2}{12} = \frac{9+2}{12} = \frac{11}{12}", font_size=FONT_SIZE),
                           MathTex(r"\frac{3}{4} + \frac{1}{6} = \frac{3\cdot 3 + 2\cdot 1}{12}", font_size=FONT_SIZE).shift(LEFT*2),
                           MathTex(r"= \frac{9+2}{12} = \frac{11}{12}", font_size=FONT_SIZE))
        helper_equations[2][0][8].set_color(ORANGE)
        helper_equations[2][0][12].set_color(GREEN)
        helper_equations[2][0][8:15].set_opacity(0)

        plus_sign=MathTex("+", font_size=FONT_SIZE).next_to(helper_numbers[0],RIGHT).shift(DOWN*0.05)

        lines_for_factors=VGroup(
            Line((0,-0.1,0),(0.3,0.2,0),stroke_width=3).move_to(helper_equations[2][0][0]).shift(LEFT*0.2+UP*0.2),
            Line((0, -0.1, 0), (0.3, 0.2, 0), stroke_width=3).move_to(helper_equations[2][0][4]).shift( LEFT * 0.2 + UP * 0.2)
        )
        factors=VGroup(MathTex('3',color=ORANGE).move_to(lines_for_factors[0]).shift(UP*0.22+LEFT*0.1),
                       MathTex('2',color=GREEN).move_to(lines_for_factors[1]).shift(UP*0.22+LEFT*0.1))

        #draw the white rectangle
        self.play(Write(rectangles[0]))
        self.wait()

        self.play(Create(VGroup(dividing_lines[0:3])))
        self.wait()

        self.play(Write(line_for_first_rectangle))
        self.wait()

        #draw the orange rectangle

        self.play(AnimationGroup(Write(rectangles[1]),FadeOut(VGroup(dividing_lines[0:3]))))
        self.wait()

        self.play(Write(helper_numbers[0]))
        self.wait(2)

        self.play(Create(VGroup(dividing_lines[3:])))
        self.wait()

        self.play(Write(line_for_second_rectangle))
        self.wait()

        #draw the green rectangle

        self.play(AnimationGroup(Write(rectangles[-1]), FadeOut(VGroup(dividing_lines[3:]))))
        self.wait(2)

        self.play(Write(helper_numbers[1]))
        self.wait(2)

        line_for_first_rectangle.set_opacity(0)
        line_for_second_rectangle.set_opacity(0)

        #transform rectangles to an equation

        self.play(AnimationGroup(ReplacementTransform(rectangles, plus_sign),helper_numbers[1].animate.next_to(plus_sign,RIGHT).shift(UP*0.05)))
        self.wait(2)

        self.play(VGroup(helper_numbers[0][0][-1],helper_numbers[1][0][-1]).animate.set_color(ORANGE).scale(1.3))
        self.wait(0.5)
        self.play(VGroup(helper_numbers[0][0][-1], helper_numbers[1][0][-1]).animate.set_color(WHITE).scale(1/1.3))
        self.wait()

        helper_equations[0][0][1].set_color(ORANGE)
        helper_equations[0][0][5].set_color(ORANGE)
        helper_equations[0][0][9].set_color(GREEN)
        helper_equations[0][0][13].set_color(GREEN)

        helper_equations[0].move_to(helper_numbers[1][0],LEFT).shift(RIGHT*0.6)

        self.play(Write(helper_equations[0],run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(VGroup(helper_numbers,plus_sign,helper_equations[0]).animate.shift(LEFT*5.6))
        self.wait()

        helper_equations[1].move_to(helper_equations[0][0][-4],LEFT).shift(RIGHT*1.3+UP*0.07)

        self.play(Write(helper_equations[1], run_time=RUN_TIME_SPEED+1))
        self.wait(2)

        #move the first equation row up
        self.play(VGroup(helper_numbers,helper_equations[0:2],plus_sign).animate.scale(0.8).shift(UP*3))
        self.wait(2)

        #write the second equation row
        self.play(Write(helper_equations[2],run_time=RUN_TIME_SPEED))
        self.wait(2)

        self.play(Write(lines_for_factors[0]))
        self.play(Write(factors[0]))
        self.wait()

        self.play(Write(lines_for_factors[1]))
        self.play(Write(factors[1]))
        self.wait()

        helper_equations[2][0][8:15].set_opacity(1)

        self.play(Write(VGroup(helper_equations[2][0][8:15])))
        self.wait()

        helper_equations[-1].move_to(helper_equations[-2][0][-3], LEFT).shift(RIGHT*3.6)

        self.play(Write(VGroup(helper_equations[-1]),run_time=RUN_TIME_SPEED))
        self.wait()


