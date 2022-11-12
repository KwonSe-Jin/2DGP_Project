import random
import collision
import Move
from pico2d import *
import play_state
import Background1
import math
import game_framework
import title_state
class Ball:
    def __init__(self):
       self.image = load_image('ball.png')
       self.x = 400
       self.y = 500
       self.frame = 0
       self.b_speedx = 10
       self.b_speedy = 10
       self.font = load_font('ENCR10B.TTF', 50)
       self.point = 0

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y, 50, 50)
        self.font.draw(100, 550, str(self.point), (255, 255, 250))
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += self.b_speedx
        self.y += self.b_speedy
        if self.x <= 50:
            self.b_speedx = -self.b_speedx
            self.x = 50
        elif self.x >= 750:
            self.b_speedx = -self.b_speedx
            self.x = 750
        if self.y <= 50:
            self.b_speedy = -self.b_speedy
            self.y = 50
        elif self.y >= 550:
            self.b_speedy = -self.b_speedy
            self.y = 550
        if  self.x > 400 and self.y <= 50:
            print("bottom")
            self.point += 1

        if (collision.collide(self, play_state.pikachu)):
            self.b_speedx = -self.b_speedx
            self.b_speedy = -self.b_speedy
        if (collision.collide(self, play_state.pikachu2)):
            self.b_speedx = -self.b_speedx
            self.b_speedy = -self.b_speedy
        if (collision.collide(self, play_state.net)):
            self.b_speedx = -self.b_speedx
            self.b_speedy = -self.b_speedy

        if self.point == 5:
            game_framework.change_state(title_state)
