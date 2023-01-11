from manim import Scene
from manim import UP, DOWN, RIGHT, LEFT, UL, UR, GREEN, ORANGE
from manim import VGroup, MathTex, Tex
from manim import Write, Create, FadeIn, FadeOut, Transform, ReplacementTransform, Circumscribe
from manim import SurroundingRectangle, Circle
from objects import SimpleSVGMobject, Weight, Scales
from .text import goose_weight, duck_weight


"""
Երկրորդ լուծում

1․  ունենք 2 կշեռք
    առաջին կշեռքի ամեն ինչը բերում ենք 2-րդ կշեռքի վրա, ու առաջին կշեռքը անհետացնում

2․  աջ կողմում հաշվում ենք գումարային զանգվածը
    հետո ձախ նժարը բաժանում ենք 5 միանման խմբերի

3․  ստանում ենք որ 1 խմբի զանգվածը 2740 է, ու այն պատկերում ենք 3-րդ կշեռքի վրա

4․  հետո վերադառնում ենք առաջին կշեռքին, ունենալով 2 խումբ և 1 սագ
    խմբերը փոխարինում ենք կշռաքարերով, կրճատում ենք կշեռքի վրա, ու ստանում սագի քաշը

5․  ստանում ենք բադի քաշը
"""


class Problem11159_2Solution(Scene):
    def construct(self):


# INIT
    # scales 1 
        
        goose = SimpleSVGMobject('goose').scale(0.8)
        duck = SimpleSVGMobject('duck').scale(0.8)
        sc_1 = Scales(2.15).scale(0.8).shift(UP)

        sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.3).next_to(sc_1.left_plate, UP, buff=0)

        sc_1_right_mobs = VGroup(Weight(6700, 700))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)

    # scales 2
        sc_2 = Scales(2.15).scale(0.8).shift(2.5*DOWN)

        sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.3).next_to(sc_2.left_plate, UP, buff=0)
        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))
        

        sc_2_right_mobs = VGroup(Weight(7000, 600))
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_2 = VGroup(Weight(7000, 600), Weight(6700, 700))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_3 = Weight(13700, 400).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_4 = VGroup(Weight(2740, 300), Weight(2740, 300), Weight(2740, 300), Weight(2740, 300), Weight(2740, 300))
        sc_2_right_mobs_4.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

    # scales 3
        sc_3 = Scales(1).scale(0.6).shift(1.5*UL+0.5*LEFT)

        sc_3_left_mobs = VGroup(duck.copy(), goose.copy())
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(Weight(2740, 300))
        sc_3_right_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0))

        sc_3_left_mobs_1 = VGroup(duck.copy(), Weight(1220, 300))
        sc_3_left_mobs_1.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs_1.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs_1 = VGroup(Weight(1220, 300), Weight(1520, 300))
        sc_3_right_mobs_1.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs_1.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0))

    # scales 4 
        sc_4 = Scales(2.15).scale(0.8).shift(2.5*DOWN)

        sc_4_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_4_left_mobs.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.left_plate, UP, buff=0)

        sc_4_right_mobs = VGroup(Weight(6700, 700))
        sc_4_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_4.right_plate, UP, buff=0)

        sc_4_left_mobs_1 = VGroup(Weight(2740, 300), Weight(2740, 300), goose.copy())
        sc_4_left_mobs_1.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.left_plate, UP, buff=0)

        sc_4_right_mobs_1 = VGroup(Weight(2740, 300), Weight(3960, 300))
        sc_4_right_mobs_1.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.right_plate, UP, buff=0)

        sc_4_right_mobs_2 = VGroup(Weight(2740, 300), Weight(1220, 300))
        sc_4_right_mobs_2.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.right_plate, UP, buff=0)

    # Equations
        eq_1 = MathTex("7000 + 6700 = 13700").shift(3*UR+RIGHT)
        eq_2 = MathTex("13700 : 5 = 2740").next_to(eq_1, DOWN, buff=0.3)
        eq_3 = Tex(goose_weight).next_to(eq_2, DOWN, buff=1)
        eq_4 = Tex(duck_weight).next_to(eq_3, DOWN, buff=0.5)

        ans_box = SurroundingRectangle(VGroup(eq_3, eq_4), color=GREEN)


