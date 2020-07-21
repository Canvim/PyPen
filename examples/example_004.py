from pypen import *
from math import sqrt


def start():
    settings.fps = 1


def update():
    points = []
    for i in range(10):
        points.append((random(640), random(480)))

    for x, y in pixels():
        least_dis = 1000000000000000000
        for point in points:
            d = sqrt((x - point[0])**2 + (y - point[1])**2)
            least_dis = d if d < least_dis else least_dis

        val = clamp(remap(least_dis, 0, 300, 255, 0), 0, 255)
        color = ( val, 30, 125 + 125 * sin( (val**3) / 170000 ))
        rectangle(x, y, 1, 1, color)

