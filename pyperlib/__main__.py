import sys
import argparse
import time
from os import path, getcwd
from importlib import util as import_util

import pyglet

from pyperlib.settings import settings
from pyperlib.drawing.window import PyperWindow
from pyperlib.drawing.primitives import draw_batch

def cli():
    try:
        argument_parser = argparse.ArgumentParser(
            description="The Pyper CLI for managing Pyper Sketches", prog="pyper")

        argument_parser.add_argument(
            "filename", help="The name/path to the file that contains your Pyper Sketch.")

        argument_parser.add_argument("-f", "--fullscreen", action="store_true")

        argument_parser.add_argument(
            "--timeout", help="Timeout in seconds. Window will close once done.", type=float, required=False, default=0.0)

        arguments = argument_parser.parse_args()

        if len(sys.argv) == 1:
            argument_parser.print_help(sys.stderr)
            sys.exit(0)

        run_pyper_window(arguments)
    except argparse.ArgumentError as error:
        print(str(error))
        sys.exit(2)

def run_pyper_window(arguments):
    file_path = path.join(getcwd(), arguments.filename)
    spec = import_util.spec_from_file_location("", file_path)
    user_sketch = import_util.module_from_spec(spec)
    spec.loader.exec_module(user_sketch)

    pyper_window = PyperWindow(
        resizable=True,
        fullscreen=arguments.fullscreen
    )

    @pyper_window.event
    def on_draw():
        draw_batch()

    def start(delta_time):
        user_sketch.start()
        update(delta_time)

    def update(delta_time):
        user_sketch.update()
        

    pyglet.clock.schedule_interval_soft(update, 1/settings.fps)
    pyglet.clock.schedule_once(start, 0)

    if arguments.timeout > 0:
        pyglet.clock.schedule_once(pyper_window.exit_callback, arguments.timeout)
        pyglet.app.run()
    else:
        pyglet.app.run()


if __name__ == "__main__":
    cli()
