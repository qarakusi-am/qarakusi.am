from manim import *

from objects import SimpleSVGMobject, Weight, Scales
from scales import RotateTheScales
from .text import together_are_510, single_apple_is_170

class Example(Scene):
    def construct(self):

        # draw the scales
        sc = Scales(plate_stretch_factor=1.25).shift(2 * DOWN)
        self.play(FadeIn(sc))
        self.wait()

        # add 3 apples and 20g to the left plate
        left_mobs = VGroup(
            SimpleSVGMobject('fruits/red_apple').scale(0.45),
            SimpleSVGMobject('fruits/red_apple').scale(0.45),
            SimpleSVGMobject('fruits/red_apple').scale(0.45),
            Weight(20, 10)
        )
        left_mobs.arrange(buff=0.15, aligned_edge=DOWN).next_to(sc.left_plate, UP, 0)

        # add 530g to the right plate
        right_mobs = Weight(530, 30).next_to(sc.right_plate, UP, 0)

        self.play(FadeIn(left_mobs, right_mobs))
        self.wait()

        scales_states = VGroup()
        scales_states.add(VGroup(sc, left_mobs, right_mobs).copy())

        # divide 530g into 2 parts - 510g and 20g
        self.play(
            Transform(
                right_mobs,
                VGroup(Weight(510, 30), Weight(20, 10)).arrange(aligned_edge=DOWN).next_to(sc.right_plate, UP, 0)
            )
        )
        self.wait()
        scales_states.add(VGroup(sc, left_mobs, right_mobs).copy())

        # remove 20g from both sides
        self.play(
            left_mobs[3].animate.shift(UP),
            right_mobs[1].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(left_mobs[3], right_mobs[1]),
            left_mobs[:-1].animate.next_to(sc.left_plate, UP, 0),
            right_mobs[:-1].animate.next_to(sc.right_plate, UP, 0)
        )
        left_mobs.remove(left_mobs[-1])
        right_mobs.remove(right_mobs[-1])
        self.wait()
        scales_states.add(VGroup(sc, left_mobs, right_mobs).copy())

        # divide 510 gram weight into 3 170 gram weights
        self.play(
            Transform(
                right_mobs,
                VGroup(Weight(170, 30), Weight(170, 30), Weight(170, 30)).arrange().next_to(sc.right_plate, UP, 0)
            )
        )
        self.wait()

        # remove 2 apples form the left side and 2 weights from the right side
        self.play(FadeOut(left_mobs[0], left_mobs[-1], right_mobs[0], right_mobs[-1]))
        self.wait()
        left_mobs.remove(left_mobs[0])
        left_mobs.remove(left_mobs[-1])
        right_mobs.remove(right_mobs[0])
        right_mobs.remove(right_mobs[-1])
        scales_states.add(VGroup(sc, left_mobs, right_mobs).copy())

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

        horizontal_states = scales_states.copy().arrange(RIGHT, buff=0.75, aligned_edge=DOWN).scale(0.25).to_edge(UP)
        vertical_states = scales_states.copy().arrange(DOWN, buff=1).scale(0.4).to_edge(LEFT)

        self.add(horizontal_states)
        self.play(
            *[ReplacementTransform(horizontal_states[i], vertical_states[i]) for i in range(4)],
            # *[ClockwiseTransform(horizontal_states[i], vertical_states[i]) for i in range(1, 4)]
        )
        self.wait()



        # # write 
        # # 3 apples are 510 grams.
        # # One apple is 510։3=170 grams.
        # three_apples_are_510 = Tex(together_are_510).shift(3 * UP)
        # one_apple_is_170 = Tex(*single_apple_is_170).next_to(three_apples_are_510, DOWN, 0.75)

        # self.play(Write(three_apples_are_510))
        # self.wait()
        # self.play(Write(one_apple_is_170))
        # self.wait()
        
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
        # self.wait()


        # ### write an equation that describes the example of 3apples+20grams = 530grams

        # # draw the scales, apples and wights
        # sc = Scales(plate_stretch_factor=1.25).shift(2 * DOWN)
        # left_mobs = VGroup(
        #     SimpleSVGMobject('fruits/red_apple').scale(0.45),
        #     SimpleSVGMobject('fruits/red_apple').scale(0.45),
        #     SimpleSVGMobject('fruits/red_apple').scale(0.45),
        #     Weight(20, 10)
        # )
        # left_mobs.arrange(buff=0.15, aligned_edge=DOWN).next_to(sc.left_plate, UP, 0)
        # right_mobs = Weight(530, 30).next_to(sc.right_plate, UP, 0)
        # VGroup(sc, left_mobs, right_mobs).scale(0.75).to_edge(DOWN)
        # self.play(FadeIn(sc, left_mobs, right_mobs))
        # self.wait()

        # # write 3x + 20 = 530
        # equation_1 = Tex('$3$', '$\cdot$', '$x$', '$+$', '$20$', ' $=$ ', '$530$', font_size=70)
        # equation_1.to_edge(UP)
        # self.play(Write(equation_1))
        # self.wait()

        # # write 3x + 20 = 510 + 20
        # self.play(Transform(
        #     right_mobs,
        #     VGroup(Weight(510, 30), Weight(20, 10)).scale(0.75).arrange(aligned_edge=DOWN).next_to(sc.right_plate, UP, 0)
        # ))
        # self.wait()

        # equation_2 = Tex('$3$', '$\cdot$', '$x$', '$+$', '$20$', ' $=$ ', '$510$', '$+$', '$20$', font_size=70)
        # equation_2.next_to(equation_1, DOWN, 0.5, LEFT)
        # self.play(Write(equation_2))
        # self.wait()

        # # write 3x = 510
        # self.play(
        #     FadeOut(left_mobs[-1], right_mobs[-1]),
        #     left_mobs[:-1].animate.next_to(sc.left_plate, UP, 0),
        #     right_mobs[0].animate.next_to(sc.right_plate, UP, 0)
        # )
        # right_mobs.remove(right_mobs[-1])
        # left_mobs.remove(left_mobs[-1])
        # self.wait()

        # equation_3 = Tex('$3$', '$\cdot$', '$x$', ' $=$ ', '$510$', font_size=70)
        # equation_3.next_to(equation_2, DOWN, 0.5, LEFT)
        # self.play(Write(equation_3))
        # self.wait()

        # # write x = 170
        # self.play(Transform(
        #     right_mobs,
        #     VGroup(Weight(170, 30), Weight(170, 30), Weight(170, 30)).scale(0.75).arrange().next_to(sc.right_plate, UP, 0)
        # ))
        # self.wait()
        # self.play(FadeOut(left_mobs[0], left_mobs[-1], right_mobs[0], right_mobs[-1]))
        # self.wait()

        # equation_4 = Tex('$x$', ' $=$ ', '$170$', font_size=70)
        # equation_4.next_to(equation_3, DOWN, 0.5, LEFT)
        # self.play(Write(equation_4))
        # self.wait()
