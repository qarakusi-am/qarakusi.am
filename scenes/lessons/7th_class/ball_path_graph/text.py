from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import meters_second,time
else:
    from .english_text import meters_second,time

__all__ = [
    "meters_second",
    "time"
]
