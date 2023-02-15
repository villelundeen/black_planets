import os
import pygame as pg
from pygame.locals import *
import numpy as np

import projectile as pr
import constants as cs

def main():
    global running, screen

    print("Welcome to Black Planets Construction Site!")
    laser = pr.Projectile(pos=np.array([100, 100]),vel=np.array([1, 0.0]))
    laser.print_info()
    print(laser.get_pos())
    pg.init()
    
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()

    laser.render(screen, cs.BLUE)

    pg.display.update()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                    laser.render(screen, cs.RED)

            if event.type == pg.QUIT:
                running = False

            laser.update(cs.DELTA_T)  
            pg.display.update()

    #main_dir = os.path.split(os.path.abspath(__file__))[0]
    #data_dir = os.path.join(main_dir, "data")


if __name__ == "__main__":
    main()
