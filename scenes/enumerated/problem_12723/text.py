from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "air_mass_str",
    "moleculs_in_one_gram_str",
    "task_number_str",
    "moleculs_in_ball_str",
    "hat_str"
]
