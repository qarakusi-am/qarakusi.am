from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw, ValueTracker, Transform
from manim import Dot, FadeOut, Line, BraceBetweenPoints
from manim import MathTex, Tex, Axes, TransformFromCopy, Brace
from manim import RIGHT, LEFT, UP, DOWN, ORANGE
from .text import *
from qarakusiscene import TaskNumberBox
from hanrahashiv import FormulaModificationsScene, ModifyFormula

FONT_SIZE = 40

class Problem12769(FormulaModificationsScene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait()

        self.coordinate_system = coordinate_system = Axes(
            x_range=[-6.5, 6.3, 1],
            y_range=[-6.5, 6.3, 1],
            x_length=8,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "tip_width": 0.2,
                "tip_height": 0.2
            },
            tips=True,
        ).shift(RIGHT * 1.85)
        self.points=VGroup()

        self.play(Write(coordinate_system))
        self.wait()

        self.conditions = VGroup(
            Tex(condition1, width=120).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition2, width=150).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition3, width=160).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition4, width=135).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition5, width=120).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition6, width=160).align_to(taskNumber, LEFT).shift(UP * 2.5),

        )
        self.solve_for_condition1()
        self.solve_for_condition2()
        self.solve_for_condition3()
        self.solve_for_condition4()
        self.solve_for_condition5()
        self.solve_for_condition6()

    def solve_for_condition1(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        coordinates = Tex("$A$", "$($", "$x$", " $,$ ", "$y$", "$)$", font_size=FONT_SIZE).scale(1.15).move_to(
            conditions[0], LEFT).shift(DOWN * 1.2 + RIGHT * 3)

        point = VGroup(Dot(point=coordinate_system.c2p(5, 5, 0)),
                       coordinate_system.get_horizontal_line(coordinate_system.c2p(5, 5, 0)),
                       coordinate_system.get_vertical_line(coordinate_system.c2p(5, 5, 0)))

        self.play(Write(conditions[0]))
        self.wait()

        self.play(Write(coordinates))
        self.wait(2)

        self.fix_formula(coordinates)
        self.play(ModifyFormula(coordinates, replace_items=[[2], [4]], replace_items_strs=[["$5$"], ["$5$"]]))
        self.wait()

        self.play(AnimationGroup(coordinates.animate.scale(1/1.15).next_to(coordinate_system.c2p(5, 5, 0)), Write(point)))
        self.wait(2)

        self.play(FadeOut(conditions[0], point[1:]))
        self.wait()

        #add to shift the whole coordinate system down in the end
        self.points.add(coordinates)
        self.points.add(point[0])

    def solve_for_condition2(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        coordinates = Tex("$B$", "$($", "$x$", " $,$ ", "$y$", "$)$", font_size=FONT_SIZE).scale(1.15).move_to(
            conditions[0], LEFT).shift(DOWN + RIGHT * 3)

        abscissa = Tex(abscissa_str, font_size=FONT_SIZE).move_to(coordinates).shift(DOWN * 1.4)
        arrow = Arrow(coordinates[2].get_bottom() + DOWN, coordinates[2].get_bottom()).scale(2, 1).shift(DOWN * 0.1)

        equation = Tex("$3 + y = 7$", font_size=FONT_SIZE).scale(1.15).move_to(coordinates, LEFT).shift(
            DOWN * 0.7)

        point = VGroup(Dot(point=coordinate_system.c2p(3, 4, 0)),
                       coordinate_system.get_horizontal_line(coordinate_system.c2p(3, 4, 0)),
                       coordinate_system.get_vertical_line(coordinate_system.c2p(3, 4, 0)))

        self.play(Write(conditions[1]))
        self.wait()

        self.play(Write(coordinates))
        self.wait(2)

        self.play(Write(arrow))
        self.play(Write(abscissa))
        self.wait()

        self.fix_formula(coordinates)
        self.play(ModifyFormula(coordinates, replace_items=[[2]], replace_items_strs=[["$3$"]]))
        self.wait(2)

        self.play(ReplacementTransform(VGroup(arrow, abscissa), equation))
        self.wait(2)

        self.play(ModifyFormula(coordinates, replace_items=[[4]], replace_items_strs=[["$4$"]]))
        self.wait()

        self.play(AnimationGroup(coordinates.animate.scale(1/1.15).next_to(coordinate_system.c2p(3, 4, 0)), Write(point)))
        self.wait(2)

        self.play(FadeOut(conditions[1], equation, point[1:]))
        self.wait()

        # add to shift the whole coordinate system down in the end
        self.points.add(coordinates)
        self.points.add(point[0])

    def solve_for_condition3(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        third_quarter = coordinate_system.get_area(
            graph=coordinate_system.plot(lambda x: 0, x_range=[-6.5, 0], ),
            bounded_graph=coordinate_system.plot(lambda x: -6.5, x_range=[-6.5, 0], ),
            x_range=(-6.5, 0),
            color=ORANGE,
            opacity=0.5,
        )
        third_quarter.z_index = third_quarter.z_index - 1

        # to move the point till finding its correct position
        line = coordinate_system.plot(lambda x: -2, x_range=[-6.5, 6.3])

        length_value = ValueTracker(1)
        length_from_x_axis = always_redraw(
            lambda: MathTex(str(round(length_value.get_value(), 2))).move_to(line, LEFT).shift(
                RIGHT * 1.7 + DOWN))

        brace = always_redraw(lambda: Brace(
            VGroup(Dot(coordinate_system.c2p(0, 0, 0)),
                   Dot(coordinate_system.c2p(round(length_value.get_value(), 2) * (-1) + 0.1, -2, 0)))).shift(LEFT * 0.1))

        point = always_redraw(lambda: Dot(coordinate_system.c2p(round(length_value.get_value(), 2) * (-1), -2, 0)))

        self.play(Write(conditions[2]))
        self.wait(2)

        self.play(Write(third_quarter))
        self.wait()

        self.play(Write(line, run_time=2, stroke_width=3))
        self.wait(2)

        self.play(Write(point))
        self.wait()

        self.play(AnimationGroup(Write(length_from_x_axis), Write(brace)))
        self.wait()

        self.play(length_value.animate.set_value(6), run_time=4)
        self.wait(3)

        point_coordinates = VGroup(
            Tex("$C(-6, -2)$", font_size=FONT_SIZE).next_to(coordinate_system.c2p(-6, -2, 0)).shift(UP * 0.25),
            coordinate_system.get_horizontal_line(coordinate_system.c2p(-6, -2, 0)),
            coordinate_system.get_vertical_line(coordinate_system.c2p(-6, -2, 0)))

        self.play(AnimationGroup(FadeOut(line), Write(point_coordinates[1:])))
        self.play(Write(point_coordinates[0]))
        self.wait(3)

        self.play(FadeOut(point_coordinates[1:], brace, length_from_x_axis, conditions[2], third_quarter))
        self.wait()

        # add to shift the whole coordinate system down in the end
        self.points.add(point_coordinates[0])

    def solve_for_condition4(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        helper_point = VGroup(Dot(point=coordinate_system.c2p(3, -5, 0)),
                              Tex("(3, -5)", font_size=FONT_SIZE).next_to(coordinate_system.c2p(3, -5, 0)))

        arrow = Arrow(helper_point[0].get_top(), coordinate_system.c2p(3, 0, 0), stroke_width=2,
                      max_tip_length_to_length_ratio=0.08).scale(1.2, 1).shift(DOWN * 0.1)

        abscissa_axes = Tex(abscissa_axis_str, font_size=FONT_SIZE).move_to(arrow, UP).shift(
            UP * 0.7 + RIGHT * 0.2)

        brace1 = VGroup(Tex("$5$", font_size=60).next_to(coordinate_system.c2p(4, -2.5, 0)),
                        BraceBetweenPoints(coordinate_system.c2p(3, -5, 0), coordinate_system.c2p(3, 0, 0))).shift(LEFT*0.14)
        brace2 = brace1.copy().shift(UP * 2.75)
        #put point up to make it visible behind A
        point = VGroup(Tex("$D(3, 5)$", font_size=FONT_SIZE).next_to(coordinate_system.c2p(2.5, 5.5, 0)),
                       Dot(point=coordinate_system.c2p(3, 5, 0)),
                       coordinate_system.get_horizontal_line(coordinate_system.c2p(3, 5, 0)),
                       coordinate_system.get_vertical_line(coordinate_system.c2p(3, 5, 0)))

        line = Line(coordinate_system.c2p(3, -5, 0), coordinate_system.c2p(3, 5, 0))

        self.play(Write(conditions[3]))
        self.wait()

        self.play(Write(helper_point))
        self.wait()

        self.play(Write(arrow))
        self.play(Write(abscissa_axes))
        self.wait(2)

        self.play(AnimationGroup(FadeOut(abscissa_axes, arrow), Write(line, run_time=2, stroke_width=3)))
        self.wait(2)

        self.play(Write(brace1))
        self.wait()

        self.play(TransformFromCopy(brace1, brace2))
        self.wait()

        self.play(Write(point))
        self.wait(2)

        self.play(FadeOut(line, helper_point, conditions[3], brace1, brace2, point[2:]))
        self.wait(2)

        # add to shift the whole coordinate system down in the end
        self.points.add(point[0:2])

    def solve_for_condition5(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        self.play(Write(conditions[4]))
        self.wait()

        coordinates = Tex("$E$","$($", "$x$", " $,$ ", "$y$", "$)$", font_size=FONT_SIZE).scale(1.15).move_to(conditions[0],
                                                                                                        LEFT).shift(
            DOWN + RIGHT * 3)
        self.play(Write(coordinates))
        self.wait(2)

        ordinate = Tex(ordinate_str, font_size=FONT_SIZE).move_to(coordinates).shift(DOWN * 1.4)
        arrow = Arrow(coordinates[4].get_bottom() + DOWN, coordinates[4].get_bottom()).scale(2, 1).shift(DOWN * 0.05)

        self.play(Write(arrow))
        self.play(Write(ordinate))
        self.wait()

        self.fix_formula(coordinates)
        self.play(ModifyFormula(coordinates, replace_items=[[4]], replace_items_strs=[["$3$"]]))
        self.wait(2)

        self.play(ModifyFormula(coordinates, replace_items=[[2]], replace_items_strs=[["$0$"]]))
        self.wait(2)

        point =Dot(point=coordinate_system.c2p(0, 3, 0))

        self.play(AnimationGroup(coordinates.animate.scale(1/1.15).next_to(coordinate_system.c2p(0, 3, 0)),Write(point)))
        self.wait(2)

        self.play(FadeOut( conditions[4], ordinate, arrow))
        self.wait()

        # add to shift the whole coordinate system down in the end
        self.points.add(coordinates)
        self.points.add(point)

    def solve_for_condition6(self):
        conditions = self.conditions
        coordinate_system = self.coordinate_system

        coordinates = Tex("$F$","$($", "$x$", " $,$ ", "$y$", "$)$", font_size=FONT_SIZE).scale(1.15).move_to(conditions[5],
                                                                                                        LEFT).shift(
            DOWN + RIGHT*1.5 )

        helper_equations = VGroup(Tex('$x\cdot y = -1$').next_to(coordinates, DOWN),
                                  Tex(x_y_are_whole_numbers, font_size=FONT_SIZE).next_to(coordinates,
                                                                                          DOWN).shift(
                                      DOWN * 0.7 + LEFT * .2),
                                  Tex('$x<0, y>0$', font_size=FONT_SIZE).scale(1.15).shift(UP),
                                  Tex("$x=-1, y=1$", font_size=FONT_SIZE).scale(1.15).next_to(coordinates, DOWN))

        self.play(Write(conditions[-1]))
        self.wait(2)

        self.play(Write(coordinates))
        self.wait(2)

        self.play(VGroup(coordinate_system,self.points).animate.shift(DOWN * 2))

        second_quarter = coordinate_system.get_area(
            graph=coordinate_system.plot(lambda x: 0, x_range=[-6.5, 0], ),
            bounded_graph=coordinate_system.plot(lambda x: 6.5, x_range=[-6.5, 0]),
            x_range=(-6.5, 0),
            color=ORANGE,
            opacity=0.5,
        )
        second_quarter.z_index = second_quarter.z_index - 1

        self.play(Write(second_quarter))
        self.wait()

        self.play(Write(helper_equations[0]))
        self.wait()

        self.play(Write(helper_equations[1]))
        self.wait()

        self.play(Write(helper_equations[2]))
        self.wait()

        self.play(Transform(VGroup(helper_equations[0:2]), helper_equations[-1]))
        self.wait(2)

        point = VGroup(Dot(point=coordinate_system.c2p(-1, 1, 0)),
                       coordinate_system.get_horizontal_line(coordinate_system.c2p(-1, 1, 0)),
                       coordinate_system.get_vertical_line(coordinate_system.c2p(-1, 1, 0)))

        self.play(Transform(helper_equations[-1], point[0]))
        self.wait()

        self.play(AnimationGroup(Write(point[1:]),coordinates.animate.scale(1/1.15).next_to(coordinate_system.c2p(-1, 1, 0)).shift(
                           LEFT * 1.5)))
        self.wait(3)
