from manim import Scene, MathTex, Write, VGroup, FadeOut, Line, GrowFromEdge, Circumscribe, ReplacementTransform, Indicate, SurroundingRectangle, Create, FadeIn
from manim import DOWN, LEFT, RIGHT, UP
from manim import RED, GREEN
from qarakusiscene import TaskNumberBox
from .text import task_number_str

FONT_SIZE = 90

class Problem12724(Scene):
    """Վիդեոյի նպատակն է բացատրել երկնիշ և եռանիշ թվերի իրար տակ բազմապատկումը, (427⋅32)"""
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))

        task = MathTex("427 \\cdot 32 = ", "13664", font_size=115)
        task[-1].set_opacity(0)
        task.to_edge(LEFT)
        srr_rect = SurroundingRectangle(task, color=GREEN, buff=.2)
        self.play(
            Create(srr_rect),
            Write(task)
        )
        self.wait()

        num1 = MathTex("427", font_size=FONT_SIZE)
        multiplication_sign = MathTex("\\times", font_size=FONT_SIZE-20)
        num2 = MathTex("32", font_size=FONT_SIZE)

        num2.next_to(num1, DOWN, aligned_edge=RIGHT)
        multiplication_sign.next_to(VGroup(num1, num2), LEFT)
        VGroup(num1, num2, multiplication_sign).to_edge(RIGHT, buff=1.6).to_edge(UP)
        
        line1 = Line().set_length(VGroup(num1, num2).width+.4)
        line1.next_to(VGroup(num1, num2), DOWN)

        self.play(Write(num1))
        self.play(Write(num2))
        self.play(Write(multiplication_sign))
        self.play(GrowFromEdge(line1, LEFT))
        self.wait()

        first_number = MathTex("14", font_size=FONT_SIZE)
        second_number = MathTex("40", font_size=FONT_SIZE)
        third_number = MathTex("800", font_size=FONT_SIZE)

        numbers1 = VGroup(first_number, second_number, third_number)
        numbers1.arrange(DOWN, aligned_edge=RIGHT).next_to(line1, DOWN).align_to(num2, RIGHT)

        for index in range(3):
            digit_index = len(num1[0])-index-1
            self.play(
                Indicate(num1[0][digit_index]),
                Indicate(num2[0][-1])
            )
            self.wait()
            self.play(Write(numbers1[index]))
            self.wait()
        
        first_number1 = MathTex("210", font_size=FONT_SIZE)
        second_number1 = MathTex("600", font_size=FONT_SIZE)
        third_number1 = MathTex("12000", font_size=FONT_SIZE)

        numbers2 = VGroup(first_number1, second_number1, third_number1)
        numbers2.arrange(DOWN, aligned_edge=RIGHT).next_to(numbers1, DOWN).align_to(num2, RIGHT)

        for index in range(3):
            digit_index = len(num1[0])-index-1
            self.play(
                Indicate(num1[0][digit_index]),
                Indicate(num2[0][0])
            )
            self.wait()
            self.play(Write(numbers2[index]))
            self.wait()
        
        plus_sign = MathTex("+", font_size=FONT_SIZE)
        plus_sign.next_to(VGroup(first_number, second_number, third_number, first_number1, second_number1, third_number1), LEFT)
        self.play(Write(plus_sign))

        line2 = line1.copy().set_length(third_number1.width+.4)
        line2.next_to(third_number1, DOWN)
        self.play(GrowFromEdge(line2, LEFT))
        self.wait()

        self.play(
            VGroup(
                num1,
                num2,
                multiplication_sign,
                line1,
                numbers1,
                numbers2,
                plus_sign,
                line2
            ).animate.scale(.85).to_edge(UP).to_edge(RIGHT, buff=1.6)
        )
        self.wait()
        NEW_FONT_SIZE = FONT_SIZE * .85

        miavorner = VGroup(
            first_number[0][-1],
            second_number[0][-1],
            third_number[0][-1],
            first_number1[0][-1],
            second_number1[0][-1],
            third_number1[0][-1]
        )
        self.play(Circumscribe(miavorner, fade_out=True, run_time=2, buff=.04))
        self.wait()

        answer = MathTex("13664", font_size=NEW_FONT_SIZE)
        answer.next_to(line2, DOWN).align_to(third_number, RIGHT)
        self.play(Write(answer[0][-1]))
        self.wait()

        tasnavorner = VGroup(
            first_number[0][-2],
            second_number[0][-2],
            third_number[0][-2],
            first_number1[0][-2],
            second_number1[0][-2],
            third_number1[0][-2]
        )
        
        self.play(Circumscribe(tasnavorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        self.play(Write(answer[0][-2]))
        self.wait()

        haryuravoner = VGroup(
            third_number[0][-3],
            first_number1[0][-3],
            second_number1[0][-3],
            third_number1[0][-3]
        )

        self.play(Circumscribe(haryuravoner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        tex1 = MathTex("1", "6", font_size=FONT_SIZE*1.5)
        tex1.to_edge(DOWN, buff=1.3).shift(LEFT*3)
        self.play(Write(tex1))
        self.wait()
        self.play(tex1[0].animate.set_color(RED))
        self.wait()
        self.play(ReplacementTransform(tex1[1], answer[0][-3]))
        self.wait()

        hazaravorner = VGroup(
            third_number1[0][-4]
        )

        self.play(Circumscribe(hazaravorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        tex2 = MathTex("+ \\ 2 =", "3", font_size=FONT_SIZE*1.6)
        tex2.next_to(tex1[0])
        self.play(Write(tex2))
        self.wait()
        self.play(
            ReplacementTransform(tex2[1], answer[0][-4]),
            FadeOut(tex1, tex2[:1])
        )
        self.wait()

        tashazaravorner = VGroup(
            third_number1[0][-5]
        )

        self.play(Circumscribe(tashazaravorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        self.play(Write(answer[0][-5]))
        self.wait()

        self.play(answer.copy().animate.match_height(task[-1]).move_to(task[-1].get_center()))

        self.wait(2)
