from pyperlib import *


def start():
    settings.fps = 70

t = 0

def update():
    global t
    clear()
    rectangle(sin(t*0.1) * 100, 20, 300, 100)

    t = t + 1
