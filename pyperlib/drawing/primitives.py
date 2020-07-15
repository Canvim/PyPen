from pyperlib.drawing.color import colors
from pyglet import shapes

import pyglet
from pyglet.gl import *

_shapes = []
_main_batch = pyglet.graphics.Batch()

def clear_screen():
    fill_screen(colors.default_background_color)
    pass


def clear():
    clear_screen()


def fill_screen(color=colors.default_background_color):
    rectangle(0, 0, 10000, 10000, color)
    pass

def fill(color=colors.default_background_color):
    fill_screen(color=color)

def rectangle(x, y, width, height, color=colors.default_color):
    rectangle_shape = shapes.Rectangle(x, y, width, height, color=color.rgb255(), batch=_main_batch)
    
    _shapes.append(rectangle_shape)

def draw_batch():
    _main_batch.draw()
    _shapes = []