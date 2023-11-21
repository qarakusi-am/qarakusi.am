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
        formula_1[2].set_color(TEAL)
        formula_1[4].set_color(RED)
        formula_1[8].set_color(BLUE)
        formula_1[10].set_color(GREEN)

        formula_2 = MathTex(
            '3', '\cdot', 'a', '\cdot', 'b','\cdot',
            'a', '\cdot', '2', '\cdot', 'a', '\cdot', 'b',
            font_size=70, tex_template=ENGTEX
        ) # 3•a•b•a•2•a•b
        formula_2[0].set_color(ORANGE)
        formula_1[2].set_color(PINK)
        formula_2[4].set_color(RED)
        formula_2[8].set_color(BLUE)
        formula_2[10].set_color(GREEN)

        self.play(Write(formula_1)) # 3•a•b•a•2•a•b
        self.fix_formula(formula_1)
        self.wait()

        self.play(formula_1[0].animate.scale(2).set_color(BLUE))
        self.wait()

        self.play(
            ModifyFormula(formula_1,
                remove_items=[1, 5],
                add_after_items=[0, 3, 8], add_items_strs=[['$a$', '$^2$'], ['$b$'], ['$^5$']], add_items_colors=[[GREEN, YELLOW], [], [BLUE]],
                replace_items=[[2], [6, 7], [10]], replace_items_strs=[['$c$'], ['$d$', '$^3$', ' $\\times$ '], ['$e$', '$^2$']], 
                replace_items_colors=[[ORANGE], [None, RED], [WHITE, ORANGE]],
                new_formula_alignment=LEFT, add_items_animation_style=FadeIn, add_lag_ratio=0.3, new_font_size=70
            ),
            run_time=1.5
        ) # 3•a•b•a•2•a•b -> 3a•ba•2•a•b -> 3a^2a•bba•2^5•a•b -> 3a^2c•bbd^3 x 2^5•e^2•b
        self.wait()

        self.rearrange_formula(
            formula_1, new_sequence=[10, 11, 12, 0, 1, 2, 3, 7, 8, 9, 13, 14, 4, 5, 6, 15, 16], 
            move_up=[5, 6], move_down=[10, 11], fade_out=[4, 12], fade_in=[2, 12]
        ) # 3a^2c•bbd^3 x 2^5•e^2•b -> 2^5•3•a^2cd^3 x e^2•bb•b

        self.play(FadeOut(formula_1))
        self.wait()



        self.play(Write(formula_2)) # 3•a•b•a•2•a•b
        self.fix_formula(formula_2)
        self.wait()

        self.play(
            ModifyFormula(formula_2,
                remove_items=[1, 5],
                add_after_items=[0, 3, 8], add_items_strs=[['a', '^2'], ['b'], ['^5']], add_items_colors=[[GREEN, YELLOW], [], [BLUE]],
                replace_items=[[2], [6, 7], [10]], replace_items_strs=[['c'], ['d', '^3', ' \\times '], ['e', '^2']], replace_items_colors=[[ORANGE], [None, RED], [WHITE, ORANGE]],
                new_formula_alignment=DL, add_items_animation_style=FadeIn, add_lag_ratio=0.3
            ),
            run_time=1.5
        ) # 3•a•b•a•2•a•b -> 3a•ba•2•a•b -> 3a^2a•bba•2^5•a•b -> 3a^2c•bbd^3 x 2^5•e^2•b
        self.wait()

        self.rearrange_formula(
            formula_2, new_sequence=[10, 11, 12, 0, 1, 2, 3, 7, 8, 9, 13, 14, 4, 5, 6, 15, 16], 
            move_up=[5, 6], move_down=[10, 11], fade_out=[4, 12], fade_in=[2, 12]
        ) # 3a^2c•bbd^3 x 2^5•e^2•b -> 2^5•3•a^2cd^3 x e^2•bb•b

        self.play(FadeOut(formula_2))
        self.wait()

        operation_1 = MathTex("x^{2}", "+", "14", "x", "-", "32", "=", "0")
        self.play(FadeIn(operation_1))
        self.wait()
        self.fix_formula(operation_1)
        self.rearrange_formula(operation_1, new_sequence=[0, 1, 2, 3, 6, 4, 5], move_up=[4, 5], remove=[7])
        self.wait(2)
