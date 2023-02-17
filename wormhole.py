import numpy as np
from body import Body


class Wormhole(Body):
    def __init__(self, rad=3, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad, pos, ang)

    def print_info(self):
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")
