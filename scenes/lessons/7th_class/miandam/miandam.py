from manim import *

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r'\usepackage{armtex}')

prop_a = 60 / 720 / 2
prop_b = 70 / 720 / 2

color_a = GREEN
color_b = ORANGE


class RoadScene(Scene):
    def construct(self):

# INITS

        aram_60 = Tex('Արամ',  ' - ',  '$60$', ' կմ/ժ', tex_template=ARMTEX, color=color_a)
        aram_60.to_edge(UL)
        babken_70 = Tex('Բաբկեն',  ' - ',  '$70$', ' կմ/ժ', tex_template=ARMTEX, color=color_b)
        babken_70.next_to(aram_60, DOWN, aligned_edge=LEFT)

        urish = Tex('Առաջին վարորդ', tex_template=ARMTEX, color=color_a).align_to(aram_60[0], DL)
        urish_urish = Tex('Երկրորդ վարորդ', tex_template=ARMTEX, color=color_b).align_to(babken_70[0], DL)

        seventy = Tex('$70$', color=color_a)
        ninty = Tex('$90$', color=color_b)

        x = Tex('$x$', color=color_a)
        y = Tex('$y$', color=color_b)

    # ճանապարհի նկար
        road = SVGMobject('objects/SVG_files/road').set_color(WHITE)
        road.scale(2).to_edge(UR).shift(DOWN)
        road.points = road.get_all_points()

        dot_prop = ValueTracker(0)
        moving_dot = always_redraw(lambda: Dot(road.point_from_proportion(dot_prop.get_value()), radius=DEFAULT_DOT_RADIUS / 10))

        car = SVGMobject('objects/SVG_files/small_car').set_color(PURE_RED).scale(0.15)
        rotation = 0
        def car_updater(mob):
            nonlocal rotation
            target_rotation = np.arctan2(
                    (road.point_from_proportion(dot_prop.get_value() + 0.0001)[1] - road.point_from_proportion(dot_prop.get_value())[1]),
                    (road.point_from_proportion(dot_prop.get_value() + 0.0001)[0] - road.point_from_proportion(dot_prop.get_value())[0])
            )
            ret = mob.rotate(target_rotation - rotation)
            rotation = target_rotation
            return ret
        car.add_updater(
            lambda mob: mob.become(car_updater(mob.move_to(moving_dot)))
        )

        segments_a = VGroup(*[VMobject(color=color_a, stroke_width=7) for _ in range(4)])
        segments_b = VGroup(*[VMobject(color=color_b, stroke_width=7) for _ in range(3)])

        def update_seg(seg):
            previous_seg = seg.copy()
            previous_seg.add_points_as_corners([moving_dot.get_center()])
            seg.become(previous_seg)
    
    # արտահայտություններ
        first_day_equation = Tex('$60$', ' $+$ ', '$70$', ' $+$ ', '$60$', ' $+$ ', '$70$', ' $+$ ', '$60$').to_edge(LEFT).shift(UP)
        VGroup(first_day_equation[0], first_day_equation[4], first_day_equation[8]).set_color(color_a)
        VGroup(first_day_equation[2], first_day_equation[6]).set_color(color_b)

        modified_equation = Tex(
            '$3$', ' $\cdot$ ', '$60$', ' $+$ ', '$2$', ' $\cdot$ ', '$70$',  ' $+$ ', 
            '$2$', ' $\cdot$ ', '$60$', ' $+$ ', '$4$', ' $\cdot$ ', '$70$'
        )
        modified_equation.to_edge(LEFT)
        modified_equation[2].set_color(color_a)
        modified_equation[6].set_color(color_b)
        modified_equation[10].set_color(color_a)
        modified_equation[14].set_color(color_b)

        surr_rects_60 = VGroup(
            SurroundingRectangle(modified_equation[0:3]),
            SurroundingRectangle(modified_equation[8:11])
        )
        surr_rects_70 = VGroup(
            SurroundingRectangle(modified_equation[4:7]),
            SurroundingRectangle(modified_equation[12:])
        )

        final_equation = Tex('$5$', ' $\cdot$ ', '$60$', ' $+$ ', '$6$', ' $\cdot$ ', '$70$')
        final_equation.to_edge(LEFT).shift(DOWN)
        final_equation[2].set_color(color_a)
        final_equation[-1].set_color(color_b)

        three_plus_two_times_60 = Tex('$($', '$3$', ' $+$ ', '$2$', '$)$', ' $\cdot$ ', '$60$')
        three_plus_two_times_60.move_to(final_equation[0]).shift(RIGHT)

        two_plus_four_times_70 = Tex('$($', '$2$', ' $+$ ', '$4$', '$)$', ' $\cdot$ ', '$70$')
        two_plus_four_times_70.move_to(final_equation[-1]).shift(0.35 * RIGHT)

        sixties = VGroup(
            aram_60[2],
            # first_day_equation[0],
            # first_day_equation[4],
            # first_day_equation[8],
            modified_equation[2],
            modified_equation[10],
            final_equation[2]
        )
        seventies = VGroup(
            babken_70[2],
            # first_day_equation[2],
            # first_day_equation[6],
            modified_equation[6],
            modified_equation[14],
            final_equation[6]
        )

