from manim import Circle, Tex, Write, FadeIn, SurroundingRectangle, VGroup, Create, Arrow, GrowArrow, ReplacementTransform, FadeOut, Brace, GrowFromCenter, ValueTracker
from manim import always_redraw
from manim import GREEN
from manim import UP, LEFT, UR, DOWN, ORIGIN, RIGHT
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from qarakusiscene import TaskNumberBox
from objects import SimpleSVGMobject
from .text import *

FONT_SIZE = 90

class Problem12723(FormulaModificationsScene):
    """Փչած ֆուտբոլի գնդակը պարունակում է 450 գրամ օդ։ Հայտնի է, որ 1գ օդում կա մոտ 2⋅1022 հատ մոլեկուլ։ Քանի՞ հատ մոլեկուլ կա փչած ֆուտբոլի գնդակի ներսում։"""
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))
        self.wait()

        ball = SimpleSVGMobject("football_1").scale(1.2)
        self.play(FadeIn(ball))
        self.wait()

        air_mass = Tex("450", air_mass_str, font_size=FONT_SIZE)
        air_mass.to_edge(UP)
        self.play(Write(air_mass))
        self.wait()

        arrow = Arrow(start=air_mass.get_bottom(), end=ball.get_top(), stroke_width=15, max_tip_length_to_length_ratio=.4)
        self.play(GrowArrow(arrow))
        self.wait()

        self.play(VGroup(air_mass, arrow, ball).animate.scale(.7).to_edge(LEFT))
        self.wait()

        molecules_in_one_gram = Tex(molecules_in_one_gram_str, font_size=.6*FONT_SIZE)
        molecules_in_one_gram.to_corner(UR).shift(UP*.1)
        srr_rect = SurroundingRectangle(molecules_in_one_gram, buff=.1, color=GREEN)
        self.play(
            FadeIn(molecules_in_one_gram),
            Create(srr_rect)
        )
        self.wait()

        molecules_in_ball = Tex(*molecules_in_ball_str, font_size=FONT_SIZE)
        molecules_in_ball.next_to(ball).shift(molecules_in_ball_shift)
        temp = air_mass[0].copy()
        self.play(Write(molecules_in_ball[0]))
        self.play(
            ReplacementTransform(temp, molecules_in_ball[1]),
            FadeOut(air_mass, arrow)
        )
        self.play(Write(molecules_in_ball[2:]))
        self.wait()

        self.fix_formula(molecules_in_ball)
        self.play(
            FadeOut(ball, srr_rect, molecules_in_one_gram),
            ModifyFormula(molecules_in_ball, [0, 6], move_to=ORIGIN)
        )
        self.wait()

        self.play(
            ModifyFormula(
                molecules_in_ball,
                replace_items=[[0, 1, 2]],
                replace_items_strs=[["$9$", "$0$","$0$"]],
                new_formula_alignment=ORIGIN
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                molecules_in_ball,
                replace_items=[[4]],
                replace_items_strs=[["1", "$0$"*22]],
                new_formula_alignment=ORIGIN
            )
        )
        self.wait()

        val_tracker = ValueTracker(11)
        brace = Brace(molecules_in_ball[-1], DOWN)
        brace_label = always_redraw(lambda: brace.get_tex(f"{int(val_tracker.get_value())*2} \\text{{{hat_str}}}").scale(1.7))
        self.play(
            GrowFromCenter(brace),
            Write(brace_label)
        )
        self.wait()

        self.play(
            ModifyFormula(
                molecules_in_ball,
                [1, 2],
                add_after_items=[len(molecules_in_ball)-1],
                add_items_strs=[["$00$"]],
                add_items_animation_style=Write
            ),
            val_tracker.animate.set_value(12),
            brace.animate.stretch_to_fit_width(molecules_in_ball[-2:].width).align_to(brace, RIGHT)
        )
        self.wait()

        brace_label.clear_updaters()

        self.fix_formula(molecules_in_ball)
        self.play(
            ModifyFormula(
                molecules_in_ball,
                add_after_items=[len(molecules_in_ball)-1],
                add_items_strs=[[" $= 9 \cdot 10^{24}$"]],
                new_font_size=FONT_SIZE*.8,
                add_items_animation_style=Write,
                new_formula_alignment=ORIGIN
            ),
            VGroup(brace, brace_label).animate.scale(.8).shift(LEFT*1.86+UP*.12)
        )
        self.wait()

        self.play(FadeOut(brace, brace_label))
        self.wait()

        self.play(molecules_in_ball.animate.shift(UP*1.5))

        tex = Tex("$900$", " $\cdot$ ", "$10^{22}$", font_size=FONT_SIZE)
        tex.next_to(molecules_in_ball, DOWN, buff=1)
        self.play(Write(tex))
        self.wait()

        self.fix_formula(tex)
        self.play(
            ModifyFormula(
                tex,
                replace_items=[[0]],
                replace_items_strs=[["$9$", " $\cdot$ ", "$100$"]],
                new_formula_alignment=ORIGIN
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                tex,
                replace_items=[[2]],
                replace_items_strs=[["$10^{2}$"]]
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                tex,
                add_after_items=[4],
                add_items_strs=[[" $= 9$ $\cdot$ ", "$10^{2+22}$"]],
                new_formula_alignment=ORIGIN,
                add_items_animation_style=Write
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                tex,
                replace_items=[[6]],
                replace_items_strs=[["$10^{24}$"]],
                new_formula_alignment=ORIGIN
            )
        )

        self.wait(2)
