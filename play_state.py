from pico2d import *
from Background1 import Background
from Pikachu import Pika
from Pikachu_R import Pikachu_R
import game_framework
import game_world
from Ball import Ball
from Background1 import Net
from Background1 import NetTop
from point import Point
from Squirtle_R import Squirtle_R
from Squirtle import Squirtle
import title_state

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    pikachu.dirx = 1
                    pikachu.locate = 5
                    pikachu.frame2 = 5
                    squirtle2.dirx = 1
                    squirtle2.locate = 3
                elif event.key == SDLK_a:
                    pikachu.dirx = -1
                    pikachu.locate = 5
                    pikachu.frame2 = 5
                    squirtle2.dirx = -1
                    squirtle2.locate = 3
                elif event.key == SDLK_s:
                    pikachu.dirx = 10
                    pikachu.locate = 2
                    pikachu.frame2 = 3
                    squirtle2.dirx = 5
                    squirtle2.locate = 2
                elif event.key == SDLK_w:
                    if pikachu.jump == 0:
                        pikachu.jump = 1
                        pikachu.locate = 4
                    if squirtle2.jump == 0:
                        squirtle2.jump = 1
                        squirtle2.locate = 1
                elif event.key == SDLK_q:
                    if pikachu.time >= 10:
                        pikachu.jump = 1
                        pikachu.locate = 6
                        pikachu.time = 0
                elif event.key == SDLK_LEFT:
                    pikachu2.dirx = -1
                    pikachu2.locate = 5
                    squirtle.dirx = -1
                    squirtle.locate = 3
                elif event.key == SDLK_RIGHT:
                    pikachu2.dirx = 1
                    pikachu2.locate = 5
                    squirtle.dirx = 1
                    squirtle.locate = 3
                elif event.key == SDLK_DOWN:
                    pikachu2.dirx = -10
                    pikachu2.locate = 2
                    pikachu2.frame2 = 3
                    squirtle.dirx = - 5
                    squirtle.locate = 2
                elif event.key == SDLK_UP:
                    if pikachu2.jump == 0:
                        pikachu2.jump = 1
                        pikachu2.locate = 4
                    if squirtle.jump == 0:
                        squirtle.jump = 1
                        squirtle.locate = 1
                elif event.key == SDLK_p:
                    if pikachu2.time >= 10:
                        pikachu2.jump = 1
                        pikachu2.locate = 6
                        pikachu2.time = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_a or event.key == SDLK_s:
                pikachu.dirx = 0
                pikachu.locate = 0
                squirtle2.dirx = 0
                squirtle2.locate = 0
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_DOWN:
                pikachu2.dirx = 0
                pikachu2.locate = 0
                squirtle.dirx = 0
                squirtle.locate = 0
            elif event.key == SDLK_w or event.key == SDLK_UP or event.key == SDLK_p:
                pikachu.locate = 0
                pikachu2.locate = 0
                squirtle.locate = 0
                squirtle2.locate = 0
            elif event.key == SDLK_q:
                pikachu.locate = 0
                pikachu2.locate = 0

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

pikachu = None
pikachu2 = None
back = None
ball = None
net = None
running = None
netTop = None
point = None
squirtle = None
squirtle2 = None
# 초기화
def enter():
    global pikachu, pikachu2, back, running, ball, net, netTop, point, squirtle2, squirtle
    pikachu = Pika()
    pikachu2 = Pikachu_R()
    ball = Ball()
    back = Background()
    net = Net()
    netTop = NetTop()
    point = Point()
    squirtle = Squirtle()
    squirtle2 = Squirtle_R()
    game_world.add_object(back, 0)
    game_world.add_object(pikachu, 1)
    game_world.add_object(squirtle2, 1)
    game_world.add_object(ball, 3)
    game_world.add_object(pikachu2, 2)
    game_world.add_object(squirtle, 2)
    game_world.add_object(net, 4)
    game_world.add_object(netTop, 5)
    game_world.add_object(point, 6)
# 종료
def exit():
    global pikachu, pikachu2, back, ball, net, netTop, point, squirtle, squirtle2
    del pikachu, pikachu2, back, ball, net, netTop, point, squirtle, squirtle2
    game_world.clear()
def update():
    # pikachu.
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.03)

def pause():
    pass

def resume():
    pass

# def test_self():
#     import play_state
#     pico2d.open_canvas()
#     game_framework.run(play_state)
#     pico2d.clear_canvas()
#
# if __name__ == '__main__':
#     test_self()