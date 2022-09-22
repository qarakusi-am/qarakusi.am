from manim import Scene, Rectangle, MathTex, Line, FadeIn, Create, Write, GrowFromEdge, FadeOut, Transform, VGroup, Circumscribe, np, Brace
from manim import LEFT, RIGHT, UP, DOWN, YELLOW, ORANGE, PI
from manim import always_redraw
from lib.qarakusiscene import TaskNumberBox
from .text import *

class Problem11273(Scene):
    def construct(self):
        scale = .6
        task_number = TaskNumberBox(task_number_string)
        rectangle1 = Rectangle(height=3, width=9).scale(scale)
        rectangle2 = Rectangle(height=3, width=3).scale(scale).align_to(rectangle1, LEFT)
        rectangle3 = Rectangle(height=3, width=6).scale(scale).align_to(rectangle1, RIGHT)
        example1 = Rectangle(height=2, width=10).scale(scale)
        example2 = Rectangle(height=1, width=11).scale(scale)
        example1_height_label = MathTex(rf"2\text{{{cm}}}").next_to(example1, LEFT)
        example1_width_label = MathTex(rf"10\text{{{cm}}}").next_to(example1, UP)
        example2_height_label = MathTex(rf"1\text{{{cm}}}").next_to(example2, LEFT)
        example2_width_label = MathTex(rf"11\text{{{cm}}}").next_to(example2, UP)
        perimeter1 = MathTex(rf"P=24\text{{{cm}}}").move_to(rectangle1.get_center())
        perimeter2 = MathTex(rf"P=12\text{{{cm}}}")
        perimeter3 = MathTex(rf"P=18\text{{{cm}}}")
        example1_perimeter = MathTex(rf"2+10+2+10=24\text{{{cm}}}").to_edge(DOWN, buff=2).to_edge(LEFT)
        example2_perimeter = MathTex(rf"1+11+1+11=24\text{{{cm}}}").to_edge(DOWN, buff=2).to_edge(LEFT)
        example1_area = MathTex(rf"S=20\text{{{cm}}}^2").move_to(rectangle1.get_center()).scale(1.2)
        example2_area = MathTex(rf"S=11\text{{{cm}}}^2").move_to(rectangle1.get_center()).scale(.85)
        question = MathTex("S=?").move_to(rectangle1.get_center()).scale(1.2)
        line = Line(UP*1.2, DOWN*1.2, color=YELLOW).next_to(rectangle2, buff=0)
        sum_of_2_perimeters = MathTex(rf"12+18=30\text{{{cm}}}").to_edge(LEFT).to_edge(DOWN, buff=1.9)
        nvazox_mas = MathTex(rf"30-24=6\text{{{cm}}}").next_to(sum_of_2_perimeters, DOWN).align_to(sum_of_2_perimeters, LEFT)
        height_label = MathTex(rf"6:2=3\text{{{cm}}}").next_to(nvazox_mas, DOWN).align_to(nvazox_mas, LEFT)
        width_plus_height = MathTex(rf"24:2=12\text{{{cm}}}").next_to(sum_of_2_perimeters, buff=5.1)
        width_label = MathTex(rf"12-3=9\text{{{cm}}}").next_to(width_plus_height, DOWN).align_to(width_plus_height, LEFT)
        self.play(FadeIn(task_number))
        self.wait()
        self.play(Create(rectangle1), run_time=1.5)
        self.wait()
        self.play(Write(perimeter1), run_time=1)
        self.wait()
        self.play(
            GrowFromEdge(line, UP),
            FadeOut(perimeter1),
            run_time=3
        )
        self.add(rectangle2, rectangle3, line)
        self.remove(rectangle1)
        self.wait()
        self.play(
            rectangle2.animate.shift(LEFT*2.5),
            rectangle3.animate.shift(RIGHT*2.5),
            run_time=3
        )
        self.wait()
        perimeter2.move_to(rectangle2.get_center()).scale(.7)
        perimeter3.move_to(rectangle3.get_center())
        self.play(Write(perimeter2), run_time=1.5)
        self.wait()
        self.play(Write(perimeter3), run_time=1.5)
        self.wait()
        self.play(FadeOut(line))
        self.wait()
        self.play(
            FadeOut(perimeter2),
            FadeOut(perimeter3)
        )
        self.play(
            rectangle2.animate.shift(RIGHT*2.5),
            rectangle3.animate.shift(LEFT*2.5),
            run_time=3
        )
        self.add(rectangle1)
        self.play(FadeOut(rectangle2, rectangle3))
        self.wait()
        self.play(
            Write(question),
            run_time=2
        )
        self.wait()
        self.play(
            rectangle1.animate.become(example1),
            FadeOut(question),
            run_time=1.5
        )
        self.wait()
        self.play(
            Write(example1_height_label),
            run_time=2
        )
        self.wait()
        self.play(
            Write(example1_width_label),
            run_time=2
        )
        self.wait()
        self.play(Write(example1_perimeter), run_time=3)
        self.wait()
        self.play(Write(example1_area), run_time=1.5)
        self.wait()
        self.play(
            FadeOut(example1_area),
            FadeOut(example1_perimeter),
            Transform(rectangle1, example2),
            Transform(example1_height_label, example2_height_label),
            Transform(example1_width_label, example2_width_label),
            run_time=2
        )
        self.wait()
        self.play(Write(example2_perimeter), run_time=3)
        self.wait()
        self.play(Write(example2_area), run_time=1.5)
        self.play(
            FadeOut(VGroup(example1_height_label, example1_width_label, example2_perimeter, example2_area)),
            run_time=1.5
        )
        self.wait()
        inital_rectangle = Rectangle(height=3, width=9).scale(scale)
        self.play(Transform(rectangle1, inital_rectangle), run_time=1.5)
        self.wait()
        self.play(
            GrowFromEdge(line, UP),
            run_time=3
        )
        self.add(rectangle2, rectangle3, line)
        self.remove(rectangle1)
        self.wait()
        self.play(
            rectangle2.animate.shift(LEFT*4),
            rectangle3.animate.shift(RIGHT*4),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(line))
        self.wait()
        perimeter2.move_to(rectangle2.get_center())
        perimeter3.move_to(rectangle3.get_center())
        self.play(
            Write(perimeter2),
            Write(perimeter3),
            run_time=2
        )
        self.wait()
        rectangle2_copy = rectangle2.copy()
        rectangle3_copy = rectangle3.copy()
        self.play(
            rectangle2_copy.animate.shift(RIGHT*4),
            rectangle3_copy.animate.shift(LEFT*4),
            run_time=3
        )
        self.add(rectangle1)
        self.play(FadeOut(rectangle2_copy, rectangle3_copy))
        self.wait()
        self.play(
            Write(perimeter1),
            run_time=2
        )
        self.wait()
        self.play(VGroup(rectangle1, perimeter1).animate.shift(UP*2.1))
        self.wait()
        self.play(Write(sum_of_2_perimeters), run_time=3)
        self.wait()
        self.play(Circumscribe(perimeter1), run_time=1.5)
        self.wait()
        self.play(
            VGroup(rectangle2, perimeter2).animate.shift(RIGHT*3.5),
            VGroup(rectangle3, perimeter3).animate.shift(LEFT*3.5),
            run_time=3
        )
        self.wait()
        korox_hatvac1 = always_redraw(lambda: Rectangle(width=0, height=3, color=ORANGE, stroke_width=10).scale(scale).align_to(rectangle2, RIGHT))
        korox_hatvac2 = always_redraw(lambda: Rectangle(width=0, height=3, color=ORANGE, stroke_width=10).scale(scale).align_to(rectangle3, LEFT))
        self.play(FadeIn(korox_hatvac1, korox_hatvac2))
        self.play(FadeOut(perimeter2, perimeter3))
        self.play(
            rectangle2.animate.shift(RIGHT*.5),
            rectangle3.animate.shift(LEFT*.5),
            run_time=2
        )
        self.wait()
        rectangle1_copy = rectangle1.copy().move_to(np.array([0,0,0]))
        self.add(rectangle1_copy)
        self.play(
            FadeOut(rectangle2, rectangle3, korox_hatvac1, korox_hatvac2),
            run_time=3.5
        )
        self.wait()
        self.play(FadeIn(rectangle2, rectangle3, korox_hatvac1, korox_hatvac2))
        self.remove(rectangle1_copy)
        self.play(
            rectangle2.animate.shift(LEFT*.7),
            rectangle3.animate.shift(RIGHT*.7),
            run_time=1.5
        )
        perimeter2.move_to(rectangle2.get_center())
        perimeter3.move_to(rectangle3.get_center())
        self.play(FadeIn(perimeter2, perimeter3))
        self.wait()
        self.play(Write(nvazox_mas), run_time=2.5)
        self.wait()
        korox_hatvac1_copy = korox_hatvac1.copy()
        korox_hatvac2_copy = korox_hatvac2.copy()
        self.play(
            korox_hatvac1_copy.animate.shift(DOWN*2.6+LEFT*.2).rotate(.5*PI),
            run_time=2
        )
        bajanox_gic = Line(start=UP*0, end=DOWN*.4, color=ORANGE, stroke_width=7).next_to(korox_hatvac1_copy, buff=0)
        self.play(
            korox_hatvac2_copy.animate.rotate(.5*PI).next_to(korox_hatvac1_copy, RIGHT, buff=0),
            FadeIn(bajanox_gic),
            run_time=2
        )
        self.wait()
        height_2x = MathTex(rf"6\text{{{cm}}}")
        self.play(
            Write(height_2x.next_to(VGroup(korox_hatvac1_copy, korox_hatvac2_copy), UP, buff=.6)),
            FadeIn(Brace(VGroup(korox_hatvac1_copy, korox_hatvac2_copy), UP)),
        )
        self.wait()
        height = MathTex(rf"3\text{{{cm}}}").next_to(rectangle1, LEFT)
        width = MathTex(rf"9\text{{{cm}}}").next_to(rectangle1, UP)
        self.play(Write(height_label), run_time=2.5)
        self.wait()
        height_copy1 = height.copy().next_to(korox_hatvac1_copy, DOWN)
        height_copy2 = height.copy().next_to(korox_hatvac2_copy, DOWN)
        self.play(
            Write(VGroup(height_copy1, height_copy2)),
            run_time=2.5
        )
        self.wait()
        self.play(
            height_copy1.copy().animate.next_to(rectangle2),
            run_time=2
        )
        self.wait()
        self.play(Write(height), run_time=1.5)
        self.wait()
        self.play(Write(width_plus_height), run_time=3)
        self.wait()
        self.play(Write(width_label), run_time=2.5)
        self.wait()
        self.play(Write(width), run_time=1.5)
        self.wait()
        self.play(perimeter1.animate.shift(UP*.28))
        self.play(
            Write(MathTex(rf"S=3\cdot9=27\text{{{cm}}}^2").move_to(rectangle1.get_center()).shift(DOWN*.27)),
            run_time=4
        )
        self.wait(2)
