from manim import DOWN, RIGHT, WHITE, LEFT, UP, BLACK, BarChart, GREEN, RED, Rectangle, GREEN_B, YELLOW, ORANGE
from manim import Tex, AnimationGroup, SurroundingRectangle, VGroup, Line, DashedLine, ReplacementTransform, \
    DrawBorderThenFill
from manim import FadeOut, Write
from manim import Scene
from . import text

from .text import *


class Histogram(Scene):
    def construct(self):
        self.text = text
        position = [-4, 1, 0]
        horizontal_shift_factor = 0.3
        vertical_shift_factor = 0.7
        data = [
            [Tex(january + '$30 \longrightarrow$'), VGroup(Tex(' $15$ ' + minute))],
            [Tex(january + '$31 \longrightarrow$'), VGroup(Tex(' $10$ ' + minute))],
            [Tex(february + '$1 \longrightarrow$'), VGroup(Tex(' $15$ ' + minute))],
            [Tex(february + '$2 \longrightarrow$'), VGroup(Tex(' $14$ ' + minute))],
            [Tex(february + '$3 \longrightarrow$'), VGroup(Tex('$17$ ' + minute))],
            [Tex(february + '$\ 6 \longrightarrow$'), VGroup(Tex('$14$ ' + minute))],
            [Tex(february + '$\ 7 \longrightarrow $ '), VGroup(Tex('$11$ ' + minute))],
            [Tex(february + '$\ 8 \longrightarrow$'), VGroup(Tex('$15$ ' + minute))],
            [Tex(february + '$\ 9 \longrightarrow$'), VGroup(Tex('$14$ ' + minute))],
            [Tex(february + '$10 \longrightarrow$'), VGroup(Tex('$15$ ' + minute))],

        ]
        date_time_text_part1 = VGroup()
        date_time_text_part2 = VGroup()
        date_time_text_part1.add(VGroup(data[0][0], VGroup(data[0][1].next_to(data[0][0], RIGHT),
                                                           SurroundingRectangle(data[0][1], color=BLACK))).move_to(
            position))
        date_time_text_part2.add(VGroup(data[5][0], VGroup(data[5][1].next_to(data[5][0], RIGHT),
                                                           SurroundingRectangle(data[5][1], color=BLACK))).next_to(
            date_time_text_part1, RIGHT).shift(RIGHT))

        for i in range(1, 5):
            date_time_text_part1.add(VGroup(data[i][0].next_to(data[i - 1][0], DOWN),
                                            VGroup(data[i][1].next_to(data[i][0], RIGHT),
                                                   SurroundingRectangle(data[i][1], color=BLACK))).shift(
                DOWN * horizontal_shift_factor))
            date_time_text_part2.add(VGroup(data[i + 5][0].next_to(data[i + 4][0], DOWN),
                                            VGroup(data[i + 5][1].next_to(data[i + 5][0], RIGHT),
                                                   SurroundingRectangle(data[i + 5][1], color=BLACK))).shift(
                DOWN * horizontal_shift_factor))

        date_time_text_part2[4][1].next_to(date_time_text_part2[3][1], DOWN * horizontal_shift_factor * 5)
        self.play(Write(date_time_text_part1.shift(UP * horizontal_shift_factor * 5)))
        self.wait()
        self.play(Write(date_time_text_part2.shift(UP * horizontal_shift_factor * 5)))
        self.wait()
        self.play(AnimationGroup(*[data[i][0][0].animate.set_opacity(0) for i in range(0, 10)]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(date_time_text_part1[i][1][1].animate.set_color(WHITE),
                                                  date_time_text_part2[i].animate.set_color(WHITE)) for i in
                                   range(0, 5)]))
        self.play(AnimationGroup(
            date_time_text_part1[1][1][0].animate.set_color(GREEN),
            date_time_text_part2[1][1][0].animate.set_color(GREEN_B),
            date_time_text_part1[3][1][0].animate.set_color(YELLOW),
            date_time_text_part2[3][1][0].animate.set_color(YELLOW),
            date_time_text_part2[0][1][0].animate.set_color(YELLOW),
            date_time_text_part1[0][1][0].animate.set_color(ORANGE),
            date_time_text_part1[2][1][0].animate.set_color(ORANGE),
            date_time_text_part2[2][1][0].animate.set_color(ORANGE),
            date_time_text_part2[4][1][0].animate.set_color(ORANGE),
            date_time_text_part1[4][1][0].animate.set_color(RED),
        ))
        self.wait()
        rectangles = VGroup()
        for i in range(0, 5):
            rectangles.add(date_time_text_part1[i][1])
            rectangles.add(date_time_text_part2[i][1])
        start_position = [-4, 3, 0]
        # put rectangle in different places
        self.play(AnimationGroup(
            rectangles[0].animate.move_to(start_position, RIGHT * 3 + DOWN * 3),
            rectangles[1].animate.move_to(rectangles[0], RIGHT + UP * 5),
            rectangles[2].animate.next_to(rectangles[0], DOWN + LEFT),
            rectangles[3].animate.next_to(rectangles[2], DOWN + RIGHT),
            rectangles[4].animate.next_to(rectangles[3], UP * 2 + LEFT),
            rectangles[5].animate.next_to(rectangles[3], DOWN * 3),
            rectangles[6].animate.next_to(rectangles[4], UP * 5 + RIGHT * 2),
            rectangles[7].animate.move_to(rectangles[1], LEFT * 2 + UP * 4),
            rectangles[8].animate.next_to(rectangles[1], LEFT * 3 + DOWN),
            rectangles[9].animate.next_to(rectangles[7], LEFT + UP),
        ))
        self.wait()

        axis_width = 2
        x_axis = Line((-6, -2, 0), (7, -2, 0), stroke_width=axis_width)
        y_axis = Line((-6, -1, 0), (-6, 2, 0), stroke_width=axis_width)
        coordinates = VGroup(x_axis).shift(UP)

        self.play(Write(coordinates))
        self.wait()

        label_font_size = 36
        labels = VGroup(
            Tex('10 ' + minute[0], minute[1:len(minute)], font_size=label_font_size, color=GREEN),
            Tex('11 ' + minute[0], minute[1:len(minute)], font_size=label_font_size, color=GREEN_B),
            Tex('14 ' + minute[0], minute[1:len(minute)], font_size=label_font_size, color=YELLOW),
            Tex('15 ' + minute[0], minute[1:len(minute)], font_size=label_font_size, color=ORANGE),
            Tex('17 ' + minute[0], minute[1:len(minute)], font_size=label_font_size, color=RED),
            Tex('12 ' + minute[0], font_size=label_font_size),
            Tex('13 ' + minute[0], font_size=label_font_size),
            Tex('16 ' + minute[0], font_size=label_font_size)
        )

        # arrange rectangles on top of their label on x_axis
        self.play(
            Write(labels[0].next_to(coordinates, DOWN).align_to(x_axis, LEFT).shift(RIGHT * horizontal_shift_factor)),
            rectangles[2].animate.scale(0.6).move_to(labels[0], UP).shift(UP * vertical_shift_factor))
        self.play(Write(labels[1].next_to(labels[0], RIGHT).shift(RIGHT * horizontal_shift_factor)),
                  rectangles[3].animate.scale(0.6).move_to(labels[1], UP).shift(UP * vertical_shift_factor))
        self.wait()
        self.play(Write(labels[2].next_to(labels[1], RIGHT).shift(RIGHT * horizontal_shift_factor)),
                  rectangles[1].animate.scale(0.6).move_to(labels[2], UP).shift(UP * vertical_shift_factor))
        self.wait()
        self.play(AnimationGroup(
            rectangles[6].animate.scale(0.6).move_to(rectangles[1], UP).shift(UP * 0.5),
            rectangles[7].animate.scale(0.6).move_to(rectangles[1], UP).shift(UP)
        ))
        self.wait()
        self.play(AnimationGroup(
            Write(labels[3].next_to(labels[2], RIGHT).shift(RIGHT * horizontal_shift_factor)),
            rectangles[0].animate.scale(0.6).move_to(labels[3], UP).shift(UP * vertical_shift_factor),
            rectangles[4].animate.scale(0.6).move_to(labels[3], UP).shift(UP * 1.2),
            rectangles[5].animate.scale(0.6).move_to(labels[3], UP).shift(UP * 1.7),
            Write(labels[4].next_to(labels[3], RIGHT).shift(RIGHT * horizontal_shift_factor)),
            rectangles[8].animate.scale(0.6).move_to(labels[4], UP).shift(UP * vertical_shift_factor),
            rectangles[9].animate.scale(0.6).move_to(labels[3], UP).shift(UP * 2.2),

        ))

        self.wait()

        histogram_label = Tex(self.text.histogram, font_size=65).move_to(coordinates, UP).shift(UP * 4.3)
        self.play(Write(histogram_label))
        self.wait()

        self.play(coordinates.animate.add(y_axis))
        self.wait()
        self.play(AnimationGroup(*[AnimationGroup(date_time_text_part1[i][1][0].animate.set_color(BLACK),
                                                  date_time_text_part2[i][1][0].animate.set_color(BLACK)) for i in
                                   range(0, 5)]))
        self.wait()
        dashed_lines = VGroup(DashedLine(date_time_text_part1[1][1][1].get_top(), (-6, -0.55, 0)),
                              DashedLine(date_time_text_part2[3][1][1].get_top(), (-6, 0.48, 0)),
                              DashedLine(date_time_text_part2[4][1][1].get_top(), (-6, 0.98, 0)),
                              DashedLine(date_time_text_part1[3][1][1].get_top(), (-6, -0.05, 0)))
        y_labels = Tex('$1$', '$3$', '$4$', '$2$')

        stroke_width = 1.5
        # label lines on y axis
        y_label_lines = VGroup(Line((-6.1, -0.55, 0), (-5.9, -0.55, 0), stroke_width=stroke_width),
                               Line((-6.1, 0.48, 0), (-5.9, 0.48, 0), stroke_width=stroke_width),
                               Line((-6.1, 0.98, 0), (-5.9, 0.98, 0), stroke_width=stroke_width),
                               Line((-6.1, -0.05, 0), (-5.9, -0.05, 0), stroke_width=stroke_width))

        # write labels and dashed lines on y_axis
        self.play(AnimationGroup(Write(dashed_lines[0]), y_label_lines[0].animate))
        self.play(Write(y_labels[0].scale(vertical_shift_factor).next_to(dashed_lines[0], LEFT)))
        self.wait()
        self.play(AnimationGroup(Write(dashed_lines[1]), y_label_lines[1].animate))
        self.play(Write(y_labels[1].scale(vertical_shift_factor).next_to(dashed_lines[1], LEFT)))
        self.wait()
        self.play(AnimationGroup(Write(dashed_lines[2]), y_label_lines[2].animate))
        self.play(Write(y_labels[2].scale(vertical_shift_factor).next_to(dashed_lines[2], LEFT)))
        self.wait()
        self.play(AnimationGroup(Write(dashed_lines[3]), y_label_lines[3].animate))
        self.play(Write(y_labels[3].scale(vertical_shift_factor).next_to(dashed_lines[3], LEFT)))
        self.wait()

        # create colored rectangles to present bars
        colored_rectangles = VGroup(
            VGroup(Rectangle(width=rectangles[0].width, height=rectangles[0].height, color=GREEN).set_fill(GREEN, 1)),
            VGroup(
                Rectangle(width=rectangles[0].width, height=rectangles[0].height, color=GREEN_B).set_fill(GREEN_B, 1)),
            VGroup(
                Rectangle(width=rectangles[0].width, height=rectangles[0].height * 3.5, color=YELLOW).set_fill(YELLOW,
                                                                                                               1)),
            VGroup(Rectangle(width=rectangles[0].width, height=rectangles[0].height * 5, color=ORANGE).set_fill(ORANGE,
                                                                                                                1)),
            VGroup(Rectangle(width=rectangles[0].width, height=rectangles[0].height, color=RED).set_fill(RED, 1)))

        self.play(FadeOut(dashed_lines))

        self.play(AnimationGroup(
            ReplacementTransform(rectangles[2],
                                 colored_rectangles[0].move_to(labels[0], UP).shift(UP * vertical_shift_factor)),
            ReplacementTransform(rectangles[3],
                                 colored_rectangles[1].move_to(labels[1], UP).shift(UP * vertical_shift_factor)),
            ReplacementTransform(VGroup(rectangles[1], rectangles[6], rectangles[7]),
                                 colored_rectangles[2].move_to(labels[2], UP).shift(UP * 1.65)),
            ReplacementTransform(VGroup(rectangles[0], rectangles[4], rectangles[5], rectangles[9]),
                                 colored_rectangles[3].move_to(labels[3], UP).shift(UP * 2.22)),
            ReplacementTransform(rectangles[8],
                                 colored_rectangles[4].move_to(labels[4], UP).shift(UP * vertical_shift_factor))))
        self.wait()

        right_elements = VGroup(labels[2], labels[3], colored_rectangles[2], colored_rectangles[3])
        self.play(AnimationGroup(right_elements.animate.shift(RIGHT * 2.5)),
                  VGroup(labels[4], colored_rectangles[4]).animate.shift(RIGHT * 3.75))
        self.wait()

        # convert minute to m and shift to center
        self.play(AnimationGroup(
            labels[0][0].animate.shift(RIGHT * horizontal_shift_factor),
            labels[1][0].animate.shift(RIGHT * horizontal_shift_factor),
            labels[2][0].animate.shift(RIGHT * horizontal_shift_factor),
            labels[3][0].animate.shift(RIGHT * horizontal_shift_factor),
            labels[4][0].animate.shift(RIGHT * horizontal_shift_factor),
            labels[0][1].animate.set_opacity(0),
            labels[1][1].animate.set_opacity(0),
            labels[2][1].animate.set_opacity(0),
            labels[3][1].animate.set_opacity(0),
            labels[4][1].animate.set_opacity(0),
            Write(labels[5].next_to(labels[1], RIGHT).shift(RIGHT * horizontal_shift_factor)),
            Write(labels[6].next_to(labels[2], LEFT).shift(LEFT * horizontal_shift_factor * 1.5)),
            Write(labels[7].next_to(labels[4], LEFT).shift(LEFT * horizontal_shift_factor))
        ))
        self.wait()
        histogram1 = VGroup(coordinates, colored_rectangles, y_labels, y_label_lines)
        for i in range(0, len(labels)):
            histogram1.add(labels[i][0])
        self.wait()
        self.play(histogram1.animate.scale(0.7).move_to(LEFT * 2).shift(UP * 1.6))
        self.wait()

        histogram2 = BarChart(
            values=[2, 0, 7, 1],
            bar_names=["10-11 " + minute[0], "12-13 " + minute[0], "14-15 " + minute[0], "16-17 " + minute[0]],
            bar_colors=[GREEN, BLACK, YELLOW, RED],
            x_axis_config={"font_size": label_font_size},
            y_range=[0, 7, 1],
            x_length=13.25,
            bar_fill_opacity=1
        )
        histogram2_dashed_line = DashedLine((-6.45, 0.01, 0), (-1.2, 0.01, 0), stroke_width=axis_width)

        self.play(DrawBorderThenFill(histogram2.scale(0.7).next_to(histogram1, DOWN).align_to(histogram1, LEFT)))
        self.wait()
        self.play(Write(histogram2_dashed_line))
        self.wait()

    def set_up(self, add=False):
        self.text = text
        self.january = text.january
        self.february = text.february
        self.minute = text.minute

    def get_date_and_time_text(self, date_time_data):
        date_and_time = date_time_data[0] + " " + '$\longrightarrow$' + str(date_time_data[1])
        return Tex(date_and_time)