# ANIMATIONS

        def anim_hamarotagrutyun(): # համառոտագրություն
            self.play(Write(aram_60))
            self.wait()
            self.play(Write(babken_70))
            self.wait(0.5)

            self.play(Write(road))
            self.add(moving_dot)
            self.wait(0.5)

            self.play(FadeIn(car))
            self.wait(0.5)

        def anim_first_day(): # առաջին օրը 60 70 60 70 60
            for i in range(5):
                if i % 2 == 0:
                    segments_a[int(i / 2)].set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])
                    self.add(segments_a[int(i / 2)], car)
                    segments_a[int(i / 2)].add_updater(update_seg)
                    if i == 0:
                        self.play(dot_prop.animate(rate_func=linear).set_value(dot_prop.get_value() + prop_a))
                        self.wait(0.5)
                        self.play(Write(first_day_equation[i]))
                    else:
                        self.play(
                            dot_prop.animate(rate_func=linear).set_value(dot_prop.get_value() + prop_a),
                            Write(first_day_equation[2*i-1 : 2*i+1])
                        )
                    segments_a[int(i / 2)].clear_updaters()
                    self.wait()
                else:
                    segments_b[int(i / 2)].set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])
                    self.add(segments_b[int(i / 2)], car)
                    segments_b[int(i / 2)].add_updater(update_seg)
                    if i == 1:
                        self.play(dot_prop.animate(rate_func=linear).set_value(dot_prop.get_value() + prop_b))
                        self.wait(0.5)
                        self.play(Write(first_day_equation[2*i-1 : 2*i+1]))
                    else:
                        self.play(
                            dot_prop.animate(rate_func=linear).set_value(dot_prop.get_value() + prop_b),
                            Write(first_day_equation[2*i-1 : 2*i+1])
                        )
                    segments_b[int(i / 2)].clear_updaters()
                    self.wait()
    
        def anim_modify_equation(): # արտահայտության ձևափոխում
            copy_60 = VGroup(first_day_equation[0], first_day_equation[4], first_day_equation[8]).copy() # init
            self.play(copy_60.animate.arrange(buff=0.5).move_to(modified_equation[2]))
            self.wait()
            self.play(
                AnimationGroup(
                    AnimationGroup(*[ReplacementTransform(tiv, modified_equation[2]) for tiv in copy_60]),
                    Write(modified_equation[:2]),
                    lag_ratio=0.5
                )
            )
            self.wait()

            copy_70 = VGroup(first_day_equation[2], first_day_equation[6]).copy() # init
            self.play(copy_70.animate.arrange(buff=0.5).next_to(modified_equation[2], RIGHT, buff=1))
            self.wait()
            self.play(
                AnimationGroup(
                    AnimationGroup(*[ReplacementTransform(tiv, modified_equation[6]) for tiv in copy_70]),
                    Write(modified_equation[3:6]),
                    lag_ratio=0.5
                )
            )
            self.wait()
            self.play(FadeOut(first_day_equation))
            self.wait()

        def anim_second_day(): # երկրորդ օրը 2 * 60 + 4 * 70
            segments_a[-1].set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])
            self.add(segments_a[-1], car)
            segments_a[-1].add_updater(update_seg)
            self.play(dot_prop.animate(rate_func=linear, run_time=1.75).set_value(dot_prop.get_value() + 2 * prop_a))
            self.wait(0.25)
            self.play(Write(modified_equation[7:11]))
            segments_a[-1].clear_updaters()
            self.wait()

            segments_b[-1].set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])
            self.add(segments_b[-1], car)
            segments_b[-1].add_updater(update_seg)
            self.play(dot_prop.animate(rate_func=linear, run_time=3).set_value(dot_prop.get_value() + 4 * prop_b))
            self.wait(0.25)
            self.play(Write(modified_equation[11:]))
            segments_b[-1].clear_updaters()
            self.wait()

        def anim_final_equation(): # արտահայտության վերջնական տեսք
            self.play(Create(surr_rects_60[0]))
            self.wait(0.25)
            self.play(Create(surr_rects_60[1]))
            self.wait(0.25)
            self.play(
                ReplacementTransform(modified_equation[0].copy(), three_plus_two_times_60[1]),
                ReplacementTransform(modified_equation[8].copy(), three_plus_two_times_60[3]),
                Write(three_plus_two_times_60[0]),
                Write(three_plus_two_times_60[2]),
                Write(three_plus_two_times_60[4]),
                Write(three_plus_two_times_60[5]),
                Write(three_plus_two_times_60[6])
            )
            self.wait(0.5)

            self.play(
                ReplacementTransform(three_plus_two_times_60[:-2], final_equation[0]),
                ReplacementTransform(three_plus_two_times_60[-2], final_equation[1]),
                ReplacementTransform(three_plus_two_times_60[-1], final_equation[2]),
            )
            self.wait()

            self.play(
                FadeOut(surr_rects_60),
                Create(surr_rects_70)
            )
            self.wait(0.5)
            self.play(
                ReplacementTransform(modified_equation[4].copy(), two_plus_four_times_70[1]),
                ReplacementTransform(modified_equation[12].copy(), two_plus_four_times_70[3]),
                Write(two_plus_four_times_70[0]),
                Write(two_plus_four_times_70[2]),
                Write(two_plus_four_times_70[4]),
                Write(two_plus_four_times_70[5]),
                Write(two_plus_four_times_70[6])
            )
            self.wait(0.5)

            self.play(
                ReplacementTransform(two_plus_four_times_70[:-2], final_equation[4]),
                ReplacementTransform(two_plus_four_times_70[-2], final_equation[5]),
                ReplacementTransform(two_plus_four_times_70[-1], final_equation[6]),
                Write(final_equation[3])
            )
            self.wait(0.25)
            self.play(FadeOut(surr_rects_70))
            self.wait()

        def anim_adding_variables(): # Ուրիշ 2 հոգի, ուրիշ արագություններ
            self.play(
                ReplacementTransform(aram_60[0], urish),
                aram_60[1:].animate.next_to(urish, buff=0.25),
                ReplacementTransform(babken_70[0], urish_urish),
                babken_70[1:].animate.next_to(urish_urish, buff=0.25)
            )
            self.wait()
            
            self.play(
                Transform(aram_60[2], seventy.move_to(aram_60[2])),
                Transform(babken_70[2], ninty.move_to(babken_70[2]))
            )
            self.wait()

            self.play(
                *[Transform(mob, seventy.copy().move_to(mob)) for mob in sixties],
                *[Transform(mob, ninty.copy().move_to(mob)) for mob in seventies]
            )
            self.wait()

            self.play(*[Transform(mob, x.copy().move_to(mob).align_to(mob, DOWN)) for mob in sixties])
            self.wait()
            self.play(*[Transform(mob, y.copy().move_to(mob).align_to(mob, DOWN).shift(0.1 * DOWN)) for mob in seventies])
            self.wait()

            self.play(Circumscribe(final_equation, fade_out=True, run_time=2))
            self.wait()

            car.clear_updaters()
            moving_dot.clear_updaters()
            self.play(FadeOut(
                aram_60, babken_70, first_day_equation,
                modified_equation, car, moving_dot, road,
                segments_a, segments_b, urish, urish_urish
            ))
            self.wait(0.5)

            self.remove(final_equation)
            self.play(
                AnimationGroup(
                    FadeOut(final_equation[1], final_equation[-2]),
                    Transform(
                        VGroup(final_equation[0], *final_equation[2:5], final_equation[-1]), 
                        Tex('$5$', '$x$', ' $+$ ', '$6$', '$y$', font_size=70)
                    ),
                    lag_ratio=0.5, run_tim=1.5
                )
            )
            self.wait()

        anim_hamarotagrutyun() # 0-7
        anim_first_day() # 8-21
        anim_modify_equation() # 22-31
        anim_second_day() # 32-39
        anim_final_equation() # 40-55
        anim_adding_variables() # 56-71


