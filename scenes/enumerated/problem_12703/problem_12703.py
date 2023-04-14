from manim import SurroundingRectangle
from manim import Write, FadeIn, FadeOut, AnimationGroup
from manim import TransformFromCopy, CounterclockwiseTransform
from manim import GREEN, RED, BLUE, GREY, WHITE
from manim import PI, UR, RIGHT, LEFT, UP, DOWN
from manim import Tex, MathTex, VGroup
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from .text import taskNumberString


FONT_SIZE=65
class Problem12703(FormulaModificationsScene):
    def construct(self):
        self.taskNumber=taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)
        self.opacity=0.6
        self.formulas = formulas = VGroup(
            Tex('$($','$2$', '$x$', ' $+$ ', '$y$','$)$', '$^2$', font_size=FONT_SIZE).next_to(2*UP + 6.5*LEFT, buff=0.2), # (2x+y)^2
            Tex('$($','$2$', '$m$', ' $+$ ', '$3$', '$n$','$)$', '$^2$', font_size=FONT_SIZE).next_to(1*UP + 6.5*LEFT, buff=0.2), # (2m+3n)^2
            Tex('$($', '$x$', '$^5$', ' $+$ ','$4$', '$y$','$)$', '$^2$', font_size=FONT_SIZE).next_to(6.5*LEFT, buff=0.2), #(x^5+4y)^2
            Tex('$($','$2$', '$a$', '$^2$', ' $+$ ','$3$', '$a$','$c$','$)$', '$^2$', font_size=FONT_SIZE).next_to(DOWN + 6.5*LEFT, buff=0.2)) #(2a^2+3ac)^2
        self.numbers = numbers = VGroup(*[MathTex(f'{i+1}. ', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3) for i in range(4)]).align_to(taskNumber, LEFT)
        
        self.play(AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5),run_time = 4 )
        self.wait(0.25)

        self.sum_square_prop = sum_square_prop = Tex(
           '$($','$a$',' $+$ ','$b$','$)$','$^2$',' $=$ ','$a$','$^2$',' $+$ ','$2$','$a$','$b$',' $+$ ','$b$','$^2$',
            font_size=FONT_SIZE
        ) # (a+b)^2=a^2+2ab+b^2

        self.product_power_prop  = Tex(
            '$($', '$a$', '$b$', '$)$', '$^n$', ' $=$ ', '$a$', '$^n$', r'$\cdot$','$b$', ' $^n$ ',
            font_size=FONT_SIZE
        )  # (ab)^n=a^n * b^n
        self.power_of_power_prop  = Tex(
            '$($', '$a$', '$^n$', '$)$', '$^m$', ' $=$ ', '$a$', '$^n$', r'$^\cdot$', '$^m$ ',
            font_size=FONT_SIZE
        )  # (a^n)^m=a^n*m

        sum_square_prop.to_corner(UR)
        self.rectangle = rectangle = SurroundingRectangle(sum_square_prop, color=GREEN)
        self.play(FadeIn(sum_square_prop), FadeIn(rectangle))
        self.wait(0.25)

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        self.wait(0.25)

        self.elements=VGroup(taskNumber,formulas,numbers,rectangle,sum_square_prop)
        self.first()
        self.second()
        self.third()
        self.fourth()
    def first(self):
        formulas = self.formulas
        sum_square_prop = self.sum_square_prop
        product_power_prop=self.product_power_prop

        self.equality1 =equality1= sum_square_prop.copy().next_to(formulas[0], 2*DOWN).align_to(formulas[0], LEFT)
        self.play(TransformFromCopy(sum_square_prop, equality1))
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
        self.wait()
        equality1[11].animate.set_color(WHITE)
        self.play(ModifyFormula(equality1, replace_items=[[7]], replace_items_strs=[['$($','$2$','$x$','$)$']],
                                replace_items_colors=[ [RED,RED,RED,RED]]))
        self.wait()

        equality1[12:15].set_color(WHITE)
        self.play(ModifyFormula(equality1, replace_items=[[14]],replace_items_strs=[[r'$\cdot$', '$2$', '$x$']],replace_items_colors=[ [WHITE,RED,RED]]))
        self.wait()

        self.play(ModifyFormula(equality1, replace_items=[[17]],  replace_items_strs=[[r'$\cdot$', '$y$']],replace_items_colors=[ [WHITE,BLUE]]))

        self.wait(2)
        equality1[19].set_color(WHITE)
        equality1[21].set_color(WHITE)

        self.play(ModifyFormula(equality1, replace_items=[[20]],replace_items_strs=[[ '$y$']],replace_items_colors=[ [BLUE]]))

        self.wait()
        product_power_prop1=product_power_prop.copy()
        self.play(Write(product_power_prop1.next_to(equality1[8],DOWN*1.2)))

        self.wait(2)
        self.play(ModifyFormula(product_power_prop1, replace_items=[[1],[6]], replace_items_strs=[['$2$'],['$2$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[2], [9]], replace_items_strs=[['$x$'], ['$x$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[4],[ 7],[10]], replace_items_strs=[['$^2$'], ['$^2$'],['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[6,7,8]],replace_items_strs=[['$4$']]))
        self.wait()
        self.play(ModifyFormula(equality1, replace_items=[[7,8,9,10]],replace_items_strs=[['$4$', '$x$']]))
        self.wait()
        self.play(FadeOut(product_power_prop1))
        self.wait()
        self.play( ModifyFormula(equality1, replace_items=[[ 11, 12,13 ]],replace_items_strs=[['$4$']]))
        self.wait()

        self.play( ModifyFormula(equality1,remove_items=[13]))
        self.wait()

        self.play(equality1[6:].animate.next_to(formulas[0], RIGHT).set_color(WHITE),
                  formulas[0].animate.set_color(WHITE),
                  FadeOut(equality1[0:6]))
        self.elements.add(equality1[6:])
        self.wait(2)

    def second(self):
        numbers = self.numbers
        formulas = self.formulas
        sum_square_prop = self.sum_square_prop
        product_power_prop = self.product_power_prop

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.wait(0.25)

        self.equality2 =equality2 = sum_square_prop.copy().next_to(formulas[1], 2 * DOWN)  # (a+b)^2=a^2+2ab+b^2
        equality2.align_to(formulas[1], LEFT)

        sum_square_prop_copy = sum_square_prop.copy()

        self.play(CounterclockwiseTransform(sum_square_prop_copy, equality2, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality2).remove(sum_square_prop_copy)
        self.fix_formula(equality2)
        self.wait(0)


        equality2[7:16].set_color(GREY)
        formulas[1][1:3].set_color(RED)
        self.wait(0.5)
        equality2[1].set_color(RED)
        self.wait()

        formulas[1][4:6].set_color(BLUE)
        self.wait(0.5)
        equality2[3].set_color(BLUE)
        self.wait()

        equality2[7:9].set_color(WHITE)

        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[7]], replace_items_strs=[['$($', '$2$', '$m$', '$)$']],replace_items_colors=[[RED,RED,RED,RED]]))
        self.wait(0)

        equality2[12:15].set_color(WHITE)
        self.play(ModifyFormula(equality2, replace_items=[[14]], replace_items_strs=[[r'$\cdot$', '$2$', '$m$']],replace_items_colors=[[WHITE,RED,RED]]))
        self.wait()

        self.play(ModifyFormula(equality2, replace_items=[[17]], replace_items_strs=[[r'$\cdot$', '$3$','$n$']],replace_items_colors=[[WHITE,BLUE,BLUE]]))

        self.wait()
        equality2[20].set_color(WHITE)
        equality2[22].set_color(WHITE)
        self.play(ModifyFormula(equality2, replace_items=[[21]], replace_items_strs=[['$($', '$3$', '$n$', '$)$']],replace_items_colors=[ [BLUE,BLUE,BLUE,BLUE]]))

        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[7, 8, 9, 10]], replace_items_strs=[['$4$', '$m$']]))
        self.wait(2)

        self.rearrange_formula(
            equality2, new_sequence=[*range(14), 15, 16, 14,*range(17,24)], move_down=[15, 16]
        )
        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[11, 12, 13, 14,15]], replace_items_strs=[['$12$']]))
        self.wait()

        product_power_prop2 = product_power_prop.copy()
        self.play(Write(product_power_prop2.next_to(equality2[16], DOWN * 1.2)))
        self.wait(2)
        self.play(ModifyFormula(product_power_prop2, replace_items=[[1], [6]], replace_items_strs=[['$3$'], ['$3$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[2], [9]], replace_items_strs=[['$n$'], ['$n$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[4], [7], [10]],replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop2, replace_items=[[6, 7, 8]], replace_items_strs=[['$9$']]))
        self.wait()
        self.play(ModifyFormula(equality2, replace_items=[[15,16, 17, 18]], replace_items_strs=[['$9$', '$n$']]))
        self.wait()
        self.play(FadeOut(product_power_prop2))
        self.wait()

        self.play(equality2[6:].animate.next_to(formulas[1], RIGHT).set_color(WHITE),
                  formulas[1].animate.set_color(WHITE),
                  FadeOut(equality2[0:6]))
        self.elements.add(equality2[6:])
        self.wait(2)


    def third(self):
        numbers = self.numbers
        formulas = self.formulas
        sum_square_prop = self.sum_square_prop
        product_power_prop = self.product_power_prop
        power_of_power_prop=self.power_of_power_prop

        self.play(FadeIn(formulas[2]), FadeIn(numbers[2]))
        self.wait(0.25)

        self.equality3 =equality3 = sum_square_prop.copy().next_to(formulas[2], 2 * DOWN)  # (a+b)^2=a^2+2ab+b^2
        equality3.align_to(formulas[2], LEFT)

        sum_square_prop_copy = sum_square_prop.copy()
        self.play(CounterclockwiseTransform(sum_square_prop_copy, equality3, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality3).remove(sum_square_prop_copy)
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

        self.wait()
        self.play(ModifyFormula(equality3, replace_items=[[7]], replace_items_strs=[['$($', '$x$', '$^5$', '$)$']],replace_items_colors=[[RED,RED,RED,RED]]))
        self.wait()

        equality3[12:15].set_color(WHITE)
        self.play(ModifyFormula(equality3, replace_items=[[14]], replace_items_strs=[[r'$\cdot$', '$x$', '$^5$']],replace_items_colors=[[WHITE,RED,RED]]))
        self.wait()

        self.play(ModifyFormula(equality3, replace_items=[[17]], replace_items_strs=[[r'$\cdot$', '$4$', '$y$']],replace_items_colors=[[WHITE,BLUE,BLUE]]))

        self.wait()
        equality3[20].set_color(WHITE)
        equality3[22].set_color(WHITE)
        self.play(ModifyFormula(equality3, replace_items=[[21]], replace_items_strs=[['$($', '$4$', '$y$', '$)$']],replace_items_colors=[[BLUE,BLUE,BLUE,BLUE]]))

        self.wait()
        power_of_power_prop1 = power_of_power_prop.copy()
        self.play(Write(power_of_power_prop1.next_to(equality3[8], DOWN * 1.2)))
        self.wait(2)

        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$x$'], ['$x$']]))
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[2], [7]], replace_items_strs=[['$^5$'], ['$^5$']]))
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[4], [9]],
                                replace_items_strs=[['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[7, 8, 9]], replace_items_strs=[['$^1$','$^0$']]))
        self.wait()
        self.play(ModifyFormula(equality3, replace_items=[[7, 8, 9, 10,11]], replace_items_strs=[['$x$', '$^1$','$^0$']]))
        self.wait()
        self.play(FadeOut(power_of_power_prop1))

        self.rearrange_formula(
            equality3, new_sequence=[*range(13), 16, 15, 13,14, *range(17, 24)], move_down=[15, 16]
        )
        self.wait()
        self.play(ModifyFormula(equality3, replace_items=[[11, 12, 13]], replace_items_strs=[['$8$']]))
        self.play(ModifyFormula(equality3, remove_items=[12]))
        self.wait()

        product_power_prop1 = product_power_prop.copy()
        self.play(Write(product_power_prop1.next_to(equality3[19], DOWN * 1.2)))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$4$'], ['$4$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[2], [9]], replace_items_strs=[['$y$'], ['$y$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[4], [7], [10]],
                                replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[6, 7, 8]], replace_items_strs=[['$16$']]))
        self.wait()
        self.play(
            ModifyFormula(equality3, replace_items=[[16, 17, 18, 19,20]], replace_items_strs=[['$1$', '$6$','$y$','$^2$']]))
        self.wait()
        self.play(FadeOut(product_power_prop1))
        self.wait()

        self.play(equality3[6:].animate.next_to(formulas[2], RIGHT).set_color(WHITE),
                  formulas[2].animate.set_color(WHITE),
                  FadeOut(equality3[0:6]))
        self.elements.add(equality3[6:])
        self.wait(2)

    def fourth(self):
        numbers = self.numbers
        formulas = self.formulas
        sum_square_prop = self.sum_square_prop
        product_power_prop = self.product_power_prop
        power_of_power_prop = self.power_of_power_prop

        self.play(FadeIn(formulas[3]), FadeIn(numbers[3]))
        self.wait(0.25)

        equality4 = sum_square_prop.copy().next_to(formulas[3], 2 * DOWN)  # (a+b)^2=a^2+2ab+b^2
        equality4.align_to(formulas[3], LEFT)

        sum_square_prop_copy = sum_square_prop.copy()
        self.play(CounterclockwiseTransform(sum_square_prop_copy, equality4, path_arc=-1 * PI), run_time=2)
        self.wait(0.25)
        self.add(equality4).remove(sum_square_prop_copy)
        self.wait(0.25)

        self.play(VGroup(self.elements,equality4).animate.shift(UP*1.4))
        self.wait()
        equality4[7:16].set_color(GREY)
        formulas[3][1:4].set_color(RED)
        self.wait(0.5)
        equality4[1].set_color(RED)
        self.wait()

        formulas[3][5:8].set_color(BLUE)
        self.wait(0.5)
        equality4[3].set_color(BLUE)
        self.wait()

        equality4[7:9].set_color(WHITE)

        self.fix_formula(equality4)

        self.wait()
        self.play(ModifyFormula(equality4, replace_items=[[7]], replace_items_strs=[['$($', '$2$','$a$', '$^2$', '$)$']],replace_items_colors=[[RED,RED,RED,RED,RED]]))
        self.wait()

        equality4[13:15].set_color(WHITE)
        self.play(ModifyFormula(equality4, replace_items=[[15]], replace_items_strs=[[r'$\cdot$', '$2$', '$a$','$^2$']],replace_items_colors=[[WHITE,RED,RED,RED]]))
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[19]], replace_items_strs=[[r'$\cdot$', '$3$', '$a$','$c$']],replace_items_colors=[[WHITE,BLUE,BLUE,BLUE]]))

        self.wait()

        equality4[23].set_color(WHITE)
        equality4[25].set_color(WHITE)
        self.play(ModifyFormula(equality4, replace_items=[[24]], replace_items_strs=[['$($', '$3$', '$a$','$c$', '$)$']],replace_items_colors=[[BLUE,BLUE,BLUE,BLUE,BLUE]]))

        self.wait()
        product_power_prop1 = product_power_prop.copy()

        self.play(Write(product_power_prop1.next_to(equality4[8], DOWN * 1.2)))
        self.fix_formula(product_power_prop1)
        self.wait(2)
        self.play(ModifyFormula(product_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$2$'], ['$2$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[2], [9]], replace_items_strs=[['$($','$a$','$^2$''$)$'], ['$($','$a$','$^2$''$)$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop1, replace_items=[[6], [9], [14]],replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[8,9,10]], replace_items_strs=[['$4$']]))
        self.wait()

        power_of_power_prop1 = power_of_power_prop.copy()
        self.play(Write(power_of_power_prop1.next_to(product_power_prop1[12], DOWN * 2.2)))
        self.wait(2)
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[1], [6]], replace_items_strs=[['$a$'], ['$a$']]))
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[2], [7]], replace_items_strs=[['$^2$'], ['$^2$']]))
        self.wait()
        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[4], [9]],replace_items_strs=[['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(power_of_power_prop1, replace_items=[[7, 8, 9]], replace_items_strs=[['$^4$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop1, replace_items=[[9,10,11,12,13]], replace_items_strs=[['$a$','$^4$']]))
        self.play(FadeOut(power_of_power_prop1))

        self.wait()
        self.play(ModifyFormula(equality4, replace_items=[[7, 8, 9, 10, 11, 12]],replace_items_strs=[['$4$', '$a$', '$^4$']]))
        self.wait()
        self.play(FadeOut(product_power_prop1))

        self.rearrange_formula(equality4, new_sequence=[*range(14), 16, 17, 14,15, *range(18, 27)], move_down=[16, 17])
        self.play(ModifyFormula(equality4, replace_items=[[11, 12, 13, 14, 15]], replace_items_strs=[['$1$', '$2$']]))
        self.wait()

        self.play(ModifyFormula(equality4, replace_items=[[14, 15]], replace_items_strs=[['$^3$']]))
        self.wait()

        self.wait()
        product_power_prop2 = product_power_prop.copy()
        self.play(Write(product_power_prop2.next_to(equality4[18], DOWN * 1.2)))
        self.fix_formula(product_power_prop2)

        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[1], [6]], replace_items_strs=[['$($', '$3$', '$a$''$)$'], ['$($', '$3$', '$a$''$)$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[4], [13]], replace_items_strs=[['$c$'], ['$c$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, replace_items=[[6], [11], [14]],replace_items_strs=[['$^2$'], ['$^2$'], ['$^2$']]))
        self.wait()

        self.play(ModifyFormula(product_power_prop2, replace_items=[[ 8,9, 10]], replace_items_strs=[['$9$','$a$']]))
        self.wait()
        self.play(ModifyFormula(product_power_prop2, remove_items=[11]))
        self.wait()
        self.wait()
        self.play(ModifyFormula(equality4, replace_items=[[17, 18, 19,20,21,22]], replace_items_strs=[['$9$','$a$','$^2$','$c$','$^2$']]))

        self.play(FadeOut(product_power_prop2))

        self.play(equality4[6:].animate.next_to(formulas[3], RIGHT).set_color(WHITE),
                  formulas[3].animate.set_color(WHITE),
                  FadeOut(equality4[0:6]))
        self.wait()

        self.play(VGroup(self.elements,equality4[6:]).animate.shift(DOWN * 1.4))
        self.wait()
