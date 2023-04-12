from manim import ThreeDScene, Cube, Circle, FadeIn, VGroup, FadeOut
from manim import WHITE, RED_C
from manim import X_AXIS, Y_AXIS
from manim import PI
from numpy import array

SIDE_LENGTH = 5
RADIUS = SIDE_LENGTH / 6.4

class Dice(ThreeDScene):
    def construct(self):
        self.wait()
        
        cube = Cube(SIDE_LENGTH, fill_opacity=1, fill_color=RED_C)
        circle = Circle(RADIUS, WHITE)
        circle.set_opacity(1).move_to(cube.get_center())
        
        nist1 = circle.copy().shift(array([0, 0, SIDE_LENGTH/2]))
        nist2 = VGroup(
            circle.copy().shift(array([2.25*RADIUS, -2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, 2.25*RADIUS, 0]))
        ).rotate(PI/2, Y_AXIS).shift(array([-SIDE_LENGTH/2, 0, 0]))
        nist3 = VGroup(
            circle.copy(),
            circle.copy().shift(array([2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, -2.25*RADIUS, 0]))
        ).rotate(PI/2, X_AXIS).shift(array([0, SIDE_LENGTH/2, 0]))
        nist4 = VGroup(
            circle.copy().shift(array([2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([2.25*RADIUS, -2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, -2.25*RADIUS, 0]))
        ).rotate(PI/2, X_AXIS).shift(array([0, -SIDE_LENGTH/2, 0]))
        nist5 = VGroup(
            circle.copy(),
            circle.copy().shift(array([2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([2.25*RADIUS, -2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, -2.25*RADIUS, 0]))
        ).rotate(PI/2, Y_AXIS).shift(array([SIDE_LENGTH/2, 0, 0]))
        nist6 = VGroup(
            circle.copy().shift(array([2.25*RADIUS, 0, 0])),
            circle.copy().shift(array([-2.25*RADIUS, 0, 0])),
            circle.copy().shift(array([2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([2.25*RADIUS, -2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, 2.25*RADIUS, 0])),
            circle.copy().shift(array([-2.25*RADIUS, -2.25*RADIUS, 0]))
        ).shift(array([0, 0, -SIDE_LENGTH/2+.001]))

        dice = VGroup(
            cube,
            nist1, nist2, nist3, nist4, nist5, nist6
        )

        # cube.set_z_index(nist6.z_index+1)
        # nist1.set_z_index(cube.z_index+1)
        # cube.set_z_index_by_z_coordinate()
        # nist1.set_z_index_by_z_coordinate()
        # nist2.set_z_index_by_z_coordinate()
        # nist3.set_z_index_by_z_coordinate()
        # nist4.set_z_index_by_z_coordinate()
        # nist5.set_z_index_by_z_coordinate()
        # nist6.set_z_index_by_z_coordinate()

        self.play(FadeIn(dice))
        self.wait()
        self.play(dice.animate(run_time=9).rotate(PI/2, Y_AXIS))

        # self.play(FadeIn(cube))
        # self.play(FadeIn(nist1))
        # self.play(FadeOut(nist1))
        # self.wait(1.5)
        # self.play(FadeIn(nist2))
        # self.play(FadeOut(nist2))
        # self.wait(1.5)
        # self.play(FadeIn(nist3))
        # self.play(FadeOut(nist3))
        # self.wait(1.5)
        # self.play(FadeIn(nist4))
        # self.play(FadeOut(nist4))
        # self.wait(1.5)
        # self.play(FadeIn(nist5))
        # self.play(FadeOut(nist5))
        # self.wait(1.5)
        # self.play(FadeIn(nist6))
        # self.play(FadeOut(nist6))
        # self.wait(1.5)

        self.wait(2)
