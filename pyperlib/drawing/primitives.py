from pyperlib.drawing.color import Color
from pyperlib.__main__ import display

import pygame

def clear_screen():
    color = Color.from_user_input("default_background_color")
    display.fill(color.rgb())

def clear():
    clear_screen()

def fill_screen(color="default_background_color"):
    display.fill(color.rgba())

def fill(color="default_background_color"):
    color = Color.from_user_input(color)

    fill_screen(color)

def rectangle(x, y, width, height, color="default_color"):
    color = Color.from_user_input(color)

    pygame.draw.rect(display, color.rgba(), (int(x), int(y), int(width), int(height)))

def circle(x, y, radius, color="default_color"):
    color = Color.from_user_input(color)

    pygame.draw.circle(display, color.rgba(), (int(x), int(y)), int(radius))

def ellipse(x, y, width, height, color="default_color"):
    color = Color.from_user_input(color)
    rect_x = int(x - width/2)
    rect_y = int(y - height/2)
    pygame.draw.ellipse(display, color.rgba(), (rect_x, rect_y, int(width), int(height)))

def arc(x, y, width, height, start_angle, stop_angle, color="default_color"):
    color = Color.from_user_input(color)
    rect_x = int(x - width/2)
    rect_y = int(y - height/2)
    pygame.draw.arc(display, color.rgba(), (rect_x, rect_y, int(width), int(height)), start_angle, stop_angle)