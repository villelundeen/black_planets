import numpy as np
from body import Nonstatic_Body
import constants as cs


class UFO(Nonstatic_Body):
    def __init__(self, mass=cs.UFO_MASS, rad=cs.UFO_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, vel, acc, ang)
        self.shot_power = (cs.MIN_SHOT_POWER + cs.MAX_SHOT_POWER)/2

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")
        print(f"Shot power: {self.shot_power}")

    def get_mass(self):
        return self.mass

    def rotate_positive(self):
        if self.rotation_enabled == True:
            self.ang += cs.UFO_ANGULAR_RESOLUTION
        else:
            print("Rotation not enabled")

    def rotate_negative(self):
        if self.rotation_enabled == True:
            self.ang -= cs.UFO_ANGULAR_RESOLUTION
        else:
            print("Rotation not enabled")
        
    def increase_shot_power(self):
        self.shot_power += cs.SHOT_POWER_INCREMENT

    def decrease_shot_power(self):
        self.shot_power -= cs.SHOT_POWER_INCREMENT

    def get_shot_power(self):
        return self.shot_power

    def get_shot_direction(self):
        ux = np.cos(self.ang)
        uy = -np.sin(self.ang)
        return np.array([ux,uy])

    