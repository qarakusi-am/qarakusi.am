from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "task_number_str",
    "task_str",
    "new_task_str",
    "tex1_str"
]
