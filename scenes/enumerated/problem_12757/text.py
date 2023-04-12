from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


SOLUTION_1_2 = r"(n^2)^2"
SOLUTION_1_3 = r"2\cdot 0.5\cdot n^2"
SOLUTION_1_4 = r" + \ 0.5^2"
SOLUTION_1_5 = r"= (n^2)^2 + 2\cdot n^2\cdot 0.5 + 0.5^2 - 0.5^2 + 1"
SOLUTION_1_6 = r"= (n^2+0.5)^2 + 0.75"
SOLUTION_2_2 = r"=n^4+(2n^2-n^2) + 1"
SOLUTION_2_3 = r" (n^2)^2 + 2\cdot n^2\cdot 1 + 1^2"
SOLUTION_2_4 = r"(n^2+1)^2"
SOLUTION_2_5 = r"=(n^2+1)^2 - n^2"
SOLUTION_2_6 = r"(n^2+1-n)(n^2+1+n)"
SOLUTION_3_2 = r"=n^4+4n^2+4-4n^2"
SOLUTION_3_3 = r"=(n^2+2)^2 - 4n^2"
SOLUTION_3_4 = r"(2n)^2"
SOLUTION_3_5 = r"=(n^2+2-2n)(n^2+2+2n)"
EQUAL = r"="
