from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


CONDITION_2 = ["4\ ", "9\ ", "1\ ", "3"]
CONDITION_4_1 = r"\text{49170239715}"
CONDITION_4_2 = r"\text{89170239715}"
CONDITION_4_3 = r"\text{84170239715}"
CONDITION_4_4 = r"\text{84970239715}"
CONDITION_4_5 = r"\text{84910239715}"
CONDITION_4 = r"\text{8 4 9 1 7 0 2 3 9 7 1 5}"
CONDITION_6 = r"\text{8 } > \text{ 4 }"
CONDITION_7 = r"\text{9 } > \text{ 4 }"
QUESTION_MARK = r"\mathord{?}"
FOUR = r"4"
NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
