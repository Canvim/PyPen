from pypen import *


def start():
    settings.fps = 120


def update():
    fill("grey")
    rectangle(100 + sin(TIME) * 50, 50, 200, 100, "red")
