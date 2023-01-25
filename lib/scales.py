from objects import Scales
from manim import PI

def RotateTheScales(scales : Scales, direction=1, angle=PI/14):
    return scales.rotating_part.animate.rotate(direction * angle, about_point=scales.rotation_dot.get_center())
