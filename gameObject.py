from settings import Setting,pygame

class GameObject(Setting):
    """
    blueprint for every in world object
    """
    def __init__(self, pos:pygame.Vector2, color):
        super().__init__()
        self.pos = pos
        self.color = color

    def draw(self):
        pass

    def move(self):
        pass

    def control(self):
        pass

    def update(self):
        self.draw()
        self.move()
        self.control()