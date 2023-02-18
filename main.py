import os
import pygame as pg
from pygame.locals import *
import numpy as np

import constants as cs
import world

def main():
    # Let's get to it
    print("Welcome to Black Planets Construction Site!")

    pg.init()
    clk = pg.time.Clock()
    wd = world.World(n_planet=5,n_wormhole=0)

    wd.projectile.stop_motion()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()
    
    wd.ufo1.render(screen)
    wd.ufo2.render(screen)
    for planet in wd.planets:
        planet.render(screen)

    pg.display.update()

    running = True
    shot_moving = False
    inside_bounds = True
    ufo1_turn = True
    last_tick = 0
    last_shot_tick = 0
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
                        shot_moving = True
                        wd.projectile.enable_motion()
                        if ufo1_turn:
                            shot_vector = wd.ufo1.get_shot_direction() * wd.ufo1.get_shot_power()
                        else:
                            shot_vector = wd.ufo2.get_shot_direction() * wd.ufo2.get_shot_power()
                        wd.projectile.set_vel(shot_vector)
                        last_shot_tick = pg.time.get_ticks()
                        if ufo1_turn:
                            ufo1_turn = False
                        else:
                            ufo1_turn = True

            if keys[pg.K_LEFT] or keys[pg.K_a]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufo1.enable_rotation()
                    wd.ufo1.rotate_positive()
                    wd.ufo1.disable_rotation()
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufo1.enable_rotation()
                    wd.ufo1.rotate_negative()
                    wd.ufo1.disable_rotation()
            if keys[pg.K_UP] or keys[pg.K_w]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufo1.enable_power_tuning()
                    wd.ufo1.increase_shot_power()
                    wd.ufo1.disable_power_tuning()
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufo1.enable_power_tuning()
                    wd.ufo1.decrease_shot_power()
                    wd.ufo1.disable_power_tuning()

        outside_bounds = wd.projectile.get_pos()[0] < -0.2*cs.WINDOW_W or \
                        wd.projectile.get_pos()[0] > 1.2*cs.WINDOW_W or \
                        wd.projectile.get_pos()[1] < -0.2*cs.WINDOW_H or \
                        wd.projectile.get_pos()[1] > 1.2*cs.WINDOW_H
        hit_planet = wd.projectile.too_close_to_planet(wd.planets, min_dist=0)
        if (pg.time.get_ticks() - last_shot_tick > cs.HIT_ACTIVATION_DELAY) and shot_moving:
            hit_ufo1 = wd.projectile.hit_ufo(wd.ufo1)
            hit_ufo2 = wd.projectile.hit_ufo(wd.ufo2)
        else:
            hit_ufo1 = False
            hit_ufo2 = False

        if outside_bounds or hit_planet or hit_ufo1 or hit_ufo2:

            if hit_ufo1:
                wd.ufo1.lose_life()
                print("UFO 1 lost a life!")
                if wd.ufo1.get_life_count() <= 0:
                    print("UFO 1 ran out of lives!")
                    continue
            if hit_ufo2:
                wd.ufo2.lose_life()
                print("UFO 2 lost a life!")
                if wd.ufo2.get_life_count() <= 0:
                    print("UFO 2 ran out of lives!")
                    continue
            
            wd.projectile.stop_motion()
            shot_moving = False
            if ufo1_turn:
                wd.projectile.set_pos(cs.PLAYER1_POS)
            else:
                wd.projectile.set_pos(cs.PLAYER2_POS)
            wd.projectile.update_motion(cs.DELTA_T, wd.planets)
            wd.projectile.render(screen, cs.RED)
            wd.ufo1.render(screen)
            wd.ufo2.render(screen)
            pg.display.update()
        
        if shot_moving:
            screen.fill(cs.BLACK)
            wd.projectile.update_motion(cs.DELTA_T, wd.planets)
            wd.projectile.render(screen, cs.RED)
            wd.ufo1.render(screen)
            wd.ufo2.render(screen)
            for planet in wd.planets:
                planet.render(screen)
            pg.display.update()

        else:
            screen.fill(cs.BLACK)
            wd.projectile.render(screen, cs.RED)
            wd.ufo1.render(screen)
            wd.ufo2.render(screen)
            for planet in wd.planets:
                planet.render(screen)
            pg.display.update()
        
        clk.tick(cs.FPS)

    pg.quit()
    quit()


if __name__ == "__main__":
    main()
