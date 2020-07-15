from pyperlib import *


def start():
    settings.fps = 70

t = 0

def update():
    global t
    clear()
    arc(320, 240, 600, 400, PI*sin(t*1.2+1.6), PI*sin(t))

    t = t + 0.014
