from manim import UP, DOWN, RIGHT, LEFT, UL, UR, GREEN, ORANGE
from manim import VGroup, MathTex, Tex
from manim import Write, FadeIn, FadeOut, ReplacementTransform, Circumscribe
from manim import Dot
from objects import SimpleSVGMobject, Weight, Scales
from .text import first, second, goose_weight, duck_weight
from scales import ScalesScene
import numpy as np



"""
Առաջին լուծում

1.  խնդիրը համառոտագրել

2.  2 կշեռք

    առաջինի 
        ձախին - 3 սագ, 2 բադ
        աջին - 6700 գ
    
    երկրորդ 
        ձախին - 2 սագ, 3 բադ
        աջին - 7000 գ

3․  circumscribe 2 բադերն ու 2 սագերը ու հետո մի քիչ ձախ տանել
    circumscribe 1 բադ ու 1 սագ ու հետո մի քիչ աջ տանել

4․  7000-6700=300

5․  երրորդ կշեռք
    ձախին - 1 բադ
    աջին - 1 սագ և 300 գ
    
6․  երկրորդ կշեռքը ֆեյդ-աութ
    երրորդ կշեռքը գալիս ա ձախ

7․  առաջին կշեռքում 1 բադը սաքրում ենք սագ+300
    
8․  2 նժարներից հանում ենք 600

9․  3-րդ հարց

10․ 4-րդ հարց
"""

class Problem11159_1Solution(ScalesScene):
    def construct(self):

# INIT
   # scales 1 

        goose = SimpleSVGMobject('goose').scale(0.8)
        duck = SimpleSVGMobject('duck').scale(0.8)
        sc_1 = Scales(2.15).scale(0.7).shift(0.3*UP+0.5*RIGHT)

        sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_1.left_plate, UP, buff=0)

        sc_1_ducks = VGroup(*sc_1_left_mobs[:2]).copy()
        sc_1_geese = VGroup(*sc_1_left_mobs[2:]).copy()
        sc_1_ducks.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[0:2], LEFT))
        sc_1_geese.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[2:], LEFT))

        sc_1_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0))

        sc_1_right_mobs = VGroup(Weight(6700, 600))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))

        sc_1_right_mobs_2 = VGroup(Weight(6100, 600), Weight(600, 150))
        sc_1_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))

    # scales 2
        sc_2 = Scales(2.15).scale(0.7).shift(3*DOWN+0.5*RIGHT)

        sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.05).next_to(sc_2.left_plate, UP, buff=0)

        sc_2_geese = VGroup(*sc_2_left_mobs[:2]).copy()
        sc_2_ducks = VGroup(*sc_2_left_mobs[2:]).copy()
        sc_2_geese.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0).align_to(sc_2_left_mobs[:2], LEFT))
        sc_2_ducks.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0).align_to(sc_2_left_mobs[2:], LEFT))

        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))

        sc_2_right_mobs = VGroup(Weight(7000, 600))
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

        sc_2_right_mobs_2 = VGroup(Weight(6700, 600), Weight(300, 150))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

    # Equations

        eq_1 = MathTex("7000 - 6700 =", " 300", font_size=48).shift([4.5, 3, 0])
        eq_2 = MathTex("6700 - 600 = 6100", font_size=48).shift([4, 1, 0]).align_to(eq_1, LEFT)
        eq_3 = MathTex("6100 : 5 = 1220", font_size=48).next_to(eq_2, DOWN, buff=0.5).align_to(eq_2, LEFT)
        eq_4 = MathTex("1220 + 300 = 1520", font_size=48).next_to(eq_3, DOWN, buff=0.5).align_to(eq_3, LEFT)

    # scales 3
        sc_3 = Scales(1.2).scale(0.5).shift(4.15 * RIGHT + 0.5 * DOWN)

        sc_3_left_mobs = duck.copy()
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(goose.copy(), Weight(300, 150))
        sc_3_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0)) 

    # Given

        first_1 = Tex(*first, font_size=48)
        first_1.shift(3 * UP + 1.85 * LEFT)
        second_2 = Tex(*second, font_size=48)
        second_2.next_to(sc_1, DOWN, buff=0.1)
        second_2.align_to(first_1, LEFT)


