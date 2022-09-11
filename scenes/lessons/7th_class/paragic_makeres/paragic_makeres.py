from manim import *

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r'\usepackage{armtex}')

class ParagicMakeres(Scene):
    def construct(self):

# INITS

    # rect angle with sides 3, 7 than a, b
        rect = Rectangle(WHITE, 3, 7).scale(0.7).to_edge(UP).shift(DOWN)
        rect_verts = rect.get_vertices()

        rect_sides = VGroup(
            Line(rect_verts[1], rect_verts[2], color=ORANGE),
            Line(rect_verts[2], rect_verts[3], color=ORANGE),
            Line(rect_verts[3], rect_verts[0], color=ORANGE),
            Line(rect_verts[0], rect_verts[1], color=ORANGE),
        )
    # արտահայտություններ 3 ու 7-ով
        sides_3 = VGroup(
            Tex('3').next_to(rect, LEFT),
            Tex('3').next_to(rect, RIGHT)
        )
        sides_7 = VGroup(
            Tex('7').next_to(rect, DOWN),
            Tex('7').next_to(rect, UP)
        )

        paragic_3_7 = Tex('3', ' + ', '7', ' + ', '3', ' + ', '7', ' = ', '20')
        paragic_3_7.next_to(sides_7[0], DOWN, buff=0.75)
        makeres_3_7 = Tex('3 $\cdot$ 7 = 21').next_to(paragic_3_7, DOWN, buff=0.75)

    # արտահայտություններ a ու b-ով
        sides_a = VGroup(
            Tex('a').next_to(rect, LEFT),
            Tex('a').next_to(rect, RIGHT)
        )
        sides_b = VGroup(
            Tex('b').next_to(rect, DOWN),
            Tex('b').next_to(rect, UP)
        )

        paragic_a_b = VGroup(
            Tex('Պարագիծ - ', tex_template=ARMTEX),
            Tex('a+b+a+b')
        ).arrange(aligned_edge=DOWN)
        paragic_a_b[1].shift(0.07 * UP)
        paragic_a_b.next_to(sides_7[0], DOWN, buff=0.75)

        makeres_a_b = VGroup(
            Tex('Մակերես - ', tex_template=ARMTEX),
            Tex('a$\cdot$b')
        ).arrange(aligned_edge=DOWN)
        makeres_a_b[1].shift(0.07 * UP)
        makeres_a_b.next_to(paragic_a_b, DOWN, buff=1).shift(0.7 * LEFT)

        middle_dashed_line = DashedLine().scale(4).rotate(-PI/2).shift(0.25 * LEFT)

    #############
    # NEW SHAPE #
        new_shape = Polygon(
            rect_verts[1], rect_verts[2], rect_verts[3], 
            rect_verts[3] + np.array([0, 1, 0]),
            rect_verts[3] + np.array([-2, 1, 0]),
            rect_verts[0] + np.array([-2, 0, 0]),
            color=WHITE
        )
        new_shape.align_to(rect, UP).to_corner(RIGHT).shift([-1, 0, 0])

        new_shape_edges = VGroup(*[
            Line(new_shape.get_vertices()[i], new_shape.get_vertices()[(i+1) % 6]) 
            for i in range(6)
        ])

        new_shape_extra_segments = VGroup(
            new_shape_edges[3].copy().shift((3 * 0.7 - 1) * UP),
            new_shape_edges[4].copy().shift(2 * RIGHT)
        )

        new_shape_full_rectangle = Polygon(
            new_shape.get_vertices()[0],
            new_shape.get_vertices()[1],
            new_shape.get_vertices()[2],
            np.array([new_shape.get_vertices()[3][0], new_shape.get_vertices()[5][1], 0]),
            color=WHITE
        ).set_fill(GREEN, 0.75)

        new_shape_extra_rectangle = Polygon(
            new_shape.get_vertices()[3],
            new_shape.get_vertices()[4],
            new_shape.get_vertices()[5],
            np.array([new_shape.get_vertices()[3][0], new_shape.get_vertices()[5][1], 0]),
            color=WHITE
        ).set_fill(RED, 0.75)

        new_a = Tex('a').next_to(new_shape_edges[0], LEFT)
        new_b = Tex('b').next_to(new_shape_edges[1], DOWN)
        new_c = Tex('c').next_to(new_shape_edges[4], RIGHT, buff=0.15).set_z(new_shape_extra_rectangle.get_z() + 1)
        new_d = Tex('d').next_to(new_shape_edges[3], UP, buff=0.15).set_z(new_shape_extra_rectangle.get_z() + 1)
        new_a_minus_c = Tex('a', '-', 'c')
        new_b_minus_d = Tex('b', '-', 'd')

        brace_a = BraceBetweenPoints(new_shape.get_vertices()[2], new_shape.get_vertices()[5], RIGHT)
        brace_a_minus_c = BraceBetweenPoints(new_shape.get_vertices()[2], new_shape.get_vertices()[3], RIGHT)
        new_a_minus_c.next_to(brace_a, RIGHT)

        brace_b = BraceBetweenPoints(new_shape.get_vertices()[0], new_shape.get_vertices()[3], UP)
        brace_b_minus_d = BraceBetweenPoints(new_shape.get_vertices()[0], new_shape.get_vertices()[5], UP)
        new_b_minus_d.next_to(brace_b, UP).shift(0.19 * RIGHT)

        brace_c = BraceBetweenPoints(new_shape.get_vertices()[3], new_shape.get_vertices()[5], LEFT)
        brace_c.align_to(new_shape_edges[2], RIGHT)
        c_on_brace = new_c.copy().next_to(brace_c, LEFT, buff=0.1)

        brace_d = BraceBetweenPoints(new_shape.get_vertices()[5], new_shape.get_vertices()[3], DOWN)
        brace_d.align_to(new_shape_edges[5], UP)
        d_on_brace = new_d.copy().next_to(brace_d, DOWN, buff=0.1)

    # new shape paragic
        new_shape_paragic = VGroup(
            Tex('a', '+', '(', 'b', '-', 'd', ')', '+', 'c', '+', 'd', '+', '(', 'a', '-', 'c', ')', '+', 'b', '='),
            Tex('=', 'a', '+', 'b', '+', 'a', '+', 'b')
        )
        new_shape_paragic.arrange(DOWN).next_to(new_shape, DOWN, buff=1.25)

        surr_rect_d_1 = SurroundingRectangle(new_shape_paragic[0][4:6], buff=0.025).shift(0.18 * RIGHT)
        surr_rect_d_2 = SurroundingRectangle(new_shape_paragic[0][9:11], buff=0.025)

        krchatman_gcikner_1 = VGroup(
            Line(
                SurroundingRectangle(new_shape_paragic[0][5]).shift(0.18 * RIGHT).get_vertices()[1], 
                SurroundingRectangle(new_shape_paragic[0][5]).shift(0.18 * RIGHT).get_vertices()[3]
            ).scale(0.9),
            Line(
                SurroundingRectangle(new_shape_paragic[0][10]).get_vertices()[1], 
                SurroundingRectangle(new_shape_paragic[0][10]).get_vertices()[3]
            ).scale(0.9)
        )

        surr_rect_c_1 = SurroundingRectangle(new_shape_paragic[0][7:9], buff=0.025)
        surr_rect_c_2 = SurroundingRectangle(new_shape_paragic[0][14:16], buff=0.025)
        surr_rect_c_2.shift(0.18 * LEFT).stretch(1.4, 1)

        krchatman_gcikner_2 = VGroup(
            Line(
                SurroundingRectangle(new_shape_paragic[0][8]).get_vertices()[1], 
                SurroundingRectangle(new_shape_paragic[0][8]).get_vertices()[3]
            ).scale(0.9),
            Line(
                SurroundingRectangle(new_shape_paragic[0][15]).shift(0.18 * LEFT).get_vertices()[1], 
                SurroundingRectangle(new_shape_paragic[0][15]).shift(0.18 * LEFT).get_vertices()[3]
            ).scale(0.9)
        )
    
    # new shape makeres
        new_shape_makeres = Tex('a$\cdot$b', ' - ', 'c$\cdot$d')
        new_shape_makeres.next_to(new_shape_paragic, DOWN, buff=0.5)

        


