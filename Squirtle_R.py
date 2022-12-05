from pico2d import*
import collision
import os
import play_state
import game_framework
import end_state

class Squirtle_R:
    def __init__(self):
        self.x = 150
        self.y = 70
        self.frame = 0
        self.frame2 = 5
        self.image = load_image('Squirtle.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0
        self.win = False
        self.lose = False
        self.celebrete = 0


    def update(self):
        self.frame = (self.frame + 1) % self.frame2

        if self.lose == False and self.win == False:
            self.x += self.dirx * 5
            if self.jump == 1:
                self.y += 15
                if self.y >= 400:
                    self.jump = -1
            elif self.jump == -1:
                self.y -= 15
                if self.y <= 70:
                    self.jump = 0
            else:
                self.y = 70
            if (collision.collide(play_state.squirtle2, play_state.net)):
                play_state.squirtle2.x = 350
        if (play_state.point.Lpoint == 2):
            self.win = True
            self.locate = 4
            self.frame2 = 3
            self.celebrete += 1
        elif (play_state.point.Rpoint == 2):
            self.lose = True
            self.locate = 5
            self.frame2 = 5
            self.celebrete += 1

    def draw(self):
        if self.lose == False and self.win == False:
            if self.locate:
                self.image.clip_composite_draw(self.frame * 64, self.locate * 64, 64, 64, 0, 'h',self.x, self.y, 120, 120)
            else:
                self.image.clip_composite_draw(0, 0, 64, 64, 0, 'h',self.x, self.y, 120, 120)
        elif self.win == True:
            self.image.clip_composite_draw(self.frame * 64, self.locate * 64, 64, 64, 0, 'h', self.x, self.y, 120, 120)
            delay(0.05)
        elif self.lose == True:
            self.image.clip_composite_draw(256, self.locate * 64, 64, 64, 0, 'h', self.x, self.y, 120, 120)
            delay(0.05)
        if self.celebrete == 50:
            game_framework.change_state(end_state)
    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 40, self.y + 40