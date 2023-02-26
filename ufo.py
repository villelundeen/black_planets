import numpy as np
from body import Moving_Body
import constants as cs
from pygame import image as im
from pygame import transform as tr
from powerbar import Powerbar

class UFO(Moving_Body):
    def __init__(self, mass=cs.UFO_MASS, \
                    rad=cs.UFO_RAD, \
                        pos=cs.PLAYER1_POS - np.array([-cs.UFO_RAD, -cs.UFO_RAD]), \
                            vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), \
                                ang=0, \
                                    lives=3):
        super().__init__(mass, rad, pos, vel, acc, ang)
        self.shot_power = (cs.MIN_SHOT_POWER + cs.MAX_SHOT_POWER)/2
        self.img = im.load("./figs/ufo.png")
        self.img = tr.scale(self.img, (2*cs.UFO_RAD,2*cs.UFO_RAD))
        self.lives = lives
        self.powerbar = Powerbar(self)

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")
        print(f"Shot power: {self.shot_power}")

    def render(self, screen):
        screen.blit(self.img, tuple(self.pos - np.array([self.rad, self.rad])))

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
        if self.shot_power < cs.MAX_SHOT_POWER:
            self.shot_power += cs.SHOT_POWER_INCREMENT

    def decrease_shot_power(self):
        if self.shot_power > cs.MIN_SHOT_POWER:
            self.shot_power -= cs.SHOT_POWER_INCREMENT

    def get_shot_power(self):
        return self.shot_power

    def get_shot_direction(self):
        ux = np.cos(self.ang)
        uy = -np.sin(self.ang)
        return np.array([ux,uy])

    def get_life_count(self):
        return self.lives

    def lose_life(self):
        self.lives -= 1

    def convert_img(self):
        self.img = self.img.convert()