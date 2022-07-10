from manim import *
import numpy as np

def length(array: np.array):
    array = np.array(array)
    return np.matmul(array.transpose(), array) **(1/2)

def normalized_vector(array: np.array):
    array = np.array(array)
    return (1/length(array)) * array


def rotate2angle(array: np.array, alpha: float):
    array = np.array(array)
    rotation__matrix = [
        [np.cos(alpha), -np.sin(alpha), 0],
        [np.sin(alpha), np.cos(alpha), 0],
        [0, 0, 1],
    ]
    return(np.matmul(rotation__matrix, array))

def normal(array: np.array):
    array = np.array(array)
    return normalized_vector(rotate2angle(array, PI/2))

### LaTeX

XeLaTeX = TexTemplate(tex_compiler='xelatex', output_format='.pdf')
XeLaTeX.add_to_preamble(
    r"""\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\usepackage[UTF8]{ctex}
"""
)

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(
    r"""\usepackage{armtex}
\usepackage{xcolor}
"""
)

DEFALT_EDGE_HIGHT = 0.2
DEFAULT_LABEL_FONT_SIZE = 50

#class Xelatex(TexTemplate):
#
#    default_documentclass = r"\documentclass[preview]{standalone}"
#    default_preamble = r"""
#\usepackage[english]{babel}
#\usepackage{amsmath}
#\usepackage{amssymb}
#\usepackage{fontspec}
#\setmainfont{DejaVu Serif}
#"""
#    default_placeholder_text = "YourTextHere"
#    default_tex_compiler = "XeLaTeX"
#    default_output_format = ".pdf"
#    default_post_doc_commands = ""

def cutting_convex_object(mob: VMobject, propotion_point_1: float, propotion_point_2: float):
    start = min([propotion_point_1, propotion_point_2])
    end = max([propotion_point_1, propotion_point_2])
    points_set_1 = [mob.point_from_proportion(p) for p in np.linspace(start, end, 120)]
    points_set_2 = [mob.point_from_proportion(p) for p in np.linspace(end, 1, 70)] + [mob.point_from_proportion(p) for p in np.linspace(0, start, 70)]
    mob_style = {
            "stroke_opacity": mob.get_stroke_opacity(),
            "stroke_width": mob.get_stroke_width(),
            "fill_color": mob.get_fill_color(),
            "fill_opacity": mob.get_fill_opacity(),
            "stroke_color": mob.get_stroke_color()
        }
    mob_1 = Polygon(*points_set_1, **mob_style)
    mob_2 = Polygon(*points_set_2, **mob_style)
    return [mob_1, mob_2]

class ConectorCurve(VMobject):
    def __init__(self, start = ORIGIN, end = 2*LEFT + DOWN, dx = 0.05, **kwargs):
        super().__init__(**kwargs)
        start = np.array(start)
        end = np.array(end)
        direction = end - start
        [x, y, z] = direction        
        shift_vector = np.array([y/2, 0, 0])
        circle_origin_1 = start + shift_vector
        n = int(round(PI/2 * length(shift_vector)/ dx))
        circle_1 = [rotate2angle(-shift_vector, -i * PI/(2*n)) + circle_origin_1 for i in range(n)]
        k = int(round(-(x - y)/ dx))
        line = [circle_origin_1 + np.array([0, y/2, 0]) + j*dx*LEFT for j in range(k+1)]
        circle_origin_2 = end - shift_vector
        circle_2 = [rotate2angle(shift_vector, -i * PI/(2*n)) + circle_origin_2 for i in range(n)]
        circle_2 = [circle_2[len(circle_2) - 1 - i] for i in range(len(circle_2))]
        points = circle_1 + line + circle_2
        self.set_points_as_corners(points)

        



### SimpleObject
class Polygonal(VMobject):
    def __init__(self, *vertex_groups, color=BLUE, **kwargs):
        #self.dim = 3
        super().__init__(color=color, **kwargs)

        for vertices in vertex_groups:
            first_vertex, *vertices = vertices
            first_vertex = np.array(first_vertex)

            #self.start_new_path(first_vertex)
            self.set_points_as_corners(
                vertex_groups
            )
    
