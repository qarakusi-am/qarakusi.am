from manim import Write, Tex, VGroup, FadeIn, Create, AnimationGroup, Arrow, SurroundingRectangle, FadeOut, CurvedArrow, \
    ReplacementTransform, Brace, MathTex,  Scene, Line
from manim import  DOWN, UP, LEFT, RIGHT
from manim import  ORANGE
from objects import SimpleSVGMobject, SVGMobject
from .text import *

FONT_SIZE=90
RUN_TIME=2

class FractionToMixedNumber(Scene):
    def construct(self):

        apple_slices = VGroup()
        for i in range(13):
            apple_slices.add(
                SimpleSVGMobject("fruits/part_of_apple" ).scale(
                    0.4))
        #move slices to different positions
        apple_slices[0].shift(LEFT * 6 + UP * 3)
        apple_slices[1].shift(LEFT + UP * 2.5)
        apple_slices[2].shift(LEFT * 3)
        apple_slices[3].shift(LEFT+UP*0.5)
        apple_slices[4].shift(LEFT * 3 + UP* 2)
        apple_slices[5].shift(RIGHT * 3 + UP * 3)
        apple_slices[6].shift(RIGHT + UP * 3)
        apple_slices[7].shift(LEFT*4.5 + UP )
        apple_slices[8].shift(RIGHT * 2 + UP*1.5 )
        apple_slices[9].shift ( UP*1.4)
        apple_slices[10].shift(LEFT * 6.5+UP*2)
        apple_slices[11].shift(LEFT * 4 + UP * 3)
        apple_slices[12].shift(RIGHT )

        apple_slices.shift(RIGHT+DOWN)

        self.play(FadeIn(apple_slices))
        self.wait()

        helper_numbers=VGroup(MathTex(r'\frac{13}{4}',font_size=FONT_SIZE).next_to(apple_slices,RIGHT).shift(RIGHT*0.5+DOWN*0.4),
                              VGroup(MathTex('13:4 = 3(1 \;\;\;\;)',font_size=FONT_SIZE).next_to(apple_slices,UP).shift(RIGHT)),
                              MathTex('3',font_size=FONT_SIZE).shift(UP*0.1+LEFT*1.3),
                              MathTex(r'\frac{1}{4}',font_size=FONT_SIZE).next_to(apple_slices,RIGHT).shift(LEFT+DOWN*0.4))

        #add remainder text like tex, so fonts of digits remain the same
        helper_numbers[1].add(Tex(remainder,font_size=FONT_SIZE).next_to(helper_numbers[1][0][0][-1],LEFT).shift(UP*0.1+RIGHT*0.1))

        self.play(FadeIn(helper_numbers[0]))
        self.wait(2)

        #create x axis
        x_axis=Line((-6,-3,0),(10,-3,0))
        self.play(Create(x_axis))
        self.wait()

        x_labels=VGroup()
        for i in range(5):
            x_labels.add(VGroup(Line((-6+3*i,-3.2,0),(-6+3*i,-2.8,0)),MathTex(i).move_to((-6+3*i,-3.2,0),DOWN).shift(DOWN*0.5)))

        self.play(Write(x_labels))
        self.wait(2)

        #move apple slices to respective range
        self.play( AnimationGroup(
            *[apple_slices[i].animate.scale(0.6).next_to(x_labels[int(i/4)],RIGHT).shift(UP*0.8+RIGHT*int(i%4)*0.65) for i in range(len(apple_slices))]))
        self.wait(2)

        braces=VGroup()
        for i in range(3):
            braces.add(Brace(VGroup(apple_slices[4*i], apple_slices[4*i+3]), sharpness=1, direction=([0., 1., 0.])))

        self.play(Write(braces,run_time=RUN_TIME))
        self.wait(2)

        self.play(FadeIn(helper_numbers[1]))
        self.wait(2)

        arrows = VGroup()
        apples = VGroup()

        for item in braces:
            arrows.add(Arrow(helper_numbers[1][0][0][5].get_bottom(), item.get_center()))
            apples.add(SimpleSVGMobject("fruits/yellow_apple",).move_to(item).shift(UP*2.1))

        self.play(Create(arrows,run_time=RUN_TIME))
        self.wait(2)

        arrows.add((Arrow(helper_numbers[1][0][0][7].get_bottom(),apple_slices[-1])))

        self.play(Create(arrows[-1]))
        self.wait(2)

        self.play(FadeOut(arrows))
        self.wait()

        #transform apple slices to apples
        self.play(ReplacementTransform(VGroup(apple_slices[0:4],braces[0]),apples[0]))
        self.wait(2)

        self.play(AnimationGroup(ReplacementTransform(VGroup(apple_slices[4:8], braces[1]), apples[1]),
                                 ReplacementTransform(VGroup(apple_slices[8:12], braces[-1]), apples[-1])))
        self.wait()

        self.play(apple_slices[-1].animate.shift(UP*2.8+RIGHT*0.3))
        self.wait(2)

        #convert apples to numbers
        signs=VGroup()
        for item in apples:
            signs.add(MathTex('+',font_size=FONT_SIZE).move_to(item).shift(RIGHT*1.5+DOWN*0.18))
        signs.add(MathTex('=',font_size=FONT_SIZE).move_to(apple_slices[-1]).shift(RIGHT*0.8+DOWN*0.3))

        self.play(Write(signs,run_time=RUN_TIME))
        self.wait()

        self.play(FadeOut(x_labels,x_axis))
        self.wait()

        self.play(ReplacementTransform(VGroup(apples,signs[0:2]),helper_numbers[-2]))
        self.wait(2)

        self.play(ReplacementTransform(apple_slices[-1], helper_numbers[-1]))
        self.wait(2)

        #obtain final number
        self.play(AnimationGroup(
            VGroup(helper_numbers[-1],signs[-1],helper_numbers[0]).animate.move_to(helper_numbers[-2]).shift(RIGHT*1.5),
            signs[-2].animate.set_opacity(0)
        ))
        self.wait()

        surrounding_box=SurroundingRectangle(VGroup(helper_numbers[2:],signs[-1],helper_numbers[0]),color=ORANGE,buff=0.3)
        self.play(Create(surrounding_box,run_time=RUN_TIME))
        self.wait()

        curved_arrows=VGroup(CurvedArrow(helper_numbers[1][0][0][5].get_bottom(),helper_numbers[-2].get_top(),angle=1,tip_length=0.25),
                      CurvedArrow(helper_numbers[1][0][0][7].get_bottom(), helper_numbers[-1][0][0].get_center(),angle=-1,tip_length=0.25))
        self.play(Create(curved_arrows,run_time=RUN_TIME))
        self.wait()
