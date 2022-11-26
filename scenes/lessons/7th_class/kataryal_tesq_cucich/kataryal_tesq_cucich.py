from manim import Tex, MathTex
from manim import VGroup, SVGMobject
from manim import Arrow, Circle, SurroundingRectangle, Brace
from manim import DOWN, RIGHT, LEFT, UP, UR, UL, DR, PI
from manim import AnimationGroup, Write, Create, FadeIn, FadeOut, ReplacementTransform, Circumscribe
from manim import YELLOW, BLUE
from manim import there_and_back_with_pause
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from constants import ARMTEX

class TwoSimpleExamples(FormulaModificationsScene):
    def construct(self):

# INITS
    # first example    x•2 = 2•x
        first_example_equation = Tex('$x$', ' $\cdot$ ', '$2$', ' $=$ ', '$x$', ' $\cdot$ ', '$2$').shift(UP).shift(LEFT)
        x_times_two = Tex('$x$', ' $\cdot$ ', '$2$').move_to(first_example_equation[:3])
        two_times_x_1 = Tex('$x$', ' $\cdot$ ', '$2$').move_to(first_example_equation[4:])
        first_equality = Tex(' $=$ ').move_to(first_example_equation[3])
        two_times_x_2 = Tex('$2$', ' $\cdot$ ', '$x$').next_to(first_example_equation, RIGHT, buff=1)
        first_ex_arrows = VGroup(
            Arrow().rotate(- 3/14 * PI).next_to(x_times_two, DOWN).shift(0.75 * RIGHT),
            Arrow().rotate(- 11/14 * PI).next_to(two_times_x_2, DOWN).shift(0.75 * LEFT)
        )
        first_are_the_same = Tex('Նույնն են', tex_template=ARMTEX).next_to(first_ex_arrows, DOWN)

    # second example    3•2•x•2 = 4•a•3
        sec_ex_first_equation_left = Tex('$3$', ' $\cdot$ ', '$2$', ' $\cdot$ ', '$a$', ' $\cdot$ ', '$2$') # 3•2•a•2
        sec_ex_first_equality = Tex(' $=$ ').next_to(sec_ex_first_equation_left)
        sec_ex_first_equation_right = Tex('$3$', ' $\cdot$ ', '$2$', ' $\cdot$ ', '$a$', ' $\cdot$ ', '$2$')
        sec_ex_first_equation_right.next_to(sec_ex_first_equality)
        VGroup(sec_ex_first_equation_left, sec_ex_first_equality, sec_ex_first_equation_right).move_to([0, -0.5, 0])

        sec_ex_second_equation_left = Tex('$4$', ' $\cdot$ ', '$a$', ' $\cdot$ ', '$3$') # 4•a•3
        sec_ex_second_equality = Tex(' $=$ ').next_to(sec_ex_second_equation_left)
        sec_ex_second_equation_right = Tex('$4$', ' $\cdot$ ', '$a$', ' $\cdot$ ', '$3$')
        sec_ex_second_equation_right.next_to(sec_ex_second_equality)
        VGroup(sec_ex_second_equation_left, sec_ex_second_equality, sec_ex_second_equation_right).move_to(1.5 * DOWN)

        sec_ex_arrows = VGroup(
                Arrow().rotate(- PI / 20).next_to(sec_ex_first_equation_right[3]).shift(0.2 * DOWN),
                Arrow().rotate(PI / 15).next_to(sec_ex_second_equation_right[3]).shift(0.2 * UP),
            )
        sec_are_the_same = Tex('Նույնն են', tex_template=ARMTEX).next_to(sec_ex_arrows)

