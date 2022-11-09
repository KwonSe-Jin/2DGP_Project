from pico2d import *
from Background1 import Background
from Move import Move
import game_framework
import title_state

def handle_events():
    global running
    global dirx
    global diry
    global locate
    global frame2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    pikachu.dirx = 1
                    pikachu.locate = 5
                    pikachu.frame2 = 5
                elif event.key == SDLK_a:
                    pikachu.dirx = -1
                    pikachu.locate = 5
                    pikachu.frame2 = 5
                elif event.key == SDLK_s:
                    pikachu.dirx = 10
                    pikachu.locate = 2
                    pikachu.frame2 = 3
                elif event.key == SDLK_w:
                    if pikachu.jump == 0:
                        pikachu.jump = 1
                        pikachu.locate = 4
                elif event.key == SDLK_LEFT:
                    pikachu2.dirx = -1
                    pikachu2.locate = 5
                elif event.key == SDLK_RIGHT:
                    pikachu2.dirx = 1
                    pikachu2.locate = 5
                elif event.key == SDLK_DOWN:
                    pikachu2.dirx = -10
                    pikachu2.locate = 2
                    pikachu2.frame2 = 3
                elif event.key == SDLK_UP:
                    if pikachu2.jump == 0:
                        pikachu2.jump = 1
                        pikachu2.locate = 4
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_a or event.key == SDLK_s:
                pikachu.dirx = 0
                pikachu.locate = 0
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_DOWN:
                pikachu2.dirx = 0
                pikachu2.locate = 0
            elif event.key == SDLK_w or event.key == SDLK_UP:
                pikachu.locate = 0
                pikachu2.locate = 0
            # pikachu.jump = 0

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


pikachu = None
pikachu2 = None
back = None
running = None
# 초기화
def enter():
    global pikachu, pikachu2, back, running
    pikachu = Move(100, False)
    pikachu2 = Move(700, True)
    back = Background()
    running = True
# 종료
def exit():
    global pikachu, pikachu2, back
    del pikachu
    del pikachu2
    del back
def update():
    pikachu.update()
    pikachu2.update()
def draw():
    clear_canvas()
    back.draw()
    pikachu.draw()
    pikachu2.draw()
    update_canvas()
    delay(0.03)