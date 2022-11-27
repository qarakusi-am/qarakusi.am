from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from manim import FadeIn, Tex, Write, Indicate, CounterclockwiseTransform, AnimationGroup, FadeOut, ReplacementTransform, Transform, SurroundingRectangle, VGroup
from manim import DOWN, LEFT, UL, DR, UR, PI, UP
from manim import ORANGE, GREEN, WHITE, BLACK
from .text import *

BIG_FONT_SIZE = 70

class Problem12658(FormulaModificationsScene):
    def construct(self):
        self.wait()
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # a(b+c) = ab + ac
        pakagceri_bacum_tex = Tex("$a$", "$($", "$b$", "$+$", "$c$", "$)$", " $=$ ", "$a$", "$b$", " $+$ ", "$a$", "$c$", font_size=BIG_FONT_SIZE)
        pakagceri_bacum_tex.set_color_by_tex("a", ORANGE)
        pakagceri_bacum_srr_rect = SurroundingRectangle(pakagceri_bacum_tex, color=GREEN)
        pakagceri_bacum = VGroup(pakagceri_bacum_tex, pakagceri_bacum_srr_rect).to_edge(UR)
        self.play(FadeIn(pakagceri_bacum))
        self.wait()
        self.play(Indicate(pakagceri_bacum))
        self.wait()
        
        formula = Tex("$2$", "$x$", "$($", "$4$", "$x$", "$+$", "$3$", "$)$", " $=$ ", "$2$", "$x$", "$\\cdot$", "$4$", "$x$", " $+$ ", "$2$", "$x$", "$\\cdot$", "$3$", " $=$ ", "$8$", "$x$", "$^2$", " $+$ " "$6$", "$x$", font_size=BIG_FONT_SIZE)
        formula[:2].set_color(ORANGE)
        formula[9:11].set_color(ORANGE)
        formula[15:17].set_color(ORANGE)
        self.play(Write(formula[:8]))
        self.wait()

        temp1 = formula[:2].copy()
        temp2 = formula[3:5].copy()
        self.play(Write(formula[8]))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    CounterclockwiseTransform(temp1, formula[9:11], path_arc=PI/2),
                    CounterclockwiseTransform(temp2, formula[12:14], path_arc=PI/2)
                ),
                Write(formula[11]),
                lag_ratio=.5
            )
        )
        self.add(
            formula[9:11],
            formula[11:14]
        )
        self.remove(
            temp1,
            temp2
        )
        self.wait()

        temp1 = formula[:2].copy()
        temp2 = formula[6].copy()
        self.play(Write(formula[14]))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    CounterclockwiseTransform(temp1, formula[15:17], path_arc=PI/2),
                    CounterclockwiseTransform(temp2, formula[18], path_arc=PI/2)
                ),
                Write(formula[17], run_time=.5),
                lag_ratio=.5
            )
        )
        self.add(
            formula[15:17],
            formula[18]
        )
        self.remove(
            temp1,
            temp2
        )
        self.wait()

        self.play(Write(formula[19:23]))
        self.wait()

        self.play(Write(formula[23:]))
        self.wait()

        self.rearrange_formula(
            formula,
            [20, 21, 22, 23, 24, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7],
            move_up=[20, 21, 22, 23, 24],
            move_down=[0, 1, 2, 3, 4, 5, 6, 7])
        self.wait()

        self.play(
            Indicate(formula[6:11]),
            Indicate(formula[12:16])
        )
        self.wait()

        self.play(
            formula[6:8].animate.scale(1.3),
            formula[12:14].animate.scale(1.3)
        )
        self.wait()

        self.play(FadeOut(formula))
        self.wait()

        # task 1
        task1 = Tex("1) ", "$x$", "$^2$", " $+$ ", "$4$", "$x$", font_size=BIG_FONT_SIZE)
        task1.to_edge(UL, buff=.4).shift(DOWN*.8)
        self.play(Write(task1))
        self.wait()

        task1_copy = Tex("$x$", "$^2$", " $+$ ", "$4$", "$x$", font_size=BIG_FONT_SIZE)
        task1_copy.align_to(task1, DR)
        self.play(task1_copy.animate.shift(DOWN))
        self.wait()

        self.fix_formula(task1_copy)
        self.play(
            ModifyFormula(
                task1_copy,
                replace_items=[[0, 1]],
                replace_items_strs=[["$x$", "$\\cdot$", "$x$"]]
            )
        )
        self.wait()

        self.play(
            task1_copy[0].animate.set_color(ORANGE),
            task1_copy[5].animate.set_color(ORANGE)
        )
        self.wait()

        self.rearrange_formula(
            task1_copy,
            [0, 1, 2, 3, 5, 4],
            move_up=[5]
        )
        self.fix_formula(task1_copy)
        self.play(
            ModifyFormula(
                task1_copy,
                add_after_items=[4],
                add_items_strs=[["$\\cdot$"]]
            )
        )
        self.wait()

        self.play(Indicate(pakagceri_bacum))
        self.wait()

        temp = [" $=$ ", "$x$", "$($", "$x$", " $+$ ", "$4$", "$)$"]
        self.play(
            ModifyFormula(
                task1_copy,
                add_after_items=[6],
                add_items_strs=[temp],
                add_items_colors=[[BLACK] * len(temp)],
                new_formula_alignment=LEFT
            )
        )
        self.play(
            Write(task1_copy[7].set_color(WHITE)),
            Write(task1_copy[8].set_color(ORANGE))
        )
        self.wait()
        
        temp = task1_copy[2].copy()
        self.play(
            Write(task1_copy[9].set_color(WHITE)),
            CounterclockwiseTransform(temp, task1_copy[10].copy().set_color(WHITE), path_arc=PI/2)
        )
        task1_copy[10].set_color(WHITE)
        self.add(task1_copy[10])
        self.remove(temp)
        self.wait()

        temp = task1_copy[3].copy()
        self.play(CounterclockwiseTransform(temp, task1_copy[11].copy().set_color(WHITE), path_arc=PI/2))
        task1_copy[11].set_color(WHITE)
        self.add(task1_copy[11])
        self.remove(temp)
        self.wait()
        
        temp = task1_copy[6].copy()
        self.play(
            CounterclockwiseTransform(temp, task1_copy[12].copy().set_color(WHITE), path_arc=PI/2)
        )
        task1_copy[12].set_color(WHITE)
        self.add(task1_copy[12])
        self.remove(temp)
        self.play(
            Write(task1_copy[-1].set_color(WHITE))
        )
        self.wait()

        self.fix_formula(task1)
        temp = [" $=$ ", "$x$", "$($", "$x$", " $+$ ", "$4$", "$)$"]
        self.play(
            ModifyFormula(
                task1,
                add_after_items=[len(task1)-1],
                add_items_strs=[temp],
                add_items_colors=[[BLACK] * len(temp)],
                new_formula_alignment=LEFT
            )
        )
        temp = task1[6:].copy().set_color(WHITE)
        self.play(
            ReplacementTransform(task1_copy[7:], temp),
            FadeOut(task1_copy[:7])
        )
        task1[6:].set_color(WHITE)
        self.remove(temp)
        self.wait()

        # task 2
        task2 = Tex("2) ", "$2$", "$a$", "$^2$", "$b$", "$^3$", " $+$ ", "$a$", "$^5$", "$b$", "$^3$", font_size=BIG_FONT_SIZE)
        task2.next_to(task1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(task2))
        self.wait()

        task2_copy = Tex("$2$", "$a$", "$^2$", "$b$", "$^3$", " $+$ ", "$a$", "$^5$", "$b$", "$^3$", font_size=BIG_FONT_SIZE).align_to(task2, DR)
        self.play(task2_copy.animate.shift(DOWN*1.2))
        self.wait()
        self.fix_formula(task2_copy)
        self.play(
            ModifyFormula(
                task2_copy,
                replace_items=[[0, 1, 2, 3, 4]],
                replace_items_strs=[["$2$", "$\\cdot$", "$a$", "$\\cdot$", "$a$", "$\\cdot$", "$b$", "$\\cdot$", "$b$", "$\\cdot$", "$b$"]]
            )
        )
        self.wait()
        
        self.play(
            ModifyFormula(
                task2_copy,
                replace_items=[[12, 13, 14, 15]],
                replace_items_strs=[["$a$", "$\\cdot$", "$a$", "$\\cdot$", "$a$", "$\\cdot$", "$a$", "$\\cdot$", "$a$", "$\\cdot$", "$b$", "$\\cdot$", "$b$", "$\\cdot$", "$b$"]],
            )
        )
        self.wait()
        self.play(
            task2_copy[2].animate.set_color(ORANGE),
            task2_copy[4].animate.set_color(ORANGE),
            task2_copy[12].animate.set_color(ORANGE),
            task2_copy[14].animate.set_color(ORANGE)
        )
        self.wait()
        self.play(
            task2_copy[6].animate.set_color(ORANGE),
            task2_copy[8].animate.set_color(ORANGE),
            task2_copy[10].animate.set_color(ORANGE),
            task2_copy[22].animate.set_color(ORANGE),
            task2_copy[24].animate.set_color(ORANGE),
            task2_copy[26].animate.set_color(ORANGE)
        )
        self.wait()

        self.rearrange_formula(
            task2_copy,
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0, 11, 12, 13, 14, 21, 22, 23, 24, 25, 26, 15, 16, 17, 18, 19, 20],
            move_down=[
                2, 3, 4, 5, 6, 7, 8, 9, 10,
                21, 22, 23, 24, 25, 26
            ]
        )
        self.wait()

        self.play(
            ModifyFormula(
                task2_copy,
                replace_items=[[0, 1, 2, 3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17, 18, 19, 20], [22, 23, 24, 25, 26]],
                replace_items_strs=[["$a$", "$^2$", "$b$", "$^3$"], ["$a$", "$^2$", "$b$", "$^3$"], ["$a^3$"]],
                replace_items_colors=[[ORANGE, ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE, ORANGE]]
            )
        )
        self.wait()
        
        temp = [" $=$ ", "$a$", "$^2$", "$b$", "$^3$", "$($", "$2$", " $+$ ", "$a$", "$^3$", "$)$"]
        self.play(
            ModifyFormula(
                task2_copy,
                add_after_items=[12],
                add_items_strs=[temp],
                add_items_colors=[[BLACK] * len(temp)],
                new_formula_alignment=LEFT
            )
        )
        self.play(
            Write(task2_copy[13].set_color(WHITE)),
            Write(task2_copy[14:18].set_color(ORANGE))
        )
        self.wait()

        temp = task2_copy[5].copy()
        self.play(Write(task2_copy[18].set_color(WHITE)))
        self.play(CounterclockwiseTransform(temp, task2_copy[19].copy().set_color(WHITE)), path_arc=PI/2)
        task2_copy[19].set_color(WHITE)
        self.remove(temp)
        self.wait()

        temp = task2_copy[6].copy()
        self.play(CounterclockwiseTransform(temp, task2_copy[20].copy().set_color(WHITE)), path_arc=PI/2)
        task2_copy[20].set_color(WHITE)
        self.remove(temp)
        self.wait()

        temp = task2_copy[12:13].copy()
        self.play(CounterclockwiseTransform(temp, task2_copy[21:23].copy().set_color(WHITE)))
        task2_copy[21:23].set_color(WHITE)
        self.remove(temp)

        self.play(Write(task2_copy[-1].set_color(WHITE)))
        self.wait()

        task2 = Tex("2) ", "$2$", "$a$", "$^2$", "$b$", "$^3$", " $+$ ", "$a$", "$^5$", "$b$", "$^3$", " $=$ ", "$a$", "$^2$", "$b$", "$^3$", "$($", "$2$", " $+$ ", "$a$", "$^3$", "$)$", font_size=BIG_FONT_SIZE).align_to(task2, UL)
        self.play(
            ReplacementTransform(task2_copy[13:], task2[11:]),
            FadeOut(task2_copy[:13])
        )
        self.wait()

        # task 3
        task3 = Tex("3) ", "$6$", "$x$", "$y$", "$^5$", " $-$ ", "$9$", "$x$", "$^3$", "$y$", "$^3$", font_size=BIG_FONT_SIZE)
        task3.next_to(task2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(task3))
        self.wait()

        task3_copy = Tex("$6$", "$x$", "$y$", "$^5$", " $-$ ", "$9$", "$x$", "$^3$", "$y$", "$^3$", font_size=BIG_FONT_SIZE)
        task3_copy.align_to(task3, UR)
        self.play(task3_copy.animate.shift(DOWN))
        self.wait()

        temp = Tex("$3$", "$x$", "$y$", "$^3$", font_size=BIG_FONT_SIZE)
        temp.next_to(task3_copy, DOWN, aligned_edge=LEFT)
        self.play(Write(temp[0]))
        self.wait()
        self.play(Write(temp[1]))
        self.wait()
        self.play(Write(temp[2:]))
        self.wait()

        self.fix_formula(task3_copy)
        self.play(
            ModifyFormula(
                task3_copy,
                replace_items=[[0, 1, 2, 3]],
                replace_items_strs=[["$3$", "$x$", "$y$", "$^3$", "$\\cdot$", "$2$", "$y$", "$^2$"]]
            )
        )
        self.wait()
        self.play(FadeOut(temp))
        self.wait()

        self.play(
            ModifyFormula(
                task3_copy,
                replace_items=[[9, 10, 11, 12, 13]],
                replace_items_strs=[["$3$", "$x$", "$y$", "$^3$", "$\\cdot$", "$3$", "$x$", "$^2$"]]
            )
        )
        self.wait()

        self.play(
            task3_copy[:4].animate.set_color(ORANGE),
            task3_copy[9:13].animate.set_color(ORANGE)
        )
        self.wait()
        
        temp = [" $=$ ", "$3$", "$x$", "$y$", "$^3$", "$($", "$2$", "$y$", "$^2$", " $-$ ", "$3$", "$x$", "$^2$", "$)$"]
        self.play(
            ModifyFormula(
                task3_copy,
                add_after_items=[len(task3_copy)-1],
                add_items_strs=[temp],
                add_items_colors=[[BLACK] * len(temp)],
                new_formula_alignment=LEFT
            )
        )
        
        self.play(Write(task3_copy[17].set_color(WHITE)))
        self.wait()
        self.play(Write(task3_copy[18:22].set_color(ORANGE)))
        self.wait()
        self.play(Write(task3_copy[22].set_color(WHITE)))
        temp = task3_copy[5:8].copy()
        self.play(CounterclockwiseTransform(temp, task3_copy[23:26].copy().set_color(WHITE), path_arc=PI/2))
        task3_copy[23:26].set_color(WHITE)
        self.add(task3_copy[23:26])
        self.remove(temp)
        self.wait()

        temp = task3_copy[8].copy()
        self.play(CounterclockwiseTransform(temp, task3_copy[26].copy().set_color(WHITE), path_arc=PI/2))
        task3_copy[26].set_color(WHITE)
        self.add(task3_copy[26])
        self.remove(temp)
        self.wait()

        temp = task3_copy[14:17].copy()
        self.play(CounterclockwiseTransform(temp, task3_copy[-4:-1].copy().set_color(WHITE), path_arc=PI/2))
        task3_copy[-4:-1].set_color(WHITE)
        self.add(task3_copy[-4:-1])
        self.remove(temp)
        self.play(Write(task3_copy[-1].set_color(WHITE)))
        self.wait()

        temp = [" $=$ ", "$3$", "$x$", "$y$", "$^3$", "$($", "$2$", "$y$", "$^2$", " $-$ ", "$3$", "$x$", "$^2$", "$)$"]
        self.play(
            ModifyFormula(
                task3,
                add_after_items=[len(task3)-1],
                add_items_strs=[temp],
                add_items_colors=[[BLACK] * len(temp)],
                new_formula_alignment=LEFT
            )
        )

        self.play(
            Transform(task3_copy[17:], task3[11:].copy().set_color(WHITE)),
            FadeOut(task3_copy[:17])
        )
        task3[11:].set_color(WHITE)
        self.remove(task3_copy)
        self.wait()

        # task 4
        task4 = Tex("4) ", "$12$", "$m$", "$n$", "$^3$", " $+$ ", "$6$", "$m$", "$^2$", "$n$", "$^3$", " $-$ ", "$18$", "$m$", "$^2$", "$n$", "$^2$", font_size=BIG_FONT_SIZE)
        task4.next_to(task3, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(task4))
        self.wait()

        task4_copy = Tex("$12$", "$m$", "$n$", "$^3$", " $+$ ", "$6$", "$m$", "$^2$", "$n$", "$^3$", " $-$ ", "$18$", "$m$", "$^2$", "$n$", "$^2$", font_size=BIG_FONT_SIZE)
        task4_copy.align_to(task4, UR)
        self.play(task4_copy.animate.shift(DOWN))
        self.wait()
        
        self.fix_formula(task4_copy)
        self.play(
            ModifyFormula(
                task4_copy,
                replace_items=[[0, 1, 2, 3]],
                replace_items_strs=[["$6$", "$m$", "$n$", "$^2$", "$\\cdot$", "$2$", "$n$"]]
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                task4_copy,
                replace_items=[[8, 9, 10, 11, 12]],
                replace_items_strs=[["$6$", "$m$", "$n$", "$^2$", "$\\cdot$", "$m$", "$n$"]]
            )
        )
        self.wait()

        self.play(
            ModifyFormula(
                task4_copy,
                replace_items=[[16, 17, 18, 19, 20]],
                replace_items_strs=[["$6$", "$m$", "$n$", "$^2$", "$\\cdot$", "$3$", "$m$"]]
            )
        )
        self.wait()

        self.play(
            task4_copy[:4].animate.set_color(ORANGE),
            task4_copy[8:12].animate.set_color(ORANGE),
            task4_copy[16:20].animate.set_color(ORANGE)
        )
        self.wait()

        task4_copy1 = Tex("$6mn^2$", "$($", "$2n$", " $+$ ", "$mn$", " $-$ ", "$3m$", "$)$", font_size=BIG_FONT_SIZE)
        task4_copy1.next_to(task4_copy, DOWN, aligned_edge=LEFT).set_color(BLACK)

        self.play(
            Write(task4_copy1[0].set_color(ORANGE)),
            Write(task4_copy1[1].set_color(WHITE))
        )
        self.wait()

        self.play(ReplacementTransform(task4_copy[5:7].copy(), task4_copy1[2].set_color(WHITE)))
        self.wait()

        self.play(Write(task4_copy1[3].set_color(WHITE)))
        self.play(ReplacementTransform(task4_copy[13:15].copy(), task4_copy1[4].set_color(WHITE)))
        self.wait()
        
        self.play(Write(task4_copy1[5].set_color(WHITE)))
        self.play(ReplacementTransform(task4_copy[21:].copy(), task4_copy1[6].set_color(WHITE)))
        self.play(Write(task4_copy1[7].set_color(WHITE)))

        self.play(FadeOut(task4_copy))
        self.fix_formula(task4)
        self.play(
            task4_copy1.animate.shift(UP).set_color(WHITE),
            ModifyFormula(
                task4,
                add_after_items=[len(task4)-1],
                add_items_strs=[[" $=$ "]]
            )
        )
        self.wait()

        # task 5
        temp = []
        for obj in self.mobjects:
            if obj != taskNumber:
                temp.append(obj)
        self.play(*[FadeOut(obj) for obj in temp])
        self.wait()

        task5 = Tex("$4$", "$a$", "$^2$", "$b$", "$^5$", " $+$ ", "$6$", "$a$", "$^3$", "$b$", "$^5$", font_size=110)
        self.play(Write(task5))

        self.wait(2)
