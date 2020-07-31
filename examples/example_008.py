from pypen import *


def start():
    settings.fps = 60


def update():
    fill_screen("orange")

    save()
    translate(60, 60)
    rotate(T*2.5)
    ellipse(0, 0, 50, 30, "red", "blue", 3)
    restore()

    save()
    translate(200, 200)
    rotate(T*1.5+0.5)
    ellipse(40*sin(T), 0, 30, 50, stroke_width=10)
    restore()

    save()
    translate(400, 300)
    rotate(T)
    ellipse(0, 100*cos(T*2), 30, 100, "green")
    restore()
