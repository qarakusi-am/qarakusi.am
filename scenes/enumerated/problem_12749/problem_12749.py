from manim import SurroundingRectangle
from manim import Write, FadeIn, FadeOut, AnimationGroup
from manim import ReplacementTransform, TransformFromCopy
from manim import YELLOW, RED, BLUE, WHITE
from manim import RIGHT, LEFT, UP, DOWN
from manim import Tex, MathTex, VGroup
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from qarakusiscene import TaskNumberBox
from .text import taskNumberString
from segment import ConnectionLine

FONT_SIZE = 60

class Problem12749(FormulaModificationsScene):
    def construct(self):
        self.taskNumber = taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)

        self.formulas = formulas = VGroup(
            Tex('$a$', '$^2$', ' $+$ ', '$1$', '$0$', '$a$', '$+$', ' $2$', '$1$', ' $=$ ',
                font_size = FONT_SIZE).next_to(2 * UP + 6.5 * LEFT, buff = 0.2),  # a^2+10a+21
            Tex('$x$', '$^2$', ' $+$ ', '$6$', '$x$', ' $-$ ', '$1$', '$6$', ' $=$ ', font_size = FONT_SIZE).next_to(
                1 * UP + 6.5 * LEFT, buff = 0.2),  # x^2+6x-16
            Tex('$z$', '$^2$', ' $-$ ', '$8$', '$z$', ' $+$ ', '$7$', '$=$ ', font_size = FONT_SIZE).next_to(6.5 * LEFT,
                                                                                                           buff = 0.2),
            # z^2-8z+7
            Tex('$4$', '$a$', '$^2$', ' $+$ ', '$1$', '$2$', '$a$', ' $+$ ', '$5$', ' $=$ ',
                font_size = FONT_SIZE).next_to(DOWN + 6.5 * LEFT, buff = 0.2))  # 4a^2+12a+5

        self.numbers = numbers = VGroup(
            *[MathTex(f'{i + 1})', font_size = FONT_SIZE - 7).next_to(formulas[i], LEFT, buff = 0.3) for i in
              range(4)]).align_to(taskNumber, LEFT)

        self.solutions = VGroup()

        for formula in formulas:
            formula[-1].set_opacity(0)

        self.play(
            AnimationGroup(*[AnimationGroup(Write(formulas[i]), Write(numbers[i])) for i in range(4)], lag_ratio=0.5),
            run_time=4
        )
        self.wait(0.25)

        self.sum_square_prop = Tex(
            '$($', '$a$', ' $+$ ', '$b$', '$)$', '$^2$', ' $=$ ',
            '$a$', '$^2$', ' $+$ ', '$2$', '$\cdot$', '$a$', '$\cdot$', '$b$', ' $+$ ', '$b$', '$^2$',
            font_size = FONT_SIZE)

        self.difference_of_squares_prop = Tex(
            '$a$', '$^2$', ' $-$ ', '$b$', '$^2$', ' $=$ ',
            '$($', '$a$', ' $-$ ', '$b$', '$)$', '$\cdot$', '$($', '$a$', ' $+$ ', '$b$', '$)$',
            font_size = FONT_SIZE)

        self.play(FadeOut(formulas[1:]), FadeOut(numbers[1:]))
        self.wait(0.25)

        self.first()
        self.second()
        self.third()
        self.fourth()

    def first(self):
        formulas = self.formulas

        # write sum square property
        square_prop = self.sum_square_prop.copy().move_to(formulas[0]).align_to(formulas[0], LEFT).shift(DOWN * 2)
        self.play(Write(square_prop))
        self.wait()

        # copy a^2+10a part and move down
        abbr_formula = Tex('$a$', '$^2$', ' $+$ ', '$1$', '$0$', '$a$', font_size = FONT_SIZE)
        abbr_formula.move_to(formulas[0]).align_to(formulas[0], LEFT)
        self.play(abbr_formula.animate.shift(DOWN))
        self.wait()

        self.fix_formula(abbr_formula)
        self.play(
            ModifyFormula(
                abbr_formula,
                replace_items = [[3, 4, 5]], replace_items_strs = [['$2$', '$\cdot$', '$a$', '$\cdot$' '$5$']]
            )
        )
        self.wait()

        self.play(AnimationGroup(
            square_prop[1].animate.set_color(RED),
            square_prop[7].animate.set_color(RED),
            square_prop[12].animate.set_color(RED),
            abbr_formula[0].animate.set_color(RED),
            abbr_formula[5].animate.set_color(RED)))
        self.wait()

        self.play(AnimationGroup(
            square_prop[3].animate.set_color(BLUE),
            square_prop[14].animate.set_color(BLUE),
            square_prop[-2].animate.set_color(BLUE),
            abbr_formula[-1].animate.set_color(BLUE)))

        self.wait()
        # change letters in sum square property to letters from the equation
        self.fix_formula(square_prop)
        self.play(
            ModifyFormula(square_prop, replace_items = [[3], [14], [16]],
                          replace_items_strs = [['$5$'], ['$5$'], ['$5$']])
        )
        self.wait()

        helper_equations = VGroup(
            Tex(' $+$ ', '$5$', '$^2$', font_size = FONT_SIZE).next_to(abbr_formula[-1], RIGHT).align_to(abbr_formula,
                                                                                                       DOWN),
            Tex(' $-$ ', '$5$', '$^2$', ' $+$ ', '$2$', '$1$', ' $=$ ', font_size = FONT_SIZE),
            Tex(' $=$ ', '$($', '$a$', ' $+$ ', '$5$', '$)$', '$^2$', font_size = FONT_SIZE).move_to(formulas[0],
                                                                                                   LEFT).shift(DOWN),
            Tex(' $-$ ', '$4$', font_size = FONT_SIZE)
        )

        self.play(TransformFromCopy(square_prop[15:], helper_equations[0]))
        self.wait()

        # add -5^2 to abbreviate form and move to equality sign
        formulas[0][-1].set_opacity(1)
        self.play(Write(formulas[0][-1]),
                  VGroup(abbr_formula, helper_equations[0]).animate.next_to(formulas[0][-1], RIGHT).align_to(
                      formulas[0], DOWN))

        helper_equations[1].next_to(helper_equations[0][-1], RIGHT).align_to(helper_equations[0], UP)
        helper_equations[1][3:].set_opacity(0)

        self.play(Write(helper_equations[1]))
        self.wait()

        # create surrounding rectangle for 5^2-5^2
        surrounding_rectangle1 = SurroundingRectangle(VGroup(helper_equations[0][1:], helper_equations[1][0:3]),
                                                      color = YELLOW, buff = 0.2)
        self.play(Write(surrounding_rectangle1))
        self.wait()

        helper_equations[1][3:].set_opacity(1)
        self.play(Write(helper_equations[1][3:]))
        self.wait()

        self.play(FadeOut(surrounding_rectangle1))
        self.wait()

        square_formula_lines = VGroup(
            ConnectionLine(abbr_formula[0], helper_equations[0][-2], alpha = 1 / 5, color = '#628E90'),
            ConnectionLine(square_prop[7], square_prop[-2], alpha = 1 / 5, color = '#628E90'))

        self.play(Write(square_formula_lines))
        self.wait()

        helper_equations[2][7:].set_opacity(0)
        self.play(Write(helper_equations[2]))
        self.wait()

        self.play(FadeOut(square_prop, square_formula_lines))
        self.wait()

        # create surrounding rectangle for -5^2+21
        surrounding_rectangle2 = SurroundingRectangle(helper_equations[1][0:6], color = YELLOW, buff = 0.2)
        self.play(Write(surrounding_rectangle2))
        self.wait()

        helper_equations[-1].next_to(helper_equations[-2][-1], RIGHT).align_to(helper_equations[2][3], UP)

        self.play(ReplacementTransform(surrounding_rectangle2, helper_equations[-1]))
        self.wait()

        self.play(FadeOut(surrounding_rectangle2))
        self.wait()

        self.fix_formula(helper_equations[-1])

        self.play(ModifyFormula(helper_equations[-1], replace_items = [[1]], replace_items_strs=[['$2$', '$^2$']]))
        self.wait()

        # write difference of squares formula
        difference_of_squares_prop = self.difference_of_squares_prop.copy().move_to(helper_equations[2], LEFT).shift(
            DOWN + LEFT * 0.2)

        self.play(Write(difference_of_squares_prop))
        self.wait()

        self.play(AnimationGroup(
            helper_equations[2][1:6].animate.set_color(RED),
            difference_of_squares_prop[0].animate.set_color(RED),
            difference_of_squares_prop[7].animate.set_color(RED),
            difference_of_squares_prop[13].animate.set_color(RED)))
        self.wait()
        self.play(AnimationGroup(
            helper_equations[-1][-2].animate.set_color(BLUE),
            difference_of_squares_prop[3].animate.set_color(BLUE),
            difference_of_squares_prop[9].animate.set_color(BLUE),
            difference_of_squares_prop[15].animate.set_color(BLUE)))
        self.wait()

        self.fix_formula(difference_of_squares_prop)

        self.play(ModifyFormula(difference_of_squares_prop, replace_items = [[0], [7], [13]],
                                replace_items_strs = [['$($', '$a$', ' $+$ ', '$5$', '$)$'],
                                                    ['$($', '$a$', ' $+$ ', '$5$', '$)$'],
                                                    ['$($', '$a$', ' $+$ ', '$5$', '$)$']]))
        self.wait()

        self.play(
            ModifyFormula(difference_of_squares_prop, replace_items = [[7], [17], [27]],
                          replace_items_strs = [['$2$'], ['$2$'], ['$2$']]))
        self.wait()

        # add result of difference of squares to the solution
        difference_of_squares_prop_result = Tex(' $=$ ', '$($', '$($', '$a$', ' $+$ ', '$5$', '$)$', ' $-$ ', '$2$',
                                                '$)$', '$\cdot$', '$($',
                                                '$($', '$a$', ' $+$ ', '$5$', '$)$', ' $+$ ', '$2$', '$)$',
                                                font_size = FONT_SIZE)

        difference_of_squares_prop_result[2:7].set_color(RED)
        difference_of_squares_prop_result[12:17].set_color(RED)
        difference_of_squares_prop_result[8].set_color(BLUE)
        difference_of_squares_prop_result[18].set_color(BLUE)
        difference_of_squares_prop_result.move_to(difference_of_squares_prop[9], LEFT)

        difference_of_squares_prop[9:].set_opacity(0)

        self.play(difference_of_squares_prop_result.animate.next_to(helper_equations[-1][-1], RIGHT).align_to(
            helper_equations[2], DOWN))

        self.play(FadeOut(difference_of_squares_prop[0:9]))
        difference_of_squares_prop.set_opacity(0)
        self.wait(2)

        # sum the result of difference of squares
        self.fix_formula(difference_of_squares_prop_result)

        self.play(
            ModifyFormula(difference_of_squares_prop_result,
                          replace_items = [[2, 3, 4, 5, 6, 7, 8]],
                          replace_items_strs = [['$a$', ' $+$ ', '$3$', ]],
                          replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(
            ModifyFormula(difference_of_squares_prop_result,
                          replace_items = [[8, 9, 10, 11, 12, 13, 14]],
                          replace_items_strs = [['$a$', ' $+$ ', '$7$']],
                          replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(difference_of_squares_prop_result.animate.next_to(helper_equations[-1][-1], RIGHT).align_to(
            helper_equations[2], DOWN))
        self.wait()

        # write final solution
        self.play(AnimationGroup(
            VGroup(helper_equations, abbr_formula, difference_of_squares_prop_result[0]).animate.set_opacity(0),
            difference_of_squares_prop_result[1:].animate.next_to(formulas[0][-1], RIGHT).align_to(formulas[0], UP)))
        self.wait()

        # used in 4 exercise to move camera down
        self.solutions.add(difference_of_squares_prop_result[1:])

    def second(self):
        formulas = self.formulas
        numbers = self.numbers

        self.play(FadeIn(formulas[1:]), FadeIn(numbers[1:]))
        self.wait(2)
        self.play(FadeOut(formulas[2:], numbers[2:]))
        self.wait()

        # copy x^2+6x part and move down
        abbr_formula = Tex('$x$', '$^2$', ' $+$ ', '$6$', '$x$', font_size = FONT_SIZE).move_to(
            formulas[1]).align_to(formulas[1], LEFT)

        self.play(abbr_formula.animate.shift(DOWN))
        self.wait()

        self.fix_formula(abbr_formula)
        self.play(
            ModifyFormula(abbr_formula, replace_items = [[3, 4, 5]],
                          replace_items_strs = [['$2$', '$\cdot$', '$x$', '$\cdot$' '$3$']])
        )
        self.wait()

        # write sum square property
        square_prop = self.sum_square_prop.copy().move_to(formulas[1]).align_to(formulas[1], LEFT).shift(DOWN * 2)
        self.play(Write(square_prop))
        self.wait()

        self.play(AnimationGroup(
            square_prop[1].animate.set_color(RED),
            square_prop[7].animate.set_color(RED),
            square_prop[12].animate.set_color(RED),
            abbr_formula[0].animate.set_color(RED),
            abbr_formula[5].animate.set_color(RED)))
        self.wait()

        self.play(AnimationGroup(
            square_prop[3].animate.set_color(BLUE),
            square_prop[14].animate.set_color(BLUE),
            square_prop[-2].animate.set_color(BLUE),
            abbr_formula[-1].animate.set_color(BLUE)))
        self.wait()

        # change letters in sum square property to letters from the equation
        self.fix_formula(square_prop)
        self.play(
            ModifyFormula(square_prop, replace_items = [[1], [7], [12]],
                          replace_items_strs = [['$x$'], ['$x$'], ['$x$']]))
        self.wait()

        self.play(
            ModifyFormula(square_prop, replace_items = [[3], [14], [16]],
                          replace_items_strs = [['$3$'], ['$3$'], ['$3$']]))
        self.wait()

        helper_equations = VGroup(
            Tex(' $+$ ', '$3$', '$^2$', font_size = FONT_SIZE).next_to(abbr_formula[-1], RIGHT).align_to(abbr_formula,
                                                                                                       DOWN),
            Tex(' $-$ ', '$3$', '$^2$', ' $-$ ', '$1$', '$6$', ' $=$ ', font_size = FONT_SIZE),
            Tex(' $=$ ', '$($', '$x$', ' $+$ ', '$3$', '$)$', '$^2$', font_size = FONT_SIZE).move_to(formulas[1],
                                                                                                   LEFT).shift(DOWN),
            Tex(' $-$ ', '$2$', '$5$', font_size = FONT_SIZE))

        self.play(TransformFromCopy(square_prop[15:], helper_equations[0]))
        self.wait()

        # add -3^2 to abbreviate form and move to equality sign
        formulas[1][-1].set_opacity(1)

        self.play(Write(formulas[1][-1]),
                  VGroup(abbr_formula, helper_equations[0]).animate.next_to(formulas[1][-1], RIGHT).align_to(
                      formulas[1], DOWN))

        helper_equations[1].next_to(helper_equations[0][-1], RIGHT).align_to(helper_equations[0], UP)
        helper_equations[1][3:].set_opacity(0)

        self.play(Write(helper_equations[1]))
        self.wait()

        # create surrounding rectangle for 3^2-3^2
        surrounding_rectangle1 = SurroundingRectangle(VGroup(helper_equations[0][1:], helper_equations[1][0:3]),
                                                      color = YELLOW, buff = 0.2)
        self.play(Write(surrounding_rectangle1))
        self.wait()

        helper_equations[1][3:].set_opacity(1)
        self.play(Write(helper_equations[1][3:]))
        self.wait()

        self.play(FadeOut(surrounding_rectangle1))
        self.wait()

        square_formula_lines = VGroup(
            ConnectionLine(abbr_formula[0], helper_equations[0][-2], alpha =  1 / 5, color = '#628E90'),
            ConnectionLine(square_prop[7], square_prop[-2], alpha = 1 / 5, color = '#628E90'))

        self.play(Write(square_formula_lines))
        self.wait()

        helper_equations[2][7:].set_opacity(0)
        self.play(Write(helper_equations[2]))
        self.wait()

        self.play(FadeOut(square_prop, square_formula_lines))
        self.wait()

        # create surrounding rectangle for -3^2-16
        surrounding_rectangle2 = SurroundingRectangle(helper_equations[1][0:6], color = YELLOW, buff = 0.2)
        self.play(Write(surrounding_rectangle2))
        self.wait()

        helper_equations[-1].next_to(helper_equations[-2][-1], RIGHT).align_to(helper_equations[2][3], UP)

        self.play(ReplacementTransform(surrounding_rectangle2, helper_equations[-1]))
        self.wait()

        self.play(FadeOut(surrounding_rectangle2))
        self.wait()
        self.fix_formula(helper_equations[-1])

        self.play(ModifyFormula(helper_equations[-1], replace_items = [[1, 2]], replace_items_strs=[['$5$', '$^2$']]))
        self.wait()

        difference_of_squares_prop_result = Tex(' $=$ ', '$($', '$($', '$x$', ' $+$ ', '$3$', '$)$', ' $-$ ', '$5$',
                                                '$)$', '$\cdot$', '$($',
                                                '$($', '$x$', ' $+$ ', '$3$', '$)$', ' $+$ ', '$5$', '$)$',
                                                font_size = FONT_SIZE)

        difference_of_squares_prop_result.next_to(helper_equations[-1][-1], RIGHT).align_to(helper_equations[2], DOWN)

        self.play(Write(difference_of_squares_prop_result))
        self.wait(2)

        # sum the result of difference of squares
        self.fix_formula(difference_of_squares_prop_result)

        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[2, 3, 4, 5, 6, 7, 8]],
                                replace_items_strs = [['$x$', ' $-$ ', '$2$', ]],
                                replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[8, 9, 10, 11, 12, 13, 14]],
                                replace_items_strs = [['$x$', ' $+$ ', '$8$']],
                                replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        # write final solution
        self.play(AnimationGroup(
            VGroup(helper_equations, abbr_formula, difference_of_squares_prop_result[0]).animate.set_opacity(0),
            difference_of_squares_prop_result[1:].animate.next_to(formulas[1][-1], RIGHT).align_to(formulas[1], UP)))

        self.wait()
        # used in 4 exercise to move camera down
        self.solutions.add(difference_of_squares_prop_result[1:])

    def third(self):
        formulas = self.formulas
        numbers = self.numbers

        self.play(FadeIn(formulas[2]), FadeIn(numbers[2]))
        self.wait(0.25)
        # copy z^2-8z part and move down
        abbr_formula = Tex('$z$', '$^2$', ' $-$ ', '$8$', '$z$', font_size = FONT_SIZE).move_to(formulas[2]).align_to(
            formulas[2], LEFT)
        self.play(abbr_formula.animate.shift(DOWN))
        self.wait()

        self.fix_formula(abbr_formula)
        self.play(ModifyFormula(abbr_formula, replace_items = [[3, 4, 5]],
                                replace_items_strs = [['$2$', '$\cdot$', '$z$', '$\cdot$' '$4$']]))
        self.wait()

        helper_equations = VGroup(
            Tex(' $+$ ', '$4$', '$^2$', font_size = FONT_SIZE).next_to(abbr_formula[-1], RIGHT).align_to(abbr_formula,
                                                                                                       DOWN),
            Tex(' $-$ ', '$4$', '$^2$', ' $+$ ', '$7$', ' $=$ ', font_size = FONT_SIZE),
            Tex(' $=$ ', '$($', '$z$', ' $-$ ', '$4$', '$)$', '$^2$', ' $-$ ', '$9$', font_size = FONT_SIZE).move_to(
                formulas[2], LEFT).shift(DOWN)
        )
        # add 4^2 to abbreviate form and move to equality sign
        self.play(Write(helper_equations[0]))
        self.wait()

        formulas[2][-1].set_opacity(1)

        self.play(Write(formulas[2][-1]),
                  VGroup(abbr_formula, helper_equations[0]).animate.next_to(formulas[2][-1], RIGHT).align_to(
                      formulas[2], DOWN))

        helper_equations[1].next_to(helper_equations[0][-1], RIGHT).align_to(helper_equations[0], UP)

        self.play(Write(helper_equations[1]))
        self.wait()
        square_formula_line = ConnectionLine(abbr_formula[0], helper_equations[0][-2], alpha = 1 / 5, color = '#628E90')

        self.play(Write(square_formula_line))
        self.wait()

        self.play(Write(helper_equations[2]))
        self.wait()

        self.play(FadeOut(square_formula_line))
        self.wait()

        self.fix_formula(helper_equations[2])

        self.play(ModifyFormula(helper_equations[2], replace_items = [[8]], replace_items_strs=[['$3$', '$^2$']]))
        self.wait()

        difference_of_squares_prop_result = Tex(' $=$ ', '$($', '$($', '$z$', ' $-$ ', '$4$', '$)$', ' $-$ ', '$3$',
                                                '$)$', '$\cdot$', '$($',
                                                '$($', '$z$', ' $-$ ', '$4$', '$)$', ' $+$ ', '$3$', '$)$',
                                                font_size = FONT_SIZE).next_to(helper_equations[2][-1], RIGHT).align_to(
            helper_equations[2], DOWN)

        self.play(Write(difference_of_squares_prop_result))

        self.wait(2)
        # sum the result of difference of squares
        self.fix_formula(difference_of_squares_prop_result)
        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[2, 3, 4, 5, 6, 7, 8]],
                                replace_items_strs = [['$z$', ' $-$ ', '$7$', ]],
                                replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[8, 9, 10, 11, 12, 13, 14]],
                                replace_items_strs = [['$z$', ' $-$ ', '$1$']],
                                replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(difference_of_squares_prop_result.animate.next_to(helper_equations[2][-1], RIGHT).align_to(
            helper_equations[2], DOWN))
        self.wait()

        self.play(AnimationGroup(
            VGroup(helper_equations, abbr_formula, difference_of_squares_prop_result[0]).animate.set_opacity(0),
            difference_of_squares_prop_result[1:].animate.next_to(formulas[2][-1], RIGHT).align_to(formulas[2], UP)))
        self.wait()

        # used in 4 exercise to move camera down
        self.solutions.add(difference_of_squares_prop_result[1:])

    def fourth(self):
        formulas = self.formulas
        numbers = self.numbers

        self.play(FadeIn(formulas[3]), FadeIn(numbers[3]))
        self.wait(0.25)
        #shift previous tasks up
        self.play(VGroup(formulas, numbers, self.solutions, self.taskNumber).animate.shift(UP))
        self.wait()

        formulas = self.formulas
        # copy 4a^2+12a part and move down
        abbr_formula = Tex('$4$', '$a$', '$^2$', ' $+$ ', '$1$', '$2$', '$a$',
                           font_size = FONT_SIZE).move_to(
            formulas[3]).align_to(formulas[3], LEFT)
        abbr_formula[8:].set_opacity(0)

        self.play(abbr_formula.animate.shift(DOWN))
        self.wait()

        self.fix_formula(abbr_formula)
        self.play(
            ModifyFormula(abbr_formula, replace_items = [[0, 1]],
                          replace_items_strs = [['$($', '$2$', '$a$', '$)$']])
        )
        self.wait()
        self.play(
            ModifyFormula(abbr_formula, replace_items = [[6, 7, 8]],
                          replace_items_strs = [['$2$', '$\cdot$', '$($', '$2$', '$a$', '$)$', '$\cdot$' '$3$']])
        )
        self.wait()

        helper_equations = VGroup(
            Tex(' $+$ ', '$3$', '$^2$', font_size = FONT_SIZE).next_to(abbr_formula[-1], RIGHT).align_to(abbr_formula,
                                                                                                       UP),
            Tex(' $-$ ', '$3$', '$^2$', ' $+$ ', '$5$', ' $=$ ', font_size = FONT_SIZE),
            Tex(' $=$ ', '$($', '$2$', '$a$', ' $+$ ', '$3$', '$)$', '$^2$', ' $-$ ', '$4$',
                font_size = FONT_SIZE).move_to(formulas[3], LEFT).shift(DOWN))
        self.play(Write(helper_equations[0]))
        self.wait()

        formulas[3][-1].set_opacity(1)

        self.play(Write(formulas[3][-1]),
                  VGroup(abbr_formula, helper_equations[0]).animate.next_to(formulas[3][-1], RIGHT).align_to(
                      formulas[3], DOWN))

        helper_equations[1].next_to(helper_equations[0][-1], RIGHT).align_to(helper_equations[0], UP)

        self.play(Write(helper_equations[1]))
        self.wait()

        square_formula_line = ConnectionLine(abbr_formula[0], helper_equations[0][-2], alpha = 1 / 5, color = '#628E90')

        self.play(Write(square_formula_line))
        self.wait()

        self.play(Write(helper_equations[2]))
        self.wait()

        self.play(FadeOut(square_formula_line))
        self.wait()

        self.fix_formula(helper_equations[2])

        self.play(
            ModifyFormula(helper_equations[2], replace_items = [[9]],
                          replace_items_strs = [['$2$', '$^2$']])
        )
        self.wait()

        difference_of_squares_prop_result = Tex(
            ' $=$', '$($', '$($', '$2$', '$a$', '$+$', '$3$', '$)$', '$-$',
            '$2$', '$)$', '$\cdot$', '$($',
            '$($', '$2$', '$a$', '$+$', '$3$', '$)$', '$+$', '$2$', '$)$',
            font_size = FONT_SIZE).next_to(helper_equations[2][-1], RIGHT).align_to(helper_equations[2], DOWN)

        self.play(Write(difference_of_squares_prop_result))

        self.wait(2)

        self.fix_formula(difference_of_squares_prop_result)
        self.fix_formula(difference_of_squares_prop_result)
        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[2, 3, 4, 5, 6, 7, 8, 9]],
                                replace_items_strs = [['$2$', '$a$', ' $+$ ', '$1$']],
                                replace_items_colors = [[WHITE, WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(ModifyFormula(difference_of_squares_prop_result,
                                replace_items = [[9, 10, 11, 12, 13, 14, 15, 16]],
                                replace_items_strs = [['$2$', '$a$'' $+$ ', '$5$']],
                                replace_items_colors = [[WHITE, WHITE, WHITE]]))
        self.wait()

        self.play(difference_of_squares_prop_result.animate.next_to(helper_equations[2][-1], RIGHT).align_to(
            helper_equations[2], DOWN))
        self.wait()

        self.add(difference_of_squares_prop_result[1:])

        self.play(AnimationGroup(
            VGroup(helper_equations, abbr_formula, difference_of_squares_prop_result[0]).animate.set_opacity(0),
            difference_of_squares_prop_result[1:].animate.next_to(formulas[3][-1], RIGHT).align_to(formulas[3], UP)))
        self.wait()

        self.solutions.add(difference_of_squares_prop_result[1:])
        #shift previous tasks down
        self.play(VGroup(formulas, numbers, self.solutions, self.taskNumber).animate.shift(DOWN))
        self.wait()
