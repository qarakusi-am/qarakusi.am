from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import *
else:
    from .english_text import *


NUMS_1 = ["61", "24", "7", "599"]
NUMS_2 = ["24", "599", "61", "7"]
QUESTION_MARK = r"\mathord{?}"
