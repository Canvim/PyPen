from pypen import *


def start():
    settings.fps = 5


def update():
    fill("#E33050")
    draw_pattern()


def draw_pattern():
    for i in range(0, 100):
        for j in range(0, 100):
            if random(1) > 0.5:
                rectangle(i*10, j*10, 8, 8, "#F34060")
