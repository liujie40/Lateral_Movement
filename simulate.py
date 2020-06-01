from settings import *
from network import System,pygame
from constants import *

class Game(Setting):

    def __init__(self, context):
        super().__init__()
        self.s = System(context)
        self.scene.append(self.s)
        self.awake()
        self.update()


    def awake(self):
        pass

    def timer(self):
        t = self.s.getClock() // CLOCK_TICK
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
            pygame.time.delay(TIME_DELAY)

        pygame.quit()


if __name__ == "__main__":
    Game([])