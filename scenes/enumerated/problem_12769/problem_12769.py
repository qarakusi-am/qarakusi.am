from manim import Write, VGroup, AnimationGroup, ReplacementTransform, Arrow, always_redraw, ValueTracker
from manim import Dot, FadeOut, Line
from manim import MathTex, Tex, Axes, TransformFromCopy, Brace
from manim import Scene, RIGHT, LEFT, UP, DOWN, ORANGE, WHITE, BLUE_C
from .text import *
from qarakusiscene import TaskNumberBox
from hanrahashiv import FormulaModificationsScene, ModifyFormula


SMALL_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 60


class Problem12769(FormulaModificationsScene):
    def construct(self):
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait()

        self.coordinate_axes=coordinate_axes = Axes(
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
        ).shift(RIGHT*2.5)
        self.play(Write(coordinate_axes))
        self.wait()

        self.conditions = VGroup(
            Tex(condition1, font_size=SMALL_FONT_SIZE,width=50).align_to(taskNumber,LEFT).shift(UP*2.5),
            Tex(condition2, font_size=SMALL_FONT_SIZE,width=200).align_to(taskNumber, LEFT).shift(UP * 2.5),
            Tex(condition3, font_size=SMALL_FONT_SIZE, width=200).align_to(taskNumber, LEFT).shift(UP * 2.5),

        )
        # self.solve_for_condition1()
        # self.solve_for_condition2()
        self.solve_for_condition3()



    def solve_for_condition1(self):

        conditions=self.conditions
        coordinate_axes=self.coordinate_axes


        self.play(Write(conditions[0]))
        self.wait()

        coordinates = Tex("$($", "$x$"," $,$ ", "$y$", "$)$", font_size=MEDIUM_FONT_SIZE).scale(1.5).move_to(conditions[0], LEFT).shift(DOWN+RIGHT*3)
        self.play(Write(coordinates))
        self.wait(2)

        self.fix_formula(coordinates)
        self.play(ModifyFormula(coordinates, replace_items=[[1], [3]], replace_items_strs=[["$5$"], ["$5$"]]))
        self.wait()

        point = VGroup(Dot(point=coordinate_axes.c2p(5, 5, 0)),
                       Tex("(5, 5)", font_size=SMALL_FONT_SIZE).next_to(coordinate_axes.c2p(5, 5, 0)),
                       coordinate_axes.get_horizontal_line(coordinate_axes.c2p(5, 5, 0)),
                       coordinate_axes.get_vertical_line(coordinate_axes.c2p(5, 5, 0)))

        self.play(Write(point))
        self.wait()
        self.play(FadeOut(coordinates,conditions[0]))

    def solve_for_condition2(self):
        conditions = self.conditions
        coordinate_axes = self.coordinate_axes

        self.play(Write(conditions[1]))
        self.wait()

        coordinates = Tex("$($", "$x$", " $,$ ", "$y$", "$)$", font_size=MEDIUM_FONT_SIZE).move_to(conditions[0],
                                                                                                       LEFT).shift(
            DOWN + RIGHT * 3)
        self.play(Write(coordinates))
        self.wait(2)

        abscissa=Tex(abscissa_str,font_size=MEDIUM_FONT_SIZE).move_to(coordinates).shift(DOWN)
        arrow=Arrow(abscissa[0][3].get_top(),coordinates[2].get_bottom()).scale(1.5,1)
        self.play(Write(arrow),Write(abscissa))
        self.wait()
        self.fix_formula(coordinates)
        self.play(ModifyFormula(coordinates, replace_items=[[1]], replace_items_strs=[["$3$"]]))
        self.wait()

        equation=Tex("$3 + y = 7$",font_size=MEDIUM_FONT_SIZE).move_to(coordinates,LEFT).shift(DOWN)
        self.play(ReplacementTransform(VGroup(arrow,abscissa),equation))
        self.wait(2)

        self.play(ModifyFormula(coordinates, replace_items=[[3]], replace_items_strs=[["$4$"]]))
        self.wait()
        point = VGroup(Dot(point=coordinate_axes.c2p(3, 4, 0)),
                       Tex("(3, 4)", font_size=SMALL_FONT_SIZE).next_to(coordinate_axes.c2p(3, 4, 0)),
                       coordinate_axes.get_horizontal_line(coordinate_axes.c2p(3, 4, 0)),
                       coordinate_axes.get_vertical_line(coordinate_axes.c2p(3, 4, 0)))

        self.play(Write(point))
        self.wait()
        self.play(FadeOut(coordinates, conditions[1],equation))
        self.wait(2)

    def solve_for_condition3(self):
        conditions = self.conditions
        coordinate_axes = self.coordinate_axes

        self.play(Write(conditions[2]))
        self.wait(2)


        third_quarter = coordinate_axes.get_area(
            graph=coordinate_axes.plot(lambda x: 0, x_range=[-5.5, 5.3], ),
            bounded_graph=coordinate_axes.plot(lambda x: -5.5, x_range=[-5.5, 5.3], ),
            x_range=(-5.5, 0),
            color=ORANGE,
            opacity=0.5,
        )
        # third_quarter.z_index = third_quarter.z_index - 1

        self.play(AnimationGroup(Write(third_quarter)))
        self.wait()


        point = VGroup(Dot(point=coordinate_axes.c2p(-3, -2, 0)),
                       Tex("(-2, -5)", font_size=SMALL_FONT_SIZE).next_to(coordinate_axes.c2p(3, 4, 0)))
        dividing_line = coordinate_axes.plot(lambda x: -2, x_range=[-5.3, 5.3])

        self.play(Write(dividing_line, run_time=2,stroke_width=3))
        self.wait(2)
        self.play(Write(point[0]))
        self.wait()

        stopwatch = ValueTracker(3)
        time = always_redraw(lambda: MathTex(str(stopwatch.get_value() // 60)))
        self.play(Write(time))
        self.wait()
        self.play(stopwatch.animate.set_value(0))
        self.wait()
        # self.play(FadeOut(coordinates, conditions[1], equation))
        # self.wait(2)


