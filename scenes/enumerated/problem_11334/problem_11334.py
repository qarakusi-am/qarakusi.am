"""

կա 5 երեխա
ամեն հաջորդը նախորդից 3 տարով փոքր ա
ավագը կրտսերից մեծ ա 4 անգամ

փոքրը պատկերենք 1 մաս
նրանից առաջ ծնվածը 1 մաս և 3
միջնեկը 1 մաս և 2 հատ 3
նախամեծը 1 մաս և 3 հատ 3

մեծը 1 մաս և 3 3 3 3, 
** այսինքն 1 մաս և 12 **
ավագը կլինի 4 մաս

գծագիրը ուղղել



"""


from manim import *

from constants import DEFAULT_SEGMENT_TEXT_POSITION
from .text import youngest, oldest


from lib.segment import Segment

class Problem11334(Scene):
    def construct(self):

# INITS
        left_boundary = -4.5
        part_length = ValueTracker(2.5)
    
    # seg_1
        seg_1 = always_redraw(lambda: Segment([left_boundary, 3, 0], [left_boundary + part_length.get_value(), 3, 0]))
        text_1 = Tex('4').next_to(seg_1, DEFAULT_SEGMENT_TEXT_POSITION)
        youngest.next_to(seg_1, 2 * LEFT)

    # seg_2
        seg_2 = always_redraw(lambda: Segment([left_boundary, 2, 0], [left_boundary + part_length.get_value(), 2, 0]))
        text_2 = Tex('4').next_to(seg_2, DEFAULT_SEGMENT_TEXT_POSITION)
        seg_2_extra = always_redraw(lambda: 
            Segment(seg_2.line.get_right(), seg_2.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )

    # seg_3
        seg_3 = always_redraw(lambda: Segment([left_boundary, 1, 0], [left_boundary + part_length.get_value(), 1, 0]))
        text_3 = Tex('4').next_to(seg_3, DEFAULT_SEGMENT_TEXT_POSITION)
        seg_3_extra_1 = always_redraw(lambda: 
            Segment(seg_3.line.get_right(), seg_3.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )
        seg_3_extra_2 = always_redraw(lambda: 
            Segment(seg_3_extra_1.line.get_right(), seg_3_extra_1.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )

    # seg_4
        seg_4 = always_redraw(lambda: Segment([left_boundary, 0, 0], [left_boundary + part_length.get_value(), 0, 0]))
        text_4 = Tex('4').next_to(seg_4, DEFAULT_SEGMENT_TEXT_POSITION)
        seg_4_extra_1 = always_redraw(lambda: 
            Segment(seg_4.line.get_right(), seg_4.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )
        seg_4_extra_2 = always_redraw(lambda: 
            Segment(seg_4_extra_1.line.get_right(), seg_4_extra_1.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )
        seg_4_extra_3 = always_redraw(lambda: 
            Segment(seg_4_extra_2.line.get_right(), seg_4_extra_2.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        )   

    # seg_5
        seg_5 = always_redraw(lambda: Segment([left_boundary, -1, 0], [left_boundary + part_length.get_value(), -1, 0]))
        text_5 = Tex('4').next_to(seg_5, DEFAULT_SEGMENT_TEXT_POSITION)
        seg_5_extra_combined = always_redraw(lambda: 
            Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5 * 4, 0, 0]), GREEN, text=Tex('12'))
        )
        # seg_5_extra_combined.add_updater(lambda mob: mob.become(Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5 * 4, 0, 0]), GREEN, text=Tex('12'))))

        seg_5_extra_1 = Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        seg_5_extra_2 = Segment(seg_5_extra_1.line.get_right(), seg_5_extra_1.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        seg_5_extra_3 = Segment(seg_5_extra_2.line.get_right(), seg_5_extra_2.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))
        seg_5_extra_4 = Segment(seg_5_extra_3.line.get_right(), seg_5_extra_3.line.get_right() + np.array([1.5, 0, 0]), GREEN, text=Tex('3'))

        oldest.next_to(seg_5, 2 * LEFT)

    # seg_5 by four parts
        seg_5_part_1 = always_redraw(lambda: 
            Segment([left_boundary, -2, 0], np.array([left_boundary, -2, 0]) + np.array([part_length.get_value(), 0, 0]))
        )
        x_1 = Tex('4').next_to(seg_5_part_1, DEFAULT_SEGMENT_TEXT_POSITION)

        seg_5_part_2 = always_redraw(lambda: 
            Segment(seg_5_part_1.get_right(), seg_5_part_1.get_right() + np.array([part_length.get_value(), 0, 0]))
        )
        seg_5_part_3 = always_redraw(lambda: 
            Segment(seg_5_part_2.get_right(), seg_5_part_2.get_right() + np.array([part_length.get_value(), 0, 0]))
        )
        seg_5_part_4 = always_redraw(lambda: 
            Segment(seg_5_part_3.get_right(), seg_5_part_3.get_right() + np.array([part_length.get_value(), 0, 0]))
        )

        brace_seg_5 = Brace(VGroup(seg_5, seg_5_part_1), LEFT, 0.2, 0.5)

    # equations
        eq_1 = MathTex("12 : 3 = ", "4", font_size=DEFAULT_FONT_SIZE).shift(3*UP+4*RIGHT)
        x_2 = eq_1[1].copy()
        x_3 = eq_1[1].copy()
        x_4 = eq_1[1].copy()



# ANIMATIONS
    # youngest - seg_1
        self.play(Write(youngest))
        self.wait(0.25)
        self.play(Create(seg_1))
        self.wait()

    # seg_2
        self.play(Create(seg_2))
        self.wait(0.25)
        self.play(Create(seg_2_extra))
        self.wait()

    # seg_3
        self.play(Create(seg_3))
        self.wait(0.25)
        self.play(Create(seg_3_extra_1))
        self.wait(0.25)
        self.play(Create(seg_3_extra_2))
        self.wait()

    # seg_4
        self.play(Create(seg_4))
        self.wait(0.25)
        self.play(Create(seg_4_extra_1))
        self.wait(0.25)
        self.play(Create(seg_4_extra_2))
        self.wait(0.25)
        self.play(Create(seg_4_extra_3))
        self.wait()
    
    # seg_5
        self.play(Write(oldest))
        self.play(Create(seg_5))
        self.wait(0.25)
        self.play(Create(seg_5_extra_1))
        self.wait(0.25)
        self.play(Create(seg_5_extra_2))
        self.wait(0.25)
        self.play(Create(seg_5_extra_3))
        self.wait(0.25)
        self.play(Create(seg_5_extra_4))
        self.wait()

        self.play(
            FadeOut(
                seg_5_extra_1.endmark_left, seg_5_extra_1.endmark_right, seg_5_extra_1.line,
                seg_5_extra_2.endmark_left, seg_5_extra_2.endmark_right, seg_5_extra_2.line,
                seg_5_extra_3.endmark_left, seg_5_extra_3.endmark_right, seg_5_extra_3.line,
                seg_5_extra_4.endmark_left, seg_5_extra_4.endmark_right, seg_5_extra_4.line,
            ),
            ReplacementTransform(
                VGroup(seg_5_extra_1.text, seg_5_extra_2.text, seg_5_extra_3.text, seg_5_extra_4.text), 
                Dot(seg_5_extra_combined.text.get_center(), 0),
                remover=True
            ),
            FadeIn(seg_5_extra_combined)
        )
        self.wait()

    # seg_5 by four parts
        self.play(Create(seg_5_part_1))
        self.wait(0.25)
        self.play(Create(seg_5_part_2))
        self.wait(0.25)
        self.play(Create(seg_5_part_3))
        self.wait(0.25)
        self.play(Create(seg_5_part_4))
        self.wait()

        self.play(oldest.animate.next_to(brace_seg_5, LEFT))
        self.wait(0.25)
        self.play(Write(brace_seg_5))
        self.wait()

    # change size of unit segment (1 part)
        self.play(part_length.animate.set_value(1))
        self.wait()
        self.play(part_length.animate.set_value(3))
        self.wait()
        self.play(part_length.animate.set_value(2))
        self.wait()

# INIT
        dline_1 = DashedLine(seg_5_extra_combined.endmark_left, seg_5_part_2.endmark_left)
        dline_2 = DashedLine(seg_5_extra_combined.endmark_right, seg_5_part_4.endmark_right)
#

        self.play(Indicate(seg_5_extra_combined))
        self.wait()

        self.play(
            Create(dline_1),
            Create(dline_2)
        )
        self.wait()

        seg_5_part_2.remove_updater()
        seg_5_part_3.remove_updater()
        seg_5_part_4.remove_updater()

        self.play(seg_5_part_2.animate.shift(0.25*UP).set_color(YELLOW), rate_func=there_and_back)
        self.wait(0.25)

        self.play(seg_5_part_3.animate.shift(0.25*UP).set_color(YELLOW), rate_func=there_and_back)
        self.wait(0.25)

        self.play(seg_5_part_4.animate.shift(0.25*UP).set_color(YELLOW), rate_func=there_and_back)
        self.wait(0.25)

        self.play(Write(eq_1))
        self.wait()

        self.play(
            x_2.animate.next_to(seg_5_part_2, DEFAULT_SEGMENT_TEXT_POSITION),
            x_3.animate.next_to(seg_5_part_3, DEFAULT_SEGMENT_TEXT_POSITION),
            x_4.animate.next_to(seg_5_part_4, DEFAULT_SEGMENT_TEXT_POSITION)
        )
        self.wait()

        self.play(
            Write(text_1),
            Write(text_2),
            Write(text_3),
            Write(text_4),
            Write(text_5),
            Write(x_1)
        )
        self.wait()
        


