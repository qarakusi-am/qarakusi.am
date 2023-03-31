from manim import Scene, Tex, ReplacementTransform, Write, Line, MathTex, VGroup, FadeIn, GrowFromEdge, Transform, AnimationGroup, Arrow, GrowArrow, FadeOut, Indicate, TransformFromCopy
from manim import UP, DOWN, RIGHT, LEFT
from manim import PI
from manim import ORANGE, WHITE, GREEN
from qarakusiscene import TaskNumberBox
from numpy import array
from .text import *

FONT_SIZE = 35
MATH_FONT_SIZE = 90

class Problem12737(Scene):
    def construct(self):
        self.wait()

        # task number
        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))
        self.wait()

        # write task
        task_tex = Tex(task_str, font_size=2.2*FONT_SIZE)
        self.play(Write(task_tex))
        self.wait()

        new_task_tex = Tex(new_task_str, font_size=2*FONT_SIZE)
        new_task_tex.to_edge(UP)
        self.play(ReplacementTransform(task_tex, new_task_tex))
        self.wait()

        # վերլուծել արտադրիչների 1-ին թիվը
        numbers_on_left_1 = VGroup(
            MathTex("60", font_size=MATH_FONT_SIZE),
            MathTex("30", font_size=MATH_FONT_SIZE),
            MathTex("15", font_size=MATH_FONT_SIZE),
            MathTex("5", font_size=MATH_FONT_SIZE),
            MathTex("1", font_size=MATH_FONT_SIZE)
        ).arrange(DOWN, aligned_edge=RIGHT)

        numbers_on_right_1 = VGroup(
            MathTex("2", font_size=MATH_FONT_SIZE),
            MathTex("2", font_size=MATH_FONT_SIZE),
            MathTex("3", font_size=MATH_FONT_SIZE),
            MathTex("5", font_size=MATH_FONT_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT)

        line_1 = Line().rotate(PI/2).set_length(numbers_on_left_1.height+.1)

        verlucel_parz_artadrichneri_1 = VGroup(
            numbers_on_left_1,
            line_1,
            numbers_on_right_1
        ).arrange(aligned_edge=UP).to_edge(LEFT, buff=2)

        for index, tex in enumerate(numbers_on_left_1):
            self.play(Write(tex))
            self.wait()

            if index == 0:
                self.play(GrowFromEdge(line_1, UP))
                self.wait()
            elif index == len(numbers_on_left_1)-1:
                break
            
            self.play(Write(numbers_on_right_1[index]))
            self.wait()

        # վերլուծել արտադրիչների 2-րդ թիվը
        numbers_on_left_2 = VGroup(
            MathTex("135", font_size=MATH_FONT_SIZE),
            MathTex("45", font_size=MATH_FONT_SIZE),
            MathTex("15", font_size=MATH_FONT_SIZE),
            MathTex("5", font_size=MATH_FONT_SIZE),
            MathTex("1", font_size=MATH_FONT_SIZE)
        ).arrange(DOWN, aligned_edge=RIGHT)

        numbers_on_right_2 = VGroup(
            MathTex("3", font_size=MATH_FONT_SIZE),
            MathTex("3", font_size=MATH_FONT_SIZE),
            MathTex("3", font_size=MATH_FONT_SIZE),
            MathTex("5", font_size=MATH_FONT_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT)

        line_2 = Line().rotate(PI/2).set_length(numbers_on_left_2.height+.1)

        verlucel_parz_artadrichneri_2 = VGroup(
            numbers_on_left_2,
            line_2,
            numbers_on_right_2
        ).arrange(aligned_edge=UP).to_edge(RIGHT, buff=2)

        for index, tex in enumerate(numbers_on_left_2):
            self.play(Write(tex))
            self.wait()

            if index == 0:
                self.play(GrowFromEdge(line_2, UP))
                self.wait()
            elif index == len(numbers_on_left_2)-1:
                break
            
            self.play(Write(numbers_on_right_2[index]))
            self.wait()
        
        # Ձևափոխել տողերով գրածի
        temp1 = MathTex("60", "=", "2", "\\cdot", "2", "\\cdot", "3", "\\cdot", "5", font_size=MATH_FONT_SIZE)
        temp2 = MathTex("135", "=", "3", "\\cdot", "3", "\\cdot", "3", "\\cdot", "5", font_size=MATH_FONT_SIZE)
        VGroup(
            temp1, temp2
        ).arrange(DOWN, aligned_edge=RIGHT, buff=.6).next_to(new_task_tex, DOWN, buff=.9)

        self.play(
            AnimationGroup(
                Transform(verlucel_parz_artadrichneri_1, temp1),
                Transform(verlucel_parz_artadrichneri_2, temp2),
                lag_ratio=.4
            )
        )
        self.wait()

        temp = VGroup(verlucel_parz_artadrichneri_1, verlucel_parz_artadrichneri_2).copy().to_edge(RIGHT, buff=2.2)
        VGroup(
            temp[0][:8],
            temp[1][:2]
        ).next_to(temp[1][2], LEFT, aligned_edge=DOWN)

        self.play(
            Transform(VGroup(verlucel_parz_artadrichneri_1, verlucel_parz_artadrichneri_2), temp)
        )
        self.wait()

        # գտնել ամենամեծ ընդհանուր բաժանարարը
        amenamec_ynd_bajanarar = MathTex("(60, 135)", "=", "3", "\\cdot", "5", "=", "15", font_size=MATH_FONT_SIZE)
        amenamec_ynd_bajanarar.next_to(verlucel_parz_artadrichneri_2, DOWN, aligned_edge=LEFT, buff=.8)
        amenamec_ynd_bajanarar.shift(array([verlucel_parz_artadrichneri_1[1].get_x()-amenamec_ynd_bajanarar[1].get_x(), 0, 0]))
        self.play(Write(amenamec_ynd_bajanarar[:2]))
        self.wait()

        tex1 = Tex(tex1_str, font_size=2*FONT_SIZE)
        tex1.next_to(verlucel_parz_artadrichneri_2, DOWN, aligned_edge=RIGHT, buff=1.5).shift(RIGHT*2)
        
        arrow = Arrow(
            start=tex1.get_top()+array([0, .1, 0]),
            end=verlucel_parz_artadrichneri_1[2:6].get_center()+array([0, -1.4, 0])
        )
        self.play(
            Write(tex1),
            GrowArrow(arrow)
        )
        self.wait()

        self.play(FadeOut(arrow, tex1))
        self.wait()

        self.play(
            VGroup(
                verlucel_parz_artadrichneri_1[6],
                verlucel_parz_artadrichneri_2[2]
            ).animate.set_color(ORANGE)
        )
        self.play(
            Indicate(verlucel_parz_artadrichneri_1[6], color=None),
            Indicate(verlucel_parz_artadrichneri_2[2], color=None)
        )
        self.wait()

        self.play(
            TransformFromCopy(
                VGroup(
                    verlucel_parz_artadrichneri_1[6],
                    verlucel_parz_artadrichneri_2[2]
                ),
                amenamec_ynd_bajanarar[2]
            )
        )
        self.wait()

        self.play(
            VGroup(
                verlucel_parz_artadrichneri_1[-1],
                verlucel_parz_artadrichneri_2[-1]
            ).animate.set_color(ORANGE)
        )
        self.play(
            Indicate(verlucel_parz_artadrichneri_1[-1], color=None),
            Indicate(verlucel_parz_artadrichneri_2[-1], color=None)
        )
        self.wait()

        self.play(
            AnimationGroup(
                TransformFromCopy(
                    VGroup(
                        verlucel_parz_artadrichneri_1[-1],
                        verlucel_parz_artadrichneri_2[-1]
                    ),
                    amenamec_ynd_bajanarar[4]
                ),
                Write(amenamec_ynd_bajanarar[3]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(Write(amenamec_ynd_bajanarar[5:]))
        self.wait()

        # գտնել ամենափոքր ընդհանուր բազմապատիկը
        self.play(
            amenamec_ynd_bajanarar.animate.to_edge(DOWN, buff=1.5),
            FadeOut(new_task_tex),
            VGroup(
                verlucel_parz_artadrichneri_1,
                verlucel_parz_artadrichneri_2
            ).animate.to_edge(UP, buff=1.2).set_color(WHITE)
        )
        self.wait()

        amenapoqr_ynd_bazmapatik = MathTex("[60, 135]", "=", "2", "\\cdot", "2", "\\cdot", "3", "\\cdot", "3", "\\cdot", "3", "\\cdot", "5", "=", "540", font_size=MATH_FONT_SIZE)
        amenapoqr_ynd_bazmapatik.next_to(verlucel_parz_artadrichneri_2, DOWN, buff=1.2, aligned_edge=LEFT)
        amenapoqr_ynd_bazmapatik.shift(array([verlucel_parz_artadrichneri_1[1].get_x()-amenapoqr_ynd_bazmapatik[1].get_x(), 0, 0]))
        self.play(Write(amenapoqr_ynd_bazmapatik[:2]))
        self.wait()

        self.play(
            VGroup(
                verlucel_parz_artadrichneri_1[2],
                verlucel_parz_artadrichneri_1[4]
            ).animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            AnimationGroup(
                TransformFromCopy(
                    VGroup(
                        verlucel_parz_artadrichneri_1[2],
                        verlucel_parz_artadrichneri_1[4]
                    ),
                    VGroup(
                        amenapoqr_ynd_bazmapatik[2],
                        amenapoqr_ynd_bazmapatik[4]
                    )
                ),
                Write(amenapoqr_ynd_bazmapatik[3]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            VGroup(
                verlucel_parz_artadrichneri_2[2],
                verlucel_parz_artadrichneri_2[4],
                verlucel_parz_artadrichneri_2[6]
            ).animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            AnimationGroup(
                TransformFromCopy(
                    VGroup(
                        verlucel_parz_artadrichneri_2[2],
                        verlucel_parz_artadrichneri_2[4],
                        verlucel_parz_artadrichneri_2[6]
                    ),
                    VGroup(
                        amenapoqr_ynd_bazmapatik[6],
                        amenapoqr_ynd_bazmapatik[8],
                        amenapoqr_ynd_bazmapatik[10]
                    )
                ),
                Write(
                    VGroup(
                        amenapoqr_ynd_bazmapatik[5],
                        amenapoqr_ynd_bazmapatik[7],
                        amenapoqr_ynd_bazmapatik[9]
                    )
                ),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            VGroup(
                verlucel_parz_artadrichneri_1[-1],
                verlucel_parz_artadrichneri_2[-1]
            ).animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            AnimationGroup(
                TransformFromCopy(
                    VGroup(
                        verlucel_parz_artadrichneri_1[-1],
                        verlucel_parz_artadrichneri_2[-1]
                    ),
                    amenapoqr_ynd_bazmapatik[12]
                ),
                Write(amenapoqr_ynd_bazmapatik[11]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(Write(amenapoqr_ynd_bazmapatik[13:]))

        self.wait(2)
