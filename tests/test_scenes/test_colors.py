from pyperlib import *

def start():
    settings.fps = 120

colors = ["#343434",
         "#a3",
         "rgb(110, 20, 30)",
         "rgba(40, 120, 160, 103)",
         "rgb(56, 78, 23)",
         "red",
         "green",
         "blue",
         (0),
         (255, 0 ,0),
         (190),
         120,
         100000.0,
         (1000.345, 23423423.2, 23.0),
         30]

colors = colors*2

def update():
    global colors
    clear()

    i = 0
    for color in colors:
        y = 30 + sin(0.3*(TIME*8 + i))*20

        d = 640/len(colors)

        rectangle(i*d, y, 30, 200, color)
        circle(i*d, y + 20, 40, color)
        circle(i*d, y + 280, 40, color)
        i += 1
