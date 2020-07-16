import sys
import re
import os
from pyperlib.settings import settings

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

def _check_if_executed_with_python():
    if not sys.argv:
        return

    if sys.argv[0] == "-m":
        return

    match = re.search("pyper", sys.argv[0])
    if match:
        return

    print()
    print("It seems like you are trying to run a Pyper sketch using the python command.")
    print("Try instead running it with 'pyper {}'!".format(" ".join(sys.argv)))
    print()
    print("Run 'pyper --help' for more information.")
    print()
    settings._is_executing_with_python = True

_check_if_executed_with_python()

from pyperlib.drawing import *
from pyperlib.utils import *

TIME = T = DELTA_TIME = DT = FRAME = F = 0
