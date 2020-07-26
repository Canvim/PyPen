from pypen import *


def start():
    rectangle(0, 0, 100, 100, "red")


def update():
    fill_screen("blue")
    rectangle(100 + sin(TIME*5) * 50, 50, 200, 100, "red")
