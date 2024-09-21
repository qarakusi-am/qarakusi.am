import numpy as np
from manim import PI, TAU
from manim import ORANGE, BLACK, BLUE
from manim import ORIGIN, X_AXIS, Y_AXIS, Z_AXIS
from manim import VGroup, MathTex, AnnularSector, Point, Cube


def length(array):
    return np.linalg.norm(array)


def normalized_vector(array):
    return np.array(array) / length(array)


def rotate2angle(array, alpha):
    rotation__matrix = [
        [np.cos(alpha), -np.sin(alpha), 0],
        [np.sin(alpha), np.cos(alpha), 0],
        [0, 0, 1],
    ]
    return np.matmul(rotation__matrix, np.array(array))


def normal_vector(array):
    return normalized_vector(rotate2angle(np.array(array), PI/2))


def getFractionsOnCircle(fraction, circle, color=ORANGE, number_of_sectors=1, stroke_width=5, stroke_color=BLACK, numbering=False, numbering_font_size=None, start_angle=0):
    """make sure your circle has the same stroke_width and stroke_color as your sectors"""

    sectors = VGroup()
    if numbering:
        numbers = VGroup()
    
    radius = circle.radius
    angle = TAU * fraction
    if numbering and numbering_font_size is None:
        numbering_font_size = radius * 44
    
    coordinates = circle.get_center()
    circle.move_to(ORIGIN)

    for sector_number in range(number_of_sectors):
        sector = AnnularSector(
            inner_radius=0,
            outer_radius=radius,
            angle=angle,
            start_angle=sector_number*angle+start_angle,
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            color=color
        )
        sectors.add(sector)
        if numbering:
            number = MathTex(f"{sector_number+1}", font_size=numbering_font_size)
            coord = np.array([radius, 0, 0])*2/3
            point = Point().move_to(coord)
            point.rotate(sector_number*angle+angle/2+start_angle, about_point=circle.get_center())
            number.move_to(point.get_center())
            numbers.add(number)

    to_coordinates = VGroup(sectors, circle)
    if numbering:
        to_coordinates.add(numbers)
    to_coordinates.move_to(coordinates)

    if numbering:
        return VGroup(sectors, numbers)
    else:
        return sectors

def minecraft(matrix, side_length=2, fill_opacity=1, stroke_width=1, stroke_color=BLUE, stroke_opacity=1, **kwargs) -> VGroup:
    """
    Creates 3D objects using Cubes (Warning! Adjust light_source and shading_factor of ThreeDCamera to cover the flaws of 3D graphics of Manim)
    
    (Demo is in 'scenes/demo/minecraft/minecraft.py')

    arr = [
        [
            [0, 1],
            [1, 1]
        ],
        [
            [0, 1],
            [1, 1]
        ]
    ]

    obj = minecraft(arr, fill_color=BLUE).rotate(-PI/10, X_AXIS).rotate(-PI/10, Y_AXIS)

    """
    obj = VGroup()
    for z, layer in enumerate(matrix):
        for y, raw in enumerate(layer):
            for x, val in enumerate(raw):
                if val:
                    cube = Cube(side_length=side_length,
                                fill_opacity=fill_opacity,
                                stroke_width=stroke_width,
                                stroke_color=stroke_color,
                                stroke_opacity=stroke_opacity,
                                **kwargs)
                    cube.shift(x*(side_length)*X_AXIS, -y*(side_length)*Y_AXIS, -z*(side_length)*Z_AXIS)
                    obj.add(cube)
                else:
                    pass

    return obj.move_to(ORIGIN)
