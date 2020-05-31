from tkinter import *
from tkinter import ttk
from network import System
from settings import *

class UI:

    def __init__(self, master):
        self.system = System()

        self.labels = ["# Computers", "Mean time to intrude",
                       "Fixing_Rate", "Damaging_Rate", "Repairing_Rate"]

        self.labels = list(map(lambda x:ttk.Label(text=x), self.labels))
        self.default_values = (M, BETA_I, FIXING_RATE, DAMAGING_RATE, REPAIRING_RATE)

        self.entries = [ttk.Entry(width=ENTRY_WIDTH_UI) for _ in range(len(self.labels))]


        self.play_button = ttk.Button(master, text="Play", command=self.simulate)

        self.setLayout()

    def setLayout(self):

        for index, label in enumerate(self.labels):
            label.grid(row=index)
            self.entries[index].insert(END, str(self.default_values[index]))
            self.entries[index].grid(row=index, column=1)

        origin = len(self.labels)
        self.play_button.grid(row=origin)


    def simulate(self):
        print("....simulation is starting....")
        

