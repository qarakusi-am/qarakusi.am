from manim import Write, FadeOut, AnimationGroup, Tex, VGroup
from manim import Arrow, CurvedArrow, SurroundingRectangle
from manim import YELLOW, ORANGE, WHITE, MathTex
from manim import Scene, LEFT, UP, DOWN
from qarakusiscene import TaskNumberBox
from .text import *

FONT_SIZE = 64
RUN_TIME_SPEED = 2

class Problem12722(Scene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)
        main_text=Tex(for_what_value_k,' $x=3 $ ',is_a_solution,font_size=FONT_SIZE).shift(UP*3)

        self.play(Write(main_text, run_time=RUN_TIME_SPEED))
        self.wait()

        equations = VGroup(
            MathTex('kx+7=2k+x^2', font_size=FONT_SIZE).shift(UP),
            MathTex(' k\cdot 3+7=2k+3^2',font_size=FONT_SIZE).shift(LEFT*0.25),
            MathTex('3k+7=2k+9', font_size=FONT_SIZE).shift(LEFT*0.15),
            MathTex('3k-2k=9-7', font_size=FONT_SIZE).shift(DOWN+LEFT*0.5),
            MathTex('k=2', font_size=FONT_SIZE).shift(DOWN*2+LEFT*0.1),
        )

        equations[1][0][2].set_color(ORANGE)
        equations[1][0][9].set_color(ORANGE)

        self.play(Write(equations[0],run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(VGroup(main_text[0],main_text[2]).animate.set_opacity(0))
        self.wait()

        arrows_to_x=VGroup(
            Arrow(main_text[1][0].get_bottom(),equations[0][0][1].get_top(),max_stroke_width_to_length_ratio=0.85,max_tip_length_to_length_ratio=0.08).scale(1.15,1),
            Arrow(main_text[1][0].get_bottom(), equations[0][0][8].get_top(),max_stroke_width_to_length_ratio=0.5,max_tip_length_to_length_ratio=0.03).scale(1.05,1)
        )

        self.play(Write(arrows_to_x,run_time=RUN_TIME_SPEED))
        self.wait()
        self.play(AnimationGroup(equations[0][0][1].animate.set_color(ORANGE),equations[0][0][8].animate.set_color(ORANGE)))

        self.play(Write(equations[1], run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(FadeOut(arrows_to_x))
        self.wait()

        self.play(AnimationGroup(main_text[1].animate.shift(LEFT),VGroup(equations[0:2]).animate.shift(UP)))
        self.wait()

        self.play(Write(equations[2], run_time=RUN_TIME_SPEED))
        self.wait()

        curved_arrows=VGroup(
            CurvedArrow(equations[2][0][3].get_bottom(),equations[2][0][7].get_bottom(),tip_length=0.15,
                                    angle=.6).shift(DOWN*0.1),
            CurvedArrow(equations[2][0][5].get_top(), equations[2][0][2].get_top(),tip_length=0.15,
                                    angle=.6).shift(UP*0.1)
        )

        self.play(Write(curved_arrows[0]))
        self.play(Write(curved_arrows[1]))
        self.wait()

        self.play(Write(equations[3], run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(FadeOut(curved_arrows))
        self.wait()

        self.play(Write(equations[4], run_time=RUN_TIME_SPEED))
        self.wait()

        surrounding_box=SurroundingRectangle(equations[4],color=WHITE, buff=0.3)

        self.play(Write(surrounding_box))
        self.wait()

        self.play(equations[4][0].animate.set_color(YELLOW).scale(1.26))
        self.wait()
