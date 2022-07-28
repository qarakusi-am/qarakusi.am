from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import ani_string, mayrik_string, one_year_after_string, now_string, another_one_year_after_string, two_years_after_string, after_some_years_string, some_years_string
else:
    from .english_text import ani_string, mayrik_string, one_year_after_string, now_string, another_one_year_after_string, two_years_after_string, after_some_years_string, some_years_string



