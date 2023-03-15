from manim import SurroundingRectangle
from manim import Write, FadeIn, FadeOut, AnimationGroup
from manim import TransformFromCopy, CounterclockwiseTransform
from manim import GREEN, RED, BLUE, GREY, WHITE
from manim import PI, UR, RIGHT, LEFT, UP, DOWN
from manim import Tex, MathTex, VGroup
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from .text import taskNumberString

FONT_SIZE = 65


class Problem12713(FormulaModificationsScene):
    def construct(self):
        self.taskNumber = taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)
        self.opacity = 0.6
        self.formulas = formulas = VGroup(
            Tex('$($', '$3$', '$x$', ' $-$ ', '$y$', '$)$', '$^2$', font_size=FONT_SIZE).next_to(2 * UP + 6.5 * LEFT,
                                                                                                 buff=0.2),  # (3x-y)^2
            Tex('$($', '$5$', '$x$', '$y$', ' $-$ ', '$2$', '$y$', '$)$', '$^2$', font_size=FONT_SIZE).next_to(
                1 * UP + 6.5 * LEFT, buff=0.2),  # (5xy-2y)^2
            Tex('$($', '$x$', '$^3$', ' $-$ ', '$3$', '$y$', '$)$', '$^2$', font_size=FONT_SIZE).next_to(6.5 * LEFT,
                                                                                                         buff=0.2),
            # (x^3-3y)^2
            Tex('$($', '$c$', '$^3$', '$d$', ' $-$ ', '$2$', '$c$', '$x$', '$)$', '$^2$', font_size=FONT_SIZE).next_to(
                DOWN + 6.5 * LEFT, buff=0.2))  # (c^3d-2cx)^2
        self.numbers = numbers = VGroup(
            *[MathTex(f'{i + 1}. ', font_size=FONT_SIZE - 7).next_to(formulas[i], LEFT, buff=0.3) for i in
              range(4)]).align_to(taskNumber, LEFT)

        self.play(
            AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5),
            run_time=4)
        self.wait(0.25)

        self.difference_square_prop = difference_square_prop = Tex(
            '$($', '$a$', ' $-$ ', '$b$', '$)$', '$^2$', ' $=$ ', '$a$', '$^2$', ' $-$ ', '$2$', '$a$', '$b$', ' $+$ ',
            '$b$', '$^2$',
            font_size=FONT_SIZE
        )  # (a-b)^2=a^2-2ab+b^2

        self.product_power_prop = Tex(
            '$($', '$a$', '$b$', '$)$', '$^n$', ' $=$ ', '$a$', '$^n$', r'$\cdot$', '$b$', ' $^n$ ',
            font_size=FONT_SIZE
        )  # (ab)^n=a^n * b^n
        self.power_of_power_prop = Tex(
            '$($', '$a$', '$^n$', '$)$', '$^m$', ' $=$ ', '$a$', '$^n$', r'$^\cdot$', '$^m$ ',
            font_size=FONT_SIZE
        )  # (a^n)^m=a^n*m

        difference_square_prop.to_corner(UR)
        self.rectangle = rectangle = SurroundingRectangle(difference_square_prop, color=GREEN)
        self.play(FadeIn(difference_square_prop), FadeIn(rectangle))
        self.wait(0.25)

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        self.wait(0.25)

        self.elements = VGroup(taskNumber, formulas, numbers, rectangle, difference_square_prop)
        self.first()
        self.second()
        self.third()
        self.fourth()

    def first(self):
        formulas = self.formulas
        difference_square_prop = self.difference_square_prop
        product_power_prop = self.product_power_prop

        self.equality1 = equality1 = difference_square_prop.copy().next_to(formulas[0], 2 * DOWN).align_to(formulas[0],
                                                                                                           LEFT)
        self.play(TransformFromCopy(difference_square_prop, equality1))
        self.wait()

        equality1[7:16].set_color(GREY)
        formulas[0][1:3].set_color(RED)
        self.wait(0.5)
        equality1[1].set_color(RED)
        self.wait()

        formulas[0][4].set_color(BLUE)
        self.wait(0.5)
        equality1[3].set_color(BLUE)
        self.wait()

        equality1[7:9].set_color(WHITE)

        self.fix_formula(equality1)
        equality1[11].animate.set_color(WHITE)
        self.play(ModifyFormula(equality1, replace_items=[[7]], replace_items_strs=[['$($', '$3$', '$x$', '$)$']],
                                replace_items_colors=[[RED, RED, RED, RED]]))
        self.wait()

        equality1[12:15].set_color(WHITE)
        self.play(ModifyFormula(equality1, replace_items=[[14]], replace_items_strs=[[r'$\cdot$', '$3$', '$x$']],
                                replace_items_colors=[[WHITE, RED, RED]]))
        self.wait()

        self.play(ModifyFormula(equality1, replace_items=[[17]], replace_items_strs=[[r'$\cdot$', '$y$']],
                                replace_items_colors=[[WHITE, BLUE]]))

        self.wait()
        equality1[19].set_color(WHITE)
        equality1[21].set_color(WHITE)

        self.play(
            ModifyFormula(equality1, replace_items=[[20]], replace_items_strs=[['$y$']], replace_items_colors=[[BLUE]]))

        self.wait(2)
        product_power_prop1 = product_power_prop.copy()
        self.play(Write(product_power_prop1.next_to(equality1[8], DOWN * 1.2), run_time=1.5))

        self.wait(2)
        self.play(ModifyFormula(product_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$3$'], ['$3$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[2], [9]], replace_items_strs=[['$x$'], ['$x$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[4], [7], [10]],
                                replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[6, 7, 8]], replace_items_strs=[['$9$']]))
        self.wait()

        self.play(ModifyFormula(equality1, replace_items=[[7, 8, 9, 10]], replace_items_strs=[['$9$', '$x$']]))
        self.wait()

        self.play(FadeOut(product_power_prop1))
        self.wait(2)
        self.play(ModifyFormula(equality1, replace_items=[[11, 12, 13]], replace_items_strs=[['$6$']]))
        self.wait()

        self.play(ModifyFormula(equality1, remove_items=[13]))
        self.wait()

        self.play(equality1[6:].animate.next_to(formulas[0], RIGHT).set_color(WHITE),
                  formulas[0].animate.set_color(WHITE),
                  FadeOut(equality1[0:6]))
        self.elements.add(equality1[6:])
        self.wait(2)

    def second(self):
        numbers = self.numbers
        formulas = self.formulas
        difference_square_prop = self.difference_square_prop
        product_power_prop = self.product_power_prop

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.wait()

        self.equality2 = equality2 = difference_square_prop.copy().next_to(formulas[1], 2 * DOWN)  # (a-b)^2=a^2-2ab+b^2
        equality2.align_to(formulas[1], LEFT)

        difference_square_prop_copy = difference_square_prop.copy()

        self.play(CounterclockwiseTransform(difference_square_prop_copy, equality2, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality2).remove(difference_square_prop_copy)
        self.fix_formula(equality2)
        self.wait()

        equality2[7:16].set_color(GREY)
        formulas[1][1:4].set_color(RED)
        self.wait(0.5)
        equality2[1].set_color(RED)
        self.wait()

        formulas[1][5:7].set_color(BLUE)
        self.wait(0.5)
        equality2[3].set_color(BLUE)
        self.wait()

        equality2[7:9].set_color(WHITE)

        self.play(
            ModifyFormula(equality2, replace_items=[[7]], replace_items_strs=[['$($', '$5$', '$x$', '$y$', '$)$']],
                          replace_items_colors=[[RED, RED, RED, RED, RED]]))
        self.wait()

        equality2[13:16].set_color(WHITE)
        self.play(ModifyFormula(equality2, replace_items=[[15]], replace_items_strs=[[r'$\cdot$', '$5$', '$x$', '$y$']],
                                replace_items_colors=[[WHITE, RED, RED, RED]]))
        self.wait()

        self.play(ModifyFormula(equality2, replace_items=[[19]], replace_items_strs=[[r'$\cdot$', '$2$', '$y$']],
                                replace_items_colors=[[WHITE, BLUE, BLUE]]))

        self.wait()
        equality2[22].set_color(WHITE)
        equality2[24].set_color(WHITE)

        self.play(ModifyFormula(equality2, replace_items=[[23]], replace_items_strs=[['$($', '$2$', '$y$', '$)$']],
                                replace_items_colors=[[BLUE, BLUE, BLUE, BLUE]]))

        self.wait(2)
        product_power_prop2 = product_power_prop.copy()
        self.play(Write(product_power_prop2.next_to(equality2[8], DOWN * 1.2)))
        self.wait(2)

        self.fix_formula(product_power_prop2)
        self.play(ModifyFormula(product_power_prop2, replace_items=[[1], [6]],
                                replace_items_strs=[['$($', '$5$', '$x$', '$)$'], ['$($', '$5$', '$x$', '$)$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[5], [15]], replace_items_strs=[['$y$'], ['$y$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[7], [13], [16]],
                                replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop2, replace_items=[[9, 10, 11, 12]],
                                replace_items_strs=[['$2$', '$5$', '$x$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, remove_items=[13]))

        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[7, 8, 9, 10, 11, 12]],
                                replace_items_strs=[['$2$', '$5$', '$x$', '$^2$', '$y$', '$^2$']]))
        self.play(FadeOut(product_power_prop2))

        self.wait(2)

        self.rearrange_formula(
            equality2, new_sequence=[*range(17), 19, 20, 17, 18, *range(21, 28)], move_down=[19, 20]
        )
        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[14, 15, 16, 17, 18]], replace_items_strs=[['$2$', '$0$']]))
        self.wait(2)

        self.play(ModifyFormula(equality2, replace_items=[[18]], replace_items_strs=[['$^2$']]))
        self.wait()

        self.play(ModifyFormula(equality2, replace_items=[[20, 21, 22, 23]], replace_items_strs=[['$4$', '$y$']]))
        self.wait(2)

        self.play(equality2[6:].animate.next_to(formulas[1], RIGHT).set_color(WHITE),
                  formulas[1].animate.set_color(WHITE),
                  FadeOut(equality2[0:6]))
        self.elements.add(equality2[6:])
        self.wait(2)

    def third(self):
        numbers = self.numbers
        formulas = self.formulas
        difference_square_prop = self.difference_square_prop
        power_of_power_prop = self.power_of_power_prop

        self.play(FadeIn(formulas[2]), FadeIn(numbers[2]))
        self.wait(0.25)

        self.equality3 = equality3 = difference_square_prop.copy().next_to(formulas[2], 2 * DOWN)  # (a-b)^2=a^2-2ab+b^2
        equality3.align_to(formulas[2], LEFT)

        difference_square_prop_copy = difference_square_prop.copy()
        self.play(CounterclockwiseTransform(difference_square_prop_copy, equality3, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality3).remove(difference_square_prop_copy)
        self.fix_formula(equality3)
        self.wait()

        equality3[7:16].set_color(GREY)
        formulas[2][1:3].set_color(RED)
        self.wait(0.5)
        equality3[1].set_color(RED)
        self.wait()

        formulas[2][4:6].set_color(BLUE)
        self.wait(0.5)
        equality3[3].set_color(BLUE)
        self.wait()

        equality3[7:9].set_color(WHITE)

        self.play(ModifyFormula(equality3, replace_items=[[7]], replace_items_strs=[['$($', '$x$', '$^3$', '$)$']],
                                replace_items_colors=[[RED, RED, RED, RED]]))
        self.wait()

        equality3[12:15].set_color(WHITE)
        self.play(ModifyFormula(equality3, replace_items=[[14]], replace_items_strs=[[r'$\cdot$', '$x$', '$^3$']],
                                replace_items_colors=[[WHITE, RED, RED]]))
        self.wait()

        self.play(ModifyFormula(equality3, replace_items=[[17]], replace_items_strs=[[r'$\cdot$', '$3$', '$y$']],
                                replace_items_colors=[[WHITE, BLUE, BLUE]]))

        self.wait()
        equality3[20].set_color(WHITE)
        equality3[22].set_color(WHITE)
        self.play(ModifyFormula(equality3, replace_items=[[21]], replace_items_strs=[['$($', '$3$', '$y$', '$)$']],
                                replace_items_colors=[[BLUE, BLUE, BLUE, BLUE]]))

        self.wait()
        power_of_power_prop1 = power_of_power_prop.copy()
        self.play(Write(power_of_power_prop1.next_to(equality3[8], DOWN * 1.2)))
        self.fix_formula(power_of_power_prop1)
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$x$'], ['$x$']]))
        self.wait()
        self.play(
            ModifyFormula(power_of_power_prop1, replace_items=[[2], [7]], replace_items_strs=[['$^3$'], ['$^3$']]))
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[4], [9]],
                                replace_items_strs=[['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[7, 8, 9]], replace_items_strs=[['$^6$']]))
        self.wait()
        self.play(ModifyFormula(equality3, replace_items=[[7, 8, 9, 10, 11]], replace_items_strs=[['$x$', '$^6$']]))
        self.play(FadeOut(power_of_power_prop1))
        self.wait(2)

        self.rearrange_formula(
            equality3, new_sequence=[*range(11), 14, 15, 11, 12, 13, *range(16, 23)], move_down=[14, 15]
        )
        self.wait()
        self.play(ModifyFormula(equality3, replace_items=[[10, 11, 12]], replace_items_strs=[['$6$']]))
        self.wait()
        self.play(ModifyFormula(equality3, remove_items=[11]))
        self.wait()

        self.play(
            ModifyFormula(equality3, replace_items=[[15, 16, 17, 18, 19]], replace_items_strs=[['$9$', '$y$', '$^2$']]))
        self.wait()

        self.play(equality3[6:].animate.next_to(formulas[2], RIGHT).set_color(WHITE),
                  formulas[2].animate.set_color(WHITE),
                  FadeOut(equality3[0:6]))
        self.elements.add(equality3[6:])
        self.wait(2)

    def fourth(self):
        numbers = self.numbers
        formulas = self.formulas
        difference_square_prop = self.difference_square_prop
        product_power_prop = self.product_power_prop
        power_of_power_prop = self.power_of_power_prop

        self.play(FadeIn(formulas[3]), FadeIn(numbers[3]))
        self.wait(0.25)

        equality4 = difference_square_prop.copy().next_to(formulas[3], 2 * DOWN)  # (a-b)^2=a^2-2ab+b^2
        equality4.align_to(formulas[3], LEFT)

        difference_square_prop_copy = difference_square_prop.copy()
        self.play(CounterclockwiseTransform(difference_square_prop_copy, equality4, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality4).remove(difference_square_prop_copy)
        self.wait(0.25)

        self.play(VGroup(self.elements, equality4).animate.shift(UP * 1.4))
        self.wait()
        equality4[7:16].set_color(GREY)
        formulas[3][1:4].set_color(RED)
        self.wait(0.5)
        equality4[1].set_color(RED)
        self.wait()

        formulas[3][5:8].set_color(BLUE)
        self.wait(0.5)
        equality4[3].set_color(BLUE)
        self.wait(2)

        equality4[7:9].set_color(WHITE)

        self.fix_formula(equality4)

        self.play(
            ModifyFormula(equality4, replace_items=[[7]], replace_items_strs=[['$($', '$c$', '$^3$', '$d$', '$)$']],
                          replace_items_colors=[[RED, RED, RED, RED, RED]]))
        self.wait()

        equality4[13:15].set_color(WHITE)
        self.play(
            ModifyFormula(equality4, replace_items=[[15]], replace_items_strs=[[r'$\cdot$', '$c$', '$^3$', '$d$']],
                          replace_items_colors=[[WHITE, RED, RED, RED]]))
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[19]], replace_items_strs=[[r'$\cdot$', '$2$', '$c$', '$x$']],
                                replace_items_colors=[[WHITE, BLUE, BLUE, BLUE]]))

        self.wait()

        equality4[23].set_color(WHITE)
        equality4[25].set_color(WHITE)
        self.play(
            ModifyFormula(equality4, replace_items=[[24]], replace_items_strs=[['$($', '$2$', '$c$', '$x$', '$)$']],
                          replace_items_colors=[[BLUE, BLUE, BLUE, BLUE, BLUE]]))

        self.wait(2)
        product_power_prop1 = product_power_prop.copy()

        self.play(Write(product_power_prop1.next_to(equality4[8], DOWN * 1.2)))
        self.fix_formula(product_power_prop1)
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[1], [6]],
                                replace_items_strs=[['$($', '$c$', '$^3$''$)$'], ['$($', '$c$', '$^3$''$)$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[4], [13]], replace_items_strs=[['$d$'], ['$d$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[6], [11], [14]],
                                replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait(2)

        power_of_power_prop1 = power_of_power_prop.copy()
        self.play(Write(power_of_power_prop1.next_to(product_power_prop1[12], DOWN * 2.2)))
        self.fix_formula(power_of_power_prop1)
        self.wait(2)
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$c$'], ['$c$']]))
        self.wait()
        self.play(
            ModifyFormula(power_of_power_prop1, replace_items=[[2], [7]], replace_items_strs=[['$^3$'], ['$^3$']]))
        self.wait()
        self.play(
            ModifyFormula(power_of_power_prop1, replace_items=[[4], [9]], replace_items_strs=[['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[7, 8, 9]], replace_items_strs=[['$^6$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[8, 9, 10, 11, 12]],
                                replace_items_strs=[['$c$', '$^6$']]))
        self.play(FadeOut(power_of_power_prop1))

        self.wait()
        self.play(ModifyFormula(equality4, replace_items=[[7, 8, 9, 10, 11, 12]],
                                replace_items_strs=[['$c$', '$^6$', '$d$', '$^2$']]))
        self.wait()
        self.play(FadeOut(product_power_prop1))
        self.wait(2)

        self.rearrange_formula(equality4, new_sequence=[*range(13), 17, 18, 13, 14, 15, 16, *range(19, 28)],
                               move_down=[17, 18])
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[12, 13, 14]], replace_items_strs=[['$4$']]))
        self.wait()
        self.play(ModifyFormula(equality4, remove_items=[13]))
        self.wait()

        self.rearrange_formula(equality4, new_sequence=[*range(15), 16, 15, *range(17, 25)], move_down=[16])
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[14, 15]], replace_items_strs=[['$^4$']]))
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[18, 19, 20, 21, 22, 23]],
                                replace_items_strs=[['$4$', '$c$', '$^2$', '$x$', '$^2$']]))
        self.wait()

        self.play(equality4[6:].animate.next_to(formulas[3], RIGHT).set_color(WHITE),
                  formulas[3].animate.set_color(WHITE),
                  FadeOut(equality4[0:6]))
        self.wait()

        self.play(VGroup(self.elements, equality4[6:]).animate.shift(DOWN * 1.4))
        self.wait()
