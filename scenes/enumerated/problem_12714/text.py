from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__ = [
    "taskNumberString",
    "is_solution",
    "equation_doesnt_have_solution_when",
    "where",
    "doesnt_have_solution"
]