# ANIMATIONS

    # scales

        self.add(
            sc_1, sc_1_left_mobs, sc_1_right_mobs,
            sc_2, sc_2_left_mobs, sc_2_right_mobs
        )
        self.wait()

        self.play(
            Circumscribe(sc_1_left_mobs),
            Circumscribe(sc_2_left_mobs)
        )
        self.wait()
        
    # առաջին կշեռքն անհետանում է

        self.play(
            sc_1_left_mobs[0].animate.next_to(sc_2_left_mobs[0], UP, buff=0.1),
            sc_1_left_mobs[1].animate.next_to(sc_2_left_mobs[1], UP, buff=0.1),
            sc_1_left_mobs[2].animate.next_to(sc_2_left_mobs[2], UP, buff=0.1),
            sc_1_left_mobs[3].animate.next_to(sc_2_left_mobs[3], UP, buff=0.1),
            sc_1_left_mobs[4].animate.next_to(sc_2_left_mobs[4], UP, buff=0.1),
            sc_2_right_mobs.animate.move_to(sc_2_right_mobs_2[0]),
            sc_1_right_mobs.animate.move_to(sc_2_right_mobs_2[1]),
            FadeOut(sc_1)
        )
        self.wait()

        self.add(sc_2_right_mobs_2)
        self.remove(sc_1_right_mobs, sc_2_right_mobs)

        sc_1_left_mobs[0].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[0], UP, buff=0.1))
        sc_1_left_mobs[1].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[1], UP, buff=0.1))
        sc_1_left_mobs[2].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[2], UP, buff=0.1))
        sc_1_left_mobs[3].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[3], UP, buff=0.1))
        sc_1_left_mobs[4].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[4], UP, buff=0.1))

    # առաջին հարց և կշռաքարերի համապատասխան միավորում

        self.play(Write(eq_1))
        self.wait()

        self.play(ReplacementTransform(sc_2_right_mobs_2, sc_2_right_mobs_3))
        self.wait()

    # Ձախ նժարի վրա 5 խմբերի առանձնացում

        self.play(sc_2_left_mobs.animate.arrange(aligned_edge=DOWN, buff=0.5).next_to(sc_2.left_plate, UP, buff=0))
        self.wait()

