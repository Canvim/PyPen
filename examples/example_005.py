from pypen import *


def start():
    for x, y in pixels():
        rectangle(x, y, 1, 1, (random(255), random(255), random(255)))
