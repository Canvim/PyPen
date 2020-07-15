import sys
import argparse
import time
from os import path, getcwd
from importlib import util as import_util

from pyperlib.settings import settings

import pygame

display = pygame.display.set_mode((settings.width, settings.height))

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

        main(arguments)
    except argparse.ArgumentError as error:
        print(str(error))
        sys.exit(2)

def main(arguments):
    file_path = path.join(getcwd(), arguments.filename)
    spec = import_util.spec_from_file_location("", file_path)
    user_sketch = import_util.module_from_spec(spec)
    spec.loader.exec_module(user_sketch)

    def start():
        user_sketch.start()
        update()

    def update():
        user_sketch.update()

    pygame.init()
    pygame.display.set_caption(f"Pyper | {arguments.filename}")
    
    start()
    
    pygame.display.flip()
    clock = pygame.time.Clock()

    is_running = True
    passed_time = 0

    while is_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
        delta_time = clock.tick(settings.fps)
        passed_time += delta_time
        
        if arguments.timeout > 0:
            if passed_time/1000 > arguments.timeout:
                is_running = False
    
        # Handle drawing...
        update()

        pygame.display.flip()

        


if __name__ == "__main__":
    cli()
