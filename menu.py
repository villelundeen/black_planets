import pygame as pg
import constants as cs
import utils
from enum import Enum
from audio import audio as au
from graphics import graphics as gr
from pygame import image as im
from pygame import transform as tr

class Menu():
    def __init__(self, screen, clk):
        self.screen = screen
        self.clk = clk
        self.in_menu = True
        self.selected = 0



class Main_Menu(Menu):
    def __init__(self, screen, clk, game, options_menu):
        super().__init__(screen, clk)
        self.buttons = Enum('buttons', ['START', 'OPTIONS', 'QUIT'], start=0)
        self.n_buttons = len(self.buttons)
        self.game = game
        self.options_menu = options_menu
        self.difficulty = 1

    def main_menu(self):
        bg = im.load("./figs/main_menu_cropped3.png")
        self.screen.blit(bg, (0,0))
        #pg.display.update()
        while self.in_menu:
            for event in pg.event.get():
                if event.type==pg.QUIT or event.type==pg.K_ESCAPE:
                    au.sfx["menu_select"].play()
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    au.sfx["menu_select"].play()
                    if event.key==pg.K_UP:
                        if self.selected > 0:
                            self.selected = self.selected - 1
                    elif event.key==pg.K_DOWN:
                        if self.selected < self.n_buttons - 1:
                            self.selected = self.selected + 1
                    if event.key==pg.K_RETURN:
                        if self.selected==self.buttons.START.value:
                            au.sfx["start_level"].play()
                            self.screen.fill(cs.BLACK)
                            pg.display.update()
                            pg.time.delay(1750)
                            self.game.game()
                            bg = im.load("./figs/main_menu_cropped3.png")
                            self.screen.blit(bg, (0,0))

                        if self.selected==self.buttons.OPTIONS.value:
                            self.options_menu.options_menu(self)
                        if self.selected==self.buttons.QUIT.value:
                            pg.quit()
                            quit()
        
            # Main Menu UI

            title_black=utils.text_format("BLACK", gr.menu_font, 120, cs.GREEN)
            title_planet=utils.text_format("PLANETS", gr.menu_font, 120, cs.BLACK)

            if self.selected==self.buttons.START.value:
                text_start=utils.text_format("START", gr.menu_font, 75, cs.GREEN)
            else:
                text_start = utils.text_format("START", gr.menu_font, 75, cs.BLACK)

            if self.selected==self.buttons.OPTIONS.value:
                text_options=utils.text_format("OPTIONS", gr.menu_font, 75, cs.GREEN)
            else:
                text_options = utils.text_format("OPTIONS", gr.menu_font, 75, cs.BLACK)

            if self.selected==self.buttons.QUIT.value:
                text_quit=utils.text_format("QUIT", gr.menu_font, 75, cs.GREEN)
            else:
                text_quit = utils.text_format("QUIT", gr.menu_font, 75, cs.BLACK)

        
            title_black_rect=title_black.get_rect()
            title_planet_rect=title_planet.get_rect()
            start_rect=text_start.get_rect()
            options_rect=text_options.get_rect()
            quit_rect=text_quit.get_rect()

            update_rects = [title_black_rect, title_planet_rect, start_rect, options_rect, quit_rect]
            
        
            # Main Menu Text
            self.screen.blit(title_black, (cs.WINDOW_W/2 - (title_black_rect[2]/2 + title_planet_rect[2]/2 + 30), 0.3*cs.WINDOW_H))
            self.screen.blit(title_planet, (cs.WINDOW_W/2 - (-title_black_rect[2]/2 + title_planet_rect[2]/2 - 30), 0.3*cs.WINDOW_H))
            self.screen.blit(text_start, (cs.WINDOW_W/2 - (start_rect[2]/2), 0.5*cs.WINDOW_H))
            self.screen.blit(text_options, (cs.WINDOW_W/2 - (options_rect[2]/2), 0.6*cs.WINDOW_H))
            self.screen.blit(text_quit, (cs.WINDOW_W/2 - (quit_rect[2]/2), 0.7*cs.WINDOW_H))
            #pg.display.update(update_rects)
            pg.display.update()
            pg.display.set_caption("Black Planets - Main Menu")
            self.clk.tick(cs.FPS)



