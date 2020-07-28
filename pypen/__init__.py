import sys
import re
import os
from pypen.settings import settings


def _check_if_executed_with_python():
    if not sys.argv:
        return

    if sys.argv[0] == "-m":
        return

    match = re.search("pypen", sys.argv[0])
    if match:
        return

    print()
    print("It seems like you are trying to run a PyPen sketch using the python command.")
    print("Try instead running it with 'pypen {}'!".format(" ".join(sys.argv)))
    print()
    print("Run 'pypen --help' for more information.")
    print()
    settings._is_executing_with_python = True


_check_if_executed_with_python()


from pypen.utils import *
from pypen.drawing import *
from pypen.drawing import _COLORS


class _Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

TIME = T = DELTA_TIME = DT = FRAME = F = FPS = 0
WIDTH = settings.width
HEIGHT = settings.height

MOUSE = _Mouse(0, 0)

def grid(spacing=1, start_x=0, start_y=0):
    spacing = max(1, abs(spacing))

    x = start_x
    y = start_y
    while y < settings.height:
        yield x, y

        x = (x + spacing)

        if x >= settings.width:
            x = start_x
            y += spacing


def pixels():
    return grid(1, 0, 0)
