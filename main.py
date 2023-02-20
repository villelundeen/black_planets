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
    wd = world.World(n_planet=5,n_wormhole_pairs=1)

    wd.projectile0.stop_motion()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    pg.display.set_caption("Black Planets")
    screen.fill(cs.BLACK)
    pg.display.update()
    
    wd.ufo0.render(screen)
    wd.ufo1.render(screen)
    for planet in wd.planets:
        planet.render(screen)
    for wormhole_pair in wd.wormholes:
        wormhole_pair[0].render(screen)
        wormhole_pair[1].render(screen)

    pg.display.update()

    running = True
    shot_moving = False
    inside_bounds = True
    last_tick = 0
    last_shot_tick = 0
    last_teleport_tick = 0
    player_idx = 0
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
                        wd.projectiles[player_idx].enable_motion()
                        shot_vector = wd.ufos[player_idx].get_shot_direction() * wd.ufos[player_idx].get_shot_power()
                        wd.projectiles[player_idx].set_vel(shot_vector)
                        last_shot_tick = pg.time.get_ticks()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufos[player_idx].enable_rotation()
                    wd.ufos[player_idx].rotate_positive()
                    wd.ufos[player_idx].disable_rotation()
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufos[player_idx].enable_rotation()
                    wd.ufos[player_idx].rotate_negative()
                    wd.ufos[player_idx].disable_rotation()
            if keys[pg.K_UP] or keys[pg.K_w]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufos[player_idx].enable_power_tuning()
                    wd.ufos[player_idx].increase_shot_power()
                    wd.ufos[player_idx].disable_power_tuning()
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                    last_tick = pg.time.get_ticks()
                    if shot_moving == False:
                        wd.ufos[player_idx].enable_power_tuning()
                    wd.ufos[player_idx].decrease_shot_power()
                    wd.ufos[player_idx].disable_power_tuning()

        outside_bounds = wd.projectiles[player_idx].get_pos()[0] < -0.2*cs.WINDOW_W or \
                        wd.projectiles[player_idx].get_pos()[0] > 1.2*cs.WINDOW_W or \
                        wd.projectiles[player_idx].get_pos()[1] < -0.2*cs.WINDOW_H or \
                        wd.projectiles[player_idx].get_pos()[1] > 1.2*cs.WINDOW_H
        hit_planet = wd.projectiles[player_idx].too_close_to_planet(wd.planets, min_dist=0)
        #hit_wormhole = wd.projectiles[player_idx].too_close_to_wormhole(wd.wormholes, min_dist=0)
        if (pg.time.get_ticks() - last_shot_tick > cs.HIT_ACTIVATION_DELAY) and shot_moving:
            hit_ufo0 = wd.projectiles[player_idx].hit_ufo(wd.ufo0)
            hit_ufo1 = wd.projectiles[player_idx].hit_ufo(wd.ufo1)
        else:
            hit_ufo0 = False
            hit_ufo1 = False

        if outside_bounds or hit_planet or hit_ufo0 or hit_ufo1:

            if hit_ufo0:
                wd.ufo0.lose_life()
                print("UFO 0 lost a life!")
                if wd.ufo0.get_life_count() <= 0:
                    print("UFO 0 ran out of lives!")
            if hit_ufo1:
                wd.ufo1.lose_life()
                print("UFO 1 lost a life!")
                if wd.ufo1.get_life_count() <= 0:
                    print("UFO 1 ran out of lives!")
            
            wd.projectiles[player_idx].stop_motion()
            shot_moving = False

            if player_idx:
                wd.projectiles[player_idx].set_pos(cs.PLAYER2_POS)
            else:
                wd.projectiles[player_idx].set_pos(cs.PLAYER1_POS)

            wd.projectiles[player_idx].update_motion(cs.DELTA_T, wd.planets)
            wd.projectiles[player_idx].render(screen, cs.RED)
            wd.ufo0.render(screen)
            wd.ufo1.render(screen)
            pg.display.update()
            if player_idx:
                player_idx = 0
            else:
                player_idx = 1
        
        elif shot_moving:
            screen.fill(cs.BLACK)
            for wormhole_pair in wd.wormholes:
                wormhole_pair[0].render(screen)
                wormhole_pair[1].render(screen)
            if (pg.time.get_ticks() - last_teleport_tick > cs.TELEPORTATION_DELAY):
                teleported = wd.projectiles[player_idx].teleport_if_in_wormhole(wd.wormholes)
                if teleported:
                    last_teleport_tick = pg.time.get_ticks()
                    
            wd.projectiles[player_idx].update_motion(cs.DELTA_T, wd.planets)
            wd.projectiles[player_idx].render(screen, cs.RED)
            wd.ufo0.render(screen)
            wd.ufo1.render(screen)
            for planet in wd.planets:
                planet.render(screen)
            pg.display.update()

        else:
            screen.fill(cs.BLACK)
            for wormhole_pair in wd.wormholes:
                wormhole_pair[0].render(screen)
                wormhole_pair[1].render(screen)
            wd.projectiles[player_idx].render(screen, cs.RED)
            wd.ufo0.render(screen)
            wd.ufo1.render(screen)
            for planet in wd.planets:
                planet.render(screen)
            pg.display.update()
        
        clk.tick(cs.FPS)

    pg.quit()
    quit()


if __name__ == "__main__":
    main()
