from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


CONDITION_3 = [r" 1)\ \frac{2}{7} + \frac{2}{7} = ", r" \frac{2 + 2}{7} = ", r"\frac{4}{7}"]
CONDITION_4 = [r" 2)\ 1 - \frac{4}{7} = ", r" \frac{7}{7} - \frac{4}{7} = ", r" \frac{7-4}{7} = ", r" \frac{3}{7}"]
CONDITION_5 = [r" 3)\ 24 : \frac{3}{7} = 24 \cdot \frac{7}{3} = ", r"56"]
