from manim import Write, FadeOut, FadeIn,AnimationGroup, Tex, VGroup, TransformFromCopy,ReplacementTransform,Transform
from manim import Arrow, CurvedArrow, SurroundingRectangle
from manim import YELLOW, ORANGE, WHITE, MathTex
from manim import Scene, LEFT, UP, DOWN, RIGHT
from qarakusiscene import TaskNumberBox
from .text import *

FONT_SIZE = 70
RUN_TIME_SPEED = 2

class Problem11018(Scene):
    def construct(self):
        scale_factor=1.2
        product_rows=VGroup(
            MathTex('*\;2\;* ',font_size=FONT_SIZE).shift(UP*2),
            MathTex(r' \frac{*\;7}{*\;*\;*\;}', font_size=FONT_SIZE).shift(UP*1/1.2),
            MathTex(r' \frac{*\;*\;*\;*}{*\;*\;*\;*\;8}', font_size=FONT_SIZE).shift(DOWN),
        ).shift(LEFT*0.5)

        #arrange all digits
        product_rows[1][0][0:2].align_to(product_rows[0][0],RIGHT)

        for i in range(len(product_rows[0][0])):
            product_rows[0][0][i].align_to(product_rows[1][0][-3+i], RIGHT)

        product_rows[1][0][0].align_to(product_rows[0][0][1],RIGHT)
        product_rows[1][0][1].align_to(product_rows[0][0][2],RIGHT)

        product_rows[2][0].align_to(product_rows[1][0],RIGHT)

        for i in range(-1,-4,-1):
            product_rows[2][0][i].align_to(product_rows[1][0][i], RIGHT)

        product_rows[2][0][3].align_to(product_rows[1][0][-2], RIGHT)
        product_rows[2][0][2].align_to(product_rows[1][0][-3], RIGHT)
        product_rows[2][0][0].align_to(product_rows[2],LEFT)
        product_rows[2][0][1].align_to(product_rows[2],LEFT).shift(RIGHT*0.65)


        product_rows[2][0][-5].align_to(product_rows[2], LEFT)
        product_rows[2][0][-4].align_to(product_rows[2][0][1],RIGHT)



        product_expressions=VGroup(MathTex(r'\times',font_size=FONT_SIZE).next_to(product_rows[0],LEFT).shift(DOWN*0.5+LEFT*0.1),
            MathTex('+', font_size=FONT_SIZE).next_to(product_rows[2],LEFT).shift(UP))


        self.play(FadeIn(product_rows,product_expressions))
        self.wait()

        helper_numbers=VGroup(MathTex('8',font_size=FONT_SIZE).move_to(product_rows[1][0][-1]),
                              MathTex('4',font_size=FONT_SIZE).move_to(product_rows[0][0][-1]).shift(UP*0.06),
                              MathTex('14',font_size=FONT_SIZE).shift(RIGHT*10),
                              MathTex('6',font_size=FONT_SIZE),
                              MathTex('1',font_size=FONT_SIZE).set_color(ORANGE).scale(scale_factor),
                              MathTex('7',font_size=FONT_SIZE).shift(RIGHT*10),
                              MathTex('8',font_size=FONT_SIZE).move_to(product_rows[1][0][-3]),
                              MathTex('9',font_size=FONT_SIZE),
                              MathTex('1','1','1','6',font_size=FONT_SIZE),
                              MathTex('1','2','0','2', font_size=FONT_SIZE)
                              )

        multiples_of_7=VGroup(MathTex('7',font_size=FONT_SIZE)).next_to(product_rows[0],RIGHT).shift(RIGHT*2+UP)
        for index in range(8):
            multiples_of_7.add(MathTex(str((index+2)*7),font_size=FONT_SIZE).move_to(multiples_of_7[index]).shift(DOWN*0.8))

        #put  8 in its position
        self.play(product_rows[2][0][-1].animate.set_color(ORANGE).scale(scale_factor))
        self.wait()

        self.play(TransformFromCopy(product_rows[2][0][-1],helper_numbers[0]),product_rows[1][0][-1].animate.set_opacity(0))
        self.wait()

        self.play(product_rows[2][0][-1].animate.set_color(WHITE).scale(1/scale_factor))
        self.wait(2)

        #find 3 rd element

        self.play(Write(multiples_of_7))
        self.wait()

        self.play(multiples_of_7[3][0].animate.set_color(ORANGE))
        self.play(multiples_of_7[3][0][1].animate.scale(1.3))
        self.wait(0.8)

        self.play(multiples_of_7[3][0][1].animate.scale(1/1.3))
        self.wait()

        self.play(VGroup(multiples_of_7[0:3],multiples_of_7[4:]).animate.set_opacity(0))
        self.wait()

        self.play(ReplacementTransform(product_rows[0][0][-1],helper_numbers[1]))
        self.wait()

        self.play(multiples_of_7[3][0].animate.set_color(WHITE))
        self.wait(0.8)

        self.play(multiples_of_7[3][0][1].animate.move_to(product_rows[1][0][-1]))
        self.wait(2)

        # find 7 th element


        self.play(VGroup(product_rows[0][0][1],product_rows[1][0][1]).animate.set_color(ORANGE).scale(scale_factor))
        self.wait()

        self.play(helper_numbers[2].animate.align_to(multiples_of_7[3][0][0],RIGHT))
        self.wait()

        helper_numbers[3].move_to(helper_numbers[2][0][1])

        self.play(multiples_of_7[3][0][0].animate.move_to(helper_numbers[2][0][1]),ReplacementTransform(VGroup(helper_numbers[2][0][1],multiples_of_7[3][0][0]),
                                                                                                        helper_numbers[3]))
        self.wait()

        self.play(helper_numbers[3].animate.move_to(product_rows[1][0][-2]),product_rows[1][0][-2].animate.set_opacity(0))
        self.wait()

        self.play(VGroup(product_rows[0][0][1], product_rows[1][0][1]).animate.set_color(WHITE).scale(1/scale_factor))
        self.wait()

        self.play(product_rows[0][0][0].animate.set_color(ORANGE).scale(scale_factor))
        self.wait(2)

        # find the first element


        helper_numbers[4].move_to(product_rows[0][0][0])

        self.play(ReplacementTransform(product_rows[0][0][0],helper_numbers[4].shift(UP*0.06)))
        self.wait()

        self.play(helper_numbers[4].animate.set_color(WHITE).scale(1/scale_factor))
        self.wait()

        # find the sixth element

        self.play(helper_numbers[5].animate.align_to(helper_numbers[2][0][0], RIGHT).shift(DOWN*0.8))
        self.wait()

        self.play(ReplacementTransform(VGroup(helper_numbers[2][0][0], helper_numbers[5][0][0]),helper_numbers[6]),product_rows[1][0][-3].animate.set_opacity(0))
        self.wait()

        self.play(VGroup(product_rows[2][0][0:4]).animate.set_color(ORANGE).scale(scale_factor-0.1))
        self.wait(2)

        #find 9-13 digits

        helper_equation=MathTex('8\cdot 124 = 992 < 1000',font_size=FONT_SIZE-10).next_to(product_rows[2][0],RIGHT)
        self.play(Write(helper_equation,run_time=RUN_TIME_SPEED))
        self.wait()

        helper_numbers[7].move_to(product_rows[1][0][0]).shift(UP*0.08)

        self.play(ReplacementTransform(product_rows[1][0][0],helper_numbers[7]))
        self.wait()
        self.play(FadeOut(helper_equation))
        self.wait()
        self.play(product_rows[2][0][0:4].animate.scale(1/(scale_factor-0.1)))
        self.wait()


        for i in range(len(helper_numbers[8])):
            helper_numbers[8][i].move_to(product_rows[2][0][i])

        for i in range(len(helper_numbers[8])-1,-1,-1):
            self.play(ReplacementTransform(product_rows[2][0][i], helper_numbers[8][i]))
        self.wait()

        for i in range(len(helper_numbers[9])):
            helper_numbers[9][i].move_to(product_rows[2][0][5+i]).shift(UP*0.07)

        for i in range(3,-1,-1):
            self.play(ReplacementTransform(product_rows[2][0][5+i], helper_numbers[9][i]))

        self.wait()




























