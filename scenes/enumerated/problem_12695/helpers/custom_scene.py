from manim import FadeIn
from manim import Axes, NumberPlane
from manim import Scene
from manim import TEAL

from lib.qarakusiscene import TaskNumberBox


class CustomScene(Scene):
    def add_plane(self):
        plane = NumberPlane(background_line_style={"stroke_color": TEAL,
                                                   "stroke_width": 2,
                                                   "stroke_opacity": 0.1}
                            ).set_opacity(0.2)
        self.add(plane)

    def add_task_number(self, text):
        task_number = TaskNumberBox(text)
        self.play(FadeIn(task_number))
        self.wait(0.5)
