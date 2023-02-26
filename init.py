import pygame as pg
import constants as cs
from pygame import mixer as mx
from audio import audio as au


def init_bp():
    # Let's get to it
    print("Welcome to Black Planets Construction Site!")
    # TODO: Clean up previous stuff if needed
    pg.init()
    # Game sound effects
    au.create_sounds()
    #screen = pg.display.set_mode(cs.WINDOW_SIZE)
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clk = pg.time.Clock()
    return screen, clk