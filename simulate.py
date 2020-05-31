from settings import *

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