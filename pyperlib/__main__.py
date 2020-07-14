import sys
import argparse

from pyperlib.drawing.window import run_pyper_window

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


if __name__ == "__main__":
    cli()
