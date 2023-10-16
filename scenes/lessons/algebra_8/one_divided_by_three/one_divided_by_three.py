from manim import Scene, MathTex, Line, Write, TransformFromCopy, GrowFromPoint, Indicate, TransformMatchingShapes, VGroup, SurroundingRectangle, Create, FadeOut
from manim import LEFT, RIGHT, PI, UL, UP, DOWN, GREEN, UR, DL, DR

MATHTEX_FONT_SIZE = 85
SCALE_FACTOR_FOR_MATHTEX = 0.013

MathTex.set_default(font_size=MATHTEX_FONT_SIZE)

class OneDividedByThree(Scene):
    """1/3 = 0.333333333"""
    def construct(self):
        self.wait()

        task_tex = MathTex("1", ":", "3", "=", "0.33333...")
        task_tex[-1].set_opacity(0)
        task_srr_rect = SurroundingRectangle(task_tex, buff=0.3, color=GREEN)
        task = VGroup(task_tex, task_srr_rect).to_corner(UR, buff=.4).shift(LEFT * .3)
        self.play(Write(task_tex))
        self.play(Create(task_srr_rect))
        self.wait()

        # create lines
        horizontal_line = Line(LEFT, RIGHT)
        vertical_line = Line(UP, DOWN)

        vertical_line.set_length(4 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX).align_to(horizontal_line, UL)
        vertical_line.shift(UP * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX)
        VGroup(vertical_line, horizontal_line).to_corner(UL).shift(RIGHT*2.2)
        horizontal_line.set_length(
            1.6 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        ).align_to(vertical_line, LEFT)

        vertical_line.set_length(
            3.5 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        ).align_to(horizontal_line, UL).shift(UP * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX)

        self.play(GrowFromPoint(horizontal_line, horizontal_line.get_start()))
        self.play(TransformFromCopy(horizontal_line, vertical_line))
        self.wait()

        # create numbers a, b and answer
        a = MathTex("1")
        b = MathTex("3")
        answer = MathTex(*"0.33333", "...")

        b.next_to(horizontal_line, UP, aligned_edge=LEFT).shift(
            RIGHT * .2 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        )
        a.next_to(
            vertical_line, LEFT,
            buff=(a.get_right()[0] - a.get_left()[0] + .07) * 3
        ).align_to(b, UP)
        answer.next_to(horizontal_line, DOWN).align_to(b, LEFT)

        self.play(TransformFromCopy(task_tex[0], a, path_arc=PI/3))
        self.play(TransformFromCopy(task_tex[2], b, path_arc=PI/3))
        self.wait()

        # start division
        # step 1
        self.play(Indicate(a))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        self.play(Write(answer[0]))
        self.wait()
        explaination_line_1 = MathTex("0", "\\cdot", "3", "=", "0")
        explaination_line_1.next_to(task, DOWN, aligned_edge=LEFT, buff=3)
        self.play(TransformFromCopy(answer[0], explaination_line_1[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_1[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_1[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_1[3:]))
        self.wait()
        num2 = MathTex("0").next_to(a, DOWN, aligned_edge=LEFT)
        minus_sign1 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(b, num2), LEFT)
        self.play(Write(minus_sign1))
        self.play(TransformFromCopy(explaination_line_1[-1], num2, path_arc=PI/2))
        self.play(FadeOut(explaination_line_1))
        self.wait()
        line1 = Line(num2.get_left(), num2.get_right()).next_to(num2, DOWN, aligned_edge=LEFT).stretch(1.5, dim=None)
        self.play(GrowFromPoint(line1, line1.get_start()))
        num3 = MathTex("1").next_to(line1, DOWN).align_to(num2, LEFT)
        self.play(Write(num3))
        self.wait()

        # step 2
        self.play(Indicate(num3))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        self.play(Write(answer[1]))
        self.wait()
        num4 = MathTex("0").next_to(num3)
        self.play(Write(num4))
        self.wait()
        self.play(Indicate(VGroup(num3, num4)))
        self.wait()
        self.play(Write(answer[2]))
        explaination_line_2 = MathTex("3", "\\cdot", "3", "=", "9")
        explaination_line_2.align_to(explaination_line_1, DL)
        self.play(TransformFromCopy(answer[2], explaination_line_2[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_2[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[3:]))
        self.wait()
        num5 = MathTex("9").next_to(num4, DOWN, aligned_edge=LEFT)
        minus_sign2 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(num3, num5), LEFT)
        self.play(Write(minus_sign2))
        self.play(TransformFromCopy(explaination_line_2[-1], num5, path_arc=PI/2))
        self.play(FadeOut(explaination_line_2))
        self.wait()
        line2 = Line(num3.get_left(), num4.get_right()).next_to(num5, DOWN, aligned_edge=RIGHT)
        self.play(GrowFromPoint(line2, line2.get_start()))
        num6 = MathTex("1").next_to(line2, DOWN).align_to(num5, LEFT)
        self.play(Write(num6))
        self.wait()

        # step 3
        self.play(Indicate(num6))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        num7 = MathTex("0").next_to(num6)
        self.play(Write(num7))
        self.wait()
        self.play(Indicate(VGroup(num6, num7)))
        self.wait()
        self.play(Write(answer[3]))
        explaination_line_2 = MathTex("3", "\\cdot", "3", "=", "9")
        explaination_line_2.align_to(explaination_line_1, DL)
        self.play(TransformFromCopy(answer[3], explaination_line_2[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_2[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[3:]))
        self.wait()
        num8 = MathTex("9").next_to(num7, DOWN, aligned_edge=LEFT)
        minus_sign3 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(num6, num8), LEFT)
        self.play(Write(minus_sign3))
        self.play(TransformFromCopy(explaination_line_2[-1], num8, path_arc=PI/2))
        self.play(FadeOut(explaination_line_2))
        self.wait()
        line3 = Line(num6.get_left(), num7.get_right()).next_to(num8, DOWN, aligned_edge=RIGHT)
        self.play(GrowFromPoint(line3, line3.get_start()))
        num9 = MathTex("1").next_to(line3, DOWN).align_to(num8, LEFT)
        self.play(Write(num9))
        self.wait()

        # step 4
        arr_steps = [VGroup(num6, num7, num8, line3, num9).copy()]
        arr_steps_minus_signs = []
        answer[4:].set_opacity(0)
        for i in range(len(answer)-5):
            self.play(
                VGroup(
                    a, b, answer, horizontal_line, vertical_line,
                    num2, minus_sign1, line1, num3,
                    num4, num5, minus_sign2, num6, line2,
                    num7, num8, minus_sign3, num9, line3,
                    *arr_steps,
                    *arr_steps_minus_signs
                ).animate.scale(.81).to_corner(UL)
            )
            step = arr_steps[i].copy()
            arr_steps.append(step)
            
            minus_sign = minus_sign2.copy()
            minus_sign.add_updater(
                lambda x: x.next_to(step[:3], LEFT)
            )
            self.add(minus_sign)

            self.play(
                step.animate(path_arc=PI/2).align_to(arr_steps[i][-1], UL),
                answer[i+4].animate.set_opacity(1)
            )
            minus_sign.clear_updaters()
            arr_steps_minus_signs.append(minus_sign.copy())
            self.remove(minus_sign)
        
        self.add(arr_steps_minus_signs[-1])
        self.wait()

        bazmaketer = MathTex("...", font_size=MATHTEX_FONT_SIZE*1.2)
        bazmaketer.next_to(arr_steps[-1][-1], DOWN, aligned_edge=LEFT)
        self.play(
            Write(bazmaketer),
            answer[-1].animate.set_opacity(1)
        )
        self.wait()

        self.play(TransformFromCopy(answer, task_tex[-1].set_opacity(1), path_arc=-PI/2))
        self.wait()

        task_answer_tex = MathTex("1", ":", "3", "=", "0.(3)")
        task_answer_srr_rect = SurroundingRectangle(task_answer_tex, buff=0.3, color=GREEN)
        task_answer = VGroup(task_answer_tex, task_answer_srr_rect).to_corner(UR, buff=.4).shift(LEFT * .3)
        self.play(TransformMatchingShapes(task, task_answer))

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )
        FiveDividedByEleven.construct(self)

        return super().construct()


class FiveDividedByEleven(Scene):
    "5/11 = 0.45454545"
    def construct(self):
        self.wait()

        task_tex = MathTex("5", ":", "11", "=", "0." + "45" * 3 + "...")
        task_tex[-1].set_opacity(0)
        task_srr_rect = SurroundingRectangle(task_tex, buff=0.3, color=GREEN)
        task = VGroup(task_tex, task_srr_rect).to_corner(UR, buff=.4).shift(LEFT * .3)
        self.play(Write(task_tex))
        self.play(Create(task_srr_rect))
        self.wait()

        # create lines
        horizontal_line = Line(LEFT, RIGHT)
        vertical_line = Line(UP, DOWN)

        vertical_line.set_length(4 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX).align_to(horizontal_line, UL)
        vertical_line.shift(UP * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX)
        VGroup(vertical_line, horizontal_line).to_corner(UL).shift(RIGHT*2.2)
        horizontal_line.set_length(
            1.6 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        ).align_to(vertical_line, LEFT)

        vertical_line.set_length(
            3.5 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        ).align_to(horizontal_line, UL).shift(UP * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX)

        self.play(GrowFromPoint(horizontal_line, horizontal_line.get_start()))
        self.play(TransformFromCopy(horizontal_line, vertical_line))
        self.wait()

        # create numbers a, b and answer
        a = MathTex("5")
        b = MathTex("11")
        answer = MathTex(*"0.454545", "...")

        b.next_to(horizontal_line, UP, aligned_edge=LEFT).shift(
            RIGHT * .2 * MATHTEX_FONT_SIZE * SCALE_FACTOR_FOR_MATHTEX
        )
        a.next_to(
            vertical_line, LEFT,
            buff=(a.get_right()[0] - a.get_left()[0] + .07) * 3
        ).align_to(b, UP)
        answer.next_to(horizontal_line, DOWN).align_to(b, LEFT)

        self.play(TransformFromCopy(task_tex[0], a, path_arc=PI/3))
        self.play(TransformFromCopy(task_tex[2], b, path_arc=PI/3))
        self.wait()

        # start division
        # step 1
        self.play(Indicate(a))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        self.play(Write(answer[0]))
        self.wait()
        explaination_line_1 = MathTex("0", "\\cdot", "11", "=", "0")
        explaination_line_1.next_to(task, DOWN, aligned_edge=LEFT, buff=3)
        self.play(TransformFromCopy(answer[0], explaination_line_1[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_1[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_1[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_1[3:]))
        self.wait()
        num2 = MathTex("0").next_to(a, DOWN, aligned_edge=LEFT)
        minus_sign1 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(b, num2), LEFT)
        self.play(Write(minus_sign1))
        self.play(TransformFromCopy(explaination_line_1[-1], num2, path_arc=PI/2))
        self.play(FadeOut(explaination_line_1))
        self.wait()
        line1 = Line(num2.get_left(), num2.get_right()).next_to(num2, DOWN, aligned_edge=LEFT)
        self.play(GrowFromPoint(line1, line1.get_start()))
        num3 = MathTex("5").next_to(line1, DOWN).align_to(num2, LEFT)
        self.play(Write(num3))
        self.wait()

        # step 2
        self.play(Indicate(num3))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        self.play(Write(answer[1]))
        self.wait()
        num4 = MathTex("0").next_to(num3, buff=.08)
        self.play(Write(num4))
        self.wait()
        self.play(Indicate(VGroup(num3, num4)))
        self.wait()
        self.play(Write(answer[2]))
        explaination_line_2 = MathTex("4", "\\cdot", "11", "=", "44")
        explaination_line_2.align_to(explaination_line_1, DL)
        self.play(TransformFromCopy(answer[2], explaination_line_2[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_2[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[3:]))
        self.wait()
        num5 = MathTex("44").next_to(num4, DOWN, aligned_edge=RIGHT)
        minus_sign2 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(num3, num5), LEFT)
        self.play(Write(minus_sign2))
        self.play(TransformFromCopy(explaination_line_2[-1], num5, path_arc=PI/2))
        self.play(FadeOut(explaination_line_2))
        self.wait()
        line2 = Line(num3.get_left(), num4.get_right()).next_to(num5, DOWN, aligned_edge=RIGHT)
        self.play(GrowFromPoint(line2, line2.get_start()))
        num6 = MathTex("6").next_to(line2, DOWN).align_to(num5, RIGHT)
        self.play(Write(num6))
        self.wait()

        # step 3
        self.play(Indicate(num6))
        self.wait()
        self.play(Indicate(b))
        self.wait()
        num7 = MathTex("0").next_to(num6, buff=.08)
        self.play(Write(num7))
        self.wait()
        self.play(Indicate(VGroup(num6, num7)))
        self.wait()
        self.play(Write(answer[3]))
        explaination_line_2 = MathTex("5", "\\cdot", "11", "=", "55")
        explaination_line_2.align_to(explaination_line_1, DL)
        self.play(TransformFromCopy(answer[3], explaination_line_2[0], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[1]))
        self.wait()
        self.play(TransformFromCopy(b, explaination_line_2[2], path_arc=-PI/2))
        self.wait()
        self.play(Write(explaination_line_2[3:]))
        self.wait()
        num8 = MathTex("55").next_to(num7, DOWN, aligned_edge=RIGHT)
        minus_sign3 = MathTex("-", font_size=MATHTEX_FONT_SIZE/2).next_to(VGroup(num6, num8), LEFT)
        self.play(Write(minus_sign3))
        self.play(TransformFromCopy(explaination_line_2[-1], num8, path_arc=PI/2))
        self.play(FadeOut(explaination_line_2))
        self.wait()
        line3 = Line(num6.get_left(), num7.get_right()).next_to(num8, DOWN, aligned_edge=RIGHT)
        self.play(GrowFromPoint(line3, line3.get_start()))
        num9 = MathTex("5").next_to(line3, DOWN).align_to(num8, RIGHT)
        self.play(Write(num9))
        self.wait()

        # step 4
        arr_steps = [
            VGroup(
                VGroup(num3, num4, line2, num5),
                VGroup(num6, num7, num8, line3, num9)
            ).copy()
        ]
        arr_steps_minus_signs = []
        answer[4:].set_opacity(0)
        k = 0
        for i in range(1, len(answer)-4, 2):
            self.play(
                VGroup(
                    a, b, answer, horizontal_line, vertical_line,
                    num2, minus_sign1, line1, num3,
                    num4, num5, minus_sign2, num6, line2,
                    num7, num8, minus_sign3, num9, line3,
                    *arr_steps,
                    *arr_steps_minus_signs
                ).animate.scale(.7).to_corner(UL)
            )
            step = arr_steps[k].copy()
            arr_steps.append(step)
            
            temp_minus_sign1 = minus_sign2.copy()
            temp_minus_sign1.add_updater(
                lambda x: x.next_to(step[0][:3], LEFT)
            )
            self.add(temp_minus_sign1)

            temp_minus_sign2 = minus_sign2.copy()
            temp_minus_sign2.add_updater(
                lambda x: x.next_to(step[1][:3], LEFT)
            )
            self.add(temp_minus_sign2)

            self.play(
                step.animate(path_arc=PI/2).align_to(arr_steps[k][1][-1], UL),
                answer[i+4].animate.set_opacity(1),
                answer[i+3].animate.set_opacity(1)
            )
            temp_minus_sign1.clear_updaters()
            temp_minus_sign2.clear_updaters()
            arr_steps_minus_signs.append(temp_minus_sign1.copy())
            arr_steps_minus_signs.append(temp_minus_sign2.copy())
            self.remove(temp_minus_sign1, temp_minus_sign2)
            k+=1
        
        self.add(arr_steps_minus_signs[-1])
        self.add(arr_steps_minus_signs[-2])
        self.wait()

        self.play(
            VGroup(
                a, b, answer, horizontal_line, vertical_line,
                num2, minus_sign1, line1, num3,
                num4, num5, minus_sign2, num6, line2,
                num7, num8, minus_sign3, num9, line3,
                *arr_steps,
                *arr_steps_minus_signs
            ).animate.scale(.95).to_corner(UL)
        )
        bazmaketer = MathTex("...", font_size=MATHTEX_FONT_SIZE*1.2)
        bazmaketer.next_to(arr_steps[-1][-1][-1], DOWN, aligned_edge=LEFT)
        self.play(
            Write(bazmaketer),
            answer[-1].animate.set_opacity(1)
        )
        self.wait()

        self.play(TransformFromCopy(answer, task_tex[-1].set_opacity(1), path_arc=-PI/2))
        self.wait()

        task_answer_tex = MathTex("5", ":", "11", "=", "0.(45)")
        task_answer_srr_rect = SurroundingRectangle(task_answer_tex, buff=0.3, color=GREEN)
        task_answer = VGroup(task_answer_tex, task_answer_srr_rect).to_corner(UR, buff=.4).shift(LEFT * .3)
        self.play(TransformMatchingShapes(task, task_answer))

        self.wait(2)
