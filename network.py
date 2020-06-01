from settings import *
import time
import random
from gameObject import GameObject
import pygame
from constants import *

class Computer(GameObject):
    w = 10
    h = 10

    def __init__(self, pos:pygame.Vector2, color=None):
        super().__init__(pos, color)
        if not color:
            self.checkState()
            self._state = State.VULNERABLE
        else:
            self._state = None

        self.exfiltrate_rate = EXFILTRATE_RATE
        self.damage_rate = DAMAGING_RATE
        self.ddx = self.dx = 0



    def checkState(self):
        if self._state == State.VULNERABLE:
            self.color = Setting.colors['red']
        elif self._state == State.INTRUDED:
            self.color = Setting.colors['green']
            self.exfiltrate()
        elif self._state == State.EXFILTRATED:
            self.color = Setting.colors['purple']
            self.damage()
        elif self._state == State.DAMAGED:
            self.color = Setting.colors['black']
            self.exfiltrate()
        elif self._state == State.SECURE:
            self.color = Setting.colors['blue']

    def exfiltrate(self):
        if self.dx < LAMBDA_J(self.exfiltrate_rate)*2:
            pygame.draw.rect(self.screen, Setting.colors['purple'],
                             (self.pos.x, self.pos.y-10, self.dx, 5))
            self.dx += self.exfiltrate_rate//2
        else:
            self._state = State.EXFILTRATED
            self.dx = 0

    def damage(self):
        if self.ddx < self.damage_rate*10:
            pygame.draw.rect(self.screen, Setting.colors['black'],
                             (self.pos.x, self.pos.y-10, self.ddx, 5))
            self.ddx += self.damage_rate//2
        else:
            self._state = State.DAMAGED
            self.ddx = 0


    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.pos.x, self.pos.y, Computer.w, Computer.h))

    def control(self):
        self.checkState()

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
        self._m = int(context[0])
        self.intrude_rate = int(context[1])
        self.intrude_index = 0


        self._computers = []
        self.legend = []
        for _ in range(self.lenComputers):
            v = pygame.Vector2()
            v.x = random.randint(Computer.w*10, Setting.screen_w)
            v.y = random.randint(Computer.h*10, Setting.screen_h)
            self._computers.append(Computer(v, Setting.colors['red']))

            self._computers[_].exfiltrate_rate = int(context[2])
            self._computers[_].damage_rate = int(context[4])

        self.states = list(map(lambda x:x.state, self.getComputers))

        self.createLegend()

    def getClock(self):
        return pygame.time.get_ticks()

    def stateChange(self):
        clock = self.getClock()//CLOCK_TICK
        # self.intrude_index = random.randint(0, self.lenComputers-1)
        # change computer to intruded
        if self.intrude_index < len(self.getComputers) and \
            clock != 0 and clock%self.intrude_rate == 0 and \
                (self.getComputers[self.intrude_index].state != State.EXFILTRATED
                or self.getComputers[self.intrude_index].state != State.SECURE):
            self.getComputers[self.intrude_index].state = State.INTRUDED
            self.intrude_index += 1

    def update(self):
        for computer in self._computers:
            computer.update()
        for legend in self.legend:
            legend.update()

        self.stateChange()

    def createLegend(self):
        comp_sign = ['red', 'green', 'purple','blue', 'black']
        legend_sign = ["Vulnerable", "Intruded", 'Exfiltrated', 'Secure', 'Damaged']
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


