from pyperlib import *


def update():
    fill((10, 200, 100))

    x = sin(TIME) * 50 + 100
    rectangle(x, 100, 200, 150, "red")
