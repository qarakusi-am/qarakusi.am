from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import first, second, goose_weight, duck_weight
else:
    from .english_text import first, second, goose_weight, duck_weight

