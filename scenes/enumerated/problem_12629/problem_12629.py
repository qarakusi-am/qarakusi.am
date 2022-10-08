from manim import Scene, FadeIn, MathTex, Write, Tex, SurroundingRectangle, VGroup, Arrow, GrowArrow, FadeOut, Circumscribe
from manim import WHITE, UL, UR, DOWN, LEFT
import numpy as np
from hanrahashiv import ReplaceItemsInFormula
from qarakusiscene import TaskNumberBox
from .text import *

FONt_SIZE = 53

class Problem12629(Scene):
    def construct(self):
        self.wait()
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        task1 = MathTex("x", "^3", "\\cdot", "*", "=", "x", "^8", font_size=FONt_SIZE).to_edge(UL, buff=.7).shift(DOWN)
        self.play(Write(task1))
        self.wait()

        property_1 = Tex('$a$', '$^m$', '$\cdot$', '$a$', '$^n$', '$=$', '$a$', '$^m$', '$^+$', '$^n$', font_size=65)
        property_1_rect = SurroundingRectangle(property_1, color=WHITE).stretch(1.25, 1).stretch(1.15, 0)
        property_1_index = Tex('1.', font_size=35).next_to(property_1_rect, UL, buff=-0.3)
        prop_1 = VGroup(property_1, property_1_rect, property_1_index).to_corner(UR, buff=0.15)
        prop_1.shift(DOWN)

        property_2 = Tex('$($', '$a$', '$\cdot$', '$b$', '$)$', '$^n$', '$=$', '$a$', '$^n$', '$\cdot$', '$b$', '$^n$', font_size=65)
        property_2_rect = SurroundingRectangle(property_2, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_2_index = Tex('2.', font_size=35).next_to(property_2_rect, UL, buff=-0.3)
        prop_2 = VGroup(property_2, property_2_rect, property_2_index).next_to(prop_1, DOWN, 1.5, LEFT)

        property_3 = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', '$=$', '$a$', '$^m$', '$^\cdot$', '$^n$', font_size=65)
        property_3_rect = SurroundingRectangle(property_3, color=WHITE).match_height(property_1_rect).stretch(1.12, 0)
        property_3_index = Tex('3.', font_size=35).next_to(property_3_rect, UL, buff=-0.3)
        prop_3 = VGroup(property_3, property_3_rect, property_3_index).next_to(prop_2, DOWN, 1.5, LEFT)

        self.play(FadeIn(prop_1, prop_2, prop_3))
        self.wait()

        new_property_1 = property_1.copy()
        self.play(new_property_1.animate.scale(FONt_SIZE/65).next_to(task1, DOWN, .8, LEFT))

        arrow1 = Arrow(start=task1[0], end=new_property_1[0])
        self.play(GrowArrow(arrow1))
        self.wait()
        self.play(ReplaceItemsInFormula(new_property_1, [0], [task1[0].get_tex_string()]))
        self.play(FadeOut(arrow1))

        arrow2 = Arrow(start=task1[1], end=new_property_1[1])
        arrow3 = Arrow(start=task1[1], end=new_property_1[8].get_center()+np.array([-0.3, .1, 0]), stroke_width=3, max_tip_length_to_length_ratio=0.1)
        self.play(
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait()
        self.play(ReplaceItemsInFormula(new_property_1, [1], [task1[1].get_tex_string()]))
        self.play(ReplaceItemsInFormula(new_property_1, [7], [task1[1].get_tex_string()]))
        self.play(FadeOut(arrow2, arrow3))
        self.wait()

        arrow4 = Arrow(start=task1[-2], end=new_property_1[-4])
        self.play(GrowArrow(arrow4))
        self.wait()
        self.play(ReplaceItemsInFormula(new_property_1, [-4], [task1[-2].get_tex_string()]))
        self.play(FadeOut(arrow4))
        self.wait()

        arrow5 = Arrow(start=task1[-1].get_center()+np.array([0, .1, 0]), end=new_property_1[-2], buff=0.3)
        self.play(
            GrowArrow(arrow5),
            Circumscribe(new_property_1[-3:], fade_out=True, run_time=2.5)
        )
        self.wait()
        self.play(ReplaceItemsInFormula(new_property_1, [-1], ["$^5$"]))
        self.play(FadeOut(arrow5))
        self.wait()

        self.play(ReplaceItemsInFormula(new_property_1, [3, 4], ["$x$" ,"$^5$"]))
        
        self.wait(2)
