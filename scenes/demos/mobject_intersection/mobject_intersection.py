from manim import Scene
from manim import Line, Circle, Dot, Arc
from manim import UP, RIGHT, TAU
import numpy as np

from bezier import Curve


def intersection(m1, m2):
    for point in list(m1.points) + list(m2.points):
        if point[-1]:
            raise ValueError('Implemented for 2D only')
    ccurves = m1.get_cubic_bezier_tuples()
    lcurves = m2.get_cubic_bezier_tuples()

    points = []
    for (c1, c2, c3, c4) in ccurves:
        for (l1, l2, l3, l4) in lcurves:
            curve1 = Curve(np.asfortranarray([c1[:-1], c2[:-1], c3[:-1], c4[:-1]]).T, 3)
            curve2 = Curve(np.asfortranarray([l1[:-1], l2[:-1], l3[:-1], l4[:-1]]).T, 3)
            intersection_points = curve1.intersect(curve2)[0, :]
            for intersection_point in intersection_points:
                points.append(list(curve1.evaluate(intersection_point).flatten()) + [0])
    return points


class MobjectIntersectionDemo(Scene):
    def construct(self):
        objects = [Circle(radius=2), Circle(radius=1).shift(UP + RIGHT), Circle().shift(UP), Line([-2, 1, 0], [2, 1, 0]), Line([0, 1, 0], [1, 2, 0]),
                   Arc(radius=2, start_angle=TAU / 8, angle=TAU / 2)]

        for obj1 in objects:
            for obj2 in objects:
                if obj1 is obj2:
                    continue
                self.add(obj1, obj2)
                self.wait()
                dots = [Dot(point) for point in intersection(obj1, obj2)]
                self.add(*dots)
                self.wait()
                self.remove(*dots)
                self.remove(obj1, obj2)
                self.wait()
