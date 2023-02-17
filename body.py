import numpy as np
import pygame as pg
import constants as cs
import utils



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

    def too_close_to_planet(self, planets, min_dist) -> bool:
        for planet in planets:
            pos = planet.get_pos()
            rad = planet.get_rad()
            dist = np.sqrt(((pos[0] - self.pos[0]) * (pos[0] - self.pos[0])) + ((pos[1] - self.pos[1]) * (pos[1] - self.pos[1])))
            if dist <= self.rad + rad + min_dist:
                return True

    def too_close_to_wormhole(self, wormholes, min_dist) -> bool:
        for wormhole in wormholes:
            pos = wormhole.get_pos()
            rad = wormhole.get_rad()
            dist = np.sqrt(((pos[0] - self.pos[0]) * (pos[0] - self.pos[0])) + ((pos[1] - self.pos[1]) * (pos[1] - self.pos[1])))
            if dist <= self.rad + rad + min_dist:
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

    

class Nonstatic_Body(Massive_Body):
    def __init__(self, mass=cs.PROJECTILE_RAD, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(mass, rad, pos, ang)
        self.vel = vel
        self.acc = acc
        self.motion_enabled = False

    def get_acc(self, planets):
        acc = np.array([0.0, 0.0])
        for planet in planets:
            mass = planet.get_mass()
            pos = planet.get_pos()
            dist = utils.get_distance(pos, self.pos) #np.sqrt(((pos[0] - self.pos[0]) * (pos[0] - self.pos[0])) + ((pos[1] - self.pos[1]) * (pos[1] - self.pos[1])))   
            u_vec = (pos - self.pos)/dist
            grav = u_vec * cs.G_CONST*(mass*self.mass)/(dist*dist)
            acc += grav/self.mass
        return acc

    def set_pos(self, pos=np.array([0.0, 0.0])):
        self.pos = pos

    def set_vel(self, vel=np.array([0.0, 0.0])):
        self.vel = vel

    def set_acc(self, acc=np.array([0.0, 0.0])):
        self.acc = acc

    def stop_motion(self):
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])

    def enable_motion(self):
        self.motion_enabled = True

    def disable_motion(self):
        self.motion_enabled = False

    def update_motion(self, dt, planets):
        if self.motion_enabled == True:
            self.pos = self.pos + self.vel*dt + 0.5*self.acc*dt*dt
            new_acc = self.get_acc(planets)
            self.vel = self.vel + 0.5*(self.acc + new_acc)*dt
            self.acc = new_acc