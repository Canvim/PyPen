from pypen import *


def start():
    settings.fps = 5


def update():
    fill_screen("#E33050")
    draw_pattern()


def draw_pattern():
    for x, y in grid(spacing=10):
        if random() > 0.5:
            rectangle(x, y, 8, 8, "#F34060")
