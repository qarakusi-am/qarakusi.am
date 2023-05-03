from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    'taskNumberString',
    'a_line_through_the_points'
]
