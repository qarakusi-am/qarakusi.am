from manim import Tex, MathTex
from manim import UP, DOWN, LEFT, DL
from manim import Scene
from manim import ReplacementTransform, FadeOut, FadeIn
from manim import VGroup, VMobject
from manim import AnimationGroup


def ExtractExponentInFormula(
    formula : Tex  or MathTex, item_index : int,
    base : str, exponent : str, add_multiplication_signs_in_between=False, base_color=None,
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
            new_items = [f'${base}$', '$\cdot$'] * int(exponent)
            new_items.pop()
        else:
            new_items = [f'${base}$'] * int(exponent)

    elif type(formula) == MathTex:
        if add_multiplication_signs_in_between:
            new_items = [f'{base}', '\cdot'] * int(exponent)
            new_items.pop()
        else:
            new_items = [f'{base}'] * int(exponent)

    new_formula = type(formula)(
        *tex_string_list[:item_index], *new_items, *tex_string_list[item_index + 2:],
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)

    for i in range(item_index):
        new_formula[i].set_color(formula[i].color)

    if not base_color:
        base_color = formula[item_index].color

    if add_multiplication_signs_in_between:
        for i in range(item_index, item_index + 2 * int(exponent), 2):
            new_formula[i].set_color(base_color)
    else:
        for i in range(item_index, item_index + int(exponent)):
            new_formula[i].set_color(base_color)
    
    for i in range(-1, item_index - len(formula) + 1, -1):
        new_formula[i].set_color(formula[i].color)


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
        font_size=formula[0].font_size, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)

    j = 0
    for i in range(len(formula)):
        if i not in items_indices:
            new_formula[j].set_color(formula[i].color)
            j += 1

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


def WriteExponentInFormula(
    formula : Tex  or MathTex, first_item_index : int, 
    last_item_index : int, base : str, exponent : str,
    base_color=None, exponent_color=None,
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

    for i in range(first_item_index + 1):
        new_formula[i].set_color(formula[i].color)
    new_formula[first_item_index + 1].set_color(formula[first_item_index].color)
    if base_color:
        new_formula[first_item_index].set_color(base_color)
        new_formula[first_item_index + 1].set_color(base_color)
    if exponent_color:
        new_formula[first_item_index + 1].set_color(exponent_color)
    for i in range(last_item_index + 1, len(formula)):
        new_formula[i - last_item_index + first_item_index + 1].set_color(formula[i].color)
    

    animations = AnimationGroup(
        ReplacementTransform(formula[:first_item_index], new_formula[:first_item_index], run_time=run_time),
        ReplacementTransform(formula[first_item_index : last_item_index + 1], new_formula[first_item_index : first_item_index + 2], run_time=run_time),
        ReplacementTransform(formula[last_item_index + 1:], new_formula[first_item_index + 2:], run_time=run_time)
    )

    formula.remove(*formula)
    formula.add(*new_formula)

    return animations


def MultiplyNumbersInFormula(
    formula : Tex  or MathTex, number_of_multiplying_items : int, 
    resulting_number_str : str, resulting_number_color=None, run_time=1
):
    """
        Multiplies the numbers in the beginning of the formula 
        number_of_multiplying_items is the number of members in the beginning of the formula
        (including multiplication sign) that need to be transformed into one number
        resulting_number_str is the product that must be written
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]

    if type(formula) == Tex:
        new_item = f'${resulting_number_str}$' if resulting_number_str[0] != '$' else resulting_number_str
    elif type(formula) == MathTex:
        new_item = resulting_number_str if resulting_number_str[0] != '$' else resulting_number_str[1:-1]

    new_formula = type(formula)(
        new_item, *tex_string_list[number_of_multiplying_items:],
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, LEFT)

    if resulting_number_color:
        new_formula[0].set_color(resulting_number_color)
    else:
        new_formula[0].set_color(formula[0].color)

    for i in range(number_of_multiplying_items, len(formula)):
        new_formula[i - number_of_multiplying_items + 1].set_color(formula[i].color)

    animations = AnimationGroup(
        ReplacementTransform(formula[:number_of_multiplying_items], new_formula[0], run_time=run_time),
        ReplacementTransform(formula[number_of_multiplying_items:], new_formula[1:], run_time=run_time)
    )

    formula.remove(*formula)
    formula.add(*new_formula)

    return animations


def CombineTwoExponents(
    formula : Tex or MathTex, bases_indices : list, exponents_indices : list, new_exponent : str, 
    fade_out : list = [], base_color=None, exponent_color=None,
    run_time=1
):
    """
        must be adjacent
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]

    if type(formula) == Tex:
        new_item_exponent = f'$^{new_exponent[1:-1]}$' if new_exponent[0] == '$' else f'$^{new_exponent}$'
    elif type(formula) == MathTex:
        new_item_exponent = f'^{new_exponent[1:-1]}' if new_exponent[0] == '$' else f'^{new_exponent}'

    last_item_index = max(bases_indices + exponents_indices)

    new_formula = type(formula)(
        *tex_string_list[:bases_indices[0] + 1], new_item_exponent, *tex_string_list[last_item_index + 1 :], 
        font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, DL)

    for i in range(bases_indices[0]):
        new_formula[i].set_color(formula[i].color)
    if not base_color:
        base_color = formula[bases_indices[0]].color
    if not exponent_color:
        exponent_color = formula[exponents_indices[0]].color
    new_formula[bases_indices[0]].set_color(base_color)
    new_formula[bases_indices[0] + 1].set_color(exponent_color)

    j = exponents_indices[-1] + 1
    for i in range(exponents_indices[0] + 1, len(new_formula)):
        new_formula[i].set_color(formula[i].color)
        j += 1

    animations = [
        ReplacementTransform(formula[:bases_indices[0]], new_formula[:bases_indices[0]], run_time=run_time),
        ReplacementTransform(VGroup(*[formula[i] for i in exponents_indices]), new_formula[bases_indices[0] + 1], run_time=run_time),
        ReplacementTransform(VGroup(*[formula[i] for i in bases_indices]), new_formula[bases_indices[0]], run_time=run_time),
        ReplacementTransform(formula[last_item_index + 1 :], new_formula[bases_indices[0] + 2 :], run_time=run_time)
    ]

    if len(fade_out) > 0:
        animations.append(FadeOut(*[formula[i] for i in fade_out], run_time=run_time))

    formula.remove(*formula)
    formula.add(*new_formula)

    return AnimationGroup(*animations)


