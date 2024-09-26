from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *
__all__ = [
    "running_time",
    "speed_in_km_h",
    "minute",
    "rest_time",
    "walk_back_speed",
    "km",
    "meter",
    "minute",
    "hour",
    "second",
    "run",
    "rest"
]




