import numpy as np
from body import Nonstatic_Body
from planet import Planet
import constants as cs
import utils


class Projectile(Nonstatic_Body):
    def __init__(self, mass=cs.PROJECTILE_RAD, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, vel, acc, ang)

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Velocity: {self.vel}")
        print(f"Acceleration: {self.acc}")
        print(f"Angle: {self.ang}")

