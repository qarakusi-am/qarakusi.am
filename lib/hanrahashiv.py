from manim import Tex, MathTex
from manim import UP, DOWN, LEFT, DL
from manim import Scene
from manim import ReplacementTransform, FadeOut, FadeIn

class FormulaModifications(Scene):

# FIXME մարդավարի docstring գրել ամեն ֆունկցիայի համար
#  միգուցե էս ամենը տեղափոխել QarakusiScene (որտև մենակ միանդամների մեջ չի, որ պետք կգան)
    """
        new_sequence addresses each of formula's item to it's new position, including '$\cdot$', ' + '
        new_sequence is a permutation of range(len(formula))
        to work properly, formula must be written in such a way that every item is in different apostrophes like so
        formula = Tex('a', '$\cdot$', 'b')
    """

    def rearrange_formula(self,
        formula : MathTex or Tex, new_sequence : list, 
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
        new_formula = type(formula)(*new_tex_string_list, font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template)
        new_formula.move_to(formula)

        in_line = []
        for i in range(len(tex_string_list)):
            if i not in move_up and i not in move_down: #and i not in fade_out: # i not in fade_in and
                in_line.append(i)

        self.play(
            *[formula[i].animate.shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.set_opacity(0) for i in fade_out],
            run_time=run_time / 3
        )
        self.play(
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * UP) for i in move_up],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]).shift(0.5 * DOWN) for i in move_down],
            *[formula[i].animate.move_to(new_formula[new_sequence.index(i)]) for i in in_line],
            run_time=run_time / 3
        )
        self.play(
            *[formula[i].animate.shift(0.5 * DOWN) for i in move_up],
            *[formula[i].animate.shift(0.5 * UP) for i in move_down],
            *[FadeIn(new_formula[i]) for i in fade_in],
            run_time=run_time / 3
        )
        self.play(
            *[ReplacementTransform(formula[new_sequence[i]], new_formula[i], run_time=0.1) for i in range(len(formula))]
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def multiply_numbers_in_formula(self,
        formula : MathTex, number_of_multiplying_items : int, 
        resulting_number : int, run_time=1
    ):
        """
            Multiplies the numbers in the beginning of the formula 
            number_of_multiplying_items is the number of members in the beginning of the formula
            (including multiplication sign) that need to be transformed into one number
            resulting_number is the product that must be written
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]
        new_formula = type(formula)(
            f'{resulting_number}', *tex_string_list[number_of_multiplying_items:],
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


    def write_exponents_in_formula(self,
        formula : MathTex, first_item_index : int, 
        last_item_index : int, base : str, exponent : int,
        run_time=1
    ):
        """
            Combines adjacent same letters and writes in form of exponent
            takes indices of items to be combined, base and exponent and
            formula[first_item_index : last_item_index + 1] transforms into base^exponent
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]
        new_formula = type(formula)(
            *tex_string_list[:first_item_index], f'${base}$'+f'$^{exponent}$', *tex_string_list[last_item_index + 1:],
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        self.play(
            ReplacementTransform(formula[:first_item_index], new_formula[:first_item_index]),
            ReplacementTransform(formula[first_item_index : last_item_index + 1], new_formula[first_item_index]),
            ReplacementTransform(formula[last_item_index + 1:], new_formula[first_item_index + 1:]),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)
