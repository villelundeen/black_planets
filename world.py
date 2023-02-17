import constants as cs
import planet as pl
import projectile as pr
import wormhole as wh
import random as rand
import numpy as np

class World():
    def __init__(self, n_planet, n_wormhole):
        self.planets = []
        self.wormholes = []
        self.projectile = None

        self.generate_planets(n_planet)
        self.generate_wormholes(n_wormhole)
        self.generate_projectile()


    def __del__(self):
        return


    def print_info(self):
        print("This is the Universe")


    def generate_planets(self, n_planet):

        for planet in self.planets:
            del planet

        self.planets = []
        for i in range(n_planet):
            rand_x = 300 #rand.random()*cs.WINDOW_H
            rand_y = 300 #rand.random()*cs.WINDOW_W
            rand_rad = 30 #rand.randrange(cs.MIN_PLANET_RAD, cs.MAX_PLANET_RAD)
            rand_mass = 1e3 #(4/3*np.pi*rand_rad*rand_rad*rand_rad) * cs.PLANET_DENSITY
            self.planets.append(pl.Planet(mass=rand_mass, rad=rand_rad, pos=np.array([rand_x,rand_y])))
        

    def generate_wormholes(self, n_wormhole):
        
        for wormhole in self.wormholes:
            del wormhole

        self.wormhole = []
        for i in range(n_wormhole):
            rand_x = 300 #rand.random()*cs.WINDOW_H
            rand_y = 300 #rand.random()*cs.WINDOW_W
            rand_rad = 30 #rand.randrange(cs.MIN_PLANET_RAD, cs.MAX_PLANET_RAD)
            rand_ang = 0 #rand.random()*2*np.pi
            self.wormhole.append(wh.Wormhole(rad=rand_rad, pos=np.array([rand_x,rand_y]), ang=rand_ang))


    def get_planets(self):
        return self.planets


    def get_wormholes(self):
        return self.wormholes


    def generate_ufos(self):
        self.ufos = []

    
    def generate_projectile(self):
        self.projectile = pr.Projectile(pos=np.array([100, 100]),vel=np.array([1, 0.0]))