from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


NUMS_1 = ["61", "24", "7", "599"]
NUMS_2 = ["2", "4", "6", "1", "5", "9", "9", "7"]
NUMS_3 = ["7", "6", "1", "2", "4", "5", "9", "9"]
# NUMS_3 = ["7", "6", "1", "2", "4", "5", "9", "9"]
QUESTION_MARK = r"\mathord{?}"

CONDITION_4_1 = r"\text{49170239715}"
CONDITION_4_2 = r"\text{89170239715}"
CONDITION_4_3 = r"\text{84170239715}"
CONDITION_4_4 = r"\text{84970239715}"
CONDITION_4_5 = r"\text{84910239715}"
CONDITION_4 = r"\text{8 4 9 1 7 0 2 3 9 7 1 5}"
CONDITION_6 = r"\text{8 } > \text{ 4 }"
CONDITION_7 = r"\text{9 } > \text{ 4 }"
FOUR = r"4"
