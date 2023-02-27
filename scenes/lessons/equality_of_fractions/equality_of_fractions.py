from manim import Scene, FadeIn, Line, GrowFromPoint, Circle, AnimationGroup, VGroup, MathTex, Line, ReplacementTransform, Write, Transform
from ..reducing_fractions.reducing_fractions import getFractionsOnCircle
from objects import SimpleSVGMobject, SVGMobject
from manim import PI
from manim import UP, DL, DOWN, DR
from manim import BLACK, ORANGE, BLUE

FONT_SIZE = 160

class Equality_of_fractions(Scene):
    """Վիդեոյի նպատակն է ցույց տալ կոտորակների հավասարությունը։"""
    def construct(self):
        # test = VGroup(
        #     SVGMobject("objects/SVG_files/schoolboy/schoolboy_1.svg").scale(2).set_stroke(width=1),
        #     SVGMobject("objects/SVG_files/schoolboy/schoolboy_2.svg").scale(2).set_stroke(width=1),
        #     SVGMobject("objects/SVG_files/books/book_colored_1.svg"),
        #     SVGMobject("objects/SVG_files/books/book_colored_2.svg"),
        #     SVGMobject("objects/SVG_files/books/book_colored_3.svg").set_stroke(width=1),
        # ).arrange()
        # self.add(test)
        # return

        self.wait()

        # draw pizza
        circle = Circle(2).to_edge(UP)
        pizza_svg = SimpleSVGMobject("pizza_full_1")
        pizza_svg.move_to(circle).match_height(circle).match_width(circle)
        self.play(FadeIn(pizza_svg))
        self.wait()

        # cut pizza (4 piece)
        line1 = Line(color=BLACK, stroke_width=8).set_length(pizza_svg.height).move_to(pizza_svg.get_center())
        line2 = line1.copy().rotate(PI/2)
        self.play(GrowFromPoint(line1, line1.get_start()))
        self.play(GrowFromPoint(line2, line2.get_start()))
        self.wait()

        # eat pizza
        sectors = getFractionsOnCircle(-1/4, circle, number_of_sectors=4, start_angle=PI/2, stroke_width=7, numbering=True)
        group1 = sectors[0][:3]
        group1_nums = sectors[1][:3]
        group1.set_fill(BLACK)
        group2 = sectors[0][3]
        group2_nums = sectors[1][3]
        group2.set_fill(BLUE)
        self.play(
            AnimationGroup(
                *[
                    FadeIn(group1[i])
                    for i in range(len(group1))
                ],
                lag_ratio=.5
            )
        )
        self.wait()

        # fadein sectors and remove pizza
        self.play(group1.animate.set_fill(ORANGE))
        self.wait()
        self.play(FadeIn(group2))
        self.remove(pizza_svg)
        self.wait()
        self.play(
            AnimationGroup(
                *[Write(num) for num in sectors[1]],
                lag_ratio=.2,
                run_time=1
            )
        )
        self.wait()

        # writing 3/4
        fraction1 = VGroup(
            MathTex("3", font_size=FONT_SIZE, color=ORANGE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("4", font_size=FONT_SIZE, color=BLUE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction1.to_corner(DL, buff=1.3)
        
        temp1 = VGroup(group1, group1_nums).copy()
        temp2 = sectors.copy()

        self.play(temp1.animate.scale(.5).move_to(fraction1[0].get_center()).align_to(fraction1[0], DOWN))
        self.play(Write(fraction1[1]))
        self.play(temp2.animate.scale(.5).move_to(fraction1[2].get_center()).align_to(fraction1[2], UP))
        self.wait()

        self.play(ReplacementTransform(temp1, fraction1[0]))
        self.wait()
        self.play(ReplacementTransform(temp2, fraction1[2]))
        self.wait()

        self.remove(*sectors, temp1, temp2, group1_nums, group2_nums)
        print(self.mobjects)

        # show 6/8 on the circle
        new_sectors = getFractionsOnCircle(-1/8, circle, number_of_sectors=8, start_angle=PI/2, stroke_width=7, numbering=True)
        group1 = new_sectors[0][:6]
        group1.set_fill(ORANGE)
        group1_nums = new_sectors[1][:6]
        group2 = new_sectors[0][6:]
        group2.set_fill(BLUE)
        group2_nums = new_sectors[1][6:]
        self.play(FadeIn(new_sectors[0]))
        self.remove(*sectors)
        self.wait()
        self.play(
            AnimationGroup(
                *[Write(num) for num in new_sectors[1]],
                lag_ratio=.2,
                run_time=1
            )
        )
        self.wait()

        # write 6/8
        fraction2 = VGroup(
            MathTex("6", font_size=FONT_SIZE, color=ORANGE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("8", font_size=FONT_SIZE, color=BLUE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction2.to_edge(DR, buff=1.3)

        temp1 = VGroup(group1, group1_nums).copy()
        temp2 = new_sectors.copy()
        self.play(temp1.animate.scale(.5).move_to(fraction2[0].get_center()).align_to(fraction2[0], DOWN))
        self.play(Write(fraction2[1]))
        self.play(temp2.animate.scale(.5).move_to(fraction2[2].get_center()).align_to(fraction2[2], UP))
        self.wait()

        self.play(ReplacementTransform(temp1, fraction2[0]))
        self.wait()
        self.play(Transform(temp2, fraction2[2]))
        self.add(fraction2[2])
        self.remove(temp2)
        self.wait()

        # show 9/12 on the circle
        self.play(FadeIn(sectors[0]))
        self.wait()
        self.remove(*new_sectors, temp1, temp2, group1_nums, group2_nums)
        
        new_sectors = getFractionsOnCircle(-1/12, circle, number_of_sectors=12, start_angle=PI/2, stroke_width=7, numbering=True, numbering_font_size=60)
        group1 = new_sectors[0][:9].set_fill(ORANGE)
        group1_nums = new_sectors[1][:9]
        group2 = new_sectors[0][9:].set_fill(BLUE)
        group2_nums = new_sectors[1][9:]
        self.play(FadeIn(new_sectors[0]))
        self.remove(sectors[0])
        self.wait()
        self.play(
            AnimationGroup(
                *[Write(num) for num in new_sectors[1]],
                lag_ratio=.2,
                run_time=1
            )
        )
        self.wait()

        # write 9/12
        fraction3 = VGroup(
            MathTex("9", font_size=FONT_SIZE, color=ORANGE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("12", font_size=FONT_SIZE, color=BLUE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction3.to_edge(DOWN, buff=1.3)
        fraction3[1].scale_to_fit_width(fraction3[2].width)
        
        temp1 = VGroup(group1, group1_nums).copy()
        temp2 = new_sectors

        self.play(
            temp1.animate.scale(.5).move_to(fraction3[0].get_center()).align_to(fraction3[0], DOWN),
            Write(fraction3[1]),
            temp2.animate.scale(.5).move_to(fraction3[2].get_center()).align_to(fraction3[2], UP)
        )
        self.wait()

        self.play(ReplacementTransform(temp1, fraction3[0]))
        self.wait()
        self.play(ReplacementTransform(temp2, fraction3[2]))
        self.wait()


        # add =
        equal1 = MathTex("=", font_size=2*FONT_SIZE)
        equal2 = equal1.copy()
        equal1.move_to(VGroup(fraction1, fraction3).get_center())
        equal2.move_to(VGroup(fraction2, fraction3).get_center())
        self.play(
            Write(equal1),
            Write(equal2)
        )

        self.wait(2)
