from hanrahashiv import FormulaModificationsScene, ModifyFormula

from manim import MathTex, Tex
from manim import VGroup
from manim import RIGHT, LEFT, DOWN, DL
from manim import BLUE, YELLOW, GREEN, ORANGE, RED, LIGHT_BROWN, WHITE
from manim import Circumscribe, Indicate
from manim import Write, ReplacementTransform, Create, Wiggle
from manim import SurroundingRectangle
from manim import there_and_back

class Exercises(FormulaModificationsScene):
    def construct(self):
        
        left_boundary = -5.5
        up_boundary = 3.25
        size = 55

        exponent_law = MathTex('a', '^m', '\cdot', 'a', '^n', '=', 'a', '^{m+n}', font_size=55)
        exponent_law.move_to([left_boundary + 9.5, 0, 0])

        sur_rec_m = SurroundingRectangle(exponent_law[1], corner_radius=0.2, color=BLUE)
        sur_rec_n = SurroundingRectangle(exponent_law[4], corner_radius=0.2, color=BLUE)
        sur_rec_mn = SurroundingRectangle(exponent_law[7], corner_radius=0.2, color=BLUE)
        sur_rec_law = SurroundingRectangle(exponent_law, color=YELLOW, buff=0.25)
        sur_rec_law.set_stroke(width=6)

    # first exercise
        first = Tex('$1)$', font_size=size).move_to([left_boundary, up_boundary, 0])
        exp = Tex('$3$', '$d$', '$^2$', '$\cdot$', '$2$', '$a$', '$d$', font_size=size).next_to(first, RIGHT)
        monom = Tex('$2$', '$a$', '$d$', font_size=size).move_to([-2.5, up_boundary, 0])

        eq_1 = Tex('$=$', font_size=size).next_to(exp[-1], RIGHT)
        ex = exp.copy()

        self.wait()

        self.play(Write(first))
        self.wait()

        self.play(Write(exp[:3]))
        self.wait()

        self.play(Write(monom))
        self.wait()

        self.play(monom.animate.move_to(exp[4:]))
        self.wait()

        self.add(exp[4:])
        self.remove(monom)

        self.play(Write(exp[3]))
        self.wait()

        self.play(Write(eq_1))
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

    # թվերը բերում ենք առաջ
        self.play(
            ex[0].animate.set_color(YELLOW),
            ex[4].animate.set_color(YELLOW)
        )
        self.wait()

        self.rearrange_formula(ex, [4, 3, 0, 1, 2, 5, 6], [4], [], [3], [3]) # 2*3d^2ad
        self.wait()

    # թվերը բազմպատկում ենք
        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[0, 1, 2]],
                replace_items_strs=[['$6$']],
                replace_items_colors=[[YELLOW]]
            )
        ) # 6d^2ad
        self.wait()

    # a-ն բերում ենք առաջ
        self.play(
            ex[3].animate.set_color(RED),
            ex[1].animate.set_color(BLUE),
            ex[2].animate.set_color(BLUE),
            ex[4].animate.set_color(BLUE)
        )
        self.rearrange_formula(ex, [0, 3, 1, 2, 4], [3], [], [], []) # 6ad^2d
        self.wait()

        self.play(Indicate(ex[1], scale_factor=1.5, color=RED))
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                add_after_items=[3],
                add_items_strs=[['$\\cdot$']],
                add_items_colors=[[WHITE]]
            )
        ) # 6ad^2*d
        self.wait()

        x = Tex('$6$', '$a$', '$d$', '$^2$', '$\cdot$', '$d$', font_size=size).align_to(ex, DL)
        x[0].set_color(YELLOW)
        x[1].set_color(RED)
        x[2].set_color(BLUE)
        x[3].set_color(BLUE)
        x[5].set_color(BLUE)

    # d^2 = d * d
        self.play(Indicate(ex[2:4], scale_factor=1.5, color=BLUE))
        self.wait()
        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[3]],
                replace_items_strs=[['$\\cdot$', '$d$']],
                replace_items_colors=[[WHITE, BLUE]]
            )
        ) # 6ad*d*d
        self.wait()

    # d * d * d = d^3
        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[3, 4, 5, 6]],
                replace_items_strs=[['$^3$']],
                replace_items_colors=[[BLUE]]
            )
        ) # 6ad^3
        self.wait(2)

    # d^3 = d^2 * d
        self.play(ReplacementTransform(ex[2:], x[2:]))
        self.add(x)
        self.remove(ex)

        ex = x

    # ցուցչի հատկություն
        self.play(Write(exponent_law))
        self.wait()

        self.play(
            Create(sur_rec_m),
            Create(sur_rec_mn),
            Create(sur_rec_n)
        )
        self.play(Create(sur_rec_law))
        self.wait()

    # d^2 * d^1 = d^3
        eq_2 = Tex('$=$', font_size=size).next_to(ex[-1], RIGHT)
        ans = Tex('$6$', '$a$', '$d$', '$^3$', font_size=size).next_to(eq_2, RIGHT)
        ans[0].set_color(YELLOW)
        ans[1].set_color(RED)
        ans[2].set_color(BLUE)
        ans[3].set_color(BLUE)
        ans_exponent_place = ans[2].get_center() + ex[3].get_center() - ex[2].get_center()
        one_power = Tex('$^1$', font_size=size, color=BLUE).move_to(ex[3].get_center() - ex[2].get_center() + ex[5].get_center())

    # answer
        self.play(Write(one_power))
        self.wait()

        self.play(Write(eq_2))
        self.wait()

        self.play(Write(ans[:2]))
        self.wait()

        self.play(Indicate(VGroup(ex[2:], one_power), color=BLUE))
        self.wait()

        self.play(Write(ans[2]))
        self.wait()

        m = ex[3].copy()
        n = one_power.copy()
        plus = Tex('$^+$', font_size=size, color=BLUE).next_to(ans_exponent_place, RIGHT, buff=0.2)

        self.play(
            m.animate.move_to(ans_exponent_place),
            Write(plus),
            n.animate.next_to(plus, RIGHT, buff=0.17)
        )
        self.wait()

        self.play(ReplacementTransform(VGroup(m, plus, n), ans[3]))
        self.wait()

    # second exercise
    # փոփոխականների անունները կրկնվում են առաջին վարժության փոփոխականների անունների հետ
        second = Tex('$2)$', font_size=size).next_to(first, DOWN, buff=0.6)
        exp = Tex(r'$\frac{1}{4}$', '$x$', '$a$', '$\cdot$', '$x$', '$\cdot$', '$6$', '$b$', '$a$', font_size=size).next_to(second, RIGHT)
        monom = Tex('$x$', '$\cdot$', '$6$', '$b$', '$a$', font_size=size).next_to(second, RIGHT, buff=3).align_to(exp[1], DOWN)

        eq_1 = Tex('$=$', font_size=size).next_to(exp[-1], RIGHT)
        ex = exp.copy()
        self.wait()

        self.play(Write(second))
        self.wait()

        self.play(Write(exp[:3]))
        self.wait()

        self.play(Write(monom))
        self.wait()

        self.play(monom.animate.move_to(exp[4:]))
        self.wait()

        self.play(Write(exp[3]))
        self.wait()

        self.add(exp[4:])
        self.remove(monom)

        self.play(Write(eq_1))
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

    # թվերը բերում ենք առաջ ու բազմապատկում
        self.play(
            ex[0].animate.set_color(YELLOW),
            ex[6].animate.set_color(YELLOW)
        )

        self.rearrange_formula(ex, [6, 5, 0, 1, 2, 3, 4, 7, 8], [6], [], [5], [5]) # 6*(1/4)xa*xba
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[0, 1, 2]],
                replace_items_strs=[['$\\frac{3}{2}$']],
                replace_items_colors=[[YELLOW]]
            )
        ) # (3/2)xa*xba
        self.wait()

        self.play(Indicate(ex[0], scale_factor=1.5))
        self.wait()

        self.play(
            ex[1].animate.set_color(GREEN),
            ex[4].animate.set_color(GREEN),
            ex[2].animate.set_color(ORANGE),
            ex[6].animate.set_color(ORANGE),
            ex[5].animate.set_color(BLUE)
        )
        self.wait()

        self.rearrange_formula(ex, [0, 1, 4, 2, 6, 3, 5], [4], [6], [], []) # (3/2)xxaa*b
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                add_after_items=[2],
                add_items_strs=[['$\\cdot$']]
            )
        ) # (3/2)xx*aa*b
        self.wait()

        self.rearrange_formula(ex, [0, 4, 5, 6, 7, 3, 1, 2], [1, 2], [4, 5], [3, 6], [3, 6]) # (3/2)aa*b*xx
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[2]],
                replace_items_strs=[['$^2$']],
                replace_items_colors=[[RED]]
            )
        ) # (3/2)a^2*b*xx
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[7]],
                replace_items_strs=[['$^2$']],
                replace_items_colors=[[GREEN]]
            )
        ) # (3/2)a^2*b*x^2
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                remove_items=[3, 5]
            )
        ) # (3/2)a^2bx^2
        self.wait()

    # add third, fourth, fifth, sixth
        third = Tex('$3)$', font_size=size).next_to(second, DOWN, buff=0.6)
        exp_3 = Tex('$2$', '$x$', '$\cdot$', '$b$', '$3$', '$b$', font_size=size).next_to(third, RIGHT)

        fourth = Tex('$4)$', font_size=size).next_to(third, DOWN, buff=0.6)
        exp_4 = Tex('$y$', '$^2$', '$\cdot$', '$7$', '$x$', '$y$', font_size=size).next_to(fourth, RIGHT)

        fifth = Tex('$5)$', font_size=size).next_to(fourth, DOWN, buff=0.6)
        exp_5 = Tex('$a$', '$^4$', '$9$', '$\cdot$', '$b$', '$^2$', '$a$', '$b$', font_size=size).next_to(fifth, RIGHT)

        sixth = Tex('$6)$', font_size=size).next_to(fifth, DOWN, buff=0.6)
        exp_6 = Tex('$3$', '$x$', '$^2$', '$y$', '$^3$', '$\cdot$', '$8$', '$a$', '$^2$', '$x$', '$^3$', font_size=size).next_to(sixth, RIGHT)

        self.add(third, fourth, fifth, sixth, exp_3, exp_4, exp_5, exp_6)
        self.wait(2)

    # third exercise
        exp = exp_3 #2x*b3b
        eq_1 = Tex('$=$', font_size=size).next_to(exp[-1], RIGHT)

        ex = exp.copy()
        self.wait()

        self.play(Write(eq_1))
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

        self.play(
            ex[4].animate.set_color(YELLOW),
            ex[0].animate.set_color(YELLOW)
        )
        self.wait()

        self.rearrange_formula(ex, [4, 2, 0, 1, 3, 5], [4], [], [2], [2]) # 3*2xbb
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[0, 1, 2]],
                replace_items_strs=[['$6$']],
                replace_items_colors=[[YELLOW]]
            )
        ) # 6xbb
        self.wait()

        self.play(Wiggle(ex[2:], scale_value=1.5))
        self.wait()

        self.play(
            ex[2:].animate.set_color(GREEN),
            ex[1].animate.set_color(ORANGE)
        )
        self.wait()

        self.rearrange_formula(ex, [0, 2, 3, 1], [1], [], [], []) # 6bbx
        self.wait(0.5)

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[2]],
                replace_items_strs=[['$^2$']],
                replace_items_colors=[[GREEN]]
            )
        ) # 6b^2x
        self.wait()

    # fourth exercise
        exp = exp_4 # y^2*7xy
        eq_1 = Tex('$=$', font_size=size).next_to(exp[-1], RIGHT)

        ex = exp.copy()
        self.wait()

        self.play(Write(eq_1))
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

        self.play(ex[3].animate.set_color(YELLOW))
        self.wait()

        self.rearrange_formula(ex, [3, 0, 1, 2, 4, 5], [3], [], [], []) # 7y^2*xy
        self.wait()

        self.play(
            ex[1].animate.set_color(BLUE),
            ex[2].animate.set_color(BLUE),
            ex[5].animate.set_color(BLUE),
            ex[4].animate.set_color(LIGHT_BROWN)
        )

        self.rearrange_formula(ex, [0, 4, 5, 3, 1, 2], [1, 2], [], [3], [3]) # 7xy*y^2
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[3, 4, 5]],
                replace_items_strs=[['$^3$']],
                replace_items_colors=[[BLUE]]
            )
        ) # 7xy^3
        self.wait()

    # fifth exercise
        exp = exp_5 # a^4 9*b^2 ab
        eq_1 = Tex('$=$', font_size=size).next_to(exp[-1], RIGHT)

        ex = exp.copy()
        self.wait()

        self.play(Indicate(VGroup(fifth, exp)))
        self.wait()

        self.play(Circumscribe(exp[2]))
        self.wait()

        self.add(eq_1)
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

        self.play(ex[2].animate.set_color(YELLOW))
        self.wait()

        self.rearrange_formula(ex, [2, 0, 1, 3, 4, 5, 6, 7], [2], [], [], []) # 9a^4*b^2ab
        self.wait()

        self.play(
            VGroup(ex[1:3], ex[6]).animate.set_color(GREEN),
            VGroup(ex[4:6], ex[7]).animate.set_color(ORANGE)
        )
        self.wait()

        self.rearrange_formula(ex, [0, 1, 2, 6, 3, 4, 5, 7], [6], [], [], []) # 9a^4a*b^2b
        self.wait()

        eq_2 = Tex('$=$', font_size=size).next_to(ex[-1], RIGHT)
        ans = Tex('$9$', '$a$', '$^5$', '$b$', '$^3$', font_size=size).next_to(eq_2, RIGHT)
        ans[0].set_color(YELLOW)
        ans[1:3].set_color(GREEN)
        ans[3:].set_color(ORANGE)

        exponent_position_for_a = ex[2].get_center() - ex[1].get_center()
        one_power_1 = Tex('$^1$', font_size=size).next_to(ex[3], exponent_position_for_a).shift(0.08 * LEFT).align_to(ex[2], DOWN)
        one_power_1.set_color(GREEN)
        plus_1 = Tex('$^+$', font_size=size).next_to(ans[1].get_center() + exponent_position_for_a, buff=0.18)
        plus_1.set_color(GREEN)

        exponent_position_for_b = ex[6].get_center() - ex[5].get_center()
        one_power_2 = Tex('$^1$', font_size=size).next_to(ex[7], exponent_position_for_b).align_to(ex[6], DOWN)
        one_power_2.set_color(ORANGE)
        plus_2 = Tex('$^+$', font_size=size).next_to(ans[3].get_center() + exponent_position_for_b, buff=0.18)
        plus_2.set_color(ORANGE)

        self.play(
            VGroup(exponent_law, sur_rec_law, sur_rec_m, sur_rec_mn, sur_rec_n).animate.scale(1.5),
            rate_func=there_and_back
        )

        self.play(Write(eq_2))
        self.wait()

        self.play(
            Write(one_power_1),
            Write(one_power_2)
        )
        self.wait()

        self.play(Write(ans[:2]))
        self.wait()

        m = ex[2].copy()
        n = one_power_1.copy()

        self.play(
            m.animate.next_to(ans[1], exponent_position_for_a).align_to(ex[2], DOWN),
            Write(plus_1),
            n.animate.next_to(plus_1, RIGHT, buff=0.1).align_to(ex[2], DOWN)
        )
        self.wait()

        self.play(ReplacementTransform(VGroup(m, plus_1, n), ans[2]))
        self.wait()

        self.play(Write(ans[3]))
        self.wait()

        m = ex[6].copy()
        n = one_power_2.copy()

        self.play(
            m.animate.next_to(ans[3], exponent_position_for_b).align_to(ex[6], DOWN),
            Write(plus_2),
            n.animate.next_to(plus_2, RIGHT, buff=0.1).align_to(ex[6], DOWN)
        )
        self.wait()

        self.play(ReplacementTransform(VGroup(m, plus_2, n), ans[4]))
        self.wait()

    # sixth exercise
        exp = exp_6 # 3 x^2 y^3 * 8 a^2 x^3
        eq_1 = Tex('$=$', font_size=size).next_to(exp[-2], RIGHT)
        ex = exp.copy()

        self.play(Write(eq_1))
        self.wait()

        self.play(ex.animate.next_to(eq_1, RIGHT))
        self.wait()

        self.play(
            ex[6].animate.set_color(YELLOW),
            ex[0].animate.set_color(YELLOW)
        )
        self.wait()

        self.rearrange_formula(ex, [6, 5, 0, 1, 2, 3, 4, 7, 8, 9, 10], [6], [], [5], [5]) # 8*3x^2y^3a^2x^3
        self.wait()

        self.fix_formula(ex)
        self.play(
            ModifyFormula(
                ex,
                replace_items=[[0, 1, 2]],
                replace_items_strs=[['$24$']],
                replace_items_colors=[[YELLOW]]
            )
        ) # 24x^2y^3a^2x^3
        self.wait()

        self.play(Indicate(ex[0], scale_factor=1.5))
        self.wait()

        self.play(
            VGroup(ex[1:3], ex[7:]).animate.set_color(BLUE),
            ex[3:5].animate.set_color(ORANGE),
            ex[5:7].animate.set_color(RED)
        )
        self.wait()

        self.rearrange_formula(ex, [0, 1, 2, 7, 8, 3, 4, 5, 6], [7, 8], [], [], []) #24x^2x^3y^3a^2
        self.wait()

        self.rearrange_formula(ex, [0, 7, 8, 1, 2, 3, 4, 5, 6], [7, 8], [], [], [])
        self.wait()

        eq_2 = Tex('$=$', font_size=size).next_to(ex[-2], RIGHT)
        ans = Tex('$24$', '$a$', '$^2$', '$x$', '$^5$', '$y$', '$^3$', font_size=size).next_to(eq_2, RIGHT)
        ans[0].set_color(YELLOW)
        ans[1:3].set_color(RED)
        ans[3:5].set_color(BLUE)
        ans[5:].set_color(ORANGE)

        self.play(Write(eq_2))
        self.wait()

        self.play(Write(ans[:4]))
        self.wait()

        exponent_position_for_x = ex[4].get_center() - ex[3].get_center()

        m = ex[4].copy()
        plus = Tex('$^+$', font_size=size).next_to(ans[3].get_center() + exponent_position_for_x, RIGHT, buff=0.18).set_color(BLUE)
        n = ex[6].copy()

        self.play(
            VGroup(exponent_law, sur_rec_law, sur_rec_m, sur_rec_mn, sur_rec_n).animate.scale(1.5),
            rate_func=there_and_back
        )
        self.play(
            m.animate.next_to(plus, LEFT, buff=0.1),
            Write(plus),
            n.animate.next_to(plus, RIGHT, buff=0.1)
        )
        self.wait()

        self.play(ReplacementTransform(VGroup(m, plus, n), ans[4]))
        self.wait()

        self.play(Write(ans[5:]))
        self.wait()
