import numpy as np
from manim import PI


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
