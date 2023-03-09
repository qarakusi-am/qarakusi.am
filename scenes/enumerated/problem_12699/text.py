from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

PLUS = r"\text{ + }"
EQUAL= r"\text{=}"
SOLUTION_PART_1 = r"\frac{4}{12} \text{ + } \frac{3}{12} \text{ = } \frac{4 \text{ + } 3}{12} \text{ = } \frac{7}{12}"
SOLUTION_PART_2 = r"\text{ 1 - } \frac{7}{12} \text{ = } \frac{12}{12} \text{ - } \frac{7}{12} " \
                  r"\text{ = } \frac{12 \text{ - } 7}{12} \text{ = } }"
FIVE_TWELFTH = r" \frac{5}{12}}"
RESULT_0 = r"\text{ = 5} \cdot \frac{12}{1} \text{ = }"
CONDITION_1 = r"\frac{1}{3}"
CONDITION_2 = r"\frac{1}{4}"
