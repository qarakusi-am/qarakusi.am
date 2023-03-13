from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


CONDITION_4 = r"\text{1,2,3,4,5,6,7,8,9}"
CONDITION_6 = r"\text{9 + 9} < {23}"
CONDITION_8 = r"\text{9+9+9} > {23}"
PLUS = r"\text{ + }"
EQUAL_23 = r"\text{ = 23 }"
NINE = r"9"
SOLUTION_PART_1 = r"\text{23 - 9 - 9 = 5 }"
