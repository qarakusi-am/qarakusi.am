from manim import *
from hanrahashiv import *
from constants import ARMTEX, ENGTEX

class test(FormulaModificationsScene):
    def construct(self):

        formula_1 = Tex(
            '$3$', '$\cdot$', '$a$', '$\cdot$', '$b$','$\cdot$',
            '$a$', '$\cdot$', '$2$', '$\cdot$', '$a$', '$\cdot$', '$b$',
            font_size=70, tex_template=ENGTEX
        ) # 3•a•b•a•2•a•b
        formula_1[0].set_color(ORANGE)
        formula_1[2].set_color(GREEN)
        formula_1[8].set_color(BLUE)
        formula_1[4].set_color(RED)

        formula_2 = MathTex(
            '3', '\cdot', 'a', '\cdot', 'b','\cdot',
            'a', '\cdot', '2', '\cdot', 'a', '\cdot', 'b',
            font_size=70, tex_template=ENGTEX
        ) # 3•a•b•a•2•a•b
        formula_2[0].set_color(ORANGE)
        formula_2[2].set_color(GREEN)
        formula_2[8].set_color(BLUE)
        formula_2[4].set_color(RED)

        def test_animations(formula):
            self.play(Write(formula)) # 3•a•b•a•2•a•b
            self.wait()
            
            self.rearrange_formula(formula, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13], [8], [], [9], [1]) # 2•3•a•b•a•a•b
            
            self.play(MultiplyNumbersInFormula(formula, 3, '6', YELLOW)) # 6•a•b•a•a•b
            
            self.rearrange_formula(formula, [0, 1, 2, 5, 6, 7, 8, 9, 10, 3, 4], [4], [], [3], [-2]) # 6•a•a•a•b•b
            
            self.play(WriteExponentInFormula(formula, 2, 6, 'a', 3, BLUE, ORANGE)) # 6•a^3•b•b
            
            self.play(WriteExponentInFormula(formula, 5, 7, 'b', 2, None, GREEN)) # 6•a^3•b^2

            self.play(RemoveItemsFromFormula(formula, [1, 4])) # 6a^3b^2

            self.play(AddItemsInFormula(formula, [0, 2], ['\cdot', '$\cdot$'])) # 6•a^3•b^2

            self.play(ExtractExponentInFormula(formula, 2, 'a', 3, False, ORANGE)) # 6•aaa•b^2
            
            self.play(ExtractExponentInFormula(formula, 6, 'b', 2, True, GREEN)) # 6•aaa•b•b

            self.play(AddItemsInFormula(formula, [2, 3], ['\cdot', '\cdot'], [YELLOW, RED])) # 6•a•a•a•b•b
            
            self.play(RemoveItemsFromFormula(formula, [1, 3, 5, 7, 9])) # 6aaabb

            self.play(ReplaceItemsInFormula(formula, [1, 2, 3], ['x', 'x', '$x$'])) # 6xxxbb
            
            self.play(RemoveItemsFromFormula(formula, [0])) # xxxbb

            self.play(WriteExponentInFormula(formula, 0, 2, 'x', 3)) # x^3bb

            self.play(WriteExponentInFormula(formula, 2, 3, 'b', 2)) # x^3b^2

            self.play(ReplaceItemsInFormula(formula, [1, 2], ['$^4$', 'x'])) # x^3x^2

            self.play(CombineTwoExponents(formula, [0, 2], [1, 3], '6', [], BLUE, RED)) # x^6

            self.wait()
            self.play(FadeOut(formula))
            self.wait()


        test_animations(formula_1)
        test_animations(formula_2)
