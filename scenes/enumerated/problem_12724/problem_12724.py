from manim import Scene, MathTex, Write, VGroup, FadeOut, Line, GrowFromEdge, Circumscribe, Indicate, SurroundingRectangle, Create, FadeIn, TransformFromCopy, ReplacementTransform
from manim import DOWN, LEFT, RIGHT, UP
from manim import GREEN, ORANGE
from manim import PI
from qarakusiscene import TaskNumberBox
from .text import task_number_str

FONT_SIZE = 100

class Problem12724(Scene):
    """Վիդեոյի նպատակն է բացատրել երկնիշ և եռանիշ թվերի իրար տակ բազմապատկումը, (427⋅32)"""
    def construct(self):
        self.wait()

        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))

        task = MathTex("427 \\cdot 32 = ", "13664", font_size=FONT_SIZE)
        task[-1].set_opacity(0)
        task.to_edge(UP)
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
        VGroup(num1, num2, multiplication_sign).next_to(srr_rect, DOWN, buff=.4, aligned_edge=LEFT).shift(RIGHT)
        
        line1 = Line().set_length(VGroup(num1, num2).width+.4)
        line1.next_to(VGroup(num1, num2), DOWN)

        self.play(Write(num1))
        self.play(Write(num2))
        self.play(Write(multiplication_sign))
        self.play(GrowFromEdge(line1, LEFT))
        self.wait()

        first_number = MathTex(*"854", font_size=FONT_SIZE)
        second_number = MathTex(*"1281", font_size=FONT_SIZE)

        first_number.next_to(line1, DOWN).align_to(num2, RIGHT)
        second_number.next_to(first_number, DOWN).align_to(first_number[-2], RIGHT)

        avelacav1 = MathTex("1", font_size=FONT_SIZE, color=ORANGE).next_to(num1, LEFT, buff=2)
        avelacav2 = MathTex("2", font_size=FONT_SIZE, color=ORANGE).next_to(num1, LEFT, buff=2)

        for index in range(len(num1[0])):
            digit_index = len(num1[0])-index-1
            self.play(
                Indicate(num1[0][digit_index]),
                Indicate(num2[0][-1])
            )
            self.wait()
            
            if index == 0:
                tex = MathTex(*"14", font_size=FONT_SIZE)
                tex.next_to(line1, LEFT).shift(LEFT*5).align_to(first_number, DOWN)
                self.play(tex.animate.shift(RIGHT*5))
                self.wait()
                self.play(
                    ReplacementTransform(tex[0], avelacav1),
                    ReplacementTransform(tex[1], first_number[len(first_number)-index-1])
                )
                self.wait()

            if index == 1:
                tex = MathTex("4", font_size=FONT_SIZE)
                tex.next_to(line1, LEFT).shift(LEFT*5).align_to(first_number, DOWN)
                self.play(tex.animate.align_to(avelacav1, RIGHT))
                self.wait()
                new_tex = MathTex("5", font_size=FONT_SIZE).move_to(tex.get_center())
                self.play(ReplacementTransform(VGroup(tex, avelacav1), new_tex))
                self.wait()
                self.play(ReplacementTransform(new_tex, first_number[len(first_number)-index-1]))
                self.wait()
            
            elif index == 2:
                self.play(Write(first_number[len(first_number)-index-1]))
                self.wait()

        for index in range(len(num1[0])):
            digit_index = len(num1[0])-index-1
            self.play(
                Indicate(num1[0][digit_index]),
                Indicate(num2[0][0])
            )
            self.wait()

            if index == 0:
                tex = MathTex(*"21", font_size=FONT_SIZE)
                tex.next_to(line1, LEFT).shift(LEFT*5).align_to(second_number, DOWN)
                self.play(tex.animate.align_to(avelacav1, RIGHT))
                self.wait()
                self.play(
                    ReplacementTransform(tex[0], avelacav2),
                    ReplacementTransform(tex[1], second_number[len(second_number)-index-1])
                )
                self.wait()
            
            elif index == 1:
                tex = MathTex("6", font_size=FONT_SIZE)
                tex.next_to(line1, LEFT).shift(LEFT*5).align_to(second_number, DOWN)
                self.play(tex.animate.align_to(avelacav1, RIGHT))
                self.wait()
                new_tex = MathTex("8", font_size=FONT_SIZE).move_to(tex.get_center())
                self.play(ReplacementTransform(VGroup(tex, avelacav2), new_tex))
                self.wait()
                self.play(ReplacementTransform(new_tex, second_number[len(second_number)-index-1]))
                self.wait()
            
            elif index == 2:
                tex = MathTex("12", font_size=FONT_SIZE)
                tex.set_y(second_number.get_y()).to_edge(LEFT).shift(LEFT*2)
                self.play(tex.animate.move_to(second_number[:2].get_center()))
                self.wait()
        
        plus_sign = MathTex("+", font_size=FONT_SIZE)
        plus_sign.next_to(VGroup(first_number, second_number), LEFT)
        self.play(Write(plus_sign))

        line2 = line1.copy().set_length(VGroup(first_number, second_number).width+.4)
        line2.next_to(VGroup(second_number, first_number), DOWN)
        self.play(GrowFromEdge(line2, LEFT))
        self.wait()

        miavorner = first_number[-1]
        self.play(Circumscribe(miavorner, fade_out=True, run_time=2, buff=.04))
        self.wait()

        answer = MathTex("13664", font_size=FONT_SIZE)
        answer.next_to(line2, DOWN).align_to(first_number, RIGHT)
        self.play(TransformFromCopy(miavorner, answer[0][-1]))
        self.wait()

        tasnavorner = VGroup(
            first_number[-2],
            second_number[-1]
        )
        
        self.play(Circumscribe(tasnavorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        self.play(Write(answer[0][-2]))
        self.wait()

        haryuravoner = VGroup(
            first_number[-3],
            second_number[-2]
        )

        self.play(Circumscribe(haryuravoner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        tex = MathTex(*"16", font_size=FONT_SIZE)
        tex.move_to(answer[0][-3], aligned_edge=RIGHT)
        self.play(Write(tex))
        self.wait()
        avelacav1 = MathTex("1", font_size=FONT_SIZE, color=ORANGE).next_to(answer, LEFT, buff=1.7)
        self.play(ReplacementTransform(tex[0], avelacav1))
        self.add(answer[0][-3])
        self.remove(tex[1])
        self.wait()

        hazaravorner = VGroup(
            second_number[-3]
        )

        self.play(Circumscribe(hazaravorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        tex = MathTex("2", font_size=FONT_SIZE)
        tex.move_to(second_number[-3].get_center())
        # self.play(tex.animate.move_to(answer[0][-4].get_center()))
        self.wait()
        self.play(ReplacementTransform(VGroup(tex, avelacav1), answer[0][-4]))
        self.wait()

        tashazaravorner = second_number[-4]

        self.play(Circumscribe(tashazaravorner, fade_out=True, run_time=2, buff=.04))
        self.wait()
        self.play(TransformFromCopy(tashazaravorner, answer[0][-5]))
        self.wait()

        self.play(answer.copy().animate(path_arc=PI/2).match_height(task[-1]).move_to(task[-1].get_center()))

        self.wait(2)
