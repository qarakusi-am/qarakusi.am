from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


EQUAL = r"="
BRACKETS_1 = [r"(\; \; \; \;)^", r"n"]
SOLUTION_1_2 = [r"=", r"3^", r"{6n}"]
HINT_1 = r"60=6n"
SOLUTION_1_3 = [r"n=\frac{60}{6}", r"=", r"10"]
BRACKETS_2 = [r"(\; \; \; \; \;)^", r"n"]
HINT_2 = r"60=15n"
SOLUTION_2_3 = r"n=\frac{60}{15}=4"
SOLUTION_3_2 = [r"9^", "n"]
SOLUTION_3_3 = [r"9=3\cdot 3= ", r"3^2"]
SOLUTION_3_4 = [r"=(3^2)^", "n"]
SOLUTION_3_5 = r"60=2n"
SOLUTION_3_6 = r"n=\frac{60}{2}=30"
SOLUTION_4_1 = [r"3^{60}=", "27^n"]
SOLUTION_4_2 = [r"(3^3)^","n"]
SOLUTION_4_3 = r"n=\frac{60}{3}=20"
