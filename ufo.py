import numpy as np
from body import Body
import constants as cs


class UFO(Body):
    def __init__(self, mass=cs.UFO_MASS, rad=cs.UFO_RAD, pos=cs.PLAYER1_POS, ang=0):
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