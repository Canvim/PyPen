from pypen import *


def update():
    global n, fps
    fill_screen("blue")
    rectangle(100 + sin(TIME*5) * 50, 50, 200, 100, "red")
