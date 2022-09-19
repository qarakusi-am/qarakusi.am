import numpy as np

from manim import LEFT, RIGHT, SMALL_BUFF, DOWN
from manim import WHITE, LIGHT_GRAY, GREEN
from manim import Tex, MathTex
from manim import VMobject, VGroup, Line, DashedLine, SurroundingRectangle
from manim import BraceLabel
from manim import Write, ReplacementTransform
from manim import Scene

from constants import DEFAULT_ENDMARK_LENGTH, DEFAULT_STROKE_WIDTH
from constants import DEFAULT_EXTRA_SEGMENT_COLOR, DEFAULT_COUNTING_COLOR
from constants import DEFAULT_SEGMENT_TEXT_POSITION
from constants import DEFAULT_SEGMENT_LENGTH_FONT_SIZE
from constants import DEFAULT_TOTAL_LENGTH_FONT_SIZE
from constants import DEFAULT_EQUATION_FONT_SIZE, ARMTEX
from objects import Scissors


class SegmentEndmark(VMobject):
    def __init__(
        self,
        length=DEFAULT_ENDMARK_LENGTH,
        *args,
        **kwargs
    ):
        super().__init__()
        endmark = Line([0, length / 2, 0],
                       [0, -length / 2, 0])

        self.add(endmark)


class Segment(VGroup):
    def __init__(
        self,
        start=LEFT,
        end=RIGHT,
        color=WHITE,
        stroke_width=DEFAULT_STROKE_WIDTH,
        endmark_color=WHITE,
        text=False,
        text_position=DEFAULT_SEGMENT_TEXT_POSITION,
        opacity=1
    ):
        super().__init__()
        self.opacity = opacity

        self.text = text
        self.text_position = text_position

        self.line = Line(start,
                         end,
                         color=color,
                         stroke_width=stroke_width)

        self.endmark_left = SegmentEndmark(length=stroke_width / 20,
                                           color=endmark_color)
        self.endmark_left.next_to(self.line, LEFT, buff=0)

        self.endmark_right = SegmentEndmark(length=stroke_width / 20,
                                            color=endmark_color)
        self.endmark_right.next_to(self.line, RIGHT, buff=0)

        self.add(self.line, self.endmark_left, self.endmark_right)

        self.set_text(text)

    def set_text(
        self,
        new_text,
        scene: Scene = None
    ):
        if scene:
            if self.text:
                scene.play(ReplacementTransform(
                    self.text,
                    new_text.next_to(self, self.text_position))
                )
            else:
                self.text = new_text.next_to(self, self.text_position)
                scene.play(Write(self.text))
        if new_text:
            self.remove(self.text)
            self.text = new_text.next_to(self, self.text_position)
            self.add(self.text)

    def add_text_updater(self):
        if self.text:
            self.remove(self.text)
            self.text.add_updater(
                lambda d: d.next_to(self, self.text_position)
            )
            self.add(self.text)
            self.add(self.text)

    def add_line_updater(self):
        self.remove(self.line)
        self.line.add_updater(
            lambda d: d.become(
                Line(
                    self.endmark_left.get_center(),
                    self.endmark_right.get_center(),
                    color=self.line.get_color()
                ).set_opacity(self.opacity)
                # .set_z_index(endmark.get_z_index_reference_point() - 1)
            )
        )
        self.add(self.line)

    def remove_updater(self):
        self.remove(self.text)
        self.clear_updaters()

    def set_superopacity(self, opacity):
        self.opacity = opacity
