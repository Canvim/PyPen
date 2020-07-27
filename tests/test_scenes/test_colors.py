from pypen import *


def start():
    settings.fps = 120


colors = ["0xF2Fab4",
          "#343434",
          "#a3",
          "rgb(110, 20, 30)",
          "rgba(40, 120, 160, 103)",
          "rgb(56, 78, 23)",
          "red",
          "green",
          "blue",
          "orange",
          "purple",
          "yellow",
          "cyan",
          [24],
          [35, 123, 0],
          (0),
          (255, 0, 0),
          (190),
          120,
          100000.0,
          (1000.345, 23423423.2, 23.0),
          30,
          [35, 123, 0, 34],
          [35, 123, 0, 200]]*3


def update():
    global colors
    clear()
    rectangle(0, 0, WIDTH, HEIGHT/2, colors[0])
    rectangle(0, HEIGHT/2, WIDTH, HEIGHT/2, colors[len(colors)-1])

    i = 0
    for color in colors:
        y = 80 + sin(0.3*(TIME*8 + i))*20

        d = WIDTH/len(colors)

        rectangle(i*d, y, 30, 200, color)
        circle(i*d, y + 20, 40, color)
        circle(i*d, y + 280, 40, color)
        i += 1
