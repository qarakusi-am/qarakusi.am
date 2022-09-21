from manim import *
from objects import SimpleSVGMobject
from constants import ENGTEX


class TarayinArtahaytutyun(Scene):
    def construct(self):

# INITS        
    # 
    
        paymanner = VGroup(
            Tex('Ճանապարհ - ', '700', ' (կմ)', font_size=40),
            Tex('Արագություն - ', '60', ' (կմ/ժ)', font_size=40),
        )

        dashed_line = DashedLine().match_width(paymanner)

        pahanj = Tex('Որքա՞ն ճանապարհ կմնա ', '4', ' (ժ) անց', font_size=40)
        pahanj.next_to(dashed_line, DOWN)

        line_hor = Line().match_width(pahanj).scale(1.1)

        VGroup(*paymanner, dashed_line, pahanj, line_hor).arrange(DOWN, aligned_edge=LEFT).to_edge(UL)

        line_hor.shift(0.3 * LEFT)
        line_ver = Line(line_hor.get_right(), line_hor.get_right() + 3 * UP)

        road = Line(stroke_width=8).scale(2.5).to_edge(RIGHT).shift([-0.6, 2, 0])
        road_length = road.get_right()[0] - road.get_left()[0]
        road_endpoint_left = Dot(road.get_left())
        road_endpoint_right = Dot(road.get_right())

        brace_total = Brace(road, DOWN)
        total_distance = Tex('700').next_to(brace_total, DOWN)

        car = SimpleSVGMobject('small_car').move_to(road_endpoint_left)
        car_trace = always_redraw(lambda: Line(road_endpoint_left.get_center(), car.get_center(), color=GREEN, stroke_width=8))

        speed_vector = VGroup(Line().scale(0.25).rotate(PI/2).next_to(car, UP))
        speed_vector.add(Line().scale(0.25).next_to(speed_vector[0], UP, buff=-0.02, aligned_edge=LEFT))
        speed_vector.add(Arrow().tip.scale(0.5).next_to(speed_vector[1], RIGHT, buff=0))
        speed_vector.add(Tex('60', font_size=35).next_to(speed_vector[1], UP))
        
        brace_passed = BraceBetweenPoints(road_endpoint_left.get_center(), road_endpoint_left.get_center() + 1.72 * RIGHT, UP)
        passed_distance = Tex('240').next_to(brace_passed, UP)

        brace_remaining = BraceBetweenPoints(road_endpoint_left.get_center() + 1.72 * RIGHT, road_endpoint_right.get_center(), UP)
        harcakan = Tex('?', tex_template=ENGTEX).next_to(brace_remaining, UP)
        remaining_distance = Tex('460').next_to(brace_remaining, UP)

    # լուծում
        solution_first_step = Tex('1) ', '60', ' $\cdot$ ', '4', ' = ', '240')
        solution_first_step.to_edge(LEFT).shift(DOWN)

        solution_second_step = Tex('2) ', '700', ' - ', '240', ' = ', '460')
        solution_second_step.to_edge(LEFT).shift(2 * DOWN)
    
    # լուծումն արտահայտությամբ ժամանակի տարբեր արժեքների դեպքում
        solution_4 = Tex('700', ' - ', '60', ' $\cdot$ ', '4', ' = ', '460', tex_template=ENGTEX)
        solution_4.next_to(VGroup(solution_first_step, solution_second_step), RIGHT).shift(2.5 * RIGHT)

        solution_5_final = Tex('700', ' - ', '60', ' $\cdot$ ', '5', ' = ', '400', tex_template=ENGTEX)
        solution_5_final.move_to([0, -0.75, 0])

        solution_5_initial = Tex('700', ' - ', '60', ' $\cdot$ ', '4', tex_template=ENGTEX)
        solution_5_initial.move_to(solution_5_final)
        solution_5_initial.align_to(solution_5_final, LEFT)

        solution_7_final = Tex('700', ' - ', '60', ' $\cdot$ ', '7', ' = ', '280', tex_template=ENGTEX)
        solution_7_final.move_to([0, -1.5, 0])

        solution_7_final_copy = solution_7_final.copy()
        case_t_is_7 = VGroup(
            Tex('t = 7', tex_template=ENGTEX),
            Tex('դեպքում')
        )
        case_t_is_7.arrange(buff=0.2, aligned_edge=UP).next_to(solution_7_final_copy, LEFT, buff= 0.5)

        solution_7_initial = Tex('700', ' - ', '60', ' $\cdot$ ', '5', tex_template=ENGTEX)
        solution_7_initial.move_to(solution_7_final)
        solution_7_initial.align_to(solution_7_final, LEFT)

        final_solution = Tex('700', ' - ', '60', ' $\cdot$ ', 't', tex_template=ENGTEX)
        final_solution.move_to([0, -0.75, 0])
        final_solution.align_to(solution_5_final, LEFT)
        rect_over_t = SurroundingRectangle(final_solution[-1])
        
        pahanj_5 = Tex('5', font_size=40).move_to(pahanj[1].get_center())
        pahanj_7 = Tex('7', font_size=40).move_to(pahanj[1].get_center())
        pahanj_t = Tex('t', font_size=40, tex_template=ENGTEX).move_to(pahanj[1].get_center())

        arrow_t = Arrow()
        VGroup(arrow_t, arrow_t.tip).scale(0.5)
        arrow_t.tip.scale(1.5)
        arrow_t.rotate(3/16 * PI).next_to(final_solution[-1], UR, buff=0.1)

        time_zhamanak = VGroup(Tex('time = ', font_size=35, tex_template=ENGTEX), Tex('ժամանակ', font_size=35))
        time_zhamanak.arrange(buff=0.1, aligned_edge=UP)
        time_zhamanak.next_to(arrow_t, UR, buff=0.1).shift([0.1, -0.05, 0])

        solution_with_v = Tex('700', ' - ', 'V', ' $\cdot$ ', '7', tex_template=ENGTEX)
        solution_with_v.move_to([0, -2, 0]).align_to(final_solution, LEFT)

        solution_v_60 = Tex('700', ' - ', '60', ' $\cdot$ ', '7', ' = ', '280', tex_template=ENGTEX)
        solution_v_60.move_to([0, -2.75, 0]).align_to(solution_with_v, LEFT)
        case_v_is_60 = VGroup(
            Tex('V = 60', tex_template=ENGTEX),
            Tex('դեպքում')
        )
        case_v_is_60.arrange(buff=0.2, aligned_edge=UP).next_to(solution_v_60, LEFT, buff= 0.5)



