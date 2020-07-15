from pyperlib import *

def start():
    settings.fps = 60

frame = 0

def update():
    global frame
    # fill(Color.from_rgb255(190, 90, 180))
    clear()

    i = 0
    for color in ["red", "green", "blue", (0), (255, 0 ,0), (190)]*5:
        y = 30 + sin(0.1*(frame + i*10))*20
        rectangle(i*30, y, 30, 200, color)

        circle(i*30, y + 20, 40, color)

        circle(i*30, y + 280, 40, color)
        i += 1

    frame = frame + 1
