from manim import WHITE, ORANGE, GREEN, YELLOW, RED, BLUE, PINK
from manim import UL,UR, DR, UP, DOWN, RIGHT, LEFT
from manim import Write, Create, Circumscribe, Indicate
from manim import Circle, Line, SurroundingRectangle
from manim import linear

from hanrahashiv import *
from objects import SimpleSVGMobject


class Nman_andamner(FormulaModificationsScene):
    def construct(self):
        property_font_size = 65
        font_size = 55
        left_boundary = [-6.5, 0, 0]
        up_boundary = [0, 3, 0]

        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_1_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_1_index = Tex('1', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_1_design = VGroup(property_1_rect, property_1_index)
        property_1_design.move_to(property_1).shift(0.05 * UP)
        prop_1 = VGroup(property_1, property_1_design)

        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_2_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_2_index = Tex('2', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_2_design = VGroup(property_2_rect, property_2_index)
        property_2_design.move_to(property_2).shift(0.05 * UP)
        prop_2 = VGroup(property_2, property_2_design)

        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = VGroup()
        vertices = [[-0.2, 1, 0], [-4.4, 1, 0], [-4.4, 0, 0], [0, 0, 0], [0, 0.8, 0]]
        for i in range(4):
            property_3_rect += Line(vertices[i], vertices[i+1], color=GREEN)
        property_3_index = Tex('3', font_size=45, color=ORANGE).move_to([-0.05, 1, 0])
        property_3_design = VGroup(property_3_rect, property_3_index)
        property_3_design.move_to(property_3).shift(0.05 * UP)
        prop_3 = VGroup(property_3, property_3_design)
        
        VGroup(prop_1, prop_2, prop_3).arrange(DOWN, 0.25).to_edge(RIGHT, buff=0.2).align_to(up_boundary, UP)


        self.wait()

        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait()

    # գրում ենք առաջին վարժությունը
        first = Tex('$1)$', font_size=property_font_size).align_to(left_boundary, LEFT).align_to(up_boundary, UP)
        first_exercise = Tex(
            '$($', '$y$', '$^2$', '$x$', '$^3$', '$)$', '$^4$', '$=$', # [0:8]
            '$($', '$y$', '$^2$', '$)$', '$^4$', '$\cdot$', '$($', '$x$', '$^3$', '$)$', '$^4$', '$=$', # [8:20]
            '$y$', '$^8$', '$\cdot$', '$x$', '$^{12}$', # [20:25]
            font_size=font_size
        ) # (y^2x^3)^4= (y^2)^4•(x^3)^4= y^8•x^12
        first_exercise.next_to(first, RIGHT)
        first_exercise[9:11].set_color(ORANGE)
        first_exercise[15:17].set_color(GREEN)
        first_exercise[22].set_opacity(0.5)
        VGroup(first_exercise[12], first_exercise[18]).set_color(YELLOW)

        self.play(Write(first))
        self.wait(0.5)

        self.play(Write(first_exercise[0:7]))
        self.wait()

        self.play(Circumscribe(first_exercise[:6], time_width=2))
        self.wait(0.5)

        self.play(Circumscribe(first_exercise[6], shape=Circle, time_width=2))
        self.wait(0.5)

        self.play(Indicate(first_exercise[1:5]))
        self.wait()

        self.play(Indicate(first_exercise[1:3]))
        self.wait(0.5)

        self.play(Indicate(first_exercise[3:5]))
        self.wait(0.5)

    # երկրորդ հատկությունը բերում ենք ներքև
        self.play(Indicate(prop_2))
        self.wait()

        property_2_copy = property_2.copy()

        self.play(
            property_2_copy.animate.scale(font_size/property_font_size),
            property_2_copy.animate.next_to(first_exercise, 2 * DOWN).align_to(first_exercise, LEFT)
        )
        self.wait()
    
    # a = y^2
        self.play(
            first_exercise[1:3].animate.set_color(ORANGE),
            property_2_copy[1].animate.set_color(ORANGE),
            property_2_copy[7].animate.set_color(ORANGE)
        )
        self.wait(0.5)

        self.play(
            first_exercise[1:3].animate.scale(1.5),
            property_2_copy[1].animate.scale(1.5),
            property_2_copy[7].animate.scale(1.5)
        )
        self.wait(0.1)

        self.fix_formula(property_2_copy)
        self.play(
            ModifyFormula(
                property_2_copy,
                replace_items=[[1], [7]],
                replace_items_strs=[['$y$', '$^2$'], ['$($', '$y$', '$^2$', '$)$']],
                replace_items_colors=[[ORANGE, ORANGE], [WHITE, ORANGE, ORANGE, WHITE]]
            ),
            first_exercise[1:3].animate.scale(1/1.5)
        )
        self.fix_formula(property_2_copy)
        self.wait()
        # property_2_copy = exp

    # b = x^3
        exp = Tex('$($', '$y$', '$^2$', '$\cdot$', '$x$', '$^3$', '$)$', '$^n$', '$=$', # [0:9]
        '$($', '$y$', '$^2$', '$)$', '$^n$', '$\cdot$', '$($', '$x$', '$^3$', '$)$', '$^n$', # [9:20]
        font_size=property_font_size).align_to(property_2_copy, DL)
        exp[1:3].set_color(ORANGE)
        exp[10:12].set_color(ORANGE)
        exp[4:6].set_color(GREEN)
        exp[16:18].set_color(GREEN)

        self.play(
            VGroup(first_exercise[3:5], property_2_copy[4], property_2_copy[14]).animate.set_color(GREEN)
        )
        self.wait(0.5)

        self.play(
            first_exercise[3:5].animate.scale(1.5),
            property_2_copy[4].animate.scale(1.5),
            property_2_copy[14].animate.scale(1.5)
        )
        self.wait(0.1)

        self.fix_formula(property_2_copy)
        self.play(
            ModifyFormula(
                property_2_copy,
                replace_items=[[4], [14]],
                replace_items_strs=[['$x$', '$^3$'], ['$($', '$x$', '$^3$', '$)$']],
                replace_items_colors=[[GREEN, GREEN], [WHITE, GREEN, GREEN, WHITE]]
            ),
            first_exercise[3:5].animate.scale(1/1.5)
        )
        self.wait(0.5)
        # property_2_copy = exp

    # n = 4
        self.play(
            first_exercise[6].animate.set_color(YELLOW).scale(1.5),
            property_2_copy[7].animate.set_color(YELLOW).scale(1.5),
            property_2_copy[13].animate.set_color(YELLOW).scale(1.5),
            property_2_copy[19].animate.set_color(YELLOW).scale(1.5)
        )
        self.wait(0.1)

        self.fix_formula(property_2_copy)
        self.play(
            ModifyFormula(
                property_2_copy,
                replace_items=[[7], [13], [19]],
                replace_items_strs=[['$^4$'], ['$^4$'], ['$^4$']]
            ),
            first_exercise[6].animate.scale(1/1.5)
        )
        self.fix_formula(property_2_copy)
        self.wait(0.5)

        self.play(Write(first_exercise[7]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(property_2_copy[9:20], first_exercise[8:19]),
            FadeOut(property_2_copy[:9])
        )
        self.wait()

        self.play(first_exercise[:19].animate.set_color(WHITE))
        self.wait()

    # (y^2)^4 = y^{2•4}=y^8
        self.play(Indicate(first_exercise[8:13]))
        self.wait(0.25)
        self.play(Indicate(first_exercise[14:19]))
        self.wait()
        self.play(
            Indicate(first_exercise[8:13]),
            first_exercise[13:19].animate.set_opacity(0.5)
        )
        self.wait()
        self.play(Indicate(prop_3))
        self.wait()

        clone = Tex('$($', '$y$', '$^2$', '$)$', '$^4$', font_size=font_size).align_to(first_exercise[8], DL)
        self.add(clone)

        self.play(clone.animate.shift(DOWN))
        self.wait()
        self.fix_formula(clone)
        self.play(
            ModifyFormula(
                clone,
                remove_items=[0, 3],
                add_after_items=[2],
                add_items_strs=[['$^\\cdot$']]
            )
        )
        self.fix_formula(clone)
        self.wait()

        self.play(
            ModifyFormula(
                clone,
                replace_items=[[1, 2, 3]],
                replace_items_strs=[['$^8$']]
            )
        )
        self.fix_formula(clone)
        self.wait()

        self.play(
            Indicate(first_exercise[10]),
            Indicate(first_exercise[12])
        )
        self.wait(0.5)

        self.play(
            Write(first_exercise[19]),
            ReplacementTransform(clone, first_exercise[20:22]),
            run_time=0.75
        )
        self.play(Write(first_exercise[22], run_time=0.5))
        self.wait(0.5)

        self.play(
            first_exercise[8:14].animate.set_opacity(0.5),
            first_exercise[20:23].animate.set_opacity(0.5),
            first_exercise[14:19].animate.set_opacity(1),
            run_time=0.5
        )
        self.wait(0.25)

    # (x^3)^4 = x^{3•4} x^12
        clone = Tex('$($', '$x$', '$^3$', '$)$', '$^4$', font_size=font_size)
        clone.align_to(first_exercise[14], DL)
        self.add(clone)
        self.play(clone.animate.shift(DOWN), run_time=0.5)
        self.wait(0.5)

        self.fix_formula(clone)
        self.play(
            ModifyFormula(
                clone,
                remove_items=[0, 3],
                add_after_items=[2],
                add_items_strs=[['$^\\cdot$']],
                new_formula_alignment=UP
            )
        )
        self.wait(0.5)

        self.fix_formula(clone)
        self.play(
            ModifyFormula(
                clone,
                replace_items=[[1, 2, 3]],
                replace_items_strs=[['$^{12}$']]
            )
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(clone, first_exercise[23:25]),
            first_exercise[8:14].animate.set_opacity(1),
            first_exercise[20:23].animate.set_opacity(1)
        )
        self.wait()

    # նկատում ենք, որ թվերը բազմապատկվել են աստիճանով)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Circumscribe(first_exercise[2], fade_out=True),
                    Circumscribe(first_exercise[4], fade_out=True)
                ),
                Circumscribe(first_exercise[6], fade_out=True),
                lag_ratio=0.75
            )
        )
        self.play(Indicate(first_exercise[2], scale_factor=1.5))
        self.wait(0.5)

        self.play(Indicate(first_exercise[4], scale_factor=1.5))
        self.wait(0.5)

        self.play(Circumscribe(first_exercise[20:], fade_out=True, run_time=1.5))
        self.wait()

        self.rearrange_formula(first_exercise, [*range(20), 23, 24, 22, 20, 21], [23, 24], [], [22], [])
        self.wait(0.5)

        self.play(
            ModifyFormula(
                first_exercise,
                remove_items=[22]
            )
        )
        self.wait()

    # Երկրորդ վարժություն - (2•a^2)^3  (անիմացիայի համարը մոտավոր 83)
        second = Tex('$2)$', font_size=property_font_size).align_to(first, LEFT).next_to(first, DOWN, buff=1)
        second_exercise = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', # [:7]
        '$=$', # [7]
        '$2$', '$^3$', '$\cdot$', '$($', '$a$', '$^2$', '$)$', '$^3$', # [8:16]
        font_size=font_size).next_to(second, RIGHT)

        self.play(Write(second))
        self.wait()
        self.play(Write(second_exercise[:7]))
        self.wait()

    # (2•a^2)^3 = 2^3 • (a^2)^3
        self.play(Indicate(prop_2))
        self.wait()

        clone = Tex('$($', '$2$', '$\\cdot$', '$a$', '$^2$', '$)$', '$^3$', font_size=font_size)
        clone.align_to(second_exercise[0], DL)
        self.add(clone)
        self.play(clone.animate.shift(DOWN))
        self.wait()

        self.play(Indicate(clone[1]))
        self.wait(0.1)
        self.play(Indicate(clone[3:5]))
        self.wait()

        self.fix_formula(clone)
        self.play(
            ModifyFormula(
                clone,
                remove_items=[0],
                add_after_items=[1, 2],
                add_items_strs=[['$^3$'], ['$($']]
            )
        )
        self.wait(0.75)

    # հավասարության 2-րդ մասը
        self.play(
            Write(second_exercise[7], run_time=0.5),
            ReplacementTransform(clone, second_exercise[8:16])
        )
        self.wait(0.5)

    # 2^3 = 2 * 2 * 2 = 8
        self.play(second_exercise[8:10].animate.set_color(YELLOW).scale(1.5), run_time=0.5)
        self.wait(0.1)
        self.play(second_exercise[8:10].animate.scale(1/1.5), run_time=0.5)
        self.wait(0.5)

        self.fix_formula(second_exercise)
        self.play(
            ModifyFormula(
                second_exercise, replace_items=[[9]],
                replace_items_strs=[['$\cdot$', '$2$', '$\cdot$', '$2$']],
                replace_items_colors=[[WHITE, YELLOW, WHITE, YELLOW]]
            ),
            run_time=0.75
        )
        self.wait(0.75)

        self.fix_formula(second_exercise)
        self.play(
            ModifyFormula(
                second_exercise,
                replace_items=[[8, 9, 10, 11, 12]],
                replace_items_strs=[['$8$']],
                replace_items_colors=[[YELLOW]]
            ),
            run_time=0.75
        )
        self.wait(0.75)
        self.play(second_exercise[8].animate.set_color(WHITE), run_time=0.75)
        self.wait(0.5)

    # (a^2)^3 = a^6
        self.play(Indicate(prop_3))
        self.wait()

        self.fix_formula(second_exercise)
        self.play(
            ModifyFormula(
                second_exercise,
                remove_items=[10, 13],
                add_after_items=[12], add_items_strs=[['$^\\cdot$']]
            )
        )
        self.wait()

    # ավարտում ենք երկրորդ վարժը
        self.fix_formula(second_exercise)
        self.play(
            ModifyFormula(
                second_exercise,
                replace_items=[[11, 12, 13]],
                replace_items_strs=[['$^6$']]
            )
        )
        self.wait()

    # Երկրորդի սխալ լուծում  (անիմացիայի համարը մոտավոր 120)
        first_2 = Tex('$1.$', font_size=property_font_size).align_to(left_boundary, LEFT).next_to(second, DOWN, buff=1)
        first_exercise_2 = Tex('$($', '$y$', '$^2$', '$x$', '$^3$', '$)$', '$^4$', # [0:7]
        '$=$', #[7]
        '$x$', '$^{12}$', '$y$', '$^8$', # [8:12]
        font_size=font_size).next_to(first_2, RIGHT)

        second_exercise_2 = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', # [0:7]
        '$=$', #[7]
        '$2$', '$\cdot$', '$3$', # [8:11] 
        font_size=font_size).next_to(first_exercise_2, DOWN, buff=1).align_to(first_exercise_2, LEFT)
        second_exercise_2[8].set_color(ORANGE)
        second_exercise_2[10].set_color(YELLOW)
        second_exercise_2_tail = Tex('$\cdot$', '$a$', '$^2$', '$^\cdot$', '$^3$', font_size=font_size)
        second_exercise_2_tail[2].set_color(GREEN)
        second_exercise_2_tail[4].set_color(YELLOW)

        self.play(
            ReplacementTransform(second_exercise[:8].copy(), second_exercise_2[:8]),
            second_exercise.animate.set_opacity(0.5),
            second.animate.set_opacity(0.5)
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(first_exercise[:8].copy(), first_exercise_2[:8]),
            ReplacementTransform(first_exercise[20:24].copy(), first_exercise_2[8:12]),
            first_exercise.animate.set_opacity(0.5),
            first.animate.set_opacity(0.5)
        )
        self.wait(0.5)

        self.play(
            property_1.animate.set_opacity(0.5),
            property_1_rect.animate.set_stroke(opacity=0.5),
            property_1_index.animate.set_opacity(0.5),
            property_2.animate.set_opacity(0.5),
            property_2_rect.animate.set_stroke(opacity=0.5),
            property_2_index.animate.set_opacity(0.5),
            property_3.animate.set_opacity(0.5),
            property_3_rect.animate.set_stroke(opacity=0.5),
            property_3_index.animate.set_opacity(0.5),
        )
        self.wait(0.5)

    # հին վարժության նկատած օրինաչափությունը
        self.play(AnimationGroup(
            Circumscribe(first_exercise_2[2], fade_out=True, run_tim=1.5),
            Circumscribe(first_exercise_2[4], fade_out=True, run_tim=1.5),
            lag_ratio=0.75
        ))
        self.wait(0.5)
        self.play(Circumscribe(first_exercise_2[6], fade_out=True, run_tim=1.5))
        self.wait(0.25)

    # գործակցում 2•3=6
        self.play(second_exercise_2[1].animate.set_color(ORANGE), run_time=0.5)
        self.wait(0.05)
        self.play(ReplacementTransform(second_exercise_2[1].copy(), second_exercise_2[8]), run_time=0.5)
        self.wait(0.05)
        self.play(Write(second_exercise_2[9]), run_time=0.5)
        self.wait(0.05)
        self.play(second_exercise_2[6].animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.05)
        self.play(ReplacementTransform(second_exercise_2[6].copy(), second_exercise_2[10]), run_time=0.5)
        self.wait(0.05)

        self.fix_formula(second_exercise_2)
        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[8, 9, 10]],
                replace_items_strs=[['$6$']],
                replace_items_colors=[[RED]]
            )
        )
        self.wait()

    # ցուցիչում 2•3=6
        second_exercise_2_tail.next_to(second_exercise_2, RIGHT, buff=0.06).align_to(second_exercise_2[8], DOWN)

        self.play(Write(second_exercise_2_tail[:2]), run_time=0.5)
        self.wait(0.05)
        self.play(second_exercise_2[4].animate.set_color(GREEN), run_time=0.5)
        self.wait(0.05)
        self.play(ReplacementTransform(second_exercise_2[4].copy(), second_exercise_2_tail[2]), run_time=0.75)
        self.wait(0.05)
        self.play(Write(second_exercise_2_tail[3]), run_time=0.5)
        self.wait(0.05)
        self.play(ReplacementTransform(second_exercise_2[6].copy(), second_exercise_2_tail[4]), run_time=0.75)
        self.wait(0.05)

        self.fix_formula(second_exercise_2_tail)
        self.play(
            ModifyFormula(
                second_exercise_2_tail,
                replace_items=[[2, 3, 4]],
                replace_items_strs=[['$^6$']],
                replace_items_colors=[[GREEN]]
            )
        )
        self.wait()

        self.play(
            second_exercise_2.animate.set_color(WHITE),
            second_exercise_2_tail.animate.set_color(WHITE)
        )
        self.wait()
        self.play(second_exercise[8:12].animate.set_opacity(1))
        self.wait()

    # տենում ենք որ գործակիցը սխալ ա
        self.play(
            Circumscribe(second_exercise[8], color=BLUE, time_width=2, fade_out=True),
            second_exercise[8].animate.set_color(BLUE),
            Circumscribe(second_exercise_2[8], color=RED, time_width=2, fade_out=True),
            second_exercise_2[8].animate.set_color(RED)
        )
        self.wait()

    # դիտարկում ենք առաջին վարժությունը (անիմացիայի համարը մոտավոր 157)
        self.play(Circumscribe(first_exercise_2, fade_out=True, run_time=1.5))
        self.wait(0.5)
        self.play(
            Indicate(first_exercise_2[2], 1.5, run_time=1.5),
            Indicate(first_exercise_2[4], 1.5, run_time=1.5)
        )
        self.wait()

        self.fix_formula(first_exercise_2)
        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[0],
                add_items_strs=[['$1$', '$\cdot$']]
            )
        ) # (1 * y^2 x^3)^4 = y^8 x^12
        self.wait()

        self.play(
            Indicate(first_exercise_2[1], scale_factor=1.5, color=ORANGE),
            Indicate(first_exercise_2[8], scale_factor=1.5)
        )
        self.wait()

        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[9],
                add_items_strs=[['$1$', '$\cdot$', '$4$']],
                add_items_colors=[[ORANGE, WHITE, YELLOW]]
            )
        ) # (1 * y^2x^3)^4 = 1 * 4 y^8 x^12
        self.wait()

        self.play(
            ModifyFormula(
                first_exercise_2,
                replace_items=[[10, 11, 12]],
                replace_items_strs=[['$4$']],
                replace_items_colors=[[RED]]
            )
        ) # (1 * y^2x^3)^4 = 4 y^8 x^12
        self.wait()

        self.play(
            ModifyFormula(
                first_exercise_2,
                replace_items=[[10]],
                replace_items_strs=[['$1$']],
                replace_items_colors=[[WHITE]]
            )
        ) # (1 * y^2x^3)^4 = 1 y^8 x^12
        self.wait()

        self.fix_formula(first_exercise_2)
        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[1],
                add_items_strs=[['$^1$']]
            )
        ) # (1^1 * y^2x^3)^4 = 1 y^8 x^12
        self.wait()

        self.play(Circumscribe(first_exercise_2[1:8]))
        self.wait()

        self.play(Indicate(first_exercise_2[1], scale_factor=1.5, color=GREEN, run_time=0.75))
        self.play(Indicate(first_exercise_2[4], scale_factor=1.5, color=GREEN, run_time=0.75))
        self.play(Indicate(first_exercise_2[6], scale_factor=1.5, color=GREEN, run_time=0.75))
        self.wait()

        self.play(
            AnimationGroup(
                Indicate(first_exercise_2[2], scale_factor=1.5, color=ORANGE, run_time=0.75),
                Indicate(first_exercise_2[5], scale_factor=1.5, color=ORANGE, run_time=0.75),
                Indicate(first_exercise_2[7], scale_factor=1.5, color=ORANGE, run_time=0.75),
                lag_ratio=0.5
            )
        )
        self.wait(0.1)
        self.play(Indicate(first_exercise_2[9], scale_factor=1.5, color=ORANGE, run_time=0.75))
        self.wait()

        self.play(
            Indicate(first_exercise_2[2], scale_factor=1.5, color=GREEN),
            Indicate(first_exercise_2[9], scale_factor=1.5)
        )
        self.wait()

        self.fix_formula(first_exercise_2)
        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[11],
                add_items_strs=[['$^1$', '$^\cdot$', '$^4$']],
                add_items_colors=[[GREEN, WHITE, YELLOW]]
            )
        ) # (1^1 * y^2x^3)^4 = 1^{1*4} y^8 x^12
        self.wait()

        self.fix_formula(first_exercise_2)
        self.play(
            ModifyFormula(
                first_exercise_2,
                remove_items=[12, 13, 14]
            )
        ) # (1^1 * y^2x^3)^4 = 1 y^8 x^12
        self.wait()

        second_exercise_2_clone = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', # [0:7]
        '$=$', #[7]
        '$6$', '$cdot$', '$a$', '$^6$', # [8:12]
        font_size=font_size).next_to(first_exercise_2, DOWN, buff=1).align_to(first_exercise_2, LEFT)
        second_exercise_2_clone[8].set_color(RED)

        self.add(second_exercise_2_clone)
        self.fix_formula(second_exercise_2)
        self.play(second_exercise_2.animate.set_opacity(0))
        self.remove(second_exercise_2_tail)

        second_exercise_2 = second_exercise_2_clone

        self.play(Indicate(second_exercise_2))
        self.wait()

        self.play(second_exercise_2[1].animate.set_color(BLUE))
        self.wait(0.5)

        self.fix_formula(second_exercise_2)
        self.play(
            ModifyFormula(
                second_exercise_2,
                add_after_items=[1],
                add_items_strs=[['$^1$']],
            )
        )
        self.wait(0.5)

        self.play(
            Indicate(second_exercise_2[2], scale_factor=1.5, color=ORANGE),
            Indicate(second_exercise_2[7], scale_factor=1.5)
        )
        self.wait()

        self.fix_formula(second_exercise_2)
        self.play(
            ModifyFormula(
                second_exercise_2,
                add_after_items=[9],
                add_items_strs=[['$^1$', '$^\cdot$', '$^3$']],
                add_items_colors=[[ORANGE, WHITE, YELLOW]],
                replace_items=[[9]],
                replace_items_strs=[['$2$']],
                replace_items_colors=[[BLUE]]
            )
        )
        self.wait()

        self.fix_formula(second_exercise_2)
        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[10, 11, 12]],
                replace_items_strs=[['$^3$']],
                replace_items_colors=[[WHITE]]
            )
        )
        self.wait(0.5)
        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[9, 10]],
                replace_items_strs=[['$8$']],
                replace_items_colors=[[BLUE]]
            )
        )
        self.wait()

        self.play(
            property_1.animate.set_opacity(1),
            property_1_rect.animate.set_stroke(opacity=1),
            property_1_index.animate.set_opacity(1),
            property_2.animate.set_opacity(1),
            property_2_rect.animate.set_stroke(opacity=1),
            property_2_index.animate.set_opacity(1),
            property_3.animate.set_opacity(1),
            property_3_rect.animate.set_stroke(opacity=1),
            property_3_index.animate.set_opacity(1),
            VGroup(first, first_exercise).animate.set_opacity(1),
            VGroup(second, second_exercise).animate.set_opacity(1),
            FadeOut(first_exercise_2),
            FadeOut(second_exercise_2),
            second_exercise[8].animate.set_color(WHITE)
        )
        self.wait()

    # Երրորդ վարժություն
        third = Tex('$3$', '$)$', font_size=property_font_size).align_to(second, LEFT).next_to(second, DOWN, buff=1)
        third_exercise = Tex('$2$', '$($', '$a$', '$^2$', '$)$', '$^3$', # [0:6]
        '$=$', # [6]
        '$2$', '$a$', '$^6$', # [7:10]
        font_size=font_size).next_to(third, RIGHT)

        self.play(Write(third))
        self.wait()

        self.play(Write(third_exercise[:6]))
        self.wait()


    # տարբերում ենք նախորդ վարժությունից
        self.play(
            Indicate(third_exercise[0], scale_factor=1.5),
            Indicate(second_exercise[1], scale_factor=1.5)
        )
        self.wait(0.5)

        self.play(
            Indicate(third_exercise[1], scale_factor=1.5, color=RED),
            Indicate(third_exercise[4], scale_factor=1.5, color=RED),
            Indicate(second_exercise[0], scale_factor=1.5, color=RED),
            Indicate(second_exercise[5], scale_factor=1.5, color=RED)
        )
        self.wait()

        self.play(Indicate(third_exercise[1:6], scale_factor=1.5))
        self.wait(0.5)

        self.play(Indicate(third_exercise[0], scale_factor=1.5))
        self.wait()

    # (a^2)^3 = a^6
        self.play(Indicate(prop_3))
        self.wait()

        clone = Tex('$($', '$a$', '$^2$', '$)$', '$^3$', font_size=font_size).align_to(third_exercise[1], DL)

        self.play(clone.animate.shift(DOWN))
        self.wait()

        self.fix_formula(clone)
        self.play(
            ModifyFormula(
                clone,
                remove_items=[0, 3],
                add_after_items=[2],
                add_items_strs=[['$^\\cdot$']]
            )
        )
        self.wait()
        
      # 2*3=6
        self.play(
            ModifyFormula(
                clone,
                replace_items=[[1, 2, 3]],
                replace_items_strs=[['$^6$']]
            )
        )
        self.wait()

        self.play(Write(third_exercise[6]))
        self.wait()

        self.play(ReplacementTransform(third_exercise[0].copy(), third_exercise[7]))
        self.wait()

        self.play(ReplacementTransform(clone, third_exercise[8:]))
        self.wait(0.5)

    # վերջապես նման անդամներ
        self.play(
            Circumscribe(second_exercise[8:], time_width=2),
            Circumscribe(third_exercise[7:], time_width=2)
        )
        self.wait()

        monom_1 = second_exercise[8:]
        monom_2 = third_exercise[7:]
        
        self.play(
            FadeOut(prop_1, prop_2, prop_3),
            FadeOut(first, first_exercise),
            FadeOut(second, second_exercise[:8]),
            FadeOut(third, third_exercise[:7]),
            monom_1.animate.scale(1.5).move_to([-2, 1, 0]),
            monom_2.animate.scale(1.5).move_to([2, 1, 0])
        )
        self.wait()

    # եկեք գումարենք
        new_font_size = 1.5 * font_size
        plus = Tex('$+$', font_size=new_font_size).move_to((monom_1.get_right() + monom_2.get_left())/2)

        self.play(Write(plus))
        self.wait()

    # գետաձիեր
        self.play(
            Indicate(monom_1[1:3]),
            Indicate(monom_2[1:3])
        )
        self.wait()

        first_hippo = SimpleSVGMobject('hippo').align_to(monom_1, DR)
        second_hippo = SimpleSVGMobject('hippo').next_to(monom_2[0], RIGHT, buff=0.2)

        self.play(
            ReplacementTransform(monom_1[1:], first_hippo),
            ReplacementTransform(monom_2[1:], second_hippo),
            monom_1[0].animate.next_to(first_hippo, LEFT, buff=0.2)
            )
        self.wait()

        self.remove(monom_1[1:], monom_2[1:])

        hippo = SimpleSVGMobject('hippo').scale(0.9)

        hippo_group_1 = VGroup()
        
        for i in range(8):
            if i == 0:
                hippo_group_1 += hippo.copy().move_to([-5.5, -0.5, 0])
            elif i == 1:
                hippo_group_1 += hippo.copy().next_to(hippo_group_1[0], DOWN, buff=0.3)
            else:
                hippo_group_1 += hippo.copy().next_to(hippo_group_1[i-2], RIGHT, buff=0.2)

        hippo_group_2 = VGroup()

        for i in range(2):
            if i == 0:
                hippo_group_2 += hippo.copy().move_to([4, -0.5, 0])
            else:
                hippo_group_2 += hippo.copy().next_to(hippo_group_2[0], DOWN, buff=0.3)

        z = hippo_group_2.copy().next_to(hippo_group_1, RIGHT, buff=0.2)

        surrec_1 = SurroundingRectangle(hippo_group_1, corner_radius=0.3, color=ORANGE, stroke_width=6)
        surrec_2 = SurroundingRectangle(hippo_group_2, corner_radius=0.3, color=ORANGE, stroke_width=6)
        surrec_all = SurroundingRectangle(VGroup(hippo_group_1, z), corner_radius=0.3, color=ORANGE, stroke_width=6)

        x = VGroup()
        for i in range(8):
            if i == 0:
                x += first_hippo
            else:
                x += first_hippo.copy()

        y = VGroup()
        for i in range(2):
            if i == 0:
                y += second_hippo
            else:
                y += second_hippo.copy()

    # գետաձիերի խմբեր
        self.play(
            ReplacementTransform(x, hippo_group_1),
            Create(surrec_1),
            monom_1[0].animate.next_to(surrec_1, UP),
            ReplacementTransform(y, hippo_group_2),
            Create(surrec_2),
            monom_2[0].animate.next_to(surrec_2, UP),
            plus.animate.move_to((surrec_1.get_right() + surrec_2.get_left())/2)
        )
        self.wait()

        self.play(Indicate(VGroup(monom_1[0], surrec_1, hippo_group_1), color=None))
        self.wait(0.5)

        self.play(Indicate(plus, scale_factor=1.5))
        self.wait(0.5)

        self.play(Indicate(VGroup(monom_2[0], surrec_2, hippo_group_2), color=None))
        self.wait(0.5)

        self.add(surrec_all)
        self.remove(surrec_all)

        self.play(
            hippo_group_2.animate.next_to(hippo_group_1, RIGHT, buff=0.2),
            plus.animate.move_to(hippo_group_1[4].get_center()).align_to(monom_1[0], DOWN),
            monom_1[0].animate.align_to(hippo_group_1[4].get_left(), RIGHT),
            monom_2[0].animate.align_to(hippo_group_1[4].get_right(), LEFT),
            ReplacementTransform(VGroup(surrec_1, surrec_2), surrec_all),
            rate_func=linear
        )
        self.wait()

        ten = Tex('$10$', font_size=new_font_size).move_to(plus)

        self.play(ReplacementTransform(VGroup(monom_1[0], monom_2[0], plus), ten))
        self.wait()
        
        expression_1 = MathTex('8', 'a', '^6', '+', '2', 'a', '^6', '=', '10', 'a', '^6', font_size=new_font_size).move_to([0, 2, 0])

        self.play(Write(expression_1[:3]))
        self.wait(0.5)

        self.play(Write(expression_1[3]))
        self.wait(0.5)

        self.play(Write(expression_1[4:7]))
        self.wait(0.5)

        self.play(Write(expression_1[7]))
        self.wait(0.5)

        self.play(Write(expression_1[8:11]))
        self.wait()

        self.play(Indicate(expression_1[8:11], scake_factor=1.5))
        self.wait()

        self.play(
            Indicate(expression_1[:3], scale_factor=1.5),
            Indicate(expression_1[4:7], scale_factor=1.5)
        )
        self.wait()

        self.play(
            expression_1.animate.shift(UP).set_opacity(0.5),
            FadeOut(hippo_group_1, hippo_group_2, surrec_all, ten)
        )
        self.wait()

        expression_2 = MathTex('x', '+', '4', 'x', '+', '2', 'x', '=', '7', 'x', font_size=new_font_size)

        self.play(
            Write(expression_2[0]),
            Write(expression_2[2:4]),
            Write(expression_2[5:7])
        )
        self.wait()

        self.play(
            Write(expression_2[1]),
            Write(expression_2[4])
        )
        self.wait(0.5)

        self.play(Write(expression_2[7:]))
        self.wait()

        self.play(expression_2.animate.next_to(expression_1, DOWN).set_opacity(0.5))
        self.wait()

        expression_3 = MathTex('7b^2c', '-', '3b^2c', '=', '4b^2c', font_size=new_font_size)

        self.play(Write(expression_3[:3]))
        self.wait()

        self.play(Write(expression_3[3:]))
        self.wait()

        self.play(
            expression_3.animate.next_to(expression_2, DOWN),
            expression_1.animate.set_opacity(1),
            expression_2.animate.set_opacity(1)
        )
        self.wait()
