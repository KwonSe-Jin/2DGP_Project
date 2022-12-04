from pico2d import *
import game_framework
import title_state
def enter():
    global image2
    image2 = load_image('End.png')

def exit():
    global image2
    del image2

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def draw():
    clear_canvas()
    image2.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass