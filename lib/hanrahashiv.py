from manim import Tex, MathTex
from manim import UP, DOWN, LEFT, DL
from manim import Scene
from manim import ReplacementTransform, FadeOut, FadeIn, Write
from manim import VGroup

class FormulaModificationsScene(Scene):

#  միգուցե էս ամենը տեղափոխել QarakusiScene (որտև մենակ միանդամների մեջ չի, որ պետք կգան)

    def rearrange_formula(self,
        formula : Tex or MathTex, new_sequence : list, 
        move_up : list = [], move_down : list = [],
        fade_out : list = [], fade_in : list = [],
        run_time=3
    ):
        """
            Rearranges formula with new_sequence 
            new_sequence is a permutation of range(len(formula))
            move_up, move_down, fade_out are list in which numbers represent the indices in the formula
            fade_in is a list in which numbers represent the indices in new formula (with new sequence)
            move_up is to move some variables (members of formula) up and into new positions
            fade_out and fade_in are mainly used for multiplication signs
            move_down is like move up, but it's just in case. You don't really need it in most of the cases

        """
        tex_string_list = [tex.get_tex_string() for tex in formula]
        new_tex_string_list = [tex_string_list[new_sequence[i]] for i in range(len(tex_string_list))]
        new_formula = type(formula)(
            *new_tex_string_list, 
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula)

        in_line = []
        for i in range(len(tex_string_list)):
            if i not in move_up and i not in move_down: #and i not in fade_out: # i not in fade_in and
                in_line.append(i)

        self.play(
            *[formula[i].animate.shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.set_opacity(0) for i in fade_out],
            run_time=run_time / 4
        )
        self.play(
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]) for i in in_line],
            run_time=run_time / 4
        )
        self.play(
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_up],
            *[formula[i].animate.shift(0.5 * UP) for i in move_down],
            *[FadeIn(new_formula[i]) for i in fade_in],
            run_time=run_time / 4
        )
        self.play(
            *[ReplacementTransform(formula[new_sequence[i]], new_formula[i], run_time=0.1) for i in range(len(formula))]
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def multiply_numbers_in_formula(self,
        formula : Tex  or MathTex, number_of_multiplying_items : int, 
        resulting_number_str : str, run_time=1
    ):
        """
            Multiplies the numbers in the beginning of the formula 
            number_of_multiplying_items is the number of members in the beginning of the formula
            (including multiplication sign) that need to be transformed into one number
            resulting_number_str is the product that must be written
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_item = '$' + resulting_number_str + '$'
        elif type(formula) == MathTex:
            new_item = resulting_number_str

        new_formula = type(formula)(
            new_item, *tex_string_list[number_of_multiplying_items:],
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, LEFT)

        self.play(
            ReplacementTransform(formula[:number_of_multiplying_items], new_formula[0]),
            ReplacementTransform(formula[number_of_multiplying_items:], new_formula[1:]),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def write_exponent_in_formula(self,
        formula : Tex  or MathTex, first_item_index : int, 
        last_item_index : int, base : str, exponent : int,
        run_time=1
    ):
        """
            Combines adjacent same letters and writes in form of exponent
            takes indices of items to be combined, base and exponent and
            formula[first_item_index : last_item_index + 1] transforms into base^exponent
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]
        

        if type(formula) == Tex:
            new_items = [f'${base}$', f'$^{exponent}$']
        elif type(formula) == MathTex:
            new_items = [f'{base}', f'^{exponent}']
        
        new_formula = type(formula)(
            *tex_string_list[:first_item_index], *new_items, *tex_string_list[last_item_index + 1:],
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        self.play(
            ReplacementTransform(formula[:first_item_index], new_formula[:first_item_index]),
            ReplacementTransform(formula[first_item_index : last_item_index + 1], new_formula[first_item_index : first_item_index + 2]),
            ReplacementTransform(formula[last_item_index + 1:], new_formula[first_item_index + 2:]),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def extract_exponent_in_formula(self,
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

        self.play(
            ReplacementTransform(
                formula[:item_index],
                new_formula[:item_index],
            ),
            ReplacementTransform(
                formula[item_index : item_index + 2], 
                new_formula[item_index : item_index + len(new_items)]
            ),
            ReplacementTransform(
                formula[item_index + 2:], 
                new_formula[item_index + len(new_items):],
            ),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def add_items_in_formula(self,
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

        animations = [FadeIn(*[new_formula[i] for i in new_items_indices_in_new_formula])]

        animations += [
            ReplacementTransform(formula[:after_items[0] + 1], new_formula[:new_items_indices_in_new_formula[0]]),
            ReplacementTransform(formula[after_items[-1] + 1:], new_formula[new_items_indices_in_new_formula[-1] + 1:])
        ]

        for i in range(0, len(after_items) - 1):
            animations.append(
                ReplacementTransform(
                    formula[after_items[i] + 1 : after_items[i + 1] + 1],
                    new_formula[new_items_indices_in_new_formula[i] + 1 : new_items_indices_in_new_formula[i + 1]]
                )
            )

        self.play(*animations, run_time=run_time)

        formula.remove(*formula)
        formula.add(*new_formula)


    def remove_items_from_formula(self,
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

        animations = [FadeOut(*[formula[i] for i in items_indices])]

        animations += [
            ReplacementTransform(formula[:items_indices[0]], new_formula[:items_indices[0]]),
            ReplacementTransform(formula[items_indices[-1] + 1:], new_formula[items_indices[-1] - len(items_indices) + 1:])
        ]

        for i in range(len(items_indices) - 1):
            animations.append(
                ReplacementTransform(
                    formula[items_indices[i] + 1 : items_indices[i + 1]],
                    new_formula[items_indices[i] - i: items_indices[i + 1] - i - 1]
                )
            )

        self.play(*animations, run_time=run_time)

        formula.remove(*formula)
        formula.add(*new_formula)


    def combine_two_exponents(self,
        formula : Tex or MathTex, bases_indices : list, exponents_indices : list, new_exponent : int, fade_out : list,
        run_time=1
    ):
        """
            must be adjacent
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_item_exponent = f'$^{new_exponent}$'
        elif type(formula) == MathTex:
            new_item_exponent = f'^{new_exponent}'
        
        last_item_index = max(bases_indices + exponents_indices)
        print(last_item_index)

        new_formula = type(formula)(
            *tex_string_list[:bases_indices[0] + 1], new_item_exponent, *tex_string_list[last_item_index + 1 :], 
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        self.play(
            ReplacementTransform(formula[:bases_indices[0]], new_formula[:bases_indices[0]]),
            ReplacementTransform(VGroup(*[formula[i] for i in exponents_indices]), new_formula[bases_indices[0] + 1]),
            ReplacementTransform(VGroup(*[formula[i] for i in bases_indices]), new_formula[bases_indices[0]]),
            ReplacementTransform(formula[last_item_index + 1 :], new_formula[bases_indices[0] + 2 :]),
            FadeOut(*[formula[i] for i in fade_out]),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)
