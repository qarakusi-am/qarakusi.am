from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "ani_name_str",
    "babken_name_str",
    "metr_str",
    "all_str",
    "ani_area_str",
    "babken_area_str"
]
