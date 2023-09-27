from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

all = [
    'taskNumberString',
    'line_passing_through_points_string',
    'and_string'
]
