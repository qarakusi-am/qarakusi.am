from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, GREEN, ORANGE, YELLOW, WHITE, RED, rate_functions
from manim import ValueTracker, VGroup,  Brace, DashedLine, SurroundingRectangle
from manim import Tex, MathTex
from manim import Create, FadeIn, FadeOut, Write, Flash, AnimationGroup, ReplacementTransform, ApplyWave, Indicate
from manim import always_redraw
from manim import Scene
from objects import Woman, Girl
from aramanim import Segment

from .text import ani_string, mayrik_string, one_year_after_string, now_string, another_one_year_after_string, two_years_after_string, after_some_years_string, some_years_string
UNIT = 0.27

class PartScene(Scene):
    def construct(self):
        self.set_up()
        self.time_pass()
        time = self.time
        daughter = self.daughter_svg
        mother = self.mother_svg
        daughter_segment = self.daughter_segment
        mother_segment = self.mother_segment
        daughter_label = self.daughter_label
        mother_label = self.mother_label


        x3_daughter_segment = self.x3_daughter_segment
        self.play(
            Create(daughter),
            FadeIn(
                Tex(ani_string).scale(0.5).next_to(daughter, DOWN),
                rate_func = rate_functions.there_and_back_with_pause
            )
        )
        self.wait(0.4)
        self.play(
            Create(mother),
            FadeIn(
                Tex(mayrik_string).scale(0.5).next_to(mother, DOWN),
                rate_func = rate_functions.there_and_back_with_pause
            )
        )
        self.wait(0.8)
        self.play(Create(daughter_segment))
        self.play(Write(daughter_label))

        self.wait(0.8)
        self.play(Create(mother_segment))
        self.play(Write(mother_label))
        self.wait(1.5)
        self.play(AnimationGroup(
            *[ReplacementTransform(daughter_segment.copy(), seg) for seg in x3_daughter_segment],
            lag_ratio = 0.25
        ))
        self.wait()
        brace = self.brace
        brace_label = self.brace_label
        self.play(FadeIn(brace))
        self.play(Write(brace_label))
        self.wait(1.5)
        main_group = always_redraw(lambda: self.time_pass())
        self.add(main_group)
        self.play(
            time.animate.set_value(1),
            Flash(daughter_segment.get_edge_center(RIGHT), run_time=0.7),
            Flash(mother_segment.get_edge_center(RIGHT), run_time=0.7),
            FadeIn(
                Tex(one_year_after_string).scale(1.5).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 2
        )
        self.wait(2.5)
        self.play(
            time.animate.set_value(2),
            Flash(daughter_segment.get_edge_center(RIGHT), run_time=0.7),
            Flash(mother_segment.get_edge_center(RIGHT), run_time=0.7),
            FadeIn(
                Tex(another_one_year_after_string).scale(1.5).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 2
        )
        self.wait(2.5)
        self.play(
            time.animate.set_value(0),
            FadeIn(
                Tex(now_string).scale(1.5).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 3
        )
        self.wait(0.5)
        fedout_box = always_redraw(
            lambda: SurroundingRectangle(VGroup(
                x3_daughter_segment,
                brace, brace_label
            ),color=BLACK, stroke_width = 0, fill_opacity = 0.7).set_z_index(10)
        )
        dash_line = always_redraw(
            lambda: DashedLine(
                mother_segment.get_right(),
                daughter_segment.line.get_projection(mother_segment.get_right()),
                stroke_width = 2
            )
        )
        diff_brece = self.diff_brece = always_redraw(lambda: Brace(VGroup(x3_daughter_segment[1], dash_line), UP, buff =0.15))
        self.play(
            FadeIn(fedout_box, diff_brece),
            Create(dash_line)
        )
        self.age_difference()
        self.wait()
        self.play(
            time.animate.set_value(1),
            Flash(daughter_segment.get_edge_center(RIGHT), run_time=0.7),
            Flash(mother_segment.get_edge_center(RIGHT), run_time=0.7),
            FadeIn(
                Tex(one_year_after_string).scale(1.5).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 1
        )
        self.age_difference()
        self.wait()
        self.play(
            time.animate.set_value(2),
            Flash(daughter_segment.get_edge_center(RIGHT), run_time=0.7),
            Flash(mother_segment.get_edge_center(RIGHT), run_time=0.7),
            FadeIn(
                Tex(two_years_after_string).scale(1.5).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 1
        )
        main_group.clear_updaters()
        fedout_box.clear_updaters()
        self.age_difference()
        self.wait(1.5)
        self.play(
            FadeOut(
                daughter_label,
                brace, brace_label,
                mother_label, fedout_box
                
            )
        )
        
        small_main_group = always_redraw(lambda: self.time_pass(False))
        self.add(small_main_group)
        self.wait(0.5)
        self.play(
            time.animate.set_value(5),
            FadeIn(
                Tex(after_some_years_string).scale(1.3).to_edge(DR).set_color(RED),
                rate_func = rate_functions.there_and_back_with_pause
            ),
            run_time = 7
        )
        small_main_group.clear_updaters()
        diff_brece.clear_updaters()
        dash_line.clear_updaters()
        self.wait()
        self.play(ApplyWave(VGroup(daughter_segment)))
        self.wait()
        self.play(ApplyWave(x3_daughter_segment))
        self.wait()
        diff_label = MathTex("24").next_to(diff_brece, UP)
        self.play(FadeIn(diff_label))
        self.wait()
        self.play(x3_daughter_segment[1:].animate(rate_func = rate_functions.wiggle).shift(0.15*UP))
        self.play(
            VGroup(diff_label, diff_brece).animate.next_to(x3_daughter_segment[1:], UP, buff = 0.1),
            FadeOut(dash_line)
        )
        x3_daughter_segment[1].set_label(MathTex(r"24:2"))
        x3_daughter_segment[2].set_label(MathTex(r"24:2"))
        self.wait()
        self.wait()
        l_12_1 = MathTex(r"12").move_to(x3_daughter_segment[1].update_label_pos().get_center())
        l_12_2 = MathTex(r"12").move_to(x3_daughter_segment[2].update_label_pos().get_center())
        self.play(
            FadeOut(diff_brece),
            ReplacementTransform(diff_label.copy(), l_12_1),
            ReplacementTransform(diff_label, l_12_2)
        )
        self.wait(0.5)
        self.play(Write(daughter_label))
        self.play(
            FadeOut(x3_daughter_segment, l_12_1, l_12_2),
            mother_segment.animate.align_to(x3_daughter_segment, UL)
        )
        formula = MathTex(r"3 \cdot 12 = 36").shift(2*DOWN)
        daughter_target = VGroup(
            self.get_part(7, "7", GREEN),
            self.get_part(5, "5", YELLOW),
        ).arrange(RIGHT, buff=0).align_to(daughter_segment, UL)

        mother_target = VGroup(
            self.get_part(31, "31", ORANGE),
            self.get_part(5, "5", YELLOW),
        ).arrange(RIGHT, buff=0).align_to(mother_segment, UL)

        formula_0 = MathTex(r"12 - 7 =", r"5").next_to(formula, DOWN, aligned_edge=LEFT)
        self.play(Write(mother_segment.update_label_pos()), Write(formula))
        self.wait(2)
        self.play(Write(formula_0))
        self.play(
            FadeIn(mother_target, daughter_target),
            FadeOut(mother_segment, daughter_segment),
            ReplacementTransform(daughter_label.copy(), daughter_target[1].update_label_pos()),
            ReplacementTransform(daughter_label, daughter_target[0].update_label_pos()),
            ReplacementTransform(mother_label.copy(), mother_target[1].update_label_pos()),
            ReplacementTransform(mother_label, mother_target[0].update_label_pos()),
            Indicate(formula_0[1], 1.1),
            Write(Tex(some_years_string).next_to(formula_0[1], RIGHT).set_color(RED))
        )
        self.wait(3)




    
    def set_up(self, add = False):
        self.time = ValueTracker(0)
        daughter = self.daughter_svg = Girl(4)
        daughter.scale(1.4)
        mother = self.mother_svg = Woman(1)
        mother.scale(1.9)

        mother_pos = self.mother_pos = [-5.5, -1, 0]
        daughter_pos = self.daughter_pos = [-5.5, 2.5, 0]
        mother.move_to(mother_pos)
        daughter.move_to(daughter_pos)

        daughter_segment = self.daughter_segment = self.get_part(7, "7", GREEN)
        daughter_segment.next_to(daughter_pos, RIGHT, buff=1)
        mother_segment = self.mother_segment = self.get_part(31, "31", ORANGE)
        mother_segment.next_to(mother_pos, RIGHT, buff=1).shift(0.75*DOWN)
        mother_label = self.mother_label = mother_segment.update_label_pos()
        daughter_label = self.daughter_label = daughter_segment.update_label_pos()

        x3_daughter_segment = self.x3_daughter_segment = VGroup(
            daughter_segment.copy(),
            daughter_segment.copy(),
            daughter_segment.copy()
        ).arrange(RIGHT, buff=0).next_to(mother_segment, UP, aligned_edge=LEFT, buff=1)

        brace = self.brace = Brace(x3_daughter_segment, UP)
        brace_label = self.brace_label = MathTex(r"3 \cdot 7 = 21").next_to(brace, UP)
        main_group = self.main_group = VGroup(
            daughter_segment, daughter_label,
            mother_segment, mother_label,
            brace, brace_label
        )
        if add:
            self.add(main_group)

        
    def get_part(self, value, label = None, color = WHITE):
        seg = Segment(
            ORIGIN,
            UNIT * value * RIGHT,
            label,
            stroke_width = 6,
            color = color
        )
        return seg

    def time_pass(self, all = True):
        time = self.time.get_value()
        
        daughter_segment = self.daughter_segment
        daughter_label = self.daughter_label
        mother_segment = self.mother_segment
        
        mother_label = self.mother_label

        x3_daughter_segment = self.x3_daughter_segment
        
        daughter_segment.become(self.get_part(
            7+time,
            r"{:,}".format(int(time+7.5)),
            color =GREEN
        ).align_to(daughter_segment, LEFT+UP))
        daughter_segment.set_label(MathTex(r"{:,}".format(int(time+7.5))))
        daughter_label.become(daughter_segment.update_label_pos())
        
        mother_segment.become(self.get_part(
            31+time,
            r"{:,}".format(int(time+31.5)),
            color =ORANGE
        ).align_to(mother_segment, LEFT+UP))
        mother_segment.set_label(MathTex(r"{:,}".format(int(time+31.5))))
        mother_label.become(mother_segment.update_label_pos())

        x3_daughter_segment.become(VGroup(
            daughter_segment.copy(),
            daughter_segment.copy(),
            daughter_segment.copy()
        ).arrange(RIGHT, buff=0).next_to(mother_segment, UP, aligned_edge=LEFT, buff=1))

        brace = self.brace 
        brace_label = self.brace_label

        brace.become(Brace(x3_daughter_segment, UP))
        brace_label.become(MathTex(r"3 \cdot", r"{:,}".format(int(time+7.5)), r"=", r"{:,}".format(3*int(time+7.5))).next_to(brace, UP))

        
        if all:
            return VGroup(
                daughter_segment, daughter_label,
                mother_segment, mother_label,
                brace, brace_label
            )
        else:
            return VGroup(
                daughter_segment,
                mother_segment,
            )

    def age_difference(self):
        daughter_label = self.daughter_label
        mother_label = self.mother_label
        diff_brece = self.diff_brece
        sign = MathTex(r"-", r"=", r"24")
        formula = VGroup(
            mother_label.copy(),
            sign[0],
            daughter_label.copy(),
            sign[1], sign[2],
        ).arrange(RIGHT, buff=0.15).next_to(diff_brece, UP)

        self.play(AnimationGroup(
            ReplacementTransform(mother_label.copy(), formula[0]),
            Write(formula[1]),
            ReplacementTransform(daughter_label.copy(), formula[2]),
            Write(formula[3]), Write(formula[4]), lag_ratio=0.8
        ), run_time = 1.7)
        self.play(Indicate(formula[4], 1.1), run_time = 0.8)
        self.play(FadeOut(formula), run_time = 0.5)



