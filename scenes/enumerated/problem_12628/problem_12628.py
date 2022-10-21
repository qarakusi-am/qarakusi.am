from manim import MathTex, Tex, VGroup, SurroundingRectangle, Arrow, Brace
from manim import rate_functions, DOWN, UP, RIGHT, LEFT, UR, UL, WHITE, BLUE, BLUE_D, GREEN_D, RED_D, YELLOW_D, TEAL_D, GOLD_D, MAROON_D, BLACK
from manim import AnimationGroup, ReplacementTransform, Wiggle, Write, FadeIn, FadeOut, Indicate, Circumscribe
from qarakusiscene import TaskNumberBox
from hanrahashiv import (
    ExtractExponentInFormula,
    ReplaceItemsInFormula,
    FormulaModificationsScene,
    RemoveItemsFromFormula,
    WriteExponentInFormula,
    MultiplyNumbersInFormula,
    AddItemsInFormula)
from .text import taskNumberString

def ChangeFormula(formula, *new_formula_string_list):
    new_formula = MathTex(*new_formula_string_list)
    new_formula.scale_to_fit_height(formula.height)
    new_formula.move_to(formula)
    return new_formula

def replacement_transform(mob_1, mob_2, scale_factor = 1):
    mob_1.match_height(mob_2)
    mob_1.move_to(mob_2)
    mob_1.scale(scale_factor)
    return ReplacementTransform(mob_2, mob_1)

    

