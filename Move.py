from pico2d import*
import collision
import os
import play_state
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2DGP_Project\\resource')

class Pika:
    def __init__(self, x, isReverse = False):
        self.x = x
        self.y = 95
        self.frame = 0
        self.frame2 = 5
        self.isReverse = isReverse
        if isReverse:
            self.image = load_image('Pikachu'+'_R'+'.png')
        else:
            self.image = load_image('Pikachu.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0
        self.isskill = 0

    def update(self):
        self.frame = (self.frame + 1) % self.frame2
        self.x += self.dirx * 5
        if self.jump == 1:
            self.y += 15
            if self.y >= 400:
                self.jump = -1
        elif self.jump == -1:
            self.y -= 15
            if self.y <= 95:
                self.jump = 0
        else:
            self.y = 95
        if (collision.collide(play_state.pikachu, play_state.net)):
            play_state.pikachu.x = 350
        if (collision.collide(play_state.pikachu2, play_state.net)):
            play_state.pikachu2.x = 450



    def draw(self):
        if self.locate:
            self.image.clip_draw(self.frame*64, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(0, 320, 64, 64, self.x, self.y, 100, 100)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 30, self.y + 10, self.x + 40, self.y + 50





