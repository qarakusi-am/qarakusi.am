from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import polynomial_str
else:
    from .english_text import polynomial_str