class Options_Menu(Menu):
    def __init__(self, screen, clk):
        super().__init__(screen, clk)
        self.buttons = Enum('buttons', ['DIFFICULTY', 'SOUND', 'BACK'], start=0)
        self.n_buttons = len(self.buttons)

    def options_menu(self, main_menu):   
        while self.in_menu:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    au.sfx["start_level"].play()
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    au.sfx["menu_select"].play()
                    if event.key==pg.K_UP:
                        if self.selected > 0:
                            self.selected = self.selected - 1
                    elif event.key==pg.K_DOWN:
                        if self.selected < self.n_buttons - 1:
                            self.selected = self.selected + 1
                    if event.key==pg.K_RETURN:
                        if self.selected==self.buttons.BACK.value:
                            main_menu.main_menu()
        
            # Options Menu UI
            self.screen.fill(cs.BLACK)
            title_options=utils.text_format("OPTIONS", gr.menu_font, 120, cs.GREEN)

            if self.selected==self.buttons.DIFFICULTY.value:
                text_start=utils.text_format("DIFFICULTY", gr.menu_font, 75, cs.GREEN)
            else:
                text_start = utils.text_format("DIFFICULTY", gr.menu_font, 75, cs.GREY)

            if self.selected==self.buttons.SOUND.value:
                text_options=utils.text_format("SOUND", gr.menu_font, 75, cs.GREEN)
            else:
                text_options = utils.text_format("SOUND", gr.menu_font, 75, cs.GREY)

            if self.selected==self.buttons.BACK.value:
                text_quit=utils.text_format("BACK", gr.menu_font, 75, cs.GREEN)
            else:
                text_quit = utils.text_format("BACK", gr.menu_font, 75, cs.GREY)

        
            title_options_rect=title_options.get_rect()
            start_rect=text_start.get_rect()
            options_rect=text_options.get_rect()
            quit_rect=text_quit.get_rect()
            
        
            # Options Menu Text
            self.screen.blit(title_options, (cs.WINDOW_W/2 - title_options_rect[2]/2 , 0.2*cs.WINDOW_H))
            self.screen.blit(text_start, (cs.WINDOW_W/2 - (start_rect[2]/2), 0.4*cs.WINDOW_H))
            self.screen.blit(text_options, (cs.WINDOW_W/2 - (options_rect[2]/2), 0.5*cs.WINDOW_H))
            self.screen.blit(text_quit, (cs.WINDOW_W/2 - (quit_rect[2]/2), 0.6*cs.WINDOW_H))
            pg.display.update()
            self.clk.tick(cs.FPS)
            pg.display.set_caption("Black Planets - Options Menu")



class Pause_Menu(Menu):
    def __init__(self, screen, clk):
        super().__init__(screen, clk)
        self.buttons = Enum('buttons', ['RESUME', 'RETURN'], start=0)
        self.n_buttons = len(self.buttons)
        #self.game = game

    def pause_menu(self):   
        back_to_main_menu = False
        while self.in_menu:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    au.sfx["start_level"].play()
                    pg.quit()
                    quit()
                if event.type==pg.KEYDOWN:
                    au.sfx["menu_select"].play()
                    if event.key==pg.K_UP:
                        if self.selected > 0:
                            self.selected = self.selected - 1
                    elif event.key==pg.K_DOWN:
                        if self.selected < self.n_buttons - 1:
                            self.selected = self.selected + 1
                    if event.key==pg.K_RETURN:
                        if self.selected==self.buttons.RESUME.value:
                            back_to_main_menu = False
                            self.in_menu = False
                        if self.selected==self.buttons.RETURN.value:
                            back_to_main_menu = True
                            self.in_menu = False
        
            # Pause Menu UI
            self.screen.fill(cs.BLACK)
            title_pause=utils.text_format("PAUSE", gr.menu_font, 120, cs.GREEN)

            if self.selected==self.buttons.RESUME.value:
                text_resume=utils.text_format("RESUME", gr.menu_font, 75, cs.GREEN)
            else:
                text_resume=utils.text_format("RESUME", gr.menu_font, 75, cs.GREY)

            if self.selected==self.buttons.RETURN.value:
                text_return=utils.text_format("MAIN MENU", gr.menu_font, 75, cs.GREEN)
            else:
                text_return=utils.text_format("MAIN MENU", gr.menu_font, 75, cs.GREY)

            title_pause_rect=title_pause.get_rect()
            resume_rect=text_resume.get_rect()
            return_rect=text_return.get_rect()            
        
            # Options Menu Text
            self.screen.blit(title_pause, (cs.WINDOW_W/2 - title_pause_rect[2]/2 , 0.2*cs.WINDOW_H))
            self.screen.blit(text_resume, (cs.WINDOW_W/2 - (resume_rect[2]/2), 0.4*cs.WINDOW_H))
            self.screen.blit(text_return, (cs.WINDOW_W/2 - (return_rect[2]/2), 0.5*cs.WINDOW_H))
            pg.display.update()
            self.clk.tick(cs.FPS)
            pg.display.set_caption("Black Planets - Options Menu")

        return back_to_main_menu
    
