from manim import Tex
from constants import DEFAULT_TASK_NUMBER_FONT_SIZE
from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import problem_statement, first_name, second_name, part
else:
    from .english_text import problem_statement, first_name, second_name, part


problem_number = Tex('$\\#10674$', font_size=DEFAULT_TASK_NUMBER_FONT_SIZE)

extra_length = 13
total_length = 51
