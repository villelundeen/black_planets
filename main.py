import pygame as pg
import constants as cs
from game import game
import init
import menus

def main():

    screen, clk = init.init_bp()

    menus.main_menu(screen, clk)

    #game(screen, clk)




if __name__ == "__main__":
    main()
