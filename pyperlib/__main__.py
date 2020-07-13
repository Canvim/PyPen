import sys
import argparse

def cli():
    try:
        argument_parser = argparse.ArgumentParser(description="The Pyper CLI for managing Pyper Sketches", prog="pyper")

        argument_parser.add_argument("-f", "--fullscreen", type=bool, default=False, action="store_true")

        arguments = argument_parser.parse_args()

        if len(sys.argv)==1:
            argument_parser.print_help(sys.stderr)
            sys.exit(1)

        main(arguments)
    except argparse.ArgumentError as error:
        print(str(error))
        sys.exit(2)

def main(arguments):
    pass

if __name__ == "__main__":
    cli()