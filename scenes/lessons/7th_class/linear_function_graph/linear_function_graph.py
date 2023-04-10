from manim import SurroundingRectangle, Axes, Dot, CurvedArrow, FadeOut
from manim import Write, AnimationGroup
from manim import  TransformFromCopy
from manim import YELLOW, BLUE, WHITE, ORANGE, GREEN
from manim import RIGHT, LEFT, UP, DOWN
from manim import MathTex,Tex, VGroup, Scene
from text import *
FONT_SIZE = 60
RUN_TIME_SPEED = 2

class LinearFunctionGraph(Scene):
    def construct(self):
        conclusions=VGroup(
            Tex("1) y = 2x + 3",passes_through_point,font_size=FONT_SIZE).to_edge(LEFT+UP),
            Tex("2) y = 2x + 3",is_parallel_to," y = 2x + 3",suffix_for_to,font_size=FONT_SIZE).to_edge(LEFT+UP).shift(DOWN)
        )
        self.play(Write(conclusions))
        self.wait()
