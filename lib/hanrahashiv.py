from manim import Tex, MathTex
from manim import UP, DOWN, LEFT, DL
from manim import Scene
from manim import ReplacementTransform, FadeOut, FadeIn

class FormulaModifications(Scene):

# FIXME մարդավարի docstring գրել ամեն ֆունկցիայի համար
#  միգուցե էս ամենը տեղափոխել QarakusiScene (որտև մենակ միանդամների մեջ չի, որ պետք կգան)
    """
        new_sequence addresses each of formula's item to it's new position, including '$\cdot$', ' + '
        new_sequence is a permutation of numbers form range(len(formula))
        to work properly, formula must be written in such a way that every item is in different apostrophes like so
        formula = Tex('a', '$\cdot$', 'b')
    """

    def rearrange_formula(self,
        formula : Tex or MathTex, new_sequence : list, 
        move_up : list, move_down : list,
        fade_out : list, fade_in : list
    ):
        tex_string_list = [tex.get_tex_string() for tex in formula]
        new_tex_string_list = [tex_string_list[new_sequence[i]] for i in range(len(tex_string_list))]
        new_formula = Tex(*new_tex_string_list, font_size=formula[0].font_size, color=formula.color).move_to(formula)

        in_line = []
        for i in range(len(tex_string_list)):
            if i not in move_up and i not in move_down: #and i not in fade_out: # i not in fade_in and
                in_line.append(i)

        self.play(
            *[formula[i].animate.shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.set_opacity(0) for i in fade_out]
        )
        self.play(
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]) for i in in_line]
        )
        self.play(
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_up],
            *[formula[i].animate.shift(0.5 * UP) for i in move_down],
            *[FadeIn(new_formula[i]) for i in fade_in]
        )
        self.play(
            *[ReplacementTransform(formula[new_sequence[i]], new_formula[i], run_time=0.1) for i in range(len(formula))]
        )

        formula.remove(*formula)
        formula.add(*new_formula)
    


    def multiply_numbers_in_formula(self, formula : Tex or MathTex, number_of_multiplying_items : int, resulting_number : int):
        tex_string_list = [tex.get_tex_string() for tex in formula]

        new_formula = Tex(
            f'{resulting_number}', *tex_string_list[number_of_multiplying_items:],
            font_size=formula[0].font_size, color=formula.color
        )
        new_formula.move_to(formula).align_to(formula, LEFT)

        self.play(
            ReplacementTransform(formula[:number_of_multiplying_items], new_formula[0]),
            ReplacementTransform(formula[number_of_multiplying_items:], new_formula[1:])
        )

        formula.remove(*formula)
        formula.add(*new_formula)

    
    def combine_and_write_power_in_formula(self, formula : Tex or MathTex, first_item_index : int, last_item_index : int, base : str, exponent : int):
        tex_string_list = [tex.get_tex_string() for tex in formula]

        new_formula = Tex(
            *tex_string_list[:first_item_index], base+f'$^{exponent}$', *tex_string_list[last_item_index + 1:],
            font_size=formula[0].font_size, color=formula.color
        )
        new_formula.move_to(formula).align_to(formula, DL)

        self.play(
            ReplacementTransform(formula[:first_item_index], new_formula[:first_item_index]),
            ReplacementTransform(formula[first_item_index : last_item_index + 1], new_formula[first_item_index]),
            ReplacementTransform(formula[last_item_index + 1:], new_formula[first_item_index + 1:])
        )

        formula.remove(*formula)
        formula.add(*new_formula)
