from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import meters_second
else:
    from .english_text import meters_second

__all__ = [
    "meters_second",
]
