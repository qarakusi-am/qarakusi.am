from manim import *
from manim import LEFT, RIGHT, UP, DOWN, DR, UR, ORIGIN, PI
from manim import ORANGE, GREEN, WHITE
from manim import Square, Rectangle, Tex, VGroup
from manim import AnimationGroup, Write, Create, FadeOut, FadeIn
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from segment import ConnectionLine

class APlusBSquared(FormulaModificationsScene):

    def recap(self): # write 5^2=5•5 and a(b+c)=ab+ac
        tvi_qarakusi = Tex('$5^2=5\cdot 5$').scale(2).shift(UP)
        pakagceri_bacum = Tex('$a(b+c)=ab+ac$').scale(2).shift(DOWN)
        
        self.play(Write(tvi_qarakusi, run_time=2, rate_func=linear))
        self.wait()
        self.play(Write(pakagceri_bacum, run_time=2, rate_func=linear))
        self.wait()
        self.play(FadeOut(tvi_qarakusi, pakagceri_bacum))

    def misconception(self): # numerically check if (1+1)^2 = 1^2+1^2
        # 2(1+1) = 2•1 + 2•1
        equal_expressions = Tex('$2(1+1)$', ' $=$ ', '$2\cdot 1 + 2\cdot 1$')
        equal_expressions.set(font_size=60).shift(2 * UP)
        equal_expressions[0].shift(0.25 * LEFT)
        equal_expressions[2].shift(0.25 * RIGHT)

        self.play(Write(equal_expressions[0], run_time=1.5, rate_func=linear))
        self.wait(0.1)
        self.play(Write(equal_expressions[2], run_time=1.5, rate_func=linear))
        self.wait(1)
        self.play(Write(equal_expressions[1]))
        self.wait()

        # (1+1)^2 != 1^2 + 1^2
        not_equal_expressions = Tex('$(1+1)^2$ ', ' $\\not =$ ', ' $1^2+1^2$')
        not_equal_expressions.set(font_size=60).shift(0.45 * LEFT)
        not_equal_expressions[0].shift(0.25 * LEFT)
        not_equal_expressions[2].shift(0.25 * RIGHT)

        self.play(Write(not_equal_expressions[0]))
        self.wait(0.1)
        self.play(Write(not_equal_expressions[2]))
        self.wait()

        # left part - 2^2=4
        left_part = Tex('$2$', font_size=60)
        left_part.next_to(not_equal_expressions[0], DOWN).shift(0.2 * LEFT)
        surr_rect = SurroundingRectangle(not_equal_expressions[0][1:4], corner_radius=0.25)

        self.play(Create(surr_rect))
        self.wait(0.25)
        self.play(Write(left_part))
        self.wait()
        self.play(
            Transform(surr_rect, SurroundingRectangle(not_equal_expressions[0][-1], corner_radius=0.2)),
            ModifyFormula(left_part, add_after_items=[0], add_items_strs=[['$^2$']])
        )
        self.wait()
        self.play(
            ModifyFormula(left_part, replace_items=[[0, 1]], replace_items_strs=[['$4$']]),
            FadeOut(surr_rect)
        )
        self.wait()

        # right part - 1+1=2
        right_part = Tex('$1$', '$+1$', font_size=60)
        right_part.next_to(not_equal_expressions[2], DOWN)
        surr_rect.become(SurroundingRectangle(not_equal_expressions[2][:2], corner_radius=0.25))

        self.play(Create(surr_rect))
        self.wait(0.25)
        self.play(Write(right_part[0]))
        self.play(
            Transform(surr_rect, SurroundingRectangle(not_equal_expressions[2][3:], corner_radius=0.25)),
            Write(right_part[1])
        )
        self.wait(0.25)
        self.play(ModifyFormula(right_part, replace_items=[[0, 1]], replace_items_strs=[['$2$']], new_formula_alignment=ORIGIN))
        self.wait(0.25)
        self.play(FadeOut(surr_rect))
        self.wait(0.25)
        self.play(Write(not_equal_expressions[1]))
        self.wait(0.5)
        self.play(FadeOut(left_part, right_part))
        self.wait()
        self.play(FadeOut(equal_expressions, not_equal_expressions))
        self.wait()

    def get_formula_by_drawing(self): # draw squares and get the correct formula
        # (a+b)^2=(a+b)(a+b)
        a_plus_b_squared = Tex(
            '$($', '$a$', '$+$', '$b$', '$)$', '$^2$', ' $=$ ',
            '$($', '$a$', '$+$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$',
            font_size=60
        )

        self.play(Write(a_plus_b_squared[:6]))
        self.wait()
        self.play(Write(a_plus_b_squared[6]))
        self.wait()
        self.play(Write(a_plus_b_squared[7:], run_time=2))
        self.wait()
        self.play(a_plus_b_squared.animate.to_edge(UP))
        self.wait()

        # draw square with side (a+b)
        big_square = Square(3)
        big_square_sides = VGroup(
            Tex('$a+b$', font_size=30).next_to(big_square, UP, buff=0.15),
            Tex('$a+b$', font_size=30).rotate(PI/2).next_to(big_square, LEFT, buff=0.15)
        )
        big_square_area = Tex('$(a+b)^2$').move_to(big_square)
        
        self.play(
            AnimationGroup(
                Create(big_square),
                Write(big_square_sides),
                lag_ratio=0.5
            )
        )
        self.wait()
        self.play(
            big_square.animate.set_fill([ORANGE, GREEN], 1),
            Write(big_square_area)
        )
        self.wait()

        # divide big square into 4 small squares
        sq_copy = VGroup(big_square, big_square_sides).copy()
        equality_sign = Tex('$=$', font_size=80)

        self.add(sq_copy, big_square_area)
        self.play(
            *[mob.animate.shift(3 * LEFT) for mob in [big_square, big_square_area, big_square_sides]],
            sq_copy.animate.shift(3 * RIGHT)
        )
        self.play(Write(equality_sign))
        self.wait()

        divided_sides = VGroup(
            Tex('$a$', font_size=30).next_to(sq_copy[0], UP, 0.15, LEFT).shift(0.5 * RIGHT),
            Tex('$b$', font_size=30).next_to(sq_copy[0], UP, 0.15, RIGHT).shift(0.75 * LEFT),
            Tex('$a$', font_size=30).next_to(sq_copy[0], LEFT, 0.15, UP).shift(0.5 * DOWN),
            Tex('$b$', font_size=30).next_to(sq_copy[0], LEFT, 0.15, DOWN).shift(0.75 * UP)
        )

        square_a = Square(1.25).set_fill(GREEN, 1)
        square_b = Square(1.75).next_to(square_a, DR, buff=0).set_fill(ORANGE, 1)
        rect_up = Rectangle(WHITE, 1.25, 1.75).next_to(square_a, RIGHT, buff=0).set_fill(YELLOW_D, 1)
        rect_down = Rectangle(WHITE, 1.75, 1.25).next_to(square_a, DOWN, buff=0).set_fill(YELLOW_D, 1)
        small_squares = VGroup(square_a, square_b, rect_up, rect_down)
        small_squares.move_to(sq_copy[0])

        self.play(
            FadeIn(small_squares),
            ReplacementTransform(sq_copy[1][0][0][0], divided_sides[0]),
            FadeOut(sq_copy[1][0][0][1]),
            ReplacementTransform(sq_copy[1][0][0][2], divided_sides[1]),
            ReplacementTransform(sq_copy[1][1][0][0], divided_sides[2]),
            FadeOut(sq_copy[1][1][0][1]),
            ReplacementTransform(sq_copy[1][1][0][2], divided_sides[3]),
            FadeOut(sq_copy[0])
        )
        self.wait()

        # write areas of each rect inside of it
        divided_areas = VGroup(
            Tex('$a^2$').move_to(square_a).shift(UR * 0.05),
            Tex('$b^2$').move_to(square_b).shift(UR * 0.075),
            Tex('$ab$').move_to(rect_up.get_center()),
            Tex('$ab$').move_to(rect_down.get_center())
        )

        self.play(
            AnimationGroup(
                AnimationGroup(*[mob.animate(rate_func=there_and_back_with_pause, run_time=3).set_opacity(0.2) for mob in [square_b, rect_down, rect_up]]),
                Write(divided_areas[0]),
                lag_ratio=1/3
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                AnimationGroup(*[mob.animate(rate_func=there_and_back_with_pause, run_time=3).set_opacity(0.2) for mob in [square_a, rect_down, rect_up, divided_areas[0]]]),
                Write(divided_areas[1]),
                lag_ratio=1/3
            )
        )
        self.wait()

        self.play(*[mob.animate.set_opacity(0.1) for mob in [square_a, square_b, divided_areas[0:2]]])
        self.wait()
        self.add(rect_down)
        self.play(Rotating(rect_down, about_point=square_a.get_center(), radians=PI/2, run_time=3, rate_func=there_and_back_with_pause))
        self.wait(0.25)
        self.play(
            Write(divided_areas[2]),
            Write(divided_areas[3])
        )
        self.wait(0.5)
        self.play(*[mob.animate.set_opacity(1) for mob in [square_a, square_b, divided_areas[0:2]]])

        # transform areas into formula
        correct_formula = Tex('$(a+b)^2$', ' $=$ ', '$a^2$', ' $+$ ', '$2ab$', ' $+$ ', '$b^2$', font_size=60)
        correct_formula.shift(3 * DOWN + 0.9 * RIGHT)

        self.play(Indicate(big_square_area, 1.75, run_time=0.75))
        self.wait(0.1)
        self.play(TransformFromCopy(big_square_area, correct_formula[:1]))
        self.wait(0.25)
        self.play(Write(correct_formula[1], run_time=0.5, rate_func=linear))
        self.wait()
        self.play(Indicate(divided_areas[0], 1.75, run_time=0.75))
        self.wait(0.1)
        self.play(TransformFromCopy(divided_areas[0], correct_formula[2]))
        self.wait(0.25)
        self.play(Write(correct_formula[3], run_time=0.5, rate_func=linear))
        self.wait(0.5)
        self.play(
            Indicate(divided_areas[2], 1.75, run_time=0.75),
            Indicate(divided_areas[3], 1.75, run_time=0.75)
        )
        self.wait(0.1)
        self.play(TransformFromCopy(divided_areas[2:4], correct_formula[4]))
        self.wait(0.25)
        self.play(Write(correct_formula[5], run_time=0.5, rate_func=linear))
        self.wait(0.5)
        self.play(Indicate(divided_areas[1], 1.75, run_time=0.75))
        self.wait(0.25)
        self.play(TransformFromCopy(divided_areas[1], correct_formula[6]))
        self.wait()

        self.play(Indicate(a_plus_b_squared))
        self.wait()
        self.play(
            FadeOut(
                small_squares, divided_areas, divided_sides, correct_formula,
                big_square, big_square_area, big_square_sides, equality_sign
            ),
            a_plus_b_squared.animate.move_to(ORIGIN).to_edge(LEFT)
        )
        self.wait()
        self.remove(a_plus_b_squared)

    def get_formula_by_multiplying(self): # get formula by opening parenthesis (a+b)(a+b)
        # (a+b)^2=(a+b)(a+b)
        formula = Tex(
            '$($', '$a$', '$+$', '$b$', '$)$', '$^2$', ' $=$ ', # 0:7
            '$($', '$a$', '$+$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$', # 7:17
            ' $=$ ', '$a$', '$\cdot$', '$a$', '$+$', '$a$', '$\cdot$', '$b$', # 17:24
            '$+$', '$b$', '$\cdot$', '$a$', '$+$', '$b$', '$\cdot$', '$b$', # 24:32
            font_size=60
        )
        formula.to_edge(LEFT)
        self.add(formula[:17])
        self.play(Write(formula[17]))
        self.wait()

        # open parenthesis and write   = a•a+a•b+b•a+b•b
        conn_line = ConnectionLine(formula[8], formula[13], alpha=0.25)
        self.play(Create(conn_line))
        self.wait(0.5)
        self.play(
            ClockwiseTransform(formula[8].copy(), formula[18], remover=True, radius=10),
            Write(formula[19]),
            ClockwiseTransform(formula[13].copy(), formula[20], remover=True)
        )
        self.add(formula[18:21])
        self.wait()

        self.play(
            Transform(conn_line, ConnectionLine(formula[8], formula[15], alpha=0.25)),
            Write(formula[21]),
            run_time=0.75
        )
        self.wait(0.5)
        self.play(
            ClockwiseTransform(formula[8].copy(), formula[22], remover=True),
            Write(formula[23]),
            ClockwiseTransform(formula[15].copy(), formula[24], remover=True)
        )
        self.add(formula[21:25])
        self.wait(0.5)

        self.play(
            Transform(conn_line, ConnectionLine(formula[10], formula[13], alpha=0.25)),
            Write(formula[25]),
            run_time=0.75
        )
        self.wait(0.5)
        self.play(
            ClockwiseTransform(formula[10].copy(), formula[26], remover=True, radius=0.1),
            Write(formula[27]),
            ClockwiseTransform(formula[13].copy(), formula[28], remover=True)
        )
        self.add(formula[25:29])
        self.wait(0.5)

        self.play(
            Transform(conn_line, ConnectionLine(formula[10], formula[15], alpha=0.25)),
            Write(formula[29]),
            run_time=0.75
        )
        self.wait(0.5)
        self.play(
            ClockwiseTransform(formula[10].copy(), formula[30], remover=True, radius=0.1),
            Write(formula[31]),
            ClockwiseTransform(formula[15].copy(), formula[32], remover=True)
        )
        self.add(formula[29:])
        self.wait()
        self.play(FadeOut(conn_line))
        self.wait()

        # simplify formula
        self.fix_formula(formula)
        self.play(
            ModifyFormula(
                formula,
                replace_items=[[18, 19, 20]], replace_items_strs=[['$a$', '$^2$']]
            )
        ) # a^2+a•b+b•a+b•b
        self.wait(0.5)
        self.play(
            ModifyFormula(
                formula,
                replace_items=[[21, 22, 23, 24, 25, 26, 27]], replace_items_strs=[['$2$', '$a$', '$b$']]
            )
        ) # a^2+2ab+b•b
        self.wait(0.5)
        self.play(
            ModifyFormula(
                formula,
                replace_items=[[25, 26, 27]], replace_items_strs=[['$b$', '$^2$']]
            )
        ) # a^2+2ab+b^2
        self.wait(0.5)
        self.play(
            ModifyFormula(
                formula, remove_items=[*range(7, 18)], new_formula_alignment=ORIGIN
            )
        ) # (a+b)^2 = a^2+2ab+b^2
        self.wait()

        # read formula
        self.play(
            AnimationGroup(
                Circumscribe(formula[1:4], Circle, fade_out=True, run_time=2),
                Circumscribe(formula[5], Circle, fade_out=True),
                lag_ratio=0.5
            )
        )
        self.wait(0.5)
        self.play(Indicate(formula[7:9], 1.5))
        self.wait(0.5)
        self.play(Indicate(formula[10:13], 1.5))
        self.wait(0.5)
        self.play(Indicate(formula[14:], 1.5))
        self.wait()

        self.play(formula.animate.to_corner(UR))
        surr_rect = SurroundingRectangle(formula, GREEN)
        self.play(Create(surr_rect))
        self.wait()
        self.formula = formula
        self.formula_rect = surr_rect

    def first_exercise(self): # (c+yz)^2 = x^2 + 2cyz + y^2z^2
        self.exercise_1 = exercise = Tex('1) ',
            '$($', '$c$', '$+$', '$yz$', '$)$', '$^2$', ' $=$ ',
            '$c$', '$^2$', '$+$', '$2$', '$c$', '$y$', '$z$', '$+$', '$y$', '$^2$', '$z$', '$^2$',
            font_size=60
        ) # 1) (c+yz)^2 = c^2+2cyz+y^2z^2
        exercise.to_edge(LEFT).shift(UP * 1.5)
        self.play(Write(exercise[:7]))
        self.wait()

        formula_copy = self.formula.copy() # (a+b)^2 = a^2+2ab+b^2
        self.play(formula_copy.animate.next_to(exercise[1:], DOWN, aligned_edge=LEFT))
        self.fix_formula(formula_copy)
        self.wait()
        
        # replace a with c
        self.play(
            *[formula_copy[i].animate.scale(1.5).set_color(ORANGE) for i in [1, 7, 11]],
            run_time=0.75
        )
        self.wait(0.1)
        self.play(exercise[2].animate.scale(1.5).set_color(ORANGE))
        self.wait(0.5)
        self.play(
            ModifyFormula(
                formula_copy,
                replace_items=[[1], [7], [11]], replace_items_strs=[['$c$']]*3
            ),
            exercise[2].animate.scale(1/1.5)
        ) # (c+b)^2 = c^2+2cb+b^2
        self.wait()

        # replace b with yz
        self.play(
            *[formula_copy[i].animate.scale(1.5).set_color(GREEN) for i in [3, 12, 14]],
            run_time=0.75
        )
        self.wait(0.1)
        self.play(exercise[4].animate.scale(1.5).set_color(GREEN))
        self.wait(0.5)
        self.play(
            ModifyFormula(
                formula_copy,
                replace_items=[[3], [12], [14]],
                replace_items_strs=[['$y$', '$z$'], ['$y$', '$z$'], ['$($', '$y$', '$z$', '$)$']],
                replace_items_colors=[[], [], [WHITE, GREEN, GREEN, WHITE]]
            ),
            exercise[4].animate.scale(1/1.5)
        ) # (c+yz)^2 = c^2+2cyz+(yz)^2
        self.wait()

        # (yz)^2=y^2z^2
        self.play(Indicate(formula_copy[16:]))
        self.wait()
        self.play(
            ModifyFormula(
                formula_copy,
                remove_items=[16, 19],
                add_after_items=[17], add_items_strs=[['$^2$']]
            )
        ) # (c+yz)^2 = c^2+2cyz+y^2z^2
        self.wait()

        # finish exercise
        self.play(
            FadeOut(formula_copy[:7]),
            ReplacementTransform(formula_copy[7:], exercise[7:]),
            exercise[:7].animate.set_color(WHITE)
        )
        self.wait()

    def second_exercise(self): # (3x+d)^2 = 9x^2 + 6xd + d^2
        self.exercise_2 = exercise = Tex('2) ',
            '$($', '$3$', '$x$', '$+$', '$d$', '$)$', '$^2$', ' $=$ ',
            '$($', '$3$', '$x$', '$)$', '$^2$', '$+$', '$2$', '$\cdot$', '$3$', '$x$', '$\cdot$', '$d$', '$+$', '$d$', '$^2$',
            font_size=60
        ) # 1) (3x+d)^2 = (3x)^2+2•3xd+d^2
        exercise.to_edge(LEFT).shift(DOWN)

        # write 1) (3x+d)^2
        self.play(Write(exercise[:8]))
        self.wait()
        self.play(Write(exercise[8], run_time=0.75))
        self.wait(0.1)

        # Indicate and write   = (3x)^2+2•3xd+d^2
        self.play(Indicate(exercise[2:4]))
        self.wait(0.5)
        self.play(Write(exercise[9:14]))
        self.wait(0.5)
        self.play(Write(exercise[14]))
        self.wait(0.5)
        self.play(Write(exercise[15:21]))
        self.wait()
        self.play(Indicate(exercise[5]))
        self.wait(0.5)
        self.play(Write(exercise[21:]))
        self.wait()

        # write polynomial in perfect form
        self.fix_formula(exercise)
        self.play(
            ModifyFormula(
                exercise,
                remove_items=[9, 12],
                replace_items=[[10]], replace_items_strs=[['$9$']]
            )
        ) # 9x^2+2•3xd+d^2
        self.wait(0.25)

        self.play(
            ModifyFormula(
                exercise,
                remove_items=[17],
                replace_items=[[13, 14, 15]], replace_items_strs=[['$6$']]
            )
        ) # 9x^2+6xd+d^2
        self.wait()

    def last_exercise(self): # (4+5k)^2 = ?
        self.play(FadeOut(self.exercise_1, self.exercise_2))
        self.wait(0.25)

        exercise = Tex('$(4+5k)^2$', font_size=80)
        self.play(Write(exercise))
        self.wait()

    def construct(self):
        self.recap()
        self.misconception()
        self.get_formula_by_drawing()
        self.get_formula_by_multiplying()
        self.first_exercise()
        self.second_exercise()
        self.last_exercise()
