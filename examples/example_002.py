from pypen import *


def start():
    settings.fps = 70


def update():
    clear()
    arc(320, 240, 600, 400, PI*sin(TIME+1.6), PI*sin(TIME))
