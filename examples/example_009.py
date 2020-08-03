from pypen import *


def start():
    settings.fps = 60


def update():
    fill_screen("#343434")

    angle = 0
    points = 10 + sin(TIME*2)*5
    radius = 100

    save()
    translate(WIDTH/2, HEIGHT/2)

    begin_shape()

    while angle <= TAU:
        angle += TAU/points
        vertex(sin(angle)*radius, cos(angle)*radius)

    end_shape("orange")
    restore()
