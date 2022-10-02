from manim import *
from hanrahashiv import *

from constants import ARMTEX, ENGTEX
from objects import SimpleSVGMobject

def throw_up_fall_down(t : float) -> float:
    new_t = 2 * t if t < 0.5 else 2 * (1 - t)
    return rush_from(new_t)

def accelerating(t : float) -> float:
    return t ** 2

def decelerating(t : float) -> float:
    return t ** (1/2)

class ThrowingBalls(Scene):
    def construct(self):

        time_scale = 1.3

        bottom_line_y = -3
        bottom_line = Line([-10, bottom_line_y, 0], [10, bottom_line_y, 0])

        ball_1 = SimpleSVGMobject('tennis_ball').scale(0.5)
        ball_1.move_to([-4, bottom_line_y, 0]).align_to(bottom_line, DOWN)
        height_1 = ValueTracker(0)
        tex_height_1 = always_redraw(lambda: Tex(f'${int(height_1.get_value())}$ մ', tex_template=ARMTEX).next_to(ball_1))
        v_1 = Tex('$V$ = 20 մ/վ', tex_template=ARMTEX).next_to(ball_1, DOWN)
        arrow_1 = Arrow().rotate(PI / 2).scale(0.75).next_to(ball_1.get_center(), UP, buff=0)

        ball_2 = SimpleSVGMobject('tennis_ball').scale(0.5)
        ball_2.move_to([0, bottom_line_y, 0]).align_to(bottom_line, DOWN)

        ball_3 = SimpleSVGMobject('tennis_ball').scale(0.5)
        ball_3.move_to([4, bottom_line_y, 0]).align_to(bottom_line, DOWN)


        self.add(bottom_line)
        self.play(FadeIn(ball_1))
        self.play(Write(tex_height_1))
        self.wait(0.5)
        self.play(
            Create(arrow_1),
            Write(v_1)
        )
        self.wait()

        self.play(
            ball_1.animate(rate_func=rush_from, run_time=3 / 2 * time_scale).shift(2 * UP),
            height_1.animate(rate_func=rush_from, run_time = 3 / 2 * time_scale).set_value(20),
            FadeOut(arrow_1)
        )
        tex_height_1.clear_updaters()
        ball_1_highest = ball_1.copy().set_opacity(0.25)
        self.add(ball_1_highest)
        self.play(
            ball_1.animate(rate_func=rush_into, run_time=3 / 2 * time_scale).shift(2 * DOWN),
        )
        self.wait()

        # self.play(
        #     ball_1.animate(rate_func=throw_up_fall_down, run_time=3 / time_scale).shift(2 * UP),
        #     height_1.animate(rate_func=rush_from, run_time = 3 / 2 * time_scale).set_value(20),
        #     tex_height_1.animate.shift(UP),
        #     ball_2.animate(rate_func=throw_up_fall_down, run_time=4 / time_scale).shift(2 * UP * 16/9),
        #     ball_3.animate(rate_func=throw_up_fall_down, run_time=5 / time_scale).shift(2 * UP * 25/9),
        # )
        self.wait()

# class FirstProperty(FormulaModificationsScene):
#     def construct(self):

#     # write formula_1   2^4 • 2^5
#         formula_1 = Tex(
#             '$2$', '$^4$', ' ', '$\cdot$', ' ', '$2$', '$^5$', ' $=$ ',
#             '$2$', '$^4$', ' ', '$\cdot$', ' ', '$2$', '$^5$',
#             font_size=60
#         ) # 2^4 • 2^5 = 2^4 • 2^5
#         formula_1.shift(2.75 * LEFT)

#         self.play(Write(formula_1[:2]))
#         self.wait(0.1)
#         self.play(Write(formula_1[2]), Write(formula_1[3]), Write(formula_1[4]))
#         self.wait(0.1)
#         self.play(Write(formula_1[5:7]))
#         self.wait()

#     # write definition of exponent
#         product_a_n_hat = Tex('$a \cdot a \cdot a \cdot ... \cdot a \cdot a$', '$=$', '$a$', '$^n$', font_size=70)
#         product_a_n_hat.to_edge(UP)
#         brace_product_n = Brace(product_a_n_hat[0], DOWN)
#         quantity_product_n = Tex('$n$', font_size=70).next_to(brace_product_n, DOWN)

#         self.play(
#             Write(product_a_n_hat),
#             Write(brace_product_n),
#             Write(quantity_product_n)
#         )
#         self.wait()

#     # extract 2^4 into 2•2•2•2 and brace under it
#         self.play(
#             ReplacementTransform(formula_1[0:7].copy(), formula_1[8:15]),
#             Write(formula_1[7])
#         )
#         self.wait(0.25)

#         self.play(Circumscribe(formula_1[8:10], fade_out=True, run_time=1.5))
#         self.wait()
#         self.play(ExtractExponentInFormula(formula_1, 8, '2', 4, True)) # 2^4 • 2^5 = 2•2•2•2 • 2^5

