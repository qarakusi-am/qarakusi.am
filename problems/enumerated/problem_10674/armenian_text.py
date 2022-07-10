from manim import Tex
from constants import DEFAULT_TASK_NUMBER_FONT_SIZE, DEFAULT_NAME_FONT_SIZE

problem_statement = Tex(
    'Գտնել երկու թիվ, որոնց գումարը $51$ է,',
    'իսկ տարբերությունը՝ $13$։',
    font_size=DEFAULT_TASK_NUMBER_FONT_SIZE
)
first_name = Tex('Առաջին', font_size=DEFAULT_NAME_FONT_SIZE)
second_name = Tex('Երկրորդ', font_size=DEFAULT_NAME_FONT_SIZE)
part = r'\textrm{մաս}'
