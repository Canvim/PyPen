from pyperlib import *

def start():
    settings.fps = 60

my_colors = [color for name, color in colors.__dict__.items() if not callable(color)]

x = 100
frame = 0

def update():
    global frame
    fill(Color.from_rgb255(190, 90, 180))

    i = 0
    for color in (my_colors*4):

        rectangle(i*30, 30 + sin(0.1*(frame + i*10))*20, 30, 200, color)
        i += 1

    frame = frame + 1
