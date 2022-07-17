from manim import *
from aramanim import *

class SimpleSegmentScene(Scene):
    def construct(self):
        small_segment = Segment(label=8)
        self.add(small_segment)
        self.play(small_segment.line.animate.scale(4))
        blue_dot = Dot([-2.5, 2, 0]).set_color(BLUE)
        self.add(blue_dot)
        self.play(Write(small_segment.update_label_pos()))
        small_segment.label.add_updater(lambda mob: mob.become(small_segment.update_label_pos()))
        self.play(small_segment.animate.next_to(blue_dot, RIGHT, buff = 0))
        self.wait(2)

        parts = VGroup(*[Segment(label = i) for i in range(3)]).arrange(RIGHT, buff=0)
        self.play(Create(parts), *[Write(p.update_label_pos()) for p in parts])
        self.wait()
        small_segment.set_label(Circle(fill_opacity=1).scale(0.2))
        self.wait()
        self.play(small_segment.animate.next_to(parts, RIGHT, buff = 0))
        self.wait(2)