import numpy as np
import random as rand
from body import Massive_Body
import constants as cs
from pygame import image as im
from pygame import transform as tr
from graphics import graphics_stock as gr



class Planet(Massive_Body):
    def __init__(self, mass=1000, rad=30, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)
        img_idx = rand.randint(0, len(gr.planet_imgs)-1)
        self.img = gr.planet_imgs[img_idx]
        self.img = tr.scale(self.img, (2*self.rad,2*self.rad))

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def render(self, screen):
        screen.blit(self.img, tuple(self.pos - np.array([self.rad, self.rad])))
