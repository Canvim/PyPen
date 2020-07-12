import argparse

def cli():
    argument_parser = argparse.ArgumentParser(description="The Pyper CLI for managing Pyper Sketches", prog="pyperlib")

    argument_parser.add_argument("-f", "--foo", action="test", help="Placeholder Argument", test=f"Pyper!")

    args = argument_parser.parse_args()
    main(args)

def main(args):
    pass

if __name__ == "__main__":
    cli()