def AddItemsInFormula(
        formula : Tex or MathTex, after_items : list, items_str_list : list, colors : list = [],
        run_time=1
    ):
        """
            Adds items to the formula in after items by fading_in and shifting the rest to the right
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_items = [item if item[0] == '$' else  f'${item}$' for item in items_str_list]

        elif type(formula) == MathTex:
            new_items = [item[1:-1] if item[0] == '$' else item for item in items_str_list]

        new_formula_tex_string_list = [*tex_string_list[:after_items[0] + 1]]
        for i in range(len(new_items) - 1):
            new_formula_tex_string_list.append(new_items[i])
            new_formula_tex_string_list += tex_string_list[after_items[i] + 1 : after_items[i + 1] + 1]
        new_formula_tex_string_list.append(new_items[-1])
        new_formula_tex_string_list += tex_string_list[after_items[-1] + 1 :]
        
        new_formula = type(formula)(
            *new_formula_tex_string_list,
            font_size=formula[0].font_size, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        new_items_indices_in_new_formula = []
        for i in range(len(after_items)):
            new_items_indices_in_new_formula.append(after_items[i] + i + 1)

        j = 0
        if len(colors) > 0:
            for i in new_items_indices_in_new_formula:
                new_formula[i].set_color(colors[j])
                j += 1
        j = 0
        for i in range(len(new_formula)):
            if i not in new_items_indices_in_new_formula:
                new_formula[i].set_color(formula[j].color)
                j += 1

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


def ReplaceItemsInFormula(
    formula : Tex or MathTex, items_indices : list, items_str_list : list, colors : list = [],
    run_time=1
):
    """
        Replaces some items in formula
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]

    if type(formula) == Tex:
        new_items = [item if item[0] == '$' else f'${item}$' for item in items_str_list]

    elif type(formula) == MathTex:
        new_items = [item[1:-1] if item[0] == '$' else item for item in items_str_list]

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
    new_formula.move_to(formula).align_to(formula, DL)

    for i in range(len(formula)):
        new_formula[i].set_color(formula[i].color)
    if len(colors) > 0:
        for i in items_indices:
            new_formula[i].set_color(formula[i])

    animations = [ReplacementTransform(formula[i], new_formula[i], run_time=run_time) for i in range(len(formula))]

    formula.remove(*formula)
    formula.add(*new_formula)

    return AnimationGroup(*animations)


