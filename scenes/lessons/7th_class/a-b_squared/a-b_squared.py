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
        self.forty_nine_squared = Tex(
            '$49$', '$^2$', ' $=$ ', '$($', '$50$', '$-$', '$1$', '$)$', '$^2$',
            font_size=60
        ) # 49^2 = (50-1)^2

        self.a_minus_b_squared = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$a$', '$^2$', '$-$', '$2$', '$a$', '$b$', '$+$', '$b$', '$^2$', # 6:16
            font_size=60
        ) # (a-b)^2 = a^2-2ab+b^2

        self.a_plus_b_squared = Tex(
            '$($', '$a$', '$+$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$a$', '$^2$', '$+$', '$2$', '$a$', '$b$', '$+$', '$b$', '$^2$', # 6:16
            font_size=60
        ) # (a+b)^2 = a^2+2ab+b^2

        # self.recap_and_get_stuck()
        self.get_formula()

    def recap_and_get_stuck(self): # 51^2=(50+1)^2..., 49^2=(40+9)^2..., 49^2=(50-1)^2=???
        # 51^2 = (50+1)^2 = 50^2 + 2•50•1 + 1^2
        fifty_one_squared = Tex(
            '$51^2$', ' $=$ ', '$(50+1)^2$', ' $=$ ', '$50^2 + 2 \cdot 50 \cdot 1 + 1^2$', ' $=$ ', '$2601$',
            font_size=60
        )
        fifty_one_squared.shift(UP).to_edge(LEFT)
        self.play(Write(fifty_one_squared[0]))
        self.wait(0.25)
        self.play(Write(fifty_one_squared[1:3]))
        self.wait(0.25)
        self.play(Write(fifty_one_squared[3:]))
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

        # try another approach and get stuck - 49^2=(50-1)^2
        self.forty_nine_squared.next_to(forty_nine_squared_1, DOWN, buff=0.75, aligned_edge=LEFT)
        self.play(Write(self.forty_nine_squared[0:2]))
        self.wait(0.5)
        self.play(Write(self.forty_nine_squared[2:]))
        self.wait()

        self.play(Circumscribe(self.forty_nine_squared[4:7], fade_out=True, run_time=2))
        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(fifty_one_squared, forty_nine_squared_1),
                self.forty_nine_squared.animate.to_corner(UL),
                lag_ratio=0.5
            )
        )
        self.wait()

    def get_formula(self):
        a_minus_b_squared_extended = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$($', '$a$', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$a$', '$-$', '$b$', '$)$', # 6:18
            ' $=$ ', '$a$', '$\cdot$', '$a$', '$+$', '$a$', '$\cdot$', '$($', '$-$', '$b$', '$)$', '$+$', # 18:31
            '$($', '$-$', '$b$', '$)$', '$\cdot$', '$a$', '$+$', '$($', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$-$', '$b$', '$)$', #31:46
            font_size=50
        ) # (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)
        a_minus_b_squared_extended.to_edge(LEFT)
        conn_line = ConnectionLine(a_minus_b_squared_extended[8], a_minus_b_squared_extended[14])

        self.play(Write(a_minus_b_squared_extended[0:6]))
        self.wait()
        self.play(Write(a_minus_b_squared_extended[6:18]))
        self.wait()
        self.play(Write(a_minus_b_squared_extended[18]))
        self.wait()

        # a•a
        self.play(
            AnimationGroup(
                Create(conn_line),
                AnimationGroup(
                    ClockwiseTransform(a_minus_b_squared_extended[8].copy(), a_minus_b_squared_extended[19], remover=True),
                    ClockwiseTransform(a_minus_b_squared_extended[14].copy(), a_minus_b_squared_extended[21], remover=True),
                    Write(a_minus_b_squared_extended[20])
                ),
                lag_ratio=0.75
            )
        )
        self.add(a_minus_b_squared_extended[19:22])
        self.wait()

        # a•(-b)
        self.play(
            AnimationGroup(
                Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[8], a_minus_b_squared_extended[16])),
                AnimationGroup(
                    ClockwiseTransform(a_minus_b_squared_extended[8].copy(), a_minus_b_squared_extended[23], remover=True),
                    ClockwiseTransform(a_minus_b_squared_extended[15:17].copy(), a_minus_b_squared_extended[26:28], remover=True),
                    Write(a_minus_b_squared_extended[22]),
                    Write(a_minus_b_squared_extended[24]),
                    Write(a_minus_b_squared_extended[25]),
                    Write(a_minus_b_squared_extended[28]),
                ),
                lag_ratio=0.75
            )
        )
        self.add(a_minus_b_squared_extended[22:29])
        self.wait()

        # (-b)•a
        self.play(
            AnimationGroup(
                Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[10], a_minus_b_squared_extended[14])),
                AnimationGroup(
                    ClockwiseTransform(a_minus_b_squared_extended[9:11].copy(), a_minus_b_squared_extended[31:33], remover=True),
                    ClockwiseTransform(a_minus_b_squared_extended[14].copy(), a_minus_b_squared_extended[35], remover=True),
                    Write(a_minus_b_squared_extended[29]),
                    Write(a_minus_b_squared_extended[30]),
                    Write(a_minus_b_squared_extended[33]),
                    Write(a_minus_b_squared_extended[34]),
                ),
                lag_ratio=0.75
            )
        )
        self.add(a_minus_b_squared_extended[29:36])
        self.wait()

        # (-b)•(-b)
        self.play(
            AnimationGroup(
                Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[10], a_minus_b_squared_extended[16])),
                AnimationGroup(
                    ClockwiseTransform(a_minus_b_squared_extended[9:11].copy(), a_minus_b_squared_extended[38:40], remover=True),
                    ClockwiseTransform(a_minus_b_squared_extended[15:17].copy(), a_minus_b_squared_extended[43:45], remover=True),
                    Write(a_minus_b_squared_extended[36]), # +
                    Write(a_minus_b_squared_extended[37]), # (
                    Write(a_minus_b_squared_extended[40]), # )
                    Write(a_minus_b_squared_extended[41]), # •
                    Write(a_minus_b_squared_extended[42]), # (
                    Write(a_minus_b_squared_extended[45]), # )
                ),
                lag_ratio=0.75
            )
        )
        self.add(a_minus_b_squared_extended[36:])
        self.wait()
