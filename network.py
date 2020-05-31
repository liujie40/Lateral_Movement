from settings import *
import time
import random
from gameObject import GameObject
import pygame

class Computer(GameObject):
    w = 5
    h = 5

    def __init__(self, pos:pygame.Vector2, color):
        super().__init__(pos, color)

        self._state = State.VULNERABLE

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.pos.x, self.pos.y, Computer.w, Computer.h))

    def control(self):
        super().control()

    def move(self):
        super().move()

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, new_state):
        self._state = new_state


class System:

    def __init__(self):
        self._m = M
        self._computers = []
        self.legend = []
        for _ in range(self.lenComputers):
            v = pygame.Vector2()
            v.x = random.randint(Computer.w*10, Setting.screen_w)
            v.y = random.randint(Computer.h*10, Setting.screen_h)
            self._computers.append(Computer(v, Setting.colors['red']))

        self.states = list(map(lambda x:x.state, self._computers))

        self.createLegend()

    def getClock(self):
        return time.clock()

    def update(self):
        for computer in self._computers:
            computer.update()
        for legend in self.legend:
            legend.update()

    def createLegend(self):
        self.legend.append(Computer(pygame.Vector2(10,10), Setting.colors['red']))

    @property
    def lenComputers(self):
        return self._m
    @property
    def getComputers(self):
        return self._computers


