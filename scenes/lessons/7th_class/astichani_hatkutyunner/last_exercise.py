from manim import Scene
from manim import Indicate
from manim import Write, ReplacementTransform
from manim import DOWN, UP, DL, RIGHT, LEFT
from manim import Tex

from hanrahashiv import CombineTwoExponents

class last_exercise(Scene):
    def construct(self):
        
        formula = Tex ('$($', '$a$', '$^2$', '$)$', '$^5$', '$\cdot$', '$a$', '$^3$',
                '$=$', '$a$', '$^{10}$', '$\cdot$', '$a$', '$^3$'
        )
        formula_1 = formula[:5].copy()
        formula_2 = formula[5:8].copy()

    # բանաձևը գրում ենք ու (a^2)^5-ը իջացնում ներքև
        self.wait()
        self.play(Write(formula[:9]))
        self.wait()
        
        self.play(Indicate(formula[:5]))
        self.wait()

        self.play(formula_1.animate.shift(DOWN))
        self.wait()

    # օգտվում ենք վերջին հատկությունից (Նարեկ, տվոյ վիխըդ)



    # (a^2)^5 -> a^10
        formula_1_new = Tex('$a$', '$^($', '$^2$','$^{\cdot}$', '$^5$', '$^)$').shift(UP)
        formula_1_new.align_to(formula_1[1], DL)
        formula_1_new_new = Tex('$a$', '$^{10}$').align_to(formula_1_new, DL)

        self.play(
            ReplacementTransform(formula_1[0], formula_1_new[1]),
            ReplacementTransform(formula_1[2], formula_1_new[2]),
            ReplacementTransform(formula_1[3], formula_1_new[5]),
            ReplacementTransform(formula_1[4], formula_1_new[4]),
            Write(formula_1_new[3])
        )
        self.add(formula_1_new[0])
        self.remove(formula_1[1])
        self.wait()

        self.play(ReplacementTransform(formula_1_new[1:], formula_1_new_new[1]))
        self.add(formula_1_new_new[0])
        self.remove(formula_1_new[0])
        self.wait()

        self.play(formula_2.animate.next_to(formula_1_new, 0.8 * RIGHT))
        self.wait()

    # տանում ենք հավասարության աջ մաս
        self.play(
            ReplacementTransform(formula_1_new_new, formula[9:11]),
            ReplacementTransform(formula_2, formula[11:])
        )
        self.wait()
    
    # ստանում ենք պատասխանը
        self.play(CombineTwoExponents(formula, [9, 12], [10, 13], '13', [11]))
        self.wait()

    # երկրորդ վարժություն
        formula_2 = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^5$').next_to(formula, DOWN).align_to(formula, LEFT)

        self.play(Write(formula_2))
        self.wait()
