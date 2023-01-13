from manim import *

from objects import SimpleSVGMobject, Weight, Scales
from scales import RotateTheScales
from .text import together_are_510, single_apple_is_170

class Example(Scene):
    def construct(self):
        
        # draw the scales
        sc = Scales().shift(2 * DOWN)
        self.play(FadeIn(sc))
        self.wait()

        # add 3 apples and 20g to the left plate
        left_mobs = VGroup(
            SimpleSVGMobject('fruits/red_apple').scale(0.35),
            SimpleSVGMobject('fruits/red_apple').scale(0.35),
            SimpleSVGMobject('fruits/red_apple').scale(0.35),
            Weight(20, 20)
        )
        left_mobs.arrange(buff=0.15, aligned_edge=DOWN).next_to(sc.left_plate, UP, 0)

        # add 530g to the right plate
        right_mobs = Weight(530, 40).next_to(sc.right_plate, UP, 0)

        self.play(FadeIn(left_mobs, right_mobs))
        self.wait()

        # divide 530g into 2 parts - 510g and 20g
        self.play(
            Transform(
                right_mobs,
                VGroup(Weight(510, 40), Weight(20, 20)).arrange(aligned_edge=DOWN).next_to(sc.right_plate, UP, 0)
            )
        )
        self.wait()

        # remove 20g from both sides
        self.play(
            left_mobs[3].animate.shift(UP),
            right_mobs[1].animate.shift(UP)
        )
        self.wait()

        self.play(FadeOut(left_mobs[3], right_mobs[1]))
        left_mobs.remove(left_mobs[-1])
        right_mobs.remove(right_mobs[-1])
        self.wait()
        self.play(
            left_mobs.animate.next_to(sc.left_plate, UP, 0),
            right_mobs.animate.next_to(sc.right_plate, UP, 0)
        )
        self.wait()

        # write 
        # 3 apples are 510 grams.
        # One apple is 510։3=170 grams.
        three_apples_are_510 = Tex(together_are_510).shift(3 * UP)
        one_apple_is_170 = Tex(*single_apple_is_170).next_to(three_apples_are_510, DOWN, 0.75)

        self.play(Write(three_apples_are_510))
        self.wait()
        self.play(Write(one_apple_is_170))
        self.wait()