# վիդյոյի վերջում հետ ենք բերում էս էկրանը
    # inits

        final_equation_copy = Tex('$5$', ' $\cdot$ ', '$x$', ' $+$ ', '$6$', ' $\cdot$ ', '$y$')
        final_equation_copy.to_edge(LEFT).shift(DOWN)
        final_equation_copy[2].set_color(color_a)
        final_equation_copy[-1].set_color(color_b)

        surr_rects_modified = VGroup(
            SurroundingRectangle(modified_equation[0:3], color=BLUE, corner_radius=0.25),
            SurroundingRectangle(modified_equation[4:7], color=BLUE, corner_radius=0.25),
            SurroundingRectangle(modified_equation[8:11], color=BLUE, corner_radius=0.25),
            SurroundingRectangle(modified_equation[12:], color=BLUE, corner_radius=0.25),
        )

        surr_rects_final = VGroup(
            SurroundingRectangle(final_equation_copy[0:3], color=BLUE, corner_radius=0.25),
            SurroundingRectangle(final_equation_copy[4:], color=BLUE, corner_radius=0.25),
        )

    # animations

        def anim_nman_miandamner():
            self.remove(*self.mobjects)
            self.add(
                aram_60, babken_70, moving_dot, road,
                modified_equation, final_equation_copy,
                segments_a, segments_b, urish, urish_urish, car
            )
            self.wait()

            self.play(Create(surr_rects_modified))
            self.wait()
            self.play(FadeOut(surr_rects_modified[1], surr_rects_modified[3]))
            self.wait()

            self.play(
                ReplacementTransform(surr_rects_modified[0], surr_rects_final[0]),
                ReplacementTransform(surr_rects_modified[2], surr_rects_final[0])
            )
            self.wait()

            self.play(Create(surr_rects_final[1]))
            self.wait()

            self.play(*[FadeOut(mob) for mob in self.mobjects])

        anim_nman_miandamner() # 72-82


