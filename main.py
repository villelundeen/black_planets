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
    clk = pg.time.Clock()
    
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()

    laser.render(screen, cs.BLUE)

    pg.display.update()

    running = True
    while running:
        pg.time.delay(10)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            laser.stop_motion()
            laser.set_vel(np.array([-1,0]))
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            laser.stop_motion()
            laser.set_vel(np.array([1,0]))
        if keys[pg.K_UP] or keys[pg.K_w]:
            laser.stop_motion()
            laser.set_vel(np.array([0,-1]))
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            laser.stop_motion()
            laser.set_vel(np.array([0,1]))

        screen.fill(cs.BLACK)
        laser.update_motion(cs.DELTA_T)
        laser.render(screen, cs.RED)
        pg.display.update()
        clk.tick(cs.FPS)

    #main_dir = os.path.split(os.path.abspath(__file__))[0]
    #data_dir = os.path.join(main_dir, "data")
    pg.quit()
    quit()

if __name__ == "__main__":
    main()
