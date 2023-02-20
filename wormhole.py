import numpy as np
from body import Massive_Body


class Wormhole(Massive_Body):
    def __init__(self, mass=100, rad=3, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)

    def print_info(self):
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")
