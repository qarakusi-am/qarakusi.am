from manim import LEFT, UP, DOWN, RIGHT, DL, UL, DR, UR, PI, ORIGIN, rate_functions
from manim import FadeIn, Write, FadeOut, Create, Indicate
from manim import Group, VGroup, AnimationGroup
from manim import MathTex, Rectangle, Line, Axes, Circle, CurvedArrow, TAU, ArcBetweenPoints, Arrow, Dot, index_labels
from manim import ReplacementTransform
from manim import ORANGE, BLUE, PURE_RED, YELLOW, GREEN, BLACK, PURE_BLUE, RED

from qarakusiscene import QarakusiScene
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from objects import SimpleSVGMobject
from . import text


class Problem13082(QarakusiScene, FormulaModificationsScene):
    """լրիվ քառակուսի անջատելով լուծել հավասարումը """
    def construct(self):
        # -------------- Base ------------ #
        ax = Axes()
        circle_point = [-7.1, 2, 0]
        solution_point = [-1, 1, 0]
        MathTex.set_default(font_size=80)
        self.add_task_number(text=text.TASK_NUMBER_STR)
        # self.add_plane()
        # self.add(index_labels(tex_, color=YELLOW))

        # -------------------------- Point 1 ------------------------------- #
        operation_1 = MathTex(*text.OPERATION_1).shift(UP + 1.5 * LEFT)
        self.play(FadeIn(operation_1))  # r"x^{2}", r"+", r"14", r"x", r"-", r"32", r"=", r"0"
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        # self.fix_formula(operation_1)
        # self.rearrange_formula(operation_1, new_sequence=[0, 1, 2, 3, 6, 4, 5], move_up=[4, 5], remove=[7])
        #
        # self.play(ModifyFormula(operation_1, remove_items=[5]))

        self.play(operation_1[4:6].animate.shift(UP))
        self.play(AnimationGroup(
            operation_1[4:6].animate.shift(0.1 * RIGHT),
            FadeOut(operation_1[4]),
            FadeOut(operation_1[7]),
            operation_1[6].animate.shift(1.8 * LEFT),
            ))
        self.play(operation_1[5].animate.shift(DOWN))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        operation_2 = MathTex(*text.OPERATION_2).next_to(operation_1, DOWN).shift(DOWN)
        self.play(Write(operation_2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        operation_1 = VGroup(operation_1[0], operation_1[1], operation_1[2], operation_1[3], operation_1[5], operation_1[6])
        self.play(operation_1.animate.shift(2.1 * RIGHT))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        # self.add(index_labels(operation_2[0], color=PURE_RED))
        operation_1[0][0].set_color(RED)
        operation_1[3].set_color(RED)
        operation_2[1].set_color(RED)
        operation_2[5].set_color(RED)
        operation_2[8].set_color(RED)
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        arrow_1 = Arrow(operation_2[7].get_critical_point(UP), operation_1[2].get_critical_point(DOWN))
        self.play(Create(arrow_1))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        # self.fix_formula(operation_1)
        # self.play(ModifyFormula(operation_1,
        #                   replace_items=[[2]],
        #                   replace_items_strs=[[text.OPERATION_1_addition]]))
        operation_1_addition = MathTex(text.OPERATION_1_addition).next_to(operation_1[1])
        self.play(ReplacementTransform(operation_1[2], operation_1_addition),
                  operation_1[3:].animate.shift(0.6 * RIGHT))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        self.play(Indicate(operation_1_addition[0][2]), Indicate(operation_2[9]))
        self.wait()
        operation_1_addition[0][2].set_color(BLUE)
        operation_2[9].set_color(BLUE)
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        # self.add(index_labels(operation_2, color=PURE_RED))
        self.fix_formula(operation_2)
        self.play(ModifyFormula(operation_2,
                                replace_items=[[1], [5], [8], [3], [9], [11]],
                                replace_items_strs=[['x'], ['x'], ['x'], ['7'], ['7'], ['7']]))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        num_1 = operation_2[10:].copy()
        num_2 = num_1.copy()

        self.play(num_1.animate.next_to(operation_1))
        self.play(AnimationGroup(operation_1[-2:].animate.shift(1.7 * RIGHT),
                                 num_1.animate.shift(1.7 * RIGHT),
                                 num_2.animate.next_to(operation_1[3], buff=0.2, aligned_edge=ORIGIN).shift(0.15 * UP)))


        self.wait()
        self.wait(3)
