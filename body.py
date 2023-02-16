import numpy as np
import pygame as pg

class Body():
    def __init__(self, rad=1, pos=np.array([0.0, 0.0]), ang=0):
        self.rad = rad
        self.pos = pos
        self.ang = ang

    def print_info(self):
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def get_pos(self):
        return self.pos

    def get_radius(self):
        return self.rad

    def render(self, screen, color):
        pg.draw.circle(screen, color, self.get_pos(), self.get_radius())