class Cup(Polygonal):
    def __init__(self, height: float = 4.0, width: float = 2.0, color=WHITE, **kwargs):
        
        super().__init__(UL, DL, DR, UR, color=color, **kwargs)
        self.stretch_to_fit_width(width)
        self.stretch_to_fit_height(height)

class Segment(VGroup):
    def __init__(self, start=0.5*LEFT, end=0.5*RIGHT, label=None, label_font_size=DEFAULT_LABEL_FONT_SIZE, **kwargs):
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

        self.left_edge = always_redraw(lambda: Line(ORIGIN, edge_hight*stroke_width/5*normal_direction, **kwargs).move_to(self.line.get_left()))
        self.right_edge = always_redraw(lambda: Line(ORIGIN, edge_hight*stroke_width/5*normal_direction, **kwargs).move_to(self.line.get_right()))
        super().__init__(self.line, self.left_edge, self.right_edge)

        
        self.label = VMobject()
        if label != None:
            label = MathTex(label, font_size=label_font_size, tex_template=ARMTEX)
            self.set_label(label)

    def set_label(self, label):
        self.label.become(label)
        self.update_label_pos()

    def update_label_pos(self, buff=0.05, direction=UP):
        self.label.next_to(self, direction, buff)
        return self.label

### ComplexObject
class FullCup(VGroup):
    def __init__(self, height: float = 4.0, width: float = 2.0, fullness = [100], cup_color=WHITE, liquid_color = BLUE, **kwargs):
        liquid_color = [liquid_color for _ in range(len(fullness))] if type(liquid_color) is not list else liquid_color
        assert len(liquid_color) == len(fullness), 'lengths of colors list and fullness are mismatching'
        value = 0
        for f in fullness:
            value +=f
        self.cup = Cup(height=height, width=width, color=cup_color)
        rectangles = []
        for i in range(len(fullness)):
                rectangles.append(Rectangle(height= fullness[i] * height/100, width=width, fill_color=liquid_color[i], fill_opacity=0.4, stroke_width=0.01))
        self.liquid = VGroup(*rectangles).arrange(UP, buff=0).align_to(self.cup, DOWN + LEFT)
        self.fullness = ValueTracker(value=value)
        
        super().__init__(self.cup, self.liquid)
        


class Stopwatch(VGroup):
    def __init__(self, **kwargs):
        self.__speed = 1
        self.time = ValueTracker(0)
        self.stopwatch = SVGMobject('stopwatch.svg').set_color(WHITE).scale(1.8)
        self.stopwatch_arrow = SVGMobject('stopwatch_arow.svg')
        self.stopwatch_resetter = SVGMobject('stopwatch_resetter.svg').set_color(WHITE).scale(0.3)
        self.__aligning()
        vmobjects = [self.stopwatch, self.stopwatch_arrow, self.stopwatch_resetter]
        super().__init__(*vmobjects, **kwargs)
    
    def __aligning(self):
        self.stopwatch_arrow.move_to(self.stopwatch.get_center()).shift(0.48*UP+0.01*RIGHT)
        self.stopwatch_resetter.next_to(self.stopwatch, UP, buff=0.05)
    def speedup(self, ratio:float):
        self.__speed *= ratio
    def set_time(self, value = 0):
        self.time.set_value(value=value)
        self.stopwatch_arrow.rotate(
            2 * value/60 * PI,
            axis=OUT,
            about_point=self.stopwatch.get_center()
        )


class Chicken(VGroup):
    def __init__(self, number_of_eggs=1, scale_factor=2, **kwargs):
        self.chicken =SVGMobject('chicken.svg')
        self.eggs =VGroup(*[SVGMobject('egg.svg').scale(0.2).shift(0.3*LEFT).set_z_index(-1) for _ in range(number_of_eggs)])
        vmobjects = [self.chicken, self.eggs]
        super().__init__(*vmobjects, **kwargs)
        self.scale(scale_factor)

