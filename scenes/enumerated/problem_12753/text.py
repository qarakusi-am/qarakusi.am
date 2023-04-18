from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


QUESTION_MARK = r"\mathord{?}"
CONDITION_6 = [r"\text{ 1 }", r"\text{ 9 }"]
PLUS = r"+"
TWO = r"2"
ZERO = r"0"
ONE = r"1"
FOUR = r"4"
