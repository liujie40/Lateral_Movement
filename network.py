from settings import *
import time
import random
from gameObject import GameObject
import pygame
from constants import *

class Computer(GameObject):
    w = 5
    h = 5

    def __init__(self, pos:pygame.Vector2, color=None):
        if not color:
            if self._state == State.VULNERABLE:
                self.color = Setting.colors['red']
            elif self._state == State.INTRUDED:
                self.color = Setting.colors['green']
            elif self._state == State.EXFILTRATED:
                self.color = Setting.colors['purple']
            elif self._state == State.SECURE:
                self.color = Setting.colors['blue']
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

class Text(GameObject):
    def __init__(self, pos: pygame.Vector2, color, text):
        super().__init__(pos, color)
        self.text = text

    def draw(self):
        vulnerable = self.font.render(self.text,
                                         False, self.color)

        self.screen.blit(vulnerable, (self.pos.x, self.pos.y))


class System:

    def __init__(self, context):
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
        comp_sign = ['red', 'green', 'purple','blue']
        legend_sign = ["Vulnerable", "Intruded", 'Exfiltrated', 'Secure']
        for index in range(len(comp_sign)):
            self.legend.append(Computer(pygame.Vector2(10,10 + 10*index),
                                        Setting.colors[comp_sign[index]]))
            self.legend.append(Text(pygame.Vector2(20, 5 + 10*index),
                                    Setting.colors['black'], legend_sign[index] +" Computer"))


    @property
    def lenComputers(self):
        return self._m
    @property
    def getComputers(self):
        return self._computers


