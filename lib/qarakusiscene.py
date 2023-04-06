from manim import UP, LEFT
from manim import VGroup
from manim import Rectangle
from manim import Tex

from manim import FadeIn
from manim import NumberPlane
from manim import Scene
from manim import TEAL


class TaskNumberBox(VGroup):
    def __init__(self, text):
        text = Tex(text, font_size=35)
        box = Rectangle(width=text.width+.4, height=text.height+.4, stroke_width=1.5).to_edge(LEFT+UP, buff=.2)
        text.move_to(box.get_center())
        super().__init__(text, box)


class QarakusiScene(Scene):
    """A class for qarakusi scene
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