class Problem12628(FormulaModificationsScene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait()
        ##formulas##
        formulas = VGroup(
            MathTex('3', 'x', '^3', r'\cdot', '3', 'x', '^3', '=',  r'\star').scale(1.1).next_to(2*UP + 6.5*LEFT, buff=0.2),
            MathTex('3', 'x', '^2', r'\cdot', r'\star', '=', '6', 'x', '^6', 'y', '^2').scale(1.1).next_to(1*UP + 6.5*LEFT, buff=0.2),
            MathTex(r'\star', r'\cdot', '(', 'm', 'n', ')', '^2', '=', '4', 'm', '^3', 'n', '^2').scale(1.1).next_to(6.5*LEFT, buff=0.2),
            MathTex('5', 'a', '^2', 'b', r'\cdot', r'\star', '=', '5', 'a', '^3', 'b', '^2', 'c').scale(1.1).next_to(DOWN + 6.5*LEFT, buff=0.2))
        numbers = VGroup(*[MathTex(f'{i+1})').next_to(formulas[i], LEFT, buff=0.2) for i in range(4)]).align_to(taskNumber, LEFT)
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
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.11)
        prop_1.to_edge(RIGHT).align_to(formulas[0], UP)
        #p2
        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 0.5, LEFT)
        #p3
        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 0.5, LEFT)
        VGroup(prop_1, prop_2, prop_3).scale_to_fit_height(formulas.height).to_edge(RIGHT).align_to(formulas[0], UP)
        #animation
        self.play(AnimationGroup(FadeIn(prop_1), FadeIn(prop_2), FadeIn(prop_3), lag_ratio=0.33), run_time = 2)
        self.wait()
        ##formula 0 modification##
        formula_0 = formulas[0].copy()
        self.play(VGroup(numbers[1:], formulas[1:]).animate.set_opacity(0))
        self.play(formula_0.animate.shift(1.25*DOWN))
        self.fix_formula(formula_0)                                                                                                         # 3  x ^3  •  3  x ^3  =  *
        self.wait()                                                                                                                         # 0  1  2  3  4  5  6  7  8
        self.play(AnimationGroup(Indicate(formula_0[0:3], 1.1, BLUE), Indicate(formula_0[4:7], 1.1, BLUE), lag_ratio=0.5))
        self.wait()
        self.rearrange_formula(
            formula_0, [0, 3, 4, 1, 2, 5, 6, 7, 8],
            move_up=[3, 4], fade_out = [3])                                                                                                 # 3  •  3  x ^3  x ^3  =  *
        self.wait()                                                                                                                         # 0  3  4  1  2  5  6  7  8
        self.play(MultiplyNumbersInFormula(formula_0, 3, '9'))
        self.wait()
        property_1_c0 = property_1.copy()                                                                                                   # a ^m  •  a ^n  = a ^m ^+ ^n 
        self.play(property_1_c0.animate.next_to(formula_0, DOWN, buff = 1))
        self.wait()
        self.fix_formula(property_1_c0)
        arrow_0_1 = Arrow(start=formula_0[1].get_center(), end=property_1_c0[0], buff=0.3)
        arrow_0_2 = Arrow(start=formula_0[3].get_center(), end=property_1_c0[3], buff=0.3)
        self.play(
            property_1_c0[0].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(BLUE_D),            
            property_1_c0[3].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(BLUE_D),
            property_1_c0[6].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(BLUE_D),
            formula_0[1].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(BLUE_D),            
            formula_0[3].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(BLUE_D),
            FadeIn(arrow_0_1, arrow_0_2), run_time = 2)
        self.play(ReplaceItemsInFormula(property_1_c0, [0, 3, 6], ['x', 'x', 'x',]), FadeOut(arrow_0_1, arrow_0_2), run_time = 2)
        self.wait()
        self.play(
            property_1_c0[1].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GREEN_D),            
            property_1_c0[7].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GREEN_D),
            formula_0[2].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GREEN_D), run_time = 2)
        self.play(ReplaceItemsInFormula(property_1_c0, [1, 7], ['^3', '^3']), run_time = 2)
        self.wait()
        self.play(
            property_1_c0[4].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW_D),            
            property_1_c0[9].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW_D),
            formula_0[4].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(YELLOW_D), run_time = 2)
        self.play(ReplaceItemsInFormula(property_1_c0, [4, 9], ['^3', '^3']), run_time = 2)
        self.wait()
        self.play(ReplaceItemsInFormula(property_1_c0, [7, 8, 9], ['^6', ' ', ' ',], [RED_D, BLACK, BLACK]))
        self.wait()
        formula_0.set_color(WHITE)
        self.play(ReplaceItemsInFormula(formula_0, [2, 3, 4], ['^6', ' ', ' ',], [WHITE, BLACK, BLACK]))
        self.wait()
        self.fix_formula(formulas[0]) 
        self.play(
            ReplaceItemsInFormula(formulas[0], [8], ['9x^6'], [RED_D]),
            formula_0.animate.set_color(RED_D))
        self.wait()
        self.play(FadeOut(formula_0, property_1_c0))
        self.play(
            Circumscribe(formulas[0][0], fade_in=True),
            Circumscribe(formulas[0][4], fade_in=True))
        self.play(
            Circumscribe(formulas[0][0], fade_out=True),
            Circumscribe(formulas[0][4], fade_out=True))
        self.wait()
        self.play(
            Circumscribe(formulas[0][2], fade_in=True),
            Circumscribe(formulas[0][6], fade_in=True))
        self.play(
            Circumscribe(formulas[0][2], fade_out=True),
            Circumscribe(formulas[0][6], fade_out=True))
        self.wait()
        ##formula 1 modification##
        formula_1 = formulas[1].copy()
        self.play(
            formula_1.animate.shift(1.25*DOWN).set_opacity(1),
            formulas[0].animate.set_opacity(0.3),
            numbers[0].animate.set_opacity(0.3),
            formulas[1].animate.set_opacity(1),
            numbers[1].animate.set_opacity(1))
        self.fix_formula(formula_1)
        self.wait()
        self.play(ReplaceItemsInFormula(formula_1, items_indices = [6], items_str_list=[r'2 \cdot 3']))                                     # 3  x ^2  •  *  = {2•3} x ^6  y ^2
        formula_1_c0 = ChangeFormula(formula_1, '3', 'x', '^2', r'\cdot', r'\star', '=', '2', r'\cdot', '3', 'x', '^6', 'y', '^2')          # 3  x ^2  •  *  =  2  •  3  x ^6  y ^2
        self.add(formula_1_c0)
        self.remove(*formula_1)
        self.fix_formula(formula_1_c0)
        self.play(formula_1_c0[8].animate.set_color(GREEN_D), formula_1_c0[0].animate.set_color(GREEN_D))                                     # 3  x ^2  •  *  =  2  •  3  x ^6  y ^2
        self.wait()
        self.play(AnimationGroup(
            Indicate(formula_1_c0[2]),
            Indicate(formula_1_c0[10]),
            lag_ratio=1), run_time = 2)                                                                                                     # 3  x ^2  •  *  =  2  •  3  x  ^6  y ^2
        self.wait()
        self.play(ExtractExponentInFormula(formula_1_c0, 1, 'x', '2', add_multiplication_signs_in_between=True))                            # 3  x  •  x  •  *  =  2  •  3  x ^6  y ^2
        self.play(ExtractExponentInFormula(formula_1_c0, 10, 'x', '6', add_multiplication_signs_in_between=True))                           # 3  x  •  x  •  *  =  2  •  3  x  •  x  •  x  •  x  •  x  •  x  y ^2
        self.play(FadeOut( Brace(formula_1_c0[10: -2], DOWN).add(MathTex('6').next_to(formula_1_c0[10: -2], DOWN, buff=0.5))), run_time=2)
        self.wait()
        self.play(RemoveItemsFromFormula(formula_1_c0, [2, 11, 13, 15, 17, 19]))                                                            # 3  x  x  •  *  =  2  •  3  x  x  x  x  x  x  y ^2
        self.wait()
        self.play(formula_1_c0[1:3].animate.set_color(RED_D), formula_1_c0[9:11].animate.set_color(RED_D))
        self.wait()
        self.play(WriteExponentInFormula(formula_1_c0, 1, 2, 'x', '2'))                                                                     # 3  x ^2  •  *  =  2  •  3  x  x  x  x  x  x  y ^2
        self.play(WriteExponentInFormula(formula_1_c0, 9, 10, 'x', '2'))                                                                    # 3  x ^2  •  *  =  2  •  3  x ^2  x  x  x  x  y ^2
        self.play(formula_1_c0[1:3].animate.set_color(RED_D), formula_1_c0[9:11].animate.set_color(RED_D))
        self.wait()
        self.play(AnimationGroup(*[Indicate(i) for i in formula_1_c0[11:15]], lag_ratio=0.1))                                               # 3  x ^2  •  *  =  2  •  3  x ^2  x  x  x  x  y ^2
        self.play(WriteExponentInFormula(formula_1_c0, 11, 14, 'x', '4'))                                                                   # 3  x ^2  •  *  =  2  •  3  x ^2  x ^4  y ^2
        self.wait()                                                                                                                         # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 
        self.rearrange_formula(
            formula_1_c0, [0, 1, 2, 3, 4, 5, 8, 9, 10, 7, 6, 11, 12, 13, 14],
            move_up=[6, 7], fade_out = [7])                                                                                                 # 3  x ^2  •  *  =  3  x ^2  •  2  x ^4  y ^2
        self.wait()
        self.fix_formula(formulas[1]) 
        self.play(
            formula_1_c0[4].animate.set_color(BLUE_D),
            formula_1_c0[10:].animate.set_color(BLUE_D),
            ReplaceItemsInFormula(formulas[1], [4], ['2x^4y^2'], [BLUE_D]))
        self.wait()
        self.play(FadeOut(formula_1_c0))
        self.wait()
        ##formula 2 modification##
        formula_2 = formulas[2].copy()
        self.play(
            formula_2.animate.shift(1.25*DOWN).set_opacity(1),
            formulas[1].animate.set_opacity(0.3),
            numbers[1].animate.set_opacity(0.3),
            formulas[2].animate.set_opacity(1),
            numbers[2].animate.set_opacity(1))
        self.fix_formula(formula_2)
        self.wait()
        property_2_c0 = property_2.copy()                                                                                                   # a ^m  •  a ^n  = a ^m ^+ ^n 
        self.play(property_2_c0.animate.next_to(formula_2, DOWN, buff = 1))
        property_2_c1 = Tex('$($', '$a$', r'$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', r'$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_c1.match_width(property_2_c0)
        property_2_c1.move_to(property_2_c0)
        self.add(property_2_c1)
        self.remove(property_2_c0)
        self.wait()
        self.fix_formula(property_2_c1)
        arrow_2_1 = Arrow(start=formula_2[3].get_center(), end=property_2_c1[1], buff=0.3)
        self.fix_formula(property_2_c1)
        self.play(
            property_2_c1[1].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),            
            property_2_c1[7].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),
            formula_2[3].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),
            FadeIn(arrow_2_1))
        self.wait()
        self.play(ReplaceItemsInFormula(property_2_c1, [1, 7], ['$m$', '$m$']), FadeOut(arrow_2_1))
        arrow_2_2 = Arrow(start=formula_2[4].get_center(), end=property_2_c1[3], buff=0.3)        
        self.play(
            property_2_c1[3].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),            
            property_2_c1[10].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),
            formula_2[4].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),
            FadeIn(arrow_2_2))
        self.wait()
        self.play(ReplaceItemsInFormula(property_2_c1, [3, 10], ['$n$', '$n$']), FadeOut(arrow_2_2))
        arrow_2_3 = Arrow(start=formula_2[6].get_center(), end=property_2_c1[5], buff=0.3)
        self.play(
            property_2_c1[5].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),            
            property_2_c1[8].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),
            property_2_c1[11].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),
            formula_2[6].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),
            FadeIn(arrow_2_3))
        self.wait()
        self.play(ReplaceItemsInFormula(property_2_c1, [5, 8, 11], ['$^2$', '$^2$', '$^2$']), FadeOut(arrow_2_3), run_time = 2)
        formula_2.set_color(WHITE)
        self.play(AddItemsInFormula(formula_2, [3], [' ']))
        self.play(ReplaceItemsInFormula(formula_2, [2, 4, 6], [' ', '^2', ' '], [WHITE, WHITE, WHITE]), run_time = 2)
        self.play(FadeOut(property_2_c1))
        self.wait()
        self.play(formula_2[12:].animate.set_color(GREEN_D), formula_2[5:8].animate.set_color(GREEN_D))
        self.wait()
        formula_2[8:-2].set_color(WHITE)
        self.play(ReplaceItemsInFormula(formula_2, [11], [r'^{1 + 2}']), run_time = 2)
        property_1_c1 = property_1.copy()
        self.play(property_1_c1.animate.next_to(formula_2, DOWN, buff = 1))
        arrow_2_4 = Arrow(start=formula_2[10].get_center(), end=property_1_c1[6], buff=0.3)
        self.wait()
        self.fix_formula(property_1_c1)
        self.play(
            property_1_c1[0].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),            
            property_1_c1[3].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),
            property_1_c1[6].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),
            formula_2[10].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(TEAL_D),
            FadeIn(arrow_2_4))
        self.wait()
        self.play(ReplaceItemsInFormula(property_1_c1, [0, 3, 6], ['$m$', '$m$', '$m$']), FadeOut(arrow_2_4,))
        arrow_2_5 = Arrow(start=formula_2[11][0].get_center(), end=property_1_c1[7], buff=0.3)
        self.play(
            property_1_c1[1].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),            
            property_1_c1[7].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),
            formula_2[11][0].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(GOLD_D),
            FadeIn(arrow_2_5))
        self.wait()
        self.play(ReplaceItemsInFormula(property_1_c1, [1, 7], ['$^1$', '$^1$']), FadeOut(arrow_2_5))
        arrow_2_6 = Arrow(start=formula_2[11][2].get_center(), end=property_1_c1[9].get_center(), buff=0.3)
        self.play(
            property_1_c1[4].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),            
            property_1_c1[9].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),
            formula_2[11][2].animate(rate_func = rate_functions.there_and_back_with_pause).set_color(MAROON_D),
            FadeIn(arrow_2_6))
        self.wait()
        formula_2[8:-2].set_color(WHITE)
        self.play(ReplaceItemsInFormula(property_1_c1, [4, 9], ['$^2$', '$^2$']), FadeOut(arrow_2_6))
        self.wait(0.5)
        self.play(AddItemsInFormula(formula_2, [11], [' ']), run_time = 0.5)
        self.play(ReplaceItemsInFormula(formula_2, [11, 12], ['^1', 'm^2']))
        self.wait()
        self.play(ReplaceItemsInFormula(formula_2, [11], [r'\cdot']))
        self.play(FadeOut(property_1_c1))
        self.wait()
        self.play(formula_2[3:5].animate.set_color(RED_D), formula_2[12].animate.set_color(RED_D))
        self.wait()
        self.fix_formula(formulas[2])
        self.play(
            ReplaceItemsInFormula(formulas[2], [0], ['4m'], [YELLOW_D]),
            formula_2[0].animate.set_color(YELLOW_D),
            formula_2[9:11].animate.set_color(YELLOW_D), 
        )
        self.wait()
        self.play(FadeOut(formula_2))
        self.wait()
        ##formula 3 modification##
        self.play(
            formulas[2].animate.set_opacity(0.3),
            numbers[2].animate.set_opacity(0.3),
            formulas[3].animate.set_opacity(1),
            numbers[3].animate.set_opacity(1))
        self.wait()
        self.play(Wiggle(formulas[3][5], 1.3))
        self.play(formulas[3][5].animate.set_color(GREEN_D))
        self.wait()
