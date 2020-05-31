from enum import Enum
import pygame
from pygame.locals import *

class Setting:

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

M = 3 # number of computers
I =  0 # Intruded computers
J = 0 # Exfiltrated Intruded computers

BETA_I = 2 # Mean time to intrude in days

LAMBDA_J = lambda j: 4 + 2 * j # Mean time to comprise J intruded computers in days
MU_J = lambda j: 2 * j # Mean time for finishing data exfiltration on j Intruded computers in days

FIXING_RATE = 2 #days
DAMAGING_RATE = 10 # days
REPAIRING_RATE = 2 # days

ENTRY_WIDTH_UI = 10
FPS = 60

