from manim import FadeIn, Cube, ThreeDScene, VGroup
from manim import BLUE, PI, Y_AXIS, X_AXIS
from utilities import minecraft

class MinecraftTest(ThreeDScene):
    """
    Demo for minecraft() function

    minecraft() creates 3D objects using cubes
    """
    def construct(self):
        # Adjust light_source and shading_factor of ThreeDCamera to cover the flaws of 3D graphics of Manim

        # self.camera.light_source = Point(np.array([5, 5, -5]))
        self.camera.shading_factor = .2
        self.camera.should_apply_shading = True

        arr0 = [
            [
                [0, 1],
                [1, 1]
            ],
            [
                [0, 1],
                [1, 1]
            ]
        ]

        arr1 = [
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]
        ]

        obj = minecraft(arr0, fill_color=BLUE).rotate(-PI/10, X_AXIS).rotate(-PI/10, Y_AXIS)

        self.play(FadeIn(obj))
        self.wait(5)
        self.play(obj.animate.rotate(PI/3, Y_AXIS))
        
        self.wait(15)