class FiveXPlusSixY(Scene):
    def construct(self):

# INITS

        five_x_plus_six_y = Tex('$5x$', ' $+$ ', '$6y$', font_size=70)
        surr_rect_five_x_plus_six_y = SurroundingRectangle(five_x_plus_six_y, buff=MED_SMALL_BUFF)
        surr_rect_six_y = SurroundingRectangle(five_x_plus_six_y[2], color=BLUE, corner_radius=0.25)
        surr_rect_five_x = SurroundingRectangle(five_x_plus_six_y[0], color=BLUE, corner_radius=0.25)
        surr_rect_five_x.stretch(1.2, 1).align_to(surr_rect_six_y, UP)

        bazmandam_arrow = Arrow(color=YELLOW).rotate(PI / 4).next_to(surr_rect_five_x_plus_six_y, UR, buff=0)
        miandam_arrows = VGroup(
            Arrow(color=BLUE).rotate(- PI * 3 / 8).next_to(surr_rect_five_x, DOWN, buff=0).shift(0.2 * RIGHT),
            Arrow(color=BLUE).rotate(- PI * 5 / 8).next_to(surr_rect_six_y, DOWN, buff=0).shift(0.2 * LEFT)
        )

        bazmandam = Tex('Բազմանդամ', tex_template=ARMTEX, font_size=60).next_to(bazmandam_arrow, UR)
        miandam = Tex('Միանդամ', tex_template=ARMTEX, font_size=60).next_to(miandam_arrows, DOWN)



