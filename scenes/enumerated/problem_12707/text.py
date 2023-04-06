from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "task_number_str",
    "condition1_str",
    "condition2_str",
    "condition3_str",
    "page_str",
    "first_solution_str",
    "second_solution_str",
]
