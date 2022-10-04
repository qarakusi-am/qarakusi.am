from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import (
        condition_1_string,
        condition_2_string,
        three_times_more_list,
        in_total_list)
else:
    from .english_text import (
        condition_1_string,
        condition_2_string,
        three_times_more_list,
        in_total_list)