#         brace_on_4 = Brace(formula_1[8:15], DOWN)
#         brace_4 = Tex('$4$').next_to(brace_on_4, DOWN)

#         self.play(Write(brace_on_4), Write(brace_4))
#         self.wait()

#     # extract 2^5 into 2•2•2•2•2 and brace under it
#         self.play(Circumscribe(formula_1[18:20], fade_out=True, run_time=1.5))
#         self.wait()
#         self.play(ExtractExponentInFormula(formula_1, 18, '2', 5, True)) # 2^4 • 2^5 = 2•2•2•2 • 2•2•2•2•2

#         brace_on_5 = Brace(formula_1[18:27], DOWN)
#         brace_5 = Tex('$5$').next_to(brace_on_5, DOWN)

#         self.play(Write(brace_on_5), Write(brace_5))
#         self.wait()

#     # remove spaces form formula
#         self.play(
#             RemoveItemsFromFormula(formula_1, [15, 17]),
#             brace_5.animate.shift(LEFT * 0.41),
#             brace_on_5.animate.shift(LEFT * 0.41),
#         )# 2•2•2•2•2•2•2•2•2
#         self.wait()
    
#     # combine 4 and 5, write 4+5=9
#         brace_on_9 = Brace(formula_1[8:25], DOWN)
#         brace_9 = Tex('$4$', '$+$', '$5$', '$=$', '$9$').next_to(brace_on_9, DOWN)

#         self.play(
#             ReplacementTransform(brace_4, brace_9[0]),
#             ReplacementTransform(brace_5, brace_9[2]),
#             Write(brace_9[1])
#         )
#         self.wait(0.1)
#         self.play(Write(brace_9[3:]))
#         self.wait()
    
#     # write = 2^{4+5} = 2^9
#         formula_2 = Tex(
#             ' $=$ ', '$2$', '$^4$', '$^+$', '$^5$', ' $=$ ', '$2$', '$^9$',
#             font_size=60
#         ) # = 2^{4+5}=2^9
#         formula_2.next_to(formula_1, RIGHT)

#         self.play(Write(formula_2, run_time=2))
#         self.wait()

#     # transform everything to 4+6=10 in exponents
#         self.replace_items_in_formula(formula_1, [6], ['$^6$'])
#         self.wait(0.25)

#         self.play(
#             AddItemsInFormula(formula_1, [len(formula_1) - 1], ['$\cdot 2$']),
#             brace_on_5.animate.stretch(1.25, 0).shift(0.3 * RIGHT),
#             ReplaceItemsInFormula(brace_9, [2, 4], ['6', '10']),
#             formula_2.animate.shift(0.4 * RIGHT)
#         )
#         self.wait(0.25)

#         self.replace_items_in_formula(formula_2, [4, 7], ['^6', '^{10}'])
#         self.wait()

#         self.play(*[mob.animate.shift(UP) for mob in [formula_1, formula_2, brace_on_4, brace_on_5, brace_9]])
#         self.wait()
    
#     # same property for m and n
#         formula_m_n_1 = Tex(
#             '$a$', '$^m$', ' $\cdot$ ', '$a$', '$^n$', '$= $',
#             '$a^m$', ' $\cdot$ ', '$a^n$',
#             font_size=70
#         ).shift([-3, -1.5, 0])
#         # [mob.set_color(GREEN) for mob in [formula_m_n_1[1], formula_m_n_1[6]]]
#         # [mob.set_color(ORANGE) for mob in [formula_m_n_1[4], formula_m_n_1[8]]]

#         self.play(Write(formula_m_n_1[:5]))
#         self.wait()
#         self.play(Write(formula_m_n_1[5:]))
#         self.wait()

#     # extract a^m brace it
#         self.replace_items_in_formula(formula_m_n_1, [6], ['$a\cdot$$a\cdot$$...$$\cdot$$a$'])
#         self.wait(0.25)

#         brace_on_m = Brace(formula_m_n_1[6], DOWN)
#         brace_m = Tex('$m$').next_to(brace_on_m, DOWN)
#         # brace_m.set_color(GREEN)

#         self.play(Write(brace_on_m), Write(brace_m))
#         self.wait(0.5)

#     # extract a^n brace it
#         self.replace_items_in_formula(formula_m_n_1, [8], ['$a\cdot$$a\cdot$$...$$\cdot$$a$'])
#         self.wait(0.25)

#         brace_on_n = Brace(formula_m_n_1[8], DOWN)
#         brace_n = Tex('$n$').next_to(brace_on_n, DOWN)
#         # brace_n.set_color(ORANGE)

#         self.play(Write(brace_on_n), Write(brace_n))
#         self.wait(0.5)
    
#     # is equal to a^{m+n}
#         formula_m_n_2 = Tex(
#             '$=$ ', '$a$', '$^m$', '$^+$', '$^n$', font_size=70
#         ).next_to(formula_m_n_1)
#         # formula_m_n_2[2].set_color(GREEN)
#         # formula_m_n_2[4].set_color(ORANGE)

#         self.play(Write(formula_m_n_2))
#         self.wait()







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

