import argparse
from pyperlib import __version__

def cli():
    argument_parser = argparse.ArgumentParser(description="The Pyper CLI for managing Pyper Sketches", prog="pyperlib")

    argument_parser.add_argument("-v", "--version", action="version", help="Displays the currently installed version of Pyper", version=f"%(prog)s {__version__}")

    args = argument_parser.parse_args()
    main(args)

def main(args):
    pass

if __name__ == "__main__":
    cli()