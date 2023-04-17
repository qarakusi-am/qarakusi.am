from qarakusiscene import QarakusiScene
from objects import SimpleSVGMobject
from hanrahashiv import ModifyFormula, FormulaModificationsScene
from . import text

from manim import LEFT, DOWN, RIGHT
from manim import FadeOut, Write, FadeIn
from manim import VGroup, ReplacementTransform, SurroundingRectangle, Group
from manim import Line, MathTex
from manim import UL, DR, UR, DL, UP, ORIGIN
from manim import RED
from manim import MovingCameraScene



class Problem12753(QarakusiScene, FormulaModificationsScene, MovingCameraScene):
    """Հասմիկն ընտրեց 10 տառ և որոշեց յուրաքանչյուր թվանշանի փոխարեն օգտագործել տառերից մեկը։
    Նա ասաց, որ իր եղբայր Գագիկը ծնվել է ԳԱԳՈ թվականին, իսկ ԳԱԹԱ թվականին կդառնա 19 տարեկան։
    Ո՞ր թվականին է ծնվել Գագիկը։"""
    def construct(self):
        condition_point = [-5.3, 3.40, 0]
        self.add_task_number(text=text.TASK_NUMBER_STR)
        self.add_plane()
        MathTex.set_default(font_size=60)

        # -------------------------- Point 1 ------------------------------- #
        girl = SimpleSVGMobject("people/children/girl_4").scale(1.5)
        self.play(FadeIn(girl))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        nums_1 = MathTex(*list(range(1, 10)))
        nums_1.arrange(DOWN, buff=0.3).to_edge().shift(0.1 * RIGHT + 0.3 * DOWN)
        self.play(Write(nums_1, run_time=2))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        question_marks = VGroup(*[MathTex(text.QUESTION_MARK).next_to(nums_1[i]) for i in range(9)])
        self.play(Write(question_marks, run_time=2))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        self.play(FadeOut(girl))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).next_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        condition_2 = MathTex(*text.CONDITION_2).next_to(condition_1, DOWN, aligned_edge=LEFT)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        condition_3 = MathTex(text.CONDITION_3).next_to(condition_2, DOWN, aligned_edge=LEFT).shift(0.5 * DOWN)
        self.play(Write(condition_3))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_4 = MathTex(*text.CONDITION_4)
        condition_4[0].next_to(condition_3[0][0]).shift(0.9 * RIGHT)
        condition_4[1].next_to(condition_3).shift(4 * RIGHT)
        self.play(ReplacementTransform(condition_3, condition_4))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        gata = condition_2[1].copy()
        self.play(gata.animate.next_to(condition_4[0], DOWN).shift(0.3 * DOWN))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        one = MathTex("1").move_to(gata[0][0])
        self.play(ReplacementTransform(gata[0][0], one))
        self.play(one.animate.scale(1.4))
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        condition_5 = MathTex(*text.CONDITION_5)
        condition_5.arrange(DOWN).next_to(gata, DOWN, aligned_edge=LEFT).shift(0.2 * DOWN + 1.4 * LEFT)
        self.play(Write(condition_5))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        line_1 = Line([-5, condition_4[0].get_critical_point(UL)[1], 0],
                      [-0.8, condition_5[-1].get_critical_point(DR)[1], 0],
                      color=RED,
                      stroke_width=7)
        line_2 = Line([-0.8, condition_4[0].get_critical_point(UR)[1], 0],
                      [-5, condition_5[-1].get_critical_point(DL)[1], 0],
                      color=RED,
                      stroke_width=7)
        self.play(Write(line_1), Write(line_2))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        # gago = MathTex(*text.GAGO).arrange(buff=0.3).next_to(condition_4[1], DOWN).shift(0.27 * DOWN + 0.06 * RIGHT)
        # gata1 = MathTex(*text.GATA).arrange(buff=0.3).next_to(gago, DOWN).shift(DOWN + 0.04 * RIGHT)
        self.play(self.camera.frame.animate.move_to(condition_4[1]).scale(0.7).shift(1.8 * DOWN), run_time=1.5)
        # gago = MathTex(*text.GAGO).next_to(condition_4[1], DOWN).shift(0.27 * DOWN + 0.06 * RIGHT)
        # gata1 = MathTex(*text.GATA).next_to(gago, DOWN).shift(DOWN + 0.04 * RIGHT)

        positions_gago = ([1.9, 2.74, 0], [2.74, 2.74, 0], [ 3.6, 2.74, 0], [4.5, 2.74, 0])
        gago = MathTex(*text.GAGO).next_to(condition_4[1], DOWN).shift(0.27 * DOWN + 0.06 * RIGHT)
        for i, p in enumerate(positions_gago):
            gago[i].next_to(p)
        # [i.next_to(p) for p, i in (positions_gago, gago)]

        positions_gata = ([1.9, -1.39, 0], [2.74, -1.39, 0], [3.6, -1.39, 0], [4.5, -1.39, 0])
        gata1 = MathTex(*text.GATA).next_to(gago, DOWN).shift(DOWN + 0.04 * RIGHT)
        for i, p in enumerate(positions_gata):
            gata1[i].next_to(p)

        # [gata1[i].next_to(p) for p, i in (positions_gata, len(gata1))]
        # print(gata1[0].get_critical_point(ORIGIN), gata1[1].get_critical_point(ORIGIN), gata1[2].get_critical_point(ORIGIN), gata1[3].get_critical_point(ORIGIN))
        self.play(Write(gata1))
        self.play(Write(gago))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        self.fix_formula(gata1)
        self.fix_formula(gago)
        self.play(ModifyFormula(gago,
                                replace_items=[[0], [2]],
                                replace_items_strs=[[r"\text{ 2 }"], [r"\text{ 2 }"]],
                                ),
                  ModifyFormula(gata1,
                                replace_items=[[0]],
                                replace_items_strs=[[r"\text{ 2 }"]],
                                ))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        self.fix_formula(gata1)
        self.fix_formula(gago)
        self.play(ModifyFormula(gata1,
                                replace_items=[[1], [3]],
                                replace_items_strs=[[r"\text{ 0 }"], [r"\text{ 0 }"]],
                                ),
                  ModifyFormula(gago,
                                replace_items=[[1]],
                                replace_items_strs=[[r"\text{ 0 }"]],
                                ))
        self.wait()

        # -------------------------- Point 16 ------------------------------- #
        condition_6 = MathTex(text.CONDITION_6).next_to(gago, DOWN).shift(0.19 * DOWN + 0.8 * RIGHT)
        plus = MathTex(text.PLUS).next_to(gago, DOWN, aligned_edge=LEFT).shift(0.4 * UP + 0.5 * LEFT)
        rectangle_1 = SurroundingRectangle(Group(gago[3], gata1[3]))
        line_3 = Line(gata1.get_critical_point(UL),
                      gata1.get_critical_point(UR),
                      stroke_width=4).shift(0.2 * UP).scale(1.2)
        self.play(Write(condition_6))
        self.play(Write(plus), Write(line_3))
        self.play(Write(rectangle_1))

        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        self.play(ModifyFormula(gago,
                                replace_items=[[3]],
                                replace_items_strs=[[r"\text{ 1 }"]],
                                ))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        self.play(ModifyFormula(gata1,
                                replace_items=[[2]],
                                replace_items_strs=[[r"\text{ 4 }"]],
                                ))
        self.wait()

        # -------------------------- Point 19 ------------------------------- #
        self.play(FadeOut(rectangle_1))
        self.wait(1)
        rectangle_2 = SurroundingRectangle(gago)
        self.play(FadeIn(rectangle_2))
        self.wait(3)
