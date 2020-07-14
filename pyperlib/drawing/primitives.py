from pyperlib.drawing.window import context
from pyperlib.drawing.color import colors

def clear_screen():
    context.clear(colors.default_background_color.rgba())

def rectangle(color=colors.default_color):
    context.clear(color=color.rgba())
    print("I am a pyper rectangle!")
