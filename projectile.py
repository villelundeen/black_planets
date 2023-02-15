import numpy as np
from body import Body
from constants import PROJECTILE_RAD


class Projectile(Body):
  def __init__(self, mass=10, rad=PROJECTILE_RAD, pos=np.array([0.0, 0.0]), vel=np.array([0.0, 0.0]), acc=np.array([0.0, 0.0]), ang=0):
    super().__init__(mass,rad,pos,ang)
    self.vel = vel
    self.acc = acc


  def print_info(self):
    print(f"Mass: {self.mass}")
    print(f"Radius: {self.rad}")
    print(f"Position: {self.pos}")
    print(f"Velocity: {self.vel}")
    print(f"Acceleration: {self.acc}")
    print(f"Angle: {self.ang}")

  def get_acc(self) -> float:
      return 9.81

  def update(self, dt):
    self.pos = self.pos + self.vel*dt + self. acc*dt*dt
    new_acc = self.get_acc()
    self.vel = self.vel + 0.5*(self.acc + new_acc)*dt
    self.acc = new_acc