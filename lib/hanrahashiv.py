from manim import Tex, MathTex
from manim import UP, DOWN, DL
from manim import Scene
from manim import ReplacementTransform, FadeOut, FadeIn
from manim import VMobject
from manim import AnimationGroup
from typing import List

def ModifyFormula(
    formula : Tex or MathTex,
    remove_items : List = [],
    add_after_items : List =[], add_items_strs : List[List] =[], add_items_colors : List[List] = [],
    replace_items : List[List] = [], replace_items_strs  : List[List] = [], replace_items_colors : List[List] = [],
    new_formula_alignment=DL, add_items_animation_style = FadeIn, add_lag_ratio = 0.3, new_font_size=None,
    move_to=None
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
        new_tex_string_list = new_tex_string_list[:item_index] + new_tex_string_list[new_replace_items[i][-1] + 1:]  # remove old items
        new_tex_string_list = new_tex_string_list[:item_index] + replace_items_strs[i] + new_tex_string_list[item_index:] # add new items
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

    if not new_font_size:
        new_font_size = formula[0].font_size

    new_formula = type(formula)(*new_tex_string_list, font_size=new_font_size, tex_template=formula.tex_template)
    
    # move_to
    if move_to is not None:
        new_formula.move_to(move_to)
    else:
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
            fixes formula to work with ModifyFormula
            don't know why or how it works
        """
        temp_formula = VMobject().add(*formula)
        self.remove(formula)
        self.add(temp_formula)
        formula.remove(*formula)
        formula.add(*temp_formula)

    def rearrange_formula(self,
        formula : Tex or MathTex, new_sequence : List,
        move_up : List = [], move_down : List = [],
        fade_out : List = [], fade_in : List = [],
        remove : List = [],
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
        [tex_string_list.pop(i) for i in remove]

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
            *[formula[i].animate.set_opacity(0) for i in remove],
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
            *[ReplacementTransform(formula[new_sequence[i]], new_formula[i], run_time=0.1) for i in range(len(new_formula))]
        )

        self.remove(*[formula[i] for i in remove])
        formula.remove(*formula)
        formula.add(*new_formula)
