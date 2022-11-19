from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from manim import FadeIn, Tex, Write, Indicate, CounterclockwiseTransform, AnimationGroup, FadeOut, ReplacementTransform, Transform, SurroundingRectangle, VGroup
from manim import ORIGIN, DOWN, LEFT, UL, DR, UR
from manim import ORANGE, GREEN, BLUE
from .text import *

BIG_FONT_SIZE = 70

class Problem12658(FormulaModificationsScene):
    def construct(self):
        self.wait()
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # a(b+c) = ab+ ac
        pakagceri_bacum_tex = Tex("$a$", "$($", "$b$", "$+$", "$c$", "$)$", " $=$ ", "$a$", "$b$", " $+$ ", "$a$", "$c$", font_size=BIG_FONT_SIZE)
        pakagceri_bacum_tex.set_color_by_tex("a", BLUE)
        pakagceri_bacum_srr_rect = SurroundingRectangle(pakagceri_bacum_tex, color=GREEN)
        pakagceri_bacum = VGroup(pakagceri_bacum_tex, pakagceri_bacum_srr_rect).to_edge(UR)
        self.play(FadeIn(pakagceri_bacum))
        self.wait()
        self.play(Indicate(pakagceri_bacum))
        self.wait()
        
        formula = Tex("$2$", "$x$", "$($", "$4$", "$x$", "$+$", "$3$", "$)$", " $=$ ", "$2$", "$x$", "$\\cdot$", "$4$", "$x$", " $+$ ", "$2$", "$x$", "$\\cdot$", "$3$", " $=$ ", "$8$", "$x$", "$^2$", " $+$ " "$6$", "$x$", font_size=BIG_FONT_SIZE)
        formula.set_color_by_tex("3", GREEN)
        formula[:2].set_color(ORANGE)
        formula[3:5].set_color(GREEN)
        formula[9:11].set_color(ORANGE)
        formula[12:14].set_color(GREEN)
        formula[15:17].set_color(ORANGE)
        self.play(Write(formula[:8]))
        self.wait()

        temp1 = formula[:2].copy()
        temp2 = formula[3:5].copy()
        self.play(
            AnimationGroup(
                Write(formula[8], run_time=.5),
                CounterclockwiseTransform(temp1, formula[9:11]),
                Write(formula[11], run_time=.5),
                CounterclockwiseTransform(temp2, formula[12:14])
            )
        )
        self.add(
            formula[9:11],
            formula[11:14]
        )
        self.remove(
            temp1,
            temp2
        )
        self.wait()

        temp1 = formula[:2].copy()
        temp2 = formula[6].copy()
        self.play(
            AnimationGroup(
                Write(formula[14], run_time=.5),
                CounterclockwiseTransform(temp1, formula[15:17]),
                Write(formula[17], run_time=.5),
                CounterclockwiseTransform(temp2, formula[18]),
            )
        )
        self.add(
            formula[15:17],
            formula[18]
        )
        self.remove(
            temp1,
            temp2
        )
        self.wait()

        self.play(Write(formula[19:23]))
        self.wait()

        self.play(Write(formula[23:]))
        self.wait()

        self.rearrange_formula(
            formula,
            [20, 21, 22, 23, 24, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7],
            move_up=[20, 21, 22, 23, 24],
            move_down=[0, 1, 2, 3, 4, 5, 6, 7])
        self.wait()

        self.play(
            Indicate(formula[6:11]),
            Indicate(formula[12:16])
        )
        self.wait()

        self.play(
            formula[6:8].animate.scale(1.3),
            formula[12:14].animate.scale(1.3)
        )
        self.wait()

        self.play(FadeOut(formula))
        self.wait()

        # task 1
        # task1 = Tex("1. ", "$x$", "$^2$", " $+$ ", "$4$", "$\\cdot$", "$x$", " $=$ ", "$x$", "$\\cdot$", "$x$", " $+$ ", "$x$", "$\\cdot$", "$4$", font_size=BIG_FONT_SIZE)
        task1 = Tex("1. ", "$x$", "$^2$", " $+$ ", "$4$", "$\\cdot$", "$x$", font_size=BIG_FONT_SIZE)
        task1.to_edge(UL, buff=.5).shift(DOWN*.8)
        self.play(Write(task1))
        self.wait()

        task1_copy = Tex(*[symbol.get_tex_string() for symbol in task1[1:]])
        task1_copy.match_height(task1)
        task1_copy.align_to(task1, DR)
        self.play(task1_copy.animate.shift(DOWN))
        self.wait()

        self.fix_formula(task1_copy)
        self.play(
            ModifyFormula(
                task1_copy,
                replace_items=[[0, 1]],
                replace_items_strs=[["$x$", "$\\cdot$", "$x$"]]
            )
        )
        self.wait()

        self.play(
            task1_copy[0].animate.set_color(GREEN),
            task1_copy[6].animate.set_color(GREEN)
        )
        self.wait()

        self.rearrange_formula(
            task1_copy,
            [0, 1, 2, 3, 6, 5, 4],
            move_up=[6],
            move_down=[4]
        )
        self.wait()

        self.play(Indicate(pakagceri_bacum))
        self.wait()

        self.play(
            ModifyFormula(
                task1_copy,
                replace_items=[[1]],
                replace_items_strs=[["$($"]],
                remove_items=[4, 5],
                add_after_items=[6],
                add_items_strs=[["$)$"]],
                new_formula_alignment=LEFT
            )
        )

        self.fix_formula(task1)
        self.play(
            ModifyFormula(
                task1,
                add_after_items=[6],
                add_items_strs=[[" $=$"]]
            )
        )
        temp = task1_copy.copy().next_to(task1)
        self.play(CounterclockwiseTransform(task1_copy, temp))

        self.wait(2)