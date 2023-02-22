import pygame as pg
import constants as cs
from pygame import mixer as mx


def init_bp():
    # Let's get to it
    print("Welcome to Black Planets Construction Site!")
    pg.init()
    # Game sound effects
    UFO_HIT_SOUND= mx.Sound("./sounds/ufo_hit_explosion.wav")
    TELEPORT_SOUND= mx.Sound("./sounds/teleport.wav")
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    clk = pg.time.Clock()
    return screen, clk