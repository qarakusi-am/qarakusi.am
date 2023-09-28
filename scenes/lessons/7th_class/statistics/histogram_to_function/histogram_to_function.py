from manim import DOWN, RIGHT, WHITE, LEFT, UP
from manim import Tex, AnimationGroup, VGroup, Line, DashedLine, ReplacementTransform, Dot,Rectangle, TransformFromCopy, Arrow
from manim import FadeOut, Write
from manim import Scene
from .text import *
class HistogramToFunction(Scene):
    def construct(self):

        running_data = VGroup(Tex(running_time, speed_in_km_h).shift(UP * 3),
                              Tex(rest_time).shift(UP * 2),
                              Tex(walk_back_speed, ).shift(UP * 1))

        self.play(Write(running_data[0]))
        self.wait()

        self.play(Write(running_data[1].align_to(running_data[0], LEFT)))
        self.wait()

        self.play(Write(running_data[2].align_to(running_data[0], LEFT)))
        self.wait(2)

        speed_text = '9' + km + '/' + hour + ' = $\\frac{9 \cdot 1000}{60}$ ' + meter + '/' + minute + ' = 150' + meter + '/' + minute
        speed = Tex(speed_text)

        self.play(Write(VGroup(speed[0][0:5])))
        self.wait()

        self.play(Write(VGroup(speed[0][5:18])))
        self.wait()

        self.play(Write(VGroup(speed[0][18:])))
        self.wait()

        self.play(AnimationGroup(VGroup(running_data[0][1]).animate.set_opacity(0),
                                 VGroup(speed[0][19:]).animate.next_to(running_data[0][0], RIGHT).shift(RIGHT * 0.1),
                                 VGroup(speed[0][0:19]).animate.set_opacity(0)))
        self.wait(2)

        reformed_walk_speed_str = '50' + meter + '/' + minute
        running_data.add(Tex(reformed_walk_speed_str).next_to(running_data[2][0][-6], RIGHT))

        self.play(ReplacementTransform(VGroup(running_data[2][0][-5:]), running_data[3]))
        self.wait(2)

        axis_width = 2
        label_font_size = 30
        x_axis = Line((-5.5, -2, 0), (5, -2, 0), stroke_width=axis_width)
        y_axis = Line((-4.45, -3, 0), (-4.45, 2, 0), stroke_width=axis_width)
        coordinates = VGroup(x_axis, y_axis)

        self.play(Write(coordinates))
        self.wait()

        label = "$1$" + minute
        x_labels = VGroup(Tex(label, font_size=label_font_size))
        x_labels[0].move_to((-4, -2.3, 0))

        y_labels = VGroup(Tex('$150$' + meter, font_size=label_font_size).move_to((-5, -1.1, 0)),
                          Tex('$300$' + meter, font_size=label_font_size).move_to((-5, -0.3, 0)),
                          Tex('$450$' + meter, font_size=label_font_size).move_to((-5, 0.5, 0)),
                          Tex('$400$' + meter, font_size=label_font_size).move_to((-5, 0.26, 0)),
                          )

        y_label_lines = VGroup()
        for i in range(4):
            y_label_lines.add(
                Line(LEFT * 0.1, RIGHT * 0.1).stretch(0.1, 1).move_to(y_labels[i], RIGHT).shift(RIGHT * 0.37))

        for i in range(2, 18):
            label = "$" + str(i) + "$" + minute
            x_labels.add(Tex(label, font_size=label_font_size).next_to(x_labels[i - 2], RIGHT).shift(RIGHT * 0.3))

        rectangle_color = WHITE
        rectangles = VGroup(Rectangle(width=0.5, height=0.8, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=1.6, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=2.4, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=2.4, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=2.4, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=2.4, fill_color=rectangle_color, fill_opacity=1),
                            Rectangle(width=0.5, height=2.4, fill_color=rectangle_color, fill_opacity=1),
                            )

        for i in range(9):
            rectangles.add(Rectangle(width=0.5, height=2.15 - i * 0.25, fill_color=rectangle_color, fill_opacity=1))

        for i in range(16):
            rectangles[i].next_to(x_labels[i], UP)

        dashed_lines = VGroup(DashedLine(rectangles[0].get_top(), (-4.4, -1.1, 0), stroke_width=axis_width),
                              DashedLine(rectangles[1].get_top(), (-4.4, -0.3, 0), stroke_width=axis_width),
                              DashedLine(rectangles[2].get_top(), (-4.4, 0.5, 0), stroke_width=axis_width))

        self.play(Write(x_labels[0]))
        self.wait()
        self.play(Write(rectangles[0]))
        self.wait()
        self.play(Write(dashed_lines[0]), Write(y_labels[0]), Write(y_label_lines[0]))
        self.wait()

        squeezed_running_data = Tex(run + ' $3$' + minute + ', ' + rest + ' $4$' + minute).shift(UP * 3)
        self.play(ReplacementTransform(VGroup(running_data, speed[0][19:]), squeezed_running_data))
        self.wait(2)

        self.play(Write(x_labels[1]))
        self.wait()
        self.play(Write(rectangles[1]))
        self.wait()
        self.play(Write(dashed_lines[1]), Write(y_labels[1]), Write(y_label_lines[1]))
        self.wait()

        self.play(Write(x_labels[2]))
        self.wait()
        self.play(Write(rectangles[2]))
        self.wait()
        self.play(Write(dashed_lines[2]), Write(y_labels[2]), Write(y_label_lines[2]))
        self.wait()

        self.play(Write(x_labels[3]), Write(x_labels[4]), Write(x_labels[5]), Write(x_labels[6]))
        self.wait()

        self.play(AnimationGroup(TransformFromCopy(rectangles[2], rectangles[3]),
                                 TransformFromCopy(rectangles[2], rectangles[4]),
                                 TransformFromCopy(rectangles[2], rectangles[5]),
                                 TransformFromCopy(rectangles[2], rectangles[6])))
        self.wait()

        self.play(FadeOut(dashed_lines))
        self.wait()

        self.play(VGroup(rectangles[0:7]).animate.stretch(0.5, 0).next_to(x_labels[1], UP).shift(RIGHT * 0.45),
                  AnimationGroup(*[x_labels[i].animate.shift(LEFT * 0.4 * i) for i in range(1, 7)]))
        self.wait(3)

        for i in range(7, 17):
            x_labels[i].shift(LEFT * 0.4 * i)

        for i in range(7, 16):
            rectangles[i].stretch(0.5, 0).next_to(x_labels[i], UP)

        dashed_lines.add(DashedLine(rectangles[7].get_top(), (-4.4, 0.25, 0), stroke_width=axis_width))

        self.play(Write(x_labels[7]))
        self.wait()
        self.play(Write(rectangles[7]))
        self.wait()
        self.play(Write(dashed_lines[3], run_time=1), Write(y_labels[3], run_time=1),
                  Write(y_label_lines[3], run_time=1))
        self.wait(2)

        self.play(FadeOut(dashed_lines[3]))
        self.wait()

        self.play(AnimationGroup(*[Write(x_labels[i]) for i in range(8, len(x_labels))]))
        self.wait(3)

        self.play(AnimationGroup(*[Write(rectangles[i]) for i in range(8, 16)]))
        self.wait(3)

        x_labels.add(Tex('2' + minute + '15' + second, font_size=label_font_size - 5).next_to(x_labels[0], RIGHT).shift(
            DOWN * 0.5 + LEFT * 0.06))
        arrow = Arrow(x_labels[17].get_top() + DOWN * 0.2, (-3.36, -1.8, 0), max_tip_length_to_length_ratio=0.1)

        self.play(Write(x_labels[17]))
        self.wait()
        self.play(Write(arrow))
        self.wait()

        self.play(AnimationGroup(*[rectangles[i].animate.stretch(0.001, 0) for i in range(0, 16)]))
        self.wait()

        rectangles.add(
            Rectangle(width=0.5, height=2, fill_color=rectangle_color, fill_opacity=1).stretch(0.001, 0).next_to(
                x_labels[1], UP).shift(RIGHT * 0.2))

        self.play(Write(rectangles[16]))
        self.wait()

        self.play(FadeOut(x_labels[17], arrow))
        self.wait()

        dotes = VGroup()
        for i in range(17):
            dotes.add(Dot(point=rectangles[i].get_top(), radius=0.05, fill_opacity=1))

        #arrange dotes for a straight looking line

        dotes[0].shift(DOWN * 0.03)
        dotes[7].shift(UP * 0.022)
        dotes[8].shift(UP * 0.073)
        dotes[9].shift(UP * 0.075)
        dotes[10].shift(UP * 0.07)
        dotes[11].shift(UP * 0.07)
        dotes[12].shift(UP * 0.06)
        dotes[13].shift(UP * 0.05)
        dotes[14].shift(UP * 0.025)
        dotes[15].shift(UP * 0.025)


        self.play(AnimationGroup(*[Write(dotes[i]) for i in range(0, 17)]))
        self.wait()

        self.play(FadeOut(rectangles))
        self.wait()

        function_lines = VGroup(Line((-4.4, -2, 0), dotes[2].get_center()),
                                Line(dotes[2].get_center(), dotes[6].get_center()),
                                Line(dotes[6].get_center(), (4., -1.95, 0)))

        self.play(Write(function_lines, run_time=2))
        self.play(FadeOut(dotes))
        self.wait()
