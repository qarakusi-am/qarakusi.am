from manim import UP, LEFT
from manim import VGroup
from manim import Rectangle
from manim import Tex

class TaskNumberBox(VGroup):
    def __init__(self, text):
        text = Tex(text, font_size=35)
        box = Rectangle(width=text.width+.4, height=text.height+.4, stroke_width=1.5).to_edge(LEFT+UP, buff=.2)
        text.move_to(box.get_center())
        super().__init__(text, box)