# ANIMATIONS
        def animate_first_example():
            self.play(Write(x_times_two))
            self.wait(0.25)
            self.play(Write(two_times_x_2))
            self.wait()

            self.play(ReplacementTransform(x_times_two.copy(), two_times_x_1))
            self.play(Write(first_equality))
            self.wait()

            self.rearrange_formula(two_times_x_1, [2, 1, 0], [0], [2], run_time=2)
            self.wait()

            self.play(Create(first_ex_arrows))
            self.wait(0.1)
            self.play(Write(first_are_the_same))
            self.wait()

            self.play( 
                    VGroup(
                        x_times_two, two_times_x_1, two_times_x_2, 
                        first_equality, first_ex_arrows, first_are_the_same
                    ).animate.scale(0.75).shift(2 * UP)
            )
            self.wait()
        
        def animate_second_example():
            self.play(Write(sec_ex_first_equation_left, run_time=1.5))
            self.wait(0.25)
            self.play(Write(sec_ex_second_equation_left, run_time=1.5))
            self.wait()

        # first equation
            self.play(ReplacementTransform(sec_ex_first_equation_left.copy(), sec_ex_first_equation_right))
            self.play(Write(sec_ex_first_equality))
            self.wait()

            self.rearrange_formula(sec_ex_first_equation_right, [0, 1, 2, 5, 6, 3, 4], [6], [], [5], [3]) # 3•2•2•a
            self.wait()

            self.fix_formula(sec_ex_first_equation_right)
            self.play(ModifyFormula(sec_ex_first_equation_right, replace_items=[[0, 1, 2, 3, 4]], replace_items_strs=[['$12$']]))
            self.wait()

        # second equation
            self.play(ReplacementTransform(sec_ex_second_equation_left.copy(), sec_ex_second_equation_right))
            self.play(Write(sec_ex_second_equality))
            self.wait(0.5)

            self.rearrange_formula(sec_ex_second_equation_right, [0, 3, 4, 1, 2], [4], [], [3], [1], run_time=2) # 3•2•2•a
            self.wait(0.5)

            self.fix_formula(sec_ex_second_equation_right)
            self.play(ModifyFormula(sec_ex_second_equation_right, replace_items=[[0, 1, 2]], replace_items_strs=[['$12$']]))
            self.wait()

            self.play(Create(sec_ex_arrows))
            self.play(Write(sec_are_the_same))
            self.wait()

        
        animate_first_example()
        animate_second_example()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ThirdExample(FormulaModificationsScene):
    def construct(self):

