import collision
from pico2d import *
import play_state
import game_framework
import end_state

class Ball:
    def __init__(self):
       self.image = load_image('ball.png')
       self.frame = 0
       self.x = 400
       self.y = 500
       self.to_x = 0
       self.to_y = 6
       self.init_spd_y = 30
       self.Lfont = load_font('ENCR10B.TTF', 75)
       self.Lpoint = 0
       self.Rfont = load_font('ENCR10B.TTF', 75)
       self.Rpoint = 0

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y, 50, 50)
        self.Lfont.draw(100, 550, str(self.Lpoint), (255, 0, 0))
        self.Rfont.draw(700, 550, str(self.Rpoint), (255, 0, 0))
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 5
        if (collision.collide(self, play_state.pikachu)):
            self.init_spd_y = 20
            self.to_x = 5
            self.to_y = self.init_spd_y
            if(play_state.pikachu.jump == 1):
                self.init_spd_y = 30
                self.to_x = 23
                self.to_y = self.init_spd_y
                if(play_state.pikachu.locate == 6):
                    self.init_spd_y = 40
                    self.to_x = 40
                    self.to_y = self.init_spd_y
        if (collision.collide(self, play_state.pikachu2)):
            self.init_spd_y = 20
            self.to_x = -5
            self.to_y = self.init_spd_y
            if(play_state.pikachu2.jump == 1):
                self.init_spd_y = 30
                self.to_x = -23
                self.to_y = self.init_spd_y
                if (play_state.pikachu2.locate == 6):
                    self.init_spd_y = 40
                    self.to_x = -40
                    self.to_y = self.init_spd_y
        if (collision.collide(self, play_state.netTop)):
            self.to_x = -self.to_x
            self.to_y = 5
        if (collision.collide(self, play_state.net)):
            self.to_x = -self.to_x
            self.to_y = -16

        if self.x <= 50 or self.x >= 750:
            self.to_x = -self.to_x
        if self.y < 40:
            self.to_y = self.init_spd_y
            self.init_spd_y -= 2
        else:
            self.to_y -= 0.5
        if self.y >= 580:
            self.to_y = -self.to_y
        self.x += self.to_x
        self.y += self.to_y
        if self.x > 400 and self.y < 40:
            print("bottom")
            self.x = 650
            self.y = 300
            play_state.pikachu2.x = 650
            play_state.pikachu.x = 150
            play_state.pikachu.time = 0
            self.Lpoint += 1
            self.to_x = 0
            delay(1)
        if self.x < 400 and self.y < 40:
            print("bottom")
            self.x = 150
            self.y = 300
            play_state.pikachu2.x = 650
            play_state.pikachu.x = 150
            play_state.pikachu.time = 0
            self.Rpoint += 1
            self.to_x = 0
            delay(2)

        if self.Lpoint == 5 or self.Rpoint == 5:
            game_framework.change_state(end_state)

