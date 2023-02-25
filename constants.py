import numpy as np
from pygame import mixer as mx
from pygame import display as dp


# Some colors
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
DARK_BLUE =     (  0, 0,   50)
RED =       (255,   0,   0)
BLACK =     (0,   0,   0)
GREY =     (150,   150,   150)
TRACE_COLOR = (  100,   100,  100)


# Game Fonts
#FONT_PATH = "./fonts/Freedom-10eM.ttf"  # Font credit to HXDes. Downloaded from: https://www.fontspace.com/category/ttf
#FONT_PATH = "./fonts/Nasa21-l23X.ttf"

# General game parameters
DELTA_T = 0.016
FPS = 60
WINDOW_W = 1500
WINDOW_H = 1000
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
PLAYER1_POS = np.array([0.05*WINDOW_W, 0.05*WINDOW_H])
PLAYER2_POS = np.array([0.95*WINDOW_W, 0.95*WINDOW_H])
MIN_KEY_PRESS_DELAY = 100
HIT_ACTIVATION_DELAY = 250

# UFO parameters
UFO_RAD = 25
UFO_MASS = 30
UFO_ANGULAR_RESOLUTION = 5*np.pi/180
MIN_SHOT_POWER = 200
MAX_SHOT_POWER = 600
SHOT_POWER_INCREMENT = 20

# Powerbar parameters
POWER_BAR_OFFSET = np.array([50, -30])
POWER_BAR_BORDER_W = 104
POWER_BAR_BORDER_H = 14
POWER_BAR_BORDER_THICKNESS = 2
POWER_BAR_W = POWER_BAR_BORDER_W - 2*POWER_BAR_BORDER_THICKNESS
POWER_BAR_H = POWER_BAR_BORDER_H - 2*POWER_BAR_BORDER_THICKNESS

# Projectile parameters
PROJECTILE_RAD = 5
PROJECTILE_MASS = 10
TRACE_DELAY = 25
TRACE_WIDTH = 2

# General physics parameters
G_CONST = 2

# Planet parameters
MIN_PLANET_RAD = 40
MAX_PLANET_RAD = 80
PLANET_DENSITY = 10
PLANET_MIN_SEPARATION = 100

# Wormhole parameters
WORMHOLE_DENSITY = PLANET_DENSITY
WORMHOLE_OUTER_RAD = 100
WORMHOLE_INNER_RAD = 0.5*WORMHOLE_OUTER_RAD
WORMHOLE_MIN_SEPARATION = PLANET_MIN_SEPARATION
TELEPORTATION_DELAY = 250