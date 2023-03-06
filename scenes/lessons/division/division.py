from manim import Scene, MathTex, SurroundingRectangle, Write, Create, Line, GrowFromEdge, Indicate, Wiggle, VGroup, TransformFromCopy, AnimationGroup, FadeOut, FadeIn
from manim import GREEN, RED, WHITE, YELLOW, BLACK
from manim import UP, LEFT, DOWN, RIGHT, UL
from manim import PI

FONT_SIZE = 85

class Division(Scene):
    """Այս վիդեոյի նպատակն է սյունակով բաժանում սովորեցնելը"""
    def construct(self):
        self.wait()

        task = MathTex("1728", ":", "12", "=", "144", font_size=1.3*FONT_SIZE)
        task[-1].set_color(YELLOW).set_opacity(0)
        task.to_edge(UP)
        srr_rect = SurroundingRectangle(task, color=GREEN, buff=.2, fill_color=BLACK)

        self.play(
            Write(task),
            Create(srr_rect)
        )
        self.wait()

        self.play(VGroup(task, srr_rect).animate.to_edge(RIGHT))
        bajanarar_bajaneli = task[:3].copy().scale(1/1.3).to_corner(UL).shift(RIGHT*.8)
        bajanarar_bajaneli[0].shift(LEFT*.15)
        self.play(
            TransformFromCopy(task[:3], bajanarar_bajaneli, path_arc=PI/2)
        )
        self.wait()

        line1 = Line(
            start=bajanarar_bajaneli[1].get_top(),
            end=bajanarar_bajaneli[1].get_bottom(),
            stroke_width=8
        ).set_length(2.5).align_to(bajanarar_bajaneli, UP)
        self.play(
            GrowFromEdge(line1, UP),
            FadeOut(bajanarar_bajaneli[1]),
            VGroup(srr_rect, task[:-1]).animate.scale(.75).set_opacity(.7)
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

        answer = MathTex(*"144", font_size=FONT_SIZE)
        answer.next_to(bajanarar_bajaneli[-1], DOWN, aligned_edge=LEFT, buff=.8)
        self.play(Write(answer[0]))
        self.wait()

        self.play(bajanarar_bajaneli[0][:2].animate.set_color(WHITE))
        self.wait()

        one_times_twelve = MathTex("1 \\cdot 12 = ", "12", font_size=1.2*FONT_SIZE)
        one_times_twelve.next_to(task, DOWN, buff=2.8)
        self.play(Write(one_times_twelve))
        self.wait()

        tex1 = one_times_twelve[-1].copy()
        self.play(tex1.animate(path_arc=-PI/2).scale(1/1.2).next_to(bajanarar_bajaneli[0], DOWN, aligned_edge=LEFT))
        minus_sign1 = MathTex("-", font_size=0.7*FONT_SIZE)
        minus_sign1.next_to(VGroup(bajanarar_bajaneli[0][:3], tex1), LEFT)
        self.play(Write(minus_sign1))
        self.wait()

        line3 = Line().set_length(tex1.width)
        line3.next_to(tex1, DOWN, aligned_edge=LEFT)
        self.play(GrowFromEdge(line3, LEFT))
        self.wait()

        tex2 = MathTex("5", font_size=FONT_SIZE, color=RED)
        tex2.next_to(line3, DOWN, aligned_edge=RIGHT)
        self.play(
            Write(tex2),
            FadeOut(one_times_twelve)
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

        for_times_twelve = MathTex("4 \\cdot 12 =", "48", font_size=1.2*FONT_SIZE)
        for_times_twelve.move_to(one_times_twelve, aligned_edge=LEFT)
        self.play(Write(for_times_twelve))
        self.wait()

        tex4 = for_times_twelve[-1].copy()
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

        tex5 = MathTex("4", font_size=FONT_SIZE, color=RED)
        tex5.next_to(line4, DOWN, aligned_edge=RIGHT)
        self.play(Write(tex5))
        self.wait()

        tex6 = bajanarar_bajaneli[0][-1].copy()
        self.play(
            tex6.animate.set_y(tex5.get_y()).set_color(GREEN),
            tex5.animate.set_color(GREEN)
        )
        self.wait()

        self.play(
            Wiggle(VGroup(tex5, tex6)),
            Wiggle(bajanarar_bajaneli[-1])
        )
        self.wait()

        self.play(Write(answer[-1]))
        self.wait()

        self.play(VGroup(tex5, tex6).animate.set_color(WHITE))
        self.wait()

        tex7 = for_times_twelve[-1].copy()
        self.play(Indicate(for_times_twelve))
        self.wait()
        self.play(
            AnimationGroup(
                tex7.animate(path_arc=-PI/2).scale(1/1.2).next_to(tex6, DOWN, aligned_edge=RIGHT),
                #line1.animate.set_length(7).align_to(bajanarar_bajaneli, UP),
                lag_ratio=.6
            )
        )
        minus_sign3 = minus_sign1.copy()
        minus_sign3.next_to(VGroup(tex5, tex6, tex7), LEFT)
        self.play(Write(minus_sign3))
        self.wait()

        line5 = Line().set_length(tex7.width)
        line5.next_to(tex7, DOWN, aligned_edge=RIGHT)
        self.play(
            GrowFromEdge(line5, LEFT),
            FadeOut(for_times_twelve)
        )
        self.wait()

        tex8 = MathTex("0", font_size=FONT_SIZE)
        tex8.next_to(line5, DOWN, aligned_edge=RIGHT)
        self.play(Write(tex8))
        self.wait()

        self.play(answer.animate.set_color(YELLOW))
        self.play(Indicate(answer))
        self.wait()

        task.set_z_index(srr_rect.z_index+1)
        
        self.play(
            VGroup(srr_rect, task[:-1]).animate.scale(1/.75).set_opacity(1),
            TransformFromCopy(answer, task[-1].set_opacity(1), path_arc=-PI/2)
        )

        self.wait(2)