# ANIMATIONS

        self.add(five_x_plus_six_y)
        self.wait()

        self.play(Create(surr_rect_five_x), Create(surr_rect_six_y))
        self.wait()
        self.play(Create(surr_rect_five_x_plus_six_y))
        self.wait(0.25)
        self.play(Create(bazmandam_arrow))
        self.play(Write(bazmandam))
        self.wait()

        self.play(Create(miandam_arrows))
        self.play(Write(miandam))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])


class FiveXPlusSixYPlusFourZ(Scene):
    def construct(self):

# INITS

        five_x_plus_six_y_plus_4_z = Tex('$5x$', ' $+$ ', '$6y$', ' $+$ ', '$4z$', font_size=70).shift(0.5 * LEFT)
        surr_rect_five_x_plus_six_y_plus_4_z = SurroundingRectangle(five_x_plus_six_y_plus_4_z, buff=MED_SMALL_BUFF)
        surr_rect_six_y = SurroundingRectangle(five_x_plus_six_y_plus_4_z[2], color=BLUE, corner_radius=0.25)
        surr_rect_five_x = SurroundingRectangle(five_x_plus_six_y_plus_4_z[0], color=BLUE, corner_radius=0.25)
        surr_rect_four_z = SurroundingRectangle(five_x_plus_six_y_plus_4_z[4], color=BLUE, corner_radius=0.25)
        surr_rect_five_x.stretch(1.2, 1).align_to(surr_rect_six_y, UP)
        surr_rect_four_z.stretch(1.2, 1).align_to(surr_rect_six_y, UP)

        bazmandam_arrow = Arrow(color=YELLOW).rotate(PI / 4).next_to(surr_rect_five_x_plus_six_y_plus_4_z, UR, buff=0)
        miandam_arrows = VGroup(
            Arrow(color=BLUE).rotate(- PI * 3 / 8).next_to(surr_rect_five_x, DOWN, buff=0).shift(0.2 * RIGHT),
            Arrow(color=BLUE).rotate(- PI * 4 / 8).next_to(surr_rect_six_y, DOWN, buff=0),
            Arrow(color=BLUE).rotate(- PI * 5 / 8).next_to(surr_rect_four_z, DOWN, buff=0).shift(0.2 * LEFT),
        )

        bazmandam = Tex('Բազմանդամ', tex_template=ARMTEX, font_size=60).next_to(bazmandam_arrow, UR, buff=0.2)
        miandam = Tex('Միանդամ', tex_template=ARMTEX, font_size=60).next_to(miandam_arrows, DOWN)



# ANIMATIONS

        self.play(Write(five_x_plus_six_y_plus_4_z))
        self.wait()

        self.play(Create(surr_rect_five_x_plus_six_y_plus_4_z))
        self.wait(0.25)
        self.play(Create(bazmandam_arrow))
        self.play(Write(bazmandam))
        self.wait()

        self.play(Create(surr_rect_five_x), Create(surr_rect_six_y), Create(surr_rect_four_z))
        self.wait()

        self.play(Create(miandam_arrows))
        self.play(Write(miandam))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])


class DefiningPolynomialAndMonomial(Scene): # unfinished
    def construct(self):

