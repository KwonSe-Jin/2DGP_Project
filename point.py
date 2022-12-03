from pico2d import *
import play_state

class Point:
    def __init__(self):
        self.Lfont = load_font('ENCR10B.TTF', 75)
        self.Lpoint = 0
        self.Rfont = load_font('ENCR10B.TTF', 75)
        self.Rpoint = 0

    def draw(self):
        self.Lfont.draw(100, 550, str(self.Lpoint), (255, 0, 0))
        self.Rfont.draw(630, 540, str(self.Rpoint), (255, 0, 0))

    def update(self):
        if play_state.ball.x > 400 and play_state.ball.y < 40:
            print("L_bottom")
            play_state.ball.x = 650
            play_state.ball.y = 550
            play_state.pikachu2.x = 650
            play_state.squirtle.x = 650
            play_state.squirtle2.x = 150
            play_state.pikachu.x = 150
            play_state.pikachu.jump = 0
            play_state.pikachu2.jump = 0
            play_state.squirtle2.jump = 0
            play_state.squirtle.jump = 0
            self.Lpoint += 1
            play_state.ball.to_x = 0
            play_state.ball.to_y = 0
            delay(1)
        if play_state.ball.x < 400 and play_state.ball.y < 40:
            print("R_bottom")
            play_state.ball.x = 650
            play_state.ball.y = 550
            play_state.pikachu2.x = 650
            play_state.squirtle.x = 650
            play_state.squirtle2.x = 150
            play_state.pikachu.x = 150
            play_state.pikachu.jump = 0
            play_state.pikachu2.jump = 0
            play_state.squirtle2.jump = 0
            play_state.squirtle.jump = 0
            self.Rpoint += 1
            play_state.ball.to_x = 0
            play_state.ball.to_y = 0
            delay(1)