# ANIMATION

        self.wait()

    # Համառոտագրություն

        self.play(Write(first_1))
        self.wait()

        self.play(Write(second_2))
        self.wait()

    # 2 կշեռքներով հավասարություններ

        self.play(FadeIn(sc_1), FadeIn(sc_2))
        self.wait()
        
        x = first_1[0].copy()
        self.play(x.animate.move_to(sc_1_geese))
        self.play(ReplacementTransform(x, sc_1_geese))
        self.rotate_scales(sc_1, 0.4)
        self.wait()

        y = first_1[2].copy()
        self.play(y.animate.move_to(sc_1_ducks.get_center() - np.array([0, 0.25, 0])))
        self.play(ReplacementTransform(y, sc_1_ducks))
        self.rotate_scales(sc_1, 0.4)
        self.wait()

        self.play(ReplacementTransform(first_1[5].copy(), sc_1_right_mobs))
        self.rotate_scales(sc_1, -0.8)
        self.remove(sc_1_ducks, sc_1_geese)
        self.add(sc_1_left_mobs)
        self.wait()

        x = second_2[0].copy()
        self.play(x.animate.move_to(sc_2_geese))
        self.play(ReplacementTransform(x, sc_2_geese))
        self.rotate_scales(sc_2, 0.4)
        self.wait()

        y = second_2[2].copy()
        self.play(y.animate.move_to(sc_2_ducks.get_center() - np.array([0, 0.25, 0])))
        self.play(ReplacementTransform(y, sc_2_ducks))
        self.rotate_scales(sc_2, 0.4)
        self.wait()

        self.play(ReplacementTransform(second_2[5].copy(), sc_2_right_mobs))
        self.rotate_scales(sc_2, -0.8)
        self.remove(sc_2_ducks, sc_2_geese)
        self.add(sc_2_left_mobs)
        self.wait()

        self.play(
            FadeOut(first_1),
            FadeOut(second_2),
            sc_1.animate.shift(2.35 * LEFT + 0.5 * UP),
            sc_2.animate.shift(2.35 * LEFT)
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[0:4]), Circumscribe(sc_2_left_mobs[0:4]))
        self.play(
            sc_1_left_mobs[0:4].animate.shift(0.2*LEFT),
            sc_2_left_mobs[0:4].animate.shift(0.2*LEFT)
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[4]), Circumscribe(sc_2_left_mobs[4]))
        self.play(
            sc_1_left_mobs[4].animate.shift(0.2*RIGHT),
            sc_2_left_mobs[4].animate.shift(0.2*RIGHT)
        )
        self.wait()

    # Սագը փոխարինում ենք սագով

# INIT

    # scale
        sc_2_right_mobs_2 = VGroup(Weight(6700, 600), Weight(300, 150))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN, buff=0.6).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

        kshraqar = sc_2_right_mobs_2[1].copy()

        

        sc_1_birds = sc_1_left_mobs[0:4].copy()
        sc_1_birds.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[0:4], LEFT))

        duck = sc_2_left_mobs[4].copy()
        goose = sc_1_left_mobs[4].copy()

