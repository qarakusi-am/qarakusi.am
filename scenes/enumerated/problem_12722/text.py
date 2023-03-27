from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__ = [
    "taskNumberString",
    "for_what_value_k",
    "is_a_solution"
]