# INITS
        first = Tex(
            '$a$', '$\cdot$', '$3$', '$\cdot$', '$a$', '$\cdot$', '$a$',
            '$\cdot$', '$b$', '$\cdot$', '$a$', '$\cdot$', '$2$', 
            '$\cdot$', '$b$', '$\cdot$', '$b$', '$\cdot$', '$a$'
        ) # a•3•a•a•b•a•2•b•b•a
        first_right = first.copy()

        second = Tex(
            '$b$', '$\cdot$', '$a$', '$\cdot$', '$a$', '$\cdot$', '$6$',
            '$\cdot$', '$b$', '$\cdot$', '$a$', '$\cdot$', '$b$', 
            '$\cdot$', '$a$', '$\cdot$', '$1$', '$\cdot$', '$a$'
        ) # b•a•a•6•b•a•b•a•1•a
        second_right = second.copy()

        third = Tex(
            '$a$', '$\cdot$', '$a$', '$\cdot$', '$b$', '$\cdot$', '$a$',
            '$\cdot$', '$b$', '$\cdot$', '$b$', '$\cdot$', '$a$', 
            '$\cdot$', '$a$', '$\cdot$', '$6$', '$\cdot$', '$b$'
        ) # a•a•b•a•b•b•a•a•6•b
        third_right = third.copy()

        fourth = Tex(
            '$2$', '$\cdot$', '$a$', '$\cdot$', '$a$', '$\cdot$', '$b$',
            '$\cdot$', '$a$', '$\cdot$', '$a$', '$\cdot$', '$2$', 
            '$\cdot$', '$a$', '$\cdot$', '$b$', '$\cdot$', '$b$'
        ) # 2•a•a•b•a•a•2•a•b•b
        fourth_right = fourth.copy()

        left_parts = VGroup(first, second, third, fourth).arrange(DOWN, buff=1).shift([-2, -1,  0])
        equalities = VGroup(*[MathTex('=').next_to(miandam) for miandam in left_parts]).next_to(left_parts)
        right_parts = VGroup(first_right, second_right, third_right, fourth_right)
        for i in range(len(right_parts)):
            right_parts[i].next_to(equalities[i])
        equalities.shift(0.05 * DOWN)
        indices = VGroup(Tex('1) '), Tex('2) '), Tex('3) '), Tex('4)' ))
        [indices[i].next_to(left_parts[i], LEFT) for i in range(len(indices))]

        rule_1 = Tex('Թվերը տանել առաջ և բազմապատկել', tex_template=ARMTEX).to_corner(UL)
        check_1 = SVGMobject('objects/SVG_files/check').scale(0.25).next_to(rule_1)

        rule_2 = Tex('Տառերը խմբավորել և դասավորել այբբենական կարգով', tex_template=ARMTEX)
        rule_2.next_to(rule_1, DOWN, aligned_edge=LEFT, buff=0.5)
        check_2 = SVGMobject('objects/SVG_files/check').scale(0.25).next_to(rule_2)

        rule_3 = Tex('Գրել աստիճանի տեսքով', tex_template=ARMTEX)
        rule_3.next_to(rule_2, DOWN, buff=0.5, aligned_edge=LEFT)
        check_3 = SVGMobject('objects/SVG_files/check').scale(0.25).next_to(rule_3)

        surr_rect_a = SurroundingRectangle(first_right[2:11], buff=0.05).shift(0.045 * DOWN)

        first_two_are_the_same = Tex('Նույնն են', tex_template=ARMTEX)

        first_two_are_equal = Tex('Հավասար են', tex_template=ARMTEX)
        brace_first_two = Brace(VGroup(first_right, second_right), RIGHT, 0.2, 1).scale(0.75)

        different_3 = Tex(' - հավասար չէ ոչ մեկին', tex_template=ARMTEX, font_size=35)
        different_4 = Tex(' - հավասար չէ ոչ մեկին', tex_template=ARMTEX, font_size=35)


