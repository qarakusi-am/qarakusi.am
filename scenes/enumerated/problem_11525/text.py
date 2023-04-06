from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

PLUS =  r"\text{+}"
CONDITION_6 = r"\text{1)}"
CONDITION_9 = r"\text{42 - 17}"
CONDITION_11 = r"\text{49 - 25}"
NUMS_1 = ["61", "24", "7", "599"]
NUMS_2 = ["24", "599", "61", "7"]
QUESTION_MARK = r"\mathord{?}"
