from manim import *
from hanrahashiv import *

from constants import ARMTEX, ENGTEX
from objects import SimpleSVGMobject


# INITS FOR EVERY CLASS EXCEPT ThrowingBalls

property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UL, buff=0.15)
property_1.shift(0.1 * RIGHT)

property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, RIGHT, 0, UP)
property_2.shift(0.1 * RIGHT)

property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, RIGHT, 0, UP)
property_3.shift(0.1 * RIGHT)


# FUNCTIONS AND INITS FOR ThrowingBalls

def height_updater(starting_point = ORIGIN, acceleration=9.8, up_scale = 1):
    def height_evolution(mob : Mobject, dt):
        mob.speed = mob.speed - acceleration * dt
        mob.shift(UP * mob.speed * dt * up_scale)

        if mob.get_center()[1] < starting_point[1] - mob.speed * dt * 0.1 and mob.speed < 0:
            mob.clear_updaters()
            mob.move_to(starting_point)

    return height_evolution


def height_tex_updater(ball): # , height : ValueTracker
    def tex_next_to(mob : Mobject):
        mob.next_to(ball) #.become(DecimalNumber(height.get_value(), 1))

        if ball.speed < 0:
            mob.clear_updaters()
    return tex_next_to


speed_scale = 0.75
up_scale = 2/9
ball_height = SimpleSVGMobject('tennis_ball').scale(0.5).height
bottom_line_y = -3
bottom_line = Line([-10, bottom_line_y, 0], [10, bottom_line_y, 0])
ball_y = bottom_line_y + ball_height / 2
def setup_ball(center_coord=ORIGIN, speed=1, arrow_scale=1, acceleration=9.8):

    ball = SimpleSVGMobject('tennis_ball').scale(0.5).move_to(center_coord)
    arrow = Arrow().rotate(PI / 2).scale(arrow_scale, True).next_to(ball.get_center(), UP, buff=0)

    height = ValueTracker(0)
    height_tex = always_redraw(lambda: DecimalNumber(height.get_value(), 1))
    meter = Tex('մ', tex_template=ARMTEX)
    height_tex.add_updater(height_tex_updater(ball))
    meter.add_updater(lambda mob: mob.become(mob.next_to(height_tex, buff=0.15)))
    v = Tex('$V$ = ' + str(speed) + ' մ/վ', tex_template=ARMTEX).next_to(ball, DOWN)
    ball_run_time = speed * speed_scale / acceleration * 2

    return ball, arrow, height, height_tex, meter, v, ball_run_time

