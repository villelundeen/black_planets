import constants as cs
import planet as pl
import wormhole as wh
import random as rand
import numpy as np

class World():
    def __init__(self, n_planet, n_wormhole):
        self.planets = []
        for i in range(n_planet):
            rand_x = 300 #rand.random()*cs.WINDOW_H
            rand_y = 300 #rand.random()*cs.WINDOW_W
            rand_rad = 30 #rand.randrange(cs.MIN_PLANET_RAD, cs.MAX_PLANET_RAD)
            rand_mass = 1e3 #(4/3*np.pi*rand_rad*rand_rad*rand_rad) * cs.PLANET_DENSITY
            self.planets.append(pl.Planet(mass=rand_mass, rad=rand_rad, pos=np.array([rand_x,rand_y])))
        self.wormhole = []
        for i in range(n_wormhole):
            rand_x = 300 #rand.random()*cs.WINDOW_H
            rand_y = 300 #rand.random()*cs.WINDOW_W
            rand_rad = 30 #rand.randrange(cs.MIN_PLANET_RAD, cs.MAX_PLANET_RAD)
            self.wormhole.append(wh.Wormhole(mass=rand_mass, rad=rand_rad, pos=np.array([rand_x,rand_y])))

    def print_info(self):
        print("This is the Universe")
