from pypen import *


def start():
    settings.fps = 70


def update():
    clear()
    arc(WIDTH/2, HEIGHT/2, HEIGHT/4, PI*sin(TIME+1.6), PI*sin(TIME), fill_color=None, stroke_color="blue", stroke_width=5)
