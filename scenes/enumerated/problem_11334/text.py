from lib.constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import youngest, oldest
else:
    from .english_text import youngest, oldest
