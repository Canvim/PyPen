from pypen import *
from pypen import _COLORS

def start():
    settings.fps = 120


colors = []

colors += _COLORS.values()
colors += _COLORS.keys()


def update():
    global colors
    clear()
    i = 0
    radius = 10
    for x, y in grid(radius*2):
        circle(x, y + cos(TIME*2 + x*0.1)*10, radius, colors[i])
        i += 1
        i %= len(colors)