# INIT
    # boxes
        box_0 = SurroundingRectangle(VGroup(sc_1_left_mobs[0], sc_2_left_mobs[0]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_1 = SurroundingRectangle(VGroup(sc_1_left_mobs[1], sc_2_left_mobs[1]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_2 = SurroundingRectangle(VGroup(sc_1_left_mobs[2], sc_2_left_mobs[2]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_3 = SurroundingRectangle(VGroup(sc_1_left_mobs[3], sc_2_left_mobs[3]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_4 = SurroundingRectangle(VGroup(sc_1_left_mobs[4], sc_2_left_mobs[4]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_5 = SurroundingRectangle(sc_3_left_mobs, color=ORANGE, corner_radius=0.3)

###

        self.play(
            Create(box_0),
            Create(box_1),
            Create(box_2),
            Create(box_3),
            Create(box_4)
        )
        self.wait()

        sc_1_left_mobs[0].clear_updaters()

        self.play(Write(eq_2))
        self.wait()

    # Երրորդ կշեռք

        self.play(ReplacementTransform(sc_2_right_mobs_3, sc_2_right_mobs_4))
        self.wait()

        self.play(FadeIn(sc_3))
        x = sc_1_left_mobs[0].copy()
        y = sc_2_left_mobs[0].copy()
        z = box_0.copy()
        t = sc_2_right_mobs_4[0].copy()
        self.play(
            x.animate.move_to(sc_3_left_mobs[0]),
            y.animate.move_to(sc_3_left_mobs[1]),
            Transform(z, box_5),
            t.animate.move_to(sc_3_right_mobs)
        )
        self.add(sc_3_left_mobs, sc_3_right_mobs, box_5)
        self.remove(x, y, z, t) # ֆսյո, էս x, y, z, t-ները էլ չկան, եթե ինչ
        self.wait()

        self.play(FadeOut(box_5))
        self.wait()

    # Չորրորդ (Առաջին) կշեռք

        self.play(
            FadeOut(sc_2),
            FadeOut(sc_2_left_mobs),
            FadeOut(sc_2_right_mobs_4),
            FadeOut(box_0),
            FadeOut(box_1),
            FadeOut(box_2),
            FadeOut(box_3),
            FadeOut(box_4),
            FadeOut(sc_1_left_mobs)
        )
        self.wait()

        self.play(
            FadeIn(sc_4),
            FadeIn(sc_4_left_mobs),
            FadeIn(sc_4_right_mobs)
        )
        self.wait()

        self.play(
            sc_4_left_mobs[1].animate.next_to(sc_4_left_mobs[3], LEFT, buff=0.4).align_to(sc_4_left_mobs[3], DOWN),
            sc_4_left_mobs[2].animate.next_to(sc_4_left_mobs[0], RIGHT, buff=0.4).align_to(sc_4_left_mobs[0], DOWN)
        )
        self.wait()

# INIT
    # box
        box_6 = SurroundingRectangle(VGroup(sc_4_left_mobs[0], sc_4_left_mobs[2]), color=ORANGE, corner_radius=0.3)
        box_7 = SurroundingRectangle(VGroup(sc_4_left_mobs[1], sc_4_left_mobs[3]), color=ORANGE, corner_radius=0.3)

###
        self.play(
            Create(box_6),
            Create(box_7)
        )
        self.wait()

    # Խմբերի փոխարինում կշռաքարերով
        
        self.play(ReplacementTransform(VGroup(box_6, sc_4_left_mobs[0], sc_4_left_mobs[2]), sc_4_left_mobs_1[0]))
        self.wait()

        self.play(ReplacementTransform(VGroup(box_7, sc_4_left_mobs[1], sc_4_left_mobs[3]), sc_4_left_mobs_1[1]))
        self.wait()

        self.play(sc_4_left_mobs[4].animate.move_to(sc_4_left_mobs_1[2]))
        self.add(sc_4_left_mobs_1[2])
        self.remove(sc_4_left_mobs[4])
        self.wait()

        self.play(ReplacementTransform(sc_4_right_mobs, sc_4_right_mobs_1))
        self.wait()

    # կշռաքարերի կրճատում

        self.play(
            sc_4_left_mobs_1[0].animate.shift(UP),
            sc_4_right_mobs_1[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_4_left_mobs_1[0]),
            FadeOut(sc_4_right_mobs_1[0])
        )
        self.wait()

        self.play(ReplacementTransform(sc_4_right_mobs_1[1], sc_4_right_mobs_2))
        self.wait()

        self.play(
            sc_4_left_mobs_1[1].animate.shift(UP),
            sc_4_right_mobs_2[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_4_left_mobs_1[1]),
            FadeOut(sc_4_right_mobs_2[0])
        )
        self.wait()

        self.play(
            sc_4_left_mobs_1[2].animate.next_to(sc_4.left_plate, UP, buff=0),
            sc_4_right_mobs_2[1].animate.next_to(sc_4.right_plate, UP, buff=0)
        )
        self.wait()

    # Սագի կշիռ
        
        self.play(Circumscribe(sc_4_left_mobs_1[2], Circle))
        self.wait()

        self.play(Circumscribe(sc_4_right_mobs_2[1], Circle))
        self.wait()

        self.play(Write(eq_3))
        self.wait()

    # Բադի կշիռ
        
        self.play(sc_3.animate.shift(0.5*DOWN))
        self.wait()

        self.play(Circumscribe(sc_3_left_mobs, Circle, time_width=2))
        self.wait()

        self.play(Circumscribe(sc_3_right_mobs, Circle, time_width=2))
        self.wait()

        self.play(ReplacementTransform(sc_3_right_mobs, sc_3_right_mobs_1))
        self.wait()

        sc_3_left_mobs.clear_updaters()
        sc_3_right_mobs_1.clear_updaters()

        self.play(
            sc_3_left_mobs[1].animate.shift(UP),
            sc_3_right_mobs_1[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_3_left_mobs[1]),
            FadeOut(sc_3_right_mobs_1[0])
        )
        self.wait()

        self.play(
            sc_3_left_mobs[0].animate.next_to(sc_3.left_plate, UP, buff=0),
            sc_3_right_mobs_1[1].animate.next_to(sc_3.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(Write(eq_4))
        self.wait()

        self.play(Create(ans_box))
        self.wait()
