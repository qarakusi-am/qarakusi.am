from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__=[
    "taskNumberString",
    "parallel_lines_have_the_same_slope"

]
