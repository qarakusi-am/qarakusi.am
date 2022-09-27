from manim import *
from aramanim import Segment
from objects import SimpleSVGMobject, Checkmark, DScissors
from .text import (
        condition_1_string,
        condition_2_string,
        three_times_more_list,
        in_total_list)

class Problem10488(Scene):
    def construct(self):
        self.set_up()
        figure_1 = self.figure_1
        figure_2 = self.figure_2
        cond_1 = self.cond_1
        cond_2 = self.cond_2
        checkmark_1 = self.checkmark_1
        checkmark_2 = self.checkmark_2
        scissors_1 = self.scissors_1
        scissors_2 = self.scissors_2
        small_pool = self.small_pool
        big_pool = self.big_pool
        self.wait()
        self.play(
            AnimationGroup(
                Create(small_pool),
                Create(big_pool),
                lag_ratio = 0.8))
        self.wait()

    def set_up(self):
        #segments set up
        figure_1 = VGroup(*[self.get_segment(), self.get_segment(60, BLUE)])
        figure_2 = VGroup(
            *[self.get_segment() for _ in range(3)],
            self.get_segment(40, BLUE))
        figure_1.arrange(RIGHT, buff=0)
        figure_1.align_to(1.5*UP + 2*LEFT, UP, LEFT)
        figure_2.arrange(RIGHT, buff=0)
        figure_2.next_to(figure_1, DOWN, buff=2)
        #text set up
        condition_1 = Tex(condition_1_string)
        condition_2 = Tex(condition_2_string)
        condition_1_content = Tex(*three_times_more_list)
        condition_2_content = Tex(*in_total_list)
        condition_1_content.arrange(DOWN, aligned_edge=LEFT)
        condition_2_content.arrange(DOWN, aligned_edge=LEFT)
        condition_1.next_to(condition_1_content, UP, aligned_edge=LEFT)
        condition_2.next_to(condition_2_content, UP, aligned_edge=LEFT)
        cond_1 = VGroup(condition_1, condition_1_content)
        cond_2 = VGroup(condition_2, condition_2_content)
        cond_1.next_to(figure_2, DOWN, buff=2, aligned_edge=LEFT)
        cond_2.next_to(cond_1, DOWN, buff=1, aligned_edge=LEFT)
        #checkmaek set up
        checkmark_1 = Checkmark()
        checkmark_2 = Checkmark()
        checkmark_1.next_to(VGroup(cond_1, cond_2), RIGHT, buff=1, aligned_edge=UP)
        checkmark_2.next_to(VGroup(cond_1, cond_2), RIGHT, buff=1, aligned_edge=DOWN)
        #scissors set up
        scissors_1 = DScissors(figure_1.get_right())
        scissors_2 = DScissors(figure_2.get_right())
        #pool SVG set up
        small_pool = SimpleSVGMobject('small_pool')
        big_pool = SimpleSVGMobject('big_pool')
        small_pool.scale(0.5)
        small_pool.next_to(figure_1, LEFT)
        big_pool.scale(0.8)
        big_pool.next_to(figure_2, LEFT)
        #self.
        self.figure_1 = figure_1
        self.figure_2 = figure_2
        self.cond_1 = cond_1
        self.cond_2 = cond_2
        self.checkmark_1 = checkmark_1
        self.checkmark_2 = checkmark_2
        self.scissors_1 = scissors_1
        self.scissors_2 = scissors_2
        self.small_pool = small_pool
        self.big_pool = big_pool

    def get_segment(self, value = 125, color = RED):
        return Segment(ORIGIN, (value/100)*RIGHT, label = "{:,}".format(value), color=color)
