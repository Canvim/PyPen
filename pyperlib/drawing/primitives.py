from pyperlib.drawing.color import Color
from pyperlib.__main__ import display

import pygame

def clear_screen():
    fill_screen("default_background_color")

def clear():
    clear_screen()

def fill_screen(color="default_background_color"):
    rectangle(0, 0, 10000, 10000, color)

def fill(color="default_background_color"):
    fill_screen(color=color)

def rectangle(x, y, width, height, color="default_color"):
    color = Color.from_user_input(color)

    pygame.draw.rect(display, color.rgba(), (int(x), int(y), int(width), int(height)))

def circle(x, y, radius, color="default_color"):
    color = Color.from_user_input(color)

    pygame.draw.circle(display, color.rgba(), (int(x), int(y)), int(radius))