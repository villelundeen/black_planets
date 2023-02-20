import numpy as np
from body import Rotating_Body
import constants as cs
from pygame import image as im
from pygame import transform as tr


class Wormhole(Rotating_Body):
    def __init__(self, mass=1000, rad=cs.WORMHOLE_INNER_RAD, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)
        self.img = im.load("./figs/wormhole.png")
        self.img = tr.scale(self.img, (2*cs.WORMHOLE_OUTER_RAD,2*cs.WORMHOLE_OUTER_RAD))
        self.img_ang = 0
        self.angle_change = 0

    def print_info(self):
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def render(self, screen):
        self.img_ang += 20*np.pi/180
        rot_img = tr.rotate(self.img, self.img_ang)
        screen.blit(rot_img, tuple(self.pos - np.array([cs.WORMHOLE_OUTER_RAD, cs.WORMHOLE_OUTER_RAD])))