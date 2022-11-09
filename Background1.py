from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.net = load_image('net.png')
    def draw(self):
        self.image.draw(400, 300)
        self.net.draw(400, 150)

    def update(self):
        pass