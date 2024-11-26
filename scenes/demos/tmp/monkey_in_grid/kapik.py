from manim import *
from objects import SimpleSVGMobject
from constants import LanguageConfig

class HungryMonkey(Scene):
    def construct(self):
        row_lines = VGroup(*[Line(color = GREEN, start=[-5, 2*i-3, 0],  end = [5, 2*i-3, 0]).set_z_index(-2) for i in range(4)])
        column_lines = VGroup(*[Line(color = GREEN, start=[2*(i-2.5), -3, 0], end = [2*(i-2.5), 3, 0]).set_z_index(-2) for i in range(6)])
        main_grid = VGroup(row_lines, column_lines)

        banana = SimpleSVGMobject('banana').move_to([4, 2, 0]).scale(2)
        monkey = SVGMobject('kapik').scale(0.9).move_to([-4, -2, 1])

        first_state_grid = VGroup(banana, monkey, row_lines, column_lines)

        first_state_grid.save_state()

        self.play(FadeIn(monkey), run_time = 2)
        self.play(Create(main_grid), rate_func = double_smooth, run_time = 2)
        self.play(FadeIn(banana), run_time = 2)
        self.wait()

        question_1 = Tex('Որոշել հնարավոր բոլոր ճանպարհների քանակը,\\\\ որոնցով կապիկը կարող է հասնել բանանին, եթե',).shift(2*DOWN)

        self.play(first_state_grid.animate.scale(0.7).shift(UP))
        self.play(Write(question_1))

        self.wait(3)

        question_2_1 = Tex('կապիկը շարժվի միայն')
        question_2_up = Tex('վերև')
        question_2_2 = Tex('կամ').next_to(question_2_up, RIGHT)
        question_2_right = Tex('աջ').next_to(question_2_2, RIGHT)

        question_2_up_or_right = VGroup(question_2_up, question_2_2, question_2_right).next_to(question_2_1, DOWN)

        question_2 = VGroup(question_2_1, question_2_up_or_right).move_to([4, 2, 0])
        self.play(first_state_grid.animate.shift(LEFT*3), FadeOut(question_1))
        self.play(Write(question_2))

        arrow_up_from_monkey = Arrow(start = [monkey.get_x(), monkey.get_y() + 0.4, 0], end = [monkey.get_x(), monkey.get_y() + 1.9, 0], color = RED)
        arrow_right_from_monkey = Arrow(start = [monkey.get_x() + 0.4, monkey.get_y(), 0], end = [monkey.get_x() + 1.9, monkey.get_y(), 0], color = BLUE)

        self.play(question_2_up.animate.set_color(RED), GrowArrow(arrow_up_from_monkey))
        self.play(question_2_right.animate.set_color(BLUE), GrowArrow(arrow_right_from_monkey))

        self.wait()

        self.play(Uncreate(question_2), FadeOut(arrow_right_from_monkey, arrow_up_from_monkey))
        self.play(first_state_grid.animate.move_to([0,0,0]).scale(10/7))

        self.wait()

        step_1 = MathTex('1', font_size = 75)
        step_2 = MathTex('2', font_size = 75)
        step_3 = MathTex('3', font_size = 75)
        step_4 = MathTex('4', font_size = 75)
        step_5 = MathTex('5', font_size = 75)
        step_6 = MathTex('6', font_size = 75)
        step_10 = MathTex('10', font_size = 75)


        step_0_1 = step_1.copy().move_to([-4, 0, 0])
        step_0_2 = step_1.copy().move_to([-4, 2, 0])
        step_1_0 = step_1.copy().move_to([-2, -2, 0])
        step_2_0 = step_1.copy().move_to([0, -2, 0])
        step_3_0 = step_1.copy().move_to([2, -2, 0])
        step_4_0 = step_1.copy().move_to([4, -2, 0])
        step_1_1 = step_2.copy().move_to([-2, 0, 0])
        step_1_2 = step_3.copy().move_to([-2, 2, 0])
        step_2_1 = step_3.copy().move_to([0, 0, 0])
        step_2_2 = step_6.copy().move_to([0, 2, 0])
        step_3_1 = step_4.copy().move_to([2, 0, 0])
        step_4_1 = step_5.copy().move_to([4, 0, 0])
        step_3_2 = step_10.copy().move_to([2, 2, 0])

        step_0_1_copy_1 = step_0_1.copy()
        step_0_2_copy_1 = step_0_2.copy()
        step_1_0_copy_1 = step_1_0.copy()
        step_2_0_copy_1 = step_2_0.copy()
        step_3_0_copy_1 = step_3_0.copy()
        step_4_0_copy_1 = step_4_0.copy()
        step_1_1_copy_1 = step_1_1.copy()
        step_1_2_copy_1 = step_1_2.copy()
        step_2_1_copy_1 = step_2_1.copy()
        step_3_1_copy_1 = step_3_1.copy()
        step_4_1_copy_1 = step_4_1.copy()
        step_3_2_copy_1 = step_3_2.copy()
        step_2_2_copy_1 = step_2_2.copy()
        step_1_1_copy_2 = step_1_1.copy()
        step_3_1_copy_2 = step_3_1.copy()
        step_2_2_copy_2 = step_2_2.copy()
        step_2_1_copy_2 = step_2_1.copy()


        steps = VGroup(
        step_0_1,
        step_0_1_copy_1,
        step_0_2,
        step_0_2_copy_1,

        step_1_0,
        step_1_0_copy_1,
        step_2_0,
        step_2_0_copy_1,
        step_3_0,
        step_3_0_copy_1,
        step_4_0,
        step_4_0_copy_1,

        step_1_1,
        step_1_2,
        step_2_1,
        step_2_2,
        step_3_1,
        step_4_1,
        step_3_2,
        step_1_1_copy_1,
        step_1_2_copy_1,
        step_2_1_copy_1,
        step_2_2_copy_1,
        step_3_1_copy_1,
        step_4_1_copy_1,
        step_3_2_copy_1,
        step_2_2_copy_2,
        step_3_1_copy_2,
        step_1_1_copy_2,
        step_2_1_copy_2,
        )

        for digit in steps[:5]:
            digit.set_color(RED)

        for digit in steps[5:13]:
            digit.set_color(BLUE)

        for digit in steps[13:]:
            digit.set_color(PURPLE)
        
        step_count = MathTex('15', color = ORANGE, font_size = 100).move_to([4,2,0]).set_color(PURPLE)

        self.play(
            GrowFromPoint(step_0_1, monkey.get_center()), GrowFromPoint(step_0_2.set_color(RED), monkey.get_center() + UP),
             )

        self.play(  
        GrowFromPoint(step_1_0, monkey.get_center()),
        GrowFromPoint(step_3_0, monkey.get_center() + RIGHT),
        GrowFromPoint(step_2_0, monkey.get_center() + 2 * RIGHT),
        GrowFromPoint(step_4_0, monkey.get_center() + 3 * RIGHT),
        )

        self.wait()

        def main_grid_filling_step(first_step, second_step, root_digit, time=1):
            self.play(
            AnimationGroup(
            GrowFromPoint(first_step, root_digit.get_center()),
            GrowFromPoint(second_step, root_digit.get_center()),
            run_time = time,
            rate_func = lambda x: 0.15 ** x),
            FadeIn(root_digit),
            run_time = time)

        main_grid_filling_step(step_0_1_copy_1, step_1_0_copy_1, step_1_1, 2)
        main_grid_filling_step(step_0_2_copy_1, step_1_1_copy_1, step_1_2)
        main_grid_filling_step(step_2_0_copy_1, step_1_1_copy_2, step_2_1)
        main_grid_filling_step(step_1_2_copy_1, step_2_1_copy_1, step_2_2)
        main_grid_filling_step(step_2_1_copy_2, step_3_0_copy_1, step_3_1)
        main_grid_filling_step(step_3_1_copy_1, step_4_0_copy_1, step_4_1)
        main_grid_filling_step(step_2_2_copy_2, step_3_1_copy_2, step_3_2)
        
        self.play(
            AnimationGroup(
            GrowFromPoint(step_3_2_copy_1, [4, 2, 0]),
            GrowFromPoint(step_4_1_copy_1, [4, 2, 0]),
            rate_func = lambda x: 0.15 ** x),
            FadeOut(banana),
            FadeIn(step_count)
        )

        self.wait(2)

        self.play(TransformMatchingTex(step_count, Tex('Պատասխան՝ 15', color=BLUE).scale(2)), FadeOut(monkey, main_grid, steps))

        self.wait()

LanguageConfig.set_language(HungryMonkey)