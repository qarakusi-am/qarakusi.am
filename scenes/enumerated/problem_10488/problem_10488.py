from manim import Scene
from manim import ORIGIN, RIGHT, LEFT, UP, DOWN, rate_functions
from manim import YELLOW, GREEN, RED, BLUE
from manim import (
    Wait, AnimationGroup, Create, Write,
    ReplacementTransform, TransformMatchingShapes,
    FadeIn, FadeOut, Indicate, Wiggle)
from manim import VGroup, MathTex, Tex, Brace
from aramanim import Segment, CutIn, CutOut
from objects import SimpleSVGMobject, Checkmark, DScissors
from .text import (
        condition_1_string,
        condition_2_string,
        three_times_more_list,
        in_total_list)

class Problem10488(Scene):
    def construct(self):
        self.set_up()
        figure_1 = self.figure_1
        figure_2 = self.figure_2
        segment_1 = self.segment_1
        segment_2 = self.segment_2
        cond_1 = self.cond_1
        cond_2 = self.cond_2
        checkmark_1 = self.checkmark_1
        checkmark_2 = self.checkmark_2
        scissors_1 = self.scissors_1
        scissors_2 = self.scissors_2
        small_pool = self.small_pool
        big_pool = self.big_pool
        brace = self.brace
        count = self.count
        formula_total_units = self.formula_total_units
        formula_one_units = self.formula_one_units
        formula_total_1 = self.formula_total_1
        formula_total_2 = self.formula_total_2
        self.wait()
        self.play(
            AnimationGroup(
                Create(small_pool),
                Create(big_pool),
                lag_ratio = 0.8))
        self.wait()
        self.play(Write(cond_1), run_time = 8)
        self.wait()
        self.play(Write(cond_2), run_time = 8)
        self.wait()
        self.play(Create(figure_1[0]))
        self.wait()
        self.play(
            AnimationGroup(
                *[ReplacementTransform(figure_1[0].copy(), figure_2[i]) for i in range(3)],
                lag_ratio=0.25), run_time = 1.5)
        self.wait()
        self.play(Indicate(checkmark_1, color=GREEN))
        self.wait()
        self.play(Create(figure_1[-1]), Write(figure_1[-1].update_label_pos()))
        self.wait()
        self.play(Create(figure_2[-1]), Write(figure_2[-1].update_label_pos()))
        self.wait()
        self.play(Write(brace))
        self.wait()
        self.play(Indicate(checkmark_2, color=GREEN))
        self.wait()
        self.play(FadeOut(
            cond_1,
            checkmark_1,
            cond_2,
            checkmark_2))
        self.wait()
        self.play(Wiggle(figure_1[0]))
        self.wait()
        self.play(
            AnimationGroup(                
                Wiggle(figure_1[0]),
                *[Wiggle(figure_2[i]) for i in range(3)],
                lag_ratio=0.5), run_time = 4)
        self.wait()
        self.play(
            AnimationGroup(
                CutIn(scissors_1),
                CutIn(scissors_2),
                lag_ratio=0.5))
        self.add(scissors_1, scissors_2)
        self.wait(0.2)
        self.play(
            AnimationGroup(
                CutOut(scissors_1),
                CutOut(scissors_2),
                lag_ratio=0.5),
            AnimationGroup(
                figure_1[-1].animate.next_to(brace, LEFT).align_to(figure_1[0], UP),
                figure_2[-1].animate.next_to(brace, LEFT).align_to(figure_2[0], UP),
                lag_ratio=0.5), run_time = 2)
        self.remove(scissors_1, scissors_2)
        self.wait()
        self.play(
            AnimationGroup(
                TransformMatchingShapes(brace[1].copy(), formula_total_units[0]),
                Write(formula_total_units[1]),
                TransformMatchingShapes(figure_1[-1].label.copy(), formula_total_units[2]),
                Write(formula_total_units[3]),
                TransformMatchingShapes(figure_2[-1].label.copy(), formula_total_units[4]),
                Write(formula_total_units[5:]),
                lag_ratio=0.75), run_time = 8)
        self.wait()
        self.play(
            AnimationGroup(
                AnimationGroup(
                    figure_1[0].animate(rate_func = rate_functions.there_and_back_with_pause).shift(0.5*UP),
                    count[0].animate(rate_func = rate_functions.there_and_back_with_pause).set_opacity(1)),
                *[
                    AnimationGroup(
                        figure_2[i].animate(rate_func = rate_functions.there_and_back_with_pause).shift(0.5*UP),
                        count[i+1].animate(rate_func = rate_functions.there_and_back_with_pause).set_opacity(1))
                        for i in range(3)],
                lag_ratio=0.5), run_time = 4)
        self.remove(count)
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(formula_total_units[-1].copy(), formula_one_units[0]),
                Wait(),
                Write(formula_one_units[1:], run_time = 3),
                lag_ratio=0.75))
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(figure_1[0].update_label_pos()),
                *[FadeIn(figure_2[i].update_label_pos()) for i in range(3)],
                lag_ratio=0.25))
        self.wait()
        self.play(
            VGroup(formula_one_units, formula_total_units).animate.shift(4*LEFT),
            figure_1[-1].animate.next_to(figure_1[:-1], RIGHT, buff=0),
            figure_2[-1].animate.next_to(figure_2[:-1], RIGHT, buff=0))
        self.wait()
        self.play(
            AnimationGroup(
                Write(formula_total_1[0]),
                Wiggle(figure_1[0]), lag_ratio=0.75))
        self.play(
            AnimationGroup(
                Write(formula_total_1[1]),
                TransformMatchingShapes(figure_1[1].label.copy(), formula_total_1[2]),
                Wait(),
                Write(formula_total_1[3:]),
                lag_ratio=0.75))
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(segment_1),
                FadeOut(figure_1),
                ReplacementTransform(VGroup(*[s.label for s in figure_1]), segment_1.update_label_pos()),
                lag_ratio=0.75))
        self.wait()
        self.play(
            AnimationGroup(
                TransformMatchingShapes(brace[1].copy(), formula_total_2[0]),
                Write(formula_total_2[1]),
                TransformMatchingShapes(segment_1.label.copy(), formula_total_2[2]),
                Wait(),
                Write(formula_total_2[3:]),
                lag_ratio=0.75))
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(segment_2),
                FadeOut(figure_2),
                ReplacementTransform(VGroup(*[s.label for s in figure_2]), segment_2.update_label_pos()),
                lag_ratio=0.75))
        self.wait(2)

    def set_up(self):
        #segments set up
        figure_1 = VGroup(*[self.get_segment(), self.get_segment(60, BLUE)])
        figure_2 = VGroup(
            *[self.get_segment() for _ in range(3)],
            self.get_segment(40, BLUE))
        figure_1.arrange(RIGHT, buff=0)
        figure_1.align_to(3*UP + 2.5*LEFT, UP + LEFT)
        figure_2.arrange(RIGHT, buff=0)
        figure_2.next_to(figure_1, DOWN, buff=2.5, aligned_edge=LEFT)
        segment_1 = self.get_segment(185, BLUE).align_to(figure_1, UP + LEFT)
        segment_2 = self.get_segment(415, BLUE).align_to(figure_2, UP + LEFT)
        segment_1.add_label_updater()
        segment_2.add_label_updater()
        #text set up
        condition_1 = Tex(condition_1_string).set_color(RED).scale(1.2)
        condition_2 = Tex(condition_2_string).set_color(BLUE).scale(1.2)
        condition_1_content = Tex(*three_times_more_list)
        condition_2_content = Tex(*in_total_list)
        condition_1_content.arrange(DOWN, aligned_edge=LEFT)
        condition_2_content.arrange(DOWN, aligned_edge=LEFT)
        condition_1.next_to(condition_1_content, UP, aligned_edge=LEFT)
        condition_2.next_to(condition_2_content, UP, aligned_edge=LEFT)
        cond_1 = VGroup(condition_1, condition_1_content).scale(0.7)
        cond_2 = VGroup(condition_2, condition_2_content).scale(0.7)
        VGroup(cond_1, cond_2).arrange(RIGHT, buff=3, aligned_edge=UP).to_corner(DOWN)
        #checkmaek set up
        checkmark_1 = Checkmark().scale(0.2)
        checkmark_2 = Checkmark().scale(0.2)
        checkmark_1.next_to(condition_1, RIGHT)
        checkmark_2.next_to(condition_2, RIGHT)
        #scissors set up
        scissors_1 = DScissors(figure_1[:-1].get_right())
        scissors_2 = DScissors(figure_2[:-1].get_right())
        #pool SVG set up
        small_pool = SimpleSVGMobject('small_pool')
        big_pool = SimpleSVGMobject('big_pool')
        small_pool.scale(0.5)
        small_pool.next_to(figure_1, LEFT)
        big_pool.scale(0.6)
        big_pool.next_to(figure_2, LEFT)
        small_pool.match_x(big_pool)
        #brace set up
        brace = Brace(VGroup(figure_1, figure_2), RIGHT, buff=0.8).set_stroke(width=2.5)
        total = MathTex("600").next_to(brace, RIGHT)
        brace.add(total)
        #count set up
        count = VGroup(*[MathTex("{:,}".format(i)) for i in range(1, 5)])
        count[0].move_to(figure_1[0]).set_color(YELLOW).scale(0.9)
        for i in range(1, 4):
            count[i].move_to(figure_2[i-1]).set_color(YELLOW).scale(0.9)
        count.set_opacity(0)
        #formula set up
        formula_total_units = MathTex(r"600", r"-", r"60", r"-", r"40", r"=", r"500")
        formula_one_units = MathTex(r"500", r":", r"4", r"=", r"125")
        VGroup(formula_total_units, formula_one_units).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(2.5*DOWN)
        formula_total_1 = MathTex(r"125", r"+", r"60", r"=", r"185")
        formula_total_2 = MathTex(r"600", r"-", r"185", r"=", r"415") 
        VGroup(formula_total_1, formula_total_2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(2.5*DOWN + 4*RIGHT)
        #self.
        self.figure_1 = figure_1
        self.figure_2 = figure_2
        self.segment_1 = segment_1
        self.segment_2 = segment_2
        self.cond_1 = cond_1
        self.cond_2 = cond_2
        self.checkmark_1 = checkmark_1
        self.checkmark_2 = checkmark_2
        self.scissors_1 = scissors_1
        self.scissors_2 = scissors_2
        self.small_pool = small_pool
        self.big_pool = big_pool
        self.brace = brace
        self.count = count
        self.formula_total_units = formula_total_units
        self.formula_one_units = formula_one_units
        self.formula_total_1 = formula_total_1
        self.formula_total_2 = formula_total_2

    def get_segment(self, value = 125, color = RED):
        s = Segment(ORIGIN, (value/56)*RIGHT, label = "{:,}".format(value), color=color, stroke_width = 8)
        s.add_label_updater()
        return s 
