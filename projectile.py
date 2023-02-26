import numpy as np
from body import Moving_Body
from planet import Planet
import constants as cs
import utils
import pygame as pg


class Projectile(Moving_Body):
    def __init__(self, mass=cs.PROJECTILE_MASS, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, vel, acc, ang)
        self.trace_points = []

    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Velocity: {self.vel}")
        print(f"Acceleration: {self.acc}")
        print(f"Angle: {self.ang}")

    def hit_ufo(self, ufo):
        pos = ufo.get_pos()
        rad = ufo.get_rad()
        dist = utils.get_distance(pos, self.pos)
        if dist < self.rad + rad:
            return True
        return False
    
    def add_trace_point(self, point):
        self.trace_points.append(point)

    def get_trace_points(self):
        return self.trace_points
    
    def clear_traces(self):
        self.trace_points = []
    
    def render_traces(self, screen):
        for point in self.trace_points:
            pg.draw.circle(screen, cs.TRACE_COLOR, point, cs.TRACE_WIDTH)

    #def convert_img(self):
    #    self.img = self.img.convert()