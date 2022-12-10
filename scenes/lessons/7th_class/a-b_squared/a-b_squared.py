from manim import *
from manim import Scene
from manim import WHITE, GREEN, ORANGE, YELLOW
from manim import UP, LEFT, DOWN, RIGHT, UL, UR, DR, DL
from manim import AnimationGroup, Write, Create, FadeOut, Circumscribe, Indicate
from manim import Transform, ReplacementTransform, ClockwiseTransform
from manim import there_and_back, there_and_back_with_pause
from manim import Tex, VGroup, Circle

from hanrahashiv import ModifyFormula
from segment import ConnectionLine

class AMinusBSquared(Scene):
    def construct(self):
        self.recap_and_get_stuck()

    def recap_and_get_stuck(self): # 51^2=(50+1)^2..., 49^2=(40+9)^2..., 49^2=(50-1)^2=???
        # 51^2 = (50+1)^2 = 50^2 + 2•50•1 + 1^2
        fifty_one_squared = Tex(
            '$51^2$', ' $=$ ', '$(50+1)^2$', ' $=$ ', '$50^2 + 2 \cdot 50 \cdot 1 + 1^2$', ' $=$ ', '$2601$',
            font_size=60
        )
        fifty_one_squared.shift(UP).to_edge(LEFT)
        self.play(Create(fifty_one_squared[0]))
        self.wait(0.25)
        self.play(Create(fifty_one_squared[1:3]))
        self.wait(0.25)
        self.play(Create(fifty_one_squared[3:]))
        self.wait()

        # 49^2 = (40+9)^2 = 40^2 + 2•40•9 + 9^2
        forty_nine_squared_1 = Tex(
            '$49^2$', ' $=$ ', '$(40+9)^2$', ' $=$ ', '$40^2$', '$+ 2 \cdot 40 \cdot 9$', '$+ 9^2$', ' $=$ ', '$2401$',
            font_size=60
        )
        forty_nine_squared_1.next_to(fifty_one_squared, DOWN, buff=0.75, aligned_edge=LEFT)
        calculations = VGroup(*Tex('$1600 + 720 + 81$', font_size=60)[0])
        calculations.next_to(forty_nine_squared_1[4:7], DOWN, buff=0.5)

        self.play(Write(forty_nine_squared_1[0]))
        self.wait(0.25)
        self.play(Write(forty_nine_squared_1[1:3]))
        self.wait(0.25)
        for i in [3, 4, 5, 6]:
            self.play(Write(forty_nine_squared_1[i]))
            self.wait(0.25)
        self.play(Write(calculations[0:4]))
        self.wait(0.5)
        self.play(Write(calculations[4:8]))
        self.wait(0.5)
        self.play(Write(calculations[8:]))
        self.wait(0.5)

        self.play(Transform(calculations, Tex('$2401$', font_size=60).move_to(calculations)))
        self.wait()
        self.play(
            Write(forty_nine_squared_1[-2]),
            ReplacementTransform(calculations, forty_nine_squared_1[-1:])
        )
        self.wait()

        # another approach - 49^2=(50-1)^2
        forty_nine_squared_2 = Tex('$49^2$', ' $=$ ', '$(50-1)^2$', font_size=60)
        forty_nine_squared_2.next_to(forty_nine_squared_1, DOWN, buff=0.75, aligned_edge=LEFT)
        self.play(Write(forty_nine_squared_2[0]))
        self.wait(0.5)
        self.play(Write(forty_nine_squared_2[1:]))
        self.wait()

        self.play(Circumscribe(forty_nine_squared_2[2][1:5], shape=Circle, fade_out=True, run_time=2))
        self.wait()

        self.play(
            FadeOut(fifty_one_squared, forty_nine_squared_1),
            forty_nine_squared_2.animate.to_corner(UL)
        )
        self.wait()

        self.forty_nine_squared = forty_nine_squared_2

    def get_formula(self):
        a_minus_b_squared = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$^2$', ' $=$ ', # 0:7
            '$($', '$a$', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$a$', '$-$', '$b$', '$)$', '$=$', # 7:19
            '$a$', '$\cdot$', '$a$', '$+$', '$a$', '$\cdot$', '$($', '$-$', '$b$', '$)$', '$+$', # 19:30
            '$($', '$-$', '$b$', '$)$', '$\cdot$', '$a$', '$+$', '$($', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$-$', '$b$', '$)$', #30:46
            font_size=60
        ) # (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)
        a_minus_b_squared.to_edge(LEFT)