# INITS

    # 5x + 6y
        five_x_plus_six_y = Tex('$5x$', ' $+$ ', '$6y$', font_size=70)
        surr_rect_five_x_plus_six_y = SurroundingRectangle(five_x_plus_six_y, buff=MED_SMALL_BUFF)
        surr_rect_six_y_1 = SurroundingRectangle(five_x_plus_six_y[2], color=BLUE, corner_radius=0.25)
        surr_rect_five_x_1 = SurroundingRectangle(five_x_plus_six_y[0], color=BLUE, corner_radius=0.25)
        surr_rect_five_x_1.stretch(1.2, 1).align_to(surr_rect_six_y_1, UP)

        bazmandam_arrow_1 = Arrow(color=YELLOW).rotate(PI / 4).next_to(surr_rect_five_x_plus_six_y, UR, buff=0)
        miandam_arrows_1 = VGroup(
            Arrow(color=BLUE).rotate(- PI * 3 / 8).next_to(surr_rect_five_x_1, DOWN, buff=0).shift(0.2 * RIGHT),
            Arrow(color=BLUE).rotate(- PI * 5 / 8).next_to(surr_rect_six_y_1, DOWN, buff=0).shift(0.2 * LEFT)
        )

        bazmandam_1 = Tex('Բազմանդամ', tex_template=ARMTEX, font_size=60).next_to(bazmandam_arrow_1, UR)
        miandam_1 = Tex('Միանդամ', tex_template=ARMTEX, font_size=60).next_to(miandam_arrows_1, DOWN)


    # 5x + 6y + 4z
        five_x_plus_six_y_plus_4_z = Tex('$5x$', ' $+$ ', '$6y$', ' $+$ ', '$4z$', font_size=70).shift(0.5 * LEFT)
        surr_rect_five_x_plus_six_y_plus_4_z = SurroundingRectangle(five_x_plus_six_y_plus_4_z, buff=MED_SMALL_BUFF)
        surr_rect_six_y_2 = SurroundingRectangle(five_x_plus_six_y_plus_4_z[2], color=BLUE, corner_radius=0.25)
        surr_rect_five_x_2 = SurroundingRectangle(five_x_plus_six_y_plus_4_z[0], color=BLUE, corner_radius=0.25)
        surr_rect_four_z = SurroundingRectangle(five_x_plus_six_y_plus_4_z[4], color=BLUE, corner_radius=0.25)
        surr_rect_five_x_2.stretch(1.2, 1).align_to(surr_rect_six_y_2, UP)
        surr_rect_four_z.stretch(1.2, 1).align_to(surr_rect_six_y_2, UP)

        bazmandam_arrow_2 = Arrow(color=YELLOW).rotate(PI / 4).next_to(surr_rect_five_x_plus_six_y_plus_4_z, UR, buff=0)
        miandam_arrows_2 = VGroup(
            Arrow(color=BLUE).rotate(- PI * 3 / 8).next_to(surr_rect_five_x_2, DOWN, buff=0).shift(0.2 * RIGHT),
            Arrow(color=BLUE).rotate(- PI * 4 / 8).next_to(surr_rect_six_y_2, DOWN, buff=0),
            Arrow(color=BLUE).rotate(- PI * 5 / 8).next_to(surr_rect_four_z, DOWN, buff=0).shift(0.2 * LEFT),
        )

        bazmandam_2 = Tex('Բազմանդամ', tex_template=ARMTEX, font_size=60).next_to(bazmandam_arrow_2, UR, buff=0.2)
        miandam_2 = Tex('Միանդամ', tex_template=ARMTEX, font_size=60).next_to(miandam_arrows_2, DOWN)



# ANIMATIONS

        self.add(five_x_plus_six_y)
        self.wait()

        self.play(Create(surr_rect_five_x_1), Create(surr_rect_six_y_1))
        self.wait()
        self.play(Create(surr_rect_five_x_plus_six_y))
        self.wait(0.25)
        self.play(Create(bazmandam_arrow_1))
        self.play(Write(bazmandam_1))
        self.wait()

        self.play(Create(miandam_arrows_1))
        self.play(Write(miandam_1))
        self.wait()

        # self.play(FadeOut())

        self.play(*[FadeOut(mob) for mob in self.mobjects])


class DefinitionExamples(Scene):
    def construct(self):

