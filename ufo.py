import numpy as np
from body import Nonstatic_Body
import constants as cs


class UFO(Nonstatic_Body):
    def __init__(self, mass=cs.UFO_MASS, rad=cs.UFO_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, vel, acc, ang)

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def get_mass(self):
        return self.mass