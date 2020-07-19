from pypen.drawing.color import Color

import pygame


def clear_screen():
    color = Color.from_user_input("default_background_color")
    display = pygame.display.get_surface()

    display.fill(color.rgb())


def clear():
    clear_screen()


def fill_screen(color="default_background_color"):
    color = Color.from_user_input(color)
    display = pygame.display.get_surface()

    display.fill(color.rgb())


def fill(color="default_background_color"):
    fill_screen(color)


def rectangle(x, y, width, height, color="default_color"):
    color = Color.from_user_input(color)
    display = pygame.display.get_surface()

    pygame.draw.rect(display, color.rgba(), (int(x), int(y), int(width), int(height)))


def circle(x, y, radius, color="default_color"):
    color = Color.from_user_input(color)
    display = pygame.display.get_surface()

    pygame.draw.circle(display, color.rgba(), (int(x), int(y)), int(radius))


def ellipse(x, y, width, height, color="default_color"):
    color = Color.from_user_input(color)
    display = pygame.display.get_surface()

    rect_x = int(x - width/2)
    rect_y = int(y - height/2)
    pygame.draw.ellipse(display, color.rgba(), (rect_x, rect_y, int(width), int(height)))


def arc(x, y, width, height, start_angle, stop_angle, color="default_color"):
    color = Color.from_user_input(color)
    display = pygame.display.get_surface()

    rect_x = int(x - width/2)
    rect_y = int(y - height/2)
    pygame.draw.arc(display, color.rgba(), (rect_x, rect_y, int(
        width), int(height)), start_angle, stop_angle)
