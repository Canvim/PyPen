from pyperlib import *

def start():
    settings.fps = 5


def update():
    for i in range(0, 100):
        for j in range(0, 100):
            rectangle(i*10, j*10, 5, 5)
    