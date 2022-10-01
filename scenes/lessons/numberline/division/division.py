from manim import UP, DOWN, RIGHT, LEFT, ORIGIN, DR, UL, BLACK, BLUE, LIGHT_PINK, LIGHT_PINK, YELLOW, WHITE, RED, DEGREES, rate_functions
from manim import VMobject, Line, DashedLine, Arrow, VGroup,  Brace, Circle, Triangle, SurroundingRectangle, NumberLine, ArcBetweenPoints
from manim import MathTex, Tex
from manim import ShowPassingFlash, Wiggle, Create, Circumscribe, FadeIn, FadeOut, Write, AnimationGroup, ReplacementTransform, MoveAlongPath, Indicate, UpdateFromAlphaFunc
from manim import Scene
from manim import always_redraw
from aramanim import Segment
from objects import SimpleSVGMobject
from .text import method_1, method_2
import numpy as np

def jump_to(mob, point, run_time = 0.5, hight = 3):
    point_initial = mob.get_center()
    path_template = lambda t: np.array([0, hight*t * (1 - t), 0]) 
    jump_path_liner = lambda t: (1 - t) * point_initial + t * point
    jump_path = lambda t: path_template(t) + jump_path_liner(t)
    jump_path_points = [jump_path(t/(int(run_time * 60) - 1)) for t in range(int(run_time * 60))]
    path = VMobject()
    path.set_points_as_corners(jump_path_points)
    animation = MoveAlongPath(mob, path, run_time=run_time, rate_func = rate_functions.linear)
    return animation

class Division(Scene):
    def construct(self):
        apple = SimpleSVGMobject('green_apple')
        apple.set_color(BLUE)
        thinking = SimpleSVGMobject('thinking_boy_outlines')
        div_8_2 = MathTex('8:2=4')
        tex_method_1 = Tex(method_1)
        tex_method_2 = Tex(method_2)

        VGroup()

