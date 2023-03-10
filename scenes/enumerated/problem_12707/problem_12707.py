from manim import Scene, FadeIn, Tex, Write, DashedLine, ReplacementTransform, BraceLabel, GrowFromCenter, FadeOut, GrowFromEdge, MathTex, ApplyWave, VGroup, TransformFromCopy, Tex, ValueTracker, Brace
from manim import always_redraw
from manim import LEFT, DOWN, UP, RIGHT, UL
from manim import RED, BLUE, YELLOW
from qarakusiscene import TaskNumberBox
from aramanim import get_segment_part
from objects import SimpleSVGMobject, Checkmark
from .text import *

FONT_SIZE = 85
SEGMENT_SCALE = .105

class Problem12707(Scene):
    def construct(self):
        """Դուբին 126 էջանոց գրքի 24 էջը կարդաց առաջին օրը, իսկ հաջորդ օրը կարդաց ևս 35 էջ։ Քանի՞ էջ մնաց կարդալու։"""

        self.wait()

        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))
        self.wait()

        # create book
        book_svg = SimpleSVGMobject("colored_book_2")
        book_svg.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(book_svg))
        self.wait()

        # write conditions
        condition1 = Tex(condition1_str, font_size=FONT_SIZE)
        condition1.to_edge(UP).shift(LEFT*.5)
        self.play(Write(condition1))
        self.wait()

        condition2 = Tex(condition2_str, font_size=FONT_SIZE)
        condition2.next_to(condition1, DOWN, aligned_edge=LEFT)
        self.play(Write(condition2))
        self.wait()

        condition3 = Tex(condition3_str, font_size=FONT_SIZE)
        condition3.next_to(condition2, DOWN, aligned_edge=LEFT)
        self.play(Write(condition3))
        self.wait()

        # show first condition
        self.play(
            condition2.animate.set_opacity(.7).scale(.9),
            condition3.animate.set_opacity(.7).scale(.9),
            condition1.animate.scale(1.1)
        )

        # transform book to segment
        total_segment = get_segment_part(126*SEGMENT_SCALE)
        total_segment.move_to(book_svg.get_center())
        self.play(ReplacementTransform(book_svg, total_segment))
        self.wait()

        # write 126 under segment
        number_of_pages = ValueTracker(126)
        book_length = VGroup(always_redraw(lambda: Brace(total_segment.line, DOWN)))
        book_length.add(always_redraw(lambda: book_length[0].get_tex(f"{int(number_of_pages.get_value())} \\text{{{page_str}}}").scale(FONT_SIZE/48)))
        # BraceLabel(total_segment, f"126 \\text{{{page_str}}}", font_size=FONT_SIZE)
        self.play(
            GrowFromCenter(book_length[0]),
            Write(book_length[1])
        )
        self.wait()

        checkmark1 = Checkmark().scale(.4)
        checkmark1.next_to(condition1, RIGHT)
        self.play(FadeIn(checkmark1))

        # show second condition
        self.play(
            condition1.animate.scale(.9/1.1).set_opacity(.7),
            condition2.animate.scale(1.1/.9).set_opacity(1)
        )

        first_day_segment = get_segment_part(24*SEGMENT_SCALE, color=RED)
        first_day_segment.move_to(total_segment, aligned_edge=LEFT)
        first_day_pages = BraceLabel(first_day_segment, f"24 \\text{{{page_str}}}", UP, font_size=FONT_SIZE)
        self.play(
            GrowFromEdge(first_day_segment, LEFT),
            GrowFromEdge(first_day_pages.brace, LEFT)
        )
        self.play(Write(first_day_pages.label))

        checkmark2 = checkmark1.copy()
        checkmark2.next_to(condition2).align_to(checkmark1, LEFT)
        self.play(FadeIn(checkmark2))

        # show second condition
        self.play(
            condition2.animate.scale(.9/1.1).set_opacity(.7),
            condition3.animate.scale(1.1/.9).set_opacity(1)
        )
        self.wait()

        second_day_segment = get_segment_part(35*SEGMENT_SCALE, color=BLUE)
        second_day_segment.next_to(first_day_segment, buff=0)
        second_day_pages = BraceLabel(second_day_segment, f"35 \\text{{{page_str}}}", UP, font_size=FONT_SIZE)
        self.play(
            GrowFromEdge(second_day_segment, LEFT),
            GrowFromEdge(second_day_pages.brace, LEFT)
        )
        self.play(Write(second_day_pages.label))
        self.wait()

        checkmark3 = checkmark1.copy()
        checkmark3.next_to(condition3).align_to(checkmark1, LEFT)
        self.play(FadeIn(checkmark3))
        self.wait()

        # write "?"
        x_segment = get_segment_part(
            67*SEGMENT_SCALE,
            color=YELLOW,
            label="?",
            label_font_size=2*FONT_SIZE
        )
        x_segment.next_to(second_day_segment, buff=0)
        x_segment.update_label_pos()
        self.play(FadeIn(x_segment))
        self.play(Write(x_segment.label))
        self.wait()

        # rmeove coditions
        self.play(FadeOut(condition1, condition2, condition3, checkmark1, checkmark2, checkmark3, x_segment.label))
        self.wait()

        # rmeove braces
        self.play(
            FadeOut(first_day_pages.brace, second_day_pages.brace),
            first_day_pages.label.animate.next_to(first_day_segment, UP),
            second_day_pages.label.animate.next_to(second_day_segment, UP)
        )
        self.wait()

        # remove total segment from background
        self.remove(total_segment)

        # show already read pages
        self.play(
            ApplyWave(VGroup(first_day_segment, second_day_segment))
        )
        self.wait()

        # write how many pages already read
        first_calc = MathTex("1)", "24", "+", "35", "=", "59", font_size=FONT_SIZE)
        first_calc.to_corner(UL).shift(DOWN)
        second_calc = MathTex("2)", "126", "-", "59", "=", "67", font_size=FONT_SIZE)
        second_calc.next_to(first_calc, DOWN, aligned_edge=LEFT)
        for index, symbol in enumerate(first_calc):
            symbol.set_x(second_calc[index].get_x())
        self.play(Write(first_calc))
        self.wait()

        # show how many pages are left
        self.play(ApplyWave(x_segment))
        self.wait()

        # write how many pages are left
        self.play(Write(second_calc))
        self.wait()

        # move 67 on the 3rd segment
        answer = MathTex(f"67 \\text{{{page_str}}}", font_size=FONT_SIZE)
        answer.next_to(x_segment, UP)
        self.play(TransformFromCopy(second_calc[-1], answer))
        self.wait()
        self.play(answer.animate.set_color(YELLOW).scale(1.2))
        self.wait()

        # 2nd solution
        dashed_line = DashedLine(UP, DOWN*3)
        dashed_line.to_edge(UP, buff=0)
        self.play(
            GrowFromEdge(dashed_line, UP),
            FadeOut(answer)
        )
        self.wait()

        first_solution_tex = Tex(first_solution_str, font_size=.7*FONT_SIZE)
        first_solution_tex.next_to(dashed_line, LEFT).to_edge(UP)
        self.play(Write(first_solution_tex))

        second_solution_tex = Tex(second_solution_str, font_size=.7*FONT_SIZE)
        second_solution_tex.next_to(dashed_line, RIGHT).to_edge(UP)
        self.play(Write(second_solution_tex))
        self.wait()

        # write 126-24=102
        first_calc2 = MathTex("1) 126 - 24 = 102", font_size=FONT_SIZE)
        first_calc2.next_to(dashed_line).set_y(first_calc.get_y())
        self.play(Write(first_calc2))
        self.wait()

        # show 126-24=102 on segment
        total_segment.set_opacity(0)
        self.play(
            total_segment.line.animate.set_length(102*SEGMENT_SCALE).align_to(total_segment, RIGHT),
            number_of_pages.animate.set_value(102)
        )

        # write 102-35=67
        second_calc2 = MathTex("2) 102 - 35 = 67", font_size=FONT_SIZE)
        second_calc2.next_to(first_calc2, DOWN, aligned_edge=LEFT)
        self.play(Write(second_calc2))
        self.wait()

        # show 102-35=67 on segment
        self.play(
            total_segment.line.animate.set_length(67*SEGMENT_SCALE).align_to(total_segment, RIGHT),
            number_of_pages.animate.set_value(67)
        )

        # move 67 on the 3rd segment
        book_length[1].clear_updaters()
        self.play(book_length[1].animate.set_color(YELLOW).scale(1.2).align_to(book_length[1], UP))
        self.wait()

        self.wait(2)