# ANIMATIONS  
    
    # գծագիր ու պայմաններ
        self.play(
            Create(road_endpoint_left),
            Create(road),
            Create(road_endpoint_right)
        )
        self.play(Write(brace_total))
        self.play(Write(total_distance))
        self.wait()

        self.play(FadeIn(car))
        self.add(car_trace, road_endpoint_left, car)
        self.wait()

        self.play(
            AnimationGroup(
                Create(speed_vector[0]),
                Create(speed_vector[1:3]),
                Write(speed_vector[3]),
                lag_ratio=0.5, run_time=1.5
            )
        )
        self.wait()

        self.play(VGroup(car, speed_vector).animate.shift(12/7 * RIGHT), rate_func=linear)
        self.play(Write(brace_remaining))
        self.play(Write(harcakan))
        self.wait()

        self.add(paymanner, pahanj, dashed_line, line_hor, line_ver)
        self.wait()

        self.play(FadeOut(speed_vector))
        self.wait()

    # լուծում

        # առաջին քայլ
        self.play(Write(solution_first_step[0]))
        self.wait(0.25)

        self.play(Circumscribe(paymanner[1], fade_out=True))
        self.play(Circumscribe(pahanj[1:], fade_out=True))
        self.wait(0.25)

        self.play(ReplacementTransform(paymanner[1][1:2].copy(), solution_first_step[1:2]))
        self.play(Write(solution_first_step[2], run_time=0.5))
        self.play(ReplacementTransform(pahanj[1:2].copy(), solution_first_step[3:4]))
        self.play(Write(solution_first_step[4:]))
        self.wait(0.5)

        self.play(Write(brace_passed))
        self.play(Write(passed_distance))
        self.wait()

        # երկրորդ քայլ
        self.play(Write(solution_second_step[0]))
        self.wait(0.25)

        self.play(Wiggle(brace_remaining, run_time=1.25, rate_func=linear))
        self.wait(0.5)
        self.play(Wiggle(brace_total, run_time=1.25, rate_func=linear))
        self.wait(0.5)
        self.play(Wiggle(brace_passed, run_time=1.25, rate_func=linear))
        self.wait(0.5)

        self.play(ReplacementTransform(total_distance.copy(), solution_second_step[1:2]))
        self.play(Write(solution_second_step[2], run_time=0.5))
        self.play(ReplacementTransform(passed_distance.copy(), solution_second_step[3:4]))
        self.play(Write(solution_second_step[4:]))
        self.wait(0.25)
        self.play(ReplacementTransform(harcakan, remaining_distance))
        self.wait()

    # լուծումն արտահայտությամբ
        self.play(Write(solution_4[:-2]), run_time=2)
        self.wait()
        self.play(Write(solution_4[-2:]))
        self.wait()

        self.play(
            FadeOut(passed_distance, brace_passed, solution_first_step, solution_second_step),
            solution_4.animate.move_to(ORIGIN)
        )
        self.wait()

    # add updaters to braces and values
        brace_remaining.add_updater(lambda mob: mob.become(BraceBetweenPoints(car.get_center(), road_endpoint_right.get_center(), UP)))
        remaining_distance.add_updater(lambda mob: 
            mob.become(Tex(f'{int(700 * (road.get_right()[0] - car.get_center()[0]) / road_length)}', tex_template=ENGTEX)).next_to(brace_remaining, UP)
        )

    # 4-ը դարձնել 5
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(pahanj[1])))
        self.play(Transform(pahanj[1], pahanj_5))
        self.wait(0.5)

        self.play(
            ReplacementTransform(solution_4[:-3].copy(), solution_5_final[:-3]),
            ReplacementTransform(solution_4[-3].copy(), solution_5_initial[-1])
        )
        self.remove(solution_5_initial[:-1])
        self.add(solution_5_final[:-3])
        self.play(ReplacementTransform(solution_5_initial[-1], solution_5_final[-3]))
        self.wait(0.5)
        self.play(Write(solution_5_final[-2:]))
        self.wait(0.5)

        self.play(car.animate.shift(3/7 * RIGHT), rate_func=linear)
        self.wait()
    
    # 5-ը դարձնել 7
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(pahanj[1])))
        self.play(Transform(pahanj[1], pahanj_7))
        self.wait(0.5)

        self.play(
            ReplacementTransform(solution_5_final[:-3].copy(), solution_7_final[:-3]),
            ReplacementTransform(solution_5_final[-3].copy(), solution_7_initial[-1])
        )
        self.remove(solution_7_initial[:-1])
        self.add(solution_7_final[:-3])
        self.play(ReplacementTransform(solution_7_initial[-1], solution_7_final[-3]))
        self.wait(0.5)
        self.play(Write(solution_7_final[-2:]))
        self.wait(0.5)

        self.play(car.animate.shift(6/7 * RIGHT), rate_func=linear)
        self.wait()

    # միավորել արտահայտությունները, նշանակել t
        self.play(FadeOut(solution_4[-2:], solution_5_final[-2:], solution_7_final[-2:]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(solution_4[0:4], final_solution[0:4], remover=True),
            ReplacementTransform(solution_5_final[0:4], final_solution[0:4]),
            ReplacementTransform(solution_7_final[0:4], final_solution[0:4], remover=True),
        )
        self.wait(0.5)

        rect_over_times = SurroundingRectangle(VGroup(solution_4[-3], solution_5_final[-3], solution_7_final[-3]))  # init
        self.play(FadeIn(rect_over_times))
        self.wait(0.5)

        self.play(
            ReplacementTransform(VGroup(solution_4[-3], solution_5_final[-3], solution_7_final[-3]), final_solution[-1]),
            ReplacementTransform(rect_over_times, rect_over_t),
            Transform(pahanj[1], pahanj_t)
        )
        self.wait(0.25)
        self.play(FadeOut(rect_over_t))
        self.wait(0.25)

        self.play(Create(arrow_t))
        self.play(Write(time_zhamanak))
        self.wait(0.5)

        self.play(FadeOut(arrow_t, time_zhamanak))
        self.wait()
    
    # t=7 դեպքում 700-60*7-=280
        self.play(Write(case_t_is_7[0]))
        self.play(Write(case_t_is_7[1]))
        self.wait(0.5)
        self.play(Write(solution_7_final_copy, run_time=2))
        self.wait()
        self.play(Circumscribe(VGroup(final_solution[-1], solution_7_final_copy[-3]), fade_out=True, run_time=2.5))
        self.wait()
        self.play(VGroup(solution_7_final_copy, case_t_is_7, final_solution).animate.shift(UP))

    # արագույթյամբ արտահայտություն, տեղադրում
        self.play(Circumscribe(paymanner[1], fade_out=True, run_time=3))
        self.wait()

        self.play(Write(solution_with_v))
        self.wait()
        self.play(Write(case_v_is_60, run_time=1.5))
        self.wait(0.5)
        self.play(Write(solution_v_60, run_time=2))
        self.wait()

        self.play(Circumscribe(VGroup(solution_v_60[-5], solution_with_v[-3]), fade_out=True, run_time=2))
        self.wait()





