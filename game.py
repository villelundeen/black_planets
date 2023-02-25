import os
import pygame as pg
from pygame.locals import *
import numpy as np
from audio import audio as au
from pygame import image as im

import constants as cs
import world



class Game():
    def __init__(self, screen, clk, pause_menu, difficulty=1):
        self.screen = screen
        self.clk = clk
        self.pause_menu = pause_menu
        self.difficulty = difficulty
        self.n_planet = 5
        self.n_wormhole_pairs = 1
        self.wd = world.World(self.n_planet,self.n_wormhole_pairs)

    def next_level(self):
        self.wd.update_level()

    def game(self):

        self.wd.projectile0.stop_motion()
        pg.display.set_caption("Black Planets")
        self.screen.fill(cs.BLACK)
        pg.display.update()
        pg.time.wait(500)
        
        self.wd.ufo0.render(self.screen)
        self.wd.ufo1.render(self.screen)
        for planet in self.wd.planets:
            planet.render(self.screen)
        for wormhole_pair in self.wd.wormholes:
            wormhole_pair[0].render(self.screen)
            wormhole_pair[1].render(self.screen)

        pg.display.update()

        running = True
        shot_moving = False
        inside_bounds = True
        last_tick = 0
        last_shot_tick = 0
        last_teleport_tick = 0
        last_trace_tick = 0
        player_idx = 0
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        quit()
                    if event.key == pg.K_SPACE:
                        back_to_main_menu = self.pause_menu.pause_menu()  # Go to Pause menu
                        if back_to_main_menu:
                            running = False
            if inside_bounds:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    if shot_moving == False:
                        if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                            last_tick = pg.time.get_ticks()
                            shot_moving = True
                            self.wd.projectiles[player_idx].enable_motion()
                            shot_vector = self.wd.ufos[player_idx].get_shot_direction() * self.wd.ufos[player_idx].get_shot_power()
                            self.wd.projectiles[player_idx].set_vel(shot_vector)
                            last_shot_tick = pg.time.get_ticks()
                            au.sfx["laser"].play()
                if keys[pg.K_LEFT] or keys[pg.K_a]:
                    if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                        last_tick = pg.time.get_ticks()
                        if shot_moving == False:
                            self.wd.ufos[player_idx].enable_rotation()
                        self.wd.ufos[player_idx].rotate_positive()
                        self.wd.ufos[player_idx].disable_rotation()
                if keys[pg.K_RIGHT] or keys[pg.K_d]:
                    if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                        last_tick = pg.time.get_ticks()
                        if shot_moving == False:
                            self.wd.ufos[player_idx].enable_rotation()
                        self.wd.ufos[player_idx].rotate_negative()
                        self.wd.ufos[player_idx].disable_rotation()
                if keys[pg.K_UP] or keys[pg.K_w]:
                    if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                        last_tick = pg.time.get_ticks()
                        if shot_moving == False:
                            self.wd.ufos[player_idx].enable_power_tuning()
                        self.wd.ufos[player_idx].increase_shot_power()
                        self.wd.ufos[player_idx].disable_power_tuning()
                if keys[pg.K_DOWN] or keys[pg.K_s]:
                    if pg.time.get_ticks() - last_tick > cs.MIN_KEY_PRESS_DELAY:
                        last_tick = pg.time.get_ticks()
                        if shot_moving == False:
                            self.wd.ufos[player_idx].enable_power_tuning()
                        self.wd.ufos[player_idx].decrease_shot_power()
                        self.wd.ufos[player_idx].disable_power_tuning()

            outside_bounds = self.wd.projectiles[player_idx].get_pos()[0] < -0.2*cs.WINDOW_W or \
                            self.wd.projectiles[player_idx].get_pos()[0] > 1.2*cs.WINDOW_W or \
                            self.wd.projectiles[player_idx].get_pos()[1] < -0.2*cs.WINDOW_H or \
                            self.wd.projectiles[player_idx].get_pos()[1] > 1.2*cs.WINDOW_H
            hit_planet = self.wd.projectiles[player_idx].too_close_to_planet(self.wd.planets, min_dist=0)
            #hit_wormhole = self.wd.projectiles[player_idx].too_close_to_wormhole(self.wd.wormholes, min_dist=0)
            if (pg.time.get_ticks() - last_shot_tick > cs.HIT_ACTIVATION_DELAY) and shot_moving:
                hit_ufo0 = self.wd.projectiles[player_idx].hit_ufo(self.wd.ufo0)
                hit_ufo1 = self.wd.projectiles[player_idx].hit_ufo(self.wd.ufo1)
            else:
                hit_ufo0 = False
                hit_ufo1 = False

            if outside_bounds or hit_planet or hit_ufo0 or hit_ufo1:
                if outside_bounds:
                    au.sfx["oob"].play()
                if hit_planet:
                    au.sfx["planet_hit"].play()
                if hit_ufo0:
                    self.wd.ufo0.lose_life()
                    if self.wd.ufo0.get_life_count() <= 0:
                        print("UFO 0 ran out of lives!")
                    au.sfx["ufo_hit"].play()
                    print("UFO 0 lost a life!")
                    au.sfx["start_level"].play()
                    self.screen.fill(cs.BLACK)
                    pg.display.update()
                    pg.time.delay(1750)
                    self.next_level()
                if hit_ufo1:
                    self.wd.ufo1.lose_life()
                    if self.wd.ufo1.get_life_count() <= 0:
                        print("UFO 1 ran out of lives!")
                    au.sfx["ufo_hit"].play()
                    print("UFO 1 lost a life!")
                    au.sfx["start_level"].play()
                    self.screen.fill(cs.BLACK)
                    pg.display.update()
                    pg.time.delay(1750)
                    self.next_level()
                self.wd.projectiles[player_idx].stop_motion()
                shot_moving = False

                if player_idx:
                    self.wd.projectiles[player_idx].set_pos(cs.PLAYER2_POS)
                else:
                    self.wd.projectiles[player_idx].set_pos(cs.PLAYER1_POS)
                self.wd.projectiles[0].render_traces(self.screen)
                self.wd.projectiles[1].render_traces(self.screen)
                self.wd.projectiles[player_idx].update_motion(cs.DELTA_T, self.wd.planets)
                self.wd.projectiles[player_idx].render(self.screen, cs.RED)
                self.wd.ufo0.render(self.screen)
                self.wd.ufo1.render(self.screen)
                pg.display.update()
                if player_idx:
                    player_idx = 0
                else:
                    player_idx = 1
            
            elif shot_moving:
                self.screen.fill(cs.BLACK)
                for wormhole_pair in self.wd.wormholes: 
                    wormhole_pair[0].render(self.screen)
                    wormhole_pair[1].render(self.screen)
                if (pg.time.get_ticks() - last_teleport_tick > cs.TELEPORTATION_DELAY):
                    teleported = self.wd.projectiles[player_idx].teleport_if_in_wormhole(self.wd.wormholes)
                    if teleported:
                        last_teleport_tick = pg.time.get_ticks()
                        
                self.wd.projectiles[player_idx].update_motion(cs.DELTA_T, self.wd.planets)
                if pg.time.get_ticks() - last_trace_tick > cs.TRACE_DELAY:
                    last_trace_tick = pg.time.get_ticks()
                    self.wd.projectiles[player_idx].add_trace_point(self.wd.projectiles[player_idx].get_pos())
                self.wd.projectiles[0].render_traces(self.screen)
                self.wd.projectiles[1].render_traces(self.screen)
                self.wd.projectiles[player_idx].render(self.screen, cs.RED)
                self.wd.ufo0.render(self.screen)
                self.wd.ufo1.render(self.screen)
                for planet in self.wd.planets:
                    planet.render(self.screen)
                pg.display.update()

            else:
                self.screen.fill(cs.BLACK)
                for wormhole_pair in self.wd.wormholes:
                    wormhole_pair[0].render(self.screen)
                    wormhole_pair[1].render(self.screen)
                self.wd.projectiles[0].render_traces(self.screen)
                self.wd.projectiles[1].render_traces(self.screen)
                self.wd.projectiles[player_idx].render(self.screen, cs.RED)
                self.wd.ufo0.render(self.screen)
                self.wd.ufo1.render(self.screen)
                self.wd.ufos[player_idx].powerbar.render(self.screen)
                for planet in self.wd.planets:
                    planet.render(self.screen)
                pg.display.update()
            
            self.clk.tick(cs.FPS)
