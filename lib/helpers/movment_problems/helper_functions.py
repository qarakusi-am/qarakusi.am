from manim import MathTex
from manim import BraceBetweenPoints
from manim import rate_functions
from manim import DOWN, UP, LEFT, RIGHT


def brace_with_text(text: str, points: tuple, brace_shift=(0.1 * UP), text_shift=(0.7 * DOWN)):
    brace = BraceBetweenPoints(points[0], points[1], direction=DOWN).shift(brace_shift)
    brace_text = MathTex(text).move_to(brace).shift(text_shift).scale(1.2)
    return brace, brace_text


def obj_movement(obj, move_to_point, run_time=1):
    res = obj.animate(rate_func=rate_functions.linear, run_time=run_time).move_to(
        move_to_point, aligned_edge=RIGHT).shift(0.05 * LEFT + 0.3 * UP)
    return res
