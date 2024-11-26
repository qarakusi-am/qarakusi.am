from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = ['taskNameString',
         'meters_second',
         'sec',
         'ball_line_distance']