class ThrowingBalls(Scene):
    def construct(self):
    
    # INITIAL BALL
        ball_0, arrow_0, height_0, height_tex_0, meter_0, v_0, ball_run_time_0 = setup_ball([-4, ball_y, 0], 15, 0.65)
        ball_0.speed = 15 * speed_scale

    # FIRST BALL
        ball_1, arrow_1, height_1, height_tex_1, meter_1, v_1, ball_run_time_1 = setup_ball([-4, ball_y, 0], 20, 0.65)
        ball_1.speed = 20 * speed_scale

    # SECOND BALL
        ball_2, arrow_2, height_2, height_tex_2, meter_2, v_2, ball_run_time_2 = setup_ball([0, ball_y, 0], 25, 0.9)
        ball_2.speed = 25  * speed_scale

    # THIRD BALL
        ball_3, arrow_3, height_3, height_tex_3, meter_3, v_3, ball_run_time_3 = setup_ball([4, ball_y, 0], 30, 1.2)
        ball_3.speed = 30  * speed_scale

    # EARTH
        ball_earth, arrow_earth, height_earth, height_tex_earth, meter_earth, v_earth, ball_run_time_earth = setup_ball([-4, ball_y, 0], 20, 0.65)
        ball_earth.speed = 20 * speed_scale
        tex_earth = Tex('Երկիր', tex_template=ARMTEX).move_to(v_earth)
        v_earth = Tex('$V$', font_size=60).next_to(ball_earth)
        formula_earth = Tex('$\\frac{V^2}{19.6}$', font_size=80).align_to(ball_earth, LEFT).to_edge(UP, buff=3.5).shift(1.75 * LEFT)
    
    # MARS
        ball_mars, arrow_mars, height_mars, height_tex_mars, meter_mars, v_mars, ball_run_time_mars = setup_ball([0, ball_y, 0], 20, 0.65, 6)
        ball_mars.speed = 20  * speed_scale
        tex_mars = Tex('Մարս', tex_template=ARMTEX).move_to(v_mars)
        v_mars = Tex('$V$', font_size=60).next_to(ball_mars)
        formula_mars = Tex('$\\frac{V^2}{7.4}$', font_size=80).align_to(ball_mars, LEFT).to_edge(UP, buff=2).shift(1.75 * LEFT)

    # MOON
        ball_moon, arrow_moon, height_moon, height_tex_moon, meter_moon, v_moon, ball_run_time_moon = setup_ball([4, ball_y, 0], 20, 0.65, 3)
        ball_moon.speed = 20  * speed_scale
        tex_moon = Tex('Լուսին', tex_template=ARMTEX).move_to(v_moon)
        v_moon = Tex('$V$', font_size=60).next_to(ball_moon)
        formula_moon = Tex('$\\frac{V^2}{3.2}$', font_size=80).align_to(ball_moon, LEFT).to_edge(UP, buff=0.5).shift(1.75 * LEFT)
        ball_moon_copy = ball_moon.copy()


    # Animations
        self.play(FadeIn(bottom_line, ball_0))
        self.wait(0.5)
        self.play(Create(arrow_0))
        self.wait()

    # just throwing without any numbers
        ball_0.add_updater(height_updater(starting_point=[-4, bottom_line_y + ball_1.height / 2, 0], acceleration=9.8, up_scale=1/2))
        self.play(FadeOut(arrow_0))
        self.wait(4)

        self.remove(ball_0)
        self.add(ball_1)

    # throwing first ball with 20 m/s
        self.play(Create(arrow_1))
        self.wait()
        self.play(Write(height_tex_1), Write(v_1), Write(meter_1))
        ball_1.add_updater(height_updater(starting_point=[-4, ball_y, 0], acceleration=9.8, up_scale=up_scale))
        self.play(
            height_1.animate(run_time=ball_run_time_1/2).set_value(20.4),
            FadeOut(arrow_1)
        )
        gcik_1 = DashedLine(dash_length=0.3, dashed_ratio=0.5).scale(0.2).next_to(height_tex_1, LEFT, buff=0.1)
        self.play(Create(gcik_1))
        self.wait(ball_run_time_1/2 - 1)
        self.wait(0.2)
        self.play(FadeIn(arrow_1, run_time=0.6))
        self.wait(0.2)

    # throwing second ball with 25 m/s
        self.play(FadeIn(ball_2))
        self.play(Write(height_tex_2), Write(v_2), Write(meter_2), Create(arrow_2))
        ball_2.add_updater(height_updater(starting_point=[0, ball_y, 0], acceleration=9.8, up_scale=up_scale))
        self.play(
            height_2.animate(run_time=ball_run_time_2/2).set_value(31.8),
            FadeOut(arrow_2)
        )
        gcik_2 = DashedLine(dash_length=0.3, dashed_ratio=0.5).scale(0.2).next_to(height_tex_2, LEFT, buff=0.1)
        self.play(Create(gcik_2))
        self.wait(ball_run_time_2/2 - 1)
        self.wait(0.2)
        self.play(FadeIn(arrow_2, run_time=0.6))
        self.wait(0.2)

    # throwing third ball with 30 m/s
        self.play(FadeIn(ball_3))
        self.play(Write(height_tex_3), Write(v_3), Write(meter_3), Create(arrow_3))
        ball_3.add_updater(height_updater(starting_point=[4, ball_y, 0], acceleration=9.8, up_scale=up_scale))
        self.play(
            height_3.animate(run_time=ball_run_time_2/2).set_value(45.9),
            FadeOut(arrow_3)
        )
        gcik_3 = DashedLine(dash_length=0.3, dashed_ratio=0.5).scale(0.2).next_to(height_tex_3, LEFT, buff=0.1)
        self.play(Create(gcik_3))
        self.wait(ball_run_time_3/2 - 1)
        self.wait(0.2)
        self.play(FadeIn(arrow_3, run_time=0.6))
        self.wait(0.2)
    
    # erase old numbers and write formula v^2/19.8
        [mob.clear_updaters() for mob in [height_tex_1, height_tex_2, height_tex_3, meter_1, meter_2, meter_3]]
        self.play(
            FadeOut(
                height_tex_1, height_tex_2, height_tex_3, meter_1, meter_2, 
                meter_3, v_1, v_2, v_3, arrow_1, arrow_2, arrow_3, ball_2, ball_3,
                gcik_1, gcik_2, gcik_3
            )
        )
        self.wait()

        self.remove(ball_1)
        self.add(ball_earth)
    
    # animations earth
        self.play(Write(formula_earth))
        self.wait()
        self.play(Write(v_earth), Create(arrow_earth))
        self.wait(0.25)
        ball_earth.add_updater(height_updater(starting_point=[-4, ball_y, 0], acceleration=9.8, up_scale=up_scale))
        self.play(FadeOut(arrow_earth))
        self.wait(ball_run_time_earth - 1)
        self.play(
            Write(tex_earth),
            FadeIn(arrow_earth, run_time=0.6)
        )
        self.wait()

    # animations for mars
        self.play(FadeIn(ball_mars), Write(tex_mars), Create(arrow_mars), Write(v_mars))
        self.wait()
        self.play(Write(formula_mars))
        self.wait(0.25)
        ball_mars.add_updater(height_updater(starting_point=[0, ball_y, 0], acceleration=6, up_scale=up_scale))
        self.play(FadeOut(arrow_mars))
        self.wait(ball_run_time_mars - 1)
        self.wait(0.2)
        self.play(FadeIn(arrow_mars, run_time=0.6))
        self.wait(0.2)

    # animations for moon
        self.play(FadeIn(ball_moon), Write(tex_moon), Create(arrow_moon), Write(v_moon))
        self.wait(0.25)
        self.play(Write(formula_moon))
        ball_moon.add_updater(height_updater(starting_point=[0, ball_y, 0], acceleration=3, up_scale=up_scale))
        self.play(FadeOut(arrow_moon))
        self.wait(ball_run_time_moon - 1)
        self.add(ball_moon_copy)
        self.wait(0.5)
        self.play(FadeIn(arrow_moon))
        self.wait(0.5)
        

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()



