import numpy as np
from body import Body


class Planet(Body):
  def __init__(self, mass=10, rad=30, pos=np.array([0.0, 0.0]), ang=0):
    super().__init__(mass, rad, pos, ang)

  def print_info(self):
    print(f"Mass: {self.mass}")
    print(f"Radius: {self.rad}")
    print(f"Position: {self.pos}")
    print(f"Angle: {self.ang}")