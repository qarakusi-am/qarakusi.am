from manim import Write, GrowFromEdge, Tex, Transform, GrowFromCenter, Brace
from manim import YELLOW, ORANGE, RED, WHITE
from lib.aramanim import *
from lib.qarakusiscene import TaskNumberBox
from objects import DScissors, Checkmark
from .text import *

class Problem10384(Scene):
    def construct(self):
        self.wait()
        self.set_up()
        self.play(FadeIn(self.task_number))
        self.wait()
        self.play(Write(self.condition1), run_time=5)
        self.wait()
        self.play(Write(self.condition2), run_time=5)
        self.wait(1)
        self.play(
            VGroup(self.condition1, self.condition2).animate.scale(.8).to_edge(DOWN+LEFT)
        )
        self.wait()
        self.play(Write(self.first_rope_label))
        self.play(GrowFromEdge(self.first_rope, LEFT))
        self.play(Write(self.second_rope_label))
        self.play(GrowFromEdge(self.second_rope, LEFT))
        self.play(
            CutIn(self.scissors1),
            CutIn(self.scissors2)
        )
        self.first_rope.become(self.get_part(2.5, color=YELLOW).align_to(self.first_rope, LEFT+UP))
        self.part2_of_first_rope.next_to(self.first_rope, buff=0)
        self.add(self.part2_of_first_rope)
        part2_of_first_rope_label = Tex(part2_of_first_rope_string, font_size=40)
        part2_of_first_rope_label.add_updater(
            lambda x: x.next_to(self.part2_of_first_rope, UP)
        )
        self.second_rope.become(self.get_part(5).align_to(self.second_rope, LEFT+UP))
        self.part2_of_second_rope.next_to(self.second_rope, buff=0)
        self.add(self.part2_of_second_rope)
        part2_of_second_rope_label = Tex(part2_of_first_rope_string, font_size=40)
        part2_of_second_rope_label.add_updater(
            lambda x: x.next_to(self.part2_of_second_rope, UP)
        )
        self.play(
            FadeIn(part2_of_second_rope_label),
            FadeIn(part2_of_first_rope_label)
        )
        self.play(
            CutOut(self.scissors1),
            CutOut(self.scissors2)
        )
        self.play(
            self.part2_of_second_rope.animate.shift(RIGHT*3),
            self.part2_of_first_rope.animate.shift(RIGHT*3)
        )
        self.wait()
        self.play(Transform(self.first_rope, self.get_part(2, color=YELLOW).align_to(self.first_rope, LEFT+UP), run_time=1))
        self.play(Transform(self.second_rope, self.get_part(6).align_to(self.second_rope, LEFT+UP), run_time=1))
        self.wait()
        x3_segments = [*[self.first_rope.copy() for x in range(3)]]
        self.play(x3_segments[0].animate.align_to(self.second_rope, LEFT+UP))
        self.play(x3_segments[1].animate.next_to(x3_segments[0], buff=0))
        self.play(x3_segments[2].animate.next_to(x3_segments[1], buff=0))
        self.wait()
        checkmark1 = Checkmark().scale(.3).next_to(self.condition2)
        self.play(
            FadeIn(checkmark1),
            FadeOut(self.second_rope)
        )
        self.wait()
        self.play(
            self.part2_of_first_rope.animate.next_to(self.first_rope, buff=0),
            self.part2_of_second_rope.animate.next_to(self.second_rope, buff=0)
        )
        self.play(
            GrowFromCenter(self.brace1),
            Write(self.brace1_label)
        )
        self.wait()
        checkmark2 = Checkmark().scale(.3).next_to(self.condition1)
        self.play(FadeIn(checkmark2))
        self.wait()
        self.play(FadeOut(self.condition1, self.condition2, checkmark1, checkmark2))
        self.wait()
        self.play(
            CutIn(self.scissors3),
            CutIn(self.scissors4)
        )
        self.part2_of_first_rope.left_edge.clear_updaters()
        self.part2_of_first_rope.right_edge.clear_updaters()
        self.part2_of_second_rope.left_edge.clear_updaters()
        self.part2_of_second_rope.right_edge.clear_updaters()
        self.play(
            CutOut(self.scissors3),
            CutOut(self.scissors4)
        )
        self.play(
            self.part2_of_first_rope.animate.shift(RIGHT*.5).set_opacity(.5),
            part2_of_first_rope_label.animate.set_opacity(.3),
            self.part2_of_second_rope.animate.shift(RIGHT*.5).set_opacity(.3),
            part2_of_second_rope_label.animate.set_opacity(.3)
        )
        self.play(self.first_rope.animate.shift(UP*.3).scale(1.1))
        self.play(self.first_rope.animate.shift(DOWN*.3).scale(.9))
        self.wait(0.1)
        self.play(x3_segments[0].animate.shift(UP*.3).scale(1.1))
        self.play(x3_segments[0].animate.shift(DOWN*.3).scale(.9))
        self.wait(0.1)
        self.play(x3_segments[1].animate.shift(UP*.3).scale(1.1))
        self.play(x3_segments[1].animate.shift(DOWN*.3).scale(.9))
        self.wait(0.1)
        self.play(x3_segments[2].animate.shift(UP*.3).scale(1.1))
        self.play(x3_segments[2].animate.shift(DOWN*.3).scale(.9))
        self.wait(0.1)
        self.play(Write(self.value_of_4_part_label), run_time=4)
        self.wait()
        self.play(Write(self.value_of_1_part_label), run_time=4)
        self.wait()
        x4_value_of_1_part = [
            Tex("$90$", font_size=50).scale(.9).next_to(self.first_rope, UP),
            *[Tex("$90$", font_size=50).scale(.9).next_to(x, UP) for x in x3_segments]
        ]
        self.play(*[Write(x) for x in x4_value_of_1_part], run_time=3)
        self.wait()
        self.play(
            self.part2_of_first_rope.animate.next_to(self.first_rope, buff=0).set_opacity(1),
            part2_of_first_rope_label.animate.set_opacity(1),
            self.part2_of_second_rope.animate.next_to(self.second_rope, buff=0).set_opacity(1),
            part2_of_second_rope_label.animate.set_opacity(1),
        )
        brace2 = Brace(VGroup(self.first_rope, self.part2_of_first_rope), DOWN)
        brace2_label1 = brace2.get_tex(brace2_string1).scale(.9)
        brace2_label2 = brace2.get_tex(brace2_string2).scale(.9)
        brace3 = Brace(VGroup(self.second_rope), DOWN)
        brace3_label1 = brace3.get_tex(brace3_string1).scale(.9)
        brace3_new = Brace(VGroup(self.second_rope, self.part2_of_second_rope), DOWN)
        brace3_label2 = brace3_new.get_tex(brace3_string2).scale(.9)
        brace3_label3 = brace3_new.get_tex(brace3_string3).scale(.9)
        self.play(
            GrowFromCenter(brace2),
            Write(brace2_label1),
            run_time=4
        )
        self.wait()
        self.play(
            GrowFromCenter(brace3),
            Write(brace3_label1),
            run_time=4
        )
        self.wait()
        self.play(brace3_label1.animate.next_to(self.value_of_4_part_label, buff=1.5).scale(1.15))
        self.play(
            Write(brace3_label2),
            brace3.animate.become(brace3_new),
            run_time=4
        )
        self.wait(1)
        self.play(Transform(brace2_label1, brace2_label2))
        self.play(Transform(brace3_label2, brace3_label3))
        self.wait(2)
        self.play(FadeOut(self.value_of_1_part_label, self.value_of_4_part_label, brace3_label1))
        self.wait()
        first_rope_length_copy = MathTex(brace2_string2).scale(.9).align_to(brace2_label2, LEFT+UP)
        second_rope_length_copy = MathTex(string4).scale(.9).align_to(brace3_label3, LEFT+UP)
        self.add(first_rope_length_copy, second_rope_length_copy)
        self.play(
            first_rope_length_copy.animate.to_edge(LEFT).to_edge(DOWN, buff=2.2),
            second_rope_length_copy.animate.become(MathTex(string1).scale(.9).align_to(brace3_label3, LEFT+UP)).to_edge(LEFT, buff=1.5).to_edge(DOWN, buff=2.2),
            run_time=2
        )
        self.wait()
        self.play(
            CutIn(self.scissors5),
            CutIn(self.scissors6),
            rum_time=2
        )
        self.play(
            CutOut(self.scissors5),
            CutOut(self.scissors6),
            rum_time=2
        )
        self.play(
            self.part2_of_first_rope.animate.shift(RIGHT*.4).set_opacity(.5),
            brace2.animate.become(Brace(self.first_rope, DOWN)),
            FadeOut(brace2_label1),
            self.part2_of_second_rope.animate.shift(RIGHT*.4).set_opacity(.5),
            brace3.animate.become(Brace(VGroup(*[x3_segments[x] for x in range(3)]), DOWN)),
            FadeOut(brace3_label2),
            run_time=3
        )
        self.wait()
        brace2_label3 = brace2.get_tex(string2).scale(.9)
        self.play(Write(brace2_label3))
        self.wait()
        brace3_label4 = brace3.get_tex(string3).scale(.9)
        self.play(Write(brace3_label4))
        self.wait()
        brace2_label3_copy = brace2.get_tex(string5).scale(.9).align_to(brace2_label3, RIGHT+UP).shift(LEFT*.3)
        brace3_label4_copy = brace3.get_tex(string6).scale(.9).align_to(brace3_label4, RIGHT+UP).shift(LEFT*.3)
        brace2_label3_copy_new = brace3.get_tex(string7).scale(.9).to_edge(LEFT).to_edge(DOWN, buff=1.6)
        self.play(
            brace2_label3_copy.animate.become(brace2_label3_copy_new),
            brace3_label4_copy.animate.next_to(brace2_label3_copy_new),
            run_time=1.5
        )
        self.wait(2)
    
    def set_up(self):
        self.task_number = TaskNumberBox(task_number_string)
        self.condition1 = Tex(condition1_string).scale(.9*.9).shift(UP)
        self.condition1[0][:8].set_color(ORANGE)
        self.condition2 = Tex(condition2_string).scale(.9*.9)
        self.condition2.next_to(self.condition1, DOWN, buff=1)
        self.condition2[0][:8].set_color(ORANGE)
        self.first_rope_label = Tex(first_rope_string, font_size=50).set_color_by_gradient("#FF9673", "#E0B851").scale(.8)
        self.second_rope_label = Tex(second_rope_string, font_size=50).set_color_by_gradient("#CFC748", "#7FC381").scale(.8)
        self.first_rope_label.to_edge(LEFT).to_edge(UP, buff=1.5)
        self.second_rope_label.next_to(self.first_rope_label, DOWN, buff=1.8).align_to(self.first_rope_label, RIGHT)
        self.first_rope = self.get_part(3.4)
        self.second_rope = self.get_part(5.9)
        self.first_rope.to_edge(LEFT).to_edge(UP, buff=1.6).shift(RIGHT*2.25)
        self.second_rope.next_to(self.second_rope_label, buff=.4).align_to(self.first_rope, LEFT)
        self.part2_of_first_rope = self.get_part(.9, color=RED)
        self.part2_of_second_rope = self.get_part(.9, color=RED)
        self.scissors1 = DScissors(cut_point=LEFT*1.88+UP*2.38)
        self.scissors2 = DScissors(cut_point=RIGHT*.63+UP*.2)
        self.brace1 = Brace(VGroup(self.first_rope, self.second_rope), RIGHT, buff=1.5).shift(RIGHT*.5)
        self.brace1_label = self.brace1.get_tex(brace1_string)
        self.scissors3 = DScissors(cut_point=LEFT*2.38+UP*2.4)
        self.scissors4 = DScissors(cut_point=RIGHT*1.63+UP*.2)
        self.scissors5 = DScissors(cut_point=LEFT*2.38+UP*2.4)
        self.scissors6 = DScissors(cut_point=RIGHT*1.63+UP*.2)
        self.value_of_4_part_label = MathTex(value_of_4_part_string).to_edge(DOWN, buff=2).to_edge(LEFT)
        self.value_of_1_part_label = Tex(value_of_1_part_string).next_to(self.value_of_4_part_label, DOWN, buff=.4).align_to(self.value_of_4_part_label, LEFT)
    
    def get_part(self, value, label = None, color = WHITE):
        seg = Segment(
            ORIGIN,
            value * RIGHT,
            label,
            stroke_width = 6,
            color = color
        )
        return seg
