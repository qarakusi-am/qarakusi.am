from manim import UP, DOWN, LEFT, RIGHT
from manim import VGroup
from manim import MathTex
from manim import YELLOW
from manim import Scene, Write
from manim import UpdateFromAlphaFunc
from manim import Rectangle
from manim import Tex

class TaskNumberBox(VGroup):
    def __init__(self, text):
        text = Tex(text, font_size=35)
        box = Rectangle(width=text.width+.4, height=text.height+.4, stroke_width=1.5).to_edge(LEFT+UP, buff=.2)
        text.move_to(box.get_center())
        super().__init__(text, box)
