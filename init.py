import pygame as pg
import constants as cs


def init_bp():
    # Let's get to it
    print("Welcome to Black Planets Construction Site!")
    pg.init()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    clk = pg.time.Clock()
    return screen, clk