from pygame import image as im
from pygame import transform as tr
from os import listdir
 

class Graphics():
    def __init__(self):
        self.planet_imgs = []
        for img_name in listdir("./figs"):
            if (img_name.endswith("planet.png")):
                img = im.load("./figs/" + img_name)
                self.planet_imgs.append(img)
        self.ufo_imgs = []
        self.projectile_imgs = []
        self.font = "./fonts/Freedom-10eM.ttf"


graphics = Graphics()