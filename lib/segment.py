from manim import DEFAULT_STROKE_WIDTH
from manim import LEFT, RIGHT, DOWN
from manim import WHITE, YELLOW
from manim import VMobject, VGroup, Line, Dot
from manim import Write, ReplacementTransform
from manim import Scene

from constants import DEFAULT_ENDMARK_LENGTH, DEFAULT_SEGMENT_STROKE_WIDTH
from constants import DEFAULT_EXTRA_SEGMENT_COLOR, DEFAULT_COUNTING_COLOR
from constants import DEFAULT_SEGMENT_TEXT_POSITION


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
        stroke_width=DEFAULT_SEGMENT_STROKE_WIDTH,
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

class ConnectionLine(VMobject):
    def __init__(self, mob_1: VMobject, mob_2: VMobject, dir = DOWN, alpha = 0.5, color=YELLOW, equal_size = False, **kwargs):
        super().__init__(color=color, **kwargs)
        vertex_0 = mob_1.get_edge_center(dir) + alpha/3*dir
        vertex_1 = vertex_0 + alpha*dir
        vertex_2 = Dot(vertex_1).match_x(mob_2).get_center()
        vertex_3 = mob_2.get_edge_center(dir) + alpha/3*dir
        if equal_size:
            a = min[abs((vertex_0-vertex_1)[1]), abs((vertex_3-vertex_2)[1])]
            vertex_0 = vertex_1 - a*dir
            vertex_3 = vertex_2 - a*dir
        self.start_new_path(vertex_0)
        self.add_points_as_corners([vertex_0, vertex_1, vertex_2, vertex_3])