# ANIMATIONS

        self.play(sc_1_left_mobs.animate.shift(0.0001 * UP))
        self.add(goose, sc_1_birds)
        self.remove(sc_1_left_mobs)

        self.play(goose.animate.shift(UP))
        self.play(goose.animate.shift(0.8 * RIGHT).set_opacity(0.5))
        self.wait()

        self.play(duck.animate.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_2_left_mobs[4], RIGHT))
        self.wait()

        duck.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_2_left_mobs[4], RIGHT))
        self.add(sc_1_birds)

        self.rotate_scales(sc_1, 0.25)
        self.wait()

        self.play(
            Write(eq_1),
            ReplacementTransform(sc_2_right_mobs, sc_2_right_mobs_2),
            run_time=2
        )

        self.play(kshraqar.animate.next_to(sc_1_right_mobs, RIGHT, aligned_edge=DOWN))
        self.wait()

        kshraqar.add_updater(lambda x: x.align_to(sc_1_right_mobs, DOWN))
        
        self.rotate_scales(sc_1, -0.25)
        self.wait()

        self.play(
            goose.animate.shift(0.8 * LEFT +DOWN).set_opacity(1),
            FadeOut(duck, kshraqar)
        )
        self.wait()

        self.play(sc_1_left_mobs.animate.shift(0.0001 * DOWN))
        self.add(sc_1_left_mobs)
        self.remove(goose, sc_1_birds)

    # Երրորդ կշեռք
    
        self.play(FadeIn(sc_3))
        self.play(FadeIn(sc_3_left_mobs))

        self.add(sc_3_right_mobs)
        sc_3_right_mobs.set_opacity(0)

        self.rotate_scales(sc_3, 0.8)

        self.play(sc_3_right_mobs[0].animate.set_opacity(1))    
        

        self.rotate_scales(sc_3, -0.4)
        
        self.play(sc_3_right_mobs[1].animate.set_opacity(1))

        self.rotate_scales(sc_3, -0.4)
        self.wait()

    # Երկրորդ կշեռքը ֆեյդ աութ

        self.play(
            FadeOut(sc_2),
            FadeOut(sc_2_left_mobs),
            FadeOut(sc_2_right_mobs_2)
        )
        self.wait()
            
        self.play(
            sc_3.animate.next_to(sc_1, DOWN, buff=2),
            sc_1_left_mobs[0:4].animate.shift(0.2*RIGHT),
            sc_1_left_mobs[4].animate.shift(0.2*LEFT)
        )
        self.wait()

        sc_3_right_mobs.clear_updaters()

    # Բադը փոխարինում ենք սագ+300-ով

        self.play(
            Circumscribe(sc_1_left_mobs[0]),
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )
        x = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[0].get_center()+0.15*LEFT).align_to(sc_1_left_mobs[2], DOWN)
        a = Dot(radius=0).move_to(x.get_center())
        y = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[1].get_center()+0.15*RIGHT).align_to(sc_1_left_mobs[2], DOWN)
        b = Dot(radius=0).move_to(y.get_center())
        self.play(
            ReplacementTransform(sc_1_left_mobs[0], a),
            ReplacementTransform(a, x)
        )
        self.wait()

        self.play(
            Circumscribe(sc_1_left_mobs[1]),
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )
        self.play(
            ReplacementTransform(sc_1_left_mobs[1], b),
            ReplacementTransform(b, y),
            sc_1_left_mobs[2:].animate.shift(0.3*RIGHT)
        )
        self.wait()

    # Երկրորդ հարց

        self.play(Write(eq_2))
        self.wait()

    # 600, 300-նոցները հանում ենք

        self.play(ReplacementTransform(sc_1_right_mobs, sc_1_right_mobs_2))
        self.play(
            x[1].animate.shift(UP * 0.5),
            y[1].animate.shift(UP * 0.5),
            sc_1_right_mobs_2[1].animate.shift(UP * 0.5)
        )
        self.play(
            FadeOut(x[1]),
            FadeOut(y[1]),
            FadeOut(sc_1_right_mobs_2[1])
        )
        self.play(
            sc_1_right_mobs_2[0].animate.next_to(sc_1.right_plate, UP, buff=0),
            sc_1_left_mobs[2:].animate.next_to(y[0], RIGHT, buff=0.1),
            x[0].animate.next_to(y[0], LEFT, buff=0.1)
        )
        self.wait()

        self.play(Write(eq_3))
        self.wait()

        self.play(
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )

        self.play(Write(eq_4))
        self.wait()
