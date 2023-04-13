from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__=[
    "taskNumberString",
    "condition1",
    "condition2",
    "condition3",
    "condition4",
    "condition5",
    "condition6",
    "abscissa_str"
]
