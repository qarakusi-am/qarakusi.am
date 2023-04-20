from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "linear_function_str",
    "passes_through_point",
    "is_parallel_to_line",
    "is_parallel_to_line_and_passes_through_point"
]