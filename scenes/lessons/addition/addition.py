from manim import Scene, MathTex, VGroup, Write, TransformFromCopy, SurroundingRectangle, Line, Circumscribe, GrowFromEdge, ReplacementTransform, Create, Transform, FadeOut
from manim import DOWN, LEFT, UP, RIGHT
from manim import PI
from manim import GREEN, ORANGE

FONT_SIZE = 150

class Addition(Scene):
    def construct(self):
        self.wait()

        task_tex = MathTex("4819", "+", "674", "=", "5493", font_size=120)
        srr_rect = SurroundingRectangle(task_tex, color=GREEN, buff=.2)
        VGroup(task_tex, srr_rect).to_edge(UP)

        self.play(Write(task_tex[:-1]))
        self.play(Create(srr_rect))
        self.wait()

        MathTex.set_default(font_size=FONT_SIZE)

        first_number = MathTex(*"4819")
        second_number = MathTex(*"674")

        both_numbers = VGroup(first_number, second_number)
        both_numbers.arrange(DOWN, aligned_edge=RIGHT).next_to(srr_rect, DOWN, buff=1.1,  aligned_edge=LEFT).shift(RIGHT*2)
        
        plus_sign = MathTex("+", font_size=FONT_SIZE/2)
        plus_sign.next_to(both_numbers, LEFT)

        line = Line().set_length(both_numbers.width+.3)
        line.next_to(both_numbers, DOWN)

        self.play(TransformFromCopy(task_tex[0], first_number))
        self.play(TransformFromCopy(task_tex[1], plus_sign))
        self.play(TransformFromCopy(task_tex[2], second_number, path_arc=4*PI/5))
        self.play(GrowFromEdge(line, LEFT))
        self.wait()

        answer = MathTex(*"5493")
        answer.next_to(line, DOWN).align_to(first_number, RIGHT)

        # 9+4=13
        self.play(Circumscribe(VGroup(first_number[-1], second_number[-1]), fade_out=True))
        self.wait()

        number1 = MathTex(*"13")
        number1.move_to(answer, RIGHT)

        self.play(TransformFromCopy(VGroup(first_number[-1], second_number[-1]), number1))
        self.wait()

        tasnavor = number1[0].copy()
        tasnavor.save_state()
        tasnavor.set_color(ORANGE)
        self.play(
            ReplacementTransform(number1[0], tasnavor),
            ReplacementTransform(number1[1], answer[-1])
        )
        self.wait()

        # 1+7=8 (+1 -> 9)
        self.play(tasnavor.animate.set_opacity(.5))
        self.wait()

        temp_srr_rect = SurroundingRectangle(VGroup(first_number[-2], second_number[-2]))
        self.play(Create(temp_srr_rect))
        self.wait()
        self.play(tasnavor.animate.restore())
        new_temp_srr_rect = SurroundingRectangle(VGroup(first_number[-2], second_number[-2], tasnavor))
        self.play(Transform(temp_srr_rect, new_temp_srr_rect))
        self.wait()

        number2 = MathTex("9")
        number2.move_to(answer[-2])

        self.play(ReplacementTransform(VGroup(VGroup(first_number[-2], second_number[-2]).copy(), tasnavor, temp_srr_rect), number2))
        self.wait()

        # 8+6=14
        self.play(Circumscribe(VGroup(first_number[-3], second_number[-3]), fade_out=True))
        self.wait()

        number3 = MathTex(*"14")
        number3.move_to(answer[-3], RIGHT)

        self.play(TransformFromCopy(VGroup(first_number[-3], second_number[-3]), number3))
        self.wait()

        tasnavor = number3[0].copy()
        tasnavor.save_state()
        tasnavor.set_color(ORANGE)
        self.play(
            ReplacementTransform(number3[0], tasnavor),
            ReplacementTransform(number3[1], answer[-3])
        )
        self.wait()

        # 4 (+1 -> 5)
        self.play(tasnavor.animate.set_opacity(.5))
        self.wait()

        temp_srr_rect = SurroundingRectangle(first_number[-4])
        self.play(Create(temp_srr_rect))
        self.wait()
        self.play(tasnavor.animate.restore())
        new_temp_srr_rect = SurroundingRectangle(VGroup(first_number[-4], tasnavor))
        self.play(Transform(temp_srr_rect, new_temp_srr_rect))
        self.wait()

        self.play(ReplacementTransform(VGroup(first_number[-4].copy(), tasnavor, temp_srr_rect), answer[-4]))
        self.wait()

        # answer
        self.play(TransformFromCopy(answer, task_tex[-1], path_arc=-PI/4))

        self.wait(2)
