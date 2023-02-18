import numpy as np
import constants as cs


def get_distance(point1, point2) -> float:
    dist = np.sqrt(((point2[0] - point1[0]) * (point2[0] - point1[0])) + ((point2[1] - point1[1]) * (point2[1] - point1[1])))
    return dist


def inside_keepout_zone():
    return
