from manim import ThreeDScene, Cube, Circle, FadeIn, VGroup, FadeOut, Cylinder
from manim import WHITE, RED_C
from manim import X_AXIS, Y_AXIS, Z_AXIS
from manim import PI
from numpy import array

SIDE_LENGTH = 5
RADIUS = SIDE_LENGTH / 7.4

class Dice(ThreeDScene):
    def construct(self):
        self.wait()
        
        cube = Cube(SIDE_LENGTH, fill_opacity=1, fill_color=RED_C)
        circle = Cylinder(RADIUS, height=0, fill_color=WHITE, fill_opacity=1)
        circle.set_opacity(1).move_to(cube.get_center())
        
        nist1 = circle.copy().shift(array([0, 0, SIDE_LENGTH/2]))
        nist2 = VGroup(
            circle.copy().shift(array([2.15*RADIUS, -2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, 2.15*RADIUS, 0]))
        ).rotate(PI/2, Y_AXIS).shift(array([-SIDE_LENGTH/2, 0, 0]))
        nist3 = VGroup(
            circle.copy(),
            circle.copy().shift(array([2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, -2.15*RADIUS, 0]))
        ).rotate(PI/2, X_AXIS).shift(array([0, SIDE_LENGTH/2, 0]))
        nist4 = VGroup(
            circle.copy().shift(array([2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([2.15*RADIUS, -2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, -2.15*RADIUS, 0]))
        ).rotate(PI/2, X_AXIS).shift(array([0, -SIDE_LENGTH/2, 0]))
        nist5 = VGroup(
            circle.copy(),
            circle.copy().shift(array([2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([2.15*RADIUS, -2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, -2.15*RADIUS, 0]))
        ).rotate(PI/2, Y_AXIS).shift(array([SIDE_LENGTH/2, 0, 0]))
        nist6 = VGroup(
            circle.copy().shift(array([2.15*RADIUS, 0, 0])),
            circle.copy().shift(array([-2.15*RADIUS, 0, 0])),
            circle.copy().shift(array([2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([2.15*RADIUS, -2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, 2.15*RADIUS, 0])),
            circle.copy().shift(array([-2.15*RADIUS, -2.15*RADIUS, 0]))
        ).shift(array([0, 0, -SIDE_LENGTH/2]))

        dice = VGroup(
            cube,
            nist1, nist2, nist3, nist4, nist5, nist6
        )

        self.set_camera_orientation(PI/4, PI/4, PI/4, .7)

        self.play(FadeIn(dice))
        self.wait()
        # self.play(dice.animate.rotate(PI, Y_AXIS))
        # self.begin_3dillusion_camera_rotation()
        self.begin_ambient_camera_rotation(.8)

        self.wait(6)
