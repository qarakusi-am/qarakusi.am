from manim import *
from hanrahashiv import ExtractExponentInFormula, ReplaceItemsInFormula, FormulaModificationsScene, RemoveItemsFromFormula, WriteExponentInFormula

def ChangeFormula(formula, *new_formula_string_list):
    new_formula = MathTex(*new_formula_string_list)
    new_formula.scale_to_fit_height(formula.height)
    new_formula.move_to(formula)
    return new_formula
    

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
        self.play(ReplaceItemsInFormula(formula_0, items_indices = [6], items_str_list=[r'2 \cdot 3']))                                     # 3  x ^2  •  *  = {2•3} x ^6  y ^2
        formula_0_c0 = ChangeFormula(formula_0, '3', 'x', '^2', r'\cdot', r'\star', '=', '2', r'\cdot', '3', 'x', '^6', 'y', '^2')          # 3  x ^2  •  *  =  2  •  3  x ^6  y ^2
        self.add(formula_0_c0)
        self.remove(*formula_0)
        self.fix_formula(formula_0_c0)
        self.play(formula_0_c0[8].animate.set_color(YELLOW), formula_0_c0[0].animate.set_color(YELLOW))                                     # 3  x ^2  •  *  =  2  •  3  x ^6  y ^2
        self.wait()
        self.play(formula_0_c0[2].animate.set_color(BLUE), formula_0_c0[10].animate.set_color(GREEN))                                       # 3  x ^2  •  *  =  2  •  3  x  ^6  y ^2
        self.wait()
        self.play(ExtractExponentInFormula(formula_0_c0, 1, 'x', '2', add_multiplication_signs_in_between=True))                            # 3  x  •  x  •  *  =  2  •  3  x ^6  y ^2
        self.play(ExtractExponentInFormula(formula_0_c0, 10, 'x', '6', add_multiplication_signs_in_between=True))                           # 3  x  •  x  •  *  =  2  •  3  x  •  x  •  x  •  x  •  x  •  x  y ^2
        self.play(FadeOut( Brace(formula_0_c0[10: -2], DOWN).add(MathTex('6').next_to(formula_0_c0[10: -2], DOWN, buff=0.5))), run_time=2)
        self.wait()
        self.play(RemoveItemsFromFormula(formula_0_c0, [2, 11, 13, 15, 17, 19]))                                                            # 3  x  x  •  *  =  2  •  3  x  x  x  x  x  x  y ^2
        self.wait()
        self.play(formula_0_c0[1:3].animate.set_color(YELLOW), formula_0_c0[9:11].animate.set_color(YELLOW))
        self.wait()
        self.play(
            AnimationGroup(*[Indicate(i) for i in formula_0_c0[1:3]], lag_ratio=0.1),
            AnimationGroup(*[Indicate(i) for i in formula_0_c0[9:11]], lag_ratio=0.1))
        self.wait()
        self.play(WriteExponentInFormula(formula_0_c0, 1, 2, 'x', '2'))                                                                     # 3  x ^2  •  *  =  2  •  3  x  x  x  x  x  x  y ^2
        self.play(WriteExponentInFormula(formula_0_c0, 9, 10, 'x', '2'))                                                                    # 3  x ^2  •  *  =  2  •  3  x ^2  x  x  x  x  y ^2
        self.play(formula_0_c0[1:3].animate.set_color(YELLOW), formula_0_c0[9:11].animate.set_color(YELLOW))
        self.wait()
        self.play(AnimationGroup(*[Indicate(i) for i in formula_0_c0[11:15]], lag_ratio=0.1))                                               # 3  x ^2  •  *  =  2  •  3  x ^2  x  x  x  x  y ^2
        self.play(WriteExponentInFormula(formula_0_c0, 11, 14, 'x', '4'))                                                                   # 3  x ^2  •  *  =  2  •  3  x ^2  x ^4  y ^2
        self.wait()                                                                                                                         # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 
        self.rearrange_formula(
            formula_0_c0, [0, 1, 2, 3, 4, 5, 8, 9, 10, 7, 6, 11, 12, 13, 14],
            move_up=[6, 7], fade_out = [7])                                                                                                 # 3  x ^2  •  *  =  3  x ^2  •  2  x ^4  y ^2
        self.wait()