class FirstProperty(FormulaModificationsScene):
    def construct(self):

    # write formula_1   2^4 • 2^5
        formula_1 = Tex(
            '$2$', '$^4$', ' $\cdot$ ', '$2$', '$^5$', ' $=$ ', # 0-5
            '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', ' $\cdot$ ', # 6-13
            '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', # 14-22
            font_size=60
        ) # 2^4 • 2^5 = 2•2•2•2 • 2•2•2•2•2 = 2^{4+5} = 2^9
        formula_1.shift(LEFT * 1.5)

        self.play(Write(formula_1[:2]))
        self.wait(0.1)
        self.play(Write(formula_1[2]))
        self.wait(0.1)
        self.play(Write(formula_1[3:5]))
        self.wait()

    # write definition of exponent
        definition_of_power = Tex('$a \cdot a \cdot a \cdot ... \cdot a \cdot a$', '$=$', '$a$', '$^n$', font_size=70)
        definition_of_power.to_edge(UP)
        brace_product_n = Brace(definition_of_power[0], DOWN)
        quantity_product_n = Tex('$n$', font_size=70).next_to(brace_product_n, DOWN)

        self.play(
            Write(definition_of_power),
            Write(brace_product_n),
            Write(quantity_product_n)
        )
        self.wait()

    # extract copy of 2^4 in the line below into 2•2•2•2 and brace under it
        formula_1_down  = Tex(
            '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', ' $\cdot$ ',
            '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$', '$\cdot$', '$2$',
            font_size=60
        ) # 2•2•2•2 • 2•2•2•2•2
        formula_1_down.next_to(formula_1, DOWN, buff=0.75, aligned_edge=LEFT)
        self.wait()

        self.play(Circumscribe(formula_1[:2], fade_out=True, run_time=1.5))
        self.wait()

        self.play(ReplacementTransform(formula_1[:2].copy(), formula_1_down[:7]))
        self.wait(0.25)

    # brace and write 4
        brace_4 = Brace(formula_1_down[:7], DOWN)
        brace_4_tex = Tex('$4$').next_to(brace_4, DOWN)

        self.play(Write(brace_4), Write(brace_4_tex))
        self.wait()

    # extract 2^5 into 2•2•2•2•2 and brace under it
        self.play(Circumscribe(formula_1[3:5], fade_out=True, run_time=1.5))
        self.wait()

        self.play(
            ReplacementTransform(formula_1[3:5].copy(), formula_1_down[8:]),
            Write(formula_1_down[7])
        )
        self.wait(0.25)

    # brace and write 5
        brace_5 = Brace(formula_1_down[8:], DOWN)
        brace_5_tex = Tex('$5$').next_to(brace_5, DOWN)

        self.play(Write(brace_5), Write(brace_5_tex))
        self.wait()
    
    # move formula_1_down to formula_1
        self.play(
            ReplacementTransform(formula_1_down, formula_1[6:23]),
            Write(formula_1[5]),
            brace_4.animate.next_to(formula_1[6:13], DOWN),
            brace_4_tex.animate.next_to(formula_1[6:13], DOWN, buff=0.75),
            brace_5.animate.next_to(formula_1[14:23], DOWN),
            brace_5_tex.animate.next_to(formula_1[14:23], DOWN, buff=0.75)
        )
        self.wait()

    # remove spaces form formula
        self.play(
            ReplaceItemsInFormula(formula_1, [13], ['\cdot']),
            brace_5_tex.animate.shift(LEFT * 0.41),
            brace_5.animate.shift(LEFT * 0.41),
        )# 2•2•2•2•2•2•2•2•2
        self.wait()
    
    # combine 4 and 5, write 4+5=9
        brace_9 = Brace(formula_1[6:23], DOWN)
        brace_9_tex = Tex('$4$', '$+$', '$5$', '$=$', '$9$').next_to(brace_9, DOWN)

        self.play(
            ReplacementTransform(brace_4_tex, brace_9_tex[0]),
            ReplacementTransform(brace_5_tex, brace_9_tex[2]),
            Write(brace_9_tex[1])
        )
        self.wait(0.1)
        self.play(Write(brace_9_tex[3:]))
        self.wait()
    
    # write = 2^{4+5} = 2^9
        formula_2 = Tex(
            ' $=$ ', '$2$', '$^4$', '$^+$', '$^5$', ' $=$ ', '$2$', '$^9$',
            font_size=60
        ) # = 2^{4+5}=2^9
        formula_2.next_to(formula_1, RIGHT)

        self.play(Write(formula_2, run_time=2))
        self.wait()

    # transform everything to 4+6=10 in exponents
        self.replace_items_in_formula(formula_1, [4], ['$^6$'])
        self.wait(0.25)

        self.play(
            AddItemsInFormula(formula_1, [len(formula_1) - 1], ['$\cdot 2$']),
            brace_5.animate.stretch(1.25, 0).shift(0.3 * RIGHT),
            ReplaceItemsInFormula(brace_9_tex, [2, 4], ['6', '10']),
            formula_2.animate.shift(0.4 * RIGHT)
        )
        self.wait(0.25)

        self.replace_items_in_formula(formula_2, [4, 7], ['^6', '^{10}'])
        self.wait()

        self.play(*[mob.animate.shift(UP) for mob in [formula_1, formula_2, brace_4, brace_5, brace_9_tex]])
        self.wait()
    
    # same property for m and n
        formula_m_n = Tex(
            '$a$', '$^m$', ' $\cdot$ ', '$a$', '$^n$', '$=$',
            '$a\cdot$$a\cdot$$...$$\cdot$$a$', ' $\cdot$ ', '$a\cdot$$a\cdot$$...$$\cdot$$a$',
            ' $=$ ', '$a$', '$^m$', '$^+$', '$^n$',
            font_size=70
        ).shift([0, -1.5, 0])

        brace_m = Brace(formula_m_n[6], DOWN)
        brace_m_tex = Tex('$m$').next_to(brace_m, DOWN)

        brace_n = Brace(formula_m_n[8], DOWN)
        brace_n_tex = Tex('$n$').next_to(brace_n, DOWN)

        [mob.set_color(GREEN) for mob in [formula_m_n[1], formula_m_n[11], brace_m_tex]] # , formula_m_n[6]
        [mob.set_color(ORANGE) for mob in [formula_m_n[4], formula_m_n[13], brace_n_tex]] # , formula_m_n[8]

        self.play(Write(formula_m_n[:5]))
        self.wait(0.25)
        self.play(Write(formula_m_n[5]))
        self.wait(0.25)
        self.play(Write(formula_m_n[6]))
        self.wait(0.25)
        self.play(Write(brace_m), Write(brace_m_tex))
        self.wait(0.25)
        self.play(Write(formula_m_n[7]))
        self.wait(0.25)
        self.play(Write(formula_m_n[8]))
        self.wait(0.25)
        self.play(Write(brace_n), Write(brace_n_tex))
        self.wait(0.25)
        self.play(Write(formula_m_n[9:]))
        self.wait()

        self.play(
            FadeOut(
                formula_1, definition_of_power, brace_product_n, brace_5, 
                brace_4, brace_9_tex, quantity_product_n, formula_2
            ),
            *[mob.animate.shift(3 * UP) for mob in [formula_m_n, brace_m_tex, brace_n_tex, brace_m, brace_n]]
        )
        self.wait()

    # a^n*a^1 = a^{n+1}
        formula_n_1 = Tex(
            '$a$', '$^n$', '$\cdot$', '$a$', '$^1$', ' $=$ ', '$a$', '$^n$', '$^+$', '$^1$',
            font_size=70
        ).shift(DOWN).align_to(formula_m_n, LEFT)

        self.play(Write(formula_n_1[:4], run_time=2))
        self.wait()

        self.play(Write(formula_n_1[4]))
        self.wait(0.5)

        self.play(Write(formula_n_1[5:]))
        self.wait(0.5)

        self.play(
            AnimationGroup(
                FadeOut(formula_m_n[6:10], formula_n_1, brace_m, brace_m_tex, brace_n, brace_n_tex),
                AnimationGroup(
                    ReplacementTransform(formula_m_n[:6], property_1[:6]),
                    ReplacementTransform(formula_m_n[10:14], property_1[6:])
                ),
                lag_ratio=0.5, run_time=1.5
            )
        )
        self.play(Create(property_1_rect), Write(property_1_index))
        self.wait(2)


