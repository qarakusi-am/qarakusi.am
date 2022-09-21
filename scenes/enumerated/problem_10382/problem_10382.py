from aramanim import Segment
from manim import WHITE, GREEN, RED, BLACK
from manim import ORIGIN, RIGHT, LEFT, UP, DOWN
from manim import Tex, MathTex,DashedLine, SurroundingRectangle, VGroup, Brace
from manim import Write, Create, FadeIn, FadeOut, TransformMatchingShapes, Indicate, ReplacementTransform
from manim import Scene
from .text import arshak_str, levon_str, toy_str, missing_str
from objects import SimpleSVGMobject

UNIT = 1/50
POSITION = [-4.5, 2.25, 0]
RUN_TIME = 2
WAIT_TIME = 1.5
NAME_SEGMENT_BUFF = 0.5
SEGMENT_SEGMENT_BUFF = 1.75

class Problem10382(Scene):
    def construct(self):
        toy_price = 440
        arshaks_money = 140
        levons_money = 240
        coins = VGroup(*[SimpleSVGMobject('20dram').copy() for _ in range(5)])
        coins.arrange(RIGHT)
        missing_tex = Tex(missing_str).scale(0.7)
        prob_number = MathTex(r'\#10382').to_corner(LEFT+UP)
        #toy (start)
        toy_seg_0 = self.get_part(
            toy_price,
            label="{:,}".format(toy_price),
            color=GREEN
        )
        toy_seg_0.add_label_updater()
        toy_seg_1 = self.get_part(
            toy_price,
            label="{:,}".format(toy_price),
            color=GREEN
        )
        toy_seg_1.add_label_updater()
        toy_seg_2 = self.get_part(
            toy_price,
            label="{:,}".format(toy_price),
            color=GREEN
        )
        toy_seg_2.add_label_updater()
        toy_tex = Tex(toy_str).scale(0.75)
        toy_tex.move_to(POSITION)
        #toy (end)
        #arshak (start)
        arshak_tex = Tex(arshak_str).scale(0.75)
        arshak_seg_0 = self.get_part(arshaks_money)
        arshak_seg_0.set_label(arshak_tex.copy())
        arshak_seg_0.add_label_updater()
        arshak_seg_1 = self.get_part(arshaks_money)
        arshak_seg_1.set_label(arshak_tex)
        arshak_seg_1.add_label_updater()
        #arshak (end)
        #levon (start)
        levon_tex = Tex(levon_str).scale(0.75)
        levon_seg_0 = self.get_part(levons_money)
        levon_seg_0.set_label(levon_tex.copy())
        levon_seg_0.add_label_updater()
        levon_seg_1 = self.get_part(levons_money)
        levon_seg_1.set_label(levon_tex.copy())
        levon_seg_1.add_label_updater()
        #levon (end)
        # toy - arshak (start)
        diff_arshak_toy_seg = self.get_part(
            toy_price - arshaks_money,
            label="{:,}".format(toy_price - arshaks_money),
            color=RED
        )
        diff_arshak_toy_seg.add_label_updater()
        # toy - arshak (end)
        # toy - levon (start)
        diff_levon_toy_seg = self.get_part(
            toy_price - levons_money,
            label="{:,}".format(toy_price - levons_money),
            color=RED
        )
        diff_levon_toy_seg.add_label_updater()
        # toy - levon (end)
        # toy - arshak - levon (start)
        diff_levon_arshak_toy_seg = self.get_part(
            toy_price - levons_money - arshaks_money,
            label="{:,}".format(toy_price - levons_money - arshaks_money),
            color=RED
        )
        diff_levon_arshak_toy_seg.add_label_updater()
        # toy - arshak - levon (end)
        self.add(prob_number)
        #toy-arshak (start animation)
        self.play(FadeIn(coins))
        self.play(ReplacementTransform(coins, toy_seg_0.next_to(POSITION, RIGHT, buff = NAME_SEGMENT_BUFF)), run_time = RUN_TIME)
        toy_brac = Brace(toy_seg_0, DOWN)
        self.wait(WAIT_TIME)
        self.play(
            Write(toy_brac.shift(0.55*DOWN)),
            Write(toy_tex.next_to(toy_brac, DOWN)),
            run_time = RUN_TIME
        )
        self.wait(0.25)
        self.play(Create(arshak_seg_0.align_to(toy_seg_0, LEFT + UP)))
        self.play(Write(arshak_seg_0.update_label_pos()), run_time = RUN_TIME)
        self.wait(WAIT_TIME)
        self.play(Create(diff_arshak_toy_seg.next_to(arshak_seg_0, RIGHT, buff = 0)), run_time = RUN_TIME)
        self.play(
            Write(diff_arshak_toy_seg.update_label_pos()),
            FadeIn(missing_tex.next_to(diff_arshak_toy_seg, DOWN)),
            run_time = RUN_TIME
        )
        self.wait(WAIT_TIME)
        #toy-arshak (end animation)
        #toy-levon (start animation)
        toy_seg_1.align_to(toy_seg_0, LEFT + UP)
        self.play(
            FadeOut(toy_tex, toy_brac, missing_tex)
        )
        self.play(
            toy_seg_1.animate.shift(2*SEGMENT_SEGMENT_BUFF*DOWN),
            run_time = RUN_TIME
        )
        self.wait(WAIT_TIME)
        self.play(
            Create(levon_seg_0.align_to(toy_seg_1, LEFT + UP)),
            run_time = RUN_TIME
        )
        self.play(Write(levon_seg_0.update_label_pos()), run_time = RUN_TIME)
        self.wait(WAIT_TIME)
        self.play(Create(diff_levon_toy_seg.next_to(levon_seg_0, RIGHT, buff = 0)), run_time = RUN_TIME)
        self.play(
            Write(diff_levon_toy_seg.update_label_pos()),
            FadeIn(missing_tex.next_to(diff_levon_toy_seg, DOWN)),
            run_time = RUN_TIME
        )
        self.wait(WAIT_TIME)
        #toy-levon (end animation)
        #toy-levon-arshak (start animation)
        toy_seg_2.align_to(toy_seg_0, LEFT + UP)
        self.play(
            toy_seg_2.animate.shift(SEGMENT_SEGMENT_BUFF*DOWN),
            FadeOut(missing_tex),
            run_time = RUN_TIME
        )
        self.wait(WAIT_TIME)
        levon_seg_1.align_to(levon_seg_0, LEFT + UP)
        arshak_seg_1.align_to(arshak_seg_0, LEFT + UP)
            # mayb to add labels
        self.add(arshak_seg_1.update_label_pos())
        self.add(levon_seg_1.update_label_pos())
        self.play(levon_seg_1.animate.align_to(toy_seg_2, LEFT + UP), run_time = RUN_TIME)
        self.play(arshak_seg_1.animate.next_to(levon_seg_1, RIGHT, buff = 0), run_time = RUN_TIME)
        self.play(Indicate(arshak_seg_1))
        self.play(Indicate(levon_seg_1))
        self.wait(WAIT_TIME)
        self.play(Create(diff_levon_arshak_toy_seg.align_to(toy_seg_2, RIGHT + UP)), run_time = RUN_TIME)
        self.play(
            Write(diff_levon_arshak_toy_seg.update_label_pos()),
            run_time = RUN_TIME
        )
        self.wait(WAIT_TIME)
        toy_seg_2.set_opacity(0)
        self.wait(WAIT_TIME)
        #toy-levon-arshak (end animation)
        #finding arshaks and toys prise (start animation)
        dashed_line_left = DashedLine(levon_seg_0.line.get_start(), levon_seg_1.line.get_start())
        dashed_line_medium = DashedLine(levon_seg_0.line.get_end(), levon_seg_1.line.get_end())
        dashed_line_right = DashedLine(toy_seg_1.line.get_end(), toy_seg_2.line.get_end())
        surrounding_rectangle_arshak = SurroundingRectangle(VGroup(toy_seg_0, toy_seg_0.label, arshak_seg_0.label), buff=0.1)
        surrounding_rectangle_arshak.set_fill(BLACK, 0.85)
        surrounding_rectangle_arshak.set_stroke(opacity=0)
        surrounding_rectangle_arshak.align_to(toy_seg_0, DOWN)
        self.play(FadeIn(surrounding_rectangle_arshak))
        self.wait(0.25)
        self.play(
            Create(dashed_line_left),
            Create(dashed_line_medium),
            Create(dashed_line_right),
            run_time = RUN_TIME
        )
        surrounding_rectangle_levon = SurroundingRectangle(VGroup(levon_seg_0, levon_seg_1, levon_seg_0.label), buff=0.5)
        surrounding_rectangle_levon.set_fill(BLACK, 0.85)
        surrounding_rectangle_levon.set_stroke(opacity=0)
        surrounding_rectangle_levon.align_to(levon_seg_0.line, RIGHT)
        self.wait(0.25)
        self.play(Indicate(arshak_seg_1))
        self.play(
            FadeIn(surrounding_rectangle_levon)
        )
        self.wait(WAIT_TIME)
        arshak_tex_in_equation = arshak_tex.copy()
        arshak_tex_in_equation.move_to(arshak_seg_1.update_label_pos())
        self.play(arshak_tex_in_equation.animate.align_to(toy_seg_1, LEFT + UP).shift(DOWN))
        arshak_equation = MathTex("=", "200", "-", "60", "=", "140" )
        arshak_equation.next_to(arshak_tex_in_equation, RIGHT, buff=0.15)
        self.play(Write(arshak_equation[0]))
        self.play(TransformMatchingShapes(diff_levon_toy_seg.label.copy(), arshak_equation[1]))
        self.play(
            TransformMatchingShapes(diff_levon_arshak_toy_seg.label.copy(), arshak_equation[3]),
            Write(arshak_equation[2])
        )
        self.play(
            FadeOut(surrounding_rectangle_levon),
            FadeOut(surrounding_rectangle_arshak)
        )
        self.wait(WAIT_TIME)
        self.play(
            Write(arshak_equation[4:])
        )
        self.play(FadeOut(dashed_line_left, dashed_line_medium, dashed_line_right))
        self.play(arshak_seg_0.label.animate.become(arshak_equation[5].copy().move_to(arshak_seg_0.update_label_pos())))
        surrounding_rectangle_arshak_levon = SurroundingRectangle(VGroup(toy_seg_1, toy_seg_2), buff=0.5)
        surrounding_rectangle_arshak_levon.align_to(toy_seg_1, DOWN)
        surrounding_rectangle_arshak_levon.set_fill(BLACK, 0.85)
        surrounding_rectangle_arshak_levon.set_stroke(opacity=0)
        toy_tex_in_equation = toy_tex.copy()
        toy_tex_in_equation.next_to(arshak_tex_in_equation, DOWN, buff=0.8, aligned_edge=LEFT)
        toy_equation = MathTex("=", "300", "+", "140", "=", "440")
        toy_equation.next_to(toy_tex_in_equation, RIGHT, buff=0.15)
        self.wait()
        self.play(Write(toy_tex_in_equation), FadeIn(surrounding_rectangle_arshak_levon))
        self.play(Write(toy_equation[0]))
        self.play(TransformMatchingShapes(diff_arshak_toy_seg.label.copy(), toy_equation[1]))
        self.play(
            TransformMatchingShapes(arshak_seg_0.label.copy(), toy_equation[3]),
            Write(toy_equation[2])
        )
        self.play(
            Write(toy_equation[4:])
        )
        self.play(
            FadeOut(surrounding_rectangle_arshak_levon),
            FadeOut(arshak_seg_0, diff_arshak_toy_seg),
            FadeOut(arshak_seg_0.label, diff_arshak_toy_seg.label),
            TransformMatchingShapes(toy_equation[5].copy(), toy_seg_0.update_label_pos())
        )
        self.wait(WAIT_TIME)
        #finding arshaks and toys prise (end animation)
        self.play(FadeOut(toy_tex_in_equation, toy_equation))
        self.wait(0.25)
        surrounding_rectangle_arshak_levon_only = SurroundingRectangle(VGroup(toy_seg_2), buff=0.5)
        surrounding_rectangle_arshak_levon_only.align_to(toy_seg_2, DOWN)
        surrounding_rectangle_arshak_levon_only.set_fill(BLACK, 0.85)
        surrounding_rectangle_arshak_levon_only.set_stroke(opacity=0)
        levon_tex_in_equation = levon_tex.copy()
        levon_tex_in_equation.clear_updaters()
        levon_tex_in_equation.next_to(arshak_tex_in_equation, DOWN, buff=0.8, aligned_edge=LEFT)
        levon_equation = MathTex("=", "440", "-", "200", "=", "240")
        levon_equation.next_to(levon_tex_in_equation, RIGHT, buff=0.15)
        self.play(Indicate(toy_seg_0.label))
        self.play(Indicate(arshak_equation[5]))
        self.wait()
        self.play(Write(levon_tex_in_equation), FadeIn(surrounding_rectangle_arshak_levon_only))
        self.play(Write(levon_equation[0]))
        self.play(TransformMatchingShapes(toy_seg_0.label.copy(), levon_equation[1]))
        self.play(
            TransformMatchingShapes(diff_levon_toy_seg.label.copy(), levon_equation[3]),
            Write(levon_equation[2])
        )
        self.play(
            Write(levon_equation[4:])
        )
        self.play(
            FadeOut(surrounding_rectangle_arshak_levon_only)
        )
        self.wait(WAIT_TIME)
        surrounding_rectangle_levon_only = SurroundingRectangle(VGroup(toy_seg_1), buff=0.5)
        surrounding_rectangle_levon_only.align_to(toy_seg_1, DOWN)
        surrounding_rectangle_levon_only.set_fill(BLACK, 0.85)
        surrounding_rectangle_levon_only.set_stroke(opacity=0)

        arshak_levon_brace = Brace(VGroup(arshak_equation, levon_equation), RIGHT)
        arshak_levon_brace_equation = MathTex("140", "+", "240", "=", "380")
        arshak_levon_brace_equation.next_to(arshak_levon_brace)
        arshak_levon_seg = self.get_part(
            arshaks_money + levons_money,
            label = "{:,}".format(arshaks_money + levons_money)
        )
        arshak_levon_seg.align_to(toy_seg_2, LEFT + UP)

        self.play(
            FadeIn(surrounding_rectangle_levon_only),
            FadeIn(arshak_levon_brace),
            Write(arshak_levon_brace_equation)
        )
        self.wait()
        self.play(
            FadeOut(arshak_seg_1, levon_seg_1),
            FadeOut(arshak_seg_1.label, levon_seg_1.label),
            FadeIn(arshak_levon_seg)
        )
        self.play(TransformMatchingShapes(arshak_levon_brace_equation[4].copy(), arshak_levon_seg.update_label_pos()))
        self.wait()
        self.play(Indicate(arshak_levon_seg.label))
        self.play(Indicate(toy_seg_0.label))
        self.play(Indicate(diff_levon_arshak_toy_seg.label))
    
    def get_part(self, value, label = None, color = WHITE):
        seg = Segment(
            ORIGIN,
            UNIT * value * RIGHT,
            label,
            stroke_width = 6,
            color = color
        )
        return seg
