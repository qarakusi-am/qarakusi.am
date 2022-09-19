from lib.constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import youngest, second, third, fourth, fifth, fifth_2, oldest, property_1, property_2, property_3
else:
    from .english_text import youngest, oldest
