from pypen import *


def start():
    settings.fps = 70


def update():
    fill_screen("#E33050")
    i = 0
    for x, y in grid(50):
        i += 1
        offset_x = cos(TIME + y + i) * 10
        offset_y = sin(TIME + x + i) * 10

        circle(x + offset_x, y + offset_y, abs(sin(TIME + i) * 20) + 1, "#F34060")
