from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import coordinate_text, number_line_text
else:
    from .english_text import coordinate_text, number_line_text