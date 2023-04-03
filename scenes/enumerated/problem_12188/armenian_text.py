TASK_NUMBER_STR = "Խ. 12188"
CONDITION_1 = r"\text{Եռանիշ թիվ}"
CONDITION_8 = r"\text{ընդամենը 3+6=9 թիվ}"

from manim import MathTex, ORANGE, PURE_GREEN

condition_8 = MathTex(CONDITION_8).move_to([0, -3.1, 0]).scale(1.75)
condition_8[0][8].set_color(ORANGE)
condition_8[0][10].set_color(PURE_GREEN)