class SecondProperty(FormulaModificationsScene):
    def construct(self):

    # (2•5)^3
        formula_1 = Tex(
            '$($', '$2$', '$\cdot$', '$5$', '$)$', '$^3$', '$=$', # 0-6
            '$10$', '$^3$', '$=$', '$10$', '$\cdot$', '$10$', '$\cdot$', '$10$', '$=$', # 7-15
            '$($', '$2$', '$\cdot$', '$5$', '$)$', '$\cdot$', # 16-21
            '$($', '$2$', '$\cdot$', '$5$', '$)$', '$\cdot$', # 22-27
            '$($', '$2$', '$\cdot$', '$5$', '$)$', '$=$', # 28-33
            '$2$', '$\cdot$', '$5$', '$\cdot$', '$2$', '$\cdot$', '$5$', '$\cdot$', '$2$', '$\cdot$', '$5$', # 34-44
            font_size=55
        )
        two_times_five = Tex('$2$', '$\cdot$', '$5$', '$=$', '$10$', font_size=55).next_to(prop_2, DOWN, buff=1)

        formula_a_b = Tex(
            '$($', '$a$', '$\cdot$', '$b$', '$)$', '$^3$', '$=$', # 0-6
            '$($', '$a$', '$\cdot$', '$b$', '$)$', '$\cdot$', # 7-12
            '$($', '$a$', '$\cdot$', '$b$', '$)$', '$\cdot$', # 13-18
            '$($', '$a$', '$\cdot$', '$b$', '$)$', '$=$', # 19-24
            '$a$', '$\cdot$', '$b$', '$\cdot$', '$a$', '$\cdot$', '$b$', '$\cdot$', '$a$', '$\cdot$', '$b$', # 25-35
            font_size=55
        )
        formula_a_b.align_to(formula_1, LEFT)

        x_cube = Tex('$x$', '$^3$', '$=$', '$x$', '$\cdot$', '$x$', '$\cdot$', '$x$', font_size=55)
        x_cube.next_to(formula_a_b, DOWN, 1, LEFT)

        property_2_copy = property_2.copy().move_to(x_cube, aligned_edge=LEFT)
    