# ANIMATIONS
    # պարագիծը հավասար է 3*7
        def animate_rect_3_7():

            self.add(rect, sides_3, sides_7)
            # self.play(Create(rect))
            # self.wait()

            # self.play(Write(sides_3))
            # self.wait(0.25)
            # self.play(Write(sides_7))
            self.wait()

            self.play(
                Create(rect_sides[0]),
                Write(paragic_3_7[0])
            )
            self.wait(0.1)
            self.play(
                AnimationGroup(
                    Create(rect_sides[1]),
                    Write(paragic_3_7[1:3]),
                    lag_ratio=0.5
                )
            )
            self.wait(0.1)

            self.play(
                AnimationGroup(
                    Create(rect_sides[2]),
                    Write(paragic_3_7[3:5]),
                    lag_ratio=0.5
                )
            )
            self.wait(0.1)

            self.play(
                AnimationGroup(
                    Create(rect_sides[3]),
                    Write(paragic_3_7[5:7]),
                    lag_ratio=0.5
                )
            )
            self.wait(0.25)

            self.play(
                Write(paragic_3_7[7:]),
                FadeOut(rect_sides)
            )
            self.wait()

            self.play(rect.animate.set_fill(opacity=0.75, color=ORANGE))
            self.play(Write(makeres_3_7, run_time=1.5, rate_func=linear))
            self.wait()
            self.play(rect.animate.set_fill(opacity=0, color=ORANGE))
            self.wait()

            self.play(FadeOut(paragic_3_7, makeres_3_7))
            self.wait(0.25)

        def animate_rect_a_b():
            self.play(ReplacementTransform(sides_3, sides_a))
            self.wait(0.25)
            self.play(ReplacementTransform(sides_7, sides_b))
            self.wait()

            self.play(Write(paragic_a_b[0], run_time=1.5, rate_func=linear))
            self.wait(0.5)
            self.play(Write(paragic_a_b[1], run_time=1.5, rate_func=linear))
            self.wait()

            self.play(Write(makeres_a_b[0], run_time=1.5, rate_func=linear))
            self.wait(0.5)
            self.play(Write(makeres_a_b[1], run_time=1.5, rate_func=linear))
            self.wait()

            self.play(VGroup(paragic_a_b, makeres_a_b, sides_a, sides_b, rect).animate.to_edge(LEFT))
            self.wait(0.5)

            self.play(Create(middle_dashed_line))
            self.wait()

    # new shape

        def animate_new_shape_paragic():
            self.play(Create(new_shape))
            self.add(new_shape_edges)
            self.remove(new_shape)
            self.wait()

            self.play(
                Write(new_a),
                Write(new_b),
                Write(new_c),
                Write(new_d)
            )
            self.wait()

            self.play(
                Wiggle(new_shape_edges[5], rotation_angle=0.02 * TAU),
                Wiggle(new_shape_edges[2], rotation_angle=0.02 * TAU),
                rate_func=linear, run_time=1.75
            )

        # write a-c
            self.play(
                Write(brace_a), Write(new_a_minus_c[0]),
                Write(brace_c), new_c.animate.next_to(brace_c, LEFT)
            )
            self.wait(0.5)
            self.play(
                ReplacementTransform(brace_a, brace_a_minus_c),
                new_a_minus_c[0].animate.shift(DOWN * 0.5),
                ReplacementTransform(Dot(radius=0).move_to(new_a_minus_c), new_a_minus_c[1:].shift(DOWN * 0.5)),
                new_c.animate.next_to(new_shape_edges[4], RIGHT),
                FadeOut(brace_c)
            )
            self.wait(0.5)
            self.play(
                FadeOut(brace_a_minus_c), 
                new_a_minus_c.animate.next_to(new_shape_edges[2], RIGHT)
            )
            self.wait(0.5)

        # write b-d
            self.play(
                Write(brace_b), Write(new_b_minus_d[0]),
                Write(brace_d), new_d.animate.next_to(brace_d, DOWN, buff=0.1)
            )
            self.wait(0.5)
            self.play(
                ReplacementTransform(brace_b, brace_b_minus_d),
                new_b_minus_d[0].animate.shift(LEFT * 1.15),
                ReplacementTransform(Dot(radius=0).move_to(new_b_minus_d), new_b_minus_d[1:].shift(LEFT * 1.15)),
                new_d.animate.next_to(new_shape_edges[3], UP, buff=0.1),
                FadeOut(brace_d)
            )
            self.wait(0.5)
            self.play(
                FadeOut(brace_b_minus_d), 
                new_b_minus_d.animate.next_to(new_shape_edges[5], UP)
            )
            self.wait(0.5)

        # write paragic
            self.play(
                Write(new_shape_paragic[0][:-1]),
                AnimationGroup(
                    *[Indicate(new_shape_edges[(6 - i) % 6], 1.2, ORANGE) for i in range(6)],
                    lag_ratio=1.1
                ),
                run_time=7, rate_func=linear
            )
            self.wait()

            self.play(
                FadeOut(
                    new_shape_paragic[0][2], new_shape_paragic[0][6], 
                    new_shape_paragic[0][12], new_shape_paragic[0][16]
                ),
                new_shape_paragic[0][0:2].animate.shift(0.36 * RIGHT),
                new_shape_paragic[0][3:6].animate.shift(0.18 * RIGHT),
                new_shape_paragic[0][13:16].animate.shift(0.18 * LEFT),
                new_shape_paragic[0][17:-1].animate.shift(0.36 * LEFT)
            )

            self.play(Create(surr_rect_d_1))
            self.play(Create(surr_rect_d_2))
            self.play(FadeOut(surr_rect_d_1, surr_rect_d_2))
            self.play(Create(krchatman_gcikner_1))
            self.wait()

            self.play(Create(surr_rect_c_1), Create(surr_rect_c_2))
            self.wait(0.5)
            self.play(FadeOut(surr_rect_c_1, surr_rect_c_2))
            self.play(Create(krchatman_gcikner_2[0]), Create(krchatman_gcikner_2[1]))
            self.wait()

            self.play(
                Write(new_shape_paragic[0][-1]),
                Write(new_shape_paragic[1])
            )
            self.wait()

            self.play(FadeIn(
                SurroundingRectangle(new_shape_paragic[1]),
                SurroundingRectangle(paragic_a_b[1]),
                rate_func=there_and_back_with_pause, run_time=2
            ))
            self.wait()

            self.play(
                ReplacementTransform(new_shape_edges[3].copy(), new_shape_extra_segments[0]),
                new_d.animate.shift((3 * 0.7 - 1) * UP),
                new_shape_edges[3].animate.set_opacity(0.3)
            )
            self.wait()

            self.play(
                ReplacementTransform(new_shape_edges[4].copy(), new_shape_extra_segments[1]),
                new_c.animate.shift(2 * RIGHT),
                new_shape_edges[4].animate.set_opacity(0.3)
            )
            self.wait()

            self.play(
                new_shape_extra_segments[0].animate.move_to(new_shape_edges[3]),
                new_d.animate.shift((3 * 0.7 - 1) * DOWN)
            )

            self.play(
                new_shape_extra_segments[1].animate.move_to(new_shape_edges[4]),
                new_c.animate.shift(2 * LEFT),
            )
            new_shape_edges[3].set_opacity(1)
            new_shape_edges[4].set_opacity(1)
            self.remove(new_shape_extra_segments)
            self.play(FadeOut(new_b_minus_d, new_a_minus_c))
            self.wait()
            
        def animate_new_shape_makeres():
            self.play(new_shape.animate.set_fill(ORANGE, 0.75))
            self.wait(0.5)
            self.play(new_shape.animate.set_fill(ORANGE, 0))
            self.wait(0.5)

            self.play(FadeIn(new_shape_full_rectangle))
            self.add(new_c, new_d)
            self.wait(0.5)
            self.play(FadeIn(new_shape_extra_rectangle))
            self.add(new_c, new_d)
            self.wait()

            self.play(Write(new_shape_makeres[0]))
            self.play(Write(new_shape_makeres[1]))
            self.play(Write(new_shape_makeres[2]))
            self.wait()

            self.play(Create(SurroundingRectangle(new_shape_makeres)))
            self.wait(0.5)
            self.play(FadeOut(self.mobjects[-2]))
            self.wait(0.5)



        animate_rect_3_7()  # animations 0-17
        animate_rect_a_b()  # animations 18-33
        animate_new_shape_paragic()  # animations 34-76
        animate_new_shape_makeres()  # animations 77-92

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


##########################################
####### LAST SHAPE DO IT YOURSELF #######

        last_shape = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [2, 1, 0],
            [1.5, 1, 0],
            [1.5, 0.25, 0],
            [0, 0.25, 0],
            [0, 1, 0],
            [-2, 1, 0],
            color=WHITE
        ).scale(2)

        last_shape_letters = VGroup(
            Tex('a', font_size=60).next_to(last_shape, LEFT),
            Tex('b', font_size=60).next_to(last_shape, DOWN),
            Tex('c', font_size=60).move_to((last_shape.get_vertices()[5] + last_shape.get_vertices()[6]) / 2).shift(0.3 * RIGHT),
            Tex('d', font_size=60).move_to((last_shape.get_vertices()[4] + last_shape.get_vertices()[5]) / 2).shift(0.35 * UP)
        )

        self.play(FadeIn(last_shape, last_shape_letters))
        self.wait()

