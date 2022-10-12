from manim import *
from hanrahashiv import ExtractExponentInFormula, ReplaceItemsInFormula, FormulaModificationsScene, RemoveItemsFromFormula, WriteExponentInFormula


class Problem12628(FormulaModificationsScene):
    def construct(self):

        formulas = VGroup(
            MathTex('3', 'x', '^2', r'\cdot', r'\star', '=', '6', 'x', '^6', 'y', '^2').next_to(2*UP + 4*LEFT, buff=0.2),
            MathTex('5', 'a', '^2', 'b', r'\cdot', r'\star', '=', '5', 'a', '^3', 'b', '^2', 'c').next_to(2*UP + 4*LEFT, buff=0.2),
            MathTex(r'\star', r'\cdot',  '3', 'a', '^2', 'b','=', '5', 'a', '^3', 'b').next_to(2*UP + 4*LEFT, buff=0.2),
            MathTex(r'\star', r'\cdot', '(', 'm', 'n', ')', '^2', '=', '4', 'm', '^3', 'n', '^2').next_to(2*UP + 4*LEFT, buff=0.2))
        numbers = VGroup(*[MathTex(f'{i+1}.').next_to(2*UP + 4*LEFT, LEFT, buff=0.2) for i in range(4)])
        self.play(Write(formulas[0]), Write(numbers[0]))
        formula_0 = formulas[0].copy()
        self.play(formula_0.animate.shift(DOWN))
        self.fix_formula(formula_0)
        self.play(ReplaceItemsInFormula(formula_0, items_indices = [6], items_str_list=[r'2 \cdot 3'])) # 3 x ^2 • * = {2•3} x ^6 y ^2
        self.play(formula_0[6][2].animate.set_color(YELLOW), formula_0[0].animate.set_color(YELLOW)) # 3 x ^2 • * = {2•3} x ^6 y ^2
        self.wait()
        self.play(ReplaceItemsInFormula(formula_0, items_indices = [0, 6], items_str_list=[r' ', r'2'])) # x ^2 • * = 2 x ^6 y ^2
        formula_0.remove(formula_0[0])
        self.wait()
        self.play(formula_0[1].animate.set_color(BLUE), formula_0[7].animate.set_color(GREEN))
        self.wait()
        self.play(ExtractExponentInFormula(formula_0, 0, 'x', '2', add_multiplication_signs_in_between=True)) # x • x • * = 2 x ^6 y ^2
        self.play(ExtractExponentInFormula(formula_0, 7, 'x', '6', add_multiplication_signs_in_between=True)) # x • x • * = 2 x • x •  x  •  x  •  x  •  x  y  ^2
        self.play(FadeOut( Brace(formula_0[7: -2], DOWN).add(MathTex('6').next_to(formula_0[7: -2], DOWN, buff=0.5))), run_time=2)
        self.wait()
        self.play(RemoveItemsFromFormula(formula_0, [1, 8, 10, 12, 14, 16]))  # x x • * = 2 x x x x x x y ^2
        self.wait()
        self.play(formula_0[:2].animate.set_color(YELLOW), formula_0[6:8].animate.set_color(YELLOW))
        self.wait()
        self.play(RemoveItemsFromFormula(formula_0, [0, 1, 2, 6, 7])) # * = 2 x x x x y ^2
        self.wait()
        self.play(AnimationGroup(*[Indicate(i) for i in formula_0[3:7]], lag_ratio=0.1))
        self.wait()
        self.play(WriteExponentInFormula(formula_0, 3, 6, 'x', '4'))
        self.wait()
        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.11)
        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 1.1, LEFT)
        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 1.1, LEFT)
        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait()
