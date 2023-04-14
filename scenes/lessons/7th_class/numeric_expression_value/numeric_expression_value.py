from manim import UP, DOWN, LEFT, RIGHT
from manim import  WHITE, RED, BLUE
from manim import VGroup, MathTex, SurroundingRectangle, Create
from manim import Write, AnimationGroup, FadeOut, TransformFromCopy, ReplacementTransform, Wiggle
from segment import ConnectionLine

from .text import *
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox

FONT_SIZE = 65


class NumericExpressionValue(FormulaModificationsScene):
    def construct(self):

        self.expression= expression=MathTex('\\frac{(4(2^3+5)-1){\div}3}{3} -(8-3^2)', font_size=FONT_SIZE)
        expression[0][0].set_opacity(0)
        expression[0][10:13].set_opacity(0)
        self.play(Write(expression))
        self.wait()
        self.play(expression.animate.shift(UP*3))
        self.wait()


        expression_copy=expression.copy().shift(DOWN*4)
        self.play(TransformFromCopy(expression,expression_copy))
        self.wait()
        self.play(AnimationGroup(
            expression_copy[0][11].animate.set_opacity(1),
            expression_copy[0][14].animate.move_to(expression_copy[0][12]),
            expression_copy[0][13].animate.set_opacity(0),
            expression_copy[0][0].animate.set_opacity(1),
            expression_copy[0][10].animate.set_opacity(1)

        ))
        self.wait()
        minuend=VGroup(expression_copy[0][0:13], expression_copy[0][14])
        self.play(minuend.animate.shift(DOWN*0.5))


        self.play(AnimationGroup(
            VGroup(expression_copy[0][2],expression_copy[0][7]).animate.set_color(BLUE),
            VGroup(expression_copy[0][16],expression_copy[0][21]).animate.set_color(RED)
        ))
        self.wait()
        brace_lines = VGroup(ConnectionLine(expression_copy[0][0], expression_copy[0][10], alpha=1/5, color = BLUE),
                             ConnectionLine(expression_copy[0][2], expression_copy[0][7], alpha=1 / 5, color=BLUE),
                             ConnectionLine(expression_copy[0][0], expression_copy[0][7], alpha=1 / 5, color=BLUE)
                             )
        self.play(Create(brace_lines[0]))
        self.wait()
        self.play(ReplacementTransform(brace_lines[0],brace_lines[1]))
        self.wait()
        self.play(VGroup(expression_copy[0][3:5]).animate.scale(1.3))
        self.wait(0.5)
        self.play(VGroup(expression_copy[0][3:5]).animate.scale(1/1.3))


        self.wait()

        helper_equations=VGroup(MathTex('2','^3','=','2','\cdot','2','\cdot','2',font_size=FONT_SIZE).next_to(expression_copy,UP).align_to(expression_copy,LEFT).shift(UP*0.5),
                                MathTex('=\\frac{(4{\cdot}13-1)}{3} -(8-3^2)', font_size=FONT_SIZE).next_to(expression,DOWN).align_to(expression_copy,LEFT),
                                MathTex('=', font_size=FONT_SIZE).next_to(expression,DOWN).align_to(expression_copy,LEFT).shift(DOWN*2))
        helper_numbers=VGroup(MathTex('8',font_size=FONT_SIZE).next_to(expression_copy[0][5],LEFT).shift(UP*0.03),
                              MathTex('\cdot 13',font_size=FONT_SIZE).next_to(expression_copy[0][1],RIGHT).shift(DOWN*0.05),
                              MathTex('52',font_size=FONT_SIZE).next_to(expression_copy[0][0],RIGHT).shift(LEFT*0.05+DOWN*0.02),
                              MathTex('51',font_size=FONT_SIZE).next_to(expression_copy[0][0],RIGHT).shift(DOWN*0.03+RIGHT*0.03),
                              MathTex('\\frac{51}{3}',font_size=FONT_SIZE).next_to(helper_equations[2],RIGHT))
        surrounding_rectangles=VGroup(SurroundingRectangle(helper_equations[0], color=BLUE,buff=0.15))
        self.play(Write(helper_equations[0],run_time=2))
        self.play(Create(surrounding_rectangles[0]))
        self.fix_formula(helper_equations[0])
        self.wait()
        self.play(ModifyFormula(helper_equations[0], replace_items=[[3,4,5]], replace_items_strs=[['4']]))
        self.wait()
        self.play(ModifyFormula(helper_equations[0], replace_items=[[3, 4, 5]], replace_items_strs=[['8']]))
        self.wait()

        self.play(AnimationGroup(ReplacementTransform(expression_copy[0][3:5],helper_numbers[0]),FadeOut(helper_equations[0],surrounding_rectangles[0])))
        self.wait()
        self.play(AnimationGroup(ReplacementTransform(VGroup(expression_copy[0][2:8],helper_numbers[0]), helper_numbers[1]),
                                 VGroup(expression_copy[0][8:13],
                                   expression_copy[0][14:22]).animate.next_to(helper_numbers[1],RIGHT),
                                 brace_lines[1].animate.set_opacity(0)))
        self.wait()
        self.play(Write(helper_equations[1]))
        self.wait()
        self.play(Create(brace_lines[2]))
        self.wait()
        self.play(Wiggle(VGroup(expression_copy[0][1], helper_numbers[1])))
        self.play(AnimationGroup(ReplacementTransform(VGroup(expression_copy[0][1], helper_numbers[1]), helper_numbers[2]),
                                 VGroup(expression_copy[0][8:13], expression_copy[0][14:22]).animate.shift(LEFT*0.65),
                                 FadeOut(brace_lines[2])
                                 ))
        self.wait(2)
        self.play(
            AnimationGroup(ReplacementTransform(VGroup(expression_copy[0][8:11],expression_copy[0][0], helper_numbers[2]), helper_numbers[3]),
                           VGroup(expression_copy[0][11:13],expression_copy[0][14:22]).animate.next_to(helper_numbers[3], RIGHT)))
        self.wait(2)
        self.play(Write(helper_equations[2]),AnimationGroup(VGroup(expression_copy[0][11:13],expression_copy[0][14:22],helper_numbers[3]).animate.next_to(helper_equations[2],RIGHT),
                  ReplacementTransform(VGroup(expression_copy[0][11:13],expression_copy[0][14],helper_numbers[3]),helper_numbers[4]),
                                                            VGroup(expression_copy[0][15:22]).animate.next_to(helper_numbers[4],RIGHT)))
        self.wait()
        self.wait()
        helper_equations.add(MathTex('=17 -(8-3^2)', font_size=FONT_SIZE).next_to(expression_copy[0][21],RIGHT))
        helper_equations.add(MathTex('3^2=3 \cdot 3=9', font_size=FONT_SIZE).align_to(helper_equations[3],LEFT).shift(DOWN*1.35))

        surrounding_rectangles.add(SurroundingRectangle(helper_equations[4], color=BLUE, buff=0.15))
        brace_lines.add( ConnectionLine(helper_equations[3][0][4], helper_equations[3][0][9], alpha=1 / 5, color=BLUE))

        self.play(Write(helper_equations[3]))
        self.wait()
        self.play(Create(brace_lines[3]),VGroup(expression_copy[0][16],expression_copy[0][21]).animate.set_color(WHITE))
        self.wait()
        self.play(VGroup(helper_equations[3][0][7:9]).animate.scale(1.3))
        self.wait()
        self.play(VGroup(helper_equations[3][0][7:9]).animate.scale(1/1.3))
        self.play(Write(helper_equations[4]))
        self.play(Write(surrounding_rectangles[1]))
        self.wait(2)
        helper_equations.add(MathTex('=17-(8-9)', font_size=FONT_SIZE).next_to(helper_equations[2], DOWN).align_to(expression,LEFT).shift(DOWN*0.8))
        helper_equations.add(MathTex('=17-(-1)', font_size=FONT_SIZE).next_to(helper_equations[5], RIGHT))
        helper_equations.add(MathTex('=17+1=18', font_size=FONT_SIZE).next_to(helper_equations[4], DOWN).align_to(expression,LEFT).shift(DOWN*0.5))

        self.play(FadeOut(helper_equations[4],surrounding_rectangles[1],brace_lines[3]))
        self.wait(0.25)
        self.play(Write(helper_equations[5]))
        self.wait()
        self.play(Write(helper_equations[6]))
        self.wait()
        self.play(Write(helper_equations[7]))
        self.wait()
