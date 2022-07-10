
from manim import *
from aramanim import *

DM = 0.4
M = 10 * DM
DECIMETER_LABEL = Tex(r'$1$դմ', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
METER_LABEL = Tex(r'$1$մ', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
DECIMETER = Segment(DM*LEFT, DM*RIGHT)
METER = Segment(M*LEFT, M*RIGHT)


class DecimeterMeters(Scene):
    def construct(self):
        formula_0 = Tex(r'$1$մ', r'=', r'$10$դմ', font_size=2 * DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        self.play(Write(formula_0), run_time = 2)
        self.play(AnimationGroup(
            formula_0[0].animate.set_color(ORANGE),
            formula_0[2].animate.set_color(GREEN),
            lag_ratio = 0.3
        ), run_time = 1.5)
        self.wait()
        
        participant_1 = VGroup(METER.copy())
        participant_2 = VGroup(*[DECIMETER.copy() for _ in range(10)])
        participant_2.arrange(RIGHT, buff = 0)
        diagram = VGroup(participant_1, participant_2)
        diagram.arrange(DOWN, buff = 1.5).shift(2.85*LEFT)

        self.play(AnimationGroup(
            formula_0.animate.next_to(diagram, buff = 2),
            FadeIn(diagram, lag_ratio = 0.1),
            lag_ratio = 0.4
        ))

        self.wait()  

        self.play(
            participant_1.animate.set_color(ORANGE),
            participant_2.animate.set_color(GREEN),
            formula_0[0].animate.next_to(participant_1, UP, buff = 0.1).scale(0.5),
            formula_0[2].animate.next_to(participant_2, UP, buff = 0.1).scale(0.5),
            FadeOut(formula_0[1], rate_func = lambda t: (rate_functions.lingering(t))**(1/2))
        )

        self.wait()  
        self.play(
            participant_2.animate.align_to(participant_1, UP + LEFT),
            formula_0[2].animate.next_to(participant_1, UP, buff = 0.1),
            FadeOut(formula_0[0])
        )
        self.remove(participant_1)
        participant_1 = participant_2
        participant_2 = VGroup(participant_1[0].copy())
        self.wait()  
        self.play(
            participant_2.animate.shift(DOWN)
        )
        participant_2[0].set_label(DECIMETER_LABEL.copy().match_height(formula_0[2]))
        self.wait()
        self.play(Write(participant_2[0].label.set_color(GREEN)))

                

        participant_1_target = VGroup(*[Segment(1.3*DM*LEFT, 1.5*DM*RIGHT) for _ in range(10)])
        participant_1_target.arrange(RIGHT, buff = 0)
        participant_1_target.align_to(participant_1, LEFT + DOWN)
        participant_2_target = VGroup(participant_1_target[0].copy())
        participant_2_target.align_to(participant_2, LEFT + DOWN)


        self.wait()
        self.play(
            ReplacementTransform(participant_1, participant_1_target),
            ReplacementTransform(participant_2, participant_2_target),
            FadeOut(
                participant_2[0].label,
                formula_0[2],
                rate_func = lambda t: (rate_functions.lingering(t))**(1/5)
            ),
            run_time = 2.5
        )
        diagram = VGroup(participant_1_target, participant_2_target)
        self.wait()
        total_brace = Brace(diagram, RIGHT)
        total_brace.label = Tex(r'$33$', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        total_brace.add(total_brace.label.next_to(total_brace, RIGHT))
        diagram.add(total_brace)
        self.play(Write(total_brace))
        self.play(diagram.animate.shift(1.5*UP))
        self.play(
            AnimationGroup(
                *[s.animate(rate_func = rate_functions.there_and_back_with_pause).shift(0.2 * UP) for s in participant_1_target + participant_2_target],
                lag_ratio = 0.7
            )
        )
        formula_1 = Tex(r'$33 : 11 = 3$', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        formula_2 = Tex(r'$3 \cdot 10 = 30$', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        formula_2.next_to(formula_1, DOWN, aligned_edge=LEFT)
        self.wait()
        self.play(Write(formula_1))
        self.play(Write(formula_2))
        self.wait(2)

        