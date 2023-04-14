from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


NUM_1 = r"16"
NUM_2 = r"64"
A = r"A"
B = r"B"
