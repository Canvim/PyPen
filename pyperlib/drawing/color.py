import colorsys
import re

from pyperlib.utils.math import clamp
from pygame.colordict import THECOLORS as _PYGAME_COLORS

_COLORS = {
    "default_background_color": (0),
    "default_color": (30, 60, 125),

    "red": (200, 30, 30),
    "green": (30, 200, 30),
    "blue": (30, 30, 200)
}

_PYGAME_COLORS.update(_COLORS)
_COLORS = _PYGAME_COLORS

_COLORS_CACHE = {}


class Color:
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = int(clamp(r, 0, 255))
        self.g = int(clamp(g, 0, 255))
        self.b = int(clamp(b, 0, 255))
        self.a = int(clamp(a, 0, 255))

    def rgb(self):
        return self.r, self.g, self.b

    def rgba(self):
        return self.r, self.g, self.b, self.a

    @classmethod
    def from_user_input(cls, user_input):
        if type(user_input) is Color:
            return user_input

        if type(user_input) is int or type(user_input) is float:
            r = g = b = user_input
            return cls(r, g, b)

        if type(user_input) is tuple:
            if len(user_input) == 1:
                r = g = b = user_input[0]
                return cls(r, g, b)

            if len(user_input) == 3:
                r, g, b = user_input
                return cls(r, g, b)

            if len(user_input) == 4:
                r, g, b, a = user_input
                return cls(r, g, b, a)

        if type(user_input) is str:
            if user_input in _COLORS_CACHE:
                return _COLORS_CACHE[user_input]

            if user_input in _COLORS.keys():
                color = Color.from_user_input(_COLORS[user_input])
                _COLORS_CACHE[user_input] = color
                return color

            hex_match = re.match(r"\#(.*)", user_input)

            if hex_match:
                hex_match_group = hex_match.group(1)
                hex_digits = re.findall(r".{1,2}", hex_match_group)
                new_user_input = tuple([int(h, 16) for h in hex_digits])
                color = Color.from_user_input(new_user_input)
                _COLORS_CACHE[user_input] = color
                return color

            rgb_rgba_match = re.match(r"(rgb|rgba)\((.*)\)", user_input)

            if rgb_rgba_match:
                rgb_rgba_match_group = rgb_rgba_match.group(2)
                new_user_input = tuple([int(d) for d in rgb_rgba_match_group.split(",")])
                color = Color.from_user_input(new_user_input)
                _COLORS_CACHE[user_input] = color
                return color

        return cls()
