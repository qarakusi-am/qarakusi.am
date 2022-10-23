from codecs import replace_errors
from manim import *

from hanrahashiv import *




class Exercise_2_false(FormulaModificationsScene, MovingCameraScene):
    def construct(self):
        property_font_size = 65

        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.11)
        prop_1.shift(DOWN+LEFT*.2)

        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 1.1, LEFT)

        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 1.1, LEFT)







        # self.add(prop_1, prop_2, prop_3)

        self.wait(0.5)

        left_boundary = [-6.5, 0, 0]
        up_boundary = [0, 3, 0]

        font_size = 55

    # գրում ենք առաջին վարժությունը
        first = Tex('$1)$', font_size=property_font_size).align_to(left_boundary, LEFT).align_to(up_boundary, UP)
        first_exercise = Tex( '$($', '$y$', '$^2$', '$x$', '$^3$', '$)$', '$^4$', '$=$', # [0:8]
        '$($', '$y$', '$^2$', '$)$', '$^4$', '$\cdot$', '$($', '$x$', '$^3$', '$)$', '$^4$', '$=$', # [8:20]
        '$y$', '$^8$', '$\cdot$', '$x$', '$^{12}$', # [20:25]
        font_size=font_size).next_to(first, RIGHT)
        first_exercise[9:11].set_color(ORANGE)
        first_exercise[15:17].set_color(GREEN)
        first_exercise[22].set_opacity(0.5)
        VGroup(first_exercise[12], first_exercise[18]).set_color(YELLOW)

        self.play(Write(first))
        self.wait(0.25)

        self.play(Write(first_exercise[0:7]))
        self.wait(0.5)

        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait(0.5)

        self.play(Circumscribe(first_exercise[:6], time_width=2))
        self.wait(0.25)

        self.play(Circumscribe(first_exercise[6], shape=Circle, time_width=2))
        self.wait(0.25)

        self.play(Indicate(first_exercise[1:5]))
        self.wait(0.5)

    # երկրորդ հատկությունը բերում ենք ներքև
        self.play(Indicate(prop_2))
        self.wait(0.5)

        property_2_copy = property_2.copy()

        self.play(
            property_2_copy.animate.scale(font_size/property_font_size),
            property_2_copy.animate.next_to(first_exercise, 2 * DOWN).align_to(first_exercise, LEFT)
        )
        self.wait(0.5)
    
    # a = y^2
        self.play(
            VGroup(first_exercise[1:3], property_2_copy[1], property_2_copy[7]).animate.set_color(ORANGE),
            VGroup(first_exercise[3:5], property_2_copy[3], property_2_copy[10]).animate.set_color(GREEN)
        )
        self.wait(0.25)

        exp = Tex('$($', '$y$', '$^2$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$',
        '$($', '$y$', '$^2$', '$)$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=property_font_size).align_to(property_2_copy, DL)
        exp[1:3].set_color(ORANGE)
        exp[9:11].set_color(ORANGE)
        exp[4].set_color(GREEN)
        exp[14].set_color(GREEN)

        self.play(
            first_exercise[1:3].animate.scale(1.5),
            property_2_copy[1].animate.scale(1.5),
            property_2_copy[7].animate.scale(1.5)
        )
        self.wait(0.25)

        self.play(
            ReplacementTransform(property_2_copy[0], exp[0]),
            ReplacementTransform(property_2_copy[1], exp[1:3]),
            ReplacementTransform(property_2_copy[2:7], exp[3:8]),
            ReplacementTransform(property_2_copy[7], exp[8:12]),
            ReplacementTransform(property_2_copy[8:], exp[12:]),
            first_exercise[1:3].animate.scale(1/1.5)
        )
        self.wait(0.5)
        property_2_copy = exp

    # b = x^3
        exp = Tex('$($', '$y$', '$^2$', '$\cdot$', '$x$', '$^3$', '$)$', '$^n$', '$=$', # [0:9]
        '$($', '$y$', '$^2$', '$)$', '$^n$', '$\cdot$', '$($', '$x$', '$^3$', '$)$', '$^n$', # [9:20]
        font_size=property_font_size).align_to(property_2_copy, DL)
        exp[1:3].set_color(ORANGE)
        exp[10:12].set_color(ORANGE)
        exp[4:6].set_color(GREEN)
        exp[16:18].set_color(GREEN)

        self.play(
            first_exercise[3:5].animate.scale(1.5),
            property_2_copy[4].animate.scale(1.5),
            property_2_copy[14].animate.scale(1.5)
        )
        self.wait(0.25)


        self.play(
            ReplacementTransform(property_2_copy[:4], exp[:4]),
            ReplacementTransform(property_2_copy[4], exp[4:6]),
            ReplacementTransform(property_2_copy[5:14], exp[6:15]),
            ReplacementTransform(property_2_copy[14], exp[15:19]),
            ReplacementTransform(property_2_copy[15], exp[19]),
            first_exercise[3:5].animate.scale(1/1.5)
        )
        self.wait(0.5)
        property_2_copy = exp

    # n = 4
        self.play(
            first_exercise[6].animate.set_color(YELLOW),
            property_2_copy[7].animate.set_color(YELLOW),
            property_2_copy[13].animate.set_color(YELLOW),
            property_2_copy[19].animate.set_color(YELLOW)
        )
        self.wait(0.25)

        self.play(
            first_exercise[6].animate.scale(1.5),
            property_2_copy[7].animate.scale(1.5),
            property_2_copy[13].animate.scale(1.5),
            property_2_copy[19].animate.scale(1.5)
        )
        self.wait(0.25)

        exp = Tex('$($', '$y$', '$^2$', '$\cdot$', '$x$', '$^3$', '$)$', '$^4$', '$=$', # [0:9]
        '$($', '$y$', '$^2$', '$)$', '$^4$', '$\cdot$', '$($', '$x$', '$^3$', '$)$', '$^4$', # [9:20]
        font_size=property_font_size).align_to(property_2_copy, DL)
        exp[1:3].set_color(ORANGE)
        exp[10:12].set_color(ORANGE)
        exp[4:6].set_color(GREEN)
        exp[16:18].set_color(GREEN)
        exp[7].set_color(YELLOW)
        exp[13].set_color(YELLOW)
        exp[19].set_color(YELLOW)

        self.play(
            ReplacementTransform(property_2_copy, exp),
            first_exercise[6].animate.scale(1/1.5)
        )
        self.wait(0.5)
        property_2_copy = exp

        self.play(Write(first_exercise[7]))
        self.wait(0.25)

        self.play(
            ReplacementTransform(property_2_copy[9:20], first_exercise[8:19]),
            FadeOut(property_2_copy[:9])
        )
        self.wait(0.5)

        self.play(first_exercise[:19].animate.set_color(WHITE))
        self.wait(0.5)

        self.play(Indicate(first_exercise[8:13]))
        self.wait(0.5)
        
        self.play(Indicate(first_exercise[13]))
        self.wait(0.5)

        self.play(Indicate(first_exercise[14:19]))
        self.wait(0.5)

        ex = first_exercise[8:13]

        self.play(
            ex.animate.scale(property_font_size/font_size),
            first_exercise[13:19].animate.set_opacity(0.5)
        )

        self.play(Indicate(prop_3))
        self.wait(0.5)

        property_3_copy = property_3.copy()

        self.play(property_3_copy.animate.next_to(ex, 2 * DOWN).align_to(ex, LEFT))
        self.wait(0.5)

    # a = y
        exp = Tex('$($', '$y$', '$^m$', '$)$', '$^n$', '$=$', '$y$', '$^m$', '$^\cdot$', '$^n$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)

        self.play(
            ex[1].animate.scale(1.5).set_color(GREEN),
            property_3_copy[1].animate.scale(1.5).set_color(GREEN),
            property_3_copy[6].animate.scale(1.5).set_color(GREEN)
        )
        self.wait(0.25)

        self.play(
            ex[1].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # m = 2
        exp = Tex('$($', '$y$', '$^2$', '$)$', '$^n$', '$=$', '$y$', '$^2$', '$^\cdot$', '$^n$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        VGroup(exp[2], exp[7]).set_color(RED)

        self.play(
            ex[2].animate.scale(1.5).set_color(RED),
            property_3_copy[2].animate.scale(1.5).set_color(RED),
            property_3_copy[7].animate.scale(1.5).set_color(RED)
        )
        self.wait(0.25)

        self.play(
            ex[2].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # n = 4
        exp = Tex('$($', '$y$', '$^2$', '$)$', '$^4$', '$=$', '$y$', '$^2$', '$^\cdot$', '$^4$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        VGroup(exp[2], exp[7]).set_color(RED)
        VGroup(exp[4], exp[9]).set_color(YELLOW)

        self.play(
            ex[4].animate.scale(1.5).set_color(YELLOW),
            property_3_copy[4].animate.scale(1.5).set_color(YELLOW),
            property_3_copy[9].animate.scale(1.5).set_color(YELLOW)
        )
        self.wait(0.25)

        self.play(
            ex[4].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # 2 * 4 = 8
        exp = Tex('$($', '$y$', '$^2$', '$)$', '$^4$', '$=$', '$y$', '$^8$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        exp[2].set_color(RED)
        exp[4].set_color(YELLOW)
        exp[7].set_color(ORANGE)

        self.play(
            ReplacementTransform(property_3_copy[:7], exp[:7]),
            ReplacementTransform(property_3_copy[7:], exp[7])
        )
        self.wait(0.5)
        property_3_copy = exp

        self.play(Write(first_exercise[19]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(property_3_copy[6:].copy(), first_exercise[20:22]),
            first_exercise[8:13].animate.scale(font_size/property_font_size).set_color(WHITE)
        )
        self.wait(0.5)

        self.play(Write(first_exercise[22]))
        self.wait(0.5)

        exp = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)

        self.play(
            first_exercise[8:14].animate.set_opacity(0.5),
            first_exercise[14:19].animate.scale(property_font_size/font_size).set_opacity(1),
            ReplacementTransform(property_3_copy, exp),
            first_exercise[20:23].animate.set_opacity(0.5)
        )
        self.wait(0.5)

        ex = first_exercise[14:19]
        property_3_copy = exp



    # a = x
        exp = Tex('$($', '$x$', '$^m$', '$)$', '$^n$', '$=$', '$x$', '$^m$', '$^\cdot$', '$^n$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)

        self.play(
            ex[1].animate.scale(1.5).set_color(GREEN),
            property_3_copy[1].animate.scale(1.5).set_color(GREEN),
            property_3_copy[6].animate.scale(1.5).set_color(GREEN)
        )
        self.wait(0.25)

        self.play(
            ex[1].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # m = 3
        exp = Tex('$($', '$x$', '$^3$', '$)$', '$^n$', '$=$', '$x$', '$^3$', '$^\cdot$', '$^n$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        VGroup(exp[2], exp[7]).set_color(RED)

        self.play(
            ex[2].animate.scale(1.5).set_color(RED),
            property_3_copy[2].animate.scale(1.5).set_color(RED),
            property_3_copy[7].animate.scale(1.5).set_color(RED)
        )
        self.wait(0.25)

        self.play(
            ex[2].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # n = 4
        exp = Tex('$($', '$x$', '$^3$', '$)$', '$^4$', '$=$', '$x$', '$^3$', '$^\cdot$', '$^4$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        VGroup(exp[2], exp[7]).set_color(RED)
        VGroup(exp[4], exp[9]).set_color(YELLOW)

        self.play(
            ex[4].animate.scale(1.5).set_color(YELLOW),
            property_3_copy[4].animate.scale(1.5).set_color(YELLOW),
            property_3_copy[9].animate.scale(1.5).set_color(YELLOW)
        )
        self.wait(0.25)

        self.play(
            ex[4].animate.scale(1/1.5),
            ReplacementTransform(property_3_copy, exp)
        )
        self.wait(0.5)
        property_3_copy = exp

    # 3 * 4 = 12
        exp = Tex('$($', '$x$', '$^3$', '$)$', '$^4$', '$=$', '$x$', '$^{12}$', font_size=property_font_size)
        exp.align_to(property_3_copy, DL)
        VGroup(exp[1], exp[6]).set_color(GREEN)       
        exp[2].set_color(RED)
        exp[4].set_color(YELLOW)
        exp[7].set_color(ORANGE)

        self.play(
            ReplacementTransform(property_3_copy[:7], exp[:7]),
            ReplacementTransform(property_3_copy[7:], exp[7])
        )
        self.wait(0.5)
        property_3_copy = exp

        self.play(
            ReplacementTransform(property_3_copy[6:].copy(), first_exercise[23:25]),
            first_exercise[14:19].animate.scale(font_size/property_font_size).set_color(WHITE),
            FadeOut(property_3_copy)
        )
        self.wait(0.5)

        self.play(
            first_exercise[8:14].animate.set_opacity(1),
            first_exercise[20:23].animate.set_opacity(1)
        )
        self.wait(0.5)

        self.rearrange_formula(first_exercise,
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 22, 20, 21],
        [23, 24], [], [22], [])
        self.wait(0.25)

        self.play(RemoveItemsFromFormula(first_exercise, [22]))
        self.wait(0.5)










    # Երկրորդ վարժություն
        second = Tex('$2)$', font_size=property_font_size).align_to(first, LEFT).next_to(first, DOWN, buff=1)
        second_exercise = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', # [:7]
        '$=$', # [7]
        '$2$', '$^3$', '$\cdot$', '$($', '$a$', '$^2$', '$)$', '$^3$', # [8:16]
        # '$=$', # [16]
        # '$8$', '$\cdot$', '$$', '$$', '$$',
        font_size=font_size).next_to(second, RIGHT)
        second_exercise[8].set_color(ORANGE)
        second_exercise[12:14].set_color(GREEN)
        VGroup(second_exercise[9], second_exercise[15]).set_color(YELLOW)


        self.play(Write(second))
        self.wait(0.5)

        self.play(Write(second_exercise[:7]))
        self.wait(0.5)

    # երկրորդ հատկությունը բերում ենք ներքև
        self.play(Indicate(prop_2))
        self.wait(0.5)

        property_2_copy = property_2.copy()

        self.play(property_2_copy.animate.next_to(second_exercise, 2 * DOWN).align_to(second_exercise, LEFT))
        self.wait(0.5)

        self.play(
            second_exercise[1].animate.set_color(ORANGE),
            VGroup(property_2_copy[1], property_2_copy[7]).animate.set_color(ORANGE),
            second_exercise[3:5].animate.set_color(GREEN),
            VGroup(property_2_copy[3], property_2_copy[10]).animate.set_color(GREEN)
        )
        self.wait(0.5)
    
    # a = 2
        self.play(
            second_exercise[1].animate.scale(1.5),
            property_2_copy[1].animate.scale(1.5),
            property_2_copy[7].animate.scale(1.5)
        )
        self.wait(0.5)

        self.play(
            ModifyFormula(property_2_copy, replace_items=[[1], [7]], replace_items_strs=[['$2$'], ['$2$']]),
            second_exercise[1].animate.scale(1/1.5)
        )
        self.wait(0.5)

    # b = a^2
        self.play(
            second_exercise[3:5].animate.scale(1.5),
            property_2_copy[3].animate.scale(1.5),
            property_2_copy[10].animate.scale(1.5)
        )
        self.wait(0.5)

        self.play(
            ModifyFormula(
                property_2_copy, replace_items=[[3], [10]],
                replace_items_strs=[['$a$', '$^2$'], ['$($', '$a$', '$^2$', '$)$']],
                replace_items_colors=[[], [WHITE, GREEN, GREEN, WHITE]]
            ),
            second_exercise[3:5].animate.scale(1/1.5)
        )
        self.wait(0.5)

    # n = 3
        self.play(
            second_exercise[6].animate.scale(1.5).set_color(YELLOW),
            property_2_copy[6].animate.scale(1.5).set_color(YELLOW),
            property_2_copy[9].animate.scale(1.5).set_color(YELLOW),
            property_2_copy[15].animate.scale(1.5).set_color(YELLOW)
        )
        self.wait(0.5)

        self.play(
            ModifyFormula(
                property_2_copy, replace_items=[[6], [9], [15]],
                replace_items_strs=[['$^3$'], ['$^3$'], ['$^3$']]
            ),
            second_exercise[6].animate.scale(1/1.5)
        )
        self.wait(0.5)

    # հավասարության 2-րդ մասը
        self.play(Write(second_exercise[7]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(property_2_copy[8:16], second_exercise[8:16]),
            FadeOut(property_2_copy[:8])
        )
        self.wait(0.5)

        self.play(second_exercise.animate.set_color(WHITE))
        self.wait(0.5)
        
    # 2^3 = 2 * 2 * 2 = 8
        self.play(second_exercise[8:10].animate.set_color(YELLOW).scale(1.5))
        self.wait(0.01)
        self.play(second_exercise[8:10].animate.scale(1/1.5))
        self.wait(0.5)

        self.play(
            ModifyFormula(second_exercise, replace_items=[[9]],
            replace_items_strs=[['$\cdot$', '$2$', '$\cdot$', '$2$']],
            replace_items_colors=[[WHITE, YELLOW, WHITE, YELLOW]])
        )
        self.wait(0.5)

        self.play(
            ModifyFormula(second_exercise,
            replace_items=[[8, 9, 10, 11, 12]],
            replace_items_strs=[['$8$']],
            replace_items_colors=[[YELLOW]])
        )
        self.wait(0.5)

        self.play(second_exercise[8].animate.set_color(WHITE))

    # (a^2)^3 = a^6
      # a = a 
        self.play(Indicate(prop_3))
        self.wait(0.5)

        property_3_copy = property_3.copy()

        self.play(property_3_copy.animate.next_to(second_exercise, DOWN, buff=0.5).align_to(second_exercise[10], LEFT))
        self.wait(0.5)

        self.play(
            second_exercise[11].animate.scale(1.5).set_color(RED),
            property_3_copy[1].animate.scale(1.5).set_color(RED),
            property_3_copy[6].animate.scale(1.5).set_color(RED)
        )
        self.wait(0.25)

        self.play(
            second_exercise[11].animate.scale(1/1.5),
            property_3_copy[1].animate.scale(1/1.5),
            property_3_copy[6].animate.scale(1/1.5)
        )
        self.wait(0.5)

      # m = 2
        self.play(
            second_exercise[12].animate.scale(1.5).set_color(BLUE),
            property_3_copy[2].animate.scale(1.5).set_color(BLUE),
            property_3_copy[7].animate.scale(1.5).set_color(BLUE)
        )
        self.wait(0.25)

        self.fix_formula(property_3_copy)

        self.play(
            second_exercise[12].animate.scale(1/1.5),
            ModifyFormula(
                property_3_copy,
                replace_items=[[2], [7]],
                replace_items_strs=[['$^2$'], ['$^2$']]
            )
        )
        self.wait(0.5)
      
      # n = 3
        self.play(
            second_exercise[14].animate.scale(1.5).set_color(ORANGE),
            property_3_copy[4].animate.scale(1.5).set_color(ORANGE),
            property_3_copy[9].animate.scale(1.5).set_color(ORANGE)
        )
        self.wait(0.25)

        self.play(
            second_exercise[14].animate.scale(1/1.5),
            ModifyFormula(
                property_3_copy,
                replace_items=[[4], [9]],
                replace_items_strs=[['$^3$'], ['$^3$']]
            )
        )
        self.wait(0.5)

        self.fix_formula(property_3_copy)

      # 2*3=6
        self.play(
            ModifyFormula(
                property_3_copy,
                replace_items=[[7, 8, 9]],
                replace_items_strs=[['$^6$']],
                replace_items_colors=[[GREEN]]
            )
        )
        self.wait(0.5)

    # ավարտում ենք երկրորդ վարժը
        self.play(
            ModifyFormula(
                second_exercise,
                replace_items=[[9, 10, 11, 12, 13, 14]],
                replace_items_strs=[['$a$', '$^6$']],
                replace_items_colors=[[RED, GREEN]]
            )
        )
        self.play(FadeOut(property_3_copy))
        self.wait(0.5)
        
        self.play(second_exercise[9:11].animate.set_color(WHITE))
        self.wait(0.5)















    # Երկրորդի սխալ լուծում 
        left_boundary_2 = [-12.75, 0, 0]

        dash_line = DashedLine([-6.75, 4, 0], [-6.75, -6, 0])
        
        first_2 = Tex('$1.$', font_size=property_font_size).align_to(left_boundary, LEFT).next_to(second, DOWN, buff=1)
        first_exercise_2 = Tex('$($', '$y$', '$^2$', '$x$', '$^3$', '$)$', '$^4$', # [0:7]
        '$=$', #[7]
        '$x$', '$^{12}$', '$y$', '$^8$', # [8:12]
        font_size=font_size).next_to(first_2, RIGHT)

        second_exercise_2 = Tex('$($', '$2$', '$\cdot$', '$a$', '$^2$', '$)$', '$^3$', # [0:7]
        '$=$', #[7]
        '$2$', '$\cdot$', '$3$', '$\cdot$', '$a$', '$^2$', '$^\cdot$', '$^3$', # [8:16]
        font_size=font_size).next_to(first_exercise_2, DOWN, buff=1).align_to(first_exercise_2, LEFT)
        second_exercise_2[8].set_color(ORANGE)
        second_exercise_2[10].set_color(YELLOW)
        second_exercise_2[13].set_color(GREEN)
        second_exercise_2[15].set_color(YELLOW)

        # self.add(first_2, first_exercise_2)


        # self.play(self.camera.frame.animate.scale(1.1)) # .shift(5 * LEFT)
        # self.wait(0.25)

        # self.play(self.camera.frame.animate.shift(6 * LEFT))
        # self.wait(0.25)

        # self.play(self.camera.frame.animate.scale(1/1.1)) # .shift(9 * LEFT)
        # self.wait(0.5)

        # self.play(Create(dash_line))
        # self.wait(0.5)

        self.play(
            ReplacementTransform(second_exercise[:8].copy(), second_exercise_2[:8]),
            second_exercise.animate.set_opacity(0.5),
            second.animate.set_opacity(0.5)
        )
        self.wait(0.25)

        self.play(
            ReplacementTransform(first_exercise[:8].copy(), first_exercise_2[:8]),
            ReplacementTransform(first_exercise[20:24].copy(), first_exercise_2[8:12]),
            first_exercise.animate.set_opacity(0.5),
            first.animate.set_opacity(0.5)
        )
        self.wait(0.25)

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
        self.wait(0.25)

        self.play(
            Indicate(first_exercise_2[2], scale_factor=1.5), 
            Indicate(first_exercise_2[6], scale_factor=1.5),
            Indicate(first_exercise_2[11], scale_factor=1.5, color=RED)
        )
        self.wait(0.5)

        self.play(
            Indicate(first_exercise_2[4], scale_factor=1.5),
            Indicate(first_exercise_2[6], scale_factor=1.5),
            Indicate(first_exercise_2[9], scale_factor=1.5, color=BLUE)
        )
        self.wait(0.5)

        self.play(second_exercise_2[1].animate.set_color(ORANGE))
        self.wait(0.25)

        self.play(ReplacementTransform(second_exercise_2[1].copy(), second_exercise_2[8]))
        self.wait(0.5)

        self.play(Write(second_exercise_2[9]))
        self.wait(0.5)

        self.play(second_exercise_2[6].animate.set_color(YELLOW))
        self.wait(0.25)

        self.play(ReplacementTransform(second_exercise_2[6].copy(), second_exercise_2[10]))
        self.wait(0.5)

        self.play(Write(second_exercise_2[11:13]))
        self.wait(0.5)

        self.play(second_exercise_2[4].animate.set_color(GREEN))
        self.wait(0.25)
        
        self.play(ReplacementTransform(second_exercise_2[4].copy(), second_exercise_2[13]))
        self.wait(0.5)

        self.play(Write(second_exercise_2[14]))
        self.wait(0.5)

        self.play(ReplacementTransform(second_exercise_2[6].copy(), second_exercise_2[15]))
        self.wait(0.5)

        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[8, 9, 10], [13, 14, 15]],
                replace_items_strs=[['$6$'], ['$^6$']],
                replace_items_colors=[[ORANGE], [GREEN]],
                remove_items=[11]
            )
        )
        self.wait(0.5)

        self.play(second_exercise_2.animate.set_color(WHITE))
        self.wait(0.5)

        self.play(
            second_exercise[8:11].animate.set_opacity(1)
        )
        self.wait(0.5)

        self.play(
            Circumscribe(second_exercise[8], color=BLUE, time_width=2),
            second_exercise[8].animate.set_color(BLUE),
            Circumscribe(second_exercise_2[8], color=RED, time_width=2),
            second_exercise_2[8].animate.set_color(RED)
        )
        self.wait(0.5)

    # դիտարկում ենք առաջին վարժությունը
        self.play(
            Indicate(first_exercise_2[2]),
            Indicate(first_exercise_2[4])
        )
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(second_exercise[8:11].animate.set_opacity(0.5))
        self.wait(0.5)

        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[0],
                add_items_strs=[['$1$', '$\cdot$']]
            )
        ) # (1 * y^2 x^3)^4 = y^8 x^12
        self.wait(0.5)

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
        self.wait(0.5)

        self.play(
            ModifyFormula(
                first_exercise_2,
                replace_items=[[10, 11, 12]],
                replace_items_strs=[['$4$']],
                replace_items_colors=[[WHITE]]
            )
        ) # (1 * y^2x^3)^4 = 4 y^8 x^12
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[1],
                add_items_strs=[['$^1$']]
            )
        )
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(
            Indicate(first_exercise_2[1], scale_factor=1.5, color=ORANGE),
            Indicate(first_exercise_2[4], scale_factor=1.5, color=BLUE),
            Indicate(first_exercise_2[6], scale_factor=1.5, color=PINK)
        )
        self.wait(0.5)


        self.play(
            Indicate(first_exercise_2[2], scale_factor=1.5, color=GREEN),
            Indicate(first_exercise_2[9], scale_factor=1.5)
        )

        self.play(
            ModifyFormula(
                first_exercise_2,
                replace_items=[[11]],
                replace_items_strs=[['$1$']],
                replace_items_colors=[[ORANGE]]
            )
        ) # (1^1 * y^2x^3)^4 = 1^{1*4} y^8 x^12
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(
            ModifyFormula(
                first_exercise_2,
                add_after_items=[11],
                add_items_strs=[['$^1$', '$^\cdot$', '$^4$']],
                add_items_colors=[[GREEN, WHITE, YELLOW]]
            )
        )
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(
            ModifyFormula(
                first_exercise_2,
                replace_items=[[12, 13, 14]],
                replace_items_strs=[['$^4$']]
            )
        )
        self.wait(0.5)

        self.fix_formula(first_exercise_2)

        self.play(
            ModifyFormula(
                first_exercise_2,
                remove_items=[12]
            )
        )
        self.wait(0.5)

        self.play(Indicate(second_exercise_2))
        self.wait(0.5)

        self.fix_formula(second_exercise_2)

        self.play(
            ModifyFormula(
                second_exercise_2,
                add_after_items=[1],
                add_items_strs=[['$^1$']],
                replace_items=[[8]],
                replace_items_strs=[['$2$']],
                replace_items_colors=[[ORANGE]]
            ),
            second_exercise_2[1].animate.set_color(ORANGE)
        )
        self.wait(0.5)

        self.play(
            Indicate(second_exercise_2[2], scale_factor=1.5, color=BLUE),
            Indicate(second_exercise_2[7], scale_factor=1.5)
        )
        self.wait(0.5)

        self.fix_formula(second_exercise_2)

        self.play(
            ModifyFormula(
                second_exercise_2,
                add_after_items=[9],
                add_items_strs=[['$^1$', '$^\cdot$', '$^3$']],
                add_items_colors=[[BLUE, WHITE, YELLOW]]
            )
        )
        self.wait(0.5)

        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[10, 11, 12]],
                replace_items_strs=[['^3']],
                replace_items_colors=[[WHITE]]
            )
        )
        self.play(
            ModifyFormula(
                second_exercise_2,
                replace_items=[[9, 10]],
                replace_items_strs=[['$8$']],
                replace_items_colors=[[ORANGE]]
            )
        )
        self.wait(0.5)

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
        self.wait(0.5)

    # Երրորդ վարժություն
        third = Tex('$3$', '$)$', font_size=property_font_size).align_to(second, LEFT).next_to(second, DOWN, buff=1)
        third_exercise = Tex('$2$', '$($', '$a$', '$^2$', '$)$', '$^3$', # [0:6]
        '$=$', # [6]
        '$2$', '$a$', '$^6$', # [7:10]
        font_size=font_size).next_to(third, RIGHT)
        third_exercise[8].set_color(RED)
        third_exercise[9].set_color(GREEN)

        self.play(Write(third))
        self.wait(0.5)

        self.play(Write(third_exercise[:6]))
        self.wait(0.5)


    # տարբերում ենք նախորդ վարժությունից
        self.play(
            Indicate(third_exercise[0], scale_factor=1.5),
            Indicate(second_exercise[1], scale_factor=1.5)
        )
        self.wait(0.25)

        self.play(
            Indicate(third_exercise[1], scale_factor=1.5, color=RED),
            Indicate(third_exercise[4], scale_factor=1.5, color=RED),
            Indicate(second_exercise[0], scale_factor=1.5, color=RED),
            Indicate(second_exercise[5], scale_factor=1.5, color=RED)
        )
        self.wait(0.5)

        self.play(Indicate(third_exercise[1:6], scale_factor=1.5))
        self.wait(0.5)

        # self.play(
        #     ModifyFormula(
        #         third_exercise,
        #         add_after_items=[0],
        #         add_items_strs=[['$\cdot$']]
        #     )
        # )
        # self.fix_formula(third_exercise)
        # self.wait(0.5)

    # (a^2)^3 = a^6
      # a = a 
        self.play(Indicate(prop_3))
        self.wait(0.5)

        property_3_copy = property_3.copy()

        self.play(property_3_copy.animate.next_to(third_exercise, DOWN, buff=0.5).align_to(third_exercise[1], LEFT))
        self.wait(0.5)

        self.play(
            third_exercise[2].animate.scale(1.5).set_color(RED),
            property_3_copy[1].animate.scale(1.5).set_color(RED),
            property_3_copy[6].animate.scale(1.5).set_color(RED)
        )
        self.wait(0.25)

        self.play(
            third_exercise[2].animate.scale(1/1.5),
            property_3_copy[1].animate.scale(1/1.5),
            property_3_copy[6].animate.scale(1/1.5)
        )
        self.wait(0.5)

      # m = 2
        self.play(
            third_exercise[3].animate.scale(1.5).set_color(BLUE),
            property_3_copy[2].animate.scale(1.5).set_color(BLUE),
            property_3_copy[7].animate.scale(1.5).set_color(BLUE)
        )
        self.wait(0.25)

        self.fix_formula(property_3_copy)

        self.play(
            third_exercise[3].animate.scale(1/1.5),
            ModifyFormula(
                property_3_copy,
                replace_items=[[2], [7]],
                replace_items_strs=[['$^2$'], ['$^2$']]
            )
        )
        self.wait(0.5)
      
      # n = 3
        self.play(
            third_exercise[5].animate.scale(1.5).set_color(ORANGE),
            property_3_copy[4].animate.scale(1.5).set_color(ORANGE),
            property_3_copy[9].animate.scale(1.5).set_color(ORANGE)
        )
        self.wait(0.25)

        self.play(
            third_exercise[5].animate.scale(1/1.5),
            ModifyFormula(
                property_3_copy,
                replace_items=[[4], [9]],
                replace_items_strs=[['$^3$'], ['$^3$']]
            )
        )
        self.wait(0.5)

        self.fix_formula(property_3_copy)

      # 2*3=6
        self.play(
            ModifyFormula(
                property_3_copy,
                replace_items=[[7, 8, 9]],
                replace_items_strs=[['$^6$']],
                replace_items_colors=[[GREEN]]
            )
        )
        self.wait(0.5)

        self.play(Write(third_exercise[6]))
        self.wait(0.5)

        self.play(ReplacementTransform(third_exercise[0].copy(), third_exercise[7]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(property_3_copy[6:], third_exercise[8:]),
            FadeOut(property_3_copy[:6])
        )
        self.wait(0.25)

        self.play(third_exercise.animate.set_color(WHITE))
        self.wait(0.5)

    

