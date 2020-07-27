from pypen import *


def start():
    settings.fps = 70


def update():
    clear()
    arc(320, 240, 150, PI*sin(TIME+1.6), PI*sin(TIME), "blue")
