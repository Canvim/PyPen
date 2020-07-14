import sys
import re

from pyperlib.settings import settings
from pyperlib.drawing import *

if len(sys.argv) > 0:
    match = re.search("pyper", sys.argv[0])
    if not match:
        print()
        print("It seems like you are trying to run a Pyper sketch using the python command.")
        print("Try instead running it with 'pyper {}'!".format(" ".join(sys.argv)))
        print()
        print("Run 'pyper --help' for more information.")
        print()
        sys.exit(0)
