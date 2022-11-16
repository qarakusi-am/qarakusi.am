from manim import *

from VilageFormulaModifications import *
#sys.path.append('../../../')
#from lib.qarakusiscene import TaskNumberBox
#from armenian_text import taskNumberString
#from .text import taskNumberString

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r'\usepackage{armtex}')
class TaskNumberBox(VGroup):
    def __init__(self, text):
        text = Tex(text, tex_template=ARMTEX, font_size=35)
        box = Rectangle(width=text.width+.4, height=text.height+.4, stroke_width=1.5).to_edge(LEFT+UP, buff=.2)
        text.move_to(box.get_center())
        super().__init__(text, box)

FONT_SIZE=65
SCALE_FACTOR = 1.5
WIGGLE_SCALE_FACTOR = 1.25

class Problem12649(FormulaModificationsScene):
    def construct(self):
        # Խնդրի համարը
        taskNumberString=r"\textrm{Խ.} 12649"
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)
        
        # 4 վարժությունները
        self.formulas = formulas = VGroup(
            Tex('$2$', '$x$', r'$\cdot$', '$($', '$3$', '$x$', '$^2$', ' $+$ ',  '$1$', '$)$', font_size=FONT_SIZE).next_to(2*UP + 6.5*LEFT, buff=0.2),
            Tex(r'$\frac{5}{3}$', '$x$', r'$\cdot$', '$($', '$6$', '$x$', '$^3$', ' $+$ ', '$2$', '$x$', '$y$', '$^2$', '$)$', font_size=FONT_SIZE).next_to(1*UP + 6.5*LEFT, buff=0.2),
            Tex('$a$', '$^2$', '$b$', '$^3$', r'$\cdot$', '$($', '$2$', '$a$', '$b$', '$c$', ' $+$ ', '$b$', '$^2$', '$)$', font_size=FONT_SIZE).next_to(6.5*LEFT, buff=0.2),
            Tex('$2$', '$x$', '$y$', r'$\cdot$', r'$($', '$($', '$x$', '$^2$', '$y$', '$)$', '$^3$', ' $+$ ', '$3$', '$x$', '$y$', '$)$', font_size=FONT_SIZE).next_to(DOWN + 6.5*LEFT, buff=0.2))
        self.numbers = numbers = VGroup(*[MathTex(f'{i+1})', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3) for i in range(4)]).align_to(taskNumber, LEFT)
        
        self.play(AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5), run_time = 4)
        self.wait(0.25)

        # բաշխական օրենքը՝ distributive property
        self.dist_prop = dist_prop = Tex('$a$', '$\cdot$', '$($', '$b$', ' $+$ ', '$c$', '$)$', ' $=$ ', '$a$', '$\cdot$', '$b$', ' $+$ ', '$a$', '$\cdot$', '$c$', font_size=FONT_SIZE)
        dist_prop.to_corner(UR)
        self.rectangle = rectangle = SurroundingRectangle(dist_prop, color=GREEN)
        self.play(FadeIn(dist_prop), FadeIn(rectangle))
        self.wait(0.25)

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        self.wait(0.25)

        # Հերթով բոլոր վարժությունները՝
        # exp-ը զուտ փորձի համար է։

        self.first()
        self.second()
        #self.exp()
        #self.third()
        self.third_real()
        self.fourth()

    def first(self):
        formulas = self.formulas
        dist_prop = self.dist_prop

        # առաջին բանաձևը
        dist_prop1 = dist_prop.copy().next_to(formulas[0], 2*DOWN).align_to(formulas[0], LEFT)
        self.play(TransformFromCopy(dist_prop, dist_prop1))
        self.wait(0.25)

        # ներկում ենք a-երը
        formulas[0][0:2].set_color(RED)
        self.play(Indicate(formulas[0][0:2], color=RED, scale_factor=SCALE_FACTOR))

        dist_prop1[0].set_color(RED)
        dist_prop1[8].set_color(RED)
        dist_prop1[12].set_color(RED)
        self.play(*[Indicate(dist_prop1[i], color=RED, scale_factor=SCALE_FACTOR) for i in [0,8,12]])

        # երկրորդ բանաձևը
        dist_prop2 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$b$', ' $+$ ', '$c$', '$)$', ' $=$ ', '$2$', '$x$', r'$\cdot$', '$b$', ' $+$ ', '$2$', '$x$',r'$\cdot$', '$c$', font_size=FONT_SIZE)
        dist_prop2.next_to(dist_prop1, DOWN).align_to(dist_prop1, LEFT)
        dist_prop2[0:2].set_color(RED)
        dist_prop2[9:11].set_color(RED)
        dist_prop2[14:16].set_color(RED)
        self.play(TransformFromCopy(dist_prop1, dist_prop2))
        self.wait(0.25)

        # ներկում ենք b-երը
        formulas[0][4:7].set_color(BLUE)
        self.play(Indicate(formulas[0][4:7], color=BLUE, scale_factor=SCALE_FACTOR))
        
        dist_prop2[4].set_color(BLUE)
        dist_prop2[12].set_color(BLUE)
        self.play(*[Indicate(dist_prop2[i], color=BLUE, scale_factor=SCALE_FACTOR) for i in [4,12]])

        # երրորդ բանաձևը
        dist_prop3 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$3$', '$x$', '$^2$', ' $+$ ', '$c$', '$)$', ' $=$ ', '$2$', '$x$', r'$\cdot$', '$3$', '$x$', '$^2$', ' $+$ ', '$2$', '$x$',r'$\cdot$', '$c$', font_size=FONT_SIZE)
        dist_prop3.next_to(dist_prop2, DOWN).align_to(dist_prop2, LEFT)
        dist_prop3[0:2].set_color(RED)
        dist_prop3[11:13].set_color(RED)
        dist_prop3[18:20].set_color(RED)
        dist_prop3[4:7].set_color(BLUE)
        dist_prop3[14:17].set_color(BLUE)
        self.play(TransformFromCopy(dist_prop2, dist_prop3))
        self.wait(0.25)

        # ներկում ենք c-երը
        formulas[0][8].set_color(ORANGE)
        self.play(Indicate(formulas[0][8], color=ORANGE, scale_factor=SCALE_FACTOR))

        dist_prop3[8].set_color(ORANGE)
        dist_prop3[21].set_color(ORANGE)
        self.play(*[Indicate(dist_prop3[i], color=ORANGE, scale_factor=SCALE_FACTOR) for i in [8,21]])
        self.wait(0.25)

        # չորրորդ բանաձևը
        dist_prop4 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$3$', '$x$', '$^2$', ' $+$ ', '$1$', '$)$', ' $=$ ', '$2$', '$x$', r'$\cdot$', '$3$', '$x$', '$^2$', ' $+$ ', '$2$', '$x$',r'$\cdot$', '$1$', font_size=FONT_SIZE)
        dist_prop4.next_to(dist_prop3, DOWN).align_to(dist_prop3, LEFT)
        dist_prop4[0:2].set_color(RED)
        dist_prop4[11:13].set_color(RED)
        dist_prop4[18:20].set_color(RED)
        dist_prop4[4:7].set_color(BLUE)
        dist_prop4[14:17].set_color(BLUE)
        dist_prop4[8].set_color(ORANGE)
        dist_prop4[21].set_color(ORANGE)
        self.play(TransformFromCopy(dist_prop3, dist_prop4))
        self.wait(0.25)
        
        # ձևափոխությունները սկսվեցին
        
        # առաջին գումարելի
        self.play(Wiggle(dist_prop4[11:17], scale_factor=WIGGLE_SCALE_FACTOR))
        new_seq = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,12,15,16,17,18,19,20,21]
        self.rearrange_formula(dist_prop4, new_seq, move_down=[13,14])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop4, remove_items=[12,13], replace_items=[[11]], replace_items_strs=[['6']]))
        self.wait(0.25)
        self.write_exponent_in_formula(dist_prop4, first_item_index=12, last_item_index=14, base='x', exponent=3)
        self.wait(0.25)

        # երկրորդ գումարելի
        self.play(Wiggle(dist_prop4[15:], scale_factor=WIGGLE_SCALE_FACTOR))
        new_seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,16]
        self.rearrange_formula(dist_prop4, new_seq, move_down=[17,18])
        self.wait(0.25)
        
        self.play(ModifyFormula(dist_prop4, remove_items=[16,17]))
        self.wait(0.25)
        
        self.play(FadeOut(dist_prop1), FadeOut(dist_prop2), FadeOut(dist_prop3), FadeOut(dist_prop4[0:10]))
        self.wait(0.25)
        self.play(dist_prop4[10:].animate.next_to(formulas[0], RIGHT).set_color(WHITE), formulas[0].animate.set_color(WHITE))
        self.wait(0.25)

    def second(self):
        numbers = self.numbers
        formulas = self.formulas
        dist_prop = self.dist_prop
        rectangle = self.rectangle

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.wait(0.25)

        dist_prop1 = dist_prop.copy().next_to(formulas[1], 2*DOWN)
        dist_prop1.align_to(formulas[1], LEFT)

        dist_prop_copy = dist_prop.copy()
        self.play(CounterclockwiseTransform(dist_prop_copy, dist_prop1, path_arc=-1*PI), run_time=2)
        self.wait(0.25)
        self.add(dist_prop1).remove(dist_prop_copy)
        

        self.fix_formula(dist_prop1)

        # a
        formulas[1][0:2].set_color(RED)
        self.play(Indicate(formulas[1][0:2], color=RED, scale_factor=SCALE_FACTOR))

        self.wait(0.25)
        dist_prop1[0].set_color(RED)
        dist_prop1[8].set_color(RED)
        dist_prop1[12].set_color(RED)
        self.play(*[Indicate(dist_prop1[i], color=RED, scale_factor=SCALE_FACTOR) for i in [0,8,12]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[0], [8], [12]], replace_items_strs=[[r'$\frac{5}{3}$', '$x$'],[r'$\frac{5}{3}$', '$x$'],[r'$\frac{5}{3}$', '$x$']]))
        self.wait(0.25)

        # b
        formulas[1][4:7].set_color(BLUE)
        self.play(Indicate(formulas[1][4:7], color=BLUE, scale_factor=SCALE_FACTOR))
        self.wait(0.25)
        dist_prop1[4].set_color(BLUE)
        dist_prop1[12].set_color(BLUE)
        self.play(*[Indicate(dist_prop1[i], color=BLUE, scale_factor=SCALE_FACTOR) for i in [4,12]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[4], [12]], replace_items_strs=[['$6$', '$x$', '$^3$'],['$6$', '$x$', '$^3$']]))
        self.wait(0.25)

        # c
        formulas[1][8:12].set_color(ORANGE)
        self.play(Indicate(formulas[1][8:12], color=ORANGE, scale_factor=SCALE_FACTOR))
        self.wait(0.25)
        dist_prop1[8].set_color(ORANGE)
        dist_prop1[21].set_color(ORANGE)
        self.play(*[Indicate(dist_prop1[i], color=ORANGE, scale_factor=SCALE_FACTOR) for i in [8,21]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[8], [21]], replace_items_strs=[['$2$', '$x$', '$y$', '$^2$'],['$2$', '$x$', '$y$', '$^2$']]))
        self.wait(0.25)
        
        # 13 ինդեքսը =ն է
        # առաջին գումարելի
        self.play(Wiggle(dist_prop1[14:20], scale_value=WIGGLE_SCALE_FACTOR))
        seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,15,18,19,20,21,22,23,24,25,26,27]
        self.rearrange_formula(dist_prop1, new_sequence=seq, move_down=[16,17])
        self.wait(0.25)

        self.play(ModifyFormula(dist_prop1, replace_items=[[14]], replace_items_strs=[['10']], remove_items=[15,16]))
        self.wait(0.25)

        self.write_exponent_in_formula(dist_prop1, first_item_index=15, last_item_index=17, base='x', exponent='4')
        self.wait(0.25)

        # երկրորդ գումարելի
        self.play(Wiggle(dist_prop1[18:], scale_value=WIGGLE_SCALE_FACTOR))
        seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,19,22, 23,24]
        self.rearrange_formula(dist_prop1, new_sequence=seq, move_down=[20,21])
        self.wait(0.25)
        
        self.play(ModifyFormula(dist_prop1, replace_items=[[18]], replace_items_strs=[[r'$\frac{10}{3}$']], remove_items=[19,20]))
        self.wait(0.25)
        

        self.write_exponent_in_formula(dist_prop1, first_item_index=19, last_item_index=20, base='x', exponent='2')
        self.wait(0.25)

        self.play(FadeOut(dist_prop1[0:13]))
        self.wait(0.25)
        self.play(dist_prop1[13:].animate.next_to(formulas[1], RIGHT).set_color(WHITE), formulas[1].animate.set_color(WHITE))
        self.wait(0.25)

    def exp(self):
        numbers = self.numbers
        formulas = self.formulas
        dist_prop = self.dist_prop
        rectangle = self.rectangle

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.wait(0.25)

        dist_prop1 = dist_prop.copy().next_to(formulas[1], 2*DOWN)
        dist_prop1.align_to(formulas[1], LEFT)

        # dist_propc = dist_prop.copy().set_opacity(0.5)
        # self.add(dist_propc)
        # self.play(Unwrite(dist_prop))
        # self.play(GrowFromCenter(dist_prop1))
        # self.wait(0.25)

        # Smbat
        # dist_propc = dist_prop.copy().set_opacity(0.5)
        # self.add(dist_propc)
        # self.play(dist_prop.animate.scale(0))
        # self.play(GrowFromCenter(dist_prop1))
        # self.wait(0.25)

        # Narek ու սև խոռոչ
        # dist_propc = dist_prop.copy().set_opacity(0.5)
        # self.add(dist_propc)
        # blackhole1 = ImageMobject('black_hole.jpg').scale(0.4).set_z_index(-1).next_to(rectangle, DOWN)
        # self.play(FadeIn(blackhole1))
        # dot1 = Dot(blackhole1.get_center(), color=WHITE).set_z_index(-0.5)
        # blackhole2 = blackhole1.copy()
        # dot2 = dot1.copy()
        # self.play(TransformFromCopy(dist_prop, dot1), run_time=0.5)
        # second = Group(blackhole2,dot2).next_to(dist_prop1, DOWN)
        # self.play(FadeIn(blackhole2), run_time=0.5)
        # self.play(FadeOut(dot1), FadeIn(dot2), run_time=0.5)
        # self.play(Transform(dot2, dist_prop1), run_time=0.5)
        # #self.play(GrowFromCenter(dist_prop1))
        # self.wait(0.25)

        # Gor
        self.wait()
        self.play(CounterclockwiseTransform(dist_prop.copy(), dist_prop1, path_arc=-1*PI))
        self.wait()

        self.play(ShowPassingFlash(
                rectangle.copy().set_color(BLUE),
                run_time=2,
            ))
        self.play(GrowFromCenter(dist_prop1))
        self.play(ShowPassingFlash(dist_prop1.copy().set_color(BLUE)))
        self.wait()

    def third(self):
        numbers = self.numbers
        formulas = self.formulas
        dist_prop = self.dist_prop

        self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.play(FadeIn(formulas[2]), FadeIn(numbers[2]))
        
        self.wait(0.25)

        dist_prop = dist_prop.copy().next_to(formulas[2], 2*DOWN)
        dist_prop.align_to(formulas[2], LEFT)
        dist_prop1 = dist_prop.copy()
        self.play(CounterclockwiseTransform(dist_prop1, dist_prop, path_arc=-1*PI))
        self.wait()

        self.fix_formula(dist_prop1)
        # a
        formulas[2][0:4].set_color(RED)
        self.play(Indicate(formulas[2][0:4], color=RED, scale_factor=SCALE_FACTOR))
        self.wait(0.25)

        dist_prop1[0].set_color(RED)
        dist_prop1[8].set_color(RED)
        dist_prop1[12].set_color(RED)
        self.play(*[Indicate(dist_prop1[i], color=RED, scale_factor=SCALE_FACTOR) for i in [0,8,12]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[0], [8], [12]], replace_items_strs=[['$a$', '$^2$', '$b$', '$^3$']]*3))
        self.wait(0.25)

        # b
        formulas[2][6:10].set_color(BLUE)
        self.play(Indicate(formulas[2][6:10], color=BLUE, scale_factor=SCALE_FACTOR))
        self.wait(0.25)
        dist_prop1[6].set_color(BLUE)
        dist_prop1[16].set_color(BLUE)
        self.play(*[Indicate(dist_prop1[i], color=BLUE, scale_factor=SCALE_FACTOR) for i in [6,16]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[6], [16]], replace_items_strs=[['$a$', '$b$', '$c$'],['$a$', '$b$', '$c$']]))
        self.wait(0.25)

        # # c
        formulas[2][11:13].set_color(ORANGE)
        self.play(Indicate(formulas[2][11:13], color=ORANGE, scale_factor=SCALE_FACTOR))
        self.wait(0.25)
        dist_prop1[10].set_color(ORANGE)
        dist_prop1[27].set_color(ORANGE)
        self.play(*[Indicate(dist_prop1[i], color=ORANGE, scale_factor=SCALE_FACTOR) for i in [10,27]])
        self.wait(0.25)
        self.play(ModifyFormula(dist_prop1, replace_items=[[10], [27]], replace_items_strs=[['$b$', '$^2$'],['$b$', '$^2$']]))
        self.wait(0.25)

        # = 13-na

        self.play(ModifyFormula(dist_prop1, remove_items=[18,27]))
        self.wait(0.25)
        
        self.rearrange_formula(dist_prop1, new_sequence=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,16,17,19,20,21,22,23,24,25,26,27], move_down=[18])
        self.wait(0.25)

        self.write_exponent_in_formula(dist_prop1, first_item_index=14, last_item_index=16, base='a', exponent='3')
        self.wait(0.25)
        self.write_exponent_in_formula(dist_prop1, first_item_index=16, last_item_index=18, base='b', exponent='4')
        self.wait(0.25)
        self.write_exponent_in_formula(dist_prop1, first_item_index=22, last_item_index=25, base='b', exponent='5')
        self.wait(0.25)

        self.play(FadeOut(dist_prop1[0:13]))
        self.wait(0.25)
        self.play(dist_prop1[13:].animate.next_to(formulas[2], RIGHT).set_color(WHITE), formulas[2].animate.set_color(WHITE))
        self.wait(0.25)

    def fourth(self):
        WIGGLE_SCALE_FACTOR = 1.25
        numbers = self.numbers
        formulas = self.formulas

        self.play(FadeIn(formulas[3]), FadeIn(numbers[3]))
        self.wait(0.25)

        self.fix_formula(formulas[3])

        self.play(Indicate(formulas[3][5:11], scale_factor=SCALE_FACTOR))

        miandam = Tex('$($', '$x$', '$^2$', '$y$', '$)$', '$^3$', ' $=$ ', '$($', '$x$','$^2$', '$)$', '$^3$', '$y$', '$^3$', ' $=$ ', '$x$', '$^6$', '$y$', '$^3$', font_size=FONT_SIZE)
        miandam.next_to(formulas[3], 3*DOWN).align_to(formulas[3], LEFT)
        # miandam[8:10].set_color(RED)
        # miandam[11].set_color(ORANGE)
        # miandam[13].set_color(ORANGE)
        # miandam[12].set_color(BLUE)
        self.play(ReplacementTransform(formulas[3][5:11].copy(), miandam[:6]))

        #self.play(formulas[3][:5].animate.set_opacity(0.25), formulas[3][11:].animate.set_opacity(0.25))
        
        # 2nd միանդամ rule
        second_rule = Tex('$($', '$a$', r'$\cdot$', '$b$', '$)$', '$^n$', ' $=$ ', '$a$', '$^n$', r'$\cdot$', '$b$', '$^n$', font_size=FONT_SIZE)
        # second_rule[1].set_color(RED)
        # second_rule[7].set_color(RED)
        # second_rule[3].set_color(BLUE)
        # second_rule[10].set_color(BLUE)
        # second_rule[5].set_color(ORANGE)
        # second_rule[8].set_color(ORANGE)
        # second_rule[11].set_color(ORANGE)
        second_rule.next_to(formulas[3], 3*DOWN)
        second_rule.to_edge(RIGHT)
        rect2 = SurroundingRectangle(second_rule, color=GREEN)
        self.play(Create(rect2), Write(second_rule))
        self.wait(0.25)

        # self.play(miandam[1:3].animate.set_color(RED), miandam[3].animate.set_color(BLUE), miandam[5].animate.set_color(ORANGE))

        # 3rd միանդամ rule
        third_rule = Tex('$($', '$a$', '$^m$', '$)$', '$^n$', ' $=$ ', '$a$', '$^m$', r'$^\cdot$', '$^n$', font_size=FONT_SIZE)
        # third_rule[1].set_color(RED)
        # third_rule[2].set_color(PURE_BLUE)
        # third_rule[4].set_color(ORANGE)
        # third_rule[6].set_color(RED)
        # third_rule[7].set_color(PURE_BLUE)
        # third_rule[9].set_color(ORANGE)
        
        #third_rule.next_to(second_rule, 2*RIGHT)
        third_rule.move_to(second_rule)
        rect3 = SurroundingRectangle(third_rule, color=GREEN)
        #self.play(Create(rect3), Write(third_rule))
        #self.wait(0.25)

        # օգտվենք 2-րդից
        self.play(Write(miandam[6:14]))

        # self.play(ApplyWave(VGroup(rect2, second_rule)))
        # self.wait(0.25)

        #self.play(formulas[3][10].animate.shift(0.5*UP))
        # self.play(
        #     #FadeOut(formulas[3][5], rate_func=there_and_back),
        #     ModifyFormula(formulas[3], remove_items=[9,10], add_after_items=[7,8], add_items_strs=[['$)$', r'$^3$'], ['$^3$']], add_lag_ratio=0.3),
        #     )
        # self.wait(0.25)

        self.play(FadeOut(VGroup(rect2, second_rule)))
        self.play(
            Indicate(miandam[7:12], scale_factor=SCALE_FACTOR),
            miandam[12:14].animate.set_color(WHITE),
            miandam[:6].animate.set_color(WHITE)
            )
        self.wait(0.25)
        self.play(Write(third_rule), Create(rect3))
        self.wait(0.25)
        #self.play(miandam[9].animate.set_color(PURE_BLUE))
        self.wait(0.25)
        #miandam[15].set_color(RED)
        #miandam[16].set_color_by_gradient([PURE_BLUE, ORANGE])
        self.play(Write(miandam[14:]))
        self.wait(0.25)

        #self.play(VGroup(rect3, third_rule).animate.move_to(rect2))
        self.wait(0.25)
        # օգտվենք 3-րդից
        # self.play(ApplyWave(VGroup(rect3, third_rule)))
        self.wait(0.25)
        self.play(
            ModifyFormula(formulas[3], remove_items=[5,9], replace_items=[[7]], replace_items_strs=[['$^6$']]), 
            )
        self.wait(0.25)

        #self.play(Uncreate(VGroup(rect2, second_rule)), Uncreate(VGroup(rect3, third_rule)))
        #self.play(formulas[3][:5].animate.set_opacity(1), formulas[3][11:].animate.set_opacity(1))
        self.play(Uncreate(VGroup(rect3, third_rule)), FadeOut(miandam))     
        self.wait(0.25)

        ans = Tex(' $=$ ', '$2$', '$x$', '$y$', r'$\cdot$', '$x$', '$^6$', '$y$', '$^3$', ' $+$ ', '$2$', '$x$', '$y$', r'$\cdot$', '$3$', '$x$', '$y$', font_size=FONT_SIZE)
        ans.next_to(formulas[3], RIGHT)

        self.play(FadeIn(ans[0]))

        # տանում ենք a-ն ու b-ն
        a_copy1 = formulas[3][0:3].copy()
        b_copy = formulas[3][5:9].copy()
        self.play(Wiggle(formulas[3][5:9], scale_value=WIGGLE_SCALE_FACTOR), Wiggle(formulas[3][0:3], scale_value=WIGGLE_SCALE_FACTOR))
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(a_copy1, ans[1:4], path_arc=PI/2),
                FadeIn(ans[4]),
                lag_ratio=0.5
                ),
            CounterclockwiseTransform(b_copy, ans[5:9], path_arc=PI/2)
            )
        self.add(ans[1:4]).remove(a_copy1)
        self.add(ans[5:9]).remove(b_copy)
        self.wait(0.25)

        self.play(FadeIn(ans[9]))
        # տանում ենք a-ն ու c-ն
        a_copy2 = formulas[3][0:3].copy()
        c_copy = formulas[3][10:13].copy()
        self.play(Wiggle(formulas[3][10:13], scale_value=WIGGLE_SCALE_FACTOR), Wiggle(formulas[3][0:3], scale_value=WIGGLE_SCALE_FACTOR))
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(a_copy2, ans[10:13], path_arc=PI/2),
                FadeIn(ans[13]), 
                lag_ratio=0.5
                ),
            CounterclockwiseTransform(c_copy, ans[14:], path_arc=PI/2)
            )
        self.add(ans[10:13]).remove(a_copy2)
        self.add(ans[14:]).remove(c_copy)
        self.wait(0.25)

        # = նշանը 14-րդ ինդեքսում ա
        self.fix_formula(ans)
        self.play(Wiggle(ans[1:9], scale_value=WIGGLE_SCALE_FACTOR))
        seq = [14,15,16,19,20,17,18,21,22,23,24,25,26,27,28,29,30]
        self.rearrange_formula(ans, new_sequence=[x-14 for x in seq], move_down=[5,6])
        self.wait(0.25)
        self.write_exponent_in_formula(ans,first_item_index=2, last_item_index=4, base='x', exponent='7')
        self.wait(0.25)
        self.write_exponent_in_formula(ans,first_item_index=4, last_item_index=7, base='y', exponent='4')
        self.wait(0.25)
        # + նշանը 23-րդ ինդեքսում ա
        self.play(Wiggle(ans[7:], scale_value=WIGGLE_SCALE_FACTOR))
        seq = [14,15,16,17,18,19,20,21,24,25,22,23,26,27]
        self.rearrange_formula(ans, new_sequence=[x-14 for x in seq], move_down=[10,11])
        self.wait(0.25)
        seq = [14,15,16,17,18,19,20,21,22,23,24,26,25,27]
        self.rearrange_formula(ans, new_sequence=[x-14 for x in seq], move_down=[12])
        self.wait(0.25)

        self.play(ModifyFormula(ans, remove_items=[8,9], replace_items=[[7]], replace_items_strs=[['$6$']]))

        self.write_exponent_in_formula(ans,first_item_index=8, last_item_index=9, base='x', exponent='2')
        self.wait(0.25)
        self.write_exponent_in_formula(ans,first_item_index=10, last_item_index=11, base='y', exponent='2')
        self.wait(0.25)


    def third_real(self):
        numbers = self.numbers
        formulas = self.formulas
        dist_prop = self.dist_prop

        #self.play(FadeIn(formulas[1]), FadeIn(numbers[1]))
        self.play(FadeIn(formulas[2]), FadeIn(numbers[2]))
        
        self.wait(0.25)

        self.fix_formula(dist_prop)

        ans = Tex(' $=$ ', '$a$', '$^2$', '$b$', '$^3$', r'$\cdot$', '$2$', '$a$', '$b$', '$c$', ' $+$ ', '$a$', '$^2$', '$b$', '$^3$', r'$\cdot$', '$b$', '$^2$', font_size=FONT_SIZE)
        ans.next_to(formulas[2], RIGHT)

        #self.fix_formula(ans)

        self.play(FadeIn(ans[0]))

        # տանում ենք a-ն ու b-ն
        a_copy1 = formulas[2][0:4].copy()
        b_copy = formulas[2][6:10].copy()
        self.play(Wiggle(formulas[2][6:10], scale_value=WIGGLE_SCALE_FACTOR), Wiggle(formulas[2][0:4], scale_value=WIGGLE_SCALE_FACTOR))
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(a_copy1, ans[1:5], path_arc=PI/2),
                FadeIn(ans[5]),
                lag_ratio=0.5
                ),
            CounterclockwiseTransform(b_copy, ans[6:10], path_arc=PI/2)
            )
        self.add(ans[1:5]).remove(a_copy1)
        self.add(ans[6:10]).remove(b_copy)
        self.wait(0.25)

        self.play(FadeIn(ans[10]))
        # տանում ենք a-ն ու c-ն
        a_copy2 = formulas[2][0:4].copy()
        c_copy = formulas[2][11:13].copy()
        self.play(Wiggle(formulas[2][11:13], scale_value=WIGGLE_SCALE_FACTOR), Wiggle(formulas[2][0:4], scale_value=WIGGLE_SCALE_FACTOR))
        self.play(
            AnimationGroup(
                CounterclockwiseTransform(a_copy2, ans[11:15], path_arc=PI/2),
                FadeIn(ans[15]), 
                lag_ratio=0.5
                ),
            CounterclockwiseTransform(c_copy, ans[16:], path_arc=PI/2)
            )
        self.add(ans[11:15]).remove(a_copy2)
        self.add(ans[16:]).remove(c_copy)
        self.wait(0.25)

        self.play(Wiggle(ans[1:10], scale_value=WIGGLE_SCALE_FACTOR))
        self.fix_formula(ans)
        self.rearrange_formula(ans, new_sequence=[0,6,7,1,2,3,4,5,8,9,10,11,12,13,14,15,16,17], move_down=[6,7])
        self.wait(0.25)

        self.write_exponent_in_formula(ans, first_item_index=2, last_item_index=4, base='a', exponent='3')
        self.wait(0.25)

        self.write_exponent_in_formula(ans, first_item_index=4, last_item_index=7, base='b', exponent='4')
        self.wait(0.25)

        self.play(Wiggle(ans[8:], scale_value=WIGGLE_SCALE_FACTOR))

        self.write_exponent_in_formula(ans, first_item_index=10, last_item_index=14, base='b', exponent='5')
        self.wait(0.25)