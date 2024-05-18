from manim import MovingCameraScene
from manim import AnimationGroup
from manim import Graph, Circle, Dot, Line, RoundedRectangle, Arrow, SurroundingRectangle, Cross, Polygon
from manim import Write, Create, FadeIn, FadeOut, ReplacementTransform, Uncreate
from manim import Wiggle, Indicate, ShowPassingFlash, Circumscribe, Flash
from manim import VGroup
from manim import MathTex
from manim import UP, RIGHT, DOWN, LEFT, UR, UL, ORIGIN
from manim import GREEN, ORANGE, RED, YELLOW, BLUE, PURPLE, WHITE, GREY
from manim import PI
from manim import linear, rush_into

from .text import problem, text_1, rule_1, text_2, rule_2, question

import numpy as np

class Problem20000(MovingCameraScene):
    def construct(self):

        self.wait()

        self.play(
            AnimationGroup(
                Write(problem[0]),
                Write(problem[1]),
                Write(problem[2]),
                Write(problem[3]),
                lag_ratio=1.5
            )
        )
        self.play(problem.animate.shift(3*UP))
        self.wait()

        V_1 = [1, 2, 3, 4, 5, 6]
        E_1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
        example_1 = Graph(V_1, E_1, layout="circular", layout_scale=1.5).shift(4.4*LEFT)
        example_1[1].scale(1.5).set_color(GREEN)
        example_1[2].scale(1.5).set_color(YELLOW)
        example_1[3].scale(1.5).set_color(PURPLE)
        example_1[4].scale(1.5).set_color(YELLOW)
        example_1[5].scale(1.5).set_color(ORANGE)
        example_1[6].scale(1.5).set_color(PURPLE)
        triangle_1_123 = Polygon(example_1[1].get_center(), example_1[2].get_center(), example_1[3].get_center()).set_opacity(0)
        triangle_1_345 = Polygon(example_1[3].get_center(), example_1[4].get_center(), example_1[5].get_center()).set_opacity(0)
        triangle_1_561 = Polygon(example_1[1].get_center(), example_1[6].get_center(), example_1[5].get_center()).set_opacity(0)
        triangle_1_135 = Polygon(example_1[3].get_center(), example_1[1].get_center(), example_1[5].get_center()).set_opacity(0)
        triangles_1 = VGroup(triangle_1_123, triangle_1_345, triangle_1_561, triangle_1_135)

        V_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        E_2 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 1)]
        example_2 = Graph(V_2, E_2, layout="circular", layout_scale=1.5)
        example_2[1].scale(1.5).set_color(RED)
        example_2[2].scale(1.5).set_color(YELLOW)
        example_2[3].scale(1.5).set_color(GREEN)
        example_2[4].scale(1.5).set_color(YELLOW)
        example_2[5].scale(1.5).set_color(ORANGE)
        example_2[6].scale(1.5).set_color(PURPLE)
        example_2[7].scale(1.5).set_color(GREEN)
        example_2[8].scale(1.5).set_color(ORANGE)
        example_2[9].scale(1.5).set_color(YELLOW)
        triangle_2_123 = Polygon(example_2[1].get_center(), example_2[2].get_center(), example_2[3].get_center()).set_opacity(0)
        triangle_2_139 = Polygon(example_2[1].get_center(), example_2[3].get_center(), example_2[9].get_center()).set_opacity(0)
        triangle_2_987 = Polygon(example_2[9].get_center(), example_2[8].get_center(), example_2[7].get_center()).set_opacity(0)
        triangle_2_765 = Polygon(example_2[7].get_center(), example_2[6].get_center(), example_2[5].get_center()).set_opacity(0)
        triangle_2_579 = Polygon(example_2[5].get_center(), example_2[7].get_center(), example_2[9].get_center()).set_opacity(0)
        triangle_2_543 = Polygon(example_2[5].get_center(), example_2[4].get_center(), example_2[3].get_center()).set_opacity(0)
        triangle_2_593 = Polygon(example_2[5].get_center(), example_2[3].get_center(), example_2[9].get_center()).set_opacity(0)
        triangles_2 = VGroup(triangle_2_123, triangle_2_139, triangle_2_987, triangle_2_765, triangle_2_579, triangle_2_543, triangle_2_593)

        V_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        E_3 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 1)]
        example_3 = Graph(V_3, E_3, layout="circular", layout_scale=1.5).shift(4.4*RIGHT)
        example_3[1].scale(1.5).set_color(YELLOW)
        example_3[2].scale(1.5).set_color(PURPLE)
        example_3[3].scale(1.5).set_color(GREEN)
        example_3[4].scale(1.5).set_color(ORANGE)
        example_3[5].scale(1.5).set_color(YELLOW)
        example_3[6].scale(1.5).set_color(ORANGE)
        example_3[7].scale(1.5).set_color(GREEN)
        example_3[8].scale(1.5).set_color(RED)
        example_3[9].scale(1.5).set_color(YELLOW)
        example_3[10].scale(1.5).set_color(GREEN)
        example_3[11].scale(1.5).set_color(PURPLE)
        example_3[12].scale(1.5).set_color(RED)
        triangle_3_987 = Polygon(example_3[9].get_center(), example_3[8].get_center(), example_3[7].get_center()).set_opacity(0)
        triangle_3_765 = Polygon(example_3[7].get_center(), example_3[6].get_center(), example_3[5].get_center()).set_opacity(0)
        triangle_3_754 = Polygon(example_3[7].get_center(), example_3[5].get_center(), example_3[4].get_center()).set_opacity(0)
        triangle_3_479 = Polygon(example_3[4].get_center(), example_3[7].get_center(), example_3[9].get_center()).set_opacity(0)
        triangle_3_4910 = Polygon(example_3[4].get_center(), example_3[9].get_center(), example_3[10].get_center()).set_opacity(0)
        triangle_3_41011 = Polygon(example_3[4].get_center(), example_3[10].get_center(), example_3[11].get_center()).set_opacity(0)
        triangle_3_41112 = Polygon(example_3[4].get_center(), example_3[11].get_center(), example_3[12].get_center()).set_opacity(0)
        triangle_3_4121 = Polygon(example_3[4].get_center(), example_3[12].get_center(), example_3[1].get_center()).set_opacity(0)
        triangle_3_412 = Polygon(example_3[4].get_center(), example_3[1].get_center(), example_3[2].get_center()).set_opacity(0)
        triangle_3_423 = Polygon(example_3[4].get_center(), example_3[2].get_center(), example_3[3].get_center()).set_opacity(0)
        triangles_3 = VGroup(triangle_3_987, triangle_3_765, triangle_3_754, triangle_3_479, triangle_3_4910,
                             triangle_3_41011, triangle_3_41112, triangle_3_4121, triangle_3_412, triangle_3_423)





        self.play(
            AnimationGroup(
                FadeIn(example_1),
                FadeIn(example_2),
                FadeIn(example_3),
                lag_ratio=1.25
            ),
            run_time=0.75
        )
        self.wait()
        
        self.play(
            AnimationGroup(
                example_1.animate.add_edges((1, 3)),
                triangle_1_123.animate.set_fill(GREY, opacity=0.5),
                example_1.animate.add_edges((3, 5)),
                triangle_1_345.animate.set_fill(GREY, opacity=0.5),
                example_1.animate.add_edges((5, 1)),
                triangle_1_561.animate.set_fill(GREY, opacity=0.5),
                triangle_1_135.animate.set_fill(GREY, opacity=0.5),
                lag_ratio=1.1
            ),
            run_time=3
        )
        self.wait()

        self.play(
            AnimationGroup(
                example_2.animate.add_edges((1, 3)),
                triangle_2_123.animate.set_fill(GREY, opacity=0.5),
                example_2.animate.add_edges((3, 9)),
                triangle_2_139.animate.set_fill(GREY, opacity=0.5),
                example_2.animate.add_edges((9, 7)),
                triangle_2_987.animate.set_fill(GREY, opacity=0.5),
                example_2.animate.add_edges((7, 5)),
                triangle_2_765.animate.set_fill(GREY, opacity=0.5),
                example_2.animate.add_edges((5, 9)),
                triangle_2_579.animate.set_fill(GREY, opacity=0.5),
                example_2.animate.add_edges((5, 3)),
                triangle_2_543.animate.set_fill(GREY, opacity=0.5),
                triangle_2_593.animate.set_fill(GREY, opacity=0.5),
                lag_ratio=1.25
            ),
            run_time=4
        )
        self.wait()

        self.play(
            AnimationGroup(
                example_3.animate.add_edges((9, 7)),
                triangle_3_987.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((7, 5)),
                triangle_3_765.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((7, 4)),
                triangle_3_754.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 9)),
                triangle_3_479.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 10)),
                triangle_3_4910.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 11)),
                triangle_3_41011.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 12)),
                triangle_3_41112.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 1)),
                triangle_3_4121.animate.set_fill(GREY, opacity=0.5),
                example_3.animate.add_edges((4, 2)),
                triangle_3_412.animate.set_fill(GREY, opacity=0.5),
                triangle_3_423.animate.set_fill(GREY, opacity=0.5),
                lag_ratio=1.25
            ),
            run_time=5, rate_func=rush_into
        )
        self.wait()


        self.remove(problem, example_1, example_2, example_3, triangles_1, triangles_2, triangles_3)
        triangles_1.set_fill(GREY, opacity=0)
        triangles_2.set_fill(GREY, opacity=0)
        triangles_3.set_fill(GREY, opacity=0)

        vertices_1 = [1, 2, 3, 4, 5, 6, 7, 8]
        edges_1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 1)]
        graph_1 = Graph(vertices_1, edges_1, layout="circular", layout_scale=2.5).shift(3*LEFT)
        for i in range(len(vertices_1)):
            graph_1[i+1].scale(1.5)
        graph_1[1].set_color(ORANGE)
        graph_1[2].set_color(GREEN)
        graph_1[3].set_color(ORANGE)
        graph_1[4].set_color(YELLOW)
        graph_1[5].set_color(GREEN)
        graph_1[6].set_color(YELLOW)
        graph_1[7].set_color(GREEN)
        graph_1[8].set_color(YELLOW)

        self.wait(0.5)

        self.play(Create(graph_1))
        self.wait()

        self.play(Circumscribe(VGroup(graph_1[2], graph_1[3], graph_1[4]), color=BLUE, time_width=1, run_time=2))
        self.wait(0.5)

        self.play(graph_1.animate.add_edges((4, 2)))
        self.wait()

        arrow_1 = Arrow(start=LEFT, end=RIGHT).next_to(graph_1)

        self.play(Create(arrow_1))
        self.wait()

        graph_2 = graph_1.copy()
        graph_2.remove_vertices(3)

        self.play(graph_2.animate.next_to(arrow_1, RIGHT).align_to(graph_1, DOWN))
        self.wait()

        self.play(VGroup(graph_1, arrow_1, graph_2).animate.scale(0.6).align_to([-6.5, 3.5, 0], UL))
        self.wait()

        self.play(ShowPassingFlash(SurroundingRectangle(VGroup(graph_2[2], graph_2[1], graph_2[8]))), time_width=2)
        self.wait()

        self.play(graph_2.animate.add_edges((2, 8)))
        self.wait()

        arrow_2 = arrow_1.copy().next_to(graph_2).align_to(arrow_1, DOWN)

        self.play(Create(arrow_2))
        self.wait()

        graph_3 = graph_2.copy()
        graph_3.remove_vertices(1)

        self.play(graph_3.animate.next_to(arrow_2).align_to(graph_2, DOWN))
        self.wait()

        arrow_3 = arrow_1.copy().rotate(-PI/2).next_to(graph_3, DOWN)
        graph_4 = MathTex("?", font_size=40).next_to(arrow_3, DOWN)

        self.play(Create(arrow_3))
        self.wait(0.5)
        
        self.play(Write(graph_4))
        self.wait()

        self.play(self.camera.frame.animate.align_to(graph_2.get_left(), LEFT).shift(UP))
        self.wait()

        color_1 = graph_3[2].copy()
        color_2 = graph_3[8].copy()

        text_1.next_to(graph_3)
        
        self.play(Write(text_1[0]))
        self.wait(0.5)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    Circumscribe(graph_3[2], shape=Circle, time_width=2, color=GREEN),
                    Circumscribe(graph_3[5], shape=Circle, time_width=2, color=GREEN),
                    Circumscribe(graph_3[7], shape=Circle, time_width=2, color=GREEN),
                ),
                AnimationGroup(
                    Circumscribe(graph_3[4], shape=Circle, time_width=2),
                    Circumscribe(graph_3[6], shape=Circle, time_width=2),
                    Circumscribe(graph_3[8], shape=Circle, time_width=2),
                ),
                lag_ratio=1
            )
        )
        self.wait()

        self.play(
            color_1.animate.move_to(text_1[1]).align_to(text_1.get_top()+0.1*UP, UP),
            color_2.animate.move_to(text_1[1]).align_to(text_1.get_bottom()+0.1*DOWN, DOWN)
        )
        self.wait(0.5)

        self.play(ReplacementTransform(VGroup(color_1, color_2), text_1[1]))
        self.wait(0.25)

        self.play(Write(text_1[2]))
        self.wait()

        cross = Cross().move_to(graph_3.get_center()+0.2*UR).scale(1.2)
        cross_2 = Cross().move_to(graph_3[2]).scale(1/12)
        cross_4 = Cross().move_to(graph_3[4]).scale(1/12)
        cross_5 = Cross().move_to(graph_3[5]).scale(1/12)
        cross_8 = Cross().move_to(graph_3[8]).scale(1/12)
        self.play(graph_3.animate.add_edges((4, 8)))
        self.wait(0.25)
        self.play(
            Create(cross_4),
            Create(cross_8)
        )
        self.wait()

        self.play(
            AnimationGroup(
                graph_3.animate.remove_edges((4, 8)),
                AnimationGroup(
                    Uncreate(cross_4),
                    Uncreate(cross_8)
                ),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(graph_3.animate.add_edges((5, 2)))
        self.wait(0.25)
        self.play(
            Create(cross_2),
            Create(cross_5)
        )
        self.wait()

        self.play(
            AnimationGroup(
                graph_3.animate.remove_edges((5, 2)),
                AnimationGroup(
                    Uncreate(cross_2),
                    Uncreate(cross_5)
                ),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(Create(cross))
        self.wait()

        self.play(
            AnimationGroup(
                self.camera.frame.animate.align_to(graph_1.get_left()+0.25*LEFT, LEFT).shift(UP),
                AnimationGroup(
                    FadeOut(text_1, arrow_2, graph_3, arrow_3, graph_4, cross)
                ),
                lag_ratio=0.5,
                rate_func=linear
            )
        )
        self.wait()

        rule_1.move_to([3.5, 5.25, 0])
        self.play(
            AnimationGroup(
                Write(rule_1[1:]),
                Write(rule_1[0]),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(
            graph_2.animate.remove_edges((2, 8)),
            graph_1.animate.set_opacity(0.5),
            arrow_1.animate.set_opacity(0.5)
        )
        self.wait()

        self.play(Flash(graph_2[1], color=ORANGE))
        self.wait(0.5)

        arrow_orange = Arrow(start=[2, 1.9, 0], end=[1, 1.9, 0])
        text_2.next_to(arrow_orange, buff=0.2)

        self.play(
            AnimationGroup(
                Write(text_2),
                Create(arrow_orange),
                lag_ratio=0.5
            )
        )
        self.wait()

        triangle_4_124 = Polygon(graph_2[1].get_center(), graph_2[2].get_center(), graph_2[4].get_center()).set_opacity(0)
        triangle_4_145 = Polygon(graph_2[1].get_center(), graph_2[4].get_center(), graph_2[5].get_center()).set_opacity(0)
        triangle_4_156 = Polygon(graph_2[1].get_center(), graph_2[5].get_center(), graph_2[6].get_center()).set_opacity(0)
        triangle_4_167 = Polygon(graph_2[1].get_center(), graph_2[6].get_center(), graph_2[7].get_center()).set_opacity(0)
        triangle_4_178 = Polygon(graph_2[1].get_center(), graph_2[7].get_center(), graph_2[8].get_center()).set_opacity(0)
        triangles_4 = VGroup(triangle_4_124, triangle_4_145, triangle_4_156, triangle_4_167, triangle_4_178)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    AnimationGroup(
                        Flash(graph_2[2], color=GREEN),
                        Flash(graph_2[4], color=YELLOW)
                    ),
                    graph_2.animate.add_edges((1, 4)),
                    lag_ratio=0.5
                ),
                triangle_4_124.animate.set_fill(GREY, opacity=0.5),
                lag_ratio=1
            ),
            run_time=1.5
        )

        for i in range(5, 9):
            if i % 2 == 1:
                self.play(
                    AnimationGroup(
                        AnimationGroup(
                            AnimationGroup(
                                AnimationGroup(
                                    Flash(graph_2[i], color=GREEN),
                                    Flash(graph_2[i-1], color=YELLOW)
                                ),
                                graph_2.animate.add_edges((1, i)),
                                lag_ratio=0.5
                            ),
                            triangles_4[i-4].animate.set_fill(GREY, opacity=0.5),
                            lag_ratio=1
                        )
                    ),
                    run_time=1.5
                )
            else:
                self.play(
                    AnimationGroup(
                        AnimationGroup(
                            AnimationGroup(
                                Flash(graph_2[i], color=YELLOW),
                                Flash(graph_2[i-1], color=GREEN)
                            ),
                            graph_2.animate.add_edges((1, i)),
                            lag_ratio=0.5
                        ),
                        triangles_4[i-4].animate.set_fill(GREY, opacity=0.5),
                        lag_ratio=1
                    ),
                    run_time=1.5
                )
        self.wait()

        rule_2[2].align_to(rule_2[1], LEFT)
        rule_2[1:].next_to(rule_1[-1], DOWN*1.5).align_to(rule_1[-1], LEFT)
        rule_2[0].next_to(rule_2[1:], LEFT, buff=0.2)

        self.play(
            AnimationGroup(
                Write(rule_2[1:]),
                Write(rule_2[0]),
                lag_ratio=0.5
            )
        )
        self.wait()
        

        self.play(graph_1.animate.set_opacity(1))
        self.wait()

        surrec = SurroundingRectangle(VGroup(graph_1[2], graph_1[3], graph_1[4]), corner_radius=0.2, color=BLUE)
        question.next_to(surrec, UP)

        self.play(
            AnimationGroup(
                Create(surrec),
                Write(question),
                lag_ratio=0.75
            )
        )
        self.wait()


        self.play(
            arrow_1.animate.set_opacity(0),
            FadeOut(graph_1, graph_2, arrow_orange, text_2, surrec, question),
            VGroup(rule_1, rule_2).animate.scale(0.75).shift(RIGHT+0.2*UP),
            triangles_4.animate.set_fill(GREY, opacity=0)
        )
        self.wait()



        vertices_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        edges_5 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)]
        graph_5 = Graph(vertices_5, edges_5, layout="circular", layout_scale=2).shift(3*LEFT+2*UP)
        for i in range(len(vertices_5)):
            graph_5[i+1].scale(1.5)

        green_dot = Dot(color=GREEN).scale(1.5)
        yellow_dot = Dot(color=YELLOW).scale(1.5)
        orange_dot = Dot(color=ORANGE).scale(1.5)
        colors_dot = VGroup(green_dot, yellow_dot, orange_dot).arrange(3*RIGHT).next_to(graph_5, 3*UP)


        self.play(Create(graph_5))
        self.wait()

        self.play(
            AnimationGroup(
                Create(green_dot),
                Create(yellow_dot),
                Create(orange_dot),
                lag_ratio=1
            )
        )
        self.wait()

        green_dot_copy = green_dot.copy()
        yellow_dot_copy = yellow_dot.copy()
        orange_dot_copy = orange_dot.copy()

        self.play(
            AnimationGroup(
                green_dot_copy.animate.move_to(graph_5[4]),
                yellow_dot_copy.animate.move_to(graph_5[5]),
                orange_dot_copy.animate.move_to(graph_5[9]),
                lag_ratio=1
            )
        )
        self.wait()
        graph_5[4].set_color(GREEN)
        graph_5[5].set_color(YELLOW)
        graph_5[9].set_color(ORANGE)
        green_dot_copy_1 = graph_5[6].copy().set_color(GREEN)

        self.play(
            AnimationGroup(
                green_dot_copy.animate.move_to(graph_5[6]),
                yellow_dot_copy.animate.move_to(graph_5[7]),
                lag_ratio=1
            )
        )
        self.play(green_dot_copy_1.animate.move_to(graph_5[8]))
        self.wait()

        graph_5[6].set_color(GREEN)
        graph_5[7].set_color(YELLOW)
        graph_5[8].set_color(GREEN)

        self.play(
            Flash(graph_5[7], color=YELLOW),
            Flash(graph_5[8], color=GREEN),
            Flash(graph_5[9], color=ORANGE)
        )
        self.wait()

        self.play(
            FadeOut(graph_5, colors_dot, green_dot_copy, green_dot_copy_1, orange_dot_copy, yellow_dot_copy)
        )
        self.wait()

        vertices_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        edges_6 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)]
        graph_6 = Graph(vertices_6, edges_6, layout="circular").shift(4.4*LEFT+0.5*UP)
        for i in range(len(vertices_6)):
            graph_6[i+1].scale(1.5)


        self.play(Create(graph_6))
        self.wait()

        self.play(
            AnimationGroup(
                Circumscribe(VGroup(graph_6[3], graph_6[4], graph_6[5]), color=BLUE, time_width=1),
                AnimationGroup(
                    graph_6[3].animate.set_color(YELLOW),
                    graph_6[4].animate.set_color(ORANGE),
                    graph_6[5].animate.set_color(GREEN)
                ),
                lag_ratio=0.75
            )
        )
        self.wait()

        

        # self.play(graph_6.animate.add_edges((5, 3)))
        # self.wait()

        self.play(
            graph_6[6].animate.scale(1.5).set_color(RED),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[6].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[7].animate.scale(1.5).set_color(GREEN),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[7].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[8].animate.scale(1.5).set_color(PURPLE),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[8].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[9].animate.scale(1.5).set_color(YELLOW),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[9].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[10].animate.scale(1.5).set_color(GREEN),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[10].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[1].animate.scale(1.5).set_color(RED),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[1].animate.scale(1/1.5), run_time=0.5)

        self.play(
            graph_6[2].animate.scale(1.5).set_color(PURPLE),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[2].animate.scale(1/1.5), run_time=0.5)
        self.wait()

        for i in range(len(vertices_6)-3):
            if i < 5:
                self.play(graph_6.animate.add_edges((4, i+6)))
            else:
                self.play(graph_6.animate.add_edges((4, i-4)))
        self.wait()

        arrow_7 = Arrow(start=ORIGIN, end=ORIGIN+1.25*UP).next_to(graph_6, UP, buff=0.15)
        self.play(Create(arrow_7))
        self.wait(0.5)

        graph_7 = graph_6.copy()
        self.play(graph_7.animate.scale(0.5).next_to(arrow_7, UP, buff=0.15))
        self.wait()

        checkmark_copy_1 = rule_2[0].copy()
        self.play(checkmark_copy_1.animate.next_to(graph_7))
        self.wait()

        for i in range(len(vertices_6)-3):
            if i < 2:
                self.play(
                    graph_6.animate.remove_edges((4, 2-i)),
                    graph_6[2-i].animate.set_color(WHITE)
                )
            else:
                self.play(
                    graph_6.animate.remove_edges((4, 12-i)),
                    graph_6[12-i].animate.set_color(WHITE)
                )
        self.wait()

        self.play(
            graph_6[8].animate.scale(1.5).set_color(ORANGE),
            rate_func=linear,
            run_time=0.5
        )
        self.play(graph_6[8].animate.scale(1/1.5), run_time=0.5)
        self.wait()

        self.play(graph_6.animate.add_edges((5, 3)))
        self.wait()

        arrow_8 = Arrow(start=ORIGIN, end=ORIGIN+1.25*RIGHT).next_to(graph_6, RIGHT, buff=0.15)
        self.play(Create(arrow_8))
        self.wait()

        graph_8 = graph_6.copy()
        graph_8.remove_vertices(4)
        self.play(graph_8.animate.next_to(arrow_8, RIGHT, buff=0.15))
        self.wait()

        arrow_9 = arrow_7.copy().next_to(graph_8, UP, buff=0.15).shift(0.2*LEFT)
        self.play(Create(arrow_9))
        self.wait(0.5)

        checkmark_copy_2 = rule_2[0].copy()
        self.play(checkmark_copy_2.animate.next_to(arrow_9, UP, buff=0.5))
        self.wait()

        arrow_10 = arrow_8.copy().next_to(graph_8, RIGHT, buff=0.15)
        self.play(Create(arrow_10))
        self.wait()

        cdots = MathTex("\\cdots").next_to(arrow_10, RIGHT, buff=0.15)
        self.play(Write(cdots))
        self.wait()