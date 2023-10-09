from manim import *

class OneBoyOneGirl(Scene):
    def construct(self):

        # Write names of boys in on column and names of girls in other column
        boys = VGroup(
            Tex('Հայկ'),
            Tex('Արմեն'),
            Tex('Ռուբեն')
        )
        boys.arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(2 * LEFT).to_edge(UP)

        girls = VGroup(
            Tex('Անի'),
            Tex('Մանե'),
            Tex('Լիլիթ'),
            Tex('Էլեն')
        )
        girls.arrange(DOWN, aligned_edge=LEFT).shift(2 * RIGHT).to_edge(UP)
        boys.move_to([boys.get_center()[0], girls.get_center()[1], 0])

        self.add(boys, girls)
        self.wait()

        # define arrows pointing from boys to girls 
        arrows = VGroup(*[VGroup(*[Arrow(start=boy.get_right(), end=girl.get_left()) for girl in girls]) for boy in boys])
        arrows[0].set_color(RED)
        arrows[1].set_color(BLUE)
        arrows[2].set_color(ORANGE)

        # FIRST BOY
        # connect the boy to all the girls with arrows, copy all of that and move to bottom
        self.play(
            boys[1:].animate.set_opacity(0.3),
            boys[0].animate.set_color(RED)
        )
        self.wait()

        for arr in arrows[0]:
            self.play(GrowArrow(arr))
            self.wait(0.5)

        first_boy_copies = VGroup(*[boys[0].copy() for _ in range(4)])
        first_boy_copies.arrange(DOWN, aligned_edge=LEFT).match_height(girls).shift(2 * LEFT).to_edge(UP)
        first_arrows = VGroup(*[Arrow(start=first_boy_copies[i].get_right(), end=girls[i].get_left()) for i in range(4)])
        first_group = VGroup(first_boy_copies, first_arrows, girls.copy())
        first_group.scale(0.65).to_corner(DL, 0.75)
        surr_rect_1 = SurroundingRectangle(first_group, RED)

        self.play(ReplacementTransform(VGroup(boys[0], arrows[0], girls).copy(), first_group))
        self.wait()
        self.play(Create(surr_rect_1))
        self.wait()

        # SECOND BOY
        # connect the boy to all the girls with arrows, copy all of that and move to bottom
        self.play(
            FadeOut(arrows[0]),
            boys[0].animate.set_opacity(0.3),
            boys[1].animate.set_opacity(1).set_color(BLUE)
        )
        self.wait()

        for arr in arrows[1]:
            self.play(GrowArrow(arr))
            self.wait(0.5)

        second_boy_copies = VGroup(*[boys[1].copy() for _ in range(4)])
        second_boy_copies.arrange(DOWN, aligned_edge=LEFT).match_height(girls).shift(2 * LEFT).to_edge(UP)
        second_arrows = VGroup(*[Arrow(start=second_boy_copies[i].get_right(), end=girls[i].get_left()) for i in range(4)])
        second_group = VGroup(second_boy_copies, second_arrows, girls.copy())
        second_group.scale(0.65).to_edge(DOWN, 0.75)
        surr_rect_2 = SurroundingRectangle(second_group, BLUE)

        self.play(ReplacementTransform(VGroup(boys[1], arrows[1], girls).copy(), second_group))
        self.wait()
        self.play(Create(surr_rect_2))
        self.wait()

        # THIRD BOY
        # connect the boy to all the girls with arrows, copy all of that and move to bottom
        self.play(
            FadeOut(arrows[1]),
            boys[1].animate.set_opacity(0.3),
            boys[2].animate.set_opacity(1).set_color(ORANGE)
        )
        self.wait()

        for arr in arrows[2]:
            self.play(GrowArrow(arr))
            self.wait(0.5)

        third_boy_copies = VGroup(*[boys[2].copy() for _ in range(4)])
        third_boy_copies.arrange(DOWN, aligned_edge=LEFT).match_height(girls).shift(2 * LEFT).to_edge(UP)
        third_arrows = VGroup(*[Arrow(start=third_boy_copies[i].get_right(), end=girls[i].get_left()) for i in range(4)])
        third_group = VGroup(third_boy_copies, third_arrows, girls.copy())
        third_group.scale(0.65).to_corner(DR, 0.75)
        surr_rect_3 = SurroundingRectangle(third_group, ORANGE)

        self.play(ReplacementTransform(VGroup(boys[2], arrows[2], girls).copy(), third_group))
        self.wait()
        self.play(Create(surr_rect_3))
        self.wait()

        self.play(
            boys.animate.set_opacity(1),
            FadeOut(arrows[2])
        )

        # write 4 on each of the group and calculate their sum
        fours = VGroup(
            Tex('$4$', color=RED, font_size=70).next_to(first_group, UP),
            Tex('$4$', color=BLUE, font_size=70).next_to(second_group, UP),
            Tex('$4$', color=ORANGE, font_size=70).next_to(third_group, UP)
        )
        for four in fours:
            self.play(Write(four))
            self.wait(0.5)

        calculation = Tex('$4$', '$+$', '$4$', '$+$', '$4$', ' $=$ ', '$3$', '$\cdot$', '$4$', ' $=$ ', '$12$', font_size=55)
        calculation.next_to(VGroup(boys, girls), DOWN, buff=0.75)

        self.play(
            ReplacementTransform(fours[0].copy(), calculation[0]),
            ReplacementTransform(fours[1].copy(), calculation[2]),
            ReplacementTransform(fours[2].copy(), calculation[4]),
            Write(calculation[1]),
            Write(calculation[3])
        )
        self.wait()

        for tex in calculation[5:]:
            self.play(Write(tex, run_time=0.75))
            self.wait(0.5)

        self.play(FadeOut(calculation[:6]))
        self.wait()
        self.play(boys.animate.set_color(WHITE))
        self.wait()
