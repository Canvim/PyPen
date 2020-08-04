from pypen import *


def start():
    settings.fps = 60

def update():
    save()
    translate(WIDTH/2, HEIGHT/2)

    x1 = 200 * cos(TIME - 10 * sin(TIME)) * cos(TIME)
    y1 = 200 * sin(TIME - FRAME/10) * sin(TIME)

    x2 = 200 * cos(TIME + FRAME ** 0.5) * cos(TIME-0.5)
    y2 = 200 * sin(TIME + FRAME/10 - 10*cos(TIME/10)) * sin(TIME - 0.5)

    line(x1, y1, x2, y2, (150, 30, 230, 10), 0.2)

    restore()
