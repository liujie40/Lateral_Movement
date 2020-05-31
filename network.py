from settings import *
import time

class Computer:

    def __init__(self):
        # first state of a computer
        self._state = State.VULNERABLE


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


