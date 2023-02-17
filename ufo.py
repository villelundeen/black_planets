import numpy as np
from body import Body


class Ufo(Body):
    def __init__(self, mass=1000, rad=30, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)
        self.mass = mass
        self.alive = True


    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def get_mass(self):
        return self.mass