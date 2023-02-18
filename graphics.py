import constants as cs
from pygame import image as im
from pygame import transform as tr
from os import listdir
 

class Graphics_Stock():
    def __init__(self):
        self.planet_imgs = []
        for img_name in listdir("./figs"):
            if (img_name.endswith("planet.png")):
                img = im.load("./figs/" + img_name)
                self.planet_imgs.append(img)
        self.ufo_imgs = []
        self.projectile_imgs = []

graphics_stock = Graphics_Stock()