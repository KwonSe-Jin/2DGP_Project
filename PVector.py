from pico2d import *

class PVector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vel):
        self.x += vel.x
        self.y += vel.y