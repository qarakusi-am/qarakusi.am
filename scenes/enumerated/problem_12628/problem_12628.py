from manim import MathTex, Tex, VGroup, Brace, Line
from manim import DOWN, UP, RIGHT, LEFT, UL, TAU
from manim import BLUE, ORANGE, GREEN, BLUE_D, GREEN_D, RED_D
from manim import AnimationGroup, Wiggle, Write, FadeIn, FadeOut, Indicate, Circumscribe, MoveToTarget
from qarakusiscene import TaskNumberBox
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from .text import taskNumberString

FONT_SIZE = 65

class Problem12628(FormulaModificationsScene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait()

    ##formulas##
        formulas = VGroup(
            MathTex('3', 'x', '^3', r'\cdot', '3', 'x', '^3', '=',  r'\ast', font_size=FONT_SIZE).next_to(2*UP + 6.5*LEFT, buff=0.2),
            MathTex('3', 'x', '^2', r'\cdot', r'\ast', '=', '6', 'x', '^6', 'y', font_size=FONT_SIZE).next_to(1*UP + 6.5*LEFT, buff=0.2),
            MathTex(r'\ast', r'\cdot', '(', 'm', 'n', ')', '^2', '=', '4', 'm', '^3', 'n', '^2', font_size=FONT_SIZE).next_to(6.5*LEFT, buff=0.2),
            MathTex('5', 'a', '^2', 'b', r'\cdot', r'\ast', '=', '5', 'a', '^3', 'b', '^2', 'c', font_size=FONT_SIZE).next_to(DOWN + 6.5*LEFT, buff=0.2))
        numbers = VGroup(*[MathTex(f'{i+1})', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3).shift(0.1*DOWN) for i in range(4)]).align_to(taskNumber, LEFT)
        self.play(AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5), run_time = 4)
        self.wait()
        self.play(
            AnimationGroup(
                Wiggle(formulas[0][8], 1.3),
                Wiggle(formulas[1][4], 1.3),
                Wiggle(formulas[2][0], 1.3),
                Wiggle(formulas[3][5], 1.3),
                lag_ratio=0.15), run_time = 3)

    ##properties##
        #p1
        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_1_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_1_index = Tex('1', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_1_design = VGroup(property_1_rect, property_1_index)
        property_1_design.move_to(property_1).shift(0.05 * UP)
        prop_1 = VGroup(property_1, property_1_design)

        #p2
        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_2_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_2_index = Tex('2', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_2_design = VGroup(property_2_rect, property_2_index)
        property_2_design.move_to(property_2).shift(0.05 * UP)
        prop_2 = VGroup(property_2, property_2_design)

        #p3
        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_3_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_3_index = Tex('3', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_3_design = VGroup(property_3_rect, property_3_index)
        property_3_design.move_to(property_3).shift(0.05 * UP)
        prop_3 = VGroup(property_3, property_3_design)

        #p1_p2_p3
        VGroup(prop_1, prop_2, prop_3).arrange(DOWN, 1).to_edge(RIGHT, buff=0.2)

        #animation
        self.play(AnimationGroup(FadeIn(prop_1), FadeIn(prop_2), FadeIn(prop_3), lag_ratio=0.33), run_time = 2)
        self.wait()

    ##FIRST EXERCISE      3x^3 • 3x^3 = *  ##
        formula_0 = MathTex('3', 'x', '^3', r'\cdot', '3', 'x', '^3', font_size=FONT_SIZE)  # 3  x ^3  •  3  x ^3
        formula_0.next_to(2*UP + 6.5*LEFT, buff=0.2)
        self.play(VGroup(numbers[1:], formulas[1:]).animate.set_opacity(0))
        self.play(formula_0.animate.shift(1.25*DOWN))
        self.fix_formula(formula_0)
        self.wait()
        self.play(AnimationGroup(Indicate(formula_0[0:3], 1.1, BLUE), Indicate(formula_0[4:7], 1.1, BLUE), lag_ratio=0.5))
        self.wait()
        self.rearrange_formula(
            formula_0, [0, 3, 4, 1, 2, 5, 6, 7, 8],
            move_up=[3, 4], fade_out = [3]
        ) # 3  •  3  x ^3  x ^3
        self.wait() # 0  3  4  1  2  5  6  7  8
        self.play(
            ModifyFormula(formula_0, replace_items=[[0, 1, 2]], replace_items_strs=[['9']])
        ) # 9  x ^3  x ^3
        self.wait()

        self.play(
            Circumscribe(formula_0[1:3], run_time=1.5, fade_out=True, buff=0.05),
            Circumscribe(formula_0[3:5], run_time=1.5, fade_out=True, buff=0.05),
        )
        self.wait()

        self.play(Indicate(prop_1))
        self.wait()
        self.fix_formula(formula_0)
        self.play(
            ModifyFormula(formula_0, replace_items=[[2, 3, 4]], replace_items_strs=[['^{3+3}']])
        ) # 9  x ^{3+3}
        self.wait()

        self.fix_formula(formula_0)
        self.play(
            ModifyFormula(formula_0, replace_items=[[2]], replace_items_strs=[['^6']])
        )  # 9  x ^6
        self.wait()

        self.fix_formula(formulas[0])
        self.play(
            FadeOut(formula_0),
            ModifyFormula(formulas[0], replace_items=[[8]], replace_items_strs=[['9', 'x', '^6']], replace_items_colors=[[BLUE_D, BLUE_D, BLUE_D]])
        )

        self.play(
            Circumscribe(formulas[0][0], fade_out=True, run_time=2),
            Circumscribe(formulas[0][4], fade_out=True, run_time=2)
        )
        self.wait(0.25)
        self.play(Circumscribe(formulas[0][8], fade_out=True, run_time=2))
        self.wait()

        self.play(
            Circumscribe(formulas[0][2], fade_out=True, run_time=1.5),
            Circumscribe(formulas[0][6], fade_out=True, run_time=1.5)
        )
        self.wait(0)

        self.play(
            Circumscribe(formulas[0][0], fade_out=True, run_time=2),
            Circumscribe(formulas[0][4], fade_out=True, run_time=2)
        )
        self.wait(0.25)
        self.play(
            Circumscribe(formulas[0][2], fade_out=True, run_time=1.5),
            Circumscribe(formulas[0][6], fade_out=True, run_time=1.5)
        )
        self.wait(0.25)
        self.play(Circumscribe(formulas[0][10], fade_out=True, run_time=2))
        self.wait()

    ##SECOND EXERCISE    3  x ^2  •  *  = 6 x ^6  y  ##
        formula_1 = formulas[1].copy()
        self.play(
            formulas[0].animate.set_opacity(0.3),
            numbers[0].animate.set_opacity(0.3),
            formulas[1].animate.set_opacity(1),
            numbers[1].animate.set_opacity(1))
        self.play(formula_1.set_opacity(0.5).animate.shift(1.25*DOWN).set_opacity(1))
        self.fix_formula(formula_1)
        self.wait()
        self.play(
            ModifyFormula(formula_1, replace_items=[[6]], replace_items_strs=[['2', r'\cdot', '3']])
        ) # 3  x ^2  •  *  = 2 • 3 x ^6  y
        self.wait()

        self.play(
            Indicate(formula_1[0], 1.5),
            Indicate(formula_1[8], 1.5)
        )
        self.wait(0.25)
        self.play(
            formula_1[8].animate.set_color(GREEN_D),
            formula_1[0].animate.set_color(GREEN_D)
        )
        self.wait()

        self.play(Indicate(formula_1[2], 1.5))
        self.play(Indicate(formula_1[10], 1.5))
        self.wait()

        self.fix_formula(formula_1)
        self.play(
            ModifyFormula(formula_1, replace_items=[[2]], replace_items_strs=[['x']])
        ) # 3  xx  •  *  =  2  •  3  x ^6  y
        self.wait(0.25)

        self.fix_formula(formula_1)
        self.play(
            ModifyFormula(formula_1, replace_items=[[10]], replace_items_strs=[['x', 'x', 'x', 'x' ,'x']])
        ) # 3  xx  •  *  =  2  •  3  xxxxxx  y
        self.wait(0.1)

        brace_down = Brace(formula_1[9: -1], DOWN).add(MathTex('6').next_to(formula_1[9: -1], DOWN, buff=0.5))
        self.play(FadeIn(brace_down))
        brace_down.generate_target()
        self.wait()
        self.play(
            formula_1[1:3].animate.set_color(RED_D),
            formula_1[9:11].animate.set_color(RED_D)
        )
        self.wait()
        brace_down.target.become(Brace(formula_1[11: -1], DOWN).add(MathTex('4').next_to(formula_1[11: -1], DOWN, buff=0.5)))
        self.play(MoveToTarget(brace_down))
        self.wait(0.5)
        self.play(
            formula_1[1:3].animate.set_color(RED_D),
            formula_1[9:11].animate.set_color(RED_D)
        )
        self.wait()
        self.play(FadeOut(brace_down))
        self.wait()
        self.rearrange_formula(
            formula_1, [0, 1, 2, 3, 4, 5, 8, 9, 10, 7, 6, 11, 12, 13, 14, 15],
            move_up=[6, 7], fade_out=[7], fade_in=[9]
        ) # 3  xx  •  *  =  3xx  2  •  xxxx  y
        self.wait()

        self.play(ModifyFormula(formula_1, replace_items=[[11, 12, 13, 14]], replace_items_strs=[['x', '^4']]))
        self.wait()

        self.fix_formula(formulas[1]) 
        self.play(
            formula_1[4].animate.set_color(BLUE_D),
            formula_1[10:].animate.set_color(BLUE_D),
            ModifyFormula(formulas[1], replace_items=[[4]], replace_items_strs=[['2x^4y']], replace_items_colors=[[BLUE_D]])
        )
        self.wait()
        self.play(FadeOut(formula_1))
        self.wait()

    ##THIRD EXERCISE   * • (mn)^2 = 4m^3n^2  ##
        formula_2_1 = MathTex(r'\ast', r'\cdot', '(', 'm', 'n', ')', '^2', font_size=FONT_SIZE).move_to(formulas[2][:7]) # * • (mn)^2
        formula_2_2 = MathTex('=', '4', 'm', '^3', 'n', '^2', font_size=FONT_SIZE).move_to(formulas[2][7:]) # = 4 m^3 n^2
        self.play(
            formulas[1].animate.set_opacity(0.3),
            numbers[1].animate.set_opacity(0.3),
            formulas[2].animate.set_opacity(1),
            numbers[2].animate.set_opacity(1)
        )
        self.play(formula_2_1.set_opacity(0.5).animate.shift(1.25*DOWN).set_opacity(1))
        self.wait()
        self.fix_formula(formula_2_1)
        self.play(Circumscribe(formula_2_1[2:], fade_out=True, run_time=2))
        self.wait()
        self.play(Indicate(prop_2))
        self.wait()
        self.play(
            ModifyFormula(formula_2_1, remove_items=[2, 5], add_after_items=[3], add_items_strs=[['^2']], new_formula_alignment=UL)
        ) # * • m^2n^2
        self.wait()

        self.play(formula_2_2.set_opacity(0.5).animate.shift(1.25*DOWN).set_opacity(1))
        self.wait()
        self.play(
            formula_2_1[-2:].animate.set_color(GREEN_D),
            formula_2_2[-2:].animate.set_color(GREEN_D)
        )
        self.wait()
        self.play(Circumscribe(formula_2_2[2:4], fade_out=True, run_time=1.5, buff=0.05))
        self.wait(0.5)
        self.play(
            ModifyFormula(formula_2_2, replace_items=[[3]], replace_items_strs=[['^{1+2}']])
        ) # = 4 m^{1+2} n^2
        self.wait(0.5)

        self.play(Indicate(prop_1))
        self.wait(0.5)
        self.play(
            ModifyFormula(formula_2_2, replace_items=[[3]], replace_items_strs=[['^1', 'm', '^2']])
        ) # = 4 m^1 m^2 n^2
        self.wait()

        self.play(Indicate(formula_2_2[3], 1.5, run_time=1.5))
        self.wait(0.15)
        self.play(
            ModifyFormula(formula_2_2, remove_items=[3])
        ) # = 4 m m^2 n^2
        self.wait()

        self.play(
            formula_2_1[2:4].animate.set_color(RED_D),
            formula_2_2[3:5].animate.set_color(RED_D)
        )
        self.wait()

        self.play(Circumscribe(formula_2_1[0], buff=0.05, fade_out=True, run_time=1.5))
        self.wait(0.5)
        self.play(Circumscribe(formula_2_2[1:3], buff=0.05, fade_out=True, run_time=1.5))
        self.wait()

        self.fix_formula(formulas[2])
        self.play(
            ModifyFormula(formulas[2], replace_items=[[0]], replace_items_strs=[['4m']], replace_items_colors=[[BLUE_D]]),
            formula_2_1[0].animate.set_color(BLUE_D),
            formula_2_2[1:3].animate.set_color(BLUE_D)
        )

        self.play(FadeOut(formula_2_1, formula_2_2))
        self.wait()

    ##FOURTH EXERCISE     ##
        self.play(
            formulas[2].animate.set_opacity(0.3),
            numbers[2].animate.set_opacity(0.3),
            formulas[3].animate.set_opacity(1),
            numbers[3].animate.set_opacity(1))
        self.wait()
        self.play(Wiggle(formulas[3][5], 1.5, 0.03 * TAU))
        self.play(formulas[3][5].animate.set_color(RED_D))
        self.wait()
