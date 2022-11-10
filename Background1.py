from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass

class Net:
    def __init__(self):
        self.net = load_image('net.png')
        self.x = 400
        self.y = 150
    def draw(self):
        self.net.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.x - 5, self.y - 125, self.x + 5, self.y + 125