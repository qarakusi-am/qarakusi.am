from manim import Tex
from manim import RIGHT
from manim import GREEN
from manim import SurroundingRectangle
#from hanrahashiv import ExtractExponentInFormula, FormulaModificationsScene
from manim import *
#from qarakusiscene import TaskNumberBox
#from .text import taskNumberString
FONT_SIZE=65

class Problem12649(Scene):
    def construct(self):
        # taskNumber = TaskNumberBox(taskNumberString)
        # self.add(taskNumber)
        # self.wait()
        taskNumber = Rectangle().scale(0.25).to_corner(UL)

        self.add(taskNumber)
        distributive_property = Tex('$a$', '$($', '$b$', '$+$', '$c$', '$)$', '$=$', '$a$', '$b$', '$+$', '$a$', '$c$')
        distributive_property.to_edge(RIGHT)
        self.add(distributive_property)
        uxx = SurroundingRectangle(distributive_property, color=GREEN)
        self.add(uxx)
        
        formulas = VGroup(
            MathTex('2', 'x', r'\cdot', '(', '3', 'x', '^2', '+',  '1', ')', font_size=FONT_SIZE).next_to(2*UP + 6.5*LEFT, buff=0.2),
            MathTex(r'\frac{5}{3}', 'x', r'\cdot', '(', '6', 'x', '^3', '+', '2', 'x', 'y', '^2', ')', font_size=FONT_SIZE).next_to(1*UP + 6.5*LEFT, buff=0.2),
            MathTex('a', '^2', 'b', '^3', r'\cdot', '(', '2', 'a', 'b', 'c', '+', 'b', '^2', ')', font_size=FONT_SIZE).next_to(6.5*LEFT, buff=0.2),
            MathTex('2', 'x', 'y', r'\cdot', r'\left(', '(', 'x', '^2', 'y', ')', '^3', '+', '3', 'x', 'y', r'\right)', font_size=FONT_SIZE).next_to(DOWN + 6.5*LEFT, buff=0.2))
        
        numbers = VGroup(*[MathTex(f'{i+1})', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3).shift(0.1*DOWN) for i in range(4)]).align_to(taskNumber, LEFT)
        formulas[0].align_to(numbers[0], DOWN)
        self.play(AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5), run_time = 4)
        self.wait()