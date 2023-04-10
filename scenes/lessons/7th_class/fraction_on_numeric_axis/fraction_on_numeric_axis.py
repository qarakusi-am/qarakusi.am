from manim import Write, Tex, VGroup, FadeIn, Create, AnimationGroup, FadeOut, \
    ReplacementTransform, MathTex, Brace, Line, PI
from manim import DOWN, UP, LEFT, RIGHT, MovingCameraScene
from manim import ORANGE, WHITE, BLACK, YELLOW_E, GrowFromPoint, Circle, TAU

from objects import SimpleSVGMobject
from .text import *

FONT_SIZE = 90
RUN_TIME = 2


class FractionOnNumericAxis(MovingCameraScene):
    def construct(self):
        self.wait()

        # FadeIn pizzas
        circle = Circle(1.5, fill_opacity=1, color=YELLOW_E, stroke_width=5, stroke_color=BLACK)
        pizza_svg1 = SimpleSVGMobject("pizza_full_1")
        pizza_svg1.match_height(circle).match_width(circle)
        pizza_svg1.shift(LEFT * 2)
        pizza_svg2 = pizza_svg1.copy().shift(RIGHT * 5)
        self.play(FadeIn(pizza_svg1, pizza_svg2))
        self.wait()

        # create X axis
        x_axis = Line((-7, -2, 0), (15, -2, 0))
        self.play(Create(x_axis))
        self.wait(2)

        x_labels = VGroup()
        for i in range(6):
            x_labels.add(VGroup(Line((-7 + 2.5 * i, -2.2, 0), (-7 + 2.5 * i, -1.8, 0)),
                                MathTex(i).move_to((-7 + 2.5 * i, -2.2, 0), DOWN).shift(DOWN * 0.5)))

        self.play(Write(x_labels))
        self.wait(2)

        # move pizzas to respective position
        self.play(AnimationGroup(pizza_svg1.animate.scale(0.7).next_to(x_labels[0], UP).shift(RIGHT * 1.3),
                                 pizza_svg2.animate.scale(0.7).next_to(x_labels[1], UP).shift(RIGHT * 1.4)))

        self.wait()

        self.play(x_labels[1][1].animate.scale(1.5).set_color(ORANGE))
        self.wait()

        self.play(x_labels[1][1].animate.scale(1 / 1.5).set_color(WHITE))
        self.wait()

        self.play(FadeOut(pizza_svg2))
        self.wait()

        # cut pizza
        circle.scale(0.7).move_to(pizza_svg1)
        lines = [
            Line(stroke_width=5, color=BLACK).match_width(circle).move_to(circle.get_center()).rotate(i * TAU / 6)
            for i in range(3)
        ]
        cutting_animation = AnimationGroup(
            *[
                GrowFromPoint(lines[i], lines[i].get_start())
                for i in range(len(lines))
            ],
            lag_ratio=.6
        )
        self.play(cutting_animation)
        self.wait(2)

        # zoom to 0-1 range

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(pizza_svg1).scale(0.6).shift(DOWN * 0.5))
        self.wait()

        # convert pizza to slices and put in respective positions
        pizza_slices = VGroup(
            SimpleSVGMobject("pizza_peace_6").rotate(PI / 6).scale(0.25).move_to(x_labels[0][0], UP).shift(
                RIGHT * 0.15 + UP * 0.5))

        for i in range(1, 6):
            pizza_slices.add(pizza_slices[0].copy().shift(RIGHT * 0.42 * i))

        self.play(FadeOut(pizza_svg1), Write(pizza_slices))
        self.remove(*lines)
        self.wait()

        x_labels_in_0_1_range = VGroup()
        for i in range(1, 6):
            x_labels_in_0_1_range.add(VGroup(x_labels[0][0].copy().stretch(0.6, 1).shift(RIGHT * 0.4 * i),
                                             MathTex(r'\frac{' + str(i) + '}{6}').scale(0.5).move_to(
                                                 x_labels[0][0]).shift(RIGHT * 0.42 * i + DOWN * 0.5)))
        self.play(AnimationGroup(*[Write(item[0]) for item in x_labels_in_0_1_range]))
        self.wait()

        self.play(VGroup(pizza_slices[1:]).animate.set_opacity(0))
        self.wait()

        helper_numbers = VGroup(
            VGroup(MathTex(r'\frac{1}{6}', font_size=30).move_to(pizza_slices[0], UP * 1.3).shift(UP + RIGHT * 0.2),
                   Tex(part, font_size=30).move_to(pizza_slices[0], UP).shift(RIGHT * 0.8 + UP * 0.8)),
            MathTex(r'\frac{2}{6}', font_size=30).move_to(pizza_slices[0], UP * 1.3).shift(UP + RIGHT * 0.2),
            MathTex(r'\frac{5}{6}', font_size=30).move_to(pizza_slices[0], UP * 1.3).shift(UP + RIGHT * 0.2)
        )

        helper_lines = VGroup(
            Line(x_labels[0][0].get_left(), x_labels_in_0_1_range[0][0].get_left(), color=ORANGE, stroke_width=5),
            Line(x_labels_in_0_1_range[0][0].get_left(), x_labels_in_0_1_range[1][0].get_left(), color=ORANGE,
                 stroke_width=5),
            Line(x_labels_in_0_1_range[1][0].get_left(), x_labels_in_0_1_range[4][0].get_left(), color=ORANGE,
                 stroke_width=5))
        braces = VGroup(Brace(VGroup(pizza_slices[0:2]), sharpness=4, direction=([0., 1., 0.])).shift(DOWN * 0.2),
                        Brace(VGroup(pizza_slices[0:5]), sharpness=4, direction=([0., 1., 0.])).shift(DOWN * 0.2))

        # 1/6 of the pizza
        self.play(Write(helper_numbers[0]))
        self.wait()

        self.play(AnimationGroup(Write(VGroup(helper_lines[0], x_labels_in_0_1_range[0][1]))))
        self.wait()

        # 2/6 of the pizza
        self.play(AnimationGroup(pizza_slices[1].animate.set_opacity(1), Write(braces[0]),
                                 ReplacementTransform(helper_numbers[0], helper_numbers[1])))
        self.wait()

        self.play(x_labels_in_0_1_range[1][1].animate.set_opacity(1), Write(helper_lines[1]))
        self.wait()

        # 5/6 of the pizza
        self.play(AnimationGroup(*[Write(x_labels_in_0_1_range[i][1]) for i in range(2, 5)],
                                 VGroup(pizza_slices[2:5]).animate.set_opacity(1),
                                 ReplacementTransform(braces[0], braces[1]),
                                 ReplacementTransform(helper_numbers[1], helper_numbers[2]),
                                 Write(helper_lines[-1])))
        self.wait(2)

        self.play(FadeOut(helper_lines, helper_numbers[2], braces[1]))
        self.wait()

        self.play(self.camera.frame.animate.scale(1.2).shift(UP * 0.5 + RIGHT * 2))
        self.wait()

        # draw remaining pizza slices on x-axis
        pizza_slices[-1].set_opacity(1)
        pizza_slices.add(VGroup(pizza_slices[0:5]).copy().move_to(x_labels[1][0], UP).shift(RIGHT + UP * 0.5))
        x_label_for_last_fraction = VGroup(x_labels[1][0].copy().stretch(0.6, 1).shift(RIGHT * 2),
                                           MathTex(r'\frac{11}{6}').scale(0.5).move_to(x_labels[1][0]).shift(
                                               RIGHT * 2 + DOWN * 0.5))

        self.play(Write(VGroup(pizza_slices[5:])))
        self.wait()

        self.play(Write(x_label_for_last_fraction))
        self.wait()