# ANIMATIONS

        def animate_rearrange_and_multiply_numbers():

            self.play(Write(rule_1))
            self.wait()

        # first
            self.play(
                ReplacementTransform(first.copy(), first_right),
                Write(equalities[0])
            )
            self.wait(0.5)

            self.rearrange_formula(
                first_right, [2, 3, 12, 13, 0, 1, *range(4, 12), *range(14, 19)], [2, 12], [], [3, 13], [1, 3],
                run_time=2
            ) # 3•2•a•a•a•b•a•b•b•a
            self.wait(0.5)
            self.fix_formula(first_right)
            self.play(ModifyFormula(first_right, replace_items=[[0, 1, 2]], replace_items_strs=[['$6$']])) # 6•a•a•a•b•a•b•b•a
            self.wait(0.5)

        # second
            self.play(
                ReplacementTransform(second.copy(), second_right),
                Write(equalities[1])
            )
            self.wait(0.5)

            self.rearrange_formula(
                second_right, [6, 7, 16, 17, *range(6), *range(8, 16), 18], [6, 16], [], [7, 17], [1, 3],
                run_time=2
            ) # 6•1•b•a•a•b•a•b•a•a
            self.wait(0.5)
            self.fix_formula(second_right)
            self.play(ModifyFormula(second_right, replace_items=[[0, 1, 2]], replace_items_strs=[['$6$']])) # 6•b•a•a•b•a•b•a•a
            self.wait(0.5)
        
        # third
            self.play(
                ReplacementTransform(third.copy(), third_right),
                Write(equalities[2])
            )
            self.wait(0.5)

            self.rearrange_formula(
                third_right, [16, 17, *range(16), 18], [16], [], [17], [1],
                run_time=2
            ) # 6•a•a•b•a•b•b•a•a•b
            self.wait(0.5)

        # fourth
            self.play(
                ReplacementTransform(fourth.copy(), fourth_right),
                Write(equalities[3])
            )
            self.wait(0.5)

            self.rearrange_formula(
                fourth_right, [12, 13, *range(12), *range(14, 19)], [12], [], [13], [1],
                run_time=2
            ) # 2•a•a•b•a•a•2•a•b•b
            self.wait(0.5)
            self.fix_formula(fourth_right)
            self.play(ModifyFormula(fourth_right, replace_items=[[0, 1, 2]], replace_items_strs=[['$4$']])) # 4•a•a•b•a•a•a•b•b
            self.wait(0.5)

            self.play(Create(check_1))
            self.wait()

        def animate_group_letters():

            self.play(Write(rule_2))
            self.wait()
        
        # first
            self.rearrange_formula(
                first_right, [0, 1, 2, 3, 4, 5, 6, 9, 10, 15, 16, 7, 8, 11, 12, 13, 14], [7, 8, 11, 12, 13, 14],
                run_time=1.5
            ) # 6•a•a•a•a•a•b•b•b
            self.wait(0.5)

        # second  
            self.rearrange_formula(
                second_right, [0, 1, 2, 7, 8, 11, 12, 3, 4, 5, 6, 9, 10, 13, 14, 15, 16], [7, 8, 11, 12],
                run_time=1.5
            ) # 6•b•b•b•a•a•a•a•a
            self.wait(0.25)

            self.rearrange_formula(
                second_right, [0, *range(7, 17), *range(1, 7)], [*range(1, 7)],
                run_time=1.5
            ) # 6•a•a•a•a•a•b•b•b
            self.wait(0.25)
        
        # third
            self.rearrange_formula(
                third_right, [0, 1, 2, 3, 4, 7, 8, 13, 14, 15, 16, 5, 6, 9, 10, 11, 12, 17, 18], [5, 6, 9, 10, 11, 12],
                run_time=1.5
            ) # 6•a•a•a•a•a•b•b•b•b
            self.wait(0.25)

        # fourth
            self.rearrange_formula(
                fourth_right, [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 5, 6, 13, 14, 15, 16], [5, 6],
                run_time=1.5
            ) # 4•a•a•a•a•a•b•b•b
            self.wait(0.25)

            self.play(Create(check_2))
            self.wait()

            self.play(
                AnimationGroup(
                    FadeIn(Brace(VGroup(first_right, second_right), RIGHT, 0.1, 1), rate_func=there_and_back_with_pause, run_time=3),
                    Write(first_two_are_the_same.next_to(first_right, DR).shift(0.5 * RIGHT)),
                    lag_ratio=0.4
                )
            )
            self.wait(0.5)

            self.play(
                Create(SurroundingRectangle(third_right[-1]), rate_func=there_and_back_with_pause, run_time=1.5)
            )
            self.wait(0.5)
            self.play(
                Create(SurroundingRectangle(fourth_right[0]), rate_func=there_and_back_with_pause, run_time=1.5)
            )
            self.wait(0.5)

            self.play(Create(surr_rect_a))
            self.wait()
            self.play(FadeOut(surr_rect_a, first_two_are_the_same))
            self.wait()

        def animate_using_exponents():
            self.play(
            *[mob.animate.shift(0.1 * UP) for mob in [fourth, equalities[3], right_parts[3], indices[3]]],
            *[mob.animate.shift(0.3 * DOWN) for mob in [third, equalities[2], right_parts[2], indices[2]]],
            *[mob.animate.shift(0.7 * DOWN) for mob in [second, equalities[1], right_parts[1], indices[1]]],
            *[mob.animate.shift(1.1 * DOWN) for mob in [first, equalities[0], right_parts[0], indices[0]]],
        )
            self.wait()
            self.play(Write(rule_3))

        # first
            self.fix_formula(first_right)
            self.play(ModifyFormula(first_right, replace_items=[[*range(2, 11)]], replace_items_strs=[['$a$', '$^5$']])) # 6•a^5•b•b•b
            self.wait(0.5)
            self.fix_formula(first_right)
            self.play(ModifyFormula(first_right, replace_items=[[*range(5, 10)]], replace_items_strs=[['$b$', '$^3$']])) # 6•a^5•b^3
            self.wait(0.5)

        # second  
            self.fix_formula(second_right)
            self.play(ModifyFormula(second_right, replace_items=[[*range(2, 11)]], replace_items_strs=[['$a$', '$^5$']])) # 6•a^5•b•b•b
            self.wait(0.25)
            self.fix_formula(second_right)
            self.play(ModifyFormula(second_right, replace_items=[[*range(5, 10)]], replace_items_strs=[['$b$', '$^3$']])) # 6•a^5•b^3
            self.wait(0.25)
        
        # third
            self.fix_formula(third_right)
            self.play(ModifyFormula(third_right, replace_items=[[*range(2, 11)]], replace_items_strs=[['$a$', '$^5$']])) # 6•a^5•b•b•b
            self.wait(0.25)
            self.fix_formula(third_right)
            self.play(ModifyFormula(third_right, replace_items=[[*range(5, 12)]], replace_items_strs=[['$b$', '$^4$']])) # 6•a^5•b^4
            self.wait(0.25)

        # fourth
            self.fix_formula(fourth_right)
            self.play(ModifyFormula(fourth_right, replace_items=[[*range(2, 11)]], replace_items_strs=[['$a$', '$^5$']])) # 4•a^5•b•b•b
            self.wait(0.25)
            self.fix_formula(fourth_right)
            self.play(ModifyFormula(fourth_right, replace_items=[[*range(5, 10)]], replace_items_strs=[['$b$', '$^3$']])) # 4•a^5•b^3
            self.wait(0.25)
        
            self.play(Create(check_3))
            self.wait()

        def animate_havasar_nman_miandamner():
            self.play(Write(brace_first_two.next_to(VGroup(first_right, second_right))))
            self.play(Write(first_two_are_equal.next_to(brace_first_two, RIGHT)))
            self.wait(0.25)

            self.play(Write(different_3.next_to(third_right), run_time=0.75))
            self.wait(0.1)
            self.play(Write(different_4.next_to(fourth_right), run_time=0.75))
            self.wait()

            self.play(
                Circumscribe(first_right[0], fade_out=True, run_time=2.5),
                Circumscribe(second_right[0], fade_out=True, run_time=2.5),
                Circumscribe(third_right[0], fade_out=True, run_time=2.5),
                Circumscribe(fourth_right[0], fade_out=True, run_time=2.5),
            )
            self.wait()

            self.play(Circumscribe(fourth_right, fade_out=True, run_time=2))
            self.play(
                Circumscribe(first_right, fade_out=True, run_time=2),
                Circumscribe(second_right, fade_out=True, run_time=2)
            )
            self.wait()
        

        self.play(FadeIn(left_parts, indices))
        self.wait()
        animate_rearrange_and_multiply_numbers() # 2,39
        animate_group_letters() # 40,78
        animate_using_exponents() # 79,99
        animate_havasar_nman_miandamner() # 100,110
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class DefiningExponent(FormulaModificationsScene):
    def construct(self):

