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
from .text import youngest, second, third, fourth, fifth, fifth_2, oldest

from segment import Segment

class Problem11334(Scene):
    def construct(self):

# INITS
        left_boundary = -4.5
        part_length = ValueTracker(2.5)

    # seg_1
        seg_1 = always_redraw(lambda: Segment([left_boundary, 3, 0], [left_boundary + part_length.get_value(), 3, 0]))


        youngest.next_to(seg_1, 2 * LEFT)
        second.shift(2 * UP).align_to(youngest, LEFT)
        third.next_to(UP).align_to(second, LEFT)
        fourth.align_to(third, LEFT)
        fifth.shift(DOWN).align_to(fourth, LEFT)
        fifth_2.shift(2 * DOWN).align_to(fifth, LEFT)

    # seg_2
        seg_2_init = Segment([left_boundary, 2, 0], [left_boundary + part_length.get_value() + 1.5, 2, 0])
        seg_2_black = seg_1.copy()

        seg_2 = always_redraw(lambda: Segment([left_boundary, 2, 0], [left_boundary + part_length.get_value(), 2, 0]))
        seg_2_extra = always_redraw(lambda: 
            Segment(seg_2.line.get_right(), seg_2.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=Tex('3'))
        )

        final_length_2 = ValueTracker(2)
        seg_2_final = always_redraw(lambda: 
            Segment(seg_2.line.get_left(), seg_2.line.get_left() + np.array([final_length_2.get_value(), 0, 0]))
        )
        final_text_2 = MathTex('4').next_to(seg_2_final, DEFAULT_SEGMENT_TEXT_POSITION)

        seg_2_final_extra = always_redraw(lambda:
            Segment(seg_2_final.line.get_right(), seg_2_final.line.get_left() + np.array([3.5, 0, 0]), ORANGE)
        )
        final_text_2_extra = MathTex('3').next_to(seg_2_final_extra, DEFAULT_SEGMENT_TEXT_POSITION)

        seconds_length = MathTex('4', '+', '3').next_to((seg_2_final.line.get_left() + seg_2_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

        ans_2 = MathTex('7').next_to((seg_2_final.line.get_left() + seg_2_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

        

    # seg_3
        unnecessary_length_3 = ValueTracker(1)
        seg_3_init = always_redraw(lambda: Segment([left_boundary, 1, 0], [left_boundary + part_length.get_value() + 2 * 1.5 + unnecessary_length_3.get_value(), 1, 0]))
        seg_3_black = VGroup(seg_2, seg_2_extra).copy()

        seg_3 = always_redraw(lambda: Segment([left_boundary, 1, 0], [left_boundary + part_length.get_value(), 1, 0]))
        seg_3_extra_combined = always_redraw(lambda: 
            Segment(seg_3.line.get_right(), seg_3.line.get_right() + np.array([1.5 * 2, 0, 0]), ORANGE, text=MathTex('6'))
        )

        seg_3_extra_1 = always_redraw(lambda: 
            Segment(seg_3.line.get_right(), seg_3.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        )
        seg_3_extra_2 = always_redraw(lambda: 
            Segment(seg_3_extra_1.line.get_right(), seg_3_extra_1.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        )

        final_length_3 = ValueTracker(2)
        seg_3_final = always_redraw(lambda: 
            Segment(seg_3.line.get_left(), seg_3.line.get_left() + np.array([final_length_3.get_value(), 0, 0]))
        )
        final_text_3 = MathTex('4').next_to(seg_3_final, DEFAULT_SEGMENT_TEXT_POSITION)

        seg_3_final_extra = always_redraw(lambda:
            Segment(seg_3_final.line.get_right(), seg_3_final.line.get_left() + np.array([5, 0, 0]), ORANGE)
        )
        final_text_3_extra = MathTex('6').next_to(seg_3_final_extra, DEFAULT_SEGMENT_TEXT_POSITION)

        thirds_length = MathTex('4', '+', '6').next_to((seg_3_final.line.get_left() + seg_3_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

        ans_3 = MathTex('10').next_to((seg_3_final.line.get_left() + seg_3_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

    # seg_4
        unnecessary_length_4 = ValueTracker(2.5)
        seg_4_init = always_redraw(lambda: Segment([left_boundary, 0, 0], [left_boundary + part_length.get_value() + 3 * 1.5 + unnecessary_length_4.get_value(), 0, 0]))
        seg_4_black = VGroup(seg_3, seg_3_extra_1, seg_3_extra_2).copy()

        seg_4 = always_redraw(lambda: Segment([left_boundary, 0, 0], [left_boundary + part_length.get_value(), 0, 0]))
        seg_4_extra_combined = always_redraw(lambda: 
            Segment(seg_4.line.get_right(), seg_4.line.get_right() + np.array([1.5 * 3, 0, 0]), ORANGE, text=MathTex('9'))
        )

        seg_4_extra_1 = always_redraw(lambda: 
            Segment(seg_4.line.get_right(), seg_4.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        )
        seg_4_extra_2 = always_redraw(lambda: 
            Segment(seg_4_extra_1.line.get_right(), seg_4_extra_1.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        )
        seg_4_extra_3 = always_redraw(lambda: 
            Segment(seg_4_extra_2.line.get_right(), seg_4_extra_2.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        )

        final_length_4 = ValueTracker(2)
        seg_4_final = always_redraw(lambda: 
            Segment(seg_4.line.get_left(), seg_4.line.get_left() + np.array([final_length_4.get_value(), 0, 0]))
        )
        final_text_4 = MathTex('4').next_to(seg_4_final, DEFAULT_SEGMENT_TEXT_POSITION)

        seg_4_final_extra = always_redraw(lambda:
            Segment(seg_4_final.line.get_right(), seg_4_final.line.get_left() + np.array([6.5, 0, 0]), ORANGE)
        )
        final_text_4_extra = MathTex('9').next_to(seg_4_final_extra, DEFAULT_SEGMENT_TEXT_POSITION)

        fourth_length = MathTex('4', '+', '9').next_to((seg_4_final.line.get_left() + seg_4_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

        ans_4 = MathTex('13').next_to((seg_4_final.line.get_left() + seg_4_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

    # seg_5
        unnecessary_length_5 = ValueTracker(1.5)
        necessary_length_5 = ValueTracker(0)
        seg_5_init = always_redraw(lambda: Segment([left_boundary + necessary_length_5.get_value(), -1, 0], [left_boundary + part_length.get_value() + 4 * 1.5 + unnecessary_length_5.get_value(), -1, 0]))
        seg_5_black = VGroup(seg_4, seg_4_extra_1, seg_4_extra_2, seg_4_extra_3).copy()

        seg_5 = always_redraw(lambda: Segment([left_boundary, -1, 0], [left_boundary + part_length.get_value(), -1, 0]))
        seg_5_extra_combined = always_redraw(lambda: 
            Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5 * 4, 0, 0]), ORANGE, text=MathTex('12'))
        )
        # seg_5_extra_combined.add_updater(lambda mob: mob.become(Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5 * 4, 0, 0]), ORANGE, text=Tex('12'))))

        seg_5_extra_1 = Segment(seg_5.line.get_right(), seg_5.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        seg_5_extra_2 = Segment(seg_5_extra_1.line.get_right(), seg_5_extra_1.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        seg_5_extra_3 = Segment(seg_5_extra_2.line.get_right(), seg_5_extra_2.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))
        seg_5_extra_4 = Segment(seg_5_extra_3.line.get_right(), seg_5_extra_3.line.get_right() + np.array([1.5, 0, 0]), ORANGE, text=MathTex('3'))

        oldest.next_to(seg_5, 2 * LEFT)

        final_length_5 = ValueTracker(2)
        seg_5_final = always_redraw(lambda: 
            Segment(seg_5.line.get_left(), seg_5.line.get_left() + np.array([final_length_5.get_value(), 0, 0]))
        )
        final_text_5 = MathTex('4').next_to(seg_5_final, DEFAULT_SEGMENT_TEXT_POSITION)

        seg_5_final_extra = always_redraw(lambda:
            Segment(seg_5_final.line.get_right(), seg_5_final.line.get_left() + np.array([8, 0, 0]), ORANGE)
        )
        final_text_5_extra = MathTex('12').next_to(seg_5_final_extra, DEFAULT_SEGMENT_TEXT_POSITION)

        fifth_length = MathTex('4', '+', '12').next_to((seg_5_final.line.get_left() + seg_5_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

        ans_5 = MathTex('16').next_to((seg_5_final.line.get_left() + seg_5_final_extra.line.get_right()) / 2, DEFAULT_SEGMENT_TEXT_POSITION)

    # seg_5 by four parts
        seg_5_part_1 = always_redraw(lambda: 
            Segment([left_boundary, -2, 0], np.array([left_boundary, -2, 0]) + np.array([part_length.get_value(), 0, 0]))
        )

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

        self.add(
            youngest,
            second, third, fourth,
            fifth, fifth_2
        )
        self.wait()
        self.play(Create(seg_1))
        self.wait(0.25)

    # seg_2
        self.play(ReplacementTransform(second, seg_2_init))
        self.wait(0.25)

        self.play(seg_2_black.animate.shift(DOWN))
        self.wait(0.25)
        self.play(
            Create(seg_2_extra)
        )
        self.wait()


        self.add(seg_2)
        self.remove(seg_2_black, seg_2_init)

    # seg_3
        self.play(ReplacementTransform(third, seg_3_init))
        self.wait(0.25)

        self.play(seg_3_black.animate.shift(DOWN))
        self.wait(0.25)

        self.play(
            Create(seg_3_extra_2),
            unnecessary_length_3.animate.set_value(0),
            rate_func=linear
        )
        self.wait()

        self.add(seg_3, seg_3_extra_1)
        self.remove(seg_3_black, seg_3_init)

    # seg_4
        self.play(ReplacementTransform(fourth, seg_4_init))
        self.wait(0.25)

        self.play(seg_4_black.animate.shift(DOWN))
        self.wait(0.25)
        
        self.play(
            Create(seg_4_extra_3),
            unnecessary_length_4.animate.set_value(0),
            rate_func=linear
        )
        self.wait()

        self.add(seg_4, seg_4_extra_1, seg_4_extra_2)
        self.remove(seg_4_black, seg_4_init)
    
    # seg_5
        self.play(
            fifth[0].animate.move_to(oldest),
            ReplacementTransform(fifth[1], seg_5_init)
        )
        self.add(oldest)
        self.remove(fifth[0])
        self.wait(0.25)
        
        self.play(seg_5_black.animate.shift(DOWN))
        self.wait(0.25)

        self.add(seg_5, seg_5_extra_1, seg_5_extra_2, seg_5_extra_3)
        self.remove(seg_5_black)

        necessary_length_5.set_value(7)

        self.play(seg_5_extra_1.animate.shift(0.25 * UP), rate_func=there_and_back)
        self.wait(0.25)

        self.play(seg_5_extra_2.animate.shift(0.25 * UP), rate_func=there_and_back)
        self.wait(0.25)

        self.play(seg_5_extra_3.animate.shift(0.25 * UP), rate_func=there_and_back)
        self.wait(0.25)

        self.play(
            Create(seg_5_extra_4),
            unnecessary_length_5.animate.set_value(0),
            rate_func=linear
        )
        self.wait()

        self.remove(seg_5_init)

        self.play(
            FadeOut(
                seg_5_extra_1.endmark_left, seg_5_extra_1.endmark_right, seg_5_extra_1.line,
                seg_5_extra_2.endmark_left, seg_5_extra_2.endmark_right, seg_5_extra_2.line,
                seg_5_extra_3.endmark_left, seg_5_extra_3.endmark_right, seg_5_extra_3.line,
                seg_5_extra_4.endmark_left, seg_5_extra_4.endmark_right, seg_5_extra_4.line
            ),
            FadeOut(
                seg_4_extra_1.endmark_left, seg_4_extra_1.endmark_right, seg_4_extra_1.line,
                seg_4_extra_2.endmark_left, seg_4_extra_2.endmark_right, seg_4_extra_2.line,
                seg_4_extra_3.endmark_left, seg_4_extra_3.endmark_right, seg_4_extra_3.line
            ),
            FadeOut(
                seg_3_extra_1.endmark_left, seg_3_extra_1.endmark_right, seg_3_extra_1.line,
                seg_3_extra_2.endmark_left, seg_3_extra_2.endmark_right, seg_3_extra_2.line
            ),
            ReplacementTransform(
                VGroup(seg_5_extra_1.text, seg_5_extra_2.text, seg_5_extra_3.text, seg_5_extra_4.text), 
                Dot(seg_5_extra_combined.text.get_center(), 0),
                remover=True
            ),
            ReplacementTransform(
                VGroup(seg_4_extra_1.text, seg_4_extra_2.text, seg_4_extra_3.text), 
                Dot(seg_4_extra_combined.text.get_center(), 0),
                remover=True
            ),
            ReplacementTransform(
                VGroup(seg_3_extra_1.text, seg_3_extra_2.text), 
                Dot(seg_5_extra_combined.text.get_center(), 0),
                remover=True
            ),
            FadeIn(
                seg_5_extra_combined,
                seg_4_extra_combined,
                seg_3_extra_combined
            )
        )
        self.wait()

    # seg_5 by four parts
        self.play(
            ReplacementTransform(fifth_2[1], seg_5_part_1),
            fifth_2[0].animate.align_to(oldest, LEFT)
        )
        self.wait(0.25)
        self.play(Create(seg_5_part_2))
        self.wait(0.25)
        self.play(Create(seg_5_part_3))
        self.wait(0.25)
        self.play(Create(seg_5_part_4))
        self.wait()

        self.play(
            oldest.animate.next_to(brace_seg_5, LEFT),
            fifth_2[0].animate.next_to(brace_seg_5, LEFT)
        )
        self.wait(0.25)
        self.play(Write(brace_seg_5))
        self.remove(fifth_2[0])
        self.wait()

    # change size of unit segment (1 part)
        self.play(part_length.animate.set_value(1), run_time=5)
        self.wait()
        self.play(part_length.animate.set_value(2), rate_func=linear, run_time=3)
        self.wait()

# INIT
        dline_1 = DashedLine(seg_5_extra_combined.endmark_left, seg_5_part_2.endmark_left)
        dline_2 = DashedLine(seg_5_extra_combined.endmark_right, seg_5_part_4.endmark_right)
        
        text_1 = always_redraw(lambda: MathTex('4').next_to(seg_1, DEFAULT_SEGMENT_TEXT_POSITION))
        text_2 = always_redraw(lambda: MathTex('4').next_to(seg_2, DEFAULT_SEGMENT_TEXT_POSITION))
        text_3 = always_redraw(lambda: MathTex('4').next_to(seg_3, DEFAULT_SEGMENT_TEXT_POSITION))
        text_4 = always_redraw(lambda: MathTex('4').next_to(seg_4, DEFAULT_SEGMENT_TEXT_POSITION))
        text_5 = always_redraw(lambda: MathTex('4').next_to(seg_5, DEFAULT_SEGMENT_TEXT_POSITION))
        x_1 = MathTex('4').next_to(seg_5_part_1, DEFAULT_SEGMENT_TEXT_POSITION)
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
        
    # find second's lenght

        self.add(seg_2_final, seg_2_final_extra, final_text_2, final_text_2_extra)
        self.remove(seg_2, seg_2_extra, text_2)

        self.play(
            final_length_2.animate.set_value(3.5),
            final_text_2.animate.move_to(seconds_length[0]),
            Write(seconds_length[1]),
            final_text_2_extra.animate.move_to(seconds_length[2]),
            rate_func=linear
        )
        self.wait(0.25)

        self.add(seconds_length[0], seconds_length[2])
        self.remove(final_text_2, final_text_2_extra)

        self.play(ReplacementTransform(seconds_length, ans_2))
        self.wait()

    # find third's lenght
        
        self.add(seg_3_final, seg_3_final_extra, final_text_3, final_text_3_extra)
        self.remove(seg_3, seg_3_extra_combined, text_3)

        self.play(
            final_length_3.animate.set_value(5),
            final_text_3.animate.move_to(thirds_length[0]),
            Write(thirds_length[1]),
            final_text_3_extra.animate.move_to(thirds_length[2]),
            rate_func=linear
        )
        self.wait(0.25)

        self.add(thirds_length[0], thirds_length[2])
        self.remove(final_text_3, final_text_3_extra)

        self.play(ReplacementTransform(thirds_length, ans_3))
        self.wait()

    # find fourth's length
        
        self.add(seg_4_final, seg_4_final_extra, final_text_4, final_text_4_extra)
        self.remove(seg_4, seg_4_extra_combined, text_4)

        self.play(
            final_length_4.animate.set_value(6.5),
            final_text_4.animate.move_to(fourth_length[0]),
            Write(fourth_length[1]),
            final_text_4_extra.animate.move_to(fourth_length[2]),
            rate_func=linear
        )
        self.wait(0.25)

        self.add(fourth_length[0], fourth_length[2])
        self.remove(final_text_4, final_text_4_extra)

        self.play(ReplacementTransform(fourth_length, ans_4))
        self.wait()

    # find fifth's length
        
        self.add(seg_5_final, seg_5_final_extra, final_text_5, final_text_5_extra)
        self.remove(seg_5, seg_5_extra_combined, text_5)

        self.play(
            final_length_5.animate.set_value(8),
            final_text_5.animate.move_to(fifth_length[0]),
            Write(fifth_length[1]),
            final_text_5_extra.animate.move_to(fifth_length[2]),
            rate_func=linear
        )
        self.wait(0.25)

        self.add(fifth_length[0], fifth_length[2])
        self.remove(final_text_5, final_text_5_extra)

        self.play(ReplacementTransform(fifth_length, ans_5))
        self.wait()



       

        
