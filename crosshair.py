import pygame as pg
import numpy as np
import constants as cs
import utils
from graphics import graphics as gr


class Crosshair():
    def __init__(self, ufo):
        self.ufo = ufo
        self.pos = self.ufo.get_pos()
        self.rad = 2 * cs.UFO_RAD
    
    def set_pos(self):
        if self.ufo.get_pos()[0] < cs.WINDOW_W/2:
            self.pos = self.ufo.get_pos() + cs.POWER_BAR_OFFSET
        else:
            self.pos = self.ufo.get_pos() - cs.POWER_BAR_OFFSET - np.array([cs.POWER_BAR_W, 0.0])
        self.border_rect = pg.Rect(self.pos, self.border_size)

    def render(self, screen):
        pg.draw.circle(screen, cs.GREEN, self.pos, self.rad, cs.CROSSHAIR_THICKNESS)
        pg.draw.line(screen, cs.GREEN, self.pos, self.pos + self.ufo.get_shot_direction()*self.rad*1.1, cs.CROSSHAIR_THICKNESS)       
        """
        if self.ufo.get_pos()[0] < cs.WINDOW_W/2:
            screen.blit(num_text, tuple(self.pos + np.array([cs.POWER_BAR_BORDER_W + 5, 0.0])))
        else:
            num_rect = num_text.get_rect()
            screen.blit(num_text, tuple(self.pos - np.array([num_rect[2] + 5, 0.0])))
        """