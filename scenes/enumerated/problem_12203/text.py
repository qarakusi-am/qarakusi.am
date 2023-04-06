from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


QUESTION_MARK = r"\mathord{?}"
ADDITION_TO_CONDITION_1 = ["3", "18"]
ADDITION_TO_CONDITION_2 = ["2", "14"]
ADDITION_TO_CONDITION_3 = ["5", "32"]
