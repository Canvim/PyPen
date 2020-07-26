import sys
import argparse
import time
from os import path, getcwd
from importlib import util as import_util
import pkg_resources
import tkinter

from pypen.settings import settings
from pypen.drawing.primitives import PrimitivesDrawer
import cairo
from PIL import Image, ImageTk

_argument_parser = argparse.ArgumentParser()

def space_print(msg=""):
    print()
    print(msg)
    print()

def print_help(msg=""):
    global _argument_parser
    if msg:
        space_print(msg)

    _argument_parser.print_help(sys.stderr)
    sys.exit(0)

def cli():
    global _argument_parser
    try:
        _argument_parser = argparse.ArgumentParser(description="The PyPen CLI for managing PyPen Sketches", prog="pypen")
        _argument_parser.add_argument(
            "-i",
            "--init",
            action="store_true",
            help="Flag to create a new PyPen sketch which imports pypen and contains default functions.")

        _argument_parser.add_argument("filename", nargs="?", help="The name/path of your PyPen Sketch.", default="")
        _argument_parser.add_argument("-f", "--fullscreen", action="store_true")
        _argument_parser.add_argument("--timeout", help="Timeout in seconds. Window will close once done.", type=float, required=False, default=0.0)
        _argument_parser.add_argument("-v", "--version",
                                      help="Displays the currently installed PyPen's version.",
                                      action="version",
                                      version=pkg_resources.get_distribution("pypen").version)

        arguments = _argument_parser.parse_args()

        if len(sys.argv) == 1:
            print_help("It seems like you are running the pypen command without any arguments.\nHere is some help:")

        if not arguments.init and not arguments.filename:
            print_help("PyPen needs a path to a sketch in order to run it!\nPlease provide a path with 'pypen <path_to_sketch>'\nor run 'pypen --init <path_to_new_sketch>' to create a new one!")

        if arguments.init:
            path_to_new_sketch = arguments.filename if arguments.filename else settings.default_pypen_name
            init(path_to_new_sketch)

        if path.splitext(arguments.filename)[1] != ".py":
            arguments.filename = "{}.py".format(arguments.filename)

        main(arguments)
    except argparse.ArgumentError as error:
        print(str(error))
        sys.exit(1)


def init(path_to_new_file):
    if path.splitext(path_to_new_file)[1] != ".py":
        path_to_new_file += ".py"

    pypen_path = path.join(getcwd(), path_to_new_file)
    template = ""

    try:
        with open(path.join(path.realpath(__file__), "..", "pypen_template.py"), "r") as template_file:
            template = template_file.read()
    except EnvironmentError:
        # In case PyPen is installed in a directory that doesn't have read access,
        # it uses the below template instead of reading the template file
        template = """from pypen import *


def start():
    settings.fps = 60


def update():
    fill_screen("orange")
    rectangle(20, 20, 300, 400, "red")
"""

    try:
        with open(pypen_path, "w") as new_file:
            new_file.writelines(template)
    except EnvironmentError:
        space_print("Could not create file {}\nDo you have the right permissions?".format(pypen_path))
        sys.exit(1)

    space_print("'{0}' has been created!\nRun it using 'pypen {0}'".format(path_to_new_file))
    sys.exit(0)



class PyPenWindow(tkinter.Tk):
    def __init__(self, user_sketch=None, window_title="Example", arguments={}, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_sketch = user_sketch
        self.window_title = window_title
        self.arguments = arguments
        self.called_after_time = self.passed_time = self.delta_time = self.frame_count = 0

        self.geometry("{}x{}".format(self.user_sketch.settings.width, self.user_sketch.settings.height))

        self._surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.user_sketch.settings.width, self.user_sketch.settings.height)
        self._context = cairo.Context(self._surface)

        self.primitives_drawer = PrimitivesDrawer(self._surface, self._context, self.user_sketch.settings)

        self.fix_primitive_functions()
        self.call_user_start()

        self._image = Image.frombuffer("RGBA", (self.user_sketch.settings.width, self.user_sketch.settings.height), self.primitives_drawer.surface.get_data().tobytes(), "raw", "BGRA", 0, 1)
        self.photo = ImageTk.PhotoImage(self._image)

        self.label = tkinter.Label(self, image=self.photo)
        self.label.pack(expand=True, fill="both")

        if self.arguments.timeout:
            self.after(int(self.arguments.timeout), self.destroy)

        self.start_time = time.time()
        self.call_pypen_loop()
        self.mainloop()


    def fix_primitive_functions(self):
        self.user_sketch.fill_screen = self.primitives_drawer.fill_screen
        self.user_sketch.clear = self.primitives_drawer.clear
        self.user_sketch.clear_screen = self.primitives_drawer.clear_screen

        self.user_sketch.rectangle = self.primitives_drawer.rectangle
        self.user_sketch.circle = self.primitives_drawer.circle
        self.user_sketch.arc = self.primitives_drawer.arc


    def call_user_start(self):
        if not self.user_sketch.settings._user_has_start:
            return
        self.user_sketch.start()

    def call_user_update(self):
        if not self.user_sketch.settings._user_has_update:
            return
        self.user_sketch.TIME = self.user_sketch.T = self.passed_time
        self.user_sketch.FRAME = self.user_sketch.F = self.frame_count

        self.user_sketch.update()
        self.user_sketch.DELTA_TIME = self.user_sketch.DT = time.time() - self.called_after_time


    def pypen_loop(self):
        self.call_user_update()

        self.primitives_drawer.update_settings(self.user_sketch.settings)
        self._image = Image.frombuffer("RGBA", (self.user_sketch.settings.width, self.user_sketch.settings.height), self.primitives_drawer.surface.get_data().tobytes(), "raw", "BGRA", 0, 1)
        self.photo = ImageTk.PhotoImage(self._image)
        self.label.configure(image=self.photo)

    def call_pypen_loop(self):
        self.pypen_loop()

        self.delta_time = 0.01
        self.passed_time = time.time() - self.start_time
        self.frame_count += 1

        self.called_after_time = time.time()
        self.after(int(1000/self.user_sketch.settings.fps), self.call_pypen_loop)


def main(arguments):
    if not arguments.init:
        try:
            file_path = path.join(getcwd(), arguments.filename)
            spec = import_util.spec_from_file_location("", file_path)
            user_sketch = import_util.module_from_spec(spec)
            spec.loader.exec_module(user_sketch)
        except FileNotFoundError:
            print()
            print(f"Hmm, PyPen can't find '{arguments.filename}'.")
            print("Are you sure that's the right path?")
            print()
            sys.exit(1)

    try:
        user_sketch.TIME
        user_sketch.T
        user_sketch.PI
    except AttributeError as error:
        print()
        print(f"It seems like you're not importing PyPen to your sketch '{arguments.filename}'")
        print("Import it by writing 'from pypen import *' at the very top!")
        print()

        print(error)
        sys.exit(1)

    try:
        user_sketch.start
    except AttributeError:
        user_sketch.settings._user_has_start = False

    try:
        user_sketch.update
    except AttributeError:
        user_sketch.settings._user_has_update = False

    if not user_sketch.settings._user_has_start and not user_sketch.settings._user_has_update:
        print()
        print(f"Your PyPen sketch '{arguments.filename}' appears to have neither a start() nor an update() function.")
        print("Try to add at least one of those and run again!")
        print()
        sys.exit(1)

    window_title = f"PyPen | {path.splitext(path.split(arguments.filename)[1])[0]}"
    pypen_window = PyPenWindow(user_sketch, window_title, arguments)


if __name__ == "__main__":
    cli()
