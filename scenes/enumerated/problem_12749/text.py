from constants import LanguageConfig

if LanguageConfig.is_armenian():
    from .armenian_text import taskNumberString
else:
    from .english_text import taskNumberString
__all__=[
    "taskNumberString"
]