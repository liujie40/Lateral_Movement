from settings import *
from network import System,pygame, Text

class Game(Setting):

    def __init__(self):
        super().__init__()
        self.awake()
        self.update()


    def awake(self):
        s = System()
        self.scene.append(s)

    def timer(self):
        t = pygame.time.get_ticks() // 1800
        text = self.font2.render(str(t)+ " Day", False, Setting.colors['blue'])
        self.screen.blit(text, (10, Setting.screen_h-30))


    def update(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    run = False

            # color the background
            self.screen.fill(super().colors['white'])
            # update gameObjects
            for gameObject in self.scene:
                gameObject.update()
            # add a timer
            self.timer()
            # update the display
            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    Game()