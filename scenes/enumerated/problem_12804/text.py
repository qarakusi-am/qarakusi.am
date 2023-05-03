from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "taskNumberString",
    "problem_setting_1_part_1",
    "problem_setting_1_part_2",
    "problem_setting_2_part_1",
    "problem_setting_2_part_2",
    "problem_setting_part3",
    "book_count_x",
    "solution_str"

]
