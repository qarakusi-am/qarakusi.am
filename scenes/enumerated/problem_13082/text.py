from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


OPERATION_1 = [r"x^{2}", r"+", r"14", r"x", r"-", r"32", r"=", r"0"]
OPERATION_1_addition = r"2 \cdot 7"
OPERATION_2 = ["(", "a" , "+", "b", ")^{2}=", "a", "^{2}+", "2", "a", "b", "+", "b", "^{2}"]