# ANIMATIONS
        self.add(prop_1)
        self.play(
            property_1_rect.animate.set_stroke(opacity=0.5),
            property_1_index.animate.set_opacity(opacity=0.5),
            property_1.animate.set_opacity(opacity=0.5)
        )
        self.wait()

    # (2•5)^3 = 10^3 = 10•10•10 = (2•5)•(2•5)•(2•5) = 2^3•5^3
        self.play(Write(formula_1[:6]))
        self.wait()
        self.play(Write(two_times_five))
        self.wait()
        self.play(Write(formula_1[6:9]))
        self.wait()
        self.play(Write(formula_1[9:15], run_time=2))
        self.wait()
        self.play(Indicate(two_times_five))
        self.wait(0.5)

        self.play(Write(formula_1[15:21]))
        self.wait(0.1)
        self.play(Write(formula_1[21], run_time=0.75))
        self.wait(0.1)
        self.play(Write(formula_1[22:27]))
        self.wait(0.1)
        self.play(Write(formula_1[27], run_time=0.75))
        self.wait(0.1)
        self.play(Write(formula_1[28:33]))
        self.wait()
        self.play(Write(formula_1[33:]))
        self.wait()

        self.rearrange_formula(formula_1,
            [*range(34), 34, 37, 38, 41, 42, 35, 36, 39, 40, 43, 44], 
            [36, 40], [], [35, 39], [39, 41]
        )
        self.wait()
        self.play(WriteExponentInFormula(formula_1, 34, 38, '2', '3'))
        self.wait()
        self.play(WriteExponentInFormula(formula_1, 37, 41, '5', '3'))
        self.wait()

        self.play(FadeOut(two_times_five))
        self.wait()
        self.play(Create(SurroundingRectangle(formula_1[:6])))
        self.wait(0.15)
        self.play(Create(SurroundingRectangle(formula_1[34:])))
        self.wait()
        self.play(FadeOut(self.mobjects[-2], self.mobjects[-4]))
        self.wait(0.25)
        self.play(formula_1.animate.shift(1.5 * UP))
        self.wait()

    # (a•b)^3 = (a•b)•(a•b)•(a•b) = a^3•b^3
        self.play(Write(formula_a_b[:6]))
        self.wait()

        self.play(Write(x_cube[:2]))
        self.wait(0.25)
        self.play(Write(x_cube[2], run_time=0.75))
        self.wait(0.25)
        self.play(Write(x_cube[3:]))
        self.wait()

        self.play(Circumscribe(x_cube[0], Circle, fade_out=True))
        self.wait(0.25)
        self.play(Circumscribe(formula_a_b[1:4], Circle, fade_out=True, run_time=2))
        self.wait(0.25)

        self.play(Write(formula_a_b[6]))
        self.wait(0.1)
        self.play(Write(formula_a_b[7:12], run_time=0.9))
        self.wait(0.1)
        self.play(Write(formula_a_b[12], run_time=0.5))
        self.wait(0.1)
        self.play(Write(formula_a_b[13:18], run_time=0.9))
        self.wait(0.1)
        self.play(Write(formula_a_b[18], run_time=0.5))
        self.wait(0.1)
        self.play(Write(formula_a_b[19:24], run_time=0.9))
        self.wait()

        self.play(Write(formula_a_b[24:], run_time=2))
        self.wait()

        self.rearrange_formula(formula_a_b,
            [*range(25), 25, 28, 29, 32, 33, 26, 27, 30, 31, 34, 35], [27, 31], [], [26, 30], [30, 32]
        )
        self.wait()

        self.play(WriteExponentInFormula(formula_a_b, 25, 29, 'a', '3'))
        self.wait(0.5)
        self.play(WriteExponentInFormula(formula_a_b, 28, 32, 'b', '3'))
        self.wait(0.5)
        self.play(FadeOut(x_cube))
        self.wait()

        self.play(Circumscribe(formula_a_b[5], Circle, fade_out=True, run_time=3))
        self.wait()

        self.play(Write(property_2_copy[:6], run_time=1.5))
        self.wait(0.1)
        self.play(Write(property_2_copy[6]))
        self.wait(0.1)
        self.play(Write(property_2_copy[7:], run_time=1.5))
        self.wait()

        self.play(FadeOut(formula_1, formula_a_b))
        self.play(ReplacementTransform(property_2_copy, property_2))
        self.play(Create(property_2_rect), Write(property_2_index))
        self.wait()


