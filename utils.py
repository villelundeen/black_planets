import numpy as np
import constants as cs
import random as rand


def get_distance(point1, point2) -> float:
    dist = np.sqrt(((point2[0] - point1[0]) * (point2[0] - point1[0])) + ((point2[1] - point1[1]) * (point2[1] - point1[1])))
    return dist


def inside_keepout_zone():
    return


def get_random_unit_vector() -> np.ndarray:
    ux2 = rand.random()
    uy2 = 1- ux2
    signx = rand.randrange(-1,1.2)
    signy = rand.randrange(-1,1.2)
    ux = signx*np.sqrt(ux2)
    uy = signy*np.sqrt(uy2)

    return np.array([ux, uy])

def get_rotation_matrix(ang):
    return np.array([[np.cos(ang), -np.sin(ang)],[np.sin(ang), np.cos(ang)]])
