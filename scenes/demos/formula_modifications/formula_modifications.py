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
            self.fix_formula(formula)
            self.wait()

            self.rearrange_formula(formula, new_sequence=[8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13], move_up=[8], move_down=[], fade_out=[9], fade_in=[1]) # 2•3•a•b•a•a•b

            self.play(MultiplyNumbersInFormula(formula, number_of_multiplying_items=3, resulting_number_str='6', resulting_number_color=YELLOW)) # 6•a•b•a•a•b

            self.rearrange_formula(formula, new_sequence=[0, 1, 2, 5, 6, 7, 8, 9, 10, 3, 4], move_up=[4], move_down=[], fade_out=[3], fade_in=[-2]) # 6•a•a•a•b•b

            self.play(WriteExponentInFormula(formula, first_item_index=2, last_item_index=6, base='a', exponent='3', base_color=BLUE, exponent_color=ORANGE)) # 6•a^3•b•b

            self.play(WriteExponentInFormula(formula, first_item_index=5, last_item_index=7, base='b', exponent=2, base_color=None, exponent_color=GREEN)) # 6•a^3•b^2

            self.play(RemoveItemsFromFormula(formula, items_indices=[1, 4])) # 6a^3b^2

            self.play(AddItemsInFormula(formula, after_items=[0, 2], items_str_list=['\cdot', '$\cdot$'])) # 6•a^3•b^2

            self.play(ExtractExponentInFormula(formula, item_index=2, base='a', exponent='3', add_multiplication_signs_in_between=False, base_color=ORANGE)) # 6•aaa•b^2
            
            self.play(ExtractExponentInFormula(formula, item_index=6, base='b', exponent='2', add_multiplication_signs_in_between=True, base_color=GREEN)) # 6•aaa•b•b

            self.play(AddItemsInFormula(formula, after_items=[2, 3], items_str_list=['\cdot', '\cdot'], colors=[YELLOW, RED])) # 6•a•a•a•b•b

            self.play(RemoveItemsFromFormula(formula, [1, 3, 5, 7, 9])) # 6aaabb

            self.play(ReplaceItemsInFormula(formula, [1, 2, 3], ['x', 'x', '$x$'])) # 6xxxbb
            
            self.play(RemoveItemsFromFormula(formula, [0])) # xxxbb

            self.play(WriteExponentInFormula(formula, 0, 2, 'x', 3)) # x^3bb

            self.play(WriteExponentInFormula(formula, 2, 3, 'b', 2)) # x^3b^2

            self.play(ReplaceItemsInFormula(formula, items_indices=[1, 2], items_str_list=['$^4$', 'x'])) # x^3x^2

            self.play(CombineTwoExponents(formula, bases_indices=[0, 2], exponents_indices=[1, 3], new_exponent='6', fade_out=[], base_color=BLUE, exponent_color=RED)) # x^6

            self.wait()
            self.play(FadeOut(formula))
            self.wait()


        test_animations(formula_1)
        test_animations(formula_2)
