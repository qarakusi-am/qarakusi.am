from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import coordinate_text, number_line_text, step_number_text, left_ruler_text, rigth_ruler_text
else:
    from .english_text import coordinate_text, number_line_text, step_number_text, left_ruler_text, rigth_ruler_text