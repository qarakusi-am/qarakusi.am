from manim import Scene, FadeIn, Square, Rectangle, VGroup, MathTex, TransformFromCopy, Write, Indicate
from manim import ORANGE, BLUE, WHITE, RED
from manim import DR, UL, LEFT, UP, RIGHT, DL
from qarakusiscene import TaskNumberBox
from .text import *

SCALE = .37
FONT_SIZE = 70

class Problem12768(Scene):
    def construct(self):
        self.wait()
        
        # task number
        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))
        self.wait()

        # Rectangle and Square
        rect = Rectangle(ORANGE, 8, 14, stroke_color=WHITE)
        rect.scale(SCALE).set_opacity(1).to_edge(UP, buff=1)
        square = VGroup(*[Square(2, color=BLUE, stroke_color=WHITE) for _ in range(4)])
        square.scale(SCALE).set_opacity(1).arrange_in_grid(buff=0).align_to(rect, DR).shift(DR*2*SCALE)

        rect_height = MathTex("8", font_size=FONT_SIZE)
        rect_height.next_to(rect, LEFT)
        rect_width = MathTex("14", font_size=FONT_SIZE)
        rect_width.next_to(rect, UP)
        square_side = MathTex("4", font_size=FONT_SIZE)
        square_side.next_to(square)

        self.play(FadeIn(rect, square, rect_height, rect_width, square_side))
        self.wait()

        # copy rect and square
        rect_copy = rect.copy().to_corner(DL).shift(RIGHT)
        square_copy = square.copy().to_corner(DR).shift(UL*.2+LEFT*1.9)
        self.play(
            TransformFromCopy(rect, rect_copy),
            TransformFromCopy(square, square_copy)
        )
        self.wait()

        # area of the rect
        rect_area = MathTex(f"8 \\text{{{cm}}} \\cdot 14 \\text{{{cm}}} = ", f"112 \\text{{{cm}}}^2", font_size=FONT_SIZE*.8)
        rect_area.move_to(rect_copy)
        self.play(Write(rect_area))
        self.wait()

        # area of the square
        square_area = MathTex(f"4 \\text{{{cm}}} \\cdot 4 \\text{{{cm}}} = ", f"16 \\text{{{cm}}}^2", font_size=FONT_SIZE*.8)
        square_area.next_to(square_copy, UP)
        self.play(Write(square_area))
        self.wait()

        # area of small squares
        areas_of_small_squares = VGroup(*[MathTex("4", font_size=FONT_SIZE*1.1) for _ in range(4)])
        for index, tex in enumerate(areas_of_small_squares):
            tex.move_to(square_copy[index].get_center())
        
        self.play(Indicate(square_area[-1]))
        self.wait()
        self.play(TransformFromCopy(square_area[-1], areas_of_small_squares))
        self.wait()

        # answer
        answer = MathTex("112", "-", "4", "=", f"108 \\text{{{cm}}}^2", font_size=FONT_SIZE*.9)
        answer.move_to(rect.get_center())
        self.play(
            square[0].animate.set_opacity(0),
            TransformFromCopy(rect_area[-1], answer[0])
        )
        self.wait()

        four_copy = areas_of_small_squares[0].copy().move_to(square[0].get_center())

        self.play(
            square[0].animate.set_opacity(1).set_fill_color(RED),
            square_copy[0].animate.set_opacity(1).set_fill_color(RED),
            FadeIn(four_copy)
        )
        self.play(
            Write(answer[1:3])
        )
        self.wait()
        self.play(Write(answer[3:]))
        self.wait()

        self.play(Indicate(answer[-1]))

        self.wait(2)