class Scissors(VGroup):
    def __init__(self, cut_point, **kwargs):
        self.scissor_1 = SVGMobject('../SVGs/siz_1.svg').set_color(WHITE)
        self.scissor_2 = SVGMobject('../SVGs/siz_2.svg').set_color(WHITE)
        self.dot = Dot().scale(0.2)
        super().__init__(self.scissor_1, self.scissor_2, **kwargs)
        self.arrange(RIGHT, buff=-1.1)
        self.add(self.dot)
        self.scale(0.5)
        
        self.scissor_1.shift(0.08 * DOWN).rotate(angle=-0.03, about_point=self.dot.get_center())
        self.scissor_2.shift(0.08 * DOWN).rotate(angle=0.03, about_point=self.dot.get_center())
        
        self.cut_point = np.array(cut_point)
        shift_vector = np.array([0, -0.35, 0])
        p_end = self.cut_point + shift_vector
        self.move_to(p_end).shift(0.5*DOWN)
    def open(self, angle):
        self.scissor_1.rotate(angle=angle, about_point=self.dot.get_center())
        self.scissor_2.rotate(angle=-angle, about_point=self.dot.get_center())


### ANimations
class FlashTrack(Animation):
    def __init__(self, mobject: VMobject, propotion_point_1: float, propotion_point_2: float, color = YELLOW, **kwargs):
        start = min([propotion_point_1, propotion_point_2])
        end = max([propotion_point_1, propotion_point_2])
        self.starting_point = mobject.point_from_proportion(start)
        self.ending_point = mobject.point_from_proportion(end)
        self.color = color
        super().__init__(mobject, **kwargs)

    def begin(self) -> None:
        small_line = Line(self.starting_point, 0.1*self.ending_point + 0.9*self.starting_point, color = self.color)
        self.initial_position = small_line.get_center()
        self.mobject.add(small_line)
        self.line = small_line
        self.shift_vector = self.ending_point + 0*self.starting_point
        super().begin()

    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        scene.remove(self.line)
        self.mobject.remove(self.line)
    def interpolate(self, alpha: float):
        if self.rate_func(alpha) <= 0.25:
            self.line.set_opacity(self.rate_func(alpha)* 4)
        if self.rate_func(alpha) >= 0.75:
            self.line.set_opacity((1-self.rate_func(alpha))* 4)
        self.line.move_to(self.rate_func(alpha)*self.starting_point + (1-self.rate_func(alpha))*self.ending_point)
        
### ComplexAnimations

        

class PourIntoCup(Animation):
    def __init__(self, mobject: FullCup, list_index, fullness,  **kwargs) -> None:
        mobject.height

        mobject.liquid[list_index]
        self.i = list_index
        self.fullness = fullness
        super().__init__(mobject, **kwargs)
    
    def interpolate(self, alpha: float) -> None:
        self.mobject.liquid[self.i].stretch_to_fit_height(
            (1-self.rate_func(alpha))*self.starting_mobject.liquid[self.i].height + self.rate_func(alpha)*self.fullness/100*self.mobject.cup.height
        )
        self.mobject.liquid.arrange(UP, buff=0).align_to(self.mobject.cup, DOWN + LEFT)
        self.mobject.fullness.set_value(
            self.mobject.fullness.get_value() - (self.starting_mobject.liquid[self.i].height/self.mobject.cup.height) *100 + ((1-self.rate_func(alpha))*self.starting_mobject.liquid[self.i].height/self.mobject.cup.height )*100 + self.rate_func(alpha)*self.fullness
        )
        

