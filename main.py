import os
import pygame as pg
from pygame.locals import *
import numpy as np

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
    world = wd.World(n_planet=5,n_wormhole=0)

    world.projectile.stop_motion()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()
    
    world.projectile.render(screen, cs.BLUE)
    world.ufo1.render(screen, cs.WHITE)
    world.ufo2.render(screen, cs.WHITE)
    for planet in world.planets:
        planet.render(screen, cs.GREEN)

    pg.display.update()

    running = True
    shot_moving = False
    inside_bounds = True
    last_tick = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if inside_bounds:
            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                if shot_moving == False:
                    if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                        last_tick = pg.time.get_ticks()

                        print(f"Shot_angle in degrees: {world.ufo1.ang/np.pi*180}")
                        print(f"Shot_angle in radians: {world.ufo1.ang}")
                        print(f"Angular resolution: {cs.UFO_ANGULAR_RESOLUTION}")

                        shot_moving = True
                        world.projectile.enable_motion()
                        shot_vector = world.ufo1.get_shot_direction() * world.ufo1.get_shot_power()
                        world.projectile.set_vel(shot_vector)
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        world.ufo1.enable_rotation()
                    world.ufo1.rotate_positive()
                    world.ufo1.disable_rotation()
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        world.ufo1.enable_rotation()
                    world.ufo1.rotate_negative()
                    world.ufo1.disable_rotation()
            if keys[pg.K_UP] or keys[pg.K_w]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        world.ufo1.enable_power_tuning()
                    world.ufo1.increase_shot_power()
                    world.ufo1.disable_power_tuning()
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        world.ufo1.enable_power_tuning()
                    world.ufo1.decrease_shot_power()
                    world.ufo1.disable_power_tuning()


        outside_bounds = world.projectile.get_pos()[0] < -0.2*cs.WINDOW_W or \
                        world.projectile.get_pos()[0] > 1.2*cs.WINDOW_W or \
                        world.projectile.get_pos()[1] < -0.2*cs.WINDOW_H or \
                        world.projectile.get_pos()[1] > 1.2*cs.WINDOW_H

        hit_planet = world.projectile.too_close_to_planet(world.planets, min_dist=0)

        if outside_bounds or hit_planet:
            
            world.projectile.stop_motion()
            shot_moving = False
            world.projectile.set_pos(cs.PLAYER1_POS)
            #screen.fill(cs.BLACK)
            world.projectile.update_motion(cs.DELTA_T, world.planets)
            world.projectile.render(screen, cs.RED)
            world.ufo1.render(screen, cs.WHITE)
            world.ufo2.render(screen, cs.WHITE)
            pg.display.update()
            clk.tick(cs.FPS)
        
        if shot_moving:
            screen.fill(cs.BLACK)
            world.projectile.update_motion(cs.DELTA_T, world.planets)
            world.projectile.render(screen, cs.RED)
            world.ufo1.render(screen, cs.WHITE)
            world.ufo2.render(screen, cs.WHITE)
            for planet in world.planets:
                planet.render(screen, cs.GREEN)
            pg.display.update()
            clk.tick(cs.FPS)

        else:
            screen.fill(cs.BLACK)
            world.projectile.render(screen, cs.RED)
            for planet in world.planets:
                planet.render(screen, cs.GREEN)
            pg.display.update()
            clk.tick(cs.FPS)

    pg.quit()
    quit()


if __name__ == "__main__":
    main()
