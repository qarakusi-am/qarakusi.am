from manim import *
from hanrahashiv import FormulaModificationsScene
from constants import ARMTEX, ENGTEX

class test(FormulaModificationsScene):
    def construct(self):

        formula_1 = Tex(
            '$3$', '$\cdot$', '$a$', '$\cdot$', '$b$','$\cdot$',
            '$a$', '$\cdot$', '$2$', '$\cdot$', '$a$', '$\cdot$', '$b$',
            font_size=70, tex_template=ENGTEX
        ) # 3•a•b•a•2•a•b

        self.add(formula_1)
        self.wait()

        self.rearrange_formula(formula_1, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13], [8], [], [9], [1]) # 2•3•a•b•a•a•b
        self.wait()

        self.multiply_numbers_in_formula(formula_1, 3, 6) # 6•a•b•a•a•b
        self.wait()

        self.rearrange_formula(formula_1, [0, 1, 2, 5, 6, 7, 8, 9, 10, 3, 4], [4], [], [3], [-2]) # 6•a•a•a•b•b
        self.wait()

        self.write_exponent_in_formula(formula_1, 2, 6, 'a', 3) # 6•a^3•b•b
        self.wait()
        self.write_exponent_in_formula(formula_1, 5, 7, 'b', 2) # 6•a^3•b^2
        self.wait()

        self.extract_exponent_in_formula(formula_1, 2, 'a', 3) # 6•aaa•b^2
        self.wait()
        self.extract_exponent_in_formula(formula_1, 6, 'b', 2) # 6•aaa•bb
        self.wait()

        self.add_items_in_formula(formula_1, [2, 3, 6], ['\cdot', '\cdot', '\cdot']) # 6•a•a•a•b•b
        self.wait()
        self.write_exponent_in_formula(formula_1, 2, 6, 'a', 3) # 6•a^3•b•b
        self.wait()

        self.play(FadeOut(formula_1))



        formula_3 = Tex(
            '$2$', '$\cdot$', '$b$', '$^2$', '$a$', '$\cdot$', '$3$', '$b$', '$a$', '$^3$',
            font_size=70, tex_template=ENGTEX
        ) # 2•b^2•a•3•b•a^3

        self.add(formula_3) # 2•b^2a•3ba^3
        self.wait()

        self.rearrange_formula(formula_3, [0, 5, 6, 1, 2, 3, 4, 7, 8, 9, 10], [6], [], [5], [1]) # 2•3•b^2aba^3
        self.wait()

        self.multiply_numbers_in_formula(formula_3, 3, 6) # 6•b^2aba^3
        self.wait()

        self.rearrange_formula(formula_3, [0, 1, 4, 6, 7, 2, 3, 5], [6, 7], [2, 3]) # 6•aa^3bb^2
        self.wait()

        self.write_exponent_in_formula(formula_3, 2, 4, 'a', 4) # 6•a^4bb^2
        self.wait()

        self.write_exponent_in_formula(formula_3, 4, 6, 'b', 3) # 6•a^4b^3
        self.wait()

        self.extract_exponent_in_formula(formula_3, 2, 'a', 4, True) # 6•a•a•a•ab^3
        self.wait()

        self.add_items_in_formula(formula_3, [8], ['$\cdot$']) # 6•a•a•a•a•b^3
        self.wait()

        self.extract_exponent_in_formula(formula_3, 10, 'b', 3) # 6•a•a•a•a•b^3
        self.wait()

        self.remove_items_from_formula(formula_3, [1, 3, 5, 7, 9]) # 6aaaab^3
        self.wait()

        self.add_items_in_formula(formula_3, [0, 1, 2, 3, 4], ['\cdot', '\cdot', '\cdot', '\cdot', '\cdot']) # 6•a•a•a•a•b^3
        self.wait()

        self.write_exponent_in_formula(formula_3, 2, 4, 'a', 2) # 6•a^2•a•a•b^3
        self.wait()

        self.write_exponent_in_formula(formula_3, 5, 7, 'a', 2) # 6•a^2•a^2•b^3
        self.wait()

        formula_3_copy = formula_3.copy().shift(DOWN)
        self.add(formula_3_copy)
        self.wait()
        self.write_exponent_in_formula(formula_3_copy, 2, 6, 'a', 4, run_time=2) # 6•a^4•b^3
        self.wait()

        self.combine_two_exponents(formula_3, [2, 5], [3, 6], 4, [4], run_time=2) # 6•a^4•b^3
        self.wait()
        
        self.remove_items_from_formula(formula_3, [2]) # 6•^4•b^3
        self.wait()
