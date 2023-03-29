from manim import Scene, FadeIn, GrowFromPoint, Circle, AnimationGroup, VGroup, MathTex, Line, ReplacementTransform, Write, Transform, Rectangle, FadeOut, ValueTracker
from utilities import getFractionsOnCircle
from objects import SimpleSVGMobject
from manim import PI
from manim import UP, DL, DOWN, LEFT, RIGHT
from manim import BLACK, ORANGE, BLUE

FONT_SIZE = 160

class Equality_of_fractions(Scene):
    """Վիդեոյի նպատակն է ցույց տալ կոտորակների հավասարությունը։"""
    def construct(self):
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
            MathTex("-", font_size=FONT_SIZE).scale(2),
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
        self.play(
            ReplacementTransform(temp2, fraction1[2]),
            fraction1[1].animate.scale(.5)
        )
        self.wait()

        # movig circle left
        self.play(sectors.animate.to_edge(RIGHT))
        self.wait()
        circle.move_to(sectors.get_center())

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
            MathTex("-", font_size=FONT_SIZE).scale(2),
            MathTex("8", font_size=FONT_SIZE, color=BLUE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction2.to_edge(DOWN, buff=1.3)

        temp1 = VGroup(group1, group1_nums).copy()
        temp2 = new_sectors.copy()
        self.play(temp1.animate.scale(.5).move_to(fraction2[0].get_center()).align_to(fraction2[0], DOWN))
        self.play(Write(fraction2[1]))
        self.play(temp2.animate.scale(.5).move_to(fraction2[2].get_center()).align_to(fraction2[2], UP))
        self.wait()

        self.play(ReplacementTransform(temp1, fraction2[0]))
        self.wait()
        self.play(
            ReplacementTransform(temp2, fraction2[2]),
            fraction2[1].animate.scale(.5)
        )
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
            MathTex("-", font_size=FONT_SIZE).scale(2),
            MathTex("12", font_size=FONT_SIZE, color=BLUE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction3.move_to(circle.get_center())#.to_edge(DR, buff=1.3)
        
        temp1 = VGroup(group1, group1_nums).copy()
        temp2 = new_sectors

        # ձեռք չտալ !!!
        # թքած կպցրած (start)
        rect = Rectangle(width=3, height=3.5).move_to(new_sectors)
        rect.set_opacity(1).set_color(BLACK)
        new_sectors.set_z_index(rect.z_index+1)
        self.add(rect)
        # թքած կպցրած (end)

        self.play(
            temp1.animate.scale(.5).move_to(fraction3[0].get_center()).align_to(fraction3[0], DOWN),
            Write(fraction3[1]),
            temp2.animate.scale(.5).move_to(fraction3[2].get_center()).align_to(fraction3[2], UP)
        )
        self.wait()

        self.play(ReplacementTransform(temp1, fraction3[0]))
        self.wait()
        self.play(
            ReplacementTransform(temp2, fraction3[2]),
            fraction3[1].animate.scale_to_fit_width(fraction3[2].width)
        )
        self.wait()

        # move up first 2 fractions and add =
        equal1 = MathTex("=", font_size=FONT_SIZE)
        equal1.move_to(VGroup(fraction1, fraction2).get_center()).set_opacity(0)

        equal2 = equal1.copy()
        equal2.move_to(VGroup(fraction2, fraction3).get_center())

        self.play(
            VGroup(
                fraction1,
                fraction2,
                equal2
            ).animate.set_y(fraction3.get_y()),
            equal1.animate.set_opacity(1).set_y(fraction3.get_y()),
            equal2.animate.set_opacity(1).set_y(fraction3.get_y())
        )
        self.wait()

        # transform 6/8 to (2*3)/(2*4)
        temp1 = MathTex("2 \\cdot", "3", font_size=FONT_SIZE)
        temp1[-1].set_color(ORANGE)
        temp1.move_to(fraction2[0].get_center()).align_to(fraction2[1], RIGHT),

        temp2 = MathTex("2 \\cdot", "4", font_size=FONT_SIZE)
        temp2[-1].set_color(BLUE)
        temp2.move_to(fraction2[2].get_center()).align_to(fraction2[1], RIGHT),

        self.play(
            Transform(fraction2[0], temp1),
            Transform(fraction2[2], temp2),
            fraction2[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction2[1], RIGHT),
            equal1.animate.next_to(fraction1, buff=.45)
        )
        self.wait()

        # transform 9/12 to (3*3)/(3*4)
        temp1 = MathTex("3 \\cdot", "3", font_size=FONT_SIZE)
        temp1[-1].set_color(ORANGE)
        temp1.move_to(fraction3[0].get_center()).align_to(fraction3[1], RIGHT)

        temp2 = MathTex("4 \\cdot", "4", font_size=FONT_SIZE)
        temp2[-1].set_color(BLUE)
        temp2.move_to(fraction3[2].get_center()).align_to(fraction3[1], RIGHT)

        self.play(
            Transform(fraction3[0], temp1),
            Transform(fraction3[2], temp2),
            fraction3[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction3[1], RIGHT),
            equal2.animate.next_to(fraction2, buff=.55)
        )
        self.wait()

        # (4*3)/(4*4)
        val_tracker = ValueTracker(0)
        equal3 = equal1.copy()
        equal3.next_to(fraction3).set_opacity(0)
        equal3.add_updater(
            lambda x: x.set_opacity(val_tracker.get_value())
        )
        self.add(equal3)

        self.play(
            VGroup(
                fraction1,
                equal1,
                fraction2,
                equal2,
                fraction3,
                equal3
            ).animate.scale(.85).to_edge(LEFT),
            val_tracker.animate.set_value(1)
        )
        self.wait()

        equal3.clear_updaters()

        fraction4 = VGroup(
            MathTex("4 \\cdot", "3", font_size=FONT_SIZE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("4 \\cdot", "4", font_size=FONT_SIZE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction4[1].stretch_to_fit_width(fraction4[2].width)
        fraction4[0][-1].set_color(ORANGE)
        fraction4[2][-1].set_color(BLUE)
        fraction4.scale(.85).next_to(equal3)

        self.play(Write(fraction4))
        self.wait()

        # (5*3)/(5*4)
        val_tracker.set_value(0)
        equal4 = equal1.copy()
        equal4.next_to(fraction4).set_opacty(0)
        equal4.add_updater(
            lambda x: x.set_opacity(val_tracker.get_value())
        )
        self.add(equal4)

        self.play(
            VGroup(
                fraction1,
                equal1,
                fraction2,
                equal2,
                fraction3,
                equal3,
                fraction4,
                equal4
            ).animate.scale(.8).to_edge(LEFT, buff=.2),
            val_tracker.animate.set_value(1)
        )
        self.wait()

        equal4.clear_updaters()

        fraction5 = VGroup(
            MathTex("5 \\cdot", "3", font_size=FONT_SIZE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("5 \\cdot", "4", font_size=FONT_SIZE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction5[1].stretch_to_fit_width(fraction5[2].width)
        fraction5[0][-1].set_color(ORANGE)
        fraction5[2][-1].set_color(BLUE)
        fraction5.scale(.65).next_to(equal4)

        self.play(Write(fraction5))
        self.wait()

        # add "= ..."
        val_tracker.set_value(0)
        equal5 = equal1.copy()
        equal5.next_to(fraction5).set_opacity(0)
        equal5.add_updater(
            lambda x: x.set_opacity(val_tracker.get_value())
        )
        self.add(equal5)

        self.play(
            VGroup(
                fraction1,
                equal1,
                fraction2,
                equal2,
                fraction3,
                equal3,
                fraction4,
                equal4,
                fraction5,
                equal5
            ).animate.scale(.85).to_edge(LEFT, buff=.2),
            val_tracker.animate.set_value(1)
        )
        self.wait()

        equal5.clear_updaters()

        bazmaketer = MathTex("...", font_size=FONT_SIZE)
        bazmaketer.next_to(equal5)
        self.play(Write(bazmaketer))
        self.wait()

        # transform (2*3)/(2*4) to 6/8
        temp1 = MathTex("6")
        temp1.match_height(fraction2[0]).move_to(fraction2[0].get_center()).set_color(ORANGE)
        temp2 = MathTex("8")
        temp2.match_height(fraction2[2]).move_to(fraction2[2].get_center()).set_color(BLUE)
        VGroup(temp1, temp2).align_to(fraction2[1], LEFT)
        
        self.play(
            Transform(fraction2[0], temp1),
            Transform(fraction2[2], temp2),
            fraction2[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction2[1], LEFT),
            VGroup(
                equal2,
                fraction3,
                equal3,
                fraction4,
                equal4,
                fraction5,
                equal5,
                bazmaketer
            ).animate.next_to(VGroup(temp1, temp2))
        )
        self.wait()

        # transform (3*3)/(3*4) to 9/12
        temp1 = MathTex("9")
        temp1.match_height(fraction3[0]).move_to(fraction3[0].get_center()).set_color(ORANGE)
        temp2 = MathTex("12")
        temp2.match_height(fraction3[2]).move_to(fraction3[2].get_center()).set_color(BLUE)
        VGroup(temp1, temp2).align_to(fraction3[1], LEFT)
        
        self.play(
            Transform(fraction3[0], temp1),
            Transform(fraction3[2], temp2),
            fraction3[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction3[1], LEFT),
            VGroup(
                equal3,
                fraction4,
                equal4,
                fraction5,
                equal5,
                bazmaketer
            ).animate.next_to(VGroup(temp1, temp2))
        )
        self.wait()

        # transform (4*3)/(4*4) to 12/16
        temp1 = MathTex("12")
        temp1.match_height(fraction4[0]).move_to(fraction4[0].get_center()).set_color(ORANGE)
        temp2 = MathTex("16")
        temp2.match_height(fraction4[2]).move_to(fraction4[2].get_center()).set_color(BLUE)
        VGroup(temp1, temp2).align_to(fraction4[1], LEFT)
        
        self.play(
            Transform(fraction4[0], temp1),
            Transform(fraction4[2], temp2),
            fraction4[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction4[1], LEFT),
            VGroup(
                equal4,
                fraction5,
                equal5,
                bazmaketer
            ).animate.next_to(VGroup(temp1, temp2))
        )
        self.wait()

        # transform (5*3)/(5*4) to 15/20
        temp1 = MathTex("15")
        temp1.match_height(fraction5[0]).move_to(fraction5[0].get_center()).set_color(ORANGE)
        temp2 = MathTex("20")
        temp2.match_height(fraction5[2]).move_to(fraction5[2].get_center()).set_color(BLUE)
        VGroup(temp1, temp2).align_to(fraction5[1], LEFT)
        
        self.play(
            Transform(fraction5[0], temp1),
            Transform(fraction5[2], temp2),
            fraction5[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction5[1], LEFT),
            VGroup(equal5, bazmaketer).animate.next_to(VGroup(temp1, temp2))
        )
        self.wait()

        # (55*3)/(55*4)
        equal6 = equal1.copy().next_to(bazmaketer)
        fraction6 = VGroup(
            MathTex("55 \\cdot", "3", font_size=FONT_SIZE),
            MathTex("-", font_size=FONT_SIZE),
            MathTex("55 \\cdot", "4", font_size=FONT_SIZE)
        ).arrange_in_grid(rows=3, cols=1)
        fraction6[1].stretch_to_fit_width(fraction6[2].width)
        fraction6[0][-1].set_color(ORANGE)
        fraction6[2][-1].set_color(BLUE)
        fraction6.match_height(fraction1).next_to(equal6)
        
        self.play(Write(equal6))
        self.play(Write(fraction6))
        self.wait()

        # = 165/220 = ...
        self.play(
            FadeOut(equal6, bazmaketer),
            fraction6.animate.next_to(equal5)
        )
        self.wait()
        
        temp1 = MathTex("165", color=ORANGE)
        temp2 = MathTex("220", color=BLUE)
        temp1.match_height(fraction6[0]).move_to(fraction6[0].get_left(), aligned_edge=LEFT)
        temp2.match_height(fraction6[2]).move_to(fraction6[2].get_left(), aligned_edge=LEFT)

        self.play(
            Transform(fraction6[0], temp1),
            Transform(fraction6[2], temp2),
            fraction6[1].animate.stretch_to_fit_width(temp2.width).align_to(fraction6[1], LEFT)
        )
        self.wait()

        equal6.next_to(fraction6)
        bazmaketer.next_to(equal6)
        self.play(Write(VGroup(equal6, bazmaketer)))

        self.wait(2)
