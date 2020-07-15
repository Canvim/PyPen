from pyperlib.drawing.window import context
from pyperlib.drawing.color import colors
from pyglet import shapes

def clear_screen():
    context.clear(color=colors.default_background_color.rgba())


def clear():
    clear_screen()


def fill_screen(color=colors.default_background_color):
    context.clear(color=color.rgba())


def fill(color=colors.default_background_color):
    fill_screen(color=color)


def rectangle(x, y, width, height, color=colors.default_color):
    rectangle_shape = shapes.Rectangle(x, y, width, height, color=color.rgb255())
    rectangle_shape.draw()

