from pico2d import*
import collision
import os
import play_state
import end_state
import game_framework
os.chdir('C:\\Users\\sejin\\Documents\\GitHub\\2DGP_Project\\resource')

class Pika:
    def __init__(self):
        self.x = 150
        self.y = 70
        self.frame = 0
        self.frame2 = 5
        self.image = load_image('Pikachu.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0
        self.time = 0
        self.win = False
        self.lose = False
        self.celebrete = 0
        self.qjump = 0
        self.font = load_font('ENCR10B.TTF', 25)
        self.time = 0
    def update(self):
        self.frame = (self.frame + 1) % self.frame2

        if self.time < 100:
            self.time += 1
        else:
            self.time = 100
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

            if (collision.collide(play_state.pikachu, play_state.net)):
                play_state.pikachu.x = 350

        if(play_state.point.Lpoint == 2):
                self.win = True
                self.locate = 1
                self.frame2 = 5
                self.celebrete += 1

        elif (play_state.point.Rpoint == 2):
                self.lose = True
                self.locate = 0
                self.frame2 = 5
                self.celebrete += 1

    def draw(self):
        if self.lose == False and self.win == False:
            if self.locate:
                self.image.clip_draw(self.frame*64, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
            else:
                self.image.clip_draw(0, 320, 64, 64, self.x, self.y, 100, 100)
        elif self.win == True:
            self.image.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
            delay(0.05)
        elif self.lose == True:
            self.image.clip_draw(256, self.locate * 64, 64, 64, self.x, self.y, 100, 100)
            delay(0.05)
        # draw_rectangle(*self.get_bb())
        self.font.draw(self.x, self.y + 60, str(self.time), (255, 0, 255))

        if self.celebrete == 50:
            game_framework.change_state(end_state)




    def get_bb(self):
        return self.x - 10, self.y - 30, self.x + 40, self.y + 40
