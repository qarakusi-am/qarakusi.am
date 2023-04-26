from manim import Scene, MathTex, FadeIn, Write, SurroundingRectangle, VGroup, Create, AnimationGroup, Transform, Brace, GrowFromEdge, Indicate, FadeOut, TransformFromCopy, ReplacementTransform
from qarakusiscene import TaskNumberBox
from manim import UP, DOWN, LEFT, DL
from manim import ORANGE
from .text import taskNumberStr

FONT_SIZE = 100

class Problem12785(Scene):
    def construct(self):
        self.wait()

        MathTex.set_default(font_size=FONT_SIZE)

        taskNumber = TaskNumberBox(taskNumberStr)
        self.play(FadeIn(taskNumber))
        self.wait()

        task = MathTex("6! - 5! = 5 \\cdot 5!")
        srr_rect = SurroundingRectangle(task, ORANGE, buff=.25)
        VGroup(task, srr_rect).to_edge(UP)
        self.play(Write(task))
        self.wait()
        self.play(Create(srr_rect))
        self.wait()

        factorial = MathTex("n! = 1 \\cdot 2 \\cdot 3 \\cdot \\ \\ldots \\ \\cdot n")
        factorial.shift(DOWN*.6)
        self.play(
            AnimationGroup(
                *[Write(tex) for tex in factorial[0]],
                lag_ratio=1,
                run_time=5
            )
        )
        self.wait()

        n1 = factorial[0][0]
        n2 = factorial[0][-1]
        bazmaketer = factorial[0][-5:-2]

        self.play(
            Indicate(n1),
            Indicate(n2)
        )
        self.wait()

        self.play(
            Transform(n1, MathTex("6").move_to(n1, DOWN)),
            Transform(n2, MathTex("6").move_to(n2, DOWN)),
            Transform(bazmaketer, MathTex("4 \\cdot 5").move_to(bazmaketer, DOWN))
        )
        self.wait()

        brace = Brace(factorial[0][3:12], DOWN)
        brace_label = brace.get_tex("5!")
        self.play(GrowFromEdge(brace, LEFT))
        self.play(Write(brace_label))
        self.wait()

        factor = brace_label.copy()
        factor.move_to(factorial[0][3], DL)
        self.play(
            brace_label.animate.move_to(factorial[0][3], DL),
            FadeOut(brace, factorial[0][3:12]),
            factorial[0][12:].animate.next_to(factor, buff=.35)
        )
        self.wait()

        proof = MathTex("6!", "-", "5!", "=", "5!", "\\cdot", "6", "-", "5!")
        proof.next_to(task, DOWN, aligned_edge=LEFT, buff=.6)

        self.play(TransformFromCopy(task[0][:5], proof[:3]))
        self.wait()
        self.play(Write(proof[3]))
        self.wait()
        self.play(
            ReplacementTransform(VGroup(brace_label, factorial[0][-2:]), proof[4:7]),
            FadeOut(factorial[0][:3])
        )
        self.wait()
        self.play(Write(proof[7:]))
        self.wait()

        self.play(VGroup(proof[4], proof[8]).animate.set_color(ORANGE))
        self.wait()

        proof1 = MathTex("6!", "-", "5!", "=", "5!", "\\cdot", "6", "-", "5!", "\\cdot", "1")
        proof1.next_to(proof, DOWN, aligned_edge=LEFT, buff=.6)
        VGroup(proof1[4], proof1[8]).set_color(ORANGE)
        self.play(Write(proof1[3]))
        self.play(TransformFromCopy(proof[4:], proof1[4:-2]))
        self.play(Write(proof1[-2:]))
        self.wait()

        proof2 = MathTex("6!", "-", "5!", "=", "5!", "(", "6", "-", "1", ")")
        proof2.next_to(proof1, DOWN, aligned_edge=LEFT, buff=.6)
        proof2[4].set_color(ORANGE)
        self.play(Write(proof2[3]))
        self.play(TransformFromCopy(VGroup(proof1[4], proof1[8]), proof2[4]))
        self.play(Write(proof2[5]))
        self.wait()
        self.play(TransformFromCopy(proof1[6], proof2[6]))
        self.play(Write(proof2[7]))
        self.play(TransformFromCopy(proof1[-1], proof2[8]))
        self.play(Write(proof2[-1]))
        self.wait()

        proof3 = MathTex("6!", "-", "5!", "=", "5!", "\\cdot", "5")
        proof3.next_to(proof2, DOWN, aligned_edge=LEFT, buff=.45)
        self.play(Write(proof3[3]))
        self.play(TransformFromCopy(proof2[4], proof3[4]))
        self.play(Write(proof3[5]))
        self.play(TransformFromCopy(proof2[-5:], proof3[-1]))

        self.wait(2)
