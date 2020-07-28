from pypen import *
from math import sqrt

def start():
    settings.fps = 5


def update():
    pixel_size = 2
    points = []
    for i in range(3):
        points.append((random(WIDTH), random(HEIGHT)))

    for x, y in grid(pixel_size):

        least_dis = 1000000000000000000

        for point in points:
            d = sqrt((x - point[0])**2 + (y - point[1])**2)
            least_dis = d if d < least_dis else least_dis

        value = clamp(remap(least_dis, 0, 300, 255, 0), 0, 255)
        color = (value, 30, 125 + 125 * sin((value**3) / 170000))
        rectangle(x, y, pixel_size, pixel_size, color)
