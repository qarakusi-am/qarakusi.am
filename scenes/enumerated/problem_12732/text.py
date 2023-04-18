from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

__all__ = [
    "taskNumberString",
    "angle_between_clock_hands",
    "right_angle",
    "straight_angle",
]