class Run(Animation):
    def __init__(self, mobject: Stopwatch, speed=1, run_time =1, dirt = 1, **kwargs) -> None:
        super().__init__(mobject, run_time = run_time,  **kwargs)
        self.radians = 2* PI * speed * run_time/60 * dirt
        self.time_passed = speed * run_time * dirt
        self.about_point = mobject.stopwatch.get_center()
        self.shift_resetter = 0.3 * (np.array(mobject.stopwatch_resetter.get_center()) - np.array(mobject.stopwatch.get_edge_center(UP)))

    def interpolate(self, alpha: float) -> None:
        if alpha < 0.1:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - (10*alpha) * self.shift_resetter)
        if alpha >= 0.9 and alpha <=1:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - (10*(1-alpha)) * self.shift_resetter)
        self.mobject.stopwatch_arrow.become(self.starting_mobject.stopwatch_arrow)
        self.mobject.stopwatch_arrow.rotate(
            -self.rate_func(alpha) * self.radians,
            axis=OUT,
            about_point=self.about_point
        )
        self.mobject.time.set_value(self.starting_mobject.time.get_value() + self.rate_func(alpha) * self.time_passed)

class Reset(Animation):
    def __init__(self, mobject: Stopwatch, **kwargs) -> None:
        super().__init__(mobject, run_time=0.4, **kwargs)
        self.shift_resetter = 0.3 * (np.array(mobject.stopwatch_resetter.get_center()) - np.array(mobject.stopwatch.get_edge_center(UP)))
        self.radians = 2*PI*(mobject.time.get_value()%60)/60
        self.about_point = mobject.stopwatch.get_center()
    def interpolate(self, alpha):
        if alpha < 0.25:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - self.rate_func(4*alpha) * self.shift_resetter)
        if alpha >= 0.25 and alpha < 0.5:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - self.rate_func(4*(0.5-alpha)) * self.shift_resetter)
        if alpha >= 0.5 and alpha < 0.75:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - self.rate_func(4*(0.75-alpha)) * self.shift_resetter)
        if alpha >= 0.75:
            self.mobject.stopwatch_resetter.move_to(self.starting_mobject.stopwatch_resetter.get_center() - self.rate_func(4*(1-alpha)) * self.shift_resetter)
        
        self.mobject.stopwatch_arrow.become(self.starting_mobject.stopwatch_arrow)
        self.mobject.stopwatch_arrow.rotate(
            self.rate_func(alpha) * self.radians,
            axis=OUT,
            about_point=self.about_point
        )
        self.mobject.time.set_value(0)

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

### Old fation
class Task(VGroup):
    def __init__(self,
                 number: MathTex,
                 text: VGroup,
                 **kwargs):
        VGroup.__init__(self)

        self.number = number.set_color(YELLOW)
        self.text = text.arrange(DOWN, aligned_edge=LEFT)
        #self = VGroup(Task.number, Task.text).arrange(RIGHT, aligned_edge=UP)

        self.add(self.number, self.text.align_to(self.number, UP))
        self.arrange(RIGHT, aligned_edge=UP)

    def up(self,
           scene: Scene):
        [x_number_0, y_number_0, z_number_0] = self.number.get_center()
        [x_text_0, y_text_0, z_text_0] = self.text.get_center()
        y_up_number_0 = self.number.get_edge_center(UP)[1]
        y_up_text_0 = self.text.get_edge_center(UP)[1]
        [x_number_1, y_number_1, z_number_1] = [-6, 24/7, 0]
        [x_text_1, y_text_1, z_text_1] = [x_text_0, 24/7 + (y_up_number_0 - y_number_0) - (y_up_text_0 - y_text_0), z_text_0]
        def go_up(self, t):
            pos_number = [x_number_0 * (1-t) + x_number_1 * t,
                          y_number_0 * (1-t) + y_number_1 * t,
                          z_number_0 * (1-t) + z_number_1 * t]
            self.number.move_to(pos_number).set_opacity(1-t/2)
            pos_text = [x_text_0 * (1-t) + x_text_1 * t,
                        y_text_0 * (1-t) + y_text_1 * t,
                        z_text_0 * (1-t) + z_text_1 * t]
            self.text.move_to(pos_text).set_opacity(1-t/3)

        scene.play(UpdateFromAlphaFunc(self, go_up)) 
