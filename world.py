import constants as cs
import planet as pl
import projectile as pr
import wormhole as wh
import ufo
import random as rand
import numpy as np
import utils

class World():
    def __init__(self, n_planet, n_wormhole_pairs):
        self.planets = []
        self.wormholes = []
        self.generate_planets(n_planet)
        self.generate_wormhole_pairs(n_wormhole_pairs)
        self.projectile0 = None
        self.projectile1 = None
        self.generate_projectiles()
        self.projectiles = [self.projectile0, self.projectile1]
        self.ufo0 = None
        self.ufo1 = None
        self.generate_ufos()
        self.ufos = [self.ufo0, self.ufo1]


    def __del__(self):
        return


    def print_info(self):
        print("This is the Universe")


    def generate_planets(self, n_planet):

        for planet in self.planets:
            del planet

        self.planets = []
        planet_pos_and_rad = []
        wormhole_pos = []
        for wormhole in self.wormholes:
            wormhole_pos.append(wormhole.get_pos())
        fails = 0
        max_fails = 100
        success = True
        while len(self.planets) < n_planet and fails <= max_fails:
            rand_x = rand.random()*0.8*cs.WINDOW_W + 0.1*cs.WINDOW_W
            rand_y = rand.random()*0.8*cs.WINDOW_H + 0.1*cs.WINDOW_H
            rand_rad = rand.randrange(cs.MIN_PLANET_RAD, cs.MAX_PLANET_RAD)
            for position, rad in planet_pos_and_rad:  
                dist = utils.get_distance(np.array([rand_x, rand_y]), position)
                if dist < (rand_rad + rad + cs.PLANET_MIN_SEPARATION):
                    if fails < max_fails:
                        fails += 1
                        success = False
                        print("Failed")
                        break
                    else:
                        return
            for position in wormhole_pos:  
                dist = utils.get_distance(np.array([rand_x, rand_y]), position)
                if dist < (cs.WORMHOLE_OUTER_RAD + rand_rad + cs.PLANET_MIN_SEPARATION):
                    if fails < max_fails:
                        fails += 1
                        success = False
                        print("Failed")
                        break
                    else:
                        return
            
            if success:
                planet_pos_and_rad.append(((np.array([rand_x, rand_y])), rand_rad))
                rand_mass = (4/3*np.pi*rand_rad*rand_rad*rand_rad) * cs.PLANET_DENSITY
                self.planets.append(pl.Planet(mass=rand_mass, rad=rand_rad, pos=np.array([rand_x,rand_y]))) 
            else:
                success = True
            

        if fails > max_fails:
            print("Too many tries required to create all the planets!")

    def generate_wormhole_pairs(self, n_wormhole_pairs):
        wormhole_idx = 0
        current_pair = [None, None]
        for wormhole_pair in self.wormholes:
            del wormhole_pair[0]
            del wormhole_pair[1]

        self.wormhole = []
        wormhole_pos = []
        planet_pos_and_rad = []
        for planet in self.planets:
            planet_pos_and_rad.append((planet.get_pos(), planet.get_rad()))

        fails = 0
        max_fails = 100
        success = True
        while len(self.wormholes) < n_wormhole_pairs and fails <= max_fails:
            rand_x = rand.random()*0.8*cs.WINDOW_W + 0.1*cs.WINDOW_W
            rand_y = rand.random()*0.8*cs.WINDOW_H + 0.1*cs.WINDOW_H
            orad = cs.WORMHOLE_OUTER_RAD
            irad = cs.WORMHOLE_INNER_RAD
            for position in wormhole_pos:  
                dist = utils.get_distance(np.array([rand_x, rand_y]), position)
                if dist < (2*orad + cs.WORMHOLE_MIN_SEPARATION):
                    if fails < max_fails:
                        fails += 1
                        success = False
                        print("Failed")
                        break
                    else:
                        return
            for position, rad in planet_pos_and_rad:  
                dist = utils.get_distance(np.array([rand_x, rand_y]), position)
                if dist < (orad + rad + cs.WORMHOLE_MIN_SEPARATION):
                    if fails < max_fails:
                        fails += 1
                        success = False
                        print("Failed")
                        break
                    else:
                        return
            if success:
                wormhole_idx = (wormhole_idx + 1) % 2
                wormhole_pos.append((np.array([rand_x, rand_y])))
                current_pair[wormhole_idx] = wh.Wormhole(rad=irad, pos=np.array([rand_x,rand_y]))
                if wormhole_idx == 0:
                    self.wormholes.append(current_pair.copy()) 
                    current_pair[0] = None
                    current_pair[1] = None
            else:
                success = True

        if fails > max_fails:
            print("Too many tries required to create all the wormholes!")


    def get_planets(self):
        return self.planets


    def get_wormholes(self):
        return self.wormholes


    def generate_ufos(self):
        self.ufo0 = ufo.UFO(pos=cs.PLAYER1_POS)
        self.ufo1 = ufo.UFO(pos=cs.PLAYER2_POS, ang=np.pi)

    
    def generate_projectiles(self):
        self.projectile0 = pr.Projectile(pos=cs.PLAYER1_POS)
        self.projectile1 = pr.Projectile(pos=cs.PLAYER2_POS)

