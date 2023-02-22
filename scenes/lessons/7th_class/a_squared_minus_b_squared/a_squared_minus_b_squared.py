from manim import *
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from segment import ConnectionLine

def get_top_left(mob : Mobject):
    return np.array([mob.get_left()[0], mob.get_top()[1], 0])

def get_top_right(mob : Mobject):
    return np.array([mob.get_right()[0], mob.get_top()[1], 0])

def get_bottom_left(mob : Mobject):
    return np.array([mob.get_left()[0], mob.get_bottom()[1], 0])

def get_bottom_right(mob : Mobject):
    return np.array([mob.get_right()[0], mob.get_bottom()[1], 0])

class DrawASquaredMinusBSquared(Scene):
    def construct(self):

        a = 4.5 # length of the sides of the big square
        b = 1.75 # length of the sides of the small square

        # vertices of polygons
        ul = np.array([-a/2, a/2, 0])
        dl = np.array([-a/2, -a/2, 0])
        ur = np.array([a/2, a/2, 0])
        dr = np.array([a/2, -a/2, 0])
        dm = np.array([a/2-b, -a/2, 0])
        rm = np.array([a/2, -(a/2-b), 0])
        mm = np.array([a/2-b, -(a/2-b), 0])
        lm = np.array([-a/2, -(a/2-b), 0])
        um = np.array([a/2-b, a/2, 0])

        # square with side a
        square_a = Polygon(ul, dl, dr, ur, color=GREEN, fill_opacity=0.5)
        side_a_up = Tex('$a$', font_size=70).next_to(square_a, UP)
        side_a_left = Tex('$a$', font_size=70).next_to(square_a, LEFT)
        area_a = Tex('$a^2$', font_size=70).move_to(square_a)

        self.play(Create(square_a))
        self.wait(0.25)
        self.play(Write(side_a_left), Write(side_a_up))
        self.wait(0.5)
        self.play(Write(area_a))
        self.wait()

        # square with side b
        square_b = Polygon(rm, mm, dm, dr, color=ORANGE, fill_opacity=0.5)
        side_b_down = Tex('$b$', font_size=60).next_to(square_b, DOWN)
        side_b_right = Tex('$b$', font_size=60).next_to(square_b, RIGHT)
        area_b = Tex('$b^2$', font_size=70).move_to(square_b)

        self.play(Create(square_b))
        self.wait(0.25)
        self.play(Write(side_b_down), Write(side_b_right))
        self.wait(0.5)
        self.play(Write(area_b))
        self.wait()

        # polygon we get by subtracting a^2 and b^2
        difference_polygon = Polygon(ul, dl, dm, mm, rm, ur, color=GREEN, fill_opacity=0.5)
        area_polygon = Tex('$a^2$', '$-$', '$b^2$', font_size=70).move_to(square_a).shift([-0.5, 0.25, 0])

        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeIn(difference_polygon), FadeOut(square_a, square_b),
                    ReplacementTransform(area_a, area_polygon[:1]),
                    ReplacementTransform(area_b, area_polygon[2:3])
                ),
                Write(area_polygon[1]),
                lag_ratio=0.5
            )
        )
        self.wait()

        # brace sides of polygon with length a-b
        # right side
        brace_right = BraceBetweenPoints(ur, rm, RIGHT)
        side_a_minus_b_right = Tex('$a$$-$$b$', font_size=70)
        side_a_minus_b_right.next_to(brace_right, RIGHT)

        self.play(Write(brace_right))
        self.wait(0.25)
        self.play(Write(side_a_minus_b_right))
        self.wait()
        self.play(
            FadeOut(brace_right),
            side_a_minus_b_right.animate.shift(LEFT * 0.5)
        )
        self.wait()

        self.play(side_b_right.animate.shift([-b-0.1, -0.05, 0]))
        self.wait(0.25)

        # down side
        brace_down = BraceBetweenPoints(dl, dm, DOWN)
        side_a_minus_b_down = Tex('$a$$-$$b$', font_size=70)
        side_a_minus_b_down.next_to(brace_down, DOWN)

        self.play(Write(brace_down))
        self.wait(0.25)
        self.play(Write(side_a_minus_b_down))
        self.wait()
        self.play(
            FadeOut(brace_down),
            side_a_minus_b_down.animate.shift(UP * 0.5)
        )
        self.wait()

        self.play(side_b_down.animate.shift([0.05, b+0.1, 0]))
        self.wait()

        # write S = a^2-b^2 in top left corner
        s_equals_difference = Tex('$S$', ' $=$ ', '$a^2$', '$-$', '$b^2$', font_size=70)
        s_equals_difference.to_corner(UL).shift(0.25 * DOWN)

        self.play(Write(s_equals_difference[:2]))
        self.wait(0.1)
        self.play(ReplacementTransform(area_polygon[0:3], s_equals_difference[2:5]))
        self.wait()


        # divide polygon into a rectangle with sides (a-b)•a and a rectangle with sides (a-b)•b
        horizontal_dashed_line = DashedLine(mm, lm)

        self.play(Create(horizontal_dashed_line))
        self.wait()

        # replace polygon with 2 rectangles - (a-b)•a and (a-b)•b
        big_rectangle = Polygon(ur, ul, lm, rm, color=GREEN, fill_opacity=0.5)
        lines_of_bottom_rectangle = VGroup(
            Line(lm, dl, color=GREEN),
            Line(dl, dm, color=GREEN),
            Line(dm, mm, color=GREEN),
            horizontal_dashed_line
        )

        fill_of_bottom_rectangle = Polygon(mm, lm, dl, dm, color=GREEN, stroke_width=0, fill_opacity=0.5)

        bottom_rectangle = VGroup(fill_of_bottom_rectangle, lines_of_bottom_rectangle)
        bottom_rectangle_with_side_lengths = VGroup(bottom_rectangle, side_a_minus_b_down, side_b_right)

        self.remove(difference_polygon)
        self.add(big_rectangle, bottom_rectangle)

        # cut the bottom rectangle, move and stick to the big rectangle
        # in the end we will have a rectangle with sides a+b and a-b
        self.play(
            bottom_rectangle_with_side_lengths.animate(rate_func=linear).shift(DOWN * 0.75),
            FadeOut(side_a_left, side_b_down)
        )
        self.wait(0.5)
        self.play(bottom_rectangle_with_side_lengths.animate(rate_func=linear).shift(LEFT * 3.5))
        self.wait()
        self.play(bottom_rectangle_with_side_lengths.animate(rate_func=linear).align_to(big_rectangle, UP).shift((a/2-b) * DOWN))
        self.wait()

        self.play(
            Rotating(bottom_rectangle, radians=-PI/2, run_time=1),
            ClockwiseTransform(
                side_b_right,
                side_b_right.copy().move_to(bottom_rectangle).shift((a/2 - b/2 + 0.45) * DOWN),
                -PI/2, rate_func=linear
            ),
            ClockwiseTransform(
                side_a_minus_b_down,
                side_a_minus_b_down.copy().move_to(bottom_rectangle).shift((b/2 + 0.73) * LEFT),
                -PI/2, rate_func=linear
            )
        )
        self.wait()
        self.play(bottom_rectangle_with_side_lengths.animate(rate_func=linear).next_to(big_rectangle, LEFT, buff=0, aligned_edge=UP))
        self.wait()

        # remove dividing line from final rectangle and calculate the big side
        final_rectangle = Polygon(ur, ul + b * LEFT, lm + b * LEFT, rm, color=GREEN, fill_opacity=0.5)
        big_side = Tex('$a$', '$+$', '$b$', font_size=70).next_to(final_rectangle, UP, buff=0.2)
        small_side = side_a_minus_b_down

        self.play(
            FadeOut(bottom_rectangle, big_rectangle, side_a_minus_b_right),
            FadeIn(final_rectangle),
            ReplacementTransform(side_a_up, big_side[:1]),
            ReplacementTransform(side_b_right, big_side[2:]),
            Write(big_side[1])
        )
        self.wait()

        # write the area of final rectangle inside of it
        final_area = Tex('$($', '$a$', '$-$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$', font_size=70)
        final_area.move_to(final_rectangle)

        self.play(
            ReplacementTransform(big_side.copy(), final_area[6:9]),
            Write(final_area[0]),
            Write(final_area[4]),
            ReplacementTransform(small_side.copy(), final_area[1:4]),
            Write(final_area[5]),
            Write(final_area[9])
        )
        self.wait()

        # write S = (a+b)(a-b) and fadeout final rectangle
        s_equals_product = Tex('$S$', ' $=$ ', '$($', '$a$', '$-$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$', font_size=70)
        s_equals_product.next_to(s_equals_difference, DOWN, buff=0.75, aligned_edge=LEFT)

        self.play(
            *[mob.animate.shift(RIGHT * 3 + DOWN) for mob in[final_rectangle, big_side, small_side]],
            Write(s_equals_product[:2]),
            ReplacementTransform(final_area, s_equals_product[2:])
        )
        self.wait()
        self.play(FadeOut(final_rectangle, big_side, small_side))
        self.wait()
        self.remove(s_equals_difference, s_equals_product)


class CalculateASquaredMinusBSquared(FormulaModificationsScene):
    def construct(self):
        # add    S = a^2-b^2   and   S = (a+b)(a-b)    from previous scene
        s_equals_difference = Tex(
            '$S$', ' $=$ ', '$a^2$', '$-$', '$b^2$',
            ' $=$ ', '$($', '$a$', '$-$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$',
            font_size=70
        )
        s_equals_difference.to_corner(UL).shift(0.25 * DOWN)
        s_equals_product = Tex('$S$', ' $=$ ', '$($', '$a$', '$-$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$', font_size=70)
        s_equals_product.next_to(s_equals_difference[:5], DOWN, buff=0.75, aligned_edge=LEFT)
        self.add(s_equals_difference[:5], s_equals_product)

        # circumscribe left and right parts and show that a^2-b^2 = (a+b)(a-b)
        self.play(
            Circumscribe(s_equals_difference[0], fade_out=True, run_time=2),
            Circumscribe(s_equals_product[0], fade_out=True, run_time=2)
        )
        self.wait()
        self.play(
            Circumscribe(s_equals_difference[2:5], fade_out=True, run_time=2),
            Circumscribe(s_equals_product[2:], fade_out=True, run_time=2)
        )
        self.wait()

        self.play(
            ReplacementTransform(s_equals_product[1:], s_equals_difference[5:]),
            FadeOut(s_equals_product[0])
        )
        self.wait()

        final_formula = s_equals_difference
        self.play(
            ModifyFormula(final_formula, remove_items=[0, 1])
        )
        self.wait()

        # open parenthesis and confirm the result
        calculations = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$($', '$a$', '$+$', '$b$', '$)$', ' $=$ ', # 0:11
            '$a^2$', ' $+$ ', '$a$', '$b$', ' $-$' , '$b$', '$a$', ' $-$ ', '$b^2$', # 11:19
            font_size=70
        )
        calculations.to_edge(LEFT).shift(DOWN)

        self.play(ReplacementTransform(final_formula[4:].copy(), calculations[:10]))
        self.wait()
        self.play(Write(calculations[10]))
        self.wait()

        conn_line = ConnectionLine(calculations[1], calculations[6])
        self.play(Create(conn_line))
        self.wait()

        # write a^2
        self.play(
            ClockwiseTransform(calculations[1].copy(), calculations[11], remover=True),
            ClockwiseTransform(calculations[6].copy(), calculations[11], remover=True)
        )
        self.add(calculations[11])
        self.wait()

        # write +ab
        self.play(Transform(conn_line, ConnectionLine(calculations[1], calculations[8])))
        self.wait(0.25)
        self.play(
            Write(calculations[12]),
            ClockwiseTransform(calculations[1].copy(), calculations[13], remover=True),
            ClockwiseTransform(calculations[8].copy(), calculations[14], remover=True)
        )
        self.add(calculations[13:15])
        self.wait()
        
        # write -ba
        self.play(Transform(conn_line, ConnectionLine(calculations[3], calculations[6])))
        self.wait(0.25)
        self.play(
            Write(calculations[15]),
            ClockwiseTransform(calculations[3].copy(), calculations[16], remover=True),
            ClockwiseTransform(calculations[6].copy(), calculations[17], remover=True)
        )
        self.add(calculations[16:18])
        self.wait()

        # write -b^2
        self.play(Transform(conn_line, ConnectionLine(calculations[3], calculations[8])))
        self.wait(0.25)
        self.play(
            Write(calculations[18]),
            ClockwiseTransform(calculations[3].copy(), calculations[19], remover=True),
            ClockwiseTransform(calculations[8].copy(), calculations[19], remover=True)
        )
        self.add(calculations[19])
        self.wait()

        self.play(FadeOut(conn_line))
        self.wait()

        # +ab and -ab cancel out
        surr_rect = SurroundingRectangle(calculations[12:18])
        self.play(Create(surr_rect, rate_func=there_and_back_with_pause, run_time=2))
        self.wait()

        krchatman_gcikner = VGroup(
            Line(get_top_left(calculations[12:15]), get_bottom_right(calculations[12:15]), color=YELLOW),
            Line(get_top_left(calculations[15:18]), get_bottom_right(calculations[15:18]), color=YELLOW)
        )
        self.play(
            Create(krchatman_gcikner[0]),
            Create(krchatman_gcikner[1])
        )
        self.wait()

        self.play(
            FadeOut(krchatman_gcikner),
            ModifyFormula(calculations, remove_items=[12, 13, 14, 15, 16, 17], replace_items=[[18]], replace_items_strs=[['$-$']])
        )
        self.wait()


class ASquaredMinusBSquared(Scene):
    def construct(self):
        DrawASquaredMinusBSquared.construct(self)
        self.remove(*self.mobjects)
        CalculateASquaredMinusBSquared.construct(self)
