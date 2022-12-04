import game_framework
from pico2d import *
import play_state
import game_world
import title_state
image1 = None

def enter():
    global image1
    image1 = load_image('Select.png')
    pass
def exit():
    global image1
    del image1
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            game_framework.change_state(play_state)
            play_state.pikachu.z = 1
            game_world.remove_object(play_state.squirtle2)
            game_world.remove_object(play_state.squirtle)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            game_framework.change_state(play_state)
            play_state.squirtle.c = 1
            game_world.remove_object(play_state.pikachu)
            game_world.remove_object(play_state.pikachu2)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image1.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