# INITS
        sum_a = Tex('$a+a+a+a+a$', ' $=$ ', '$5$', '$\cdot$', '$a$', font_size=70).shift(UP)
        brace_sum = Brace(sum_a[0], DOWN)
        quantity_sum = Tex('$5$', font_size=70).next_to(brace_sum, DOWN)

        product_a_5_hat = Tex('$a \cdot a \cdot a \cdot a \cdot a$', ' $=$ ', '$a$', '$^5$', font_size=70).shift(DOWN)
        brace_product_5 = Brace(product_a_5_hat[0], DOWN)
        quantity_product_5 = Tex('$5$', font_size=70).next_to(brace_product_5, DOWN)
        quantity_product_5_copy = quantity_product_5.copy()

        product_a_n_hat = Tex('$a \cdot a \cdot a \cdot ... \cdot a \cdot a$', '$=$', '$a$', '$^n$', font_size=70).shift(0.5 * DOWN)
        brace_product_n = Brace(product_a_n_hat[0], DOWN)
        quantity_product_n = Tex('$n$', font_size=70).next_to(brace_product_n, DOWN)

        case_1 = Tex('$a^1 = a$', font_size=70).shift(0.75 * UP)
        case_2 = Tex('$a^2 = a\cdot a$ - քառակուսի', font_size=70, tex_template=ARMTEX).shift(0.75 * DOWN)
        case_3 = Tex('$a^3 = a\cdot a\cdot a$ - խորանարդ', font_size=70, tex_template=ARMTEX).shift(2.75 * DOWN)
        case_1.align_to(case_3, LEFT)
        case_2.align_to(case_3, LEFT)

        square = SVGMobject('objects/SVG_files/square').scale(0.5).next_to(case_2, buff=0.5)
        cube = SVGMobject('objects/SVG_files/cube').scale(0.58).next_to(case_3, buff=0.5)
        side_length_square = MathTex('a').next_to(square, RIGHT)
        side_length_cube = MathTex('a').next_to(cube, RIGHT).shift(0.1 * UP)

        surr_rect_base = SurroundingRectangle(product_a_n_hat[-2], buff=0.05, corner_radius=0.1).shift([-1, 2.5, 0])
        arrow_base = Arrow(color=YELLOW).rotate(-PI / 4)
        VGroup(arrow_base, arrow_base.tip).scale(0.75).next_to(surr_rect_base, DR, buff=0.15)
        base = Tex('Հիմք', tex_template=ARMTEX).next_to(arrow_base, DR, buff=0.15)

        surr_rect_exponent = SurroundingRectangle(product_a_n_hat[-1], buff=0.05, color=BLUE, corner_radius=0.1).shift([-1, 2.5, 0])
        arrow_exponent = Arrow(color=BLUE).rotate(PI / 8)
        VGroup(arrow_exponent, arrow_exponent.tip).scale(0.6).next_to(surr_rect_exponent, UR, buff=0.1)
        exponent_1 = Tex('Ցուցիչ,', tex_template=ARMTEX).next_to(arrow_exponent, RIGHT, buff=0.1).shift(0.25 * UP)
        exponent_2 = Tex('Աստիճանացույց', tex_template=ARMTEX).next_to(exponent_1, DOWN, buff=0.15, aligned_edge=LEFT)
        arrow_exponent.shift(0.1 * DOWN)

