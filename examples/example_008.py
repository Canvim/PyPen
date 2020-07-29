from pypen import *


def start():
    settings.fps = 60


def update():
    fill_screen("orange")
    ellipse(50, 40, 50, 30, "red", "blue", 3)

    ellipse(200, 200, 30, 50, stroke_width=10)

    ellipse(400, 400, 30, 100, "green")
