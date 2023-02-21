import numpy as np
from body import Rotating_Body
import constants as cs
from pygame import image as im
from pygame import transform as tr
import utils
import random as rand


class Wormhole(Rotating_Body):
    def __init__(self, rad=cs.WORMHOLE_INNER_RAD, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad, pos, ang)
        self.img = im.load("./figs/wormhole.png")
        self.img = tr.scale(self.img, (2*cs.WORMHOLE_OUTER_RAD,2*cs.WORMHOLE_OUTER_RAD))
        self.img_ang = 0        # degrees
        self.rot_vel = 1        # degrees/tick
        self.rotation_matrix = utils.get_rotation_matrix(rand.random() * 2 * np.pi)


    def print_info(self):
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def render(self, screen):
        """ Wormholes rotate """
        self.img_ang = (self.img_ang + 2 * self.rot_vel) % (360)
        rot_img = tr.rotate(self.img, self.img_ang)
        new_rect = rot_img.get_rect(center = self.img.get_rect(topleft = self.get_pos() - np.array([cs.WORMHOLE_OUTER_RAD, cs.WORMHOLE_OUTER_RAD])).center)
        screen.blit(rot_img, new_rect)

        """
        # This own rotation is not working for some reason.
        rot_img = tr.rotate(self.img, 180*self.img_ang/np.pi)
        d = 2*cs.WORMHOLE_OUTER_RAD
        print(f"Angle: {2*self.img_ang}")
        a = abs(np.sin(2*self.img_ang)*d)
        b = abs(np.cos(2*self.img_ang)*d)
        offset = ((a + b) - d)/2
        print(f"{tuple(self.pos - np.array([cs.WORMHOLE_OUTER_RAD - offset, cs.WORMHOLE_OUTER_RAD - offset]))}")
        screen.blit(rot_img, tuple(self.pos - np.array([cs.WORMHOLE_OUTER_RAD - offset, cs.WORMHOLE_OUTER_RAD - offset])))
        """
        """
        # Found online, not working
        orig_rect = self.img.get_rect()
        rot_img = tr.rotate(self.img, self.img_ang)
        rot_rect = orig_rect.copy()
        rot_rect.center = orig_rect.center
        rot_img = rot_img.subsurface(rot_rect).copy()
        screen.blit(rot_img, rot_rect)
        """
        """
        # Not working
        rot_image = tr.rotate(self.img, self.img_ang)
        rot_rect = rot_image.get_rect(center=self.img.get_rect().center)
        screen.blit(rot_img, rot_rect)
        """