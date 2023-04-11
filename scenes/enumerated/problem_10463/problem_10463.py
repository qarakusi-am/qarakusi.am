from manim import SurroundingRectangle, Brace, CurvedArrow, Transform, Arrow
from manim import Write, Indicate, Wiggle, Create, Uncreate, FadeIn, FadeOut, AnimationGroup
from manim import ReplacementTransform, TransformFromCopy, CounterclockwiseTransform
from manim import GREEN, RED, BLUE, ORANGE, WHITE, YELLOW
from manim import PI, UR, RIGHT, LEFT, UP, DOWN
from manim import Tex, MathTex, VGroup
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from .text import *


FONT_SIZE=63
SCALE_FACTOR = 1.5
WIGGLE_SCALE_FACTOR = 1.25

class Problem10463(FormulaModificationsScene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)

        solve_equations_text=Tex(solve_equations,font_size=FONT_SIZE).shift(UP*3.3)
        self.play(Write(solve_equations_text))
        self.wait()

        self.formulas = formulas = VGroup(
            Tex('$x$', '$^2$', ' $+$ ', '$6$', '$x$',' $+$ ', '$y$', '$^2$', ' $+$ ', '$8$', '$y$',' $+$ ', '$2$', '$5$', ' $=$ ', '$0$', font_size=FONT_SIZE).next_to(2.5*UP + 6.5*LEFT, buff=0.2),
            Tex('$x$', '$^2$', ' $-$ ', '$6$', '$x$','$y$',' $+$ ',  '$1$', '$3$','$y$', '$^2$', ' $-$ ', '$4$', '$y$',' $+$ ','$1$', ' $=$ ', '$0$', font_size=FONT_SIZE).next_to(1.5*UP + 6.5*LEFT, buff=0.2),
             )
        self.numbers = numbers = VGroup(*[MathTex(f'{i+1})', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3) for i in range(2)]).align_to(taskNumber, LEFT)

        self.play(
            AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(2)], lag_ratio=0.5),
            run_time = 3
        )
        self.wait(0.25)

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        self.wait()

        self.first()
        self.second()


    def first(self):
        formulas = self.formulas
        # copy x^2+6x part and move down
        abbr_formula = Tex('$x$', '$^2$', ' $+$ ', '$6$', '$x$', font_size=FONT_SIZE).move_to(
            formulas[0]).align_to(formulas[0], LEFT)
        self.play(abbr_formula.animate.shift(DOWN))
        self.wait()
        self.fix_formula(abbr_formula)

        self.play(ModifyFormula(abbr_formula, replace_items=[[3, 4, 5]],
                                replace_items_strs=[['$2$', '$\cdot$', '$x$', '$\cdot$' '$3$']]))
        self.wait()

        helper_equations = VGroup(
            Tex(' $+$ ', '$3$', '$^2$', font_size=FONT_SIZE).next_to(abbr_formula[-1], RIGHT).align_to(abbr_formula,
                                                                                                       DOWN),
            Tex(' $-$ ', '$3$', '$^2$', font_size=FONT_SIZE),
            Tex(' $+$ ', '$y$', '$^2$', ' $+$ ', '$8$', '$y$',' $+$ ', '$2$', '$5$', ' $=$ ', '$0$', font_size=FONT_SIZE),
            Tex('$($','$x$', ' $+$ ', '$3$','$)$', '$^2$', font_size=FONT_SIZE),
            Tex(' $+$ ', '$y$', '$^2$', ' $+$ ', '$8$', '$y$', ' $+$ ', '$1$', '$6$', ' $=$ ', '$0$',
                font_size=FONT_SIZE),
            Tex( '$y$', '$^2$', ' $+$ ', '$2$', '$\cdot$','$y$', '$\cdot$','$4$',' $+$ ', '$4$', '$^2$',
                font_size=FONT_SIZE),
            Tex('$($', '$y$', ' $+$ ', '$4$', '$)$', '$^2$', font_size=FONT_SIZE),
            Tex('$($', '$x$', ' $+$ ', '$3$', '$)$', '$^2$', ' $+$ ', font_size=FONT_SIZE),
            Tex( ' $=$ ', '$0$',
                font_size=FONT_SIZE),
        )
        # add 3^2 to abbreviate form and move to equality sign

        self.play(Write(helper_equations[0]))
        self.wait()

        helper_equations[1].next_to(helper_equations[0][-1], RIGHT).align_to(abbr_formula,
                                                  UP),
        self.play(Write(helper_equations[1]))
        self.wait()

        # create surrounding rectangle for 3^2-3^2
        surrounding_rectangle1 = SurroundingRectangle(VGroup(helper_equations[0][1:], helper_equations[1]),
                                                      color=YELLOW, buff=0.2)
        self.play(Write(surrounding_rectangle1))
        self.wait()

        helper_equations[2].next_to(helper_equations[1][-1], RIGHT).align_to(abbr_formula,DOWN)
        self.play(Write(helper_equations[2],run_time=2))
        self.wait()

        self.play(FadeOut(surrounding_rectangle1))
        self.wait()

        # extract first square from equality
        brace1=Brace(VGroup(abbr_formula,helper_equations[0]),sharpness=1)
        self.play(Write(brace1))
        self.wait()

        helper_equations[3].move_to(brace1).shift(DOWN*0.5)
        self.play(Write(helper_equations[3]))
        self.wait(2)

        self.play(AnimationGroup(FadeOut(brace1),helper_equations[3].animate.align_to(formulas[0],LEFT)))
        self.wait()

        curved_arrow=CurvedArrow(helper_equations[1][1].get_bottom(), helper_equations[2][-3].get_bottom(), tip_length=0.15,
                    angle=.5).shift(DOWN * 0.1)

        self.play(Write(curved_arrow))
        self.wait()

        helper_equations[4].next_to(helper_equations[3][-1], RIGHT).align_to(helper_equations[4],
                                                                             DOWN).shift(DOWN*0.2),
        self.play(Write(helper_equations[4],run_time=1.5))
        self.wait()
        self.play(FadeOut(curved_arrow))
        self.wait()

        # extract second square from equality
        brace2 = Brace(helper_equations[4][1:9], sharpness=1)
        helper_equations[5].move_to(brace2).shift(DOWN*0.5)
        helper_equations[6].move_to(helper_equations[5])

        self.play(Write(brace2))
        self.play(Write(helper_equations[5]))
        self.wait(2)

        self.play(ReplacementTransform(helper_equations[5],helper_equations[6]))
        self.wait()

        #combine squares
        helper_equations[-2].align_to(helper_equations[3],LEFT).shift(UP*0.2)
        self.play(helper_equations[-2].animate.shift(DOWN*1.05))
        self.wait()

        self.play(helper_equations[-3].animate.next_to(helper_equations[-2][-1],RIGHT))
        helper_equations[-1].next_to(helper_equations[-3][-1],RIGHT).shift(DOWN*0.2)
        self.play(Write(helper_equations[-1]))
        self.wait()
        self.play(FadeOut(brace2))
        self.wait()

        #find solutions
        non_negative=Tex(non_negative_str,font_size=FONT_SIZE).move_to(helper_equations[-2]).shift(DOWN*1.2+RIGHT*2)
        self.play(Write(non_negative))
        self.wait()

        arrows=VGroup(
            Arrow(non_negative[0][5].get_top(),helper_equations[-3][2].get_bottom(),max_stroke_width_to_length_ratio=2,max_tip_length_to_length_ratio=0.1).scale(1.3,1),
            Arrow(non_negative[0][5].get_top(),helper_equations[-2][2].get_bottom(),max_stroke_width_to_length_ratio=0.9,max_tip_length_to_length_ratio=0.08).scale(1.15,1),
        )
        self.play(Write(arrows))
        self.wait(2)

        solution_equations = VGroup(
            Tex('$($', '$x$', ' $+$ ', '$3$', '$)$', '$^2$', ' $=$ ', '$0$', font_size=FONT_SIZE).align_to(
                helper_equations[-2], LEFT).shift(DOWN*1.8 ),

            Tex('$($', '$y$', ' $+$ ', '$4$', '$)$', '$^2$',' $=$ ', '$0$', font_size=FONT_SIZE).align_to(helper_equations[-2],LEFT).shift(DOWN*1.8+ RIGHT * 5),
            Tex( '$x$', ' $+$ ', '$3$', ' $=$ ', '$0$', font_size=FONT_SIZE),
            Tex('$y$', ' $+$ ', '$4$', ' $=$ ', '$0$', font_size=FONT_SIZE))

        solution_equations[2].align_to(solution_equations[0],LEFT).shift(DOWN*2.7)
        solution_equations[3].align_to(solution_equations[1],LEFT).shift(DOWN*2.7)



        self.play(ReplacementTransform(VGroup(arrows,non_negative),solution_equations[0:2]))
        self.wait()
        self.play(Write(solution_equations[2]))
        self.play(Write(solution_equations[3]))
        self.wait(2)

        self.fix_formula(solution_equations[2])
        self.fix_formula(solution_equations[3])
        self.play(AnimationGroup(
            ModifyFormula(solution_equations[2], replace_items=[[1,2,3,4,5]],
                          replace_items_strs=[[' $=$ ', '$-$' '$3$']]),
            ModifyFormula(solution_equations[3], replace_items=[[1,2,3,4,5]],
                          replace_items_strs=[[' $=$ ', '$-$' '$4$']])
        ))
        self.wait()
        self.play(AnimationGroup(solution_equations[2].animate.next_to(formulas[0],RIGHT).shift(RIGHT*0.2+UP*0.06),
                                 solution_equations[3].animate.next_to(formulas[0],RIGHT).shift(RIGHT*2.46)))
        self.play(FadeOut(helper_equations[0:5],helper_equations[6:],solution_equations[0:2],abbr_formula))
        self.wait(2)



    def second(self):
        formulas = self.formulas
        numbers = self.numbers

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.wait()

        self.play(formulas[1].animate.shift(RIGHT))
        self.wait()
        # divide 13y^2 into 2 parts

        self.fix_formula(formulas[1])

        self.play(ModifyFormula(formulas[1], replace_items=[[7, 8,9,10]],
                                replace_items_strs=[['$9$','$y$', '$^2$', ' $+$ ','$4$','$y$', '$^2$', ]]))
        self.wait()

        brace1 = Brace(formulas[1][0:10])
        brace2 = Brace(formulas[1][11:19])

        helper_equations = VGroup(
            Tex('$($','$2$','$x$', ' $+$ ', '$3$','$y$','$)$', '$^2$', font_size=FONT_SIZE).move_to(brace1).shift(DOWN*0.5+RIGHT*0.2),
            Tex('$($', '$2$', '$y$', ' $-$ ', '$1$', '$)$', '$^2$', font_size=FONT_SIZE).move_to(brace2).shift(
                DOWN * 0.5)
        )

        # extract first square from equality

        self.play(Write(brace1))
        self.play(Write(helper_equations[0]))
        self.wait()

        # extract second square from equality

        self.play(Write(brace2))
        self.play(Write(helper_equations[1]))
        self.wait()

        self.play(FadeOut(brace1,brace2))
        self.wait()

        # combine squares
        helper_signs= VGroup(
            Tex( ' $+$ ', font_size=FONT_SIZE).next_to(helper_equations[0],RIGHT).shift(RIGHT*0.65),
            Tex( ' $=$ ', '$0$',  font_size=FONT_SIZE).next_to(helper_equations[1],RIGHT)
        )
        self.play(Write(helper_signs[0]))
        self.play(Write(helper_signs[1]))
        self.wait()

        # find solutions

        solution_equations = VGroup(
            Tex('$2$', '$x$', ' $+$ ', '$3$', '$y$',  ' $=$ ', '$0$', font_size=FONT_SIZE).move_to(
                helper_equations[0], LEFT).shift(DOWN*1.15),

            Tex('$2$', '$y$', ' $-$ ', '$1$', ' $=$ ', '$0$', font_size=FONT_SIZE).move_to(
                helper_equations[1], LEFT).shift(DOWN*1.15),
            Tex('$2$', '$x$', ' $-$ ', '$1.5$', ' $=$ ', '$0$', font_size=FONT_SIZE).move_to(
                helper_equations[0], LEFT).shift(DOWN * 2.3),
        )


        self.play(Write(solution_equations[0]))
        self.play(Write(solution_equations[1]))
        self.wait(2)

        final_values = VGroup(

            Tex('$x$', ' $=$ ', '$\\frac{3}{4}$', font_size=FONT_SIZE).move_to(
                helper_equations[0], LEFT).shift(DOWN * 2.3),
            Tex('$y$', ' $=$ ', '-$\\frac{1}{2}$', font_size=FONT_SIZE).move_to(
                helper_equations[1], LEFT).shift(DOWN * 2.3),
        )
        #find y
        surrounding_rectangle=SurroundingRectangle(VGroup(helper_equations[1],helper_signs[1]),color=YELLOW,buff=0.2)
        self.play(Write(surrounding_rectangle))
        self.wait()

        self.play(Write(final_values[1]))
        self.wait()

        self.play(FadeOut(surrounding_rectangle))
        self.wait()

        # find x
        curved_arrow = CurvedArrow(final_values[1][2].get_bottom(), solution_equations[0][4].get_bottom(),
                                   tip_length=0.15,angle=-.5).shift(DOWN * 0.1)

        self.play(Write(curved_arrow))
        self.wait()

        self.play(Write(solution_equations[-1]))
        self.wait()
        self.play(FadeOut(curved_arrow))
        self.wait()

        self.play(ReplacementTransform(solution_equations[-1],final_values[0]))
        self.wait(2)

        #write final solution
        self.play(AnimationGroup(TransformFromCopy(final_values[0],final_values[0].copy().move_to(helper_equations[0],LEFT).shift(LEFT*2.5)),
                                 TransformFromCopy(final_values[1],final_values[1].copy().move_to(helper_equations[0],LEFT).shift(LEFT*2.5+DOWN))))
        self.wait()
