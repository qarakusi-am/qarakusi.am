from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

CONDITION_1 = [r"2 \frac{13}{28}", r"\cdot", r" 1 \frac{19}{23}"]
CONDITION_2 = [r" = \frac{2 \cdot 28 + 13}{28}}", r"=", r" \frac{69}{28}"]
CONDITION_3 = [r" = \frac{1 \cdot 23 + 19}{23}} =", r" \frac{42}{23}"]
CONDITION_5 = [r" = \frac{69 \cdot 42}{28 \cdot 23}" , r" = \frac{2898}{644}", r" = 4 \frac{1}{2}"]


PLUS = r"\text{ + }"
EQUAL= r"\text{=}"
SOLUTION_PART_1 = r"\frac{4}{12} \text{ + } \frac{3}{12} \text{ = } \frac{4 \text{ + } 3}{12} \text{ = } \frac{7}{12}"
SOLUTION_PART_2 = r"\text{ 1 - } \frac{7}{12} \text{ = } \frac{12}{12} \text{ - } \frac{7}{12} " \
                  r"\text{ = } \frac{12 \text{ - } 7}{12} \text{ = } }"
FIVE_TWELFTH = r" \frac{5}{12}}"
RESULT_0 = r"\text{ = 5} \cdot \frac{12}{1} \text{ = }"
