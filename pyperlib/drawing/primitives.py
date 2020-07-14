from pyperlib.drawing.window import context
from pyperlib.drawing.color import colors


def clear_screen():
    context.clear(colors.default_background_color.rgba())


def clear():
    clear_screen()


def fill_screen(color=colors.default_background_color):
    context.clear(color=color.rgba())


def fill(color=colors.default_background_color):
    fill_screen(color=color)


def rectangle(color=colors.default_color):
    context.clear(color=color.rgba())
    print("I am a pyper rectangle!")
