from manim import Tex
from constants import DEFAULT_TASK_NUMBER_FONT_SIZE, DEFAULT_NAME_FONT_SIZE

problem_statement = Tex(
    'Find two numbers, the sum of which is $51$, and the difference is $13$.',
    font_size=DEFAULT_TASK_NUMBER_FONT_SIZE
)
first_name = Tex('First', font_size=DEFAULT_NAME_FONT_SIZE)
second_name = Tex('Second', font_size=DEFAULT_NAME_FONT_SIZE)
part = r'\textrm{part}'
