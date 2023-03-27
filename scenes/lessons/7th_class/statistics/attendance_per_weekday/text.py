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
    "five_consecutive_days",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday"
]
