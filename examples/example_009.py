from pypen import *


def start():
    settings.fps = 60


def update():
    fill_screen("#343434")

    begin_shape()
    vertex(40, 40)
    vertex(40, 140)
    vertex(FRAME, 140)
    end_shape("red")

    begin_shape()
    vertex(40+FRAME, 240+FRAME)
    vertex(40, 340)
    vertex(FRAME, 340)
    vertex(340, 280)

    end_shape("yellow", "blue", 5)

    reset_style()

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
    reset_style()
