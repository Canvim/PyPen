import sys
import argparse
import time
from os import path, getcwd

from importlib import util as import_util

from pypen.settings import settings
import pygame

_argument_parser = argparse.ArgumentParser()

def space_print(msg=""):
    print()
    print(msg)
    print()

def print_help(msg=""):
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

        arguments = _argument_parser.parse_args()

        if len(sys.argv) == 1:
            print_help("It seems like you are running the pypen command without any arguments.\nHere is some help:")

        if not arguments.init and not arguments.filename:
            print_help("PyPen needs a path to a sketch in order to run it!\nPlease provide a path with 'pypen <path_to_sketch>'\nor run 'pypen --init <path_to_new_sketch>' to create a new one!")

        if arguments.init:
            path_to_new_sketch = arguments.filename if arguments.filename else settings.default_pypen_name
            init(path_to_new_sketch)

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
    clear()
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
        user_sketch.rectangle
        user_sketch.PI
    except AttributeError:
        print()
        print(f"It seems like you're not importing PyPen to your sketch '{arguments.filename}'")
        print("Import it by writing 'from pypen import *' at the very top!")
        print()
        sys.exit(1)

    try:
        user_sketch.start
    except AttributeError:
        settings._user_has_start = False

    try:
        user_sketch.update
    except AttributeError:
        settings._user_has_update = False

    if not settings._user_has_start and not settings._user_has_update:
        print()
        print(
            f"Your PyPen sketch '{arguments.filename}' appears to have neither a start() nor an update() function.")
        print("Try to add at least one of those and run again!")
        print()
        sys.exit(1)

    def start():
        user_sketch.start()
        update()

    def update(passed_time=0, delta_time=0, frame_count=0):
        user_sketch.TIME = user_sketch.T = passed_time
        user_sketch.DELTA_TIME = user_sketch.DT = delta_time
        user_sketch.FRAME = user_sketch.F = frame_count

        user_sketch.update()

    pygame.display.set_mode((settings.width, settings.height), pygame.SRCALPHA)

    pygame.init()
    pygame.display.set_caption(f"PyPen | {arguments.filename}")

    if settings._user_has_start:
        start()

    pygame.display.set_mode((settings.width, settings.height), pygame.SRCALPHA)
    pygame.display.flip()
    clock = pygame.time.Clock()

    is_running = True
    passed_time = frame_count = 0

    while is_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

        delta_time = clock.tick(settings.fps if settings.fps > 0 else 1)/1000
        passed_time += delta_time
        frame_count += 1

        if arguments.timeout > 0:
            if passed_time > arguments.timeout:
                is_running = False

        if settings._user_has_update:
            update(passed_time, delta_time, frame_count)

        pygame.display.flip()


if __name__ == "__main__":
    cli()
