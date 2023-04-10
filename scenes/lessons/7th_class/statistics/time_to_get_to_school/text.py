from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__ = [
    "january",
    "february",
    "minute",
    "day",
    "time",
    "width",
    "average_time",
    "mode",
    "data_str",
    "count",
    "frequency_table_str"
]

