from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

TRANSFORM_1 = r"2 \cdot 1 ,"
TRANSFORM_2 = r"2 \cdot 2 ,"
TRANSFORM_3 = r"2 \cdot 3 ,"
TRANSFORM_4 = r"2 \cdot 4 ,"
TRANSFORM_5 = r"2 \cdot 5 ,"
TRANSFORM_6 = r"2 \cdot 6"
MULTIPOINT = r"..."
FOR_49 = r"2 \cdot 49"
NUM_49 = r"49"
TRANSFORM_7 = r"3 \cdot 1"
TRANSFORM_8 = r"3 \cdot 2"
TRANSFORM_9 = r"3 \cdot 3"
TRANSFORM_10 = r"3 \cdot 4"
TRANSFORM_11 = r"3 \cdot 5"
FOR_33 = r"3 \cdot 33"
NUM_33 = r"33"
CONDITION_2 = [r" 6\cdot ", r"16", r" = 96"]
NUM_17 = r"17"
RESULT = r"33 + 17 = 50"
