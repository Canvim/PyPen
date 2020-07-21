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

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pypen.utils import *
from pypen.drawing import *

TIME = T = DELTA_TIME = DT = FRAME = F = 0
WIDTH = settings.width
HEIGHT = settings.height


def grid(spacing=1, start_x=0, start_y=0):
    global HEIGHT, WIDTH
    spacing = max(1, abs(spacing))

    x = start_x
    y = start_y
    while y < HEIGHT:
        yield x, y

        x = (x + spacing)

        if x >= WIDTH:
            x = start_x
            y += spacing


def pixels():
    return grid(1, 0, 0)