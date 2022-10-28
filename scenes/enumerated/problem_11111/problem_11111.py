import numpy as np
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from manim import Write, Tex, VGroup, FadeIn, Rectangle, Create, AnimationGroup, GrowFromCenter, TransformMatchingTex, GrowArrow, Arrow, SurroundingRectangle, FadeOut, always_redraw, Group, Indicate
from manim import UL, DOWN, UP, LEFT, UR, RIGHT, ORIGIN
from manim import LIGHT_BROWN, BLUE, ORANGE, GREEN
from objects import SimpleSVGMobject, SVGMobject
from .text import *

FONT_SIZE = 55
scale = .6

class Problem11111(FormulaModificationsScene):
    def construct(self):
        self.wait()
        tasknumber = TaskNumberBox(task_number_string)
        self.play(FadeIn(tasknumber))
        self.wait()

        # formula = Tex("$a$", "$($" "$b$", "$+$", "$c$", "$)$" " $=$ ", "$a$", "$b$", "$+$", "$a$", "$c$", font_size=FONT_SIZE)
        # self.play(Write(formula))
        # self.wait()
        # self.play(formula.animate.to_edge(UL, buff=.7).shift(DOWN*.4))

        # Անի
        ani_svg = SimpleSVGMobject("girl_3")
        ani_name = Tex(ani_name_str).next_to(ani_svg, DOWN)
        ani_name.set_color_by_gradient("#FF9673", "#E0B851")
        ani = VGroup(ani_svg, ani_name)
        self.play(FadeIn(ani))
        self.wait()
        self.play(ani.animate.scale(.6).to_edge(UL).shift(DOWN*.8+LEFT*.2))
        self.wait()

        anis_garden = Rectangle(LIGHT_BROWN, 5*scale, 6*scale).next_to(ani, buff=.45, aligned_edge=UP).shift(DOWN*.55)
        self.play(Create(anis_garden))
        self.wait()
        anis_carrots = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(30)]).arrange_in_grid(5, 6, buff=.15).move_to(anis_garden.get_center())
        self.play(AnimationGroup(*[GrowFromCenter(anis_carrots[i]) for i in range(30)], lag_ratio=.8), run_time=5)
        self.wait()

        anis_garden_height = Tex("$5$", metr_str, font_size=FONT_SIZE).next_to(anis_garden, LEFT).set_color(ORANGE)
        anis_garden_width = Tex("$6$", metr_str, font_size=FONT_SIZE).next_to(anis_garden, UP).set_color(GREEN)
        self.play(
            Write(anis_garden_height),
            Write(anis_garden_width)
        )
        self.wait()

        area_of_anis_garden = Tex("$5$", metr_str, "$\\cdot$", "$6$", metr_str, "$=$", "$30$", metr_str, "$^2$", font_size=FONT_SIZE).next_to(anis_garden, DOWN, 1)
        area_of_anis_garden[:2].set_color(ORANGE)
        area_of_anis_garden[3:5].set_color(GREEN)
        srr_rect1 = SurroundingRectangle(area_of_anis_garden, BLUE, buff=.2, corner_radius=.3)
        arrow1 = always_redraw(lambda: Arrow(anis_garden.get_bottom(), srr_rect1.get_center()+np.array([0, .35, 0]), max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))
        self.play(
            TransformMatchingTex(VGroup(anis_garden_height, anis_garden_width).copy(), area_of_anis_garden),
            GrowArrow(arrow1),
            Create(srr_rect1)
        )
        self.wait()

        # Բաբկեն
        babken_svg = SimpleSVGMobject("boy_2")
        babken_name = Tex(babken_name_str).next_to(babken_svg, DOWN)
        babken_name.set_color_by_gradient("#CFC748", "#7FC381")
        babken = VGroup(babken_name, babken_svg).scale(.6).next_to(ani, aligned_edge=DOWN, buff=9)
        self.play(FadeIn(babken))
        self.wait()

        babkens_garden = Rectangle(LIGHT_BROWN, 5*scale, 4*scale).next_to(babken, LEFT, buff=.45, aligned_edge=UP).shift(DOWN*.55)
        self.play(Create(babkens_garden))
        self.wait()
        babkens_carrots = VGroup(*[SVGMobject("objects/SVG_files/fruits/carrot.svg").scale(.2) for _ in range(20)]).arrange_in_grid(5, 4, buff=.15).move_to(babkens_garden.get_center())
        self.play(AnimationGroup(*[GrowFromCenter(babkens_carrots[i]) for i in range(20)], lag_ratio=.8), run_time=5)
        self.wait()

        babkens_garden_height = always_redraw(lambda: Tex("$5$", metr_str, font_size=FONT_SIZE).next_to(babkens_garden, LEFT).set_color(ORANGE))
        babkens_garden_width = always_redraw(lambda: Tex("$4$", metr_str, font_size=FONT_SIZE).next_to(babkens_garden, UP).set_color(GREEN))
        self.play(
            Write(babkens_garden_height),
            Write(babkens_garden_width)
        )
        self.wait()

        area_of_babkens_garden = Tex("$5$", metr_str, "$\\cdot$", "$4$", metr_str, "$=$", "$20$", metr_str, "$^2$", font_size=FONT_SIZE).next_to(babkens_garden, DOWN, 1)
        # area_of_babkens_garden.add_updater(lambda x: x.next_to(babkens_garden, DOWN, 1))
        always_redraw(lambda: area_of_babkens_garden[:2].set_color(ORANGE))
        always_redraw(lambda: area_of_babkens_garden[3:5].set_color(GREEN))
        srr_rect2 = SurroundingRectangle(area_of_babkens_garden, BLUE, buff=.2, corner_radius=.3)
        arrow2 = always_redraw(lambda: Arrow(babkens_garden.get_bottom(), srr_rect2.get_center()+np.array([0, .35, 0]), max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))
        self.play(
            TransformMatchingTex(VGroup(babkens_garden_height, babkens_garden_width).copy(), area_of_babkens_garden),
            GrowArrow(arrow2),
            Create(srr_rect2)
        )
        self.wait()

        self.play(
            FadeOut(babkens_garden_height),
            #VGroup(babkens_garden, babkens_carrots, babken).animate.next_to(anis_garden, buff=0, aligned_edge=DOWN)
            VGroup(VGroup(ani, anis_garden, anis_carrots, anis_garden_height, anis_garden_width), VGroup(babken, babkens_garden, babkens_garden, babkens_carrots, babkens_garden_width)).animate.arrange(buff=0).move_to(VGroup(anis_garden, babkens_garden).get_center()).align_to(anis_garden, DOWN)
        )
        plus_tex = Tex("$+$", font_size=FONT_SIZE).move_to(VGroup(area_of_anis_garden, area_of_babkens_garden).get_center())
        arrow2.clear_updaters()
        srr_rect2.clear_updaters()
        self.play(
            Write(plus_tex)
        )
        self.wait()

        # ընդամենը՝ 5*10=50մ^2
        # Անի՝ 30մ^2
        # Բաբկեն՝ 20մ^2
        temp = Group()
        for obj in self.mobjects:
            if obj != tasknumber:
                temp.add(obj)
        self.play(
            temp.animate.shift(LEFT)
        )
        
        all_tex = Tex(all_str, " $5$", metr_str, "$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$", "$=$", "$50$", metr_str, "$^2$", font_size=FONT_SIZE).to_edge(UR, buff=.4)
        all_tex[1:3].set_color(ORANGE)
        all_tex[5:7].set_color(GREEN)
        all_tex[8:10].set_color(GREEN)
        self.play(Write(all_tex))
        self.wait()
        self.fix_formula(all_tex)
        self.play(ModifyFormula(all_tex, replace_items=[[4, 5, 6, 7, 8, 9, 10]], replace_items_strs=[["$10$", metr_str]], replace_items_colors=[[GREEN, GREEN]], new_formula_alignment=RIGHT))
        self.wait()

        ani_area_tex = Tex(ani_area_str, " $30$", metr_str, "$^2$", font_size=FONT_SIZE).next_to(all_tex, DOWN, aligned_edge=RIGHT)
        always_redraw(lambda: ani_area_tex[0].set_color_by_gradient("#FF9673", "#E0B851"))
        self.play(Write(ani_area_tex))
        self.wait()

        babken_area_tex = Tex(babken_area_str, " $20$", metr_str, "$^2$", font_size=FONT_SIZE).next_to(ani_area_tex, DOWN, aligned_edge=RIGHT)
        always_redraw(lambda: babken_area_tex[0].set_color_by_gradient("#CFC748", "#7FC381"))
        self.play(Write(babken_area_tex))
        self.wait()

        # 50 = 30 + 20
        # 5*10 = 5*6 +5*4
        # 5*(6+4) = 5*4 +5*4
        formula = Tex("$50$", "$=$", "$30$", "$+$", "$20$", font_size=FONT_SIZE).next_to(babken_area_tex, DOWN, buff=1, aligned_edge=RIGHT)
        self.play(Write(formula))
        self.wait()

        formula_copy = formula.copy()
        self.play(formula_copy.animate.shift(DOWN))
        self.wait()
        self.fix_formula(formula_copy)
        self.play(ModifyFormula(formula_copy, replace_items=[[0], [2], [4]], replace_items_strs=[["$5$", "$\\cdot$", "$10$"], ["$5$", "$\\cdot$", "$6$"], ["$5$", "$\\cdot$", "$4$"]], replace_items_colors=[[ORANGE], [ORANGE, None, GREEN], [ORANGE, None, GREEN]], new_formula_alignment=RIGHT))
        self.wait()

        self.play(ModifyFormula(formula_copy, replace_items=[[2]], replace_items_strs=[["$($", "$6$", "$+$", "$4$", "$)$"]], new_formula_alignment=RIGHT, replace_items_colors=[[None, GREEN, None, GREEN]]))
        self.wait()

        # transform 5 to 7
        # միաժամանակ
        self.fix_formula(anis_garden_height)
        self.fix_formula(all_tex)
        self.fix_formula(ani_area_tex)
        self.fix_formula(babken_area_tex)
        self.fix_formula(formula)
        self.fix_formula(formula_copy)
        self.fix_formula(area_of_anis_garden)
        self.fix_formula(area_of_babkens_garden)
        self.play(
            Indicate(anis_garden_height[0]),
            Indicate(area_of_anis_garden[0]),
            Indicate(area_of_anis_garden[-3]),
            Indicate(ani_area_tex[1]),
            Indicate(area_of_babkens_garden[0]),
            Indicate(area_of_babkens_garden[-3]),
            Indicate(babken_area_tex[1]),
            Indicate(all_tex[1]),
            Indicate(all_tex[-3]),
            Indicate(formula[0]),
            Indicate(formula[2]),
            Indicate(formula[4]),
            Indicate(formula_copy[0]),
            Indicate(formula_copy[8]),
            Indicate(formula_copy[12]),
            run_time=2
        )
        self.wait()
        self.play(
            ModifyFormula(anis_garden_height, replace_items=[[0]], replace_items_strs=[["$7$"]]),
            ModifyFormula(all_tex, replace_items=[[1], [7]], replace_items_strs=[[" $7$"], ["$70$"]]),
            ModifyFormula(area_of_anis_garden, replace_items=[[0], [6]], replace_items_strs=[["$7$"], ["$42$"]]),
            ModifyFormula(ani_area_tex, replace_items=[[1]], replace_items_strs=[[" $42$"]]),
            ModifyFormula(area_of_babkens_garden, replace_items=[[0], [6]], replace_items_strs=[["$7$"], ["$28$"]]),
            ModifyFormula(babken_area_tex, replace_items=[[1]], replace_items_strs=[[" $28$"]]),
            ModifyFormula(formula, replace_items=[[0], [2], [4]], replace_items_strs=[["$70$"], ["$42$"], ["$28$"]]),
            ModifyFormula(formula_copy, replace_items=[[0], [8], [12]], replace_items_strs=[["$7$"], ["$7$"], ["$7$"]])
        )
        self.wait()

        # հերթով
        # self.play(Indicate(anis_garden_height))
        # self.wait()
        # self.fix_formula(anis_garden_height)
        # self.play(ModifyFormula(anis_garden_height, replace_items=[[0]], replace_items_strs=[["$7$"]]))
        # self.wait()
        
        # self.play(
        #     Indicate(area_of_anis_garden),
        #     Indicate(ani_area_tex)
        # )
        # self.wait()
        # self.fix_formula(area_of_anis_garden)
        # self.fix_formula(ani_area_tex)
        # self.play(ModifyFormula(area_of_anis_garden, replace_items=[[0], [6]], replace_items_strs=[["$7$"], ["$42$"]]))
        # self.play(ModifyFormula(ani_area_tex, replace_items=[[1]], replace_items_strs=[[" $42$"]]))
        # self.wait()

        # self.play(
        #     Indicate(area_of_babkens_garden),
        #     Indicate(babken_area_tex)
        # )
        # self.wait()
        # self.fix_formula(area_of_babkens_garden)
        # self.fix_formula(babken_area_tex)
        # self.play(ModifyFormula(area_of_babkens_garden, replace_items=[[0], [6]], replace_items_strs=[["$7$"], ["$28$"]]))
        # self.play(ModifyFormula(babken_area_tex, replace_items=[[1]], replace_items_strs=[[" $28$"]]))
        # self.wait()
        
        # self.play(Indicate(all_tex))
        # self.wait()
        # self.fix_formula(all_tex)
        # self.play(ModifyFormula(all_tex, replace_items=[[1], [7]], replace_items_strs=[[" $7$"], ["$70$"]]))
        # self.wait()
        
        # self.play(Indicate(formula))
        # self.wait()
        # self.fix_formula(formula)
        # self.play(ModifyFormula(formula, replace_items=[[0], [2], [4]], replace_items_strs=[["$70$"], ["$42$"], ["$28$"]]))
        # self.wait()

        # self.play(Indicate(formula_copy))
        # self.wait()
        # self.fix_formula(formula_copy)
        # self.play(ModifyFormula(formula_copy, replace_items=[[0], [8], [12]], replace_items_strs=[["$7$"], ["$7$"], ["$7$"]]))
        # self.wait()

        # a*(b+c) = a*b + b*c
        temp = Group()
        for obj in self.mobjects:
            if obj != tasknumber and obj != formula_copy:
                temp.add(obj)
        self.play(
            FadeOut(temp)
        )
        self.wait()

        self.play(formula_copy.animate.scale(1.6).move_to(ORIGIN))
        self.wait()
        
        self.play(
            Indicate(formula_copy[0]),
            Indicate(formula_copy[8]),
            Indicate(formula_copy[12])
        )
        self.wait()
        self.fix_formula(formula_copy)
        self.play(ModifyFormula(formula_copy, replace_items=[[0], [8], [12]], replace_items_strs=[["$a$"], ["$a$"], ["$a$"]]))
        self.wait()

        self.play(
            Indicate(formula_copy[3]),
            Indicate(formula_copy[10])
        )
        self.wait()
        self.fix_formula(formula_copy)
        self.play(ModifyFormula(formula_copy, replace_items=[[3], [10]], replace_items_strs=[["$b$"], ["$b$"]]))
        self.wait()

        self.play(
            Indicate(formula_copy[5]),
            Indicate(formula_copy[14])
        )
        self.wait()
        self.fix_formula(formula_copy)
        self.play(ModifyFormula(formula_copy, replace_items=[[5], [14]], replace_items_strs=[["$c$"], ["$c$"]]))

        self.wait(2)
