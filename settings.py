from enum import Enum
import pygame
from pygame.locals import *
from abc import ABC

class Setting(ABC):

    colors = {
        "white":(0xff,0xff,0xff),
        "black":(0,0,0),
        "red":(0xff,0,0),
        "green":(0,0xff,0),
        'yellow':(0xff,0xff,0),
        'purple':(0xff,0,0xff),
        "blue":(0,0,0xff),
    }

    screen_w = 600
    screen_h = 600

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', 12)
        self.font2 = pygame.font.SysFont('arial', 20)


        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption("Simulation")

        self.scene = []


class State(Enum):
    VULNERABLE = 0
    INTRUDED = 1
    EXFILTRATED = 2
    SECURE = 3
    DAMAGED = 4


