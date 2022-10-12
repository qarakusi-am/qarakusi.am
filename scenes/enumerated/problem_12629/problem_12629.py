import numpy as np
from manim import FadeIn, Write, Tex, SurroundingRectangle, VGroup, Arrow, GrowArrow, FadeOut, AnimationGroup, rate_functions, Indicate, Circumscribe
from manim import WHITE, UL, UR, DOWN, LEFT, BLUE, ORANGE, YELLOW, GREEN
from hanrahashiv import AddItemsInFormula, ReplaceItemsInFormula, RemoveItemsFromFormula
from hanrahashiv import FormulaModificationsScene
from qarakusiscene import TaskNumberBox
from .text import *

FONT_SIZE = 65

class Problem12629(FormulaModificationsScene):
    def construct(self):
        self.wait()
        # 1-ին վարժ․
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.11)
        prop_1.shift(DOWN)

        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 1.1, LEFT)

        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 1.1, LEFT)

        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait()

        task1_number = Tex("$1.$", font_size=FONT_SIZE).to_edge(UL, buff=.4).shift(DOWN)
        task1 = Tex("$x$", "$^3$", " $\cdot$ ", "$*$", " $=$ ", "$x$", "$^8$", font_size=FONT_SIZE).next_to(task1_number, buff=.2, aligned_edge=DOWN)
        self.play(Write(VGroup(task1_number, task1)))
        self.fix_formula(task1)
        self.wait()

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
            AnimationGroup(
                GrowArrow(arrow5, rate_func=rate_functions.there_and_back_with_pause, run_time=4),
                AnimationGroup(
                    FadeIn(SurroundingRectangle(new_property_1[-3:], color=BLUE, corner_radius=.2), rate_func=rate_functions.there_and_back_with_pause, run_time=4),
                    AnimationGroup(
                        ReplaceItemsInFormula(new_property_1, [9], ['^5'], colors=[YELLOW])
                    ),
                    lag_ratio=.5
                )
            )
        )
        self.wait()
        self.play(FadeOut(arrow5))
        self.wait()

        self.play(Circumscribe(new_property_1[4], fade_out=True))
        self.play(new_property_1[4].animate.set_color(YELLOW))
        self.play(ReplaceItemsInFormula(new_property_1, [4], ['^5']))
        self.wait()
        # self.replace_items_in_formula(task1, [3], ["$x^5$"])
        self.play(ReplaceItemsInFormula(task1, [3], ["$x$"], colors=[ORANGE]))
        self.play(AddItemsInFormula(task1, [3], ["$^5$"], colors=[YELLOW]))
        self.wait()

        self.play(FadeOut(new_property_1))
        self.wait()

        # 2-րդ վարժ.
        task2_number = Tex("$2.$", font_size=FONT_SIZE).next_to(task1_number, DOWN, buff=1, aligned_edge=LEFT)
        task2 = Tex("$($", "$a$", "$^2$", "$)$", "$^4$", " $\\cdot$ ", "$($", "$a$", "$^3$", "$)$", "$^2$", " $=$ ", "$a$", "$^9$", " $\\cdot$ ", "$*$", font_size=FONT_SIZE).next_to(task2_number, buff=.2, aligned_edge=DOWN).shift(DOWN*.09)
        self.play(Write(VGroup(task2_number, task2)))
        self.fix_formula(task2)
        self.wait()

        self.play(Circumscribe(task2[:5], fade_out=True))
        self.wait()
        new_property_3 = property_3.copy()
        self.play(new_property_3.animate.next_to(task2, DOWN, buff=1, aligned_edge=LEFT))
        self.wait()

        arrow1 = Arrow(start=task2[1], end=new_property_3[1].get_center())
        arrow2 = Arrow(start=task2[2], end=new_property_3[2].get_center())
        arrow3 = Arrow(start=task2[2], end=new_property_3[7].get_center())

        self.play(GrowArrow(arrow1))
        self.wait()

        self.play(FadeOut(arrow1))
        self.wait()
        self.play(
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            task2[2].animate.set_color(GREEN),
            new_property_3[2].animate.set_color(GREEN),
            new_property_3[7].animate.set_color(GREEN)
        )
        self.wait()
        self.replace_items_in_formula(new_property_3, [2, 7], ["$^2$", "$^2$"])
        self.play(FadeOut(arrow2, arrow3))
        self.wait()

        arrow4 = Arrow(start=task2[4], end=new_property_3[4].get_center())
        arrow5 = Arrow(start=task2[4], end=new_property_3[9].get_center())
        self.play(
            GrowArrow(arrow4),
            GrowArrow(arrow5),
            task2[4].animate.set_color(YELLOW),
            new_property_3[4].animate.set_color(YELLOW),
            new_property_3[9].animate.set_color(YELLOW)
        )
        self.wait()
        self.replace_items_in_formula(new_property_3, [4, 9], ["$^4$", "$^4$"])
        self.play(FadeOut(arrow4, arrow5))
        self.wait()

        self.play(
            ReplaceItemsInFormula(task2, [2, 4], [" ", "$^8$"])
        )
        self.remove_items_from_formula(task2, [2])
        self.wait()
        self.play(
            FadeOut(new_property_3),
            task2[3].animate.set_color(WHITE)
        )
        self.wait()
        # self.remove_items_from_formula(task2, [7])
        # self.replace_items_in_formula(task2, [8], ["$^6$"])
        self.play(
            ReplaceItemsInFormula(task2, [7, 9], [" ", "$^6$"])
        )
        self.remove_items_from_formula(task2, [7])
        self.wait()
        self.play(Indicate(prop_1))
        self.wait()
        self.multiply_numbers_in_formula(task2, 9, "$a^{14}$")
        self.wait()
        self.rearrange_formula(task2, [2, 3, 4, 5, 1, 0], move_up=[2,3,4,5], move_down=[0])
        self.wait()

        self.play(Circumscribe(task1))
        self.wait()
        self.play(Indicate(prop_1))
        self.wait()
        self.replace_items_in_formula(task2, [5], ["$a^{9+5}$"])
        self.wait()
        self.replace_items_in_formula(task2, [3], ["$a^5$"])

        self.wait(2)
