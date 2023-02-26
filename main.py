from game import Game
import init
from menu import Main_Menu, Options_Menu, Pause_Menu


def main():

    while True:
        
        screen, clk = init.init_bp()
        
        pause_menu = Pause_Menu(screen, clk)
        game = Game(screen, clk, pause_menu)

        options_menu = Options_Menu(screen, clk)
        main_menu = Main_Menu(screen, clk, game, options_menu)
        
        main_menu.main_menu()


if __name__ == "__main__":
    main()
