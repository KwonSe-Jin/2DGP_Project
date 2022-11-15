from pico2d import*
import collision
import os
import play_state

class Pikachu_R:
    def __init__(self):
        self.x = 650
        self.y = 70
        self.frame = 0
        self.frame2 = 5
        self.image = load_image('Pikachu'+'_R'+'.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0

    def update(self):
        self.frame = (self.frame + 1) % self.frame2
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
        if (collision.collide(play_state.pikachu2, play_state.net)):
            play_state.pikachu2.x = 450

    def draw(self):
        if self.locate:
            self.image.clip_draw(self.frame*64, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(0, 320, 64, 64, self.x, self.y, 100, 100)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 40