# INITS
        sahmanum = VGroup(
            Tex('Միանդամը թվերի և տառերի արտադրյալ հանդիսացող', tex_template=ARMTEX),
            Tex('հանրահաշվական արտահայտությունն է։', tex_template=ARMTEX)
        )
        sahmanum[1].next_to(sahmanum[0], DOWN) #, aligned_edge=LEFT
        sahmanum.to_edge(UP)
        surr_rect_sahmanum = SurroundingRectangle(sahmanum)

        miandams_1 = VGroup(
            MathTex('2\cdot x'),
            Tex(','),
            MathTex('y\cdot 3\cdot d')
        ).arrange()
        miandams_2 = VGroup(
            MathTex('z'),
            Tex(','),
            MathTex('9'),
            Tex(','),
            MathTex('9\cdot z\cdot 9\cdot z')
        ).arrange()
        VGroup(
            miandams_1[1],
            miandams_2[1],
            miandams_2[3],
        ).shift(0.25 * DOWN)

        miandams_3 = VGroup(
            MathTex('0\cdot a\cdot 7'),
            Arrow().scale(0.75),
            Tex('Զրոյական միանդամ', tex_template=ARMTEX, font_size=37)
        ).arrange()

        miandams_4 = MathTex(r'\frac{5}{2}', r'\cdot', r'x')

        miandams = VGroup(miandams_1, miandams_2, miandams_3, miandams_4)
        miandams.arrange(DOWN, 0.35, aligned_edge=LEFT).to_edge(LEFT).shift(DOWN + 0.5 * RIGHT)

        is_miandam = Tex('Միանդամներ են', tex_template=ARMTEX)
        is_miandam.next_to(miandams, UP, buff=0.5, aligned_edge=LEFT)
        is_not_miandam = Tex('Միանդամներ չեն', tex_template=ARMTEX)
        is_not_miandam.align_to(is_miandam, UP).shift(RIGHT * 3.5)

        not_miandam_1 = MathTex('a', ' + ', 'b')
        not_miandam_1[1].set_color(RED)
        not_miandam_2 = MathTex(r'\frac{5}{a}\cdot x')

        not_miandams = VGroup(not_miandam_1, not_miandam_2)
        not_miandams.arrange(DOWN, buff=0.5).next_to(is_not_miandam, DOWN, buff=0.5)

        surr_rects_miandam_4 = VGroup(
            SurroundingRectangle(miandams_4[0]),
            SurroundingRectangle(miandams_4[2])
        )

        surr_rect_not_miandam_2 = Rectangle(color=YELLOW)
        surr_rect_not_miandam_2.move_to(not_miandam_2).shift([-0.35, -0.4, 0]).scale(0.11).stretch(1.75, 1)
        not_miandam_haytarar = MathTex(r'a', color=RED).move_to(not_miandam_2).shift([-0.35, -0.4, 0])


# ANIMATIONS

        self.play(Write(sahmanum[0], run_time=2.5))
        self.play(Write(sahmanum[1], run_time=1.5))
        self.play(Create(surr_rect_sahmanum))
        self.wait(0.25)

        self.play(Write(is_miandam))
        self.wait(0.25)

        self.play(Write(miandams_1[0]))
        self.wait(0.25)
        self.play(Write(miandams_1[1], run_time=0.5))
        self.play(Write(miandams_1[2]))
        self.wait(0.75)

        self.play(
            AnimationGroup(
               Write(miandams_2[0]),
               Write(miandams_2[1]),
               lag_ratio=0.75, run_time=0.75
            )
        )
        self.wait(0.1)
        self.play(
            AnimationGroup(
               Write(miandams_2[2]),
               Write(miandams_2[3]),
               lag_ratio=0.75, run_time=0.75
            )
        )
        self.wait(0.1)
        self.play(Write(miandams_2[4], run_time=2, rate_func=linear))
        self.wait()

        self.play(Write(miandams_3[0], run_time=1.75, rate_func=linear))
        self.wait()
        self.play(Write(miandams_3[1]))
        self.play(Write(miandams_3[2]))
        self.wait(0.25)

        self.play(Write(is_not_miandam))
        self.wait(0.25)

        self.play(Write(not_miandam_1))
        self.wait()

        self.play(Write(miandams_4))
        self.wait()

        self.play(Write(not_miandam_2))
        self.wait()

        self.play(Create(surr_rects_miandam_4))
        self.wait(0.5)
        self.play(FadeOut(surr_rects_miandam_4))
        self.wait(0.5)

        self.play(
            Create(surr_rect_not_miandam_2),
            FadeIn(not_miandam_haytarar)
        )
        self.wait(0.5)
        self.play(FadeOut(surr_rect_not_miandam_2))
        self.wait()

        self.remove(*self.mobjects)


class Miandam(Scene):
    def construct(self):
        RoadScene.construct(self)
        FiveXPlusSixY.construct(self)
        FiveXPlusSixYPlusFourZ.construct(self)
        DefinitionExamples.construct(self)

