from manim import Scene, MathTex, SurroundingRectangle, Write, Create, Line, GrowFromEdge, Indicate, Wiggle, VGroup, TransformFromCopy, AnimationGroup, FadeOut
from manim import GREEN, RED, WHITE, YELLOW, BLACK
from manim import UP, LEFT, DOWN, RIGHT, UL
from manim import PI

FONT_SIZE = 85

class Division_2(Scene):
    """Այս վիդեոյի նպատակն է սյունակով բաժանում սովորեցնելը"""
    def construct(self):
        self.wait()

        task = MathTex("56916", ":", "27", "=", "2108", font_size=1.3*FONT_SIZE)
        task[-1].set_color(YELLOW).set_opacity(0)
        task.to_edge(UP)
        srr_rect = SurroundingRectangle(task, color=GREEN, buff=.2, fill_color=BLACK)

        self.play(
            Write(task),
            Create(srr_rect)
        )
        self.wait()

        self.play(VGroup(srr_rect, task).animate.to_edge(RIGHT))
        bajanarar_bajaneli = task[:3].copy().scale(1/1.3).to_corner(UL).shift(RIGHT*.8)
        bajanarar_bajaneli[0].shift(LEFT*.15)
        self.play(
            TransformFromCopy(task[:3], bajanarar_bajaneli, path_arc=PI/2),
            VGroup(srr_rect, task[:-1]).animate.set_opacity(.7).scale(.75).to_edge(RIGHT)
        )
        self.wait()

        line1 = Line(
            start=bajanarar_bajaneli[1].get_top(),
            end=bajanarar_bajaneli[1].get_bottom(),
            stroke_width=8
        ).set_length(2.5).align_to(bajanarar_bajaneli, UP)
        self.play(
            GrowFromEdge(line1, UP),
            FadeOut(bajanarar_bajaneli[1])
        )

        line2 = line1.copy().rotate(PI/2)
        line2.set_length(bajanarar_bajaneli[1:].width+.6).next_to(bajanarar_bajaneli[1:], DOWN, buff=.4, aligned_edge=LEFT).align_to(line1, LEFT)
        self.play(GrowFromEdge(line2, LEFT))
        self.wait()

        self.play(Indicate(bajanarar_bajaneli[-1]))
        self.wait()

        self.play(bajanarar_bajaneli[0][0].animate.set_color(RED))
        self.wait()

        self.play(bajanarar_bajaneli[0][:2].animate.set_color(GREEN))
        self.wait()

        self.play(
            Wiggle(bajanarar_bajaneli[0][:2]),
            Wiggle(bajanarar_bajaneli[-1])
        )
        self.wait()

        answer = MathTex(*"2108", font_size=FONT_SIZE)
        answer.next_to(bajanarar_bajaneli[-1], DOWN, aligned_edge=LEFT, buff=.8)
        self.play(Write(answer[0]))
        self.wait()

        self.play(bajanarar_bajaneli[0][:2].animate.set_color(WHITE))
        self.wait()

        two_time_twentytwo = MathTex("2 \\cdot 27 = ", "54", font_size=1.2*FONT_SIZE)
        two_time_twentytwo.next_to(task, DOWN, buff=2.8)
        self.play(Write(two_time_twentytwo))
        self.wait()

        tex1 = two_time_twentytwo[-1].copy()
        self.play(tex1.animate(path_arc=-PI/2).scale(1/1.2).next_to(bajanarar_bajaneli[0], DOWN, aligned_edge=LEFT))
        minus_sign1 = MathTex("-", font_size=0.7*FONT_SIZE)
        minus_sign1.next_to(VGroup(bajanarar_bajaneli[0][:3], tex1), LEFT)
        self.play(Write(minus_sign1))
        self.wait()

        line3 = Line().set_length(tex1.width)
        line3.next_to(tex1, DOWN, aligned_edge=LEFT)
        self.play(GrowFromEdge(line3, LEFT))
        self.wait()

        tex2 = MathTex("2", font_size=FONT_SIZE, color=RED)
        tex2.next_to(line3, DOWN, aligned_edge=RIGHT)
        self.play(
            Write(tex2),
            FadeOut(two_time_twentytwo)
        )
        self.wait()

        tex3 = bajanarar_bajaneli[0][2].copy()
        self.play(
            tex3.animate.set_y(tex2.get_y()).set_color(GREEN),
            tex2.animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            Wiggle(VGroup(tex2, tex3)),
            Wiggle(bajanarar_bajaneli[-1])
        )
        self.wait()

        self.play(Write(answer[1]))
        self.wait()

        self.play(VGroup(tex2, tex3).animate.set_color(WHITE))
        self.wait()

        one_time_twentytwo = MathTex("1 \\cdot 27 =", "27", font_size=1.2*FONT_SIZE)
        one_time_twentytwo.move_to(two_time_twentytwo, aligned_edge=LEFT)
        self.play(Write(one_time_twentytwo))
        self.wait()

        tex4 = one_time_twentytwo[-1].copy()
        self.play(
            tex4.animate(path_arc=-PI/2).scale(1/1.2).next_to(tex2, DOWN, aligned_edge=LEFT),
            line1.animate.set_length(4).align_to(bajanarar_bajaneli, UP)
        )
        minus_sign2 = minus_sign1.copy()
        minus_sign2.next_to(VGroup(tex2, tex3, tex4), LEFT)
        self.play(Write(minus_sign2))
        self.wait()

        line4 = Line().set_length(tex4.width)
        line4.next_to(tex4, DOWN, aligned_edge=LEFT)
        self.play(GrowFromEdge(line4, LEFT))
        self.wait()

        self.play(FadeOut(one_time_twentytwo))

        tex5 = MathTex("2", font_size=FONT_SIZE, color=RED)
        tex5.next_to(line4, DOWN, aligned_edge=RIGHT)
        self.play(Write(tex5))
        self.wait()

        tex6 = bajanarar_bajaneli[0][-2].copy()
        self.play(
            tex6.animate.set_y(tex5.get_y()).set_color(RED)
        )
        self.wait()

        self.play(
            Wiggle(VGroup(tex5, tex6)),
            Wiggle(bajanarar_bajaneli[-1])
        )
        self.wait()

        self.play(Write(answer[2]))
        self.wait()

        tex7 = bajanarar_bajaneli[0][-1].copy()
        self.play(
            tex7.animate.set_y(tex6.get_y()).set_color(GREEN),
            tex6.animate.set_color(GREEN),
            tex5.animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            Wiggle(VGroup(tex5, tex6, tex7)),
            Wiggle(bajanarar_bajaneli[-1])
        )
        self.wait()

        self.play(Write(answer[3]))
        self.wait()

        self.play(VGroup(tex5, tex6, tex7).animate.set_color(WHITE))
        self.wait()

        eight_time_twentytwo = MathTex("8 \\cdot 27 =", "216", font_size=1.2*FONT_SIZE)
        eight_time_twentytwo.move_to(two_time_twentytwo, aligned_edge=LEFT)
        self.play(Write(eight_time_twentytwo))
        tex8 = eight_time_twentytwo[-1].copy()
        self.wait()
        self.play(
            AnimationGroup(
                tex8.animate(path_arc=-PI/2).scale(1/1.2).next_to(tex7, DOWN, aligned_edge=RIGHT),
                lag_ratio=.6
            )
        )
        minus_sign3 = minus_sign1.copy()
        minus_sign3.next_to(VGroup(tex5, tex6, tex7, tex8), LEFT)
        self.play(Write(minus_sign3))
        self.wait()

        line5 = Line().set_length(VGroup(tex5, tex6, tex7).width+.1)
        line5.next_to(tex8, DOWN, aligned_edge=RIGHT)
        self.play(
            GrowFromEdge(line5, LEFT),
            FadeOut(eight_time_twentytwo)
        )
        self.wait()

        tex9 = MathTex("0", font_size=FONT_SIZE)
        tex9.next_to(line5, DOWN, aligned_edge=RIGHT)
        self.play(Write(tex9))
        self.wait()

        self.play(answer.animate.set_color(YELLOW))
        self.play(Indicate(answer))
        self.wait()

        task.set_z_index(srr_rect.z_index+1)

        texs = VGroup(
            tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9,
            line1, line2, line3, line4, line5,
            minus_sign1, minus_sign2, minus_sign3,
            bajanarar_bajaneli,
            answer
        )
        
        self.play(
            VGroup(srr_rect, task[:-1]).animate.scale(1/.75).set_opacity(1).to_edge(RIGHT),
            TransformFromCopy(answer, task[-1].set_opacity(1), path_arc=-PI/2),
            texs.animate.scale(.8).to_edge(LEFT)
        )

        self.wait(2)
