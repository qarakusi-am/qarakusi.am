from manim import Write, FadeOut, AnimationGroup, Tex, VGroup
from manim import Arrow, Cross, CurvedArrow, SurroundingRectangle
from manim import WHITE, ORANGE, GREEN, MathTex, TransformFromCopy
from manim import Scene, UR, RIGHT, LEFT, UP, DOWN
from qarakusiscene import TaskNumberBox
from .text import *

FONT_SIZE = 64
RUN_TIME_SPEED = 2


class Problem12714(Scene):
    def construct(self):
        self.taskNumber = taskNumber = TaskNumberBox(taskNumberString)
        self.add(taskNumber)
        self.wait(0.25)
        self.main_equation = main_equation = MathTex('4x+k+1=kx+2', font_size=80)
        self.play(Write(main_equation, run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(main_equation.animate.shift(UP * 3).scale(0.8))
        self.wait()

        self.write_wrong_solution()
        self.write_correct_solution()

    def write_wrong_solution(self, add=False):
        main_equation = self.main_equation
        shift_down_factor = 1.7
        equations = VGroup(
            MathTex('k = 2', font_size=FONT_SIZE),
            MathTex('4x + 2+1=2x+2', font_size=FONT_SIZE),
            MathTex('4x+3=2x+2', font_size=FONT_SIZE),
            MathTex('4x-2x=2-3', font_size=FONT_SIZE),
            MathTex('2x=-1', font_size=FONT_SIZE),
            MathTex(r"x = -\frac{1}{2} ", font_size=FONT_SIZE)
        )
        equations[0].next_to(main_equation, DOWN * shift_down_factor).shift(LEFT * 5)
        surrounding_k_box = SurroundingRectangle(equations[0][0], color=GREEN)

        k_value = VGroup(equations[0][0], surrounding_k_box)
        self.play(Write(k_value, run_time=RUN_TIME_SPEED))
        self.wait()

        equations[1][0][3].set_color(ORANGE)
        equations[1][0][7].set_color(ORANGE)
        equations[1].move_to(main_equation).shift(DOWN)
        self.play(Write(equations[1], run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(
            AnimationGroup(equations[1][0][3].animate.set_color(WHITE), equations[1][0][7].animate.set_color(WHITE)))
        self.wait()
        equations[2].move_to(equations[1]).shift(RIGHT * 0.57 + DOWN)
        equations[3].move_to(equations[2]).shift(0.375 * LEFT + DOWN)
        equations[4].move_to(equations[3]).shift(0.44 * RIGHT + DOWN)
        equations[5].move_to(equations[4]).shift(0.23 * RIGHT + DOWN*1.2)

        self.play( Write(equations[2][0], run_time=RUN_TIME_SPEED))
        self.wait()
        self.wait()

        arrow_to_left = CurvedArrow(equations[2][0][5].get_top(), equations[2][0][2].get_top(), tip_length=0.15,
                                    angle=.6).shift(UP * 0.1)
        arrow_to_right = CurvedArrow(equations[2][0][3].get_bottom(), equations[2][0][8].get_bottom(), tip_length=0.15,
                                     angle=.6).shift(DOWN * 0.1)
        self.play(Write(arrow_to_left))
        self.wait()
        self.play(Write(arrow_to_right))
        self.wait()
        self.play(
            Write(equations[3], run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(Write(equations[4], run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(Write(equations[5], run_time=RUN_TIME_SPEED))
        self.wait()

        surrounding_answer_box = SurroundingRectangle(equations[5], color=ORANGE)

        self.play(Write(surrounding_answer_box))
        self.wait()

        answer_arrow = Arrow(equations[5][0].get_center() + RIGHT * 1.5, equations[5][0].get_center() + RIGHT * 3,
                             max_stroke_width_to_length_ratio=2)

        self.play(Write(answer_arrow))
        self.wait()
        is_solution_label = Tex(is_solution, font_size=FONT_SIZE)
        self.play(Write(is_solution_label.next_to(answer_arrow)))
        self.wait()

        solution = VGroup(equations, arrow_to_right, arrow_to_left, answer_arrow, is_solution_label,
                          surrounding_answer_box, surrounding_k_box)

        cross = Cross(solution)
        self.play(Write(cross, run_time=RUN_TIME_SPEED))
        self.wait(2)
        self.play(FadeOut(solution, cross))

    def write_correct_solution(self, add=False):
        taskNumber = self.taskNumber
        main_equation = self.main_equation
        shift_down_factor = 1.7

        no_solution_str = Tex(equation_doesnt_have_solution_when, '$0$', '$\cdot$', '$x$', '$ = $', '$a$', '$, $ ', where,
                              '$a$', '$\\neq$', '$0$', font_size=FONT_SIZE)

        equations = VGroup(MathTex('4x-kx = 2-k-1',
                                   font_size=FONT_SIZE),
                           MathTex(' (4-k){\cdot}x = 1-k',
                                   font_size=FONT_SIZE),
                           MathTex(' k=4', font_size=FONT_SIZE),
                           MathTex(' (4-4){\cdot}x=1-4', font_size=FONT_SIZE),
                           MathTex(' 0{\cdot}x=-3', font_size=FONT_SIZE))

        self.play(Write(no_solution_str, run_time=RUN_TIME_SPEED + 1))
        self.wait(2)

        self.play(AnimationGroup(FadeOut(no_solution_str[0],
                          no_solution_str[7]),
                                 VGroup(no_solution_str[8:11]).animate.to_corner(UR).align_to(taskNumber, DOWN),
                  VGroup(no_solution_str[1:7]).animate.to_corner(UR).shift(LEFT * 1.3).align_to(taskNumber, DOWN)))

        self.wait(2)
        arrow_to_left = CurvedArrow(main_equation[0][7].get_top(), main_equation[0][2].get_top(), tip_length=0.15,
                                    angle=.6).shift(UP * 0.1)
        arrow_to_right = CurvedArrow(main_equation[0][4].get_bottom(), main_equation[0][9].get_bottom(),
                                     tip_length=0.13,
                                     angle=.6).shift(DOWN * 0.1)
        self.play(Write(arrow_to_left))
        self.wait()
        self.play(Write(arrow_to_right))
        self.wait()

        equations[0].move_to(main_equation).shift(DOWN+RIGHT*0.76)
        equations[1].move_to(equations[0]).shift( 0.72*LEFT + DOWN)
        equations[2].move_to(equations[1]).shift(DOWN*2+RIGHT*0.5)
        equations[3].move_to(equations[1]).shift(DOWN)
        equations[4].move_to(equations[3]).shift( DOWN+RIGHT*0.5)

        self.play(
            Write(equations[0],run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(AnimationGroup(
            equations[0][0][1].animate.set_color(ORANGE),
            equations[0][0][4].animate.set_color(ORANGE),
        ))
        self.wait()
        self.play(FadeOut(arrow_to_left,arrow_to_right))

        self.play(
            Write(equations[1],run_time=RUN_TIME_SPEED))
        self.wait()

        x_factor = VGroup(equations[1][0][0:5])
        surrounding_box = SurroundingRectangle(VGroup(equations[1][0][0:5]), color=ORANGE, buff=0.3)

        self.play(AnimationGroup(x_factor.animate.scale(1.2),Write(surrounding_box)))
        self.wait()

        arrow_to_solution_equation = CurvedArrow(surrounding_box.get_end()+DOWN*1.3, no_solution_str[1].get_bottom(),
                                                 tip_length=0.15, angle=2.5)
        self.play(Write(arrow_to_solution_equation,run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(FadeOut(arrow_to_solution_equation, surrounding_box), x_factor.animate.scale(1 / 1.2))

        equation_4 = MathTex('4-k', font_size=FONT_SIZE).next_to(equations[0][0][2],DOWN * 2).shift(DOWN+RIGHT*0.36)
        equality_sign=MathTex('=', font_size=FONT_SIZE).next_to(equation_4, RIGHT)
        equality_4_result=MathTex('0', font_size=FONT_SIZE).next_to(main_equation[0][7], DOWN).shift(DOWN*shift_down_factor*1.2)

        self.play(AnimationGroup(
            TransformFromCopy(x_factor, equation_4),
            TransformFromCopy(no_solution_str[1],equality_4_result),
            Write(equality_sign)))
        self.wait()

        self.play(
            Write(equations[2], run_time=RUN_TIME_SPEED))
        self.wait()


        self.play(AnimationGroup(
            FadeOut(equation_4,equality_sign,equality_4_result)),
            equations[2].animate.move_to(equations[1],LEFT).shift(LEFT*2))

        surrounding_k_box = SurroundingRectangle(VGroup(equations[2][0]), color=GREEN)

        self.play(Write(surrounding_k_box))
        self.wait()

        arrow_to_first_k = CurvedArrow(equations[2][0][0].get_bottom(), equations[1][0][3].get_bottom(), tip_length=0.15,angle=0.6).shift(DOWN*0.1)
        arrow_to_second_k = CurvedArrow(equations[2][0][0].get_bottom(), equations[1][0][10].get_bottom(), tip_length=0.15,angle=0.6).shift(DOWN*0.1)

        self.play(Write(arrow_to_first_k))
        self.wait()
        self.play(Write(arrow_to_second_k))
        self.wait()

        self.play(FadeOut(arrow_to_second_k,arrow_to_first_k))
        self.wait()

        self.play(
            Write(equations[3],run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(
            Write(equations[4],run_time=RUN_TIME_SPEED))
        self.wait()

        arrow_to_a = CurvedArrow(equations[4][0][5].get_bottom(),no_solution_str[5].get_bottom(), tip_length=0.15,angle=2.4).shift(DOWN*0.1)
        self.play(Write(arrow_to_a,run_time=RUN_TIME_SPEED))
        self.wait()

        self.play(Write(Tex('$\\neq 0$', font_size=FONT_SIZE).next_to(equations[4],RIGHT)))
        self.wait()


        self.play(Write(Tex(doesnt_have_solution, font_size=FONT_SIZE).next_to(equations[4], DOWN*shift_down_factor)))
        self.wait()








