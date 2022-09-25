from manim import *

from constants import ARMTEX, ENGTEX
from objects import SimpleSVGMobject


class ThrowingBall(Scene):
    def construct(self):

# INITS
        ball = SimpleSVGMobject('tennis_ball')
        # self.add(ball)

        arr_1 = Arrow().rotate()
