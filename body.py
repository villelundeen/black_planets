import numpy as np
import pygame as pg
import constants as cs
import utils
import random as rand


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

    def get_ang(self):
        return self.ang

    def too_close_to_planet(self, planets, min_dist) -> bool:
        for planet in planets:
            pos = planet.get_pos()
            rad = planet.get_rad()
            dist = utils.get_distance(pos, self.pos)
            if dist <= self.rad + rad + min_dist:
                return True
        return False

    def too_close_to_wormhole(self, wormholes, min_dist) -> bool:
        for wormhole_pair in wormholes:
            pos0 = wormhole_pair[0].get_pos()
            rad0 = wormhole_pair[0].get_rad()
            dist0 = utils.get_distance(pos0, self.pos)
            pos1 = wormhole_pair[1].get_pos()
            rad1 = wormhole_pair[1].get_rad()
            dist1 = utils.get_distance(pos1, self.pos)
            if dist0 <= self.rad + cs.WORMHOLE_OUTER_RAD + min_dist:
                return True
            elif dist1 <= self.rad + cs.WORMHOLE_OUTER_RAD + min_dist:
                return True
        return False

    def render(self, screen, color):
        pg.draw.circle(screen, color, self.get_pos(), self.get_rad())



class Massless_Body(Body):
    def __init__(self, rad=3, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad, pos, ang)



class Massive_Body(Body):
    def __init__(self, mass=100, rad=3, pos=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad, pos, ang)
        self.mass = mass

    def get_mass(self):
        return self.mass



class Rotating_Body(Massless_Body):
    def __init__(self, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, ang=0):
        super().__init__(rad, pos, ang)
    
    def set_ang(self, new_ang):
        self.ang = new_ang

    def enable_rotation(self):
        self.rotation_enabled = True

    def disable_rotation(self):
        self.rotation_enabled = False

    def update_rotation(self, angle_increment):
        self.ang += angle_increment



class Moving_Body(Massive_Body, Rotating_Body):
    def __init__(self, mass=1000, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)
        self.vel = vel
        self.acc = acc
        self.motion_enabled = False
        self.power_tuning_enabled = False

    def get_acc(self, planets):
        acc = np.array([0.0, 0.0])
        for planet in planets:
            mass = planet.get_mass()
            pos = planet.get_pos()
            dist = utils.get_distance(pos, self.pos)
            u_vec = (pos - self.pos)/dist
            grav = u_vec * cs.G_CONST*(mass*self.mass)/(dist*dist)
            acc += grav/self.mass
        return acc

    def set_pos(self, pos=np.array([0.0, 0.0])):
        self.pos = pos

    def set_vel(self, vel=np.array([0.0, 0.0])):
        self.vel = vel

    def get_vel(self):
        return self.vel

    def set_acc(self, acc=np.array([0.0, 0.0])):
        self.acc = acc

    def stop_motion(self):
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])

    def enable_motion(self):
        self.motion_enabled = True

    def disable_motion(self):
        self.motion_enabled = False

    def enable_power_tuning(self):
        self.power_tuning_enabled = True

    def disable_power_tuning(self):
        self.power_tuning_enabled = False

    def update_motion(self, dt, planets):
        if self.motion_enabled == True:
            self.pos = self.pos + self.vel*dt + 0.5*self.acc*dt*dt
            new_acc = self.get_acc(planets)
            self.vel = self.vel + 0.5*(self.acc + new_acc)*dt
            self.acc = new_acc

    def teleport_if_in_wormhole(self, wormholes) -> bool:
        for wormhole_pair in wormholes:
            pos0 = wormhole_pair[0].get_pos()
            rad0 = wormhole_pair[0].get_rad()
            dist0 = utils.get_distance(pos0, self.pos)
            pos1 = wormhole_pair[1].get_pos()
            rad1 = wormhole_pair[1].get_rad()
            dist1 = utils.get_distance(pos1, self.pos)
            if dist0 <= self.rad + rad0:
                self.set_pos(wormhole_pair[1].get_pos())
                self.set_vel(np.dot(wormhole_pair[1].rotation_matrix, self.get_vel()))
                return True
            elif dist1 <= self.rad + rad1:
                self.set_pos(wormhole_pair[0].get_pos())
                self.set_vel(np.dot(wormhole_pair[0].rotation_matrix, self.get_vel()))
                return True
        return False