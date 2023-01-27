from manim import *

class ASquaredMinusBSquared(Scene):
    def construct(self):

        a = 4.5 # length of the sides of the big square
        b = 1.75 # length of the sides of the small square
        
        # vertices of polygons
        ul = np.array([-a/2, a/2, 0])
        dl = np.array([-a/2, -a/2, 0])
        ur = np.array([a/2, a/2, 0])
        dr = np.array([a/2, -a/2, 0])
        dm = np.array([a/2-b, -a/2, 0])
        rm = np.array([a/2, -(a/2-b), 0])
        mm = np.array([a/2-b, -(a/2-b), 0])
        lm = np.array([-a/2, -(a/2-b), 0])
        um = np.array([a/2-b, a/2, 0])
        
        # square with side a
        square_a = Polygon(ul, dl, dr, ur, color=GREEN, fill_opacity=0.5)
        side_a_up = Tex('$a$', font_size=70).next_to(square_a, UP)
        side_a_left = Tex('$a$', font_size=70).next_to(square_a, LEFT)
        area_a = Tex('$a^2$', font_size=70).move_to(square_a)

        self.play(Create(square_a))
        self.wait(0.25)
        self.play(Write(side_a_left), Write(side_a_up))
        self.wait(0.5)
        self.play(Write(area_a))
        self.wait()

        # square with side b
        square_b = Polygon(rm, mm, dm, dr, color=ORANGE, fill_opacity=0.5)
        side_b_down = Tex('$b$', font_size=60).next_to(square_b, DOWN)
        side_b_right = Tex('$b$', font_size=60).next_to(square_b, RIGHT)
        area_b = Tex('$b^2$', font_size=70).move_to(square_b)

        self.play(Create(square_b))
        self.wait(0.25)
        self.play(Write(side_b_down), Write(side_b_right))
        self.wait(0.5)
        self.play(Write(area_b))
        self.wait()

        # polygon we get by subtracting a^2 and b^2
        difference_polygon = Polygon(ul, dl, dm, mm, rm, ur, color=GREEN, fill_opacity=0.5)
        area_polygon = Tex('$a^2$', '$-$', '$b^2$', font_size=70).move_to(square_a).shift([-0.5, 0.25, 0])

        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeIn(difference_polygon), FadeOut(square_a, square_b),
                    ReplacementTransform(area_a, area_polygon[:1]),
                    ReplacementTransform(area_b, area_polygon[2:3])
                ),
                Write(area_polygon[1]),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(side_b_right.animate.shift([-b-0.1, -0.05, 0]))
        self.wait(0.25)
        self.play(side_b_down.animate.shift([0.05, b+0.1, 0]))
        self.wait()

        # write S = a^2-b^2 in top left corner
        s_equals_difference = Tex('$S$', ' $=$ ', '$a^2$', '$-$', '$b^2$', font_size=70)
        s_equals_difference.to_corner(UL)

        self.play(Write(s_equals_difference[:2]))
        self.wait(0.1)
        self.play(ReplacementTransform(area_polygon[0:3], s_equals_difference[2:5]))
        self.wait()

        # brace sides of polygon with length a-b
        # right side
        brace_right = BraceBetweenPoints(ur, rm, RIGHT)
        side_a_minus_b_right = Tex('$a$$-$$b$', font_size=70)
        side_a_minus_b_right.next_to(brace_right, RIGHT)

        self.play(Write(brace_right))
        self.wait(0.25)
        self.play(Write(side_a_minus_b_right))
        self.wait()
        self.play(
            FadeOut(brace_right),
            side_a_minus_b_right.animate.shift(LEFT * 0.5)
        )
        self.wait()

        # down side
        brace_down = BraceBetweenPoints(dl, dm, DOWN)
        side_a_minus_b_down = Tex('$a$$-$$b$', font_size=70)
        side_a_minus_b_down.next_to(brace_down, DOWN)

        self.play(Write(brace_down))
        self.wait(0.25)
        self.play(Write(side_a_minus_b_down))
        self.wait()
        self.play(
            FadeOut(brace_down),
            side_a_minus_b_down.animate.shift(UP * 0.5)
        )
        self.wait()

        # divide polygon into a square with side a-b and 2 rectangles with sides (a-b)•b
        vertical_dashed_line = DashedLine(mm, um)
        horizontal_dashed_line = DashedLine(mm, lm)

        self.play(Create(vertical_dashed_line))
        self.wait()
        self.play(Create(horizontal_dashed_line))
        self.wait()

        # replace polygon with 2 rectangles - (a-b)•a and (a-b)•b
        big_rectangle = Polygon(ur, ul, lm, rm, color=GREEN, fill_opacity=0.5)
        lines_of_bottom_rectangle = VGroup(
            Line(lm, dl, color=GREEN),
            Line(dl, dm, color=GREEN),
            Line(dm, mm, color=GREEN),
            horizontal_dashed_line
        )

        fill_of_bottom_rectangle = Polygon(mm, lm, dl, dm, color=GREEN, stroke_width=0, fill_opacity=0.5)

        bottom_rectangle = VGroup(fill_of_bottom_rectangle, lines_of_bottom_rectangle)
        bottom_rectangle_with_side_lengths = VGroup(bottom_rectangle, side_a_minus_b_down, side_b_right)

        self.remove(difference_polygon)
        self.add(big_rectangle, vertical_dashed_line, bottom_rectangle)
        self.play(
            bottom_rectangle_with_side_lengths.animate(rate_func=linear).shift(DOWN * 0.75),
            FadeOut(side_a_left)
        )
        self.wait(0.5)
        self.play(bottom_rectangle_with_side_lengths.animate(rate_func=linear).shift(RIGHT * 5.55))
        self.wait()

        self.play(
            Rotating(bottom_rectangle, radians=PI/2, run_time=1),
            CounterclockwiseTransform(
                side_b_right,
                side_b_right.copy().move_to(bottom_rectangle).shift((a/2 - b/2 + 0.45) * UP),
                PI/2, rate_func=linear
            ),
            CounterclockwiseTransform(
                side_a_minus_b_down,
                side_a_minus_b_down.copy().move_to(bottom_rectangle).shift((b/2 + 0.73) * RIGHT),
                PI/2, rate_func=linear
            )
            # side_b_right.animate.move_to(bottom_rectangle).shift((a/2 - b/2 + 0.45) * UP),
            # side_a_minus_b_down.animate.move_to(bottom_rectangle).shift((b/2 + 0.73) * RIGHT)
        )
        self.wait()
        self.play(bottom_rectangle_with_side_lengths.animate(rate_func=linear).align_to(big_rectangle, DOWN))
        self.wait()
        self.play(
            bottom_rectangle_with_side_lengths.animate(rate_func=linear).next_to(big_rectangle, RIGHT, buff=0, aligned_edge=DOWN),
            FadeOut(side_a_minus_b_right, side_b_down, vertical_dashed_line)
        )
        self.wait()
