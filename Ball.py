import random

from pico2d import *
import math

class Ball:
    def __init__(self):
        self.image = load_image('ball_0.png')
        self.x = 200
        self.y = 350
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25