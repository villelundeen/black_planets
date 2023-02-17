import numpy as np
import pygame as pg

class Body():
    def __init__(self, rad=1, pos=np.array([0.0, 0.0]), ang=0):
        self.rad = rad
        self.pos = pos
        self.ang = ang

    def __del__(self):
        return

    def print_info(self):
        print(f"Position: {self.pos}")
        print(f"Angle: {self.ang}")

    def get_pos(self):
        return self.pos

    def get_rad(self):
        return self.rad

    def too_close_to_planet(self, planets) -> bool:
        for planet in planets:
            pos = planet.get_pos()
            rad = planet.get_rad()
            dist = np.sqrt(((pos[0] - self.pos[0]) * (pos[0] - self.pos[0])) + ((pos[1] - self.pos[1]) * (pos[1] - self.pos[1])))
            if dist <= self.rad + rad:
                return True
        return False

    def render(self, screen, color):
        pg.draw.circle(screen, color, self.get_pos(), self.get_rad())


class Massless_Body(Body):
    def __init__(self, rad=3, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad, pos, ang)