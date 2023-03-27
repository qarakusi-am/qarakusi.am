from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "multiples_are",
    "is_a_divisor",
    "numbers_ending_with_0",
    "and_no_other_number_str",
    "number_divisible_by_5_end_with_0_and_5",
    "number_divisible_by_2"

]