# ANIMATIONS
        self.play(Write(sum_a[0]))
        self.wait(0.5)
        self.play(Write(brace_sum), Write(quantity_sum))
        self.wait()
        self.play(Write(sum_a[1], run_time=0.75))
        self.wait(0.1)
        self.play(ReplacementTransform(quantity_sum.copy(), sum_a[2]))
        self.play(Write(sum_a[-2:]))
        self.wait()

        self.play(Write(product_a_5_hat[0:2]))
        self.wait(0.5)
        self.play(Write(brace_product_5), Write(quantity_product_5))
        self.wait()

        self.play(Write(product_a_5_hat[2]))
        self.play(Circumscribe(quantity_product_5, Circle, fade_out=True, run_time=2))
        self.wait()

        self.play(
            product_a_5_hat[-2].animate.shift(0.3 * RIGHT),
            quantity_product_5_copy.animate.next_to(product_a_5_hat[-3], RIGHT, buff=0.1)
        )
        self.wait()

        self.play(
            product_a_5_hat[-2].animate.shift(0.3 * LEFT),
            quantity_product_5_copy.animate.shift(0.65 * RIGHT)
        )
        self.wait()

        self.play(ReplacementTransform(quantity_product_5_copy, product_a_5_hat[-1]))
        self.wait()

        self.play(
            *[mob.animate.shift(5 * UP) for mob in [sum_a, brace_sum, quantity_sum]],
            *[mob.animate.shift(3.5 * UP) for mob in [product_a_5_hat, brace_product_5, quantity_product_5]]
        )
        self.wait()
        self.remove(sum_a, brace_sum, quantity_sum)

    # Write a•a•...•a = a^n
        self.play(Write(product_a_n_hat[0]))
        self.wait(0.1)
        self.play(Write(brace_product_n), Write(quantity_product_n))
        self.wait()
        self.play(Write(product_a_n_hat[1:]))
        self.wait()

        self.play(
            *[mob.animate.shift(4 * UP) for mob in [product_a_5_hat, brace_product_5, quantity_product_5]],
            *[mob.animate.shift(3.5 * UP) for mob in [product_a_n_hat, brace_product_n, quantity_product_n]]
        )
        self.remove(product_a_5_hat, brace_product_5, quantity_product_5)
        self.wait()

        self.play(Write(case_1))
        self.wait()
        self.play(Write(case_2))
        self.wait(0.5)
        self.play(FadeIn(square), Write(side_length_square))
        self.wait()

        self.play(Write(case_3))
        self.wait()
        self.play(FadeIn(cube), Write(side_length_cube))
        self.wait()

        self.play(
            FadeOut(square, cube, side_length_cube, side_length_square),
            case_2.animate.next_to(case_3, UP, buff=0.5, aligned_edge=LEFT),
            case_1.animate.next_to(case_3, UP, buff=1 + case_2.height, aligned_edge=LEFT),
            *[mob.animate.shift([-1, -1, 0]) for mob in [product_a_n_hat, brace_product_n, quantity_product_n]]
        )
        self.wait()

        self.play(Create(surr_rect_base))
        self.play(Create(arrow_base))
        self.play(Write(base))
        self.wait()

        self.play(Create(surr_rect_exponent))
        self.play(Create(arrow_exponent))
        self.play(Write(exponent_1))
        self.play(Write(exponent_2))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class FewNmanMiandamner(FormulaModificationsScene):
    def construct(self):

