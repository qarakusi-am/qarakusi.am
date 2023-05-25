from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

TRANSFORM_1 = r"1 \cdot 2 ,"
TRANSFORM_2 = r"2 \cdot 2 ,"
TRANSFORM_3 = r"3 \cdot 2 ,"
TRANSFORM_4 = r"4 \cdot 2 ,"
TRANSFORM_5 = r"5 \cdot 2 ,"
TRANSFORM_6 = r"6 \cdot 2"
MULTIPOINT = r"..."
FOR_49 = r"49 \cdot 2"
NUM_49 = r"49"
TRANSFORM_7 = r"1 \cdot 3,"
TRANSFORM_8 = r"2 \cdot 3,"
TRANSFORM_9 = r"3 \cdot 3,"
TRANSFORM_10 = r"4 \cdot 3"
FOR_33 = r"33 \cdot 3"
NUM_33 = r"33"
CONDITION_2 = [r" 6\cdot ", r"16", r" = 96"]
NUM_17 = r"17"
RESULT = ["17", " + ", "33", " = 50"]