class ThirdProperty(FormulaModificationsScene):
    def construct(self):
    
    # write previous properties with low opacity
        property_1_rect.set_stroke(opacity=0.5),
        property_1_index.set_opacity(opacity=0.5),
        property_1.set_opacity(opacity=0.5)
        self.add(prop_1, prop_2)
        self.wait()

        self.play(
            property_2_rect.animate.set_stroke(opacity=0.5),
            property_2_index.animate.set_opacity(opacity=0.5),
            property_2.animate.set_opacity(opacity=0.5)
        )
        self.wait()

    # inits for (a^4)^3 = a^4•a^4•a^4
        formula_1 = Tex(
            '$($', '$a$', '$^4$', '$)$', '$^3$', ' $=$ ', '$a$', '$^4$', '$\cdot$', '$a$', '$^4$', '$\cdot$', '$a$', '$^4$',
            font_size=65
        ).shift([-1, 1.5, 0])

        formula_2 = Tex(
            '$($', '$a$', '$^4$', '$)$', '$^3$', ' $=$ ', '$a$', '$^4$', '$^\cdot$', '$^3$', '$=$', '$a$', '$^{12}$',
            font_size=65
        ).next_to(formula_1, DOWN, buff=3)

        x_cube = Tex('$x$', '$^3$', '$=$', '$x$', '$\cdot$', '$x$', '$\cdot$', '$x$', font_size=70).next_to(formula_1, DOWN, 1, LEFT)

        a_4_1 = Tex('$a$', '$^4$', '$\cdot$', font_size=65).move_to(formula_1[6:9])
        a_4_2 = Tex('$\cdot$', '$a$', '$^4$', '$\cdot$', font_size=65).next_to(a_4_1, DOWN, buff=0.25, aligned_edge=RIGHT)
        a_4_3 = Tex('$\cdot$', '$a$', '$^4$', font_size=65).next_to(a_4_2[:-1], DOWN, buff=0.25, aligned_edge=RIGHT)

        four_times_three = Tex('$4\cdot 3=12$', font_size=70).to_edge(RIGHT, 0.5)

    # animations for (a^4)^3 = a^4•a^4•a^4
        self.play(Write(formula_1[1:3]))
        self.wait(0.1)
        self.play(Write(formula_1[0]), Write(formula_1[3]))
        self.wait(0.1)
        self.play(Write(formula_1[4]))
        self.wait()
        
        self.play(Write(x_cube[:2]))
        self.wait(0.25)
        self.play(Write(x_cube[2:], run_time=3))
        self.wait(0.5)

        self.play(Circumscribe(formula_1[1:3], Circle, fade_out=True, run_time=1))
        self.wait(0.5)

        self.play(Write(formula_1[5:], run_time=3.5))
        self.wait(0.5)

        self.play(FadeOut(x_cube))
        self.wait()

        self.play(
            ReplacementTransform(formula_1[6:9], a_4_1),
            ReplacementTransform(formula_1[9:12], a_4_2[1:]),
            FadeIn(a_4_2[0]),
            ReplacementTransform(formula_1[12:14], a_4_3[1:]),
            FadeIn(a_4_3[0])
        )
        self.wait()

        self.extract_exponent_in_formula(a_4_1, 0, 'a', 4, True)
        self.wait(0.5)
        self.extract_exponent_in_formula(a_4_2, 1, 'a', 4, True)
        self.wait(0.5)
        self.extract_exponent_in_formula(a_4_3, 1, 'a', 4, True)
        self.wait()

    # init braces
        rect_4_3 = VGroup(a_4_1, a_4_2, a_4_3)

        brace_3 = Brace(rect_4_3, RIGHT)
        brace_3_tex = Tex('$3$', font_size=65).next_to(brace_3, RIGHT, 0.15)

        brace_4 = Brace(rect_4_3, UP, 0.15)
        brace_4_tex = Tex('$4$', font_size=65).next_to(brace_4, UP, 0.15)

    # animate braces
        self.play(Write(brace_4), Write(brace_4_tex))
        self.wait(0.1)
        self.play(Write(brace_3), Write(brace_3_tex))
        self.wait(0.5)

        self.play(Write(four_times_three, run_time=2))
        self.wait()

        self.play(Write(formula_2[:5], run_time=1.5))
        self.wait(0.25)
        self.play(Write(formula_2[5:10], run_time=1.5))
        self.wait(0.25)
        self.play(Write(formula_2[10:], run_time=1.5))
        self.wait()

        self.play(
            FadeOut(formula_1[:6], brace_3, brace_3_tex, brace_4, brace_4_tex, rect_4_3, four_times_three),
            formula_2.animate.align_to(formula_1, UP)
        )
        self.wait()


    # inits fot (a^m)^n = m•n a-s in rectangle
        formula_m_n = Tex(
            '$($', '$a$', '$^m$', '$)$', '$^n$', ' $=$ ', # 0-5
            '$a$', '$^m$', '$\cdot$', '$a$', '$^m$', '$\cdot$', '$...$', '$\cdot$', '$a$', '$^m$', # 6-15
            font_size=65
        ).next_to(formula_2, DOWN, buff=1.25)

        a_m_1 = Tex('$a$', '$^m$', '$\cdot$', font_size=65).move_to(formula_m_n[6:9])
        a_m_2 = Tex('$\cdot$', '$a$', '$^m$', '$\cdot$', font_size=65).next_to(a_m_1, DOWN, 0.25, RIGHT)
        a_m_dots = Tex('$\\vdots$', font_size=65).next_to(a_m_2[1], DOWN, 0.25, LEFT)
        a_m_3 = Tex('$\cdot$', '$a$', '$^m$', font_size=65).next_to(a_m_dots, DOWN, 0.15).align_to(a_m_2[:-1], RIGHT)

        self.play(Write(formula_m_n[:5]))
        self.wait(0.25)
        self.play(Write(formula_m_n[5:]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(formula_m_n[6:9], a_m_1),
            ReplacementTransform(formula_m_n[9:12], a_m_2[1:]),
            FadeIn(a_m_2[0]),
            ReplacementTransform(formula_m_n[12], a_m_dots),
            ReplacementTransform(formula_m_n[13:16], a_m_3)
        )
        self.wait(0.5)

    # init brace vertical
        brace_n = always_redraw(lambda: Brace(VGroup(a_m_1, a_m_2, a_m_dots, a_m_3), RIGHT))
        brace_n_tex = always_redraw(lambda: Tex('$n$', font_size=65).next_to(brace_n))


        self.play(Write(brace_n), Write(brace_n_tex))
        self.wait(0.5)

        self.play(
            Transform(a_m_1, Tex('$a$', '$\cdot$', '$a$', '$\cdot$', '$...$', '$\cdot$', '$a$', '$\cdot$', font_size=65).align_to(a_m_1, DL)),
            Transform(a_m_2, Tex('$\cdot$', '$a$', '$\cdot$', '$a$', '$\cdot$', '$...$', '$\cdot$', '$a$', '$\cdot$', font_size=65).align_to(a_m_2, DL)),
            Transform(a_m_3, Tex('$\cdot$', '$a$', '$\cdot$', '$a$', '$\cdot$', '$...$', '$\cdot$', '$a$', font_size=65).align_to(a_m_3, DL))
        )
        self.wait(0.5)
    
    # init brace horizontal
        brace_m = Brace(a_m_1, UP, 0.15)
        brace_m_tex = Tex('$m$', font_size=65).next_to(brace_m, UP, 0.15)

        self.play(Write(brace_m), Write(brace_m_tex))
        self.wait(0.5)

        self.play(Write(property_3[:5]))
        self.wait(0.5)
        self.play(Write(property_3[5:], run_time=2))
        self.wait(0.5)
        self.play(Create(property_3_rect), Write(property_3_index))
        self.wait(0.5)

        self.play(FadeOut(brace_m, brace_m_tex, brace_n, brace_n_tex, a_m_1, a_m_2, a_m_3, a_m_dots, formula_m_n[:6], formula_2))
        self.wait()

        self.play(
            property_2_rect.animate.set_stroke(opacity=1),
            property_2_index.animate.set_opacity(opacity=1),
            property_2.animate.set_opacity(opacity=1),
            property_1_rect.animate.set_stroke(opacity=1),
            property_1_index.animate.set_opacity(opacity=1),
            property_1.animate.set_opacity(opacity=1)
        )
        self.wait()


class TwoExercises(Scene):
    def construct(self):
        self.add(prop_1, prop_2, prop_3)
        self.wait()
        
        formula = Tex ('$($', '$a$', '$^2$', '$)$', '$^5$', '$\cdot$', '$a$', '$^3$',
                '$=$', '$a$', '$^{10}$', '$\cdot$', '$a$', '$^3$', '$=$', '$a$', '$^{10+3}$', '$^{13}$',
                font_size=65
        )
        formula[-1].align_to(formula[-2], LEFT)
        formula_1 = formula[:5].copy()
        formula_2 = formula[5:8].copy()

    # բանաձևը գրում ենք ու (a^2)^5-ը իջացնում ներքև
        self.wait()
        self.play(Write(formula[:5]))
        self.wait(0.25)
        self.play(Write(formula[5:8]))
        self.wait()
        
        self.play(Indicate(property_3))
        self.wait()

        self.play(formula_1.animate.shift(DOWN))
        self.wait()

    # (a^2)^5 -> a^10
        formula_1_new = Tex('$a$', '$^2$','$^{\cdot}$', '$^5$', font_size=65).shift(UP)
        formula_1_new.align_to(formula_1[1], DL)
        formula_1_new_new = Tex('$a$', '$^{10}$', font_size=65).align_to(formula_1_new, DL)

        self.play(
            ReplacementTransform(formula_1[2], formula_1_new[1]),
            ReplacementTransform(formula_1[4], formula_1_new[3]),
            FadeOut(formula_1[0], formula_1[3]),
            Write(formula_1_new[2])
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
            ReplacementTransform(formula_2, formula[11:-4]),
            Write(formula[8])
        )
        self.wait()
        self.play(Indicate(property_1))
        self.wait()
    
    # ստանում ենք պատասխանը
        self.play(Write(formula[-4:-1]))
        self.wait(0.25)
        self.play(ReplacementTransform(formula[-2], formula[-1]))
        self.wait()
        self.play(formula.animate.shift(UP))
        self.wait()

    # երկրորդ վարժություն
        formula_2 = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', ' $=$ ', '$?$', font_size=65)
        formula_2.next_to(formula, DOWN, buff=1).align_to(formula, LEFT)

        self.play(Write(formula_2, run_time=2))
        self.wait()
        






# class HorizontalThrowingBall(Scene):
#     def construct(self):

# # INITS
#         ball_initial_pos = np.array([-4, -1, 0])
#         ball_pos_prop = ValueTracker(0)

#         path_1 = SVGMobject('objects/SVG_files/ball_paths/path_1').scale(4).set_color(WHITE).next_to(ball_initial_pos, UR, buff=0)
#         path_1.points = path_1.get_all_points()
#         arrow_1 = Arrow().rotate(4/9 * PI).next_to(ball_initial_pos, UR, buff=0)

#         path_2 = SVGMobject('objects/SVG_files/ball_paths/path_2').scale(2/7).set_color(WHITE).next_to(ball_initial_pos, UR, buff=0)
#         path_2.points = path_2.get_all_points()
#         ball_pos_prop = ValueTracker(0)

#         ball = SimpleSVGMobject('tennis_ball').move_to(ball_initial_pos).scale(0.5)
#         ball.add_updater(lambda mob: mob.move_to(path_1.point_from_proportion(ball_pos_prop.get_value())))

#         self.add(ball)
#         self.wait()

#         self.play(Create(arrow_1))
#         self.wait()
#         self.play(ball_pos_prop.animate(run_time=1, rate_func=rush_from).set_value(0.25))
#         self.play(ball_pos_prop.animate(run_time=1, rate_func=rush_into).set_value(0.5))
#         self.wait()
#         ball.clear_updaters()
#         ball_pos_prop.set_value(0)

#         ball.move_to(ball_initial_pos)
#         self.wait()
#         ball.add_updater(lambda mob: mob.move_to(path_2.point_from_proportion(ball_pos_prop.get_value())))
#         self.play(ball_pos_prop.animate(run_time=0.5, rate_func=rush_from).set_value(0.25))
#         self.play(ball_pos_prop.animate(run_time=0.5, rate_func=rush_into).set_value(0.5))
#         self.wait()
