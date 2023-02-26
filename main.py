from game import Game
import init
from menu import Main_Menu, Options_Menu, Pause_Menu


def main(screen, clk):

    while True:

        pause_menu = Pause_Menu(screen, clk)
        game = Game(screen, clk, pause_menu)
        print(f"{game.wd.ufo0.get_life_count()}")
        print(f"{game.wd.ufo1.get_life_count()}")
        options_menu = Options_Menu(screen, clk)
        main_menu = Main_Menu(screen, clk, game, options_menu)
        
        main_menu.main_menu()

        # Clean up of old level and menus when exiting the old game
        print("Clean up!")
        for planet in game.wd.planets:
            del planet
        for wormhole in game.wd.wormholes:
            del wormhole
        for ufo in game.wd.ufos:
            del ufo
        for projectile in game.wd.projectiles:
            del projectile


if __name__ == "__main__":
            
    screen, clk = init.init_black_planets()
    main(screen, clk)
