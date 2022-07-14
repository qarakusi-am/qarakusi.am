from manim import UP, LEFT, RIGHT, ORIGIN, PI, DEFAULT_STROKE_WIDTH
from manim import VMobject, VGroup, Line
from manim import TexTemplate, MathTex
from manim import always_redraw
import numpy as np

# np վեկտորների համար ՛մեթոդներ՛

def length(array):
    array = np.array(array)
    return np.matmul(array.transpose(), array) **(1/2)

def normalized_vector(array):
    array = np.array(array)
    return (1/length(array)) * array


def rotate2angle(array, alpha):
    array = np.array(array)
    rotation__matrix = [
        [np.cos(alpha), -np.sin(alpha), 0],
        [np.sin(alpha), np.cos(alpha), 0],
        [0, 0, 1],
    ]
    return np.matmul(rotation__matrix, array)

def normal(array):
    array = np.array(array)
    return normalized_vector(rotate2angle(array, PI/2))

# հայերեն լեզվով LaTeX աշխատացնելու համար

XELATEX_preamble = r"""
\usepackage{tikz}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage{amsfonts,amssymb,amsthm,mathtools}
\usepackage{amsmath}
\usepackage{upgreek}
\usepackage{mathrsfs}
"""
XELATEX = TexTemplate('xelatex', '.pdf', preamble=XELATEX_preamble)


ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(
    r"""\usepackage{armtex}
\usepackage{xcolor}
"""
)

# Մասերով խնդրի համար

DEFALT_EDGE_HIGHT = 0.2
DEFAULT_LABEL_FONT_SIZE = 50



class Segment(VGroup):
    def __init__(
            self,
            start = 0.5 * LEFT,
            end  = 0.5 * RIGHT,
            label = None,
            label_font_size = DEFAULT_LABEL_FONT_SIZE,
            **kwargs
        ):
        start = np.array(start)
        end = np.array(end)
        normal_direction = normal(end-start)

        if 'stroke_width' in kwargs:
            stroke_width = kwargs['stroke_width']
        else:
            stroke_width = DEFAULT_STROKE_WIDTH

        if 'edge_hight' in kwargs:
            edge_hight = kwargs['edge_hight']
            del kwargs['edge_hight']
        else:
            edge_hight = DEFALT_EDGE_HIGHT
        
        self.line = Line(start, end, buff=0, **kwargs)

        self.left_edge = always_redraw(
            lambda: Line(
                ORIGIN,
                edge_hight * stroke_width / 5 * normal_direction,
                **kwargs
            ).move_to(self.line.get_left())
        )
        self.right_edge = always_redraw(
            lambda: Line(
                ORIGIN,
                edge_hight * stroke_width / 5 * normal_direction,
                **kwargs
            ).move_to(self.line.get_right())
        )
        
        super().__init__(self.line, self.left_edge, self.right_edge)

        
        self.label = VMobject()
        if label != None:
            label = MathTex(label, font_size = label_font_size, tex_template = ARMTEX)
            self.set_label(label)

    def set_label(self, label):
        self.label.become(label)
        self.update_label_pos()

    def update_label_pos(self, buff = 0.05, direction = UP):
        self.label.next_to(self, direction, buff)
        return self.label
