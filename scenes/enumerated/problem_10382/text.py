from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import arshak_str, levon_str, toy_str, missing_str
else:
    from .english_text import arshak_str, levon_str, toy_str, missing_str



