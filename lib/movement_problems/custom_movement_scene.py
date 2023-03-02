from manim import FadeIn
from manim import NumberPlane
from manim import Scene
from manim import TEAL

from lib.qarakusiscene import TaskNumberBox


class CustomMovementScene(Scene):
    """A class for custom movement scene
       --Methods
           add_plane()
               add to screen coordinate system
           add_task_number
               takes in text module content, get task number and add to scene with wait(0.5)"""
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
