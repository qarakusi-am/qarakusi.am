"""

60+70+60+70+60
2*60 + 4*70

5*60 + 6*70 = 720

մյուս արագությունները 70 և 90

"""


prop_a = 60 / 720
prop_b = 70 / 720


from manim import *

class miandam(Scene):
    def construct(self):

# INITS

        road = SVGMobject('../../../../objects/SVG_files/road').set_color(WHITE)

# ANIMATIONS

        self.add(road)

