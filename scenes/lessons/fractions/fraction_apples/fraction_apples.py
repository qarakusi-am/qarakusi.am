from manim import MovingCameraScene, FadeIn, VGroup, ReplacementTransform, AnimationGroup, MathTex, Write, Tex
from manim import UP, DOWN, RIGHT
from manim import BLUE
from objects import SimpleSVGMobject
from numpy import array
from .text import *

FONT_SIZE = 24

class FractionApples(MovingCameraScene):
    def construct(self):
        self.wait()

        # apples
        apple_svg = SimpleSVGMobject("green_apple", scale=1)
        
        apples_3x = VGroup(*[apple_svg.copy() for _ in range(3)])
        apples_3x.arrange(buff=3).to_edge(UP)
        apples_3x.save_state()
        self.play(FadeIn(apples_3x))
        self.wait()

        # plates
        plate_svg = SimpleSVGMobject("plate_2", scale=.4)

        plates_4x = VGroup(*[plate_svg.copy() for _ in range(4)])
        plates_4x.arrange(buff=.5).to_edge(DOWN, buff=1)
        self.play(FadeIn(plates_4x))
        self.wait()

        #  start _________________________ move quarter apples into plates __________________________

        # transform 1st apple to 4 quarter apples
        quarter_apple_svg = SimpleSVGMobject("part_of_apple", scale=.4)
        
        quarter_apples_4x_1 = VGroup(*[quarter_apple_svg.copy() for _ in range(4)])
        quarter_apples_4x_1.arrange_in_grid().move_to(apples_3x[0].get_center())
        self.play(ReplacementTransform(apples_3x[0], quarter_apples_4x_1))
        self.wait()

        # move 1st apple's parts into plane
        self.play(
            AnimationGroup(
                *[
                    quarter_apple.animate.scale(.7).move_to(plates_4x[index].get_center())
                    for index, quarter_apple in enumerate(reversed(quarter_apples_4x_1))
                ],
                lag_ratio=.4
            )
        )
        self.wait()
        
        # transform 2nd apple to 4 quarter apples
        quarter_apples_4x_2 = VGroup(*[quarter_apple_svg.copy() for _ in range(4)])
        quarter_apples_4x_2.arrange_in_grid().move_to(apples_3x[1].get_center())
        self.play(ReplacementTransform(apples_3x[1], quarter_apples_4x_2))
        self.wait()

        # move 2nd apple's parts into plane
        self.play(
            AnimationGroup(
                *[
                    quarter_apple.animate.scale(.7).move_to(plates_4x[index].get_center()+array([-.8, .1, 0]))
                    for index, quarter_apple in enumerate(reversed(quarter_apples_4x_2))
                ],
                lag_ratio=.4
            )
        )
        self.wait()
        
        # transform 3rd apple to 4 quarter apples
        quarter_apples_4x_3 = VGroup(*[quarter_apple_svg.copy() for _ in range(4)])
        quarter_apples_4x_3.arrange_in_grid().move_to(apples_3x[2].get_center())
        self.play(ReplacementTransform(apples_3x[2], quarter_apples_4x_3))
        self.wait()

        # move 3rd apple's parts into plane
        self.play(
            AnimationGroup(
                *[
                    quarter_apple.animate.scale(.7).move_to(plates_4x[index].get_center()+array([.8, .1, 0]))
                    for index, quarter_apple in enumerate(reversed(quarter_apples_4x_3))
                ],
                lag_ratio=.4
            )
        )
        self.wait()

        #  end ___________________________ move quarter apples into plates __________________________
        
        # zoom in camera on first plane
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(plates_4x[0].get_center()+array([0, .4, 0])).set(width=plates_4x[0].width+.1))
        self.wait()

        # write 1/4 on quarter apples of the first plate
        quarter_texs = VGroup(
            MathTex("\\bf{\\frac{1}{4}}", font_size=FONT_SIZE, color=BLUE).move_to(quarter_apples_4x_2[-1].get_center()),
            MathTex("\\bf{\\frac{1}{4}}", font_size=FONT_SIZE, color=BLUE).move_to(quarter_apples_4x_1[-1].get_center()),
            MathTex("\\bf{\\frac{1}{4}}", font_size=FONT_SIZE, color=BLUE).move_to(quarter_apples_4x_3[-1].get_center())
        ).shift(RIGHT*.1) #.shift(array([.14, -.012, 0]))
        self.play(Write(quarter_texs))
        self.wait()

        # transform 3x "1/4"s to "3/4"
        three_quarters = MathTex("\\frac{3}{4}", font_size=1.15*FONT_SIZE, color=BLUE)
        three_quarters.next_to(plates_4x[0], UP)
        self.play(ReplacementTransform(quarter_texs, three_quarters))
        self.wait()

        # zoom out camera
        apples_3x.restore()
        apples_3x.set_opacity(.02).scale(.7).to_edge(UP)
        self.add(apples_3x)

        for index in range(3):
            self.add(three_quarters.copy().scale(2.5).next_to(plates_4x[index+1], UP))

        self.play(
            self.camera.frame.animate.restore(),
            three_quarters.animate.scale(2.5).next_to(plates_4x[0], UP)
        )
        self.wait()

        # write text
        text = Tex(text_str, font_size=TEXT_FONT_SIZE)
        text.next_to(apples_3x, DOWN, buff=.3)
        self.play(Write(text))

        self.wait(2)
