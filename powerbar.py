import pygame as pg
import numpy as np
import constants as cs
import utils
from graphics import graphics as gr


class Powerbar():
    def __init__(self, ufo):
        self.ufo = ufo
        self.pos = np.array([0.0, 0.0])
        self.border_size = np.array([cs.POWER_BAR_BORDER_W, cs.POWER_BAR_BORDER_H])
        self.bar_size = np.array([cs.POWER_BAR_W, cs.POWER_BAR_H])
        self.power_size = np.array([((self.ufo.get_shot_power() - cs.MIN_SHOT_POWER) / (cs.MAX_SHOT_POWER - cs.MIN_SHOT_POWER)) * 100, cs.POWER_BAR_H])
        self.border_rect = pg.Rect(self.pos, self.border_size)
        self.power_rect = pg.Rect(self.pos + cs.POWER_BAR_BORDER_THICKNESS, self.power_size)
    
    def set_pos(self):
        if self.ufo.get_pos()[0] < cs.WINDOW_W/2:
            self.pos = self.ufo.get_pos() + cs.POWER_BAR_OFFSET
        else:
            self.pos = self.ufo.get_pos() - cs.POWER_BAR_OFFSET - np.array([cs.POWER_BAR_W, 0.0])
        self.border_rect = pg.Rect(self.pos, self.border_size)

    def render(self, screen):
        pg.draw.rect(screen, cs.GREY, self.border_rect, cs.POWER_BAR_BORDER_THICKNESS)
        self.power_size = np.array([((self.ufo.get_shot_power() - cs.MIN_SHOT_POWER) / (cs.MAX_SHOT_POWER - cs.MIN_SHOT_POWER)) * 100, cs.POWER_BAR_H])
        self.power_rect = pg.Rect(self.pos + cs.POWER_BAR_BORDER_THICKNESS, self.power_size)
        pg.draw.rect(screen, cs.GREEN, self.power_rect)
        num = (((self.ufo.get_shot_power() - cs.MIN_SHOT_POWER) / (cs.MAX_SHOT_POWER - cs.MIN_SHOT_POWER)) - 0.5) * 10
        num_text = utils.text_format(f"{num}", gr.font, cs.POWER_BAR_H, cs.GREEN)
        screen.blit(num_text, tuple(self.pos + np.array([cs.POWER_BAR_BORDER_W + 5, 0.0])))