from pypen import *


def pseudo_random(seed: float):
    return abs(sin(seed % 478562)*cos(seed % 3579))

def update():
    clear_screen()

    i = 0
    offset_y = TIME*170

    for x, y in grid(spacing=30):
        seed = i+x*y

        actual_y = (y + offset_y) % HEIGHT - 30
        percentage = (1-(actual_y/HEIGHT)**5)
        color = (80, 130, 50, pseudo_random(seed)*255*percentage)

        circle(x, actual_y, pseudo_random(seed)*14*percentage, color)

        i += 1
