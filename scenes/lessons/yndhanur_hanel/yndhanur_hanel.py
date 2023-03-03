from manim import Scene, MathTex, Write, Transform, ReplacementTransform, VGroup, Indicate, Tex, FadeOut, AnimationGroup, SurroundingRectangle, Create
from manim import LEFT, DOWN, UP, ORIGIN, RIGHT
from manim import YELLOW, GREEN
from objects import SimpleSVGMobject
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from .text import *

FONT_SIZE = 175
SMALL_FONT_SIZE = 100

class Yndhanur_hanel(FormulaModificationsScene):
    def construct(self):
        self.wait()

        task = MathTex("6", "\\cdot", "8", "+", "6", "\\cdot", "12", font_size=FONT_SIZE)
        self.play(Write(task))
        self.wait()

        self.play(VGroup(task[0], task[4]).animate.set_color(YELLOW))
        self.play(
            Indicate(task[0], color=YELLOW),
            Indicate(task[4], color=YELLOW)
        )
        self.wait()

        egg_carton_svg = SimpleSVGMobject("egg_carton_2").scale(.7)
        egg_carton1 = egg_carton_svg.copy().move_to(task[0].get_center())
        egg_carton2 = egg_carton_svg.copy().move_to(task[4].get_center())

        self.play(
            Transform(task[0], egg_carton1),
            Transform(task[4], egg_carton2)
        )
        self.wait()

        self.play(task.animate.to_edge(UP))

        egg_cartons8 = VGroup(*[egg_carton_svg.copy().scale(.7) for _ in range(8)])
        egg_cartons8.arrange_in_grid(3, 3, flow_order="ld")

        egg_cartons12 = VGroup(*[egg_carton_svg.copy().scale(.7) for _ in range(12)])
        egg_cartons12.arrange_in_grid(3, 4)
        egg_cartons12.next_to(egg_cartons8, buff=2.5)

        VGroup(egg_cartons8, egg_cartons12).move_to(ORIGIN).shift(DOWN*.3)

        self.play(
            ReplacementTransform(task[2].copy(), egg_cartons8)
        )
        self.wait()
        egg_cartons8_tex = Tex("$8$", carton_str, font_size=SMALL_FONT_SIZE)
        egg_cartons8_tex.next_to(egg_cartons8, DOWN)
        self.play(Write(egg_cartons8_tex))
        self.wait()

        self.play(
            ReplacementTransform(task[6].copy(), egg_cartons12)
        )
        self.wait()
        egg_cartons12_tex = Tex("$12$", carton_str, font_size=SMALL_FONT_SIZE)
        egg_cartons12_tex.next_to(egg_cartons12, DOWN)
        self.play(Write(egg_cartons12_tex))
        self.wait()

        plus_tex = MathTex("+", font_size=SMALL_FONT_SIZE)
        plus_tex.move_to(VGroup(egg_cartons8_tex, egg_cartons12_tex).get_center())
        plus_tex.next_to(egg_cartons8_tex).shift(LEFT)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    egg_cartons12_tex.animate.next_to(plus_tex, RIGHT),
                    egg_cartons8.animate.next_to(egg_cartons12, LEFT, buff=1.35),
                    egg_cartons12.animate.next_to(egg_cartons8, buff=1.35),
                    egg_cartons8_tex.animate.shift(LEFT)
                ),
                Write(plus_tex),
                lag_ratio=.6
            )
        )

        total_egg_cartons_tex = Tex("$= 20$", carton_str, font_size=SMALL_FONT_SIZE)
        total_egg_cartons_tex.next_to(egg_cartons12_tex)
        self.play(Write(total_egg_cartons_tex))
        self.wait()

        self.play(task.animate.scale(.7).to_edge(LEFT).shift(LEFT*.4))
        self.wait()

        equal = MathTex("=", font_size=FONT_SIZE).scale(.7)
        equal.next_to(task, buff=.35)
        self.play(Write(equal))
        self.wait()
        
        task_2nd_part = Tex("$6$  ", "$\\cdot$", "$20$", font_size=FONT_SIZE).scale(.7)
        task_2nd_part.next_to(equal, buff=0.6)
        task_2nd_part[0].set_color(YELLOW)
        egg_carton3 = egg_carton_svg.copy().move_to(task_2nd_part[0].get_center()).scale(.8)
        self.play(Write(egg_carton3))
        self.play(Write(task_2nd_part[1:]))
        self.wait()

        self.play(FadeOut(egg_cartons8, egg_cartons12))
        self.wait()

        self.play(
            VGroup(
                egg_cartons8_tex,
                plus_tex,
                egg_cartons12_tex,
                total_egg_cartons_tex
            ).animate.shift(UP*2)
        )
        self.wait()

        self.play(Indicate(task_2nd_part[-1]))
        self.wait()
        self.play(
            Indicate(egg_cartons8_tex[0]),
            Indicate(egg_cartons12_tex[0])
        )
        self.wait()

        tex1 = MathTex("(", "8", "+", "12", ")", font_size=FONT_SIZE).scale(.65)
        tex1.move_to(task_2nd_part[-1].get_center()).align_to(task_2nd_part[-1], LEFT).shift(DOWN*.1)
        self.play(Transform(task_2nd_part[-1], tex1))
        self.add(tex1)
        self.remove(task_2nd_part[-1])
        self.wait()
        
        temp1 = task_2nd_part[0].copy().move_to(task[0].get_center())
        temp2 = task_2nd_part[0].copy().move_to(task[4].get_center())
        self.play(
            Transform(task[0], temp1),
            Transform(task[4], temp2),
            ReplacementTransform(egg_carton3, task_2nd_part[0]),
            ReplacementTransform(egg_carton3, task_2nd_part[0]),
            FadeOut(egg_cartons8_tex, plus_tex, egg_cartons12_tex, total_egg_cartons_tex),
            equal.animate.shift(RIGHT*.18),
            task_2nd_part[1].animate.shift(LEFT*.18)
        )
        self.wait()
        
        self.play(
            VGroup(
                task,
                equal,
                task_2nd_part[:-1],
                tex1
            ).animate.move_to(ORIGIN)
        )
        self.wait()

        self.play(
            Indicate(task[0]),
            Indicate(task[4]),
            Indicate(task_2nd_part[0])
        )
        self.wait()

        self.fix_formula(task)
        self.play(
            ModifyFormula(
                task,
                replace_items=[[0], [4]],
                replace_items_strs=[["a"], ["a"]],
                replace_items_colors=[[YELLOW], [YELLOW]]
            ),
            Transform(
                task_2nd_part[0],
                MathTex("a", font_size=FONT_SIZE, color=YELLOW).scale(.7).move_to(task_2nd_part[0].get_center()).shift(DOWN*.1)
            )
        )
        self.wait()

        self.play(
            Indicate(task[2]),
            Indicate(tex1[1])
        )
        self.wait()
        
        self.fix_formula(task)
        self.fix_formula(tex1)
        self.play(
            ModifyFormula(
                task,
                replace_items=[[2]],
                replace_items_strs=[["b"]]
            ),
            ModifyFormula(
                tex1,
                replace_items=[[1]],
                replace_items_strs=[["b"]]
            )
        )
        self.wait()

        self.play(
            Indicate(task[-1]),
            Indicate(tex1[-2])
        )
        self.wait()
        
        self.fix_formula(task)
        self.fix_formula(tex1)

        self.play(
            ModifyFormula(
                task,
                replace_items=[[6]],
                replace_items_strs=[["c"]]
            ),
            ModifyFormula(
                tex1,
                replace_items=[[3]],
                replace_items_strs=[["c"]]
            ),
            equal.animate.shift(DOWN*.1 + LEFT*.35)
        )
        self.wait()

        formula = VGroup(
            task,
            equal,
            task_2nd_part[:2],
            tex1
        )

        self.play(
            formula.animate.move_to(ORIGIN)
        )
        srr_rect = SurroundingRectangle(formula, GREEN, buff=.25)
        self.play(Create(srr_rect))

        self.wait(2)