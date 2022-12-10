from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import paragic_str, makeres_str
else:
    from .english_text import paragic_str, makeres_str
