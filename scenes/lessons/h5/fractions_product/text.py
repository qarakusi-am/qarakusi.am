from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *

CONDITION_1 = [r"2 \frac{13}{28}", r"\cdot", r" 1 \frac{19}{23}"]
CONDITION_2 = [r" = \frac{2 \cdot 28 + 13}{28}}", r"=", r" \frac{69}{28}"]
CONDITION_3 = [r" = \frac{1 \cdot 23 + 19}{23}} =", r" \frac{42}{23}"]
CONDITION_5 = [r" = \frac{69 \cdot 42}{28 \cdot 23}" , r" = \frac{2898}{644}", r" = 4 \frac{1}{2}"]
CONDITION_7 = [r" = \frac{3\cdot 3}{2\cdot 1}" , r" = \frac{9}{2}", r" = 4 \frac{1}{2}"]
NUMS = ["1", "2", "3", "3"]
