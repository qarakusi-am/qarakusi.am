from manim import Scene, Write, MathTex, Circle, AnnularSector, VGroup, FadeIn, AnimationGroup, Indicate, Point, ReplacementTransform, Line, FadeOut, TransformFromCopy, GrowFromPoint
from manim import ORANGE, ORIGIN, BLACK, BLUE, YELLOW_E
from manim import UP, UR, DOWN, LEFT, UL
from manim import PI, TAU
from numpy import array
from objects import SimpleSVGMobject
from .text import fraction_tex

class ReducingFraction(Scene):
    def construct(self):
        self.wait()
        
        def getFractionsOnCircle(fraction, circle, color=ORANGE, number_of_sectors=1, stroke_width=5, stroke_color=BLACK, numbering=False, numbering_font_size=None, start_angle=0):
            """make sure your circle has the same stroke_width and stroke_color as your sectors"""

            sectors = VGroup()
            if numbering:
                numbers = VGroup()
            
            radius = circle.radius
            angle = TAU * fraction
            if numbering and numbering_font_size==None:
                numbering_font_size = radius * 44
            
            coordinates = circle.get_center()
            circle.move_to(ORIGIN)

            for sector_number in range(number_of_sectors):
                sector = AnnularSector(
                    inner_radius=0,
                    outer_radius=radius,
                    angle=angle,
                    start_angle=sector_number*angle+start_angle,
                    stroke_width=stroke_width,
                    stroke_color=stroke_color,
                    color=color
                )
                sectors.add(sector)
                if numbering:
                    number = MathTex(f"{sector_number+1}", font_size=numbering_font_size)
                    coord = array([radius, 0, 0])*2/3
                    point = Point().move_to(coord)
                    point.rotate(sector_number*angle+angle/2+start_angle, about_point=circle.get_center())
                    number.move_to(point.get_center())
                    numbers.add(number)

            to_coordinates = VGroup(sectors, circle)
            if numbering:
                to_coordinates.add(numbers)
            to_coordinates.move_to(coordinates)

            if numbering:
                return VGroup(sectors, numbers)
            else:
                return sectors
        
        # FadeIn pizza
        circle = Circle(2.5, fill_opacity=1, color=YELLOW_E, stroke_width=5, stroke_color=BLACK)
        pizza_svg = SimpleSVGMobject("pizza_full_1")
        pizza_svg.match_height(circle).match_width(circle)
        self.play(FadeIn(pizza_svg))
        self.wait()

        # cut pizza
        lines = [
            Line(stroke_width=5, color=BLACK).match_width(circle).move_to(circle.get_center()).rotate(i*TAU/8)
            for i in range(4)
        ]
        cutting_animation = AnimationGroup(
            *[
                GrowFromPoint(lines[i], lines[i].get_start())
                for i in range(len(lines))
            ],
            lag_ratio=.6
        )
        self.play(cutting_animation)
        self.wait()

        # showing 1/8
        sectors_and_numbers = getFractionsOnCircle(-1/8, circle, number_of_sectors=8, numbering=True, color=YELLOW_E, start_angle=PI/2)
        sectors = sectors_and_numbers[0]
        numbers = sectors_and_numbers[1]
        sectors_animation = AnimationGroup(
            *[FadeIn(sector.set_color(BLACK)) for sector in sectors[:6]],
            lag_ratio=.4
        )
        self.play(sectors_animation)
        self.wait()

        # painting
        group1 = VGroup(sectors[:6], numbers[:6])
        group2 = VGroup(sectors[6:], numbers[6:])
        group2[0].set_fill(ORANGE)
        self.play(group1[0].animate.set_fill(BLUE))
        self.wait()
        self.play(FadeIn(group2[0]))
        self.wait()

        # remove the pizza and cutting in back
        self.remove(pizza_svg, *lines)

        # numbering
        numbering = AnimationGroup(
            *[Write(number) for number in numbers],
            lag_ratio=.6,
            run_time=1.2
        )
        self.play(numbering)
        self.wait()

        # fraction 1:  6/8
        fraction1 = VGroup(
            MathTex("6", font_size=160),
            MathTex("-", font_size=160),
            MathTex("8", font_size=160)
        ).arrange_in_grid(rows=3, cols=1)
        fraction1.next_to(circle, LEFT, buff=2.8)
        
        self.play(Indicate(group1, color=None))
        self.wait()
        temp1 = group1.copy()
        self.play(temp1.animate.scale(.5).move_to(fraction1[0].get_center()).align_to(fraction1[0], DOWN))
        self.wait()
        self.play(Write(fraction1[1]))
        self.wait()
        self.play(Indicate(sectors_and_numbers, color=None))
        self.wait()
        temp2 = sectors_and_numbers.copy()
        self.play(temp2.animate.scale(.5).move_to(fraction1[2].get_center()).align_to(fraction1[2], UP))
        self.wait()

        self.play(ReplacementTransform(temp1, fraction1[0]))
        self.wait()
        self.play(ReplacementTransform(temp2, fraction1[2]))
        self.wait()
        
        fraction1_tex = fraction_tex.copy()
        fraction1_tex.next_to(fraction1)
        self.play(Write(fraction1_tex))
        self.wait()

        # scale circle and fraction and move to corner
        self.play(VGroup(sectors_and_numbers, fraction1, fraction1_tex).animate.shift(DOWN*.6))
        self.wait()

        circle_and_fraction_copy1 = VGroup(
            sectors_and_numbers.copy(),
            fraction1.copy().next_to(sectors_and_numbers, LEFT)
        ).scale(.45).to_corner(UL)
        self.play(
            ReplacementTransform(
                VGroup(sectors_and_numbers, fraction1).copy(),
                circle_and_fraction_copy1
            )
        )
        self.wait()

        # fraction 2:  3/4
        circle.move_to(sectors_and_numbers.get_center())
        new_numbers = getFractionsOnCircle(-1/4, circle, number_of_sectors=4, numbering=True, start_angle=PI/2, numbering_font_size=180)[1]
        line1 = Line(stroke_width=15, color=BLACK)
        line1.match_width(circle).move_to(circle.get_center())
        line2 = line1.copy().rotate(PI/2)
        self.play(
            FadeIn(line1, line2),
            FadeOut(numbers)
        )
        self.wait()
        new_numbering = AnimationGroup(
            *[Write(number) for number in new_numbers],
            lag_ratio=.6,
            run_time=1
        )
        self.play(new_numbering)
        self.wait()
        
        fraction2 = VGroup(
            MathTex("3", font_size=160),
            MathTex("-", font_size=160),
            MathTex("4", font_size=160)
        ).arrange_in_grid(rows=3, cols=1)
        fraction2.next_to(circle, buff=.7)

        temp1 = VGroup(group1[0], new_numbers[:3], line1, line2).copy()
        temp2 = VGroup(sectors_and_numbers[0], new_numbers, line1, line2).copy()
        frac2_animation = AnimationGroup(
            temp1.animate.scale(.5).move_to(fraction2[0].get_center()).align_to(fraction2[0], DOWN),
            Write(fraction2[1]),
            temp2.animate.scale(.5).move_to(fraction2[2].get_center()).align_to(fraction2[2], UP),
            lag_ratio=0
        )
        self.play(frac2_animation)

        self.wait()
        self.play(ReplacementTransform(temp1, fraction2[0]))
        self.wait()
        self.play(ReplacementTransform(temp2, fraction2[2]))
        self.wait()
        
        fraction2_tex = fraction_tex.copy()
        fraction2_tex.next_to(fraction2)
        self.play(Write(fraction2_tex))
        self.wait()

        # scale 2nd circle and fraction and move to corner
        circle_and_fraction_copy2 = VGroup(fraction2.copy().next_to(sectors_and_numbers), sectors_and_numbers[0], new_numbers, line1, line2).copy()
        circle_and_fraction_copy2.scale(.45).to_corner(UR)
        self.play(
            ReplacementTransform(
                VGroup(fraction2, sectors_and_numbers[0], new_numbers, line1, line2).copy(),
                circle_and_fraction_copy2
            )
        )
        self.wait()

        # transform circle to equal
        equal_tex = MathTex("=", font_size=250).move_to(circle.get_center())
        self.play(
            ReplacementTransform(
                VGroup(sectors_and_numbers[0], new_numbers, line1, line1),
                equal_tex
            )
        )

        # կրճատելու ձևը
        self.play(
            FadeOut(
                circle_and_fraction_copy1,
                circle_and_fraction_copy2
            )
        )
        self.play(
            VGroup(
                fraction1,
                fraction1_tex,
                fraction2,
                fraction2_tex,
                equal_tex
            ).animate.scale(.8).to_edge(UP)
        )
        self.wait()

        tex1 = MathTex("\\frac{6}{8}", "=", "\\frac{6:2}{8:2}", "=", "\\frac{3}{4}", font_size=140)
        tex1.next_to(
            VGroup(
                fraction1,
                fraction1_tex,
                fraction2,
                fraction2_tex,
                equal_tex
            ),
            DOWN, buff=.8
        )

        self.play(TransformFromCopy(fraction1, tex1[0]))
        self.wait()
        self.play(Write(tex1[1]))
        self.wait()
        self.play(Write(tex1[2]))
        self.wait()
        self.play(Write(tex1[3]))
        self.wait()
        self.play(TransformFromCopy(fraction2, tex1[-1]))
        
        self.wait(2)
