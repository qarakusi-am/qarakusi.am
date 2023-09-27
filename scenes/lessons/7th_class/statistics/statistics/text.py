from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__ = [
    "minute",
    "day",
    "data",
    "count",
    "total_days_str",
    "bought_a_pie",
    "days_bought_a_pie_str",
    "number_of_pie_bought_days",
    "part"
]