# INITS
        nman_en = Tex('Նման են', tex_template=ARMTEX)
        nmanner = VGroup(
            Tex('$4\cdot x^2\cdot y$'),
            Tex('$9\cdot x^2\cdot y$'),
            Tex('$4\cdot x\cdot y\cdot x$'),
            Tex('$x^2\cdot y$'),
        )
        nmanner.arrange(DOWN, buff=0.5, aligned_edge=RIGHT).shift(3 * LEFT)
        nman_en.next_to(nmanner, UP, buff=0.75)

        nman_chen = Tex('Նման միանդամներ չկան', tex_template=ARMTEX)
        chnmanner = VGroup(
            Tex('$2\cdot x^2\cdot y$'),
            Tex('$7\cdot x^2\cdot y^3$'),
            Tex('$2\cdot x^2\cdot y^2$'),
            Tex('$7\cdot x\cdot y^2$'),
        )
        chnmanner.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(3 * RIGHT)
        nman_chen.next_to(chnmanner, UP, buff=0.75)

# ANIMATIONS
        self.play(Write(nman_en))
        self.wait(0.1)
        self.play(FadeIn(nmanner))
        self.wait()

        self.play(Write(nman_chen))
        self.wait(0.1)
        self.play(FadeIn(chnmanner))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class PerfectFormExponent(FormulaModificationsScene):
    def construct(self):
        TwoSimpleExamples.construct(self)
        ThirdExample.construct(self)
        DefiningExponent.construct(self)
        FewNmanMiandamner.construct(self)
