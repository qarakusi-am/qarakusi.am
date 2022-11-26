from manim import *
from hanrahashiv import FormulaModificationsScene, ModifyFormula
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
        arrow1 = always_redraw(lambda: Arrow(anis_garden.get_bottom(), srr_rect1.get_center() + 0.35 * UP, max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))

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
        arrow2 = always_redraw(lambda: Arrow(babkens_garden.get_bottom(), srr_rect2.get_center() + 0.35 * UP, max_stroke_width_to_length_ratio=8, max_tip_length_to_length_ratio=.3))

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
            AnimationGroup(*[GrowFromCenter(babkens_carrots[i]) for i in range(20)], lag_ratio=.8, run_time=2.5),
            AnimationGroup(*[GrowFromCenter(anis_carrots[i]) for i in range(30)], lag_ratio=.8, run_time=2.5),
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
        garden = Rectangle(LIGHT_BROWN, 5*scale, 10*scale).align_to(anis_garden, UL)
        temp = Tex("$6$", metr_str, "$+$", "$4$", metr_str, font_size=SMALL_FONT_SIZE, color=GREEN).next_to(garden, UP)
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
        self.play(Transform(temp, Tex("$10$", metr_str, font_size=SMALL_FONT_SIZE, color=GREEN).next_to(garden, UP)))
        self.wait()
        anis_garden.set_color(BLACK)
        anis_garden_width.set_opacity(0)
        babkens_garden.set_color(BLACK)
        babkens_garden_width.set_opacity(0)
        self.play(
            VGroup(
                ani,
                anis_garden,
                anis_carrots,
                anis_garden_height,
                anis_garden_width,
                babken,
                babkens_garden,
                babkens_carrots,
                babkens_garden_width,
                garden,
                temp
            ).animate.scale(.77).to_edge(UR, buff=.1).shift(DOWN*.1)
        )
        self.wait()
        anis_garden = anis_garden.copy().set_color(ORANGE)
        anis_garden_width = anis_garden_width.copy().set_opacity(1)
        babkens_garden = babkens_garden.copy().set_color(ORANGE)
        babkens_garden_width = babkens_garden_width.copy().set_opacity(1)
        total_tex = Tex(total_str, font_size=SMALL_FONT_SIZE).to_edge(UL, buff=.2)

        self.play(FadeOut(ani, babken))
        self.play(Write(total_tex))
        self.wait()
        self.fix_formula(total_tex)
        self.play(ModifyFormula(total_tex, add_after_items=[0], add_items_strs=[[" $5$", metr_str]], add_items_colors=[[ORANGE, ORANGE]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(total_tex, add_after_items=[2], add_items_strs=[["$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$"]], add_items_colors=[[None, None, GREEN, GREEN, None, GREEN, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(total_tex, add_after_items=[10], add_items_strs=[["$=$", "$5$", metr_str, "$\\cdot$", "$10$", metr_str]], add_items_colors=[[None, ORANGE, ORANGE, None, GREEN, GREEN]], add_items_animation_style=Write))
        self.wait()
        self.fix_formula(total_tex)
        self.play(ModifyFormula(total_tex, replace_items=[[12, 13, 14, 15, 16]], replace_items_strs=[["$50$", metr_str, "$^2$"]], replace_items_colors=[[WHITE, WHITE, WHITE]], new_formula_alignment=LEFT))
        self.wait()

        self.play(Indicate(VGroup(garden, anis_carrots, babkens_carrots), color=None))
        self.wait()

        arrow1.shift(0.5 * RIGHT)
        arrow2.shift(0.25 * RIGHT)

        area_of_anis_garden = Tex("$5$", metr_str, "$\\cdot$", "$6$", metr_str, font_size=area_of_anis_garden.font_size)
        area_of_anis_garden.next_to(arrow1.get_end(), DOWN)
        area_of_anis_garden[:2].set_color(ORANGE)
        area_of_anis_garden[3:5].set_color(GREEN)
        area_of_babkens_garden = Tex("$5$", metr_str, "$\\cdot$", "$4$", metr_str, font_size=area_of_babkens_garden.font_size)
        area_of_babkens_garden.next_to(arrow2.get_end(), DOWN)
        area_of_babkens_garden[:2].set_color(ORANGE)
        area_of_babkens_garden[3:5].set_color(GREEN)
        srr_rect1 = SurroundingRectangle(area_of_anis_garden, BLUE, buff=.2, corner_radius=.3)
        srr_rect2 = SurroundingRectangle(area_of_babkens_garden, BLUE, buff=.2, corner_radius=.3)
        self.play(  
            FadeIn(
                VGroup(
                    area_of_anis_garden,
                    area_of_babkens_garden,
                    srr_rect1,
                    srr_rect2,
                    arrow1,
                    arrow2,
                    plus_tex
                ).scale(.77).next_to(garden, DOWN),
                anis_garden,
                babkens_garden
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
        tex1 = Tex("$5$", metr_str, "$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$", " $=$" , font_size=SMALL_FONT_SIZE)
        tex1.align_to(total_tex[1], UL)
        tex1[:2].set_color(ORANGE)
        tex1[4:6].set_color(GREEN)
        tex1[7:9].set_color(GREEN)
        self.play(tex1.animate.scale(.77).next_to(srr_rect1, LEFT))
        self.wait()

    # transform 5 to 7
        self.play(
            FadeOut(
                total_tex,
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
            area_of_babkens_garden[0].animate.scale(1.3)
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
                anis_garden, anis_carrots, anis_garden_height, anis_garden_width, babkens_garden,
                babkens_carrots, babkens_garden_width, temp3, temp4, arrow1, arrow2
            )
        )
        self.wait()
        tex1_copy = Tex(
            "$7$", metr_str, "$\\cdot$", "$($", "$6$", metr_str, "$+$", "$4$", metr_str, "$)$", " $=$ ", # 7մ•(6մ+4մ)=   [0:11]
            "$7$", metr_str, "$\\cdot$", "$6$", metr_str, ' $+$ ', # 5մ•6մ +  [11:17]
            "$7$", metr_str, "$\\cdot$", "$4$", metr_str, # 5մ•4մ
            font_size=100
        )
        tex1_copy.move_to(ORIGIN)
        tex1_copy[:2].set_color(ORANGE)
        tex1_copy[4:6].set_color(GREEN)
        tex1_copy[7:9].set_color(GREEN)
        tex1_copy[11:13].set_color(ORANGE)
        tex1_copy[14:16].set_color(GREEN)
        tex1_copy[17:19].set_color(ORANGE)
        tex1_copy[20:22].set_color(GREEN)

        self.play(
            ReplacementTransform(tex1, tex1_copy[:11]),
            ReplacementTransform(area_of_anis_garden, tex1_copy[11:16]),
            ReplacementTransform(plus_tex, tex1_copy[16]),
            ReplacementTransform(area_of_babkens_garden, tex1_copy[17:])
        )
        self.remove(tex1)
        formula = tex1_copy
        self.add(formula)
        self.wait()

    # transform 7 to a
        self.fix_formula(formula)

        self.play(
            formula[:2].animate.scale(1.3),
            formula[11:13].animate.scale(1.3),
            formula[17:19].animate.scale(1.3)
        )
        self.wait()

        self.play(
            ModifyFormula(
                formula,
                replace_items=[[0, 1], [11, 12], [17, 18]], replace_items_strs=[["$a$"], ["$a$"], ["$a$"]],
                new_font_size=formula[2].font_size, new_formula_alignment=ORIGIN
            )
        )
        self.wait()

    # transform 6 to b
        self.play(
            formula[3:5].animate.scale(1.3),
            formula[12:14].animate.scale(1.3)
        )
        self.wait()

        self.play(
            ModifyFormula(
                formula,
                replace_items=[[3, 4], [12, 13]], replace_items_strs=[["$b$"], ["$b$"]],
                new_formula_alignment=ORIGIN
            )
        )
        self.wait()

    # transform 4 to c
        self.play(
            formula[5:7].animate.scale(1.3),
            formula[15:17].animate.scale(1.3)
        )
        self.wait()

        self.play(
            ModifyFormula(
                formula,
                replace_items=[[5, 6], [15, 16]], replace_items_strs=[["$c$"], ["$c$"]],
                new_formula_alignment=ORIGIN
            )
        )
        self.wait()

    # տարբեր արտահայտություններ
        self.play(formula.animate.to_edge(UP))
        self.wait()

        formulas = VGroup(
            Tex("$20$", color=YELLOW).scale(2.5).move_to([-3.5, 1, 0]),
            Tex("$7^2$", color=PURPLE).scale(2.5).move_to([3.5, -1, 0]),
            Tex("$-4$", color=BLUE_C).scale(2.5).move_to([0, 0, 0]),
            Tex("$x^2$", color=BLUE).scale(2).move_to([-3, -1, 0]),
            Tex("$y+c^2$", color=RED).scale(2).move_to([3, 1, 0]),
            Tex("$-x$", " $+$ ", "$3y$", "$^2$", color=ORANGE).scale(2).move_to([-2.5, 1, 0]),
            Tex("$b$", " $+$ ", "$c$", " $-$ ", "$1$", color=YELLOW_C).scale(2).move_to([2.5, -1, 0])
        )

        self.play(
            AnimationGroup(
                *[FadeIn(obj, rate_func=there_and_back_with_pause, run_time=3) for obj in formulas],
                lag_ratio=.25
            )
        )
        self.wait()

    # examples
    # 2x(3y+5)=2x*3y+2x*5=6x+10x
        example1 = Tex(
            "$2x$", "$\\cdot$", "$($", "$3y$", "$+$", "$5$", "$)$", ' $=$ ',
            '$2x$', '$\\cdot$', '$3y$', ' $+$ ', '$2x$', '$\\cdot$', '$5$',
            font_size=BIG_FONT_SIZE - 2
        )
        example1.next_to(formula, DOWN, 1, LEFT)
        example1[0].set_color(ORANGE)
        example1[3].set_color(GREEN)
        example1[5].set_color(GREEN)
        example1[8].set_color(ORANGE)
        example1[12].set_color(ORANGE)
        example1[10].set_color(GREEN)
        example1[14].set_color(GREEN)

        self.play(Write(example1[:7]))
        self.wait()

        arrow1 = Arrow(formula[0].get_center() + 0.1 * LEFT, example1[0].get_center(), buff=.4)
        arrow3 = Arrow(formula[5].get_center(), example1[5].get_center(), buff=.4)
        arrow2 = Arrow(formula[3].get_center(), example1[3].get_center(), buff=.4)

        self.play(GrowArrow(arrow1))
        self.wait()
        self.play(GrowArrow(arrow2))
        self.wait()
        self.play(GrowArrow(arrow3))
        self.wait()

        self.play(Write(example1[7], run_time=0.75))
        self.wait(0.15)
        self.play(
            Indicate(example1[0], run_time=0.75),
            Indicate(example1[3], run_time=0.75)
        )
        self.wait(0.15)
        temp_1 = example1[0].copy()
        temp_2 = example1[3].copy()
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(temp_1, example1[8]),
                Write(example1[9], run_time=0.5),
                CounterclockwiseTransform(temp_2, example1[10]),
                lag_ratio=0.5
            )
        )
        self.remove(temp_1, temp_2)
        self.add(example1[8], example1[10])
        self.wait(0.25)

        self.play(Write(example1[11], run_time=0.75))
        self.wait(0.15)
        self.play(
            Indicate(example1[0], run_time=0.75),
            Indicate(example1[5], run_time=0.75)
        )
        self.wait(0.15)
        temp_1 = example1[0].copy()
        temp_2 = example1[5].copy()
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(temp_1, example1[12]),
                Write(example1[13], run_time=0.5),
                CounterclockwiseTransform(temp_2, example1[14]),
                lag_ratio=0.5
            )
        )
        self.remove(temp_1, temp_2)
        self.add(example1[12], example1[14])
        self.wait(0.5)

        self.play(
            example1.animate.to_edge(LEFT),
            FadeOut(arrow1, arrow2, arrow3)
        )
        self.wait(0.5)
        self.fix_formula(example1)
        self.play(ModifyFormula(example1, add_after_items=[14], add_items_strs=[[" $=$ ", "$6xy$"]], add_items_animation_style=Write))
        self.wait()
        self.play(ModifyFormula(example1, add_after_items=[16], add_items_strs=[["$+$", "$10x$"]], add_items_animation_style=Write))
        self.wait()

        self.play(example1.animate.shift(DOWN*3.5))
        self.wait()

    # 3k(4l+6z)=12kl+18kz
        example2 = Tex(
            "$3k$", "$\\cdot$", "$($", "$4l$", "$+$", "$6z$", "$)$", " $=$ ",
            "$3k$", "$\\cdot$", "$4l$", " $+$ ", "$3k$", "$\\cdot$", "$6z$",
            font_size=BIG_FONT_SIZE - 3
        )
        example2.next_to(formula, DOWN, 1, LEFT)
        example2[0].set_color(ORANGE)
        example2[3].set_color(GREEN)
        example2[5].set_color(GREEN)
        example2[8].set_color(ORANGE)
        example2[12].set_color(ORANGE)
        example2[10].set_color(GREEN)
        example2[14].set_color(GREEN)

        self.play(Write(example2[:7]))
        self.wait()

        arrow1 = Arrow(formula[0].get_center(), example2[0].get_center(), buff=.4)
        arrow3 = Arrow(formula[5].get_center(), example2[5].get_center(), buff=.4)
        arrow2 = Arrow(formula[3].get_center(), example2[3].get_center(), buff=.4)
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait()
        
        self.play(Write(example2[7], run_time=0.75))
        self.wait(0.15)
        self.play(
            Indicate(example2[0], run_time=0.75),
            Indicate(example2[3], run_time=0.75)
        )
        self.wait(0.15)
        temp_1 = example2[0].copy()
        temp_2 = example2[3].copy()
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(temp_1, example2[8]),
                Write(example2[9], run_time=0.5),
                CounterclockwiseTransform(temp_2, example2[10]),
                lag_ratio=0.4
            )
        )
        self.remove(temp_1, temp_2)
        self.add(example2[8], example2[10])
        self.wait(0.15)
        self.play(Write(example2[11], run_time=0.5))
        self.wait(0.15)
        self.play(
            Indicate(example2[0], run_time=0.75),
            Indicate(example2[5], run_time=0.75)
        )
        self.wait(0.15)
        temp_1 = example2[0].copy()
        temp_2 = example2[5].copy()
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(temp_1, example2[12]),
                Write(example2[13], run_time=0.5),
                CounterclockwiseTransform(temp_2, example2[14]),
                lag_ratio=0.4
            )
        )
        self.remove(temp_1, temp_2)
        self.add(example2[12], example2[14])
        self.wait(0.5)

        self.play(
            example2.animate.to_edge(LEFT, buff=.18),
            FadeOut(arrow1, arrow2, arrow3)
        )
        self.wait(0.25)

        self.fix_formula(example2)
        self.play(ModifyFormula(example2, add_after_items=[14], add_items_strs=[[" $=$ ", "$12kl$"]], add_items_animation_style=Write))
        self.wait(0.75)
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