def ModifyFormula(
    formula : Tex or MathTex,
    remove_items : list = [],
    add_after_items : list =[], add_items_strs : list[list] =[], add_items_colors : list[list] = [],
    replace_items : list[list] = [], replace_items_strs  : list[list] = [], replace_items_colors : list[list] = [],
    new_formula_alignment=DL, add_items_animation_style = FadeIn, add_lag_ratio = 0.3
):
    """
        All indices must be indices of original formula
        In each list and sublist indices must be in increasing order
    """
    tex_string_list = [tex.get_tex_string() for tex in formula]
    colors = [item.color for item in formula]

    new_tex_string_list = tex_string_list.copy()
    new_add_after_items = add_after_items.copy()
    new_replace_items = []
    for i in range(len(replace_items)):
        new_replace_items.append(replace_items[i].copy())
    new_colors = colors.copy()

    # remove items
    for i in range(len(remove_items)):
        del new_tex_string_list[remove_items[i] - i]
        del new_colors[remove_items[i] - i]

    # fix indices of add_after_items
    for i in range(len(new_add_after_items)):
        new_add_after_items[i] -= sum(k < new_add_after_items[i] for k in remove_items)

    # fix indices of replace_items
    for i in range(len(new_replace_items)):
        for j in range(len(new_replace_items[i])):
            new_replace_items[i][j] -= sum(k < new_replace_items[i][j] for k in remove_items)

    # insert items
    added_items = []
    for i in range(len(new_add_after_items)):
        subgroup_added_items = []
        for j in range(len(add_items_strs[i])):
            new_tex_string_list.insert(new_add_after_items[i] + 1 + j, add_items_strs[i][j])
            subgroup_added_items.append(new_add_after_items[i] + 1 + j)
        added_items.append(subgroup_added_items)
        for j in range(i + 1, len(new_add_after_items)):
            new_add_after_items[j] += len(add_items_strs[i])
        for j in range(len(new_replace_items)):
            for k in range(len(new_replace_items[j])):
                if new_add_after_items[i] < new_replace_items[j][k]:
                    new_replace_items[j][k] += len(add_items_strs[i])

    # replace items
    replaced_items = []
    for i in range(len(new_replace_items)):
        item_index = new_replace_items[i][0]
        for j in range(len(new_replace_items[i])):
            del new_tex_string_list[item_index]
        for j in range(len(replace_items_strs[i]) - 1, -1, -1):
            new_tex_string_list.insert(item_index, replace_items_strs[i][j])
        for j in range(i, len(new_replace_items)):
            for k in range(len(new_replace_items[j])):
                new_replace_items[j][k] += len(replace_items_strs[i]) - len(new_replace_items[i])
        for j in range(len(added_items)):
            for k in range(len(added_items[j])):
                if added_items[j][k] > item_index:
                    added_items[j][k] += len(replace_items_strs[i]) - len(new_replace_items[i])
        replaced_items.append(list(range(item_index, item_index + len(replace_items_strs[i]))))

    flattened_replaced_items = [item for sublist in replaced_items for item in sublist]
    flattened_added_items = [item for sublist in added_items for item in sublist]
    flattened_replace_items = [item for sublist in replace_items for item in sublist]

    # find indices of fixed item to transformed later
    fixed_items_old = []
    for i in range(len(tex_string_list)):
        if i not in remove_items and i not in flattened_replace_items:
            fixed_items_old.append(i)
    fixed_items_new = []
    for i in range(len(new_tex_string_list)):
        if i not in flattened_added_items and i not in flattened_replaced_items:
            fixed_items_new.append(i)

    new_formula = type(formula)(
        *new_tex_string_list,
        font_size=formula[0].font_size, tex_template=formula.tex_template
    )
    new_formula.move_to(formula).align_to(formula, new_formula_alignment)

    # fix colors
    for i in range(len(fixed_items_old)):
        new_formula[fixed_items_new[i]].set_color(formula[fixed_items_old[i]].color)
    for i in range(len(add_items_colors)):
        for j in range(len(add_items_colors[i])):
            if add_items_colors[i][j]:
                new_formula[added_items[i][j]].set_color(add_items_colors[i][j])
    for i in range(len(replace_items_strs)):
        for j in range(len(replace_items_strs[i])):
            new_formula[replaced_items[i][j]].set_color(formula[replace_items[i][0]].color)
    for i in range(len(replace_items_colors)):
        for j in range(len(replace_items_colors[i])):
            if replace_items_colors[i][j]:
                new_formula[replaced_items[i][j]].set_color(replace_items_colors[i][j])

    # animation groups
    animations = []
    animations += [FadeOut(formula[i]) for i in remove_items]
    animations += [
        ReplacementTransform(formula[replace_items[i][0] : replace_items[i][-1] + 1],
        new_formula[replaced_items[i][0] : replaced_items[i][-1] + 1])
        for i in range(len(replace_items))
    ]
    animations += [
        ReplacementTransform(formula[fixed_items_old[i]], new_formula[fixed_items_new[i]])
        for i in range(len(fixed_items_new))
    ]
    animations_add_items = [add_items_animation_style(new_formula[i]) for i in flattened_added_items]

    formula.remove(*formula)
    formula.add(*new_formula)

    return AnimationGroup(AnimationGroup(*animations), AnimationGroup(*animations_add_items), lag_ratio=add_lag_ratio)


