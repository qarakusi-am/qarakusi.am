TASK_NUMBER_STR = "P. 12188"
CONDITION_1 = r"\text{A three-digit number}"
CONDITION_8 = r"\text{total 3+6=9 numbers}"

from manim import MathTex, ORANGE, PURE_GREEN

condition_8 = MathTex(CONDITION_8).move_to([0, -3.1, 0]).scale(1.75)
condition_8[0][5].set_color(ORANGE)
condition_8[0][7].set_color(PURE_GREEN)
