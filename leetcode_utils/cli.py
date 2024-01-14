import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("path", help="name or path for a new problem directory")
    args = parser.parse_args()

    if args.command == "init":
        os.makedirs(args.path)
        with open(f"{args.path}/solution1.py", "w") as f:
            pass

        sanitized_name = (
            os.path.basename(args.path)
            .split(" ", maxsplit=1)[1]
            .lower()
            .translate(str.maketrans(" -", "__"))
        )
        with open(f"{args.path}/test_{sanitized_name}.py", "w") as f:
            pass
    else:
        print("Unknown command")
