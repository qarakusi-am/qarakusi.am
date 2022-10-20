import numpy as np
from manim import FadeIn, Write, Tex, SurroundingRectangle, VGroup, Arrow, GrowArrow, FadeOut, AnimationGroup, rate_functions, Indicate, Circumscribe, MathTex
from manim import WHITE, UL, UR, DOWN, LEFT, BLUE, ORANGE, YELLOW, GREEN
from hanrahashiv import ReplaceItemsInFormula
from hanrahashiv import FormulaModificationsScene
from qarakusiscene import TaskNumberBox
from .text import *

FONT_SIZE = 65

class Problem12629(FormulaModificationsScene):
    def construct(self):
        self.wait()
        
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # 1-ին վարժ․
        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.1)
        prop_1.shift(DOWN)

        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 1.1, LEFT)

        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0).match_width(property_1_rect)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 1.1, LEFT)

        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait()

        task1_number = Tex("$1.$", font_size=FONT_SIZE).to_edge(UL, buff=.35).shift(DOWN)
        task1 = Tex("$x$", "$^3$", " $\cdot$ ", "$*$", " $=$ ", "$x$", "$^8$", font_size=FONT_SIZE).next_to(task1_number, buff=.2, aligned_edge=DOWN)
        self.play(Write(VGroup(task1_number, task1)))
        self.fix_formula(task1)
        self.wait()

        self.play(Indicate(prop_1))
        new_property_1 = property_1.copy()
        self.play(new_property_1.animate.next_to(task1, DOWN, .8, LEFT))
        self.fix_formula(new_property_1)
        self.wait()

        arrow1 = Arrow(start=task1[0].get_center()+np.array([0,-.1,0]), end=new_property_1[0], buff=.1)
        arrow2 = Arrow(start=task1[-2], end=new_property_1[-4], buff=.1)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait()
        self.play(
            task1[0].animate.set_color(ORANGE),
            task1[-2].animate.set_color(ORANGE),
            new_property_1[0].animate.set_color(ORANGE),
            new_property_1[3].animate.set_color(ORANGE),
            new_property_1[6].animate.set_color(ORANGE)
        )
        self.wait()
        self.play(
            Indicate(task1[0], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(task1[-2], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(new_property_1[0], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(new_property_1[3], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(new_property_1[6], rate_func=rate_functions.there_and_back_with_pause),
            run_time=2
        )
        self.wait()
        self.replace_items_in_formula(new_property_1, [0, 3, 6], ['x', 'x', 'x'])
        self.play(FadeOut(arrow1), FadeOut(arrow2))
        self.wait()

        arrow3 = Arrow(start=task1[1], end=new_property_1[1].get_center(), buff=.2)
        arrow4 = Arrow(start=task1[1], end=new_property_1[7].get_center(), stroke_width=3.5, max_tip_length_to_length_ratio=0.1, buff=.2)
        self.play(
            GrowArrow(arrow3),
            GrowArrow(arrow4)
        )
        self.wait()
        self.play(
            task1[1].animate.set_color(GREEN),
            new_property_1[1].animate.set_color(GREEN),
            new_property_1[7].animate.set_color(GREEN)
        )
        self.wait()
        self.play(
            Indicate(task1[1], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(new_property_1[1], rate_func=rate_functions.there_and_back_with_pause),
            Indicate(new_property_1[7], rate_func=rate_functions.there_and_back_with_pause),
            run_time=2
        )
        self.wait()
        self.play(ReplaceItemsInFormula(new_property_1, [1, 7], ['^3', '^3']))
        self.play(FadeOut(arrow3, arrow4))
        self.wait()

        arrow5 = Arrow(start=task1[-1].get_center()+np.array([0, .1, 0]), end=new_property_1[-2], buff=0.3)
        self.play(
            task1[-1].animate.set_color(ORANGE)
        )
        self.play(Indicate(task1[-1], rate_func=rate_functions.there_and_back_with_pause, run_time=2))
        self.play(
            GrowArrow(arrow5, rate_func=rate_functions.there_and_back_with_pause, run_time=4),
            AnimationGroup(
                FadeIn(SurroundingRectangle(new_property_1[-3:], color=BLUE, corner_radius=.2), rate_func=rate_functions.there_and_back_with_pause, run_time=4),
                ReplaceItemsInFormula(new_property_1, [9], ["$^5$"], colors=[YELLOW]),
                lag_ratio=.5
            )
        )
        self.wait()
        self.play(FadeOut(arrow5))
        self.wait()

        self.play(Circumscribe(new_property_1[4], fade_out=True))
        self.play(new_property_1[4].animate.set_color(YELLOW))
        self.play(ReplaceItemsInFormula(new_property_1, [4], ['^5']))
        self.wait()
        answer1 = MathTex("*", "=", "x", "^5", font_size=FONT_SIZE).next_to(task1, aligned_edge=DOWN, buff=1)
        answer1[2].set_color(ORANGE)
        answer1[3].set_color(YELLOW)
        self.play(Write(answer1))
        self.wait()

        self.play(FadeOut(new_property_1))
        self.wait()

        # 2-րդ վարժ.
        task2_number = Tex("$2.$", font_size=FONT_SIZE).next_to(task1_number, DOWN, buff=.7, aligned_edge=LEFT)
        task2 = Tex("$($", "$a$", "$^2$", "$)$", "$^4$", " $\\cdot$ ", "$($", "$a$", "$^3$", "$)$", "$^2$", " $=$ ", "$a$", "$^9$", " $\\cdot$ ", "$*$", font_size=FONT_SIZE).next_to(task2_number, buff=.2, aligned_edge=DOWN).shift(DOWN*.09)
        self.play(Write(VGroup(task2_number, task2)))
        self.fix_formula(task2)
        self.wait()

        # a^2^4 -> a^8
        self.play(Circumscribe(task2[:5], fade_out=True))
        self.wait()
        new_property_3 = property_3.copy()
        self.play(new_property_3.animate.next_to(task2, DOWN, buff=1, aligned_edge=LEFT))
        self.fix_formula(new_property_3)
        self.wait()

        arrow1 = Arrow(start=task2[2], end=new_property_3[2].get_center())
        arrow2 = Arrow(start=task2[2], end=new_property_3[7].get_center(), buff=.4)

        self.wait()
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            task2[2].animate.set_color(GREEN),
            new_property_3[2].animate.set_color(GREEN),
            new_property_3[7].animate.set_color(GREEN)
        )
        self.wait()
        self.replace_items_in_formula(new_property_3, [2, 7], ["$^2$", "$^2$"])
        self.play(FadeOut(arrow1, arrow2))
        self.wait()

        arrow3 = Arrow(start=task2[4], end=new_property_3[4].get_center())
        arrow4 = Arrow(start=task2[4], end=new_property_3[9].get_center(), buff=.4)
        self.play(
            GrowArrow(arrow3),
            GrowArrow(arrow4),
            task2[4].animate.set_color(YELLOW),
            new_property_3[4].animate.set_color(YELLOW),
            new_property_3[9].animate.set_color(YELLOW)
        )
        self.wait()
        self.replace_items_in_formula(new_property_3, [4, 9], ["$^4$", "$^4$"])
        self.play(FadeOut(arrow3, arrow4))
        self.wait()

        self.replace_items_in_formula(new_property_3, [7, 8, 9], ["$^8$", " ", " "])
        
        tex1 = Tex("$a$", "$^8$", font_size=FONT_SIZE).move_to(new_property_3, UR)
        self.add(tex1)

        self.play(
            FadeOut(new_property_3),
            task2[1].animate.set_color(WHITE)
        )

        self.play(tex1.animate.next_to(task2[1], DOWN, .3, LEFT))
        
        self.wait()

        # a^3^2 -> a^6
        self.play(Circumscribe(task2[6:11], fade_out=True))
        self.wait()
        new_property_3 = property_3.copy()
        
        tex2 = Tex("$a$", "$^6$", font_size=FONT_SIZE).next_to(task2[7], DOWN, .3, LEFT)
        self.play(Write(tex2))
        self.wait()

        # a^8 * a^6
        cdot_tex = Tex("$\\cdot$", font_size=FONT_SIZE).move_to(VGroup(tex1[0], tex2[0]))
        self.play(Write(cdot_tex))

        # a^8 * a^6 = a^14
        self.play(Indicate(prop_1))
        new_property_1 = property_1.copy()
        self.play(new_property_1.animate.next_to(tex1, DOWN, buff=.7, aligned_edge=LEFT))
        self.fix_formula(new_property_1)
        self.wait()

        arrow1 = Arrow(tex1[1].get_center(), new_property_1[1].get_center())
        arrow2 = Arrow(tex1[1].get_center(), new_property_1[7].get_center())
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            tex1[1].animate.set_color(GREEN),
            new_property_1[1].animate.set_color(GREEN),
            new_property_1[7].animate.set_color(GREEN)
        )
        self.wait()
        self.play(
            ReplaceItemsInFormula(new_property_1, [1, 7], ["$^8$", "$^8$"]),
            FadeOut(arrow1, arrow2)
        )
        self.wait()

        arrow3 = Arrow(tex2[1].get_center(), new_property_1[4].get_center())
        arrow4 = Arrow(tex2[1].get_center(), new_property_1[9].get_center())
        self.play(
            GrowArrow(arrow3),
            GrowArrow(arrow4),
            tex2[1].animate.set_color(YELLOW),
            new_property_1[4].animate.set_color(YELLOW),
            new_property_1[9].animate.set_color(YELLOW)
        )
        self.wait()
        self.play(
            ReplaceItemsInFormula(new_property_1, [4, 9], ["$^6$", "$^6$"]),
            FadeOut(arrow3, arrow4)
        )
        self.wait()

        self.replace_items_in_formula(new_property_1, [7, 8, 9], ["$^{14}$", " ", " "])
        self.wait()
        self.play(Circumscribe(task2[:11], fade_out=True))
        self.wait()

        self.play(Circumscribe(new_property_1[6:8], fade_out=True))
        self.wait()

        tex3 = Tex("$a$", "$^{14}$", font_size=FONT_SIZE).move_to(new_property_1, UR)
        self.add(tex3)
        self.play(FadeOut(new_property_1, tex1, tex2, cdot_tex))
        self.play(tex3.animate.next_to(task2, DOWN, buff=.8, aligned_edge=LEFT))

        modified_task2 = Tex("$a$", "$^{14}$", " $=$ ", "$a$", "$^9$", " $\\cdot$ ", "$*$", font_size=FONT_SIZE).next_to(task2, DOWN, buff=.8, aligned_edge=LEFT)
        modified_task2[3:].set_opacity(0)
        self.play(Write(modified_task2))
        self.remove(tex3)
        temp_tex = Tex("$a$", "$^9$", " $\\cdot$ ", "$*$", font_size=FONT_SIZE).move_to(task2, UR)
        self.play(temp_tex.animate.move_to(modified_task2, UR))
        modified_task2[3:].set_opacity(1)
        self.remove(temp_tex)
        self.wait()

        self.rearrange_formula(modified_task2, [3, 4, 5, 6, 2, 0, 1], [3, 4, 5, 6], [0, 1])
        self.wait()

        self.play(ReplaceItemsInFormula(modified_task2, [6], ["$^{9+5}$"]))
        self.wait()
        self.play(
            ReplaceItemsInFormula(modified_task2, [3], ["$a^5$"])
        )
        self.wait()
        
        self.play(FadeOut(modified_task2))
        answer2 = MathTex("*", "=", "a", "^5", font_size=FONT_SIZE).next_to(task2, DOWN, buff=.2, aligned_edge=LEFT)
        self.play(Write(answer2))
        self.wait()

        # 3-րդ վարժ.
        task3_number = Tex("$3.$", font_size=FONT_SIZE).next_to(task2_number, DOWN, buff=1.35, aligned_edge=LEFT)
        task3 = Tex("$($", "$*$", "$)$", "$^3$", " $=$ ", "$y$", "$^6$", font_size=FONT_SIZE).next_to(task3_number, buff=.2, aligned_edge=DOWN).shift(DOWN*.09)
        self.play(
            Write(task3_number),
            Write(task3)
        )
        self.wait()

        self.play(Indicate(prop_3))
        new_property_3 = property_3.copy()
        self.play(new_property_3.animate.next_to(task3, DOWN, 1, LEFT))
        self.fix_formula(new_property_3)

        arrow1 = Arrow(task3[3].get_center(), new_property_3[4].get_center())
        arrow2 = Arrow(task3[3].get_center(), new_property_3[9].get_center())
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            task3[3].animate.set_color(YELLOW),
            new_property_3[4].animate.set_color(YELLOW),
            new_property_3[9].animate.set_color(YELLOW)
        )
        self.wait()
        self.play(
            ReplaceItemsInFormula(new_property_3, [4, 9], ["$^3$", "$^3$"]),
            FadeOut(arrow1, arrow2)
        )
        self.wait()

        arrow3 = Arrow(task3[5].get_center(), new_property_3[1].get_center())
        arrow4 = Arrow(task3[5].get_center(), new_property_3[6].get_center())
        self.play(
            GrowArrow(arrow3),
            GrowArrow(arrow4),
            task3[5].animate.set_color(ORANGE),
            new_property_3[1].animate.set_color(ORANGE),
            new_property_3[6].animate.set_color(ORANGE)
        )
        self.wait()
        self.play(
            ReplaceItemsInFormula(new_property_3, [1, 6], ["$y$", "$y$"]),
            FadeOut(arrow3, arrow4)
        )
        self.wait()

        srr_rect = SurroundingRectangle(new_property_3[7:], corner_radius=.2, color=BLUE)
        arrow5 = Arrow(task3[6].get_center(), srr_rect.get_center())
        self.play(
            GrowArrow(arrow5),
            FadeIn(srr_rect)
        )
        self.wait()
        self.play(
            ReplaceItemsInFormula(new_property_3, [2, 7], ["$^2$", "$^2$"]),
            FadeOut(arrow5, srr_rect)
        )
        self.wait()

        answer3 = Tex("$*$", " $=$ ", "$y$", "$^2$", font_size=FONT_SIZE).next_to(task3, buff=1.1)
        answer3[2].set_color(ORANGE)
        self.play(Write(answer3))
        self.play(FadeOut(new_property_3))
        self.wait()

        # 4-րդ վարժ.
        task4_number = Tex("$4.$", font_size=FONT_SIZE).next_to(task3_number, DOWN, buff=.7, aligned_edge=LEFT)
        task4 = Tex("$($", "$*$", "$)$", "$^5$", " $\\cdot$ ", "$($", "$a$", "$^3$", "$)$", "$^4$", " $=$ ", "$($", "$a$", "$^4$", "$)$", "$^6$", " $\\cdot$ ", "$a$", "$^3$", " $\\cdot$ ", "$a$", "$^5$", font_size=FONT_SIZE).next_to(task4_number, buff=.2, aligned_edge=DOWN).shift(DOWN*.09)
        self.play(
            Write(task4_number),
            Write(task4)
        )
        self.wait()



        self.wait(2)
