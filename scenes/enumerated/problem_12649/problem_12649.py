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

class Problem12649(FormulaModificationsScene):
    def construct(self):
        taskNumberString=r"\textrm{Խ.} 12649"
        taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait()
        
        self.formulas = formulas = VGroup(
            MathTex('2', 'x', r'\cdot', '(', '3', 'x', '^2', '+',  '1', ')', font_size=FONT_SIZE).next_to(2*UP + 6.5*LEFT, buff=0.2),
            MathTex(r'\mathsmaller{\frac{5}{3}}', 'x', r'\cdot', '(', '6', 'x', '^3', '+', '2', 'x', 'y', '^2', ')', font_size=FONT_SIZE).next_to(1*UP + 6.5*LEFT, buff=0.2),
            MathTex('a', '^2', 'b', '^3', r'\cdot', '(', '2', 'a', 'b', 'c', '+', 'b', '^2', ')', font_size=FONT_SIZE).next_to(6.5*LEFT, buff=0.2),
            MathTex('2', 'x', 'y', r'\cdot', r'\left(', '(', 'x', '^2', 'y', ')', '^3', '+', '3', 'x', 'y', r'\right)', font_size=FONT_SIZE).next_to(DOWN + 6.5*LEFT, buff=0.2))
        self.numbers = numbers = VGroup(*[MathTex(f'{i+1})', font_size=FONT_SIZE-7).next_to(formulas[i], LEFT, buff=0.3) for i in range(4)]).align_to(taskNumber, LEFT)
        
        self.play(AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5), run_time = 4)
        self.wait()

        #self.dp = distributive_property = MathTex('a', '\cdot', '(', 'b', '+', 'c', ')', '=', 'a', 'b', '+', 'a', 'c', font_size=FONT_SIZE)
        self.dp = distributive_property = Tex('$a$', '$\cdot$', '$($', '$b$', '$+$', '$c$', '$)$', '$=$', '$a$', '$b$', '$+$', '$a$', '$c$', font_size=FONT_SIZE)
        distributive_property.to_edge(RIGHT)
        uxx = SurroundingRectangle(distributive_property, color=GREEN)
        self.play(FadeIn(distributive_property), FadeIn(uxx))
        self.wait()

        self.first()

    def first(self):
        numbers = self.numbers
        formulas = self.formulas
        dp = self.dp

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        dist_prop1 = dp.copy().next_to(formulas[0], 2*DOWN)
        self.play(TransformFromCopy(dp, dist_prop1))
        self.wait()

        #arectangle = SurroundingRectangle(formulas[0][0:2], color=BLUE)
        #self.play(FadeIn(arectangle))
        formulas[0][0:2].set_color(RED)
        self.play(Indicate(formulas[0][0:2], color=RED))

        #slacks = VGroup(Arrow(arectangle, dist_prop1[0]), Arrow(arectangle, dist_prop1[8]), Arrow(arectangle, dist_prop1[11]))
        #self.play(Create(slacks))
        # arectangles = VGroup(SurroundingRectangle(dist_prop1[0]), SurroundingRectangle(dist_prop1[8]), SurroundingRectangle(dist_prop1[11]))
        # self.play(FadeIn(arectangles))
        dist_prop1[0].set_color(RED)
        dist_prop1[8].set_color(RED)
        dist_prop1[11].set_color(RED)
        self.play(*[Indicate(dist_prop1[i], color=RED) for i in [0,8,11]])
        
        # twox1 = Tex('$2x$', font_size=FONT_SIZE).move_to(dist_prop1[0])
        # twox2 = twox1.copy().move_to(dist_prop1[8])
        dist_prop2 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$b$', '$+$', '$c$', '$)$', '$=$', '$2$', '$x$', '$b$', '$+$', '$2$', '$x$', '$c$', font_size=FONT_SIZE)
        dist_prop2[0:2].set_color(RED)
        dist_prop2[9:11].set_color(RED)
        dist_prop2[13:15].set_color(RED)
        dist_prop2.next_to(dist_prop1, DOWN).align_to(dist_prop1, LEFT)
        self.play(TransformFromCopy(dist_prop1, dist_prop2))
        self.wait()

        # brectangle = SurroundingRectangle(formulas[0][4:7], color=ORANGE)
        # self.play(FadeIn(brectangle))
        formulas[0][4:7].set_color(BLUE)
        self.play(Indicate(formulas[0][4:7], color=BLUE))
        
        dist_prop2[4].set_color(BLUE)
        dist_prop2[11].set_color(BLUE)
        self.play(*[Indicate(dist_prop2[i], color=BLUE) for i in [4,11]])

        dist_prop3 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$3$', '$x$', '$^2$', '$+$', '$c$', '$)$', '$=$', '$2$', '$x$', '$3$', '$x$', '$^2$', '$+$', '$2$', '$x$', '$c$', font_size=FONT_SIZE)
        dist_prop3[0:2].set_color(RED)
        dist_prop3[11:13].set_color(RED)
        dist_prop3[17:19].set_color(RED)
        dist_prop3[4:7].set_color(BLUE)
        dist_prop3[13:16].set_color(BLUE)
        dist_prop3.next_to(dist_prop2, DOWN).align_to(dist_prop2, LEFT)
        self.play(TransformFromCopy(dist_prop2, dist_prop3))
        self.wait()
        
        formulas[0][8].set_color(ORANGE)
        self.play(Indicate(formulas[0][8], color=ORANGE))

        dist_prop3[8].set_color(ORANGE)
        dist_prop3[19].set_color(ORANGE)
        self.play(*[Indicate(dist_prop3[i], color=ORANGE) for i in [8,19]])
        self.wait()

        dist_prop4 = Tex('$2$', '$x$', r'$\cdot$', '$($', '$3$', '$x$', '$^2$', '$+$', '$1$', '$)$', '$=$', '$2$', '$x$', '$3$', '$x$', '$^2$', '$+$', '$2$', '$x$', '$1$', font_size=FONT_SIZE)
        dist_prop4.next_to(dist_prop3, DOWN).align_to(dist_prop3, LEFT)
        dist_prop4[0:2].set_color(RED)
        dist_prop4[11:13].set_color(RED)
        dist_prop4[17:19].set_color(RED)
        dist_prop4[4:7].set_color(BLUE)
        dist_prop4[13:16].set_color(BLUE)
        dist_prop4[8].set_color(ORANGE)
        dist_prop4[19].set_color(ORANGE)
        self.play(TransformFromCopy(dist_prop3, dist_prop4))
        self.wait()

        
        new_seq = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,13,15,16,17,18,19,21,20]
        self.add_items_in_formula(dist_prop4, after_items=[11,17], items_str_list=[r'\cdot', r'\cdot'])
        self.rearrange_formula(dist_prop4, new_seq, move_down=[14,21])
        #self.remove_items_from_formula(dist_prop4, items_indices=[12,13,19,20])
        #self.replace_items_in_formula(dist_prop4, items_indices=[11], items_str_list=['6'])
        self.play(ModifyFormula(dist_prop4, remove_items=[12,13,19,20], replace_items=[[11]], replace_items_strs=[['6']]))

        self.write_exponent_in_formula(dist_prop4, first_item_index=12, last_item_index=14, base='x', exponent=3)
        self.play(FadeOut(dist_prop1), FadeOut(dist_prop2), FadeOut(dist_prop3), FadeOut(dist_prop4[0:10]))
        self.play(dist_prop4[10:].animate.next_to(formulas[0], RIGHT))

        self.wait()