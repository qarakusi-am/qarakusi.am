from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

CDOT = r"\cdot"
CONDITION_2 = r"\text{ = 5}"
CONDITION_3 = r"\text{ = 6}"
CONDITION_4 = r"\text{6 = 3} \cdot \text{2}"
CONDITION_5 = r"\text{,1,1}"
CONDITION_6 = r"\text{,}"
CONDITION_7 = r"\text{,1}"
NUMS_1 = ["1", "1", "5"]
NUMS_2 = ["115", "151", "511"]
NUMS_3 = "116,161,611"
NUMS_4 = ["123,132,213,", "231,312,321"]
