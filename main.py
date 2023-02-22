from game import Game
import init
from menu import Main_Menu, Options_Menu


"""
# For Aalto-3 demonstration
class Body():
    def __init__(self, x=100, y=100, dx=10, dy=0, rad=30):
        self.x=x
        self.y=y
        self.pos = np.array([self.x, self.y])
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.img = im.load("./figs/wormhole.png")
        self.img = tr.scale(self.img, (2*self.rad,2*self.rad))
        

    def new_pos(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.pos = (self.x, self.y)
        

    #def render(self, screen, color):
     #   pg.draw.circle(screen, color, (self.x, self.y), self.rad)
    
    def render(self, screen):
        screen.blit(self.img, self.pos - np.array([self.rad, self.rad]))
    """

def main():

    screen, clk = init.init_bp()
    
    game = Game(screen, clk)

    options_menu = Options_Menu(screen, clk)
    main_menu = Main_Menu(screen, clk, game, options_menu)
    
    main_menu.main_menu()

    """
    # For Aalto-3 demonstration

    BLUE =      (  0,   0, 255)
    WHITE =     (255, 255, 255)

    pg.init()
    screen = pg.display.set_mode(cs.WINDOW_SIZE)
    clk = pg.time.Clock()

    running = True

    obj = Body(dx=1)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(WHITE)
        obj.render(screen)
        obj.new_pos()


        pg.display.update()



        clk.tick(cs.FPS)

    pg.quit()
    quit()
    """

if __name__ == "__main__":
    main()
