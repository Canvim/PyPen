import sys
import argparse
from os import path, getcwd
from importlib import util as import_util

import time
import pyglet
import moderngl

class PyperWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(200, 200)
    
    def exit_callback(self, dt):
        self.close()

def cli():
    try:
        argument_parser = argparse.ArgumentParser(description="The Pyper CLI for managing Pyper Sketches", prog="pyper")

        argument_parser.add_argument("filename", help="The name/path to the file that contains your Pyper Sketch.")

        argument_parser.add_argument("-f", "--fullscreen", action="store_true")

        argument_parser.add_argument("--timeout", help="Timeout in seconds. Window will close once done.", type=float, required=False, default=0.0)

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

    window = PyperWindow(
        resizable=True,
        fullscreen=arguments.fullscreen
    )
    context = moderngl.create_context(require=300)

    @window.event
    def on_draw():
        user_sketch.update()
        context.clear(0.0, 1.0, 0.0, 0.0)

    if arguments.timeout > 0:
        pyglet.clock.schedule_once(window.exit_callback, arguments.timeout)
        pyglet.app.run()
    else:
        pyglet.app.run()
    

        

if __name__ == "__main__":
    cli()