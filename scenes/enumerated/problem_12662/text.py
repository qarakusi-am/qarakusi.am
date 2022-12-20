from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "taskNumberString",
    "mianish_str",
    "erknish_str",
    "table_col_label1_str",
    "table_col_label2_str",
    "table_col_label3_str",
    "table_col_label4_str",
    "top_left_entry_str",
    "total_str"
]