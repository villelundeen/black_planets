import numpy as np


class Form():
    def __init__(self, pos=np.array([0.0, 0.0]), ang=0):
        self.pos = pos
        self.ang = ang