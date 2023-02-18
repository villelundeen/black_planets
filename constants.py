import numpy as np

DELTA_T = 0.016
FPS = 60
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK =     (0,   0,   0)
TEXTCOLOR = (  0,   0,  0)
WINDOW_W = 1500
WINDOW_H = 1000
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
PROJECTILE_RAD = 5
PRJECTILE_MASS = 10
UFO_RAD = 20
UFO_MASS = 30
UFO_ANGULAR_RESOLUTION = 5*np.pi/180
MIN_SHOT_POWER = 100
MAX_SHOT_POWER = 400
SHOT_POWER_INCREMENT = 20
MIN_PLANET_RAD = 40
MAX_PLANET_RAD = 80
G_CONST = 2
PLANET_DENSITY = 10
PLAYER1_POS = np.array([0.05*WINDOW_W, 0.05*WINDOW_H])
PLAYER2_POS = np.array([0.95*WINDOW_W, 0.95*WINDOW_H])
PLANET_MIN_SEPARATION = 100
MIN_KEY_PRESS_DELAY = 250
HIT_ACTIVATION_DELAY = 250