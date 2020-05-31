from settings import *
import time
from gameObject import GameObject
import pygame

class Computer(GameObject):
    def __init__(self, pos:pygame.Vector2, color):
        super().__init__(pos, color)

        self._state = State.VULNERABLE


    def draw(self):
        pygame.draw.rect(self.screen, self.color,(self.pos.x, self.pos.y))

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
        self._computers = [Computer() for _ in  range(self.lenComputers)]
        self.states = list(map(lambda x:x.state, self._computers))

    def getClock(self):
        return time.clock()

    @property
    def lenComputers(self):
        return self._m
    @property
    def getComputers(self):
        return self._computers


