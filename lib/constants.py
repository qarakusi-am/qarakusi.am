from manim import UP
from manim import WHITE, GREEN, ORANGE, RED, BLUE, YELLOW, PURE_GREEN
from manim import TexTemplate, Tex, MathTex

# Հիմնական գույներ
COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW]


# Մասերով խնդիրների հաստատուններ
DEFAULT_ENDMARK_LENGTH = 0.2
DEFAULT_SEGMENT_TEXT_POSITION = 0.75 * UP

DEFAULT_EXTRA_SEGMENT_COLOR = PURE_GREEN
DEFAULT_COUNTING_COLOR = ORANGE

DEFAULT_TASK_FONT_SIZE = 35
DEFAULT_TASK_NUMBER_FONT_SIZE = 40
DEFAULT_NAME_FONT_SIZE = 40
DEFAULT_SEGMENT_LENGTH_FONT_SIZE = 50
DEFAULT_TOTAL_LENGTH_FONT_SIZE = 70
DEFAULT_EQUATION_FONT_SIZE = 50


# Կշեռքով խնդիրների հաստատուններ
DEFAULT_SCALES_BUFF = 0

# Ամիսներ, շաբաթներ, օրեր
MONTHS_ARM = [
    'Հունվար',
    'Փետրվար',
    'Մարտ',
    'Ապրիլ',
    'Մայիս',
    'Հունիս',
    'Հուլիս',
    'Օգոստոս',
    'Սեպտեմբեր',
    'Հոկտեմբեր',
    'Նոյեմբեր',
    'Դեկտեմբեր'
]

MONTHS_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

WEEK_DAYS_ARM = ['ԵԿ', 'ԵՔ', 'ՉՈ', 'ՀԻ', 'Ու', 'ՇԱ', 'ԿԻ']
WEEK_DAYS_ARM_LONG = ['ԵՐԿ', 'ԵՐՔ', 'ՉՐՔ', 'ՀՆԳ', 'ՈւՐԲ', 'ՇԲԹ', 'ԿԻՐ']

WEEK_BLOCK_WIDTH = 0.35
WEEK_BLOCK_HEIGHT = 0.25

# ԽԱՌԸ

DEFAULT_PAPERS_BUFF = 0.125


# Հայերեն գրելու համար tex_template (նույն բանն են)
XELATEX_preamble = r"""
\usepackage{tikz}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{amsfonts,amssymb,amsthm,mathtools}
\usepackage{amsmath}
\usepackage{upgreek}
\usepackage{mathrsfs}
"""
ARMTEX = TexTemplate('xelatex', '.pdf', preamble=XELATEX_preamble)
ENGTEX = ARMTEX

class LanguageConfig:
    language = 'armenian'

    Tex.set_default(tex_template=ARMTEX)
    MathTex.set_default(tex_template=ARMTEX)

    @classmethod
    def set_language(cls, language):
        if language == 'english':
            Tex.set_default(tex_template=ENGTEX)
            MathTex.set_default(tex_template=ENGTEX)
        elif language == 'armenian':
            Tex.set_default(tex_template=ARMTEX)
            MathTex.set_default(tex_template=ARMTEX)
        cls.language = language

    @classmethod
    def is_armenian(cls):
        return cls.language == 'armenian'
