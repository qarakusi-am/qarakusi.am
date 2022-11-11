import numpy as np
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from manim import Write, Tex, VGroup, FadeIn, Rectangle, Create, AnimationGroup, GrowFromCenter, TransformMatchingTex, GrowArrow, Arrow, SurroundingRectangle, FadeOut, Transform, Indicate, ReplacementTransform
from manim import always_redraw
from manim import UL, DOWN, UP, LEFT, UR, RIGHT, DL, ORIGIN
from manim import LIGHT_BROWN, BLUE, ORANGE, GREEN, WHITE, BLACK
from objects import SimpleSVGMobject, SVGMobject
from .text import *

SMALL_FONT_SIZE = 55
BIG_FONT_SIZE = 75
scale = .6

class PakagceriBacum(FormulaModificationsScene):
    def construct(self):
        self.wait()

        # Անի
        ani_svg = SimpleSVGMobject("girl_3")
        ani_name = Tex(ani_name_str).next_to(ani_svg, DOWN)
        ani_name.set_color_by_gradient("#FF9673", "#E0B851")
        ani = VGroup(ani_svg, ani_name).scale(.6).to_edge(UL).shift(DOWN*.8+LEFT*.2)

        anis_garden = Rectangle(LIGHT_BROWN, 5*scale, 6*scale).next_to(ani, buff=.45, aligned_edge=UP).shift(DOWN*.55)
        anis_carrots = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(30)]).arrange_in_grid(5, 6, buff=.15).move_to(anis_garden.get_center())

        anis_garden_height = Tex("$5$", metr_str, font_size=SMALL_FONT_SIZE).next_to(anis_garden, LEFT).set_color(ORANGE)
        anis_garden_width = Tex("$6$", metr_str, font_size=SMALL_FONT_SIZE).next_to(anis_garden, UP).set_color(GREEN)

        area_of_anis_garden = Tex("$5$", metr_str, "$\\cdot$", "$6$", metr_str, "$=$", "$30$", metr_str, "$^2$", font_size=SMALL_FONT_SIZE).next_to(anis_garden, DOWN, 1)
        area_of_anis_garden[:2].set_color(ORANGE)
        area_of_anis_garden[3:5].set_color(GREEN)
        srr_rect1 = SurroundingRectangle(area_of_anis_garden, BLUE, buff=.2, corner_radius=.3)
        arrow1 = always_redraw(lambda: Arrow(anis_garden.get_bottom(), srr_rect1.get_center()+np.array([0, .35, 0]), max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))

        # Բաբկեն
        babken_svg = SimpleSVGMobject("boy_2")
        babken_name = Tex(babken_name_str).next_to(babken_svg, DOWN)
        babken_name.set_color_by_gradient("#CFC748", "#7FC381")
        babken = VGroup(babken_name, babken_svg).scale(.6).next_to(ani, aligned_edge=DOWN, buff=9)

        babkens_garden = Rectangle(LIGHT_BROWN, 5*scale, 4*scale).next_to(babken, LEFT, buff=.45, aligned_edge=UP).shift(DOWN*.55)
        babkens_carrots = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(20)]).arrange_in_grid(5, 4, buff=.15).move_to(babkens_garden.get_center())
        
        babkens_garden_height = always_redraw(lambda: Tex("$5$", metr_str, font_size=SMALL_FONT_SIZE).next_to(babkens_garden, LEFT).set_color(ORANGE))
        babkens_garden_width = always_redraw(lambda: Tex("$4$", metr_str, font_size=SMALL_FONT_SIZE).next_to(babkens_garden, UP).set_color(GREEN))
        
        area_of_babkens_garden = Tex("$5$", metr_str, "$\\cdot$", "$4$", metr_str, "$=$", "$20$", metr_str, "$^2$", font_size=SMALL_FONT_SIZE).next_to(babkens_garden, DOWN, 1)
        always_redraw(lambda: area_of_babkens_garden[:2].set_color(ORANGE))
        always_redraw(lambda: area_of_babkens_garden[3:5].set_color(GREEN))
        srr_rect2 = SurroundingRectangle(area_of_babkens_garden, BLUE, buff=.2, corner_radius=.3)
        arrow2 = always_redraw(lambda: Arrow(babkens_garden.get_bottom(), srr_rect2.get_center()+np.array([0, .35, 0]), max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))

        # FadeIn Ani and Babken
        self.play(
            FadeIn(ani),
            FadeIn(babken)
        )
        self.wait()

        self.play(
            Create(anis_garden),
            Create(babkens_garden)
        )
        self.wait()

        self.play(
            AnimationGroup(*[GrowFromCenter(babkens_carrots[i]) for i in range(20)], lag_ratio=.8),
            AnimationGroup(*[GrowFromCenter(anis_carrots[i]) for i in range(30)], lag_ratio=.8),
            run_time=5
        )
        self.wait()

        self.play(
            Write(anis_garden_height),
            Write(anis_garden_width)
        )
        self.wait()
        self.play(
            Write(babkens_garden_height),
            Write(babkens_garden_width)
        )
        self.wait()

        self.play(
            TransformMatchingTex(VGroup(anis_garden_height, anis_garden_width).copy(), area_of_anis_garden),
            GrowArrow(arrow1),
            Create(srr_rect1)
        )
        self.wait()
        self.play(
            TransformMatchingTex(VGroup(babkens_garden_height, babkens_garden_width).copy(), area_of_babkens_garden),
            GrowArrow(arrow2),
            Create(srr_rect2)
        )
        self.wait()

        self.play(
            FadeOut(babkens_garden_height),
            VGroup(VGroup(ani, anis_garden, anis_carrots, anis_garden_height, anis_garden_width), VGroup(babken, babkens_garden, babkens_garden, babkens_carrots, babkens_garden_width)).animate.arrange(buff=0).move_to(VGroup(anis_garden, babkens_garden).get_center()).align_to(anis_garden, DOWN)
        )
        plus_tex = Tex("$+$", font_size=SMALL_FONT_SIZE).move_to(VGroup(area_of_anis_garden, area_of_babkens_garden).get_center())
        arrow2.clear_updaters()
        srr_rect2.clear_updaters()
        self.play(
            Write(plus_tex)
        )
        self.wait()

        # ընդամենը՝ 5*10=50մ^2
        arrow1.clear_updaters()
        arrow2.clear_updaters()
        babkens_garden_width.clear_updaters()
        self.play(
            VGroup(
                ani,
                anis_garden,
                anis_carrots,
                area_of_anis_garden,
                anis_garden_height,
                anis_garden_width,
                srr_rect1,
                arrow1,
                babken,
                babkens_garden,
                babkens_carrots,
                area_of_babkens_garden,
                babkens_garden_width,
                arrow2,
                srr_rect2,
                plus_tex
            ).animate.scale(.77).to_edge(UR, buff=.1).shift(DOWN*.1)
        )
        self.wait()

        garden = Rectangle(LIGHT_BROWN, 5*scale*.77, 10*scale*.77).align_to(anis_garden, UL)
        temp = Tex("$6$", metr_str, "$+$", "$4$", metr_str, font_size=SMALL_FONT_SIZE*.77, color=GREEN).next_to(garden, UP)
        self.play(
            FadeOut(
                area_of_anis_garden,
                area_of_babkens_garden,
                srr_rect1,
                srr_rect2,
                arrow1,
                arrow2,
                anis_garden,
                babkens_garden,
                plus_tex
            ),
            FadeIn(
                garden
            ),
            anis_carrots.animate.shift(RIGHT*.1),
            babkens_carrots.animate.shift(LEFT*.1),
            FadeOut(VGroup(anis_garden_width, babkens_garden_width)),
            TransformMatchingTex(VGroup(anis_garden_width, babkens_garden_width).copy(), temp)
        )
        self.wait()
        self.play(Transform(temp, Tex("$10$", metr_str, font_size=SMALL_FONT_SIZE*.77, color=GREEN).next_to(garden, UP)))
        
        all_tex = Tex(all_str, " $5$", metr_str, "$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$", "$=$", "$5$", metr_str, "$\\cdot$", "$10$", metr_str, font_size=SMALL_FONT_SIZE).to_edge(UL, buff=.2)
        all_tex[1:3].set_color(ORANGE)
        all_tex[5:7].set_color(GREEN)
        all_tex[8:10].set_color(GREEN)
        all_tex[-5:-3].set_color(ORANGE)
        all_tex[-2:].set_color(GREEN)
        self.play(
            FadeOut(ani, babken)
        )
        self.play(
            Write(all_tex)
        )
        self.wait()
        self.fix_formula(all_tex)
        self.play(ModifyFormula(all_tex, replace_items=[[12, 13, 14, 15, 16]], replace_items_strs=[["$50$", metr_str, "$^2$"]], replace_items_colors=[[WHITE, WHITE, WHITE]], new_formula_alignment=LEFT))
        self.wait()

        self.play(Indicate(VGroup(garden, anis_carrots, babkens_carrots), color=None))
        self.wait()

        area_of_anis_garden = Tex("$5$", metr_str, " $\\cdot$ ", "$6$", metr_str, font_size=area_of_anis_garden.font_size).next_to(arrow1.get_end(), DOWN)
        area_of_anis_garden[:2].set_color(ORANGE)
        area_of_anis_garden[3:5].set_color(GREEN)
        area_of_babkens_garden = Tex("$5$", metr_str, " $\\cdot$ ", "$4$", metr_str, font_size=area_of_babkens_garden.font_size).next_to(arrow2.get_end(), DOWN)
        area_of_babkens_garden[:2].set_color(ORANGE)
        area_of_babkens_garden[3:5].set_color(GREEN)
        srr_rect1 = SurroundingRectangle(area_of_anis_garden, BLUE, buff=.2, corner_radius=.3)
        srr_rect2 = SurroundingRectangle(area_of_babkens_garden, BLUE, buff=.2, corner_radius=.3)
        self.play(  
            FadeIn(
                area_of_anis_garden,
                area_of_babkens_garden,
                srr_rect1,
                srr_rect2,
                arrow1,
                arrow2,
                anis_garden,
                babkens_garden,
                plus_tex
            ),
            anis_carrots.animate.shift(LEFT*.1),
            babkens_carrots.animate.shift(RIGHT*.1),
            ReplacementTransform(temp, VGroup(anis_garden_width, babkens_garden_width))
        )
        self.remove(garden)
        self.wait()

        self.play(Indicate(VGroup(anis_garden, anis_carrots), color=None))
        self.wait()
        self.play(Indicate(VGroup(babkens_garden, babkens_carrots), color=None))
        self.wait()

        # 5*(6+4) =
        tex1 = Tex("$5$", metr_str, " $\\cdot$ ", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, ")", " $=$" , font_size=SMALL_FONT_SIZE).align_to(all_tex[1], UL)
        tex1[:2].set_color(ORANGE)
        tex1[4:6].set_color(GREEN)
        tex1[7:9].set_color(GREEN)
        self.play(tex1.animate.scale(.77).next_to(srr_rect1, LEFT))
        self.wait()

        # transform 5 to 7
        self.play(
            FadeOut(
                all_tex,
                srr_rect1,
                srr_rect2
            )
        )

        self.play(
            VGroup(
                anis_garden_height,
                anis_garden_width,
                babkens_garden_width,
                anis_garden,
                anis_carrots,
                babkens_garden,
                babkens_carrots,
                tex1,
                area_of_anis_garden,
                area_of_babkens_garden,
                arrow1,
                arrow2,
                plus_tex
            ).animate.move_to(ORIGIN).scale(1.2)
        )
        self.wait()

        self.play(
            anis_garden_height[0].animate.scale(1.5),
            tex1[0].animate.scale(1.3),
            area_of_anis_garden[0].animate.scale(1.3),
            area_of_babkens_garden[0].animate.scale(1.3),
            run_time=2
        )
        self.wait()

        new_anis_garden_height = Tex("$7$", metr_str, font_size=SMALL_FONT_SIZE*.77).align_to(anis_garden_height, UL).shift(UP*.72)
        new_anis_garden_height.set_color(ORANGE)
        temp1 = anis_garden.copy().stretch_to_fit_height(7*scale*.9).align_to(anis_garden, DL)
        temp2 = babkens_garden.copy().stretch_to_fit_height(7*scale*.9).align_to(babkens_garden, DL)
        temp3 = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(12)]).arrange_in_grid(2, 6, buff=.15).next_to(anis_carrots, UP, .05).scale(.924)
        temp4 = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(8)]).arrange_in_grid(2, 4, buff=.15).next_to(babkens_carrots, UP, .05).scale(.924)
        
        self.fix_formula(anis_garden_height)
        self.fix_formula(tex1)
        self.fix_formula(area_of_anis_garden)
        self.fix_formula(area_of_babkens_garden)

        self.play(
            Transform(anis_garden_height, new_anis_garden_height),
            ModifyFormula(tex1, replace_items=[[0]], replace_items_strs=[["$7$"]], new_font_size=tex1[1].font_size, new_formula_alignment=LEFT),
            ModifyFormula(area_of_anis_garden, replace_items=[[0]], replace_items_strs=[["$7$"]], new_font_size=tex1[2].font_size, new_formula_alignment=LEFT),
            ModifyFormula(area_of_babkens_garden, replace_items=[[0]], replace_items_strs=[["$7$"]], new_font_size=tex1[3].font_size, new_formula_alignment=LEFT),
            Transform(anis_garden, temp1),
            Transform(babkens_garden, temp2),
            FadeIn(temp3),
            FadeIn(temp4),
            anis_garden_width.animate.shift(UP),
            babkens_garden_width.animate.shift(UP)
        )
        self.wait()

        # fade out garden
        self.play(
            FadeOut(
                anis_garden, anis_carrots, anis_garden_height, anis_garden_width, babkens_garden, babkens_carrots, babkens_garden_width, temp3, temp4, arrow1, arrow2
            )
        )
        self.wait()
        tex1_copy = Tex("$7$", metr_str, "$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$").match_height(tex1).align_to(tex1, DL)
        tex1_copy[:2].set_color(ORANGE)
        tex1_copy[4:6].set_color(GREEN)
        tex1_copy[7:9].set_color(GREEN)
        equal_tex = Tex("$=$", font_size=BIG_FONT_SIZE/.9).next_to(tex1_copy)
        area_of_anis_garden_copy = area_of_anis_garden.copy().next_to(equal_tex)
        plus_tex_copy = plus_tex.copy().next_to(area_of_anis_garden_copy)
        area_of_babkens_garden_copy = area_of_babkens_garden.copy().next_to(plus_tex_copy)
        temp = VGroup(tex1_copy, equal_tex, area_of_anis_garden_copy, plus_tex_copy, area_of_babkens_garden_copy).move_to(ORIGIN).scale(1.5)
        self.play(
            Transform(VGroup(tex1, area_of_anis_garden, plus_tex, area_of_babkens_garden), temp.remove(equal_tex)),
            FadeIn(equal_tex)
        )
        self.remove(tex1)
        tex1 = tex1_copy
        self.add(tex1)
        self.wait()

        # transform 7 to a
        self.fix_formula(tex1)
        self.fix_formula(area_of_anis_garden)
        self.fix_formula(area_of_babkens_garden)

        self.play(
            tex1[:2].animate.scale(1.3),
            area_of_anis_garden[:2].animate.scale(1.3),
            area_of_babkens_garden[:2].animate.scale(1.3),
            run_time=2
        )

        self.play(
            ModifyFormula(tex1, replace_items=[[0, 1]], replace_items_strs=[["$a$"]], new_formula_alignment=RIGHT, new_font_size=tex1_copy[2].font_size),
            ModifyFormula(area_of_anis_garden, replace_items=[[0, 1]], replace_items_strs=[["$a$"]], new_formula_alignment=RIGHT, new_font_size=area_of_anis_garden[2].font_size),
            ModifyFormula(area_of_babkens_garden, replace_items=[[0, 1]], replace_items_strs=[["$a$"]], new_formula_alignment=RIGHT, new_font_size=area_of_babkens_garden[2].font_size),
            equal_tex.animate.shift(RIGHT*.19),
            plus_tex.animate.shift(RIGHT*.19)
        )
        self.wait()

        # transform 6 to b
        self.fix_formula(tex1)
        self.fix_formula(area_of_anis_garden)

        self.play(
            tex1[3:5].animate.scale(1.3),
            area_of_anis_garden[2:4].animate.scale(1.3),
            run_time=2
        )
        self.wait()

        self.play(
            ModifyFormula(tex1, replace_items=[[3, 4]], replace_items_strs=[["$b$"]], new_formula_alignment=RIGHT),
            ModifyFormula(area_of_anis_garden, replace_items=[[2, 3]], replace_items_strs=[["$b$"]], new_formula_alignment=RIGHT),
            equal_tex.animate.shift(RIGHT*.2),
        )
        self.wait()

        # transform 4 to c
        self.fix_formula(tex1)
        self.fix_formula(area_of_babkens_garden)

        self.play(
            tex1[5:7].animate.scale(1.3),
            area_of_babkens_garden[2:].animate.scale(1.3),
            run_time=2
        )
        self.wait()

        self.play(
            ModifyFormula(tex1, replace_items=[[5, 6]], replace_items_strs=[["$c$"]], new_formula_alignment=RIGHT),
            ModifyFormula(area_of_babkens_garden, replace_items=[[2, 3]], replace_items_strs=[["$c$"]], new_formula_alignment=RIGHT),
            plus_tex.animate.shift(RIGHT*.2)
        )
        self.wait()

        # examples
        # 2x(3y+5)=2x*3y+2x*5=6x+10x
        formula = VGroup(tex1, equal_tex, area_of_anis_garden, plus_tex, area_of_babkens_garden)
        self.play(formula.animate.to_edge(UP))
        self.wait()

        example1 = Tex("$2x$", "$\\cdot$", "$($", "$3y$", "$+$", "$5$", "$)$", font_size=BIG_FONT_SIZE).next_to(formula, DOWN, 1, LEFT)
        example1[0].set_color(ORANGE)
        example1[3].set_color(GREEN)
        example1[5].set_color(GREEN)
        self.play(Write(example1))
        self.wait()

        arrow1 = Arrow(tex1[0].get_center()+np.array([-.1, 0, 0]), example1[0].get_center(), buff=.4)
        arrow3 = Arrow(tex1[5].get_center(), example1[5].get_center(), buff=.4)
        arrow2 = Arrow(tex1[3].get_center(), example1[3].get_center(), buff=.4)
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait()
        
        self.fix_formula(example1)
        self.play(ModifyFormula(example1, add_after_items=[6], add_items_strs=[[" $=$ ", "$2x$", "$\\cdot$", "$3y$"]], add_items_colors=[[None, ORANGE, None, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(example1, add_after_items=[10], add_items_strs=[["$+$", "$2x$", "$\\cdot$", "$5$"]], add_items_colors=[[None, ORANGE, None, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.play(
            example1.animate.to_edge(LEFT),
            FadeOut(arrow1, arrow2, arrow3)
        )
        self.wait()
        self.fix_formula(example1)
        self.play(ModifyFormula(example1, add_after_items=[14], add_items_strs=[[" $=$ ", "$6xy$"]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(example1, add_after_items=[16], add_items_strs=[["$+$", "$10x$"]], add_items_animation_style=Write))
        self.wait()

        # 3k(4l+6z)=12kl+18kz
        self.play(example1.animate.shift(DOWN*3.5))
        self.wait()

        example2 = Tex("$3k$", "$\\cdot$", "$($", "$4l$", "$+$", "$6z$", "$)$", font_size=BIG_FONT_SIZE).next_to(formula, DOWN, 1, LEFT)
        example2[0].set_color(ORANGE)
        example2[3].set_color(GREEN)
        example2[5].set_color(GREEN)
        self.play(Write(example2))
        self.wait()

        arrow1 = Arrow(tex1[0].get_center(), example2[0].get_center(), buff=.4)
        arrow3 = Arrow(tex1[5].get_center(), example2[5].get_center(), buff=.4)
        arrow2 = Arrow(tex1[3].get_center(), example2[3].get_center(), buff=.4)
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait()
        
        self.fix_formula(example2)
        self.play(ModifyFormula(example2, add_after_items=[6], add_items_strs=[[" $=$ ", "$3k$", "$\\cdot$", "$4l$"]], add_items_colors=[[None, ORANGE, None, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(example2, add_after_items=[10], add_items_strs=[["$+$", "$3k$", "$\\cdot$", "$6z$"]], add_items_colors=[[None, ORANGE, None, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.play(
            example2.animate.to_edge(LEFT, buff=.18),
            FadeOut(arrow1, arrow2, arrow3)
        )
        self.wait()
        self.fix_formula(example2)
        self.play(ModifyFormula(example2, add_after_items=[14], add_items_strs=[[" $=$ ", "$12kl$"]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(example2, add_after_items=[16], add_items_strs=[["$+$", "$18kz$"]], add_items_animation_style=Write))
        self.wait()

        # task
        # 2x^2(3x+1)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.wait()

        task = Tex("$2$", "$x$", "$^2$", " $\\cdot$ " "$($", "$3$", "$x$", " $+$ ", "$1$", "$)$", font_size=BIG_FONT_SIZE).scale(1.5)
        task[:3].set_color(ORANGE)
        task[4:6].set_color(GREEN)
        task[7].set_color(GREEN)
        self.play(Write(task))

        self.wait(2)
