from lib.constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import youngest, second, third, fourth, fifth, fifth_2
else:
    from .english_text import youngest, second, third, fourth, fifth, fifth_2
