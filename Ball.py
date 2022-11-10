import random
import collision
import Move
from pico2d import *
import play_state
import math

class Ball:
    def __init__(self):
       self.image = load_image('ball.png')
       self.x = random.randint(100, 200)
       self.y = random.randint(350, 450)
       self.frame = 0
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.y -= 7
        if self.y < 90:
            self.y += 550
        if (collision.collide(self, play_state.pikachu)):
            self.x += 150
            self.y += 250
        if (collision.collide(self, play_state.pikachu2)):
            self.x -= 150
            self.y += 250