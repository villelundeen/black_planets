import os
import pygame as pg
from pygame.locals import *
import numpy as np

import projectile as pr
import constants as cs
import world as wd

def main():
    # Let's get to it
    print("Welcome to Black Planets Construction Site!")
    # Important to init pygame
    pg.init()
    # Init game clock that is used to limit the FPS of the game
    clk = pg.time.Clock()
    # Create the World, i.e., planets, wormholes, and ufos.
    world = wd.World(n_planet=1,n_wormhole=0)

    world.projectile.stop_motion()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()
    
    world.projectile.render(screen, cs.BLUE)

    pg.display.update()

    running = True
    moving = False
    inside_bounds = True
    while running:
        #pg.time.delay(10)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if inside_bounds:
            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                moving = True
                world.projectile.set_vel(np.array([1.5,-0.5]))
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                world.projectile.set_vel(np.array([-1,0]))
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                world.projectile.set_vel(np.array([1,0]))
            if keys[pg.K_UP] or keys[pg.K_w]:
                world.projectile.set_vel(np.array([0,-1]))
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                world.projectile.set_vel(np.array([0,1]))
        
        if world.projectile.get_pos()[0] < -0.2*cs.WINDOW_W or world.projectile.get_pos()[0] > 1.2*cs.WINDOW_W or world.projectile.get_pos()[1] < -0.2*cs.WINDOW_H or world.projectile.get_pos()[1] > 1.2*cs.WINDOW_H:
            world.projectile.stop_motion()
            moving = False
            world.projectile.set_pos(np.array([100,100]))
            screen.fill(cs.BLACK)
            world.projectile.update_motion(cs.DELTA_T, world.planets)
            world.projectile.render(screen, cs.RED)
            pg.display.update()
            clk.tick(cs.FPS)
        if moving:
            screen.fill(cs.BLACK)
            world.projectile.update_motion(cs.DELTA_T, world.planets)
            world.projectile.render(screen, cs.RED)
            pg.display.update()
            clk.tick(cs.FPS)

    #main_dir = os.path.split(os.path.abspath(__file__))[0]
    #data_dir = os.path.join(main_dir, "data")
    pg.quit()
    quit()


if __name__ == "__main__":
    main()
