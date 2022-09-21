from objects import Scales
from manim import Scene, PI

class ScalesScene(Scene):

    def rotate_scales(self, scales : Scales, direction=1, angle=PI/14):

        self.play(scales.rotating_part.animate.rotate(direction * angle, about_point=scales.rotation_dot.get_center()))


    


