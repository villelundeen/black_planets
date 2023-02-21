import pygame as pg
import constants as cs
from game import game
import utils


def start_menu():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            running = False


# Main Menu
def main_menu(screen, clk):
    
    menu=True
    selected="start"
    
    while menu:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_UP:
                    selected="start"
                elif event.key==pg.K_DOWN:
                    selected="quit"
                if event.key==pg.K_RETURN:
                    if selected=="start":
                        print("Start")
                        game(screen, clk)
                    if selected=="quit":
                        pg.quit()
                        quit()
    
        # Main Menu UI
        screen.fill(cs.BLACK)
        title=utils.text_format("BLACK PLANETS", cs.FONT, 90, cs.GREEN)
        if selected=="start":
            text_start=utils.text_format("START", cs.FONT, 75, cs.WHITE)
        else:
            text_start = utils.text_format("START", cs.FONT, 75, cs.GREY)
        if selected=="quit":
            text_quit=utils.text_format("QUIT", cs.FONT, 75, cs.WHITE)
        else:
            text_quit = utils.text_format("QUIT", cs.FONT, 75, cs.GREY)
    
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
    
        # Main Menu Text
        screen.blit(title, (cs.WINDOW_W/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (cs.WINDOW_W/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (cs.WINDOW_W/2 - (quit_rect[2]/2), 500))
        pg.display.update()
        clk.tick(cs.FPS)
        pg.display.set_caption("Python - Pygame Simple Main Menu Selection")

