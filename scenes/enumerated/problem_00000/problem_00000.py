from manim import Scene, FadeIn, FadeOut, VGroup, GrowFromEdge, AnimationGroup, TransformFromCopy, rate_functions, Tex, Arrow, Axes, Write, Circumscribe, SurroundingRectangle, Create, MathTex, TransformFromCopy, AnimationGroup, Dot, ReplacementTransform, ValueTracker, BraceBetweenPoints, GrowFromCenter, Difference, Union, BraceBetweenPoints, Transform, Indicate, Wiggle, GrowArrow, CurvedArrow
from manim import ORIGIN, UP, DOWN, LEFT, RIGHT, UL, DL, DR, UR
from manim import BLUE, RED, GREEN, BLACK, WHITE, ORANGE
from manim import PI
import numpy as np
from qarakusiscene import TaskNumberBox
from aramanim import get_segment_part
from objects import SimpleSVGMobject

SCALE = .14
NUM_FONT_SIZE = 85

class Problem00000(Scene):
    def construct(self):
        self.wait()
        task_number = TaskNumberBox("Խ. 00000")

        self.play(FadeIn(task_number))
        self.wait()

        # fade in tigran and gagik
        tigran_svg = SimpleSVGMobject("boy_1", color=BLUE)
        tigran_tex = Tex("Տիգրան", color=BLUE)
        gagik_svg = SimpleSVGMobject("boy_2", color=RED)
        gagik_tex = Tex("Գագիկ", color=RED)
        tigran = VGroup(tigran_svg, tigran_tex).arrange(DOWN)
        gagik = VGroup(gagik_svg, gagik_tex).arrange(DOWN)
        runers = VGroup(gagik, tigran)

        runers.arrange().move_to(ORIGIN)

        self.play(FadeIn(runers))
        self.wait()

        # fade in road
        road = get_segment_part(94.5*SCALE)
        finish_flag = SimpleSVGMobject('flag_finish_1')
        road.move_to(ORIGIN).to_edge(DOWN)
        finish_flag.set_x(road.right_edge.get_x()).align_to(road.line, DOWN).shift(DL*.05)

        self.play(GrowFromEdge(road, LEFT))
        self.play(FadeIn(finish_flag))
        self.wait()

        # fade in location signs
        location_tigran = SimpleSVGMobject('location_sign', color=BLUE, scale=.4)
        location_gagik = SimpleSVGMobject('location_sign', color=RED, scale=.4)

        location_tigran.set_x(road.left_edge.get_x()).align_to(road.line, DOWN)
        location_gagik.set_x(road.left_edge.get_x()).align_to(road.line, DOWN)

        self.play(
            AnimationGroup(
                TransformFromCopy(tigran_svg, location_tigran),
                TransformFromCopy(gagik_svg, location_gagik)
            )
        )
        self.wait()

        self.play(
            tigran.animate.to_edge(RIGHT).shift(UP),
            gagik.animate.to_edge(LEFT).shift(UP)
        )
        self.wait()

        # fade in coordinate system
        coord_sys = Axes(
            x_range=[0, 13, 1],
            y_range=[0, 10, 1]
        ).add_coordinates()
        coord_sys.scale_to_fit_width(0.85*(self.camera.frame_width-tigran.width-gagik.width))
        coord_sys.next_to(gagik).shift(DOWN*.6)
        coord_sys_y_label = coord_sys.get_y_axis_label("V\\text{(մ/վ)}")
        coord_sys_x_label = coord_sys.get_x_axis_label("t\\text{(վ)}")

        self.play(FadeIn(coord_sys))
        self.play(
            Write(coord_sys_y_label),
            Write(coord_sys_x_label)
        )

        # write info about Tigran
        tigran_info = VGroup(
            Tex("արագացում՝ ", "$2$", " մ/վ$^2$", color=BLUE),
            Tex("վերջն․ արագություն՝ ", "$8$", " մ/վ", color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)
        tigran_info.scale(1.07).to_corner(UR).shift(LEFT*1.5)
        
        self.play(Write(tigran_info))
        self.wait()

        # draw Tigran's graph points
        self.play(Circumscribe(tigran_info[1][-2:], fade_out=True), run_time=1.5)
        self.wait()
        curved_arrow1 = CurvedArrow(
            tigran_info[1][-2:].get_bottom() + np.array([-.5, 0, 0]),
            coord_sys.coordinate_labels[1][7].get_bottom() + np.array([.1, -.1, 0]),
            angle=-PI/3
        )
        self.play(Create(curved_arrow1))
        self.wait()
        srr_circle_t1 = SurroundingRectangle(coord_sys.coordinate_labels[1][7], color=BLUE, corner_radius=0.15)
        self.play(Create(srr_circle_t1))
        self.play(FadeOut(curved_arrow1))
        self.wait()

        first_second = VGroup(
            coord_sys.get_lines_to_point(coord_sys.c2p(1, 2), color=BLUE),
            Dot(coord_sys.coords_to_point(1, 2), color=BLUE)
        )
        first_second.add(
            MathTex("I \\text{ վ}").scale(.7).next_to(first_second[1], UR, 0.01)
        )
        self.play(Circumscribe(tigran_info[0][-2:], fade_out=True), run_time=1.5)
        self.wait()
        self.play(Create(first_second))
        self.wait()

        second_second = VGroup(
            coord_sys.get_lines_to_point(coord_sys.c2p(2, 4), color=BLUE),
            Dot(coord_sys.coords_to_point(2, 4), color=BLUE)
        )
        second_second.add(
            MathTex("II \\text{ վ}").scale(.7).next_to(second_second[1], UR, 0.001)
        )
        self.play(Create(second_second))
        self.wait()

        third_second = VGroup(
            coord_sys.get_lines_to_point(coord_sys.c2p(3, 6), color=BLUE),
            Dot(coord_sys.coords_to_point(3, 6), color=BLUE)
        )
        third_second.add(
            MathTex("III \\text{ վ}").scale(.7).next_to(third_second[1], UR, 0.01)
        )
        self.play(Create(third_second))
        self.wait()

        fourth_second = VGroup(
            coord_sys.get_lines_to_point(coord_sys.c2p(4, 8), color=BLUE),
            Dot(coord_sys.coords_to_point(4, 8), color=BLUE)
        )
        fourth_second.add(
            MathTex("IV \\text{ վ}").scale(.7).next_to(fourth_second[1], UR, 0.01)
        )
        self.play(Create(fourth_second))
        self.wait()

        tigran_acceleration_time = MathTex("8", ":", "2", "=", "4 \\text{ վ}", font_size=80, color=BLUE)
        tigran_acceleration_time.move_to(tigran_info, aligned_edge=UP)
        
        self.play(
            AnimationGroup(
                TransformFromCopy(tigran_info[1][1], tigran_acceleration_time[0]),
                Write(tigran_acceleration_time[1]),
                TransformFromCopy(tigran_info[0][1], tigran_acceleration_time[2]),
                Write(tigran_acceleration_time[3:]),
                lag_ratio=.3
            ), 
            FadeOut(tigran_info)
        )
        self.wait()

        self.play(Circumscribe(tigran_acceleration_time[-1], fade_out=True), run_time=1.5)
        self.wait()
        srr_circle_t2 = SurroundingRectangle(coord_sys.coordinate_labels[0][3], color=BLUE, corner_radius=0.15)
        arrow1 = Arrow(tigran_acceleration_time[-1], coord_sys.coordinate_labels[0][3])
        self.play(GrowArrow(arrow1))
        self.wait()
        self.play(Create(srr_circle_t2))
        self.play(FadeOut(arrow1))
        self.wait()

        tigran_acceleration_coord_lines = coord_sys.get_lines_to_point(coord_sys.c2p(4, 8), color=BLUE)
        tigran_acceleration_coord_point = Dot(coord_sys.coords_to_point(4, 8), color=BLUE)
        self.add(
            tigran_acceleration_coord_lines,
            tigran_acceleration_coord_point
        )
        self.play(
            FadeOut(
                tigran_acceleration_time,
                first_second[-1],
                second_second[-1],
                third_second[-1],
                fourth_second,
                srr_circle_t1,
                srr_circle_t2
            )
        )
        self.wait()

        # write info about Gagik
        gagik_info = VGroup(
            Tex("արագացում՝ ", "$3$", " մ/վ$^2$", color=RED),
            Tex("վերջն․ արագություն՝ ", "$9$", " մ/վ", color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        gagik_info.scale(1.2).to_corner(UR).shift(LEFT*1.5)

        self.play(Write(gagik_info))
        self.wait()

        # draw Gagik's graph points
        self.play(Circumscribe(gagik_info[1][-2:], fade_out=True), run_time=1.5)
        self.wait()
        curved_arrow2 = CurvedArrow(
            gagik_info[1][-2:].get_bottom() + np.array([-.5, 0, 0]),
            coord_sys.coordinate_labels[1][8].get_center() + np.array([.1, -.1, 0]),
            angle=-PI/3
        )
        self.play(Create(curved_arrow2))
        self.wait()
        srr_circle_g1 = SurroundingRectangle(coord_sys.coordinate_labels[1][8], color=RED, corner_radius=0.15)
        self.play(Create(srr_circle_g1))
        self.play(FadeOut(curved_arrow2))
        self.wait()
        
        # first_second = VGroup(
        #     coord_sys.get_lines_to_point(coord_sys.c2p(1, 3), color=RED),
        #     Dot(coord_sys.coords_to_point(1, 3), color=RED)
        # )
        # first_second.add(
        #     MathTex("I \\text{ վ}").scale(.7).next_to(first_second[1], UR, 0.01)
        # )
        # self.play(Circumscribe(gagik_info[0][-2:], fade_out=True), run_time=1.5)
        # self.wait()
        # self.play(Create(first_second))
        # self.wait()

        # second_second = VGroup(
        #     coord_sys.get_lines_to_point(coord_sys.c2p(2, 6), color=RED),
        #     Dot(coord_sys.coords_to_point(2, 6), color=RED)
        # )
        # second_second.add(
        #     MathTex("II \\text{ վ}").scale(.7).next_to(second_second[1], UR, 0.001)
        # )
        # self.play(Create(second_second))
        # self.wait()

        # third_second = VGroup(
        #     coord_sys.get_lines_to_point(coord_sys.c2p(3, 9), color=RED),
        #     Dot(coord_sys.coords_to_point(3, 9), color=RED)
        # )
        # third_second.add(
        #     MathTex("III \\text{ վ}").scale(.7).next_to(third_second[1], UR, 0.01)
        # )
        # self.play(Create(third_second))
        # self.wait()

        gagik_acceleration_time = MathTex("9", ":", "3", "=", "3 \\text{ վ}", font_size=80, color=RED)
        gagik_acceleration_time.move_to(gagik_info, aligned_edge=UP)
        
        self.play(
            AnimationGroup(
                TransformFromCopy(gagik_info[1][1], gagik_acceleration_time[0]),
                Write(gagik_acceleration_time[1]),
                TransformFromCopy(gagik_info[0][1], gagik_acceleration_time[2]),
                Write(gagik_acceleration_time[3:]),
                lag_ratio=.3
            ), 
            FadeOut(gagik_info)
        )
        self.wait()

        self.play(Circumscribe(gagik_acceleration_time[-1], fade_out=True), run_time=1.5)
        self.wait()
        srr_circle_g2 = SurroundingRectangle(coord_sys.coordinate_labels[0][2], color=RED, corner_radius=0.15)
        arrow2 = Arrow(gagik_acceleration_time[-1], coord_sys.coordinate_labels[0][2])
        self.play(GrowArrow(arrow2))
        self.wait()
        self.play(Create(srr_circle_g2))
        self.play(FadeOut(arrow2))
        self.wait()

        gagik_acceleration_coord_lines = coord_sys.get_lines_to_point(coord_sys.c2p(3, 9), color=RED)
        gagik_acceleration_coord_lines.set_z_index(tigran_acceleration_coord_lines.z_index + 1)
        gagik_acceleration_coord_point = Dot(coord_sys.coords_to_point(3, 9), color=RED)
        self.play(
            Create(gagik_acceleration_coord_lines),
            Create(gagik_acceleration_coord_point)
        )
        self.wait()

        self.play(
            FadeOut(
                gagik_acceleration_time,
                # first_second[-1],
                # second_second[-1],
                # third_second,
                srr_circle_g1,
                srr_circle_g2
            )
        )
        self.wait()

        # Gagik's graph
        gagik_acceleration_graph = coord_sys.plot(lambda x: 3*x, x_range=[0, 3], color=RED)
        gagik_const_speed_graph = coord_sys.plot(lambda x: 9, x_range=[3, 12], color=RED)
        gagik_location_value_1 = ValueTracker(0)
        gagik_location_value_2 = ValueTracker(13.5/94.5)
        
        def gagik_location_mover(location):
            if gagik_location_value_2.get_value() == 13.5/94.5:
                location.set_x(road.left_edge.get_x()+road.line.get_length()*gagik_location_value_1.get_value())
            else:
                location.set_x(road.left_edge.get_x()+road.line.get_length()*gagik_location_value_2.get_value())

        location_gagik.add_updater(gagik_location_mover)

        # Tigran's graph
        tigran_acceleration_graph = coord_sys.plot(lambda x: 2*x, x_range=[0, 4], color=BLUE)
        tigran_const_speed_graph = coord_sys.plot(lambda x: 8, x_range=[4, 12], color=BLUE)
        tigran_location_value_1 = ValueTracker(0)
        tigran_location_value_2 = ValueTracker(16/94.5)

        def tigran_location_mover(location):
            if tigran_location_value_2.get_value() == 16/94.5:
                location.set_x(road.left_edge.get_x()+road.line.get_length()*tigran_location_value_1.get_value())
            else:
                location.set_x(road.left_edge.get_x()+road.line.get_length()*tigran_location_value_2.get_value())

        location_tigran.add_updater(tigran_location_mover)
        
        # draw Gagik's and Tigran's graphs and paths
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Create(gagik_acceleration_graph, rate_func=rate_functions.ease_in_sine, run_time=3),
                    gagik_location_value_1.animate(rate_func=rate_functions.ease_in_sine, run_time=3).set_value(13.5/94.5)
                ),
                AnimationGroup(
                    Create(gagik_const_speed_graph, rate_func=rate_functions.linear, run_time=9),
                    gagik_location_value_2.animate(rate_func=rate_functions.linear, run_time=9).set_value(94.5/94.5)
                ),
                lag_ratio=1
            ),
            AnimationGroup(
                AnimationGroup(
                    Create(tigran_acceleration_graph, rate_func=rate_functions.ease_in_sine, run_time=4),
                    tigran_location_value_1.animate(rate_func=rate_functions.ease_in_sine, run_time=4).set_value(16/94.5)
                ),
                AnimationGroup(
                    Create(tigran_const_speed_graph, rate_func=rate_functions.linear, run_time=8),
                    tigran_location_value_2.animate(rate_func=rate_functions.linear, run_time=8).set_value(80/94.5)
                ),
                lag_ratio=1
            )
        )
        self.play(
            FadeOut(
                first_second[:-1],
                second_second[:-1],
                third_second[:-1]
            )
        )
        gagik_finish_coord_lines = coord_sys.get_lines_to_point(coord_sys.c2p(12, 9), color=RED)
        gagik_finish_coord_point = Dot(coord_sys.coords_to_point(12, 9), color=RED)
        self.play(Create(gagik_finish_coord_lines))
        self.play(FadeIn(gagik_finish_coord_point))
        self.wait()

        # fade in qauestion
        question_brace = BraceBetweenPoints(location_tigran.get_bottom(), location_gagik.get_bottom(), direction=UP, buff=0, color=GREEN).scale(.88)
        question_brace_tex = question_brace.get_tex("?")
        self.play(GrowFromCenter(question_brace))
        self.play(Write(question_brace_tex))
        self.wait()

        # Tigran's passed road on graph
        tigran_acceleration_road_graph = coord_sys.get_area(
            tigran_acceleration_graph,
            color=BLUE,
            fill_opacity=1
        )
        tigran_const_speed_road_graph = coord_sys.get_area(
            tigran_const_speed_graph,
            color=BLUE,
            fill_opacity=1
        )
        tigran_road = VGroup(
            tigran_acceleration_road_graph,
            tigran_const_speed_road_graph
        )
        tigran_road_tex = MathTex("S_{\\text{Տիգրան}}", color=WHITE, font_size=100)
        tigran_road_tex.set_stroke(BLACK, 1.2).move_to(tigran_road.get_center())
        self.play(FadeIn(tigran_road))
        self.play(Write(tigran_road_tex))
        self.wait(2)

        self.play(FadeOut(tigran_road, tigran_road_tex))
        self.wait()

        # Gagik's passed road on graph
        gagik_acceleration_road_graph = coord_sys.get_area(
            gagik_acceleration_graph,
            color=RED,
            fill_opacity=1
        )
        gagik_const_speed_road_graph = coord_sys.get_area(
            gagik_const_speed_graph,
            color=RED,
            fill_opacity=1
        )
        gagik_road = VGroup(
            gagik_acceleration_road_graph,
            gagik_const_speed_road_graph
        )
        gagik_road_tex = MathTex("S_{\\text{Գագիկ}}", color=WHITE, font_size=110)
        gagik_road_tex.set_stroke(BLACK, 1.2).move_to(gagik_road.get_center())
        self.play(FadeIn(gagik_road))
        self.play(Write(gagik_road_tex))
        self.wait(2)

        self.play(FadeOut(gagik_road, gagik_road_tex))
        self.wait()

        # show difference between Gagik's passed road and Tigran's passed road on graph
        difference_graph = Difference(
            Union(*gagik_road),
            Union(*tigran_road),
            color=GREEN,
            fill_opacity=0.3,
            stroke_opacity=0
        )
        self.play(FadeIn(difference_graph))
        self.wait()
        self.play(FadeOut(difference_graph))
        self.wait()

        # calculate Tigran's passed road
        self.play(FadeIn(tigran_road))
        self.wait()
        self.play(
            tigran_acceleration_road_graph.animate.set_stroke(ORANGE, 4, opacity=1),
            tigran_const_speed_road_graph.animate.set_stroke(ORANGE, 4, opacity=1)
        )
        self.wait()

        tigran_rect_width_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(4, 0),
            coord_sys.coords_to_point(12, 0),
            buff=.5,
            direction=DOWN
        )
        tigran_rect_width_brace_label = tigran_rect_width_brace.get_tex("12-4").scale(1.5)
        self.play(GrowFromCenter(tigran_rect_width_brace))
        self.wait()
        self.play(Write(tigran_rect_width_brace_label))
        self.wait()
        self.play(
            Transform(
                tigran_rect_width_brace_label,
                tigran_rect_width_brace.get_tex("8").scale(1.5)
            )
        )
        self.wait()

        tigran_rect_height_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(4, 0),
            coord_sys.coords_to_point(4, 8),
            direction=LEFT
        )
        tigran_rect_height_brace_label = tigran_rect_height_brace.get_tex("8").scale(1.5)
        self.play(GrowFromCenter(tigran_rect_height_brace))
        self.wait()
        self.play(Write(tigran_rect_height_brace_label))
        self.wait()

        tigran_const_speed_road = MathTex("8", "\\cdot", "8", font_size=NUM_FONT_SIZE)
        tigran_const_speed_road.move_to(tigran_const_speed_road_graph.get_center())
        self.play(
            AnimationGroup(
                TransformFromCopy(tigran_rect_height_brace_label, tigran_const_speed_road[0]),
                TransformFromCopy(tigran_rect_width_brace_label, tigran_const_speed_road[2]),
                Write(tigran_const_speed_road[1]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            FadeOut(
                tigran_rect_width_brace,
                tigran_rect_width_brace_label,
                tigran_rect_height_brace,
                tigran_rect_height_brace_label
            ),
            Transform(
                tigran_const_speed_road,
                MathTex("64", font_size=NUM_FONT_SIZE).move_to(tigran_const_speed_road_graph.get_center())
            )
        )
        self.wait()

        tigran_triangle_height_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(4, 0),
            coord_sys.coords_to_point(4, 8),
            direction=RIGHT
        )
        tigran_triangle_height_brace_label = tigran_triangle_height_brace.get_tex("8").scale(1.5)
        self.play(GrowFromCenter(tigran_triangle_height_brace))
        self.wait()
        self.play(Write(tigran_triangle_height_brace_label))
        self.wait()

        tigran_triangle_width_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(0, 0),
            coord_sys.coords_to_point(4, 0),
            direction=DOWN,
            buff=.5
        )
        tigran_triangle_width_brace_label = tigran_triangle_width_brace.get_tex("4").scale(1.5)
        self.play(GrowFromCenter(tigran_triangle_width_brace))
        self.wait()
        self.play(Write(tigran_triangle_width_brace_label))
        self.wait()

        tigran_acceleration_road = MathTex("\\frac{4 \\cdot 8}{2}")
        tigran_acceleration_road.move_to(tigran_acceleration_road_graph.copy().scale(.58, about_edge=DR))
        self.play(
            AnimationGroup(
                TransformFromCopy(
                    tigran_triangle_width_brace_label,
                    tigran_acceleration_road[0][0]
                ),
                TransformFromCopy(
                    tigran_triangle_height_brace_label,
                    tigran_acceleration_road[0][2]
                ),
                Write(tigran_acceleration_road[0][1]),
                Write(tigran_acceleration_road[0][3:]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            Transform(
                tigran_acceleration_road,
                MathTex("16", font_size=NUM_FONT_SIZE).move_to(tigran_acceleration_road_graph.copy().scale(.59, about_edge=DR))
            ),
            FadeOut(
                tigran_triangle_width_brace,
                tigran_triangle_width_brace_label,
                tigran_triangle_height_brace,
                tigran_triangle_height_brace_label
            )
        )
        self.wait()

        tigran_passed_road_tex = MathTex("16", "+", "64", font_size=NUM_FONT_SIZE)
        tigran_passed_road_tex.move_to(tigran_road)

        self.play(
            tigran_acceleration_road_graph.animate.set_stroke(width=0),
            tigran_const_speed_road_graph.animate.set_stroke(width=0)
        )
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    tigran_acceleration_road,
                    tigran_passed_road_tex[0]
                ),
                ReplacementTransform(
                    tigran_const_speed_road,
                    tigran_passed_road_tex[2]
                ),
                Write(tigran_passed_road_tex[1]),
                lag_ratio=.5
            )
        )
        self.wait()
        self.play(
            Transform(
                tigran_passed_road_tex,
                MathTex("80 \\text{մ}", font_size=1.3*NUM_FONT_SIZE).move_to(tigran_road)
            )
        )
        self.wait()

        tigran_road_info = MathTex("S_{\\text{Տիգրան}} = ", "80\\text{մ}", font_size=0.7*NUM_FONT_SIZE, color=BLUE)
        tigran_road_info.to_corner(UR)

        self.play(
            AnimationGroup(
                Write(tigran_road_info[0]),
                ReplacementTransform(
                    tigran_passed_road_tex,
                    tigran_road_info[1]
                ),
                lag_ratio=.5
            )
        )
        self.wait()

        # calculate Gagik's passed road
        self.play(FadeOut(tigran_road))
        self.wait()

        self.play(
            FadeIn(gagik_road),
            VGroup(
                tigran_acceleration_coord_lines,
                tigran_acceleration_coord_point,
                tigran_acceleration_graph,
                tigran_const_speed_graph
            ).animate.set_opacity(.5)
        )
        self.wait()

        self.play(
            gagik_acceleration_road_graph.animate.set_stroke(ORANGE, 4, opacity=1),
            gagik_const_speed_road_graph.animate.set_stroke(ORANGE, 4, opacity=1)
        )
        self.wait()

        gagik_rect_width_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(3, 0),
            coord_sys.coords_to_point(12, 0),
            buff=.5,
            direction=DOWN
        )
        gagik_rect_width_brace_label = gagik_rect_width_brace.get_tex("12-3").scale(1.5)
        self.play(GrowFromCenter(gagik_rect_width_brace))
        self.wait()
        self.play(Write(gagik_rect_width_brace_label))
        self.wait()
        self.play(
            Transform(
                gagik_rect_width_brace_label,
                gagik_rect_width_brace.get_tex("9").scale(1.5)
            )
        )
        self.wait()

        gagik_rect_height_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(3, 0),
            coord_sys.coords_to_point(3, 9),
            direction=LEFT
        )
        gagik_rect_height_brace_label = gagik_rect_height_brace.get_tex("9").scale(1.5)
        self.play(GrowFromCenter(gagik_rect_height_brace))
        self.wait()
        self.play(Write(gagik_rect_height_brace_label))
        self.wait()

        gagik_const_speed_road = MathTex("9", "\\cdot", "9", font_size=NUM_FONT_SIZE)
        gagik_const_speed_road.move_to(gagik_const_speed_road_graph.get_center())
        self.play(
            AnimationGroup(
                TransformFromCopy(gagik_rect_height_brace_label, gagik_const_speed_road[0]),
                TransformFromCopy(gagik_rect_width_brace_label, gagik_const_speed_road[2]),
                Write(gagik_const_speed_road[1]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            FadeOut(
                gagik_rect_width_brace,
                gagik_rect_width_brace_label,
                gagik_rect_height_brace,
                gagik_rect_height_brace_label
            ),
            Transform(
                gagik_const_speed_road,
                MathTex("81", font_size=NUM_FONT_SIZE).move_to(gagik_const_speed_road_graph.get_center())
            )
        )
        self.wait()

        gagik_triangle_height_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(3, 0),
            coord_sys.coords_to_point(3, 9),
            direction=RIGHT
        )
        gagik_triangle_height_brace_label = gagik_triangle_height_brace.get_tex("9").scale(1.5)
        self.play(GrowFromCenter(gagik_triangle_height_brace))
        self.wait()
        self.play(Write(gagik_triangle_height_brace_label))
        self.wait()

        gagik_triangle_width_brace = BraceBetweenPoints(
            coord_sys.coords_to_point(0, 0),
            coord_sys.coords_to_point(3, 0),
            direction=DOWN,
            buff=.5
        )
        gagik_triangle_width_brace_label = gagik_triangle_width_brace.get_tex("3").scale(1.5)
        self.play(GrowFromCenter(gagik_triangle_width_brace))
        self.wait()
        self.play(Write(gagik_triangle_width_brace_label))
        self.wait()

        gagik_acceleration_road = MathTex("\\frac{3 \\cdot 9}{2}")
        gagik_acceleration_road.move_to(gagik_acceleration_road_graph.copy().scale(.58, about_edge=DR))
        self.play(
            AnimationGroup(
                TransformFromCopy(
                    gagik_triangle_width_brace_label,
                    gagik_acceleration_road[0][0]
                ),
                TransformFromCopy(
                    gagik_triangle_height_brace_label,
                    gagik_acceleration_road[0][2]
                ),
                Write(gagik_acceleration_road[0][1]),
                Write(gagik_acceleration_road[0][3:]),
                lag_ratio=.5
            )
        )
        self.wait()

        self.play(
            Transform(
                gagik_acceleration_road,
                MathTex("13.5", font_size=0.6*NUM_FONT_SIZE).move_to(gagik_acceleration_road_graph.copy().scale(.59, about_edge=DR)).shift(LEFT*0.07)
            ),
            FadeOut(
                gagik_triangle_width_brace,
                gagik_triangle_width_brace_label,
                gagik_triangle_height_brace,
                gagik_triangle_height_brace_label
            )
        )
        self.wait()

        gagik_passed_road_tex = MathTex("13.5", "+", "81", font_size=NUM_FONT_SIZE)
        gagik_passed_road_tex.move_to(gagik_road)

        self.play(
            gagik_acceleration_road_graph.animate.set_stroke(width=0),
            gagik_const_speed_road_graph.animate.set_stroke(width=0)
        )
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    gagik_acceleration_road,
                    gagik_passed_road_tex[0]
                ),
                ReplacementTransform(
                    gagik_const_speed_road,
                    gagik_passed_road_tex[2]
                ),
                Write(gagik_passed_road_tex[1]),
                lag_ratio=.5
            )
        )
        self.wait()
        self.play(
            Transform(
                gagik_passed_road_tex,
                MathTex("94.5 \\text{մ}", font_size=1.3*NUM_FONT_SIZE).move_to(gagik_road)
            )
        )
        self.wait()

        gagik_road_info = MathTex("S_{\\text{Գագիկ}} = ", "94.5\\text{մ}", font_size=.7*NUM_FONT_SIZE, color=RED)
        gagik_road_info.next_to(tigran_road_info, LEFT, buff=1)

        self.play(
            AnimationGroup(
                Write(gagik_road_info[0]),
                ReplacementTransform(
                    gagik_passed_road_tex,
                    gagik_road_info[1]
                ),
                lag_ratio=.5
            )
        )
        self.wait()

        # calculate their distance
        self.play(
            FadeOut(
                runers,
                coord_sys,
                coord_sys_x_label,
                coord_sys_y_label,
                tigran_const_speed_graph,
                tigran_acceleration_graph,
                tigran_acceleration_coord_lines,
                tigran_acceleration_coord_point,
                gagik_road,
                gagik_acceleration_graph,
                gagik_const_speed_graph,
                gagik_acceleration_coord_lines,
                gagik_acceleration_coord_point,
                gagik_finish_coord_lines,
                gagik_finish_coord_point
            )
        )

        self.play(
            VGroup(
                road,
                location_gagik,
                location_tigran,
                question_brace,
                question_brace_tex,
                finish_flag
            ).animate.move_to(ORIGIN)
        )
        self.wait()

        gagik_brace = BraceBetweenPoints(
            road.get_left(),
            road.get_right(),
            direction=DOWN,
            color=RED
        )
        gagik_brace_label = gagik_brace.get_tex("94.5", "\\text{մ}")
        gagik_brace_label.scale(1.6).set_color(RED)

        self.play(Indicate(gagik_road_info))
        self.wait()
        self.play(GrowFromCenter(gagik_brace))
        self.wait()
        self.play(
            TransformFromCopy(
                gagik_road_info[-1],
                gagik_brace_label
            )
        )
        self.wait()

        tigran_brace = BraceBetweenPoints(
            road.get_left(),
            location_tigran.get_bottom(),
            direction=UP,
            buff=.01,
            color=BLUE
        ).scale(.99)
        tigran_brace_label = tigran_brace.get_tex("80", "\\text{մ}")
        tigran_brace_label.scale(1.6).set_color(BLUE)

        self.play(Indicate(tigran_road_info))
        self.wait()
        self.play(GrowFromCenter(tigran_brace))
        self.wait()
        self.play(
            TransformFromCopy(
                tigran_road_info[-1],
                tigran_brace_label
            )
        )
        self.wait()

        self.play(
            FadeOut(
                gagik_road_info,
                tigran_road_info
            )
        )

        self.play(Wiggle(question_brace))
        self.wait()

        difference = MathTex("94.5", "-", "80", "=", "14.5 \\text{մ}", font_size=NUM_FONT_SIZE)
        difference.next_to(road, UP, buff=3)
        difference[0].set_color(RED)
        difference[2].set_color(BLUE)
        difference[-1].set_color(GREEN)
        self.play(
            AnimationGroup(
                TransformFromCopy(
                    gagik_brace_label[0],
                    difference[0]
                ),
                TransformFromCopy(
                    tigran_brace_label[0],
                    difference[2]
                ),
                Write(difference[1]),
                Write(difference[3:]),
                lag_ratio=.5
            )
        )
        self.wait()

        answer_on_brace = question_brace.get_tex("14.5 \\text{մ}").set_color(GREEN)
        self.play(FadeOut(question_brace_tex))
        self.play(TransformFromCopy(difference[-1], answer_on_brace))
        self.wait()

        answer = Tex("Պատ.՝ $14.5$մ։")
        answer.to_edge(DR, buff=1)
        answer_srr_rect = SurroundingRectangle(answer, color=RED, buff=.2)
        self.play(
            Create(answer_srr_rect),
            Write(answer)
        )

        self.wait(2)
