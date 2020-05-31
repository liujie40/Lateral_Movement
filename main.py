from ui import *
from network import System

def main():
    root = Tk()
    # give a title
    root.title("Lateral Movement Attacks")
    root.geometry("300x300")
    ui = UI(root)
    root.mainloop()



if __name__ == "__main__":
    main()
    a = System()
    print(a.getComputers)
    print(a.states)
