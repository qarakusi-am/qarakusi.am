from manim import *
# from hanrahashiv import *

from constants import ARMTEX, ENGTEX
from objects import SimpleSVGMobject


def AddItemsInFormula(
        formula : Tex or MathTex, after_items : list, items_str_list : list,
        run_time=1
    ):
        """
            Adds items to the formula in after items by fading_in and shifting the rest to the right
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            if items_str_list[0][0] == '$':
                new_items = items_str_list
            else:
                new_items = ['$' + item + '$' for item in items_str_list]

        elif type(formula) == MathTex:
            if items_str_list[0][0] == '$':
                new_items = [item[1:-1] for item in items_str_list]   
            else:
                 new_items = items_str_list

        new_formula_tex_string_list = [*tex_string_list[:after_items[0] + 1]]
        for i in range(len(new_items) - 1):
            new_formula_tex_string_list.append(new_items[i])
            new_formula_tex_string_list += tex_string_list[after_items[i] + 1 : after_items[i + 1] + 1]
        new_formula_tex_string_list.append(new_items[-1])
        new_formula_tex_string_list += tex_string_list[after_items[-1] + 1 :]
        
        new_formula = type(formula)(
            *new_formula_tex_string_list,
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        new_items_indices_in_new_formula = []
        for i in range(len(after_items)):
            new_items_indices_in_new_formula.append(after_items[i] + i + 1)

        animations = [FadeIn(*[new_formula[i] for i in new_items_indices_in_new_formula], run_time=run_time)]

        animations += [
            ReplacementTransform(formula[:after_items[0] + 1], new_formula[:new_items_indices_in_new_formula[0]], run_time=run_time),
            ReplacementTransform(formula[after_items[-1] + 1:], new_formula[new_items_indices_in_new_formula[-1] + 1:], run_time=run_time)
        ]

        for i in range(0, len(after_items) - 1):
            animations.append(
                ReplacementTransform(
                    formula[after_items[i] + 1 : after_items[i + 1] + 1],
                    new_formula[new_items_indices_in_new_formula[i] + 1 : new_items_indices_in_new_formula[i + 1]],
                    run_time=run_time
                )
            )

        formula.remove(*formula)
        formula.add(*new_formula)

        return AnimationGroup(*animations)


def ExtractExponentInFormula(
    formula : Tex  or MathTex, item_index : int,
    base : str, exponent : int, add_multiplication_signs_in_between=False,
    run_time=1
):
    """
        Extracts an item that is written in form of exponent (ex. a^3 -> aaa)
        Takes index of that first item ('a' '^3'), base('a'), exponent(3)
        Depending on value of add_multiplication_signs_in_between it can write aaa or a•a•a
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]

    if type(formula) == Tex:
        if add_multiplication_signs_in_between:
            new_items = [f'${base}$', '$\cdot$'] * exponent
            new_items.pop()
        else:
            new_items = [f'${base}$'] * exponent

    elif type(formula) == MathTex:
        if add_multiplication_signs_in_between:
            new_items = [f'{base}', '\cdot'] * exponent
            new_items.pop()
        else:
            new_items = [f'{base}'] * exponent

    new_formula = type(formula)(
        *tex_string_list[:item_index], *new_items, *tex_string_list[item_index + 2:],
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)

    animations = AnimationGroup(
        ReplacementTransform(
            formula[:item_index],
            new_formula[:item_index],
            run_time=run_time
        ),
        ReplacementTransform(
            formula[item_index : item_index + 2], 
            new_formula[item_index : item_index + len(new_items)],
            run_time=run_time
        ),
        ReplacementTransform(
            formula[item_index + 2:], 
            new_formula[item_index + len(new_items):],
            run_time=run_time
        )
    )

    formula.remove(*formula)
    formula.add(*new_formula)

    return animations


def ReplaceItemsInFormula(
    formula : Tex or MathTex, items_indices : list, items_str_list : list,
    run_time=1
):
    tex_string_list = [tex.get_tex_string() for tex in formula]

    if type(formula) == Tex:
        if items_str_list[0][0] == '$':
            new_items = items_str_list
        else:
            new_items = ['$' + item + '$' for item in items_str_list]

    elif type(formula) == MathTex:
        if items_str_list[0][0] == '$':
            new_items = [item[1:-1] for item in items_str_list]   
        else:
            new_items = items_str_list
    
    new_formula_tex_string_list = [*tex_string_list[:items_indices[0]]]
    for i in range(len(items_indices) - 1):
        new_formula_tex_string_list.append(new_items[i])
        new_formula_tex_string_list += tex_string_list[items_indices[i] + 1 : items_indices[i + 1]]
    new_formula_tex_string_list.append(new_items[-1])
    new_formula_tex_string_list += tex_string_list[items_indices[-1] + 1 :]

    new_formula = type(formula)(
        *new_formula_tex_string_list,
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)#.shift(DOWN)

    animations = [ReplacementTransform(formula[i], new_formula[i], run_time=run_time) for i in range(len(formula))]

    formula.remove(*formula)
    formula.add(*new_formula)

    return AnimationGroup(*animations)


