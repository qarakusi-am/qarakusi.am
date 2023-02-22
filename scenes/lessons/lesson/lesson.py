from manim import Scene, MathTex, Write, VGroup, AnimationGroup, Line, GrowFromEdge, Circumscribe, Wiggle, Indicate, SurroundingRectangle, Create
from manim import DOWN, LEFT, RIGHT, UP, DL
from manim import RED, ORANGE, YELLOW, GREEN

FONT_SIZE = 90

class Lesson(Scene):
    """Դասի նպատակն է բացատրել, թե բնական թվերի իրար տակ բազմապատկումը ոնց է բացատրվում բազմապատկման և գումարման բաշխական օրենքով։"""
    def construct(self):
        self.wait()

        tex1 = MathTex("7 \\cdot 134 = ", "938", font_size=115)
        tex1[-1].set_opacity(0)
        tex1.to_edge(UP)
        srr_rect = SurroundingRectangle(tex1, color=GREEN, buff=.2)
        self.play(
            Create(srr_rect),
            Write(tex1)
        )
        self.wait()

        tex2 = MathTex(
            "7 \\cdot 134 = 7 \\cdot (100 + 30+ 4) =",
            "7 \\cdot 100 + 7 \\cdot 30 + 7 \\cdot 4 =",
            "700 + 210 + 28 =",
            "700 + 200 + 10 + 20 + 8 =",
            "(700 + 200) + (10 + 20) + 8 =",
            "900 + 30 + 8 = 938",
            font_size=60
        )
        
        tex2.arrange(DOWN, aligned_edge=LEFT, buff=.4).to_edge(DL).shift(UP*.5)
        
        num1 = MathTex("134", font_size=FONT_SIZE)
        multiply_sign = MathTex("\\times", font_size=FONT_SIZE-20)
        num2 = MathTex("7", font_size=FONT_SIZE)

        num2.next_to(num1, DOWN, aligned_edge=RIGHT)
        multiply_sign.next_to(VGroup(num1, num2), LEFT)
        VGroup(num1, num2, multiply_sign).to_edge(RIGHT, buff=1.6).shift(UP*1.9)
        
        line1 = Line().set_length(VGroup(num1, num2).width+.4)
        line1.next_to(VGroup(num1, num2), DOWN)

        first_number = tex2[2][8:10].copy()
        second_number = tex2[2][4:7].copy()
        third_number = tex2[2][0:3].copy()

        for tex in tex2:
            if tex == tex2[3]:
                self.play(Write(tex[:4]))
                self.wait()
                self.play(Indicate(tex2[2][4:7]))
                self.wait()
                self.play(Write(tex[4:11]))
                self.wait()
                self.play(Indicate(tex2[2][8:10]))
                self.wait()
                self.play(Write(tex[11:]))
                self.wait()
                continue

            self.play(Write(tex))
            self.wait()

            if tex == tex2[2]:
                self.play(
                    AnimationGroup(
                        Write(num1),
                        Write(num2),
                        Write(multiply_sign),
                        lag_ratio=.6
                    )
                )
                self.wait()

                self.play(GrowFromEdge(line1, LEFT))
                self.wait()
                
                self.play(first_number.animate.scale(FONT_SIZE/60).next_to(line1, DOWN).align_to(num2, RIGHT))
                self.wait()

                self.play(second_number.animate.scale(FONT_SIZE/60).next_to(first_number, DOWN, aligned_edge=RIGHT))
                self.wait()

                self.play(third_number.animate.scale(FONT_SIZE/60).next_to(second_number, DOWN, aligned_edge=RIGHT))
                self.wait()
        
        numbers_in_red = VGroup(tex2[3][11:13], tex2[4][14:16])
        numbers_in_orange = VGroup(tex2[3][4:7], tex2[4][5:8])

        self.play(numbers_in_red.animate.set_color(RED))
        self.wait()
        self.play(numbers_in_orange.animate.set_color(ORANGE))
        self.wait()

        plus_sign = MathTex("+", font_size=FONT_SIZE)
        plus_sign.next_to(VGroup(first_number, second_number, third_number), LEFT)
        self.play(Write(plus_sign))

        line2 = line1.copy()
        line2.next_to(third_number, DOWN)
        self.play(GrowFromEdge(line2, LEFT))
        self.wait()

        miavorner = VGroup(
            first_number[-1],
            second_number[-1],
            third_number[-1]
        )
        self.play(Circumscribe(miavorner, fade_out=True, run_time=2))
        self.wait()

        answer = MathTex("938", font_size=FONT_SIZE)
        answer.next_to(line2, DOWN).align_to(third_number, RIGHT)
        self.play(Write(answer[0][-1]))
        self.wait()

        tasnavorner = VGroup(
            first_number[-2],
            second_number[-2],
            third_number[-2]
        )

        self.play(tasnavorner[0].animate.set_color(RED))
        self.play(
            Wiggle(tasnavorner[0], n_wiggles=12, run_time=4),
            Wiggle(numbers_in_red, n_wiggles=12, run_time=4),
        )
        self.wait()
        
        self.play(Circumscribe(tasnavorner, fade_out=True, run_time=2))
        self.wait()
        self.play(Write(answer[0][-2]))
        self.wait()

        haryuravoner = VGroup(
            second_number[0],
            third_number[0]
        )
        self.play(haryuravoner[0].animate.set_color(ORANGE))
        self.play(
            Wiggle(haryuravoner[0], n_wiggles=12, run_time=4),
            Wiggle(numbers_in_orange, n_wiggles=12, run_time=4)
        )
        self.wait()

        self.play(Circumscribe(haryuravoner, fade_out=True, run_time=2))
        self.wait()
        self.play(Write(answer[0][0]))
        self.wait()

        self.play(
            tex2[-1][-3:].animate.set_color(YELLOW),
            answer.animate.set_color(YELLOW)
        )
        self.play(
            Indicate(tex2[-1][-3:]),
            Indicate(answer)
        )
        self.wait()

        self.play(answer.copy().animate.scale(115/FONT_SIZE).move_to(tex1[-1].get_center()))

        self.wait(2)
