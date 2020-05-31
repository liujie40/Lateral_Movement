import pygame
from pygame.locals import *

class Setting:

    colors = {
        "white":(0xff,0xff,0xff),
        "Black":(0,0,0),
        "Red":(0xff,0,0),
        "Green":(0,0xff,0),
        "Blue":(0,0,0xff),
    }

    def __init__(self):
        pygame.init()

        self.screen_w = 600
        self.screen_h = 600

        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption("Simulation")

        self.scene = []



class Game(Setting):

    def __init__(self):
        super().__init__()
        self.awake()
        self.update()


    def awake(self):
        pass

    def update(self):
        run = True
        while run:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    run = False

            # color the background
            self.screen.fill(super().colors['white'])
            # update gameObjects
            for gameObject in self.scene:
                gameObject.update()
            # update the display
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    Game()