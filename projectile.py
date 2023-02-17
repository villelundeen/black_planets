import numpy as np
from body import Body
from planet import Planet
import constants as cs
import utils


class Projectile(Body):
    def __init__(self, mass=cs.PROJECTILE_RAD, rad=cs.PROJECTILE_RAD, pos=cs.PLAYER1_POS, vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
        super().__init__(rad,pos,ang)
        self.mass = mass
        self.vel = vel
        self.acc = acc


    def print_info(self):
        print(f"Mass: {self.mass}")
        print(f"Radius: {self.rad}")
        print(f"Position: {self.pos}")
        print(f"Velocity: {self.vel}")
        print(f"Acceleration: {self.acc}")
        print(f"Angle: {self.ang}")


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


    def update_motion(self, dt, planets):
        self.pos = self.pos + self.vel*dt + 0.5*self.acc*dt*dt
        new_acc = self.get_acc(planets)
        self.vel = self.vel + 0.5*(self.acc + new_acc)*dt
        self.acc = new_acc