from manim import *
from aramanim import *
UNIT = 2.1
name_tex_1 = "Փոքր թիվ"
name_tex_2 = "Մեծ թիվ"


class PartScene(Scene):
    def construct(self):
        line = Line(2*UP, 2*DOWN)
        segment_1 = Segment(ORIGIN, UNIT*LEFT, stroke_width = 6)
        segment_2 = Segment(ORIGIN, UNIT*22/7*LEFT, stroke_width = 6)
        participant_1 = VGroup(Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE)).shift(4.5*LEFT+3*UP)
        participant_2 = VGroup(
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*15/7*LEFT, "150", stroke_width = 6).set_color(GREEN)
        ).arrange(RIGHT, buff= 0)
        participant_2.next_to(participant_1, DOWN, buff=1.25, aligned_edge=LEFT)

        name_1 =  Tex(name_tex_1, font_size=0.7*DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(participant_1, LEFT)
        name_2 =  Tex(name_tex_2, font_size=0.7*DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(participant_2, LEFT)

        #self.play(Write(name_1))
        segment_1.align_to(participant_1, LEFT + UP)
        segment_2.align_to(participant_2, LEFT + UP)
        self.play(Create(segment_2))
        self.wait()
        self.play(Create(segment_1))
        self.wait()



        self.play(Create(participant_1), run_time=1.5)
        self.remove(segment_1)
        self.wait(2)
        #self.play(Write(name_2))
        self.play(ReplacementTransform(participant_1[0].copy(), participant_2[0]), run_time=1.5)
        self.play(Create(participant_2[1]), run_time=1.5)
        self.remove(segment_2)
        self.wait(0.5)
        self.play(Write(participant_2[1].update_label_pos()))
        self.wait(2)

        participant_2_interim = VGroup(
            Segment(ORIGIN, UNIT*(15+7)/7*LEFT, stroke_width = 6).set_color(WHITE)
        ).set_opacity(0.5)
        participant_2_interim.align_to(participant_2, LEFT+DOWN)
        self.play(
            FadeIn(participant_2_interim),
            participant_2.animate.shift(1.5*DOWN),
            participant_2[1].label.animate.shift(1.5*DOWN)
        )
        participant_2_alternativ = VGroup(
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*1/7*LEFT, "10", stroke_width = 6).set_color(WHITE)
        ).arrange(RIGHT, buff=0)
        participant_2_alternativ.align_to(participant_2_interim, LEFT+DOWN)
        self.wait(0.5)
        self.play(AnimationGroup(
            AnimationGroup(
                ReplacementTransform(participant_1[0].copy(), participant_2_alternativ[0]),
                ReplacementTransform(participant_1[0].copy(), participant_2_alternativ[1]),
                ReplacementTransform(participant_1[0].copy(), participant_2_alternativ[2]),
                lag_ratio=0.2
            ),
            FadeIn(participant_2_alternativ[3], participant_2_alternativ[3].update_label_pos()),
            lag_ratio=1
        ))
        self.remove(participant_2_interim)
        self.wait(2)
        participant_2_target=VGroup(
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*2*LEFT, "140", stroke_width = 6).set_color(GREEN),
            Segment(ORIGIN, UNIT*1/7*LEFT, "10", stroke_width = 6).set_color(WHITE)
        ).arrange(RIGHT, buff=0)
        participant_2_target.align_to(participant_2, LEFT+DOWN)
        s_1 = Scissors(participant_2_target[-1].get_left())
        s_2 = Scissors(participant_2_alternativ[-1].get_left())

        s_3 = Scissors(participant_2_target[0].get_right())
        s_4 = Scissors(participant_2_alternativ[0].get_right())
        self.play(
            AnimationGroup(
                CutIn(s_1), CutIn(s_2),
                lag_ratio=0.2
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                CutIn(s_3), CutIn(s_4),
                lag_ratio=0.2
            )
        )
        formula_0 = MathTex("150 - 10 = 140").next_to(participant_2_target, DOWN, aligned_edge=LEFT, buff=0.75)
        self.add(s_1, s_2, s_3, s_4)
        self.play(FadeOut(s_1, s_2, s_3, s_4))
        self.wait(1)
        self.play(
            ReplacementTransform(
                participant_2[1].update_label_pos(),
                VGroup(participant_2_target[1].update_label_pos(),
                participant_2_target[2].update_label_pos())
            ),
            #FadeOut(s_1, s_2, s_3, s_4),
            FadeOut(participant_2), FadeIn(participant_2_target),
            Write(formula_0),
            run_time = 2
        )
        self.wait()
        
        formula_1 = MathTex("140 : 2 = 70").next_to(formula_0, DOWN, aligned_edge=LEFT)
        self.play(
            participant_2_alternativ[1:3].animate.shift(0.25*DOWN),
            participant_2_target[1].animate.shift(0.25*DOWN),
            participant_2_target[1].label.animate.shift(0.25*DOWN),
        )
        self.wait(2)
        for mob in self.mobjects:
            mob.set_opacity(0.2)
        participant_2_alternativ[3].set_opacity(0.2)
        participant_2_alternativ[3].label.set_opacity(0.2)
        participant_2_alternativ[1].set_opacity(1)
        participant_2_alternativ[2].set_opacity(1)
        participant_2_target[1].set_opacity(1)
        participant_2_target[1].label.set_opacity(1)
        self.wait(2)
        self.play(AnimationGroup(
            participant_2_alternativ[1].animate(rate_func=rate_functions.there_and_back).shift(0.2*UP),
            participant_2_alternativ[2].animate(rate_func=rate_functions.there_and_back).shift(0.2*UP),
            lag_ratio=0.6
            
        ))
        self.play(
            *[mob.animate.set_opacity(1) for mob in self.mobjects],
            participant_2_alternativ[3].animate.set_opacity(1),
            participant_2_alternativ[3].label.animate.set_opacity(1)
        )
        self.wait()
        self.play(Write(formula_1))
        self.wait(2)
        participant_2 = VGroup(
            Segment(ORIGIN, UNIT*LEFT, "70", stroke_width = 6).set_color(ORANGE),
            Segment(ORIGIN, UNIT*15/7*LEFT, "150", stroke_width = 6).set_color(GREEN)
        ).arrange(RIGHT, buff= 0)
        participant_2.next_to(participant_1, DOWN, buff=1.25, aligned_edge=LEFT)

        self.play(
            Write(participant_1[0].update_label_pos()),
            FadeOut(
                participant_2_target,
                participant_2_alternativ,
                participant_2_target[1].label,
                participant_2_target[2].label,
                participant_2_alternativ[3].label,
            ),
            FadeIn(participant_2, participant_2[1].update_label_pos())
        )
        formula_2 = MathTex("70 + 150 = 220").next_to(formula_1, DOWN, aligned_edge=LEFT)
        self.play(Write(formula_2))
        participant_2_interim = VGroup(
            Segment(ORIGIN, UNIT*(15+7)/7*LEFT, "220", stroke_width = 6).set_color(GREEN)
        )
        participant_2_interim.align_to(participant_2, LEFT+DOWN)

        self.play(
            FadeOut(participant_2, participant_2[1].update_label_pos()),
            FadeIn(participant_2_interim, participant_2_interim[0].update_label_pos())
        )
        self.wait()
