from settings import *
import time
import random
from gameObject import GameObject
import pygame
from constants import *
from multiprocessing import Process
from threading import Thread
import matplotlib.pyplot as plt

class Computer(GameObject):
    """
    Computer class to preview the simulation
    Computer is a rectangular object
    w: width of the computer
    h: height of the computer
    """
    w = 10
    h = 10

    def __init__(self, pos:pygame.Vector2, color=None):
        """
        (Computer, pygame.Vector2, (int, int, int))
        :param pos: position of the gameObject
        :param color: color of the computer, depends on the state
        """
        super().__init__(pos, color)
        # determine whether computer is static
        if not color:
            self._state = State.VULNERABLE
            self.checkState()
        else:
            self._state = None


        self.clock = 0
        self.i_computers = 0

        self.dx = 0



    def checkState(self):
        """
        (Computer) -> None
        set the color of the computer
        depending its state
        VULNERABLE: red
        INTRUDED: green
        EXFILTRATED:pink
        DAMAGED:black
        SECURE:blue
        :return: None
        """
        if self._state == State.VULNERABLE:
            self.color = Setting.colors['red']
        elif self._state == State.INTRUDED:
            self.color = Setting.colors['green']
        elif self._state == State.EXFILTRATED:
            self.exfiltrate()
        elif self._state == State.DAMAGED:
            self.color = Setting.colors['black']
        elif self._state == State.SECURE:
            self.color = Setting.colors['blue']



    def exfiltrate(self):
        """
        (Computer) -> None
        checks if computer becomes exfiltrated
        once triggered it will try to load files
        :return:None
        """
        if self.dx < MU_J(self.i_computers)*2:
            pygame.draw.rect(self.screen, Setting.colors['purple'],
                             (self.pos.x, self.pos.y-10, self.dx, 5))
            self.dx += 2
        else:
            self.color = Setting.colors['purple']

    def draw(self):
        """
        draw rectangle represented as computer
        :return:
        """
        pygame.draw.rect(self.screen, self.color,
                         (self.pos.x, self.pos.y, Computer.w, Computer.h))

    def control(self):
        """
        controls the state
        :return:
        """
        self.checkState()


    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, new_state):
        self._state = new_state

class Text(GameObject):
    """
    Create a text and add it to the scene
    """
    def __init__(self, pos: pygame.Vector2, color, text):
        """
        :param pos: position in the world
        :param color: color of the text
        :param text: the actual name of the text
        """
        super().__init__(pos, color)
        self.text = text

    def draw(self):
        """
        show the text
        :return: None
        """
        vulnerable = self.font.render(self.text,
                                         False, self.color)

        self.screen.blit(vulnerable, (self.pos.x, self.pos.y))


class System:
    """
    Manages every thing in the world
    """

    def __init__(self, context):
        """
        :param context:{
            number of computers,
            intrude_rate,
            secure_rate,
            damage_rate,
            repair_rate
        } all in days
        """
        self._m = int(context[0])
        self.intrude_rate = int(context[1])
        self.secure_rate = int(context[3])
        self.damage_rate = int(context[4])
        self.repair_rate = int(context[5])


        self._computers = []
        self.intruded = []
        self.exfiltrate = []
        self.secure = []
        self.damaged = []

        self.log = []
        self.d_log = []
        self.e_log = []
        self.s_log = []
        self.i_log = []
        self.v_log = []

        # create a legend at top left corner
        self.legend = []
        for _ in range(self.lenComputers):
            v = pygame.Vector2()
            v.x = random.randint(Computer.w*10, Setting.screen_w)
            v.y = random.randint(Computer.h*10, Setting.screen_h)
            self._computers.append(Computer(v, Setting.colors['red']))


        self.states = list(map(lambda x:x.state, self.getComputers))

        self.createLegend()

    def __del__(self):
        """
        create a graph of the simulation once
        sim is destroyed
        """
        plt.title(f"Intrude_Rate: {self.intrude_rate} "
                  f"Fixing_Rate: {self.secure_rate} "
                  f"Damage_Rate: {self.damage_rate} "
                  f"Repair_Rate: {self.repair_rate}")
        plt.xlabel("Time")
        plt.ylabel("State of computers")
        plt.plot(self.log, self.s_log, label="Secured")
        plt.plot(self.log, self.i_log, label="Intruded")
        plt.plot(self.log, self.d_log, label="Damaged")
        plt.plot(self.log, self.e_log, label="Exfiltrated")
        plt.plot(self.log, self.v_log, label='Vulnerable')
        plt.legend()
        plt.show()

    def getClock(self):
        """
        time counting
        """
        return pygame.time.get_ticks()

    def stateChange(self):
        """
        change the state of the computer
        """
        clock = self.getClock()//CLOCK_TICK

        self.log.append(clock)
        self.d_log.append(len(self.damaged))
        self.e_log.append(len(self.exfiltrate))
        self.i_log.append(len(self.intruded))
        self.s_log.append(len(self.secure))
        self.v_log.append(len(self.getComputers))

        rand_state = random.randint(0, 2)
        state = [self.getComputers, self.intruded, self.exfiltrate]

        if len(self.getComputers) > 0 and \
            clock != 0 and clock%self.intrude_rate == 0:
            self.getComputers[0].state = State.INTRUDED
            self.getComputers[0].clock = clock
            self.intruded.append(self.getComputers.pop(0))

        if len(state[rand_state]) > 0 and \
            clock !=0 and clock%self.secure_rate==0:
                state[rand_state][0].state = State.SECURE
                self.secure.append(state[rand_state].pop(0))

        if len(self.intruded) > 0 and \
            clock%LAMBDA_J(len(self.intruded)) == 0:
            self.intruded[0].clock = clock
            self.intruded[0].state = State.EXFILTRATED
            self.intruded[0].i_computers = len(self.intruded)
            self.exfiltrate.append(self.intruded.pop(0))

        if len(self.exfiltrate) > 0 and \
            clock%self.damage_rate == 0:
            print(self.exfiltrate)
            self.exfiltrate[0].state = State.DAMAGED
            self.damaged.append(self.exfiltrate.pop(0))

        if len(self.damaged) > 0 and \
            clock%self.repair_rate == 0:
            self.damaged[0].state = State.EXFILTRATED
            self.exfiltrate.append(self.damaged.pop(0))


    def update(self):
        for computer in self._computers:
            computer.update()
        for intrude in self.intruded:
            intrude.update()
        for secure in self.secure:
            secure.update()
        for exfiltrate in self.exfiltrate:
            exfiltrate.update()
        for damaged in self.damaged:
            damaged.update()
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