def RemoveItemsFromFormula(
    formula : Tex or MathTex, items_indices : list,
    run_time=1
):
    """
        removes items by fading out
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]

    for i in range(len(items_indices)):
        del tex_string_list[items_indices[i] - i]
    
    new_formula = type(formula)(
        *tex_string_list, 
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)

    animations = [FadeOut(*[formula[i] for i in items_indices], run_time=run_time)]

    animations += [
        ReplacementTransform(formula[:items_indices[0]], new_formula[:items_indices[0]], run_time=run_time),
        ReplacementTransform(formula[items_indices[-1] + 1:], new_formula[items_indices[-1] - len(items_indices) + 1:], run_time=run_time)
    ]

    for i in range(len(items_indices) - 1):
        animations.append(
            ReplacementTransform(
                formula[items_indices[i] + 1 : items_indices[i + 1]],
                new_formula[items_indices[i] - i: items_indices[i + 1] - i - 1],
                run_time=run_time
            )
        )

    formula.remove(*formula)
    formula.add(*new_formula)

    return AnimationGroup(*animations)



# class ThrowingBall(Scene):
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



class FirstProperty(Scene):
    def construct(self):

    # write formula_1   2^4 • 2^5
        formula_1 = Tex(
            '$2$', '$^4$', ' ', '$\cdot$', ' ', '$2$', '$^5$', ' $=$ ',
            '$2$', '$^4$', ' ', '$\cdot$', ' ', '$2$', '$^5$',
            font_size=60
        ) # 2^4 • 2^5 = 2^4 • 2^5
        formula_1.shift(2.75 * LEFT)

        self.play(Write(formula_1[:2]))
        self.wait(0.1)
        self.play(Write(formula_1[2]), Write(formula_1[3]), Write(formula_1[4]))
        self.wait(0.1)
        self.play(Write(formula_1[5:7]))
        self.wait()

    # write definition of exponent
        product_a_n_hat = Tex('$a \cdot a \cdot a \cdot ... \cdot a \cdot a$', '$=$', '$a$', '$^n$', font_size=70)
        product_a_n_hat.to_edge(UP)
        brace_product_n = Brace(product_a_n_hat[0], DOWN)
        quantity_product_n = Tex('$n$', font_size=70).next_to(brace_product_n, DOWN)

        self.play(
            Write(product_a_n_hat),
            Write(brace_product_n),
            Write(quantity_product_n)
        )
        self.wait()

    # extract 2^4 into 2•2•2•2 and brace under it
        self.play(
            ReplacementTransform(formula_1[0:7].copy(), formula_1[8:15]),
            Write(formula_1[7])
        )
        self.wait(0.25)

        self.play(Circumscribe(formula_1[8:10], fade_out=True, run_time=1.5))
        self.wait()
        self.play(ExtractExponentInFormula(formula_1, 8, '2', 4, True)) # 2^4 • 2^5 = 2•2•2•2 • 2^5

        brace_on_4 = Brace(formula_1[8:15], DOWN)
        brace_4 = Tex('$4$').next_to(brace_on_4, DOWN)

        self.play(Write(brace_on_4), Write(brace_4))
        self.wait()

    # extract 2^5 into 2•2•2•2•2 and brace under it
        self.play(Circumscribe(formula_1[18:20], fade_out=True, run_time=1.5))
        self.wait()
        self.play(ExtractExponentInFormula(formula_1, 18, '2', 5, True)) # 2^4 • 2^5 = 2•2•2•2 • 2•2•2•2•2

        brace_on_5 = Brace(formula_1[18:27], DOWN)
        brace_5 = Tex('$5$').next_to(brace_on_5, DOWN)

        self.play(Write(brace_on_5), Write(brace_5))
        self.wait()

    # remove spaces form formula
        self.play(
            RemoveItemsFromFormula(formula_1, [15, 17]),
            brace_5.animate.shift(LEFT * 0.41),
            brace_on_5.animate.shift(LEFT * 0.41),
        )# 2•2•2•2•2•2•2•2•2
        self.wait()
    
    # combine 4 and 5, write 4+5=9
        brace_on_9 = Brace(formula_1[8:25], DOWN)
        brace_9 = Tex('$4$', '$+$', '$5$', '$=$', '$9$').next_to(brace_on_9, DOWN)

        self.play(
            ReplacementTransform(brace_4, brace_9[0]),
            ReplacementTransform(brace_5, brace_9[2]),
            Write(brace_9[1])
        )
        self.wait(0.1)
        self.play(Write(brace_9[3:]))
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
        self.play(
            AddItemsInFormula(formula_1, [len(formula_1) - 1], ['$\cdot 2$']),
            brace_on_5.animate.stretch(1.25, 0).shift(0.3 * RIGHT),
            ReplaceItemsInFormula(brace_9, [2, 4], ['6', '10']),
            formula_2.animate.shift(0.4 * RIGHT)
        )
        self.wait()

        self.play(ReplaceItemsInFormula(formula_2, [4, 7], ['^6', '^{10}']))
        self.wait()

        # self.play(ReplaceItemsInFormula(formula_2, [1, 6], ['3', '3']))
        # self.wait()







class test(Scene):
    def construct(self):
        formula_1 = Tex('$4$', '$+$', '$5$', '$=$', '$9$')

        self.add(formula_1)
        self.wait()
        self.play(ReplaceItemsInFormula(formula_1, [2, 4], ['6', '10']))
        self.wait()






