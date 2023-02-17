import numpy as np

def get_distance(point1, point2) -> float:
    dist = np.sqrt(((point2[0] - point1[0]) * (point2[0] - point1[0])) + ((point2[1] - point1[1]) * (point2[1] - point1[1])))
    return dist