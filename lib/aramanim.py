from manim import UP, DOWN, LEFT, RIGHT, ORIGIN, OUT, PI, DEFAULT_STROKE_WIDTH
from manim import VMobject, VGroup, Line
from manim import TexTemplate, MathTex
from manim import FadeIn, FadeOut, Animation, Scene
from manim import always_redraw
import numpy as np
from numpy import linalg as la
from objects import Scissors, Stopwatch

from utilities import normal_vector

# Մասերով խնդրի համար
DEFAULT_EDGE_HEIGHT = 0.2
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
        normal_direction = normal_vector(end-start)
        if 'stroke_width' in kwargs:
            stroke_width = kwargs['stroke_width']
        else:
            stroke_width = DEFAULT_STROKE_WIDTH
        if 'edge_hight' in kwargs:
            edge_hight = kwargs['edge_hight']
            del kwargs['edge_hight']
        else:
            edge_hight = DEFAULT_EDGE_HEIGHT        
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
            label = MathTex(label, font_size = label_font_size)
            self.set_label(label)

    def set_label(self, label):
        self.label.become(label)
        self.update_label_pos()

    def update_label_pos(self, buff = 0.05, direction = UP):
        self.label.next_to(self, direction, buff)
        return self.label


### մկրատի անիմացիաներ (Scissors) ###
class CutIn(FadeIn):
    def __init__(self, mobject: Scissors, **kwargs):
        super().__init__(mobject, **kwargs)
    def interpolate(self, alpha: float):
        if self.rate_func(alpha) < 0.5:
            angle = (PI / 6) * self.rate_func(alpha)
            self.mobject.set_opacity(2*self.rate_func(alpha))
        else:
            angle = (PI / 6) * (1-self.rate_func(alpha))
        self.mobject.become(self.starting_mobject)
        self.mobject.open(angle)
        self.mobject.shift(0.5*UP*self.rate_func(alpha))
    def clean_up_from_scene(self, scene: Scene) -> None:
        scene.add(self.mobject)


class CutOut(FadeOut):
    def __init__(self, mobject: Scissors, **kwargs):
        super().__init__(mobject, **kwargs)
    def interpolate(self, alpha: float):
        if self.rate_func(alpha) > 0.5:
            self.mobject.set_opacity(2*(1-self.rate_func(alpha)))
        angle = (PI / 9) * self.rate_func(alpha)
        self.mobject.become(self.starting_mobject)
        self.mobject.open(angle)
        self.mobject.shift(0.5*DOWN*self.rate_func(alpha))
    def clean_up_from_scene(self, scene: Scene) -> None:
        scene.remove(self.mobject)

### մկրատի անիմացիաներ (Scissors) END ###

### ժամացույցի անիմացիա  ###
class Run(Animation):
    def __init__(
        self,
        mobject: Stopwatch,
        speed=1,
        run_time =1,
        dirt = 1,
        **kwargs
    ) -> None:
        super().__init__(
            mobject,
            run_time = run_time,
            **kwargs
        )
        self.radians = 2 * PI * speed * run_time / 60 * dirt
        self.time_passed = speed * run_time * dirt
        self.about_point = mobject.stopwatch.get_center()
        self.shift_resetter = 0.3 * (
            np.array(mobject.stopwatch_resetter.get_center())
            - np.array(mobject.stopwatch.get_edge_center(UP))
        )

    def interpolate(self, alpha: float) -> None:
        if alpha < 0.1:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - (10*alpha) * self.shift_resetter
            )
        if alpha >= 0.9 and alpha <=1:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - (10*(1-alpha)) * self.shift_resetter
            )
        self.mobject.stopwatch_arrow.become(
            self.starting_mobject.stopwatch_arrow
        )
        self.mobject.stopwatch_arrow.rotate(
            -self.rate_func(alpha) * self.radians,
            axis=OUT,
            about_point=self.about_point
        )
        self.mobject.time.set_value(
            self.starting_mobject.time.get_value()
            + self.rate_func(alpha) * self.time_passed
        )

class Reset(Animation):
    def __init__(
        self,
        mobject: Stopwatch,
        **kwargs
    ) -> None:
        super().__init__(mobject, run_time=0.4, **kwargs)
        self.shift_resetter = 0.3 * (
            np.array(mobject.stopwatch_resetter.get_center())
            - np.array(mobject.stopwatch.get_edge_center(UP))
        )
        self.radians = 2*PI*(mobject.time.get_value()%60)/60
        self.about_point = mobject.stopwatch.get_center()
    def interpolate(self, alpha):
        if alpha < 0.25:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - self.rate_func(4*alpha) * self.shift_resetter
            )
        if alpha >= 0.25 and alpha < 0.5:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - self.rate_func(4*(0.5-alpha)) * self.shift_resetter
            )
        if alpha >= 0.5 and alpha < 0.75:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - self.rate_func(4*(0.75-alpha)) * self.shift_resetter
            )
        if alpha >= 0.75:
            self.mobject.stopwatch_resetter.move_to(
                self.starting_mobject.stopwatch_resetter.get_center()
                - self.rate_func(4*(1-alpha)) * self.shift_resetter
            )
        self.mobject.stopwatch_arrow.become(self.starting_mobject.stopwatch_arrow)
        self.mobject.stopwatch_arrow.rotate(
            self.rate_func(alpha) * self.radians,
            axis=OUT,
            about_point=self.about_point
        )
        self.mobject.time.set_value(0)

### ժամացույցի անիմացիա  END ###
