import sys
import argparse
from os import path, getcwd
from importlib import util as import_util

import moderngl_window

class PyperWindow(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (500, 400)
    title = "Pyper"  
    resizable = True
    samples = 8
    log_level = 0

    def render(self, time, frametime):
        self.ctx.clear(0.0, 1.0, 0.0, 1.0)


def our_parse_args(args=None, parser=None):
    """Parse arguments from sys.argv

    Passing in your own argparser can be user to extend the parser.

    Keyword Args:
        args: override for sys.argv
        parser: Supply your own argparser instance
    """
    parser = parser or create_parser()
    return parser.parse_args(args)

def cli():
    try:
        argument_parser = argparse.ArgumentParser(description="The Pyper CLI for managing Pyper Sketches", prog="pyper")

        argument_parser.add_argument("-f", "--fullscreen", action="store_true")

        argument_parser.add_argument("filename", help="The name/path to the file that contains your Pyper Sketch.")

        arguments = argument_parser.parse_args()

        if len(sys.argv)==1:
            argument_parser.print_help(sys.stderr)
            sys.exit(0)

        main(arguments)
    except argparse.ArgumentError as error:
        print(str(error))
        sys.exit(2)

def main(arguments):
    file_path = path.join(getcwd(), arguments.filename)
    spec = import_util.spec_from_file_location("", file_path)
    user_sketch = import_util.module_from_spec(spec)
    spec.loader.exec_module(user_sketch)

    moderngl_window.parse_args = our_parse_args
    moderngl_window.run_window_config(PyperWindow, args = [])
    pass

if __name__ == "__main__":
    cli()