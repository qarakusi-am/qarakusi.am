from manim import MathTex
from manim import BraceBetweenPoints
from manim import rate_functions
from manim import DOWN, UP, LEFT, RIGHT
from manim import WHITE


def down_brace_with_text(text: str, points: tuple, color=WHITE, brace_shift=(0.1 * UP), text_shift=(0.7 * DOWN)):
    """Parameters:
           text: str
           points: tuple
           color: str
           brace_shift: step
           text_shift: step
       Returns:
           down_brace_with_text (tuple): down_brace_with_text"""
    brace = BraceBetweenPoints(points[0], points[1], direction=DOWN).shift(brace_shift)
    brace_text = MathTex(text, color=color).move_to(brace).shift(text_shift).scale(1.2)
    return brace, brace_text

def up_brace_with_text(text: str, points: tuple, color=WHITE, brace_shift=(0.1 * DOWN), text_shift=(0.5 * UP)):
    """Parameters:
           text: str
           points: tuple
           color: str
           brace_shift: step
           text_shift: step
       Returns:
           up_brace_with_text (tuple): up_brace_with_text"""
    brace = BraceBetweenPoints(points[0], points[1], direction=UP).shift(brace_shift)
    brace_text = MathTex(text, color=color).move_to(brace).shift(text_shift).scale(1.2)
    return brace, brace_text


def obj_movement(obj, move_to_point, run_time=1):
    """Parameters:
           obj: object
           move_to_point: point to where object must be moved
           run_time: execution time
       Returns:
           obj_movement (obj): moved object"""
    res = obj.animate(rate_func=rate_functions.linear, run_time=run_time).move_to(
        move_to_point, aligned_edge=RIGHT).shift(0.05 * LEFT + 0.3 * UP)
    return res