class FormulaModificationsScene(Scene):

    def fix_formula(self, formula : Tex or MathTex):
        """
            fixes formula to work with functions
            don't know why or how it works
        """
        temp_formula = VMobject().add(*formula)
        self.remove(formula)
        self.add(temp_formula)
        formula.remove(*formula)
        formula.add(*temp_formula)


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
            font_size=formula[0].font_size, tex_template=formula.tex_template
        )
        new_formula.move_to(formula)

        colors = [tex.color for tex in formula]
        [new_formula[i].set_color(colors[new_sequence[i]]) for i in range(len(new_formula))]

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
        resulting_number_str : str, resulting_number_color=None, run_time=1
    ):
        """
            Multiplies the numbers in the beginning of the formula 
            number_of_multiplying_items is the number of members in the beginning of the formula
            (including multiplication sign) that need to be transformed into one number
            resulting_number_str is the product that must be written
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_item = f'${resulting_number_str}$' if resulting_number_str[0] != '$' else resulting_number_str
        elif type(formula) == MathTex:
            new_item = resulting_number_str if resulting_number_str[0] != '$' else resulting_number_str[1:-1]

        new_formula = type(formula)(
            new_item, *tex_string_list[number_of_multiplying_items:],
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, LEFT)

        if resulting_number_color:
            new_formula[0].set_color(resulting_number_color)
        else:
            new_formula[0].set_color(formula[0].color)

        for i in range(number_of_multiplying_items, len(formula)):
            new_formula[i - number_of_multiplying_items + 1].set_color(formula[i].color)

        self.play(
            ReplacementTransform(formula[:number_of_multiplying_items], new_formula[0]),
            ReplacementTransform(formula[number_of_multiplying_items:], new_formula[1:]),
            run_time=run_time
        )

        formula.remove(*formula)
        formula.add(*new_formula)


    def write_exponent_in_formula(self,
        formula : Tex  or MathTex, first_item_index : int, 
        last_item_index : int, base : str, exponent : str,
        base_color=None, exponent_color=None,
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

        for i in range(first_item_index + 1):
            new_formula[i].set_color(formula[i].color)
        new_formula[first_item_index + 1].set_color(formula[first_item_index].color)
        if base_color:
            new_formula[first_item_index].set_color(base_color)
            new_formula[first_item_index + 1].set_color(base_color)
        if exponent_color:
            new_formula[first_item_index + 1].set_color(exponent_color)
        for i in range(last_item_index + 1, len(formula)):
            new_formula[i - last_item_index + first_item_index + 1].set_color(formula[i].color)

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
        base : str, exponent : int, add_multiplication_signs_in_between=False, base_color=None,
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

        for i in range(item_index):
            new_formula[i].set_color(formula[i].color)

        if not base_color:
            base_color = formula[item_index].color

        if add_multiplication_signs_in_between:
            for i in range(item_index, item_index + 2 * exponent, 2):
                new_formula[i].set_color(base_color)
        else:
            for i in range(item_index, item_index + exponent):
                new_formula[i].set_color(base_color)
        
        for i in range(-1, item_index - len(formula) + 1, -1):
            new_formula[i].set_color(formula[i].color)

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
        formula : Tex or MathTex, after_items : list, items_str_list : list, colors : list = [],
        run_time=1
    ):
        """
            Adds items to the formula in after items by fading_in and shifting the rest to the right
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_items = [item if item[0] == '$' else f'${item}$' for item in items_str_list]

        elif type(formula) == MathTex:
            new_items = [item[1:-1] if item[0] == '$' else item for item in items_str_list]

        new_formula_tex_string_list = [*tex_string_list[:after_items[0] + 1]]
        for i in range(len(new_items) - 1):
            new_formula_tex_string_list.append(new_items[i])
            new_formula_tex_string_list += tex_string_list[after_items[i] + 1 : after_items[i + 1] + 1]
        new_formula_tex_string_list.append(new_items[-1])
        new_formula_tex_string_list += tex_string_list[after_items[-1] + 1 :]
        
        new_formula = type(formula)(
            *new_formula_tex_string_list,
            font_size=formula[0].font_size, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        new_items_indices_in_new_formula = []
        for i in range(len(after_items)):
            new_items_indices_in_new_formula.append(after_items[i] + i + 1)

        j = 0
        if len(colors) > 0:
            for i in new_items_indices_in_new_formula:
                new_formula[i].set_color(colors[j])
                j += 1
        j = 0
        for i in range(len(new_formula)):
            if i not in new_items_indices_in_new_formula:
                new_formula[i].set_color(formula[j].color)
                j += 1

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
            font_size=formula[0].font_size, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        j = 0
        for i in range(len(formula)):
            if i not in items_indices:
                new_formula[j].set_color(formula[i].color)
                j += 1

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
        formula : Tex or MathTex, bases_indices : list, exponents_indices : list, new_exponent : str, 
        fade_out : list = [], base_color=None, exponent_color=None,
        run_time=1
    ):
        """
            must be adjacent
        """
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_item_exponent = f'$^{new_exponent[1:-1]}$' if new_exponent[0] == '$' else f'$^{new_exponent}$'
        elif type(formula) == MathTex:
            new_item_exponent = f'^{new_exponent[1:-1]}' if new_exponent[0] == '$' else f'^{new_exponent}'

        last_item_index = max(bases_indices + exponents_indices)

        new_formula = type(formula)(
            *tex_string_list[:bases_indices[0] + 1], new_item_exponent, *tex_string_list[last_item_index + 1 :], 
            font_size=formula[0].font_size, color=formula.color, tex_template=formula.tex_template
        )
        new_formula.move_to(formula).align_to(formula, DL)

        for i in range(bases_indices[0]):
            new_formula[i].set_color(formula[i].color)
        if not base_color:
            base_color = formula[bases_indices[0]].color
        if not exponent_color:
            exponent_color = formula[exponents_indices[0]].color
        new_formula[bases_indices[0]].set_color(base_color)
        new_formula[bases_indices[0] + 1].set_color(exponent_color)

        j = exponents_indices[-1] + 1
        for i in range(exponents_indices[0] + 1, len(new_formula)):
            new_formula[i].set_color(formula[i].color)
            j += 1

        if len(fade_out > 0):
            self.play(
                ReplacementTransform(formula[:bases_indices[0]], new_formula[:bases_indices[0]]),
                ReplacementTransform(VGroup(*[formula[i] for i in exponents_indices]), new_formula[bases_indices[0] + 1]),
                ReplacementTransform(VGroup(*[formula[i] for i in bases_indices]), new_formula[bases_indices[0]]),
                ReplacementTransform(formula[last_item_index + 1 :], new_formula[bases_indices[0] + 2 :]),
                FadeOut(*[formula[i] for i in fade_out]),
                run_time=run_time
            )
        else:
            self.play(
                ReplacementTransform(formula[:bases_indices[0]], new_formula[:bases_indices[0]]),
                ReplacementTransform(VGroup(*[formula[i] for i in exponents_indices]), new_formula[bases_indices[0] + 1]),
                ReplacementTransform(VGroup(*[formula[i] for i in bases_indices]), new_formula[bases_indices[0]]),
                ReplacementTransform(formula[last_item_index + 1 :], new_formula[bases_indices[0] + 2 :]),
                run_time=run_time
            )


        formula.remove(*formula)
        formula.add(*new_formula)


    def replace_items_in_formula(self,
        formula : Tex or MathTex, items_indices : list, items_str_list : list, colors : list = [],
        run_time=1
    ):
        tex_string_list = [tex.get_tex_string() for tex in formula]

        if type(formula) == Tex:
            new_items = [item if item[0] == '$' else f'${item}$' for item in items_str_list]

        elif type(formula) == MathTex:
            new_items = [item[1:-1] if item[0] == '$' else item for item in items_str_list]
        
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
        new_formula.move_to(formula).align_to(formula, DL)

        for i in range(len(formula)):
            new_formula[i].set_color(formula[i].color)
        if len(colors) > 0:
            for i in items_indices:
                new_formula[i].set_color(formula[i])

        animations = [ReplacementTransform(formula[i], new_formula[i], run_time=run_time) for i in range(len(formula))]

        self.play(*animations)

        formula.remove(*formula)
        formula.add(*new_formula)
