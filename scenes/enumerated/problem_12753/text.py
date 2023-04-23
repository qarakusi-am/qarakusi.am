from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


QUESTION_MARK = r"\mathord{?}"
CONDITION_6 = ["1", "9"]
PLUS = "+"
TWO = "2"
ZERO = "0"
ONE = "1"
FOUR = "4"
