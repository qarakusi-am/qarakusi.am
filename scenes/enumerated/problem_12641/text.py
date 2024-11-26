from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


OPERATION_1 = r" - \, 5 = "
OPERATION_2 = r" : 3 = "
OPERATION_3 = r" + \, 1 = "
OPERATION_4 = [r" \cdot \, 2 ", r"= 20"]
SOLUTION_1 = [r"20 : 2 = ", "10"]
SOLUTION_2 = [r"10 - 1 = ", "9"]
SOLUTION_3 = [r"9 \cdot 3 = ","27"]
SOLUTION_4 = [r"27 + 5 = ", "32"]
NUMS = ["10", "10", "9", "9", "27", "27", "32"]
