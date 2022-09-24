from manim import *
from hanrahashiv import FormulaModifications
from constants import ARMTEX, ENGTEX

# FIXME import doesn't work
class test(FormulaModifications):
    def construct(self):

        tex_1 = Tex(
            '3', '$\cdot$', 'a', '$\cdot$', 'b','$\cdot$',
            'a', '$\cdot$', '2', '$\cdot$', 'a', '$\cdot$', 'b',
            font_size=70, tex_template=ENGTEX
        ) # 3aba2a

        self.add(tex_1)
        self.wait()

        self.rearrange_formula(tex_1, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13], [8], [], [9], [1]) # 23abaab
        self.wait()

        self.multiply_numbers_in_formula(tex_1, 3, 6) # 6•a•b•a•a•b
        self.wait()

        self.rearrange_formula(tex_1, [0, 1, 2, 5, 6, 7, 8, 9, 10, 3, 4], [4], [], [3], [-2]) # 6•a•a•a•b•b
        self.wait()

        self.write_exponents_in_formula(tex_1, 2, 6, 'a', 3) # 6•a^3•b•b
        self.wait()

        self.write_exponents_in_formula(tex_1, 4, 6, 'b', 2) # 6•a^3•b^2
        self.wait()

