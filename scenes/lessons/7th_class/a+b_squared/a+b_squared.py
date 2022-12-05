from manim import *
from manim import LEFT, RIGHT, UP, DOWN, DR, DL, UR, UL, ORIGIN, PI
from manim import ORANGE, GREEN, WHITE, YELLOW
from manim import Square, Rectangle, Tex, VGroup
from manim import AnimationGroup, Write, Create, FadeOut, FadeIn
from hanrahashiv import FormulaModificationsScene, ModifyFormula

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
            '$(a$', '$+$', '$b$', '$)$', '$(a$', '$+$', '$b$', '$)$',
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

    def get_formula_by_multiplying(self):
        formula = Tex(
            '$($', '$a$', '$+$', '$b$', '$)$', '$^2$', ' $=$ ',
            '$(a$', '$+$', '$b$', '$)$', '$(a$', '$+$', '$b$', '$)$',
            font_size=60
        )
        formula.to_edge(LEFT)
        self.add(formula)
        self.fix_formula(formula)

    def construct(self):
        self.recap()
        self.misconception()
        self.get_formula_by_drawing()
        self.get_formula_by_multiplying()
