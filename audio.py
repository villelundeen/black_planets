from pygame import mixer as mx
 

class Audio():
    def __init__(self):
        self.sfx = {}

    def create_sounds(self):
        self.sfx = {
            "menu_select":      mx.Sound("./sounds/menu_select.wav"), 
            "start_level":      mx.Sound("./sounds/game_start_woosh.wav"),
            "laser":            mx.Sound("./sounds/laser_shot.wav"),
            "ufo_hit":          mx.Sound("./sounds/ufo_hit.wav"),
            "planet_hit":       mx.Sound("./sounds/planet_hit.wav"),
            "teleport":         mx.Sound("./sounds/teleport.wav"),
            "oob":              mx.Sound("./sounds/oob_lightsaber.wav")
        }

    def tune_volumes(self):
        self.sfx["laser"].set_volume(0.5)
        # TODO: Finish tuning relative sound effect volumes


audio = Audio()
