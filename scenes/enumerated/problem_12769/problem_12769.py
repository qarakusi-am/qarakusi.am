from manim import Write, VGroup, AnimationGroup, ReplacementTransform
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, TransformFromCopy, Brace
from manim import Scene, RIGHT, LEFT, UP, DOWN, ORANGE, WHITE, BLUE_C
from .text import *
from qarakusiscene import TaskNumberBox

FONT_SIZE = 60
DOT_SIZE= 40

class Problem12769(Scene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)

        coordinate_axes = Axes(
            x_range=[-5.5, 5.3, 1],
            y_range=[-5.5, 15.3, 1],
            x_length=10,
            y_length=10,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        )
        self.play(Write(coordinate_axes))
        self.wait()

        conditions = VGroup(
            Tex(condition1, font_size=FONT_SIZE).align_to(taskNumber,LEFT).shift(DOWN),

        )
        self.play(Write(conditions[1]))
        self.wait()


