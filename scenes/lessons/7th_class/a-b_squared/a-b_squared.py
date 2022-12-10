from manim import *

from hanrahashiv import ModifyFormula
from segment import ConnectionLine

class AMinusBSquared(Scene):
    def construct(self):
        self.recap()

    def recap(self):
        fifty_one_squared = Text('')
        self.play(Create(fifty_one_squared, run_time=2))
        self.wait()
