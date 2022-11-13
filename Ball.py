import random
import collision
import Move
from pico2d import *
import play_state
import Background1
from math import *
import game_framework
import title_state


class Ball:
    def __init__(self):

       self.image = load_image('ball.png')
       self.frame = 0
       self.x = 150
       self.y = 300
       self.to_x = 3
       self.to_y = -6
       # self.init_spd_x = 10
       self.init_spd_y = 30
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
        if self.x <= 50 or self.x >= 750:
            self.to_x = -self.to_x
        if self.y < 50:
            self.to_y = self.init_spd_y
            self.init_spd_y -= 2
        else:
            self.to_y -= 0.5
        if self.y >= 580:
            self.to_y = -self.to_y
        self.x += self.to_x
        self.y += self.to_y
        # if self.x > 400 and self.y < 50:
        #     print("bottom")
        #     self.point += 1

        if (collision.collide(self, play_state.pikachu)):
            self.to_x = -self.to_x
            self.to_y = self.init_spd_y
            self.init_spd_y = 16
        if (collision.collide(self, play_state.pikachu2)):
            self.to_x = -self.to_x
            self.to_y = self.init_spd_y
            self.init_spd_y = 16
        # if (collision.collide(self, play_state.net)):
        #     self.init_spd_x = -self.init_spd_x
        #     self.init_spd_y = -self.init_spd_y

        if self.point == 5:
            game_framework.change_state(title_state)
