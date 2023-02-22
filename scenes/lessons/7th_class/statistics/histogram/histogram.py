import numpy as np
from manim import  DOWN, RIGHT, WHITE, LEFT, UP, BLACK,MobjectTable, PI,GREEN,RED,Table
from manim import Tex, Wiggle,AnimationGroup, ReplacementTransform, VGroup, Brace
from manim import  FadeOut, Write
from manim import Scene
from . import text

from .text import *
UNIT = 0.27

class Histogram(Scene):
    def construct(self):
        self.set_up()
        data_table1 = [
            [january + '30','15' + minute],
            [january + '31','10' + minute],
            [february + '1', '15' + minute],
            [february + '2', '14' + minute],
            [february + '3', '17' + minute]
        ]
        data_table2 = [
            [february + '6', '14' + minute],
            [february + '7', '11' + minute],
            [february + '8', '15' + minute],
            [february + '9', '14' + minute],
            [february + '10', '15' + minute]
        ]



        table1 = Table(
            data_table1,
            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )
        table2 = Table(
            data_table2,

            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )
        table1.set_color(WHITE).scale(0.5).move_to(LEFT*2)
        table2.set_color(WHITE).next_to(table1,RIGHT).align_to(table1,RIGHT).scale(0.5)
        self.play(AnimationGroup(table1.create(),table2.create()))
        self.wait()

    def set_up(self, add = False):
        self.text = text
        self.january=text.january
        self.february=text.february
        self.minute